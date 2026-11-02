"""Fetch a source into the research trail as readable text, with retries and fallbacks to other copies.

Usage (from the project root):
  fetch.py get  --base TASK --id S101 --slug short-name --task T05 --part 1 URL_OR_ID [URL_OR_ID ...] [--append]
  fetch.py meta --base TASK --id S101 --slug short-name --task T05 --part 1 DOI_OR_ARXIV   (metadata record only)
  fetch.py find "title words"            list matching works (DOI, year, venue, citations, open-access URL)
  fetch.py convert FILE                  convert a local file (PDF, HTML, JSON, text) and print text + readability
  fetch.py probe URL_OR_ID               show the candidate ladder and each verdict without writing anything
  fetch.py local --base TASK --id S901 --slug name --task T04 --part 3 --repo DIR [--rev COMMIT] [--url-prefix URL]
                 PATH [PATH ...]         verbatim copy of files from a local git repository at one revision

URL_OR_ID is a URL, a DOI (10.xxxx/… or doi:…) or an arXiv ID (arXiv:2406.03684). `get` walks a ladder of
candidates until one converts to readable text:
  L1  the requested URL, retried on 429/5xx/network errors with backoff, and on 403 with a second user agent;
  L2  other representations of the same work: arXiv HTML → PDF → abstract page; for a DOI, the publisher page,
      then every open-access copy that OpenAlex and Semantic Scholar list (repositories, arXiv, author PDFs);
  L3  the Wayback Machine snapshot of each URL (raw "id_" copy);
  L4  a metadata-only record from Crossref and OpenAlex (title, authors, venue, year, pages, DOI, citations),
      saved with status partial so bibliographic facts stay citable while the full text is missing.
Each download is converted to text (HTML: structure-preserving text with citation_* metadata on top; PDF: macOS
PDFKit, then a standard-library extractor; JSON: bibliographic fields) and scored for readability (word count,
letter ratio, broken-encoding and blocking signatures). The first readable candidate wins; otherwise the best
partial one. The source folder receives raw.<ext>, crawl.md (header + converted text, verbatim, unedited
afterwards) and attempts.md (every attempt with its HTTP code, converter and verdict).
Exit codes: 0 readable (status ok), 3 partial or metadata only, 4 nothing usable (status blocked/error): search for
another source that covers the same facts (L5, see reference.md) and record it in search-log.md.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import zlib
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

from common import ROOT, base_dir, load_register, source_folder

HERE = Path(__file__).resolve().parent
CACHE = ROOT / "build" / ".cache" / "fetch" / f"run-{os.getpid()}"   # one folder per run: parallel agents never share a file
AGENTS = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
          "Version/17.0 Safari/605.1.15",
          "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"]
RETRY_CODES = {0, 429, 500, 502, 503, 504, 520, 522, 524}
BLOCK_SIGNS = ["access denied", "captcha", "just a moment", "enable javascript", "request unsuccessful",
               "are you a robot", "cookies must be enabled", "403 forbidden", "bot verification",
               "unusual traffic", "checking your browser", "cloudflare ray id"]
LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "ft", "ﬆ": "st"}
STOP = set("the of and to in a is that for on with as are by this be from or an at which it we can not was "
           "their these has have its were been also more than other such between".split())
STOP_VI = set("và của là các có được trong cho những với không một này để từ theo khi người đã như".split())


# ----------------------------------------------------------------------------- download
def curl(url: str, out: Path, agent: str, timeout: int = 60) -> dict:
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["curl", "-sSL", "--compressed", "-m", str(timeout), "-A", agent, "-o", str(out),
           "-H", "Accept: text/html,application/xhtml+xml,application/pdf,application/json;q=0.9,*/*;q=0.8",
           "-H", "Accept-Language: en,vi;q=0.8", "-w", "%{http_code}\t%{content_type}\t%{url_effective}", url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    code, ctype, final = (r.stdout.split("\t") + ["", "", ""])[:3]
    return dict(code=int(code) if code.isdigit() else 0, type=ctype.lower(), final=final or url,
                error=r.stderr.strip()[:120], size=out.stat().st_size if out.exists() else 0)


def download(url: str, out: Path, tries: int = 3, log=None) -> dict:
    """curl with retries: backoff on 429/5xx/network errors, a second user agent on 403."""
    delay, agent_i, res = 2, 0, {}
    for attempt in range(1, tries + 1):
        res = curl(url, out, AGENTS[agent_i])
        res["attempt"] = attempt
        if log is not None and attempt > 1:
            log.append((url, f"retry {attempt}", res))
        if 200 <= res["code"] < 300 and res["size"] > 0:
            return res
        if res["code"] == 403 and agent_i + 1 < len(AGENTS):
            agent_i += 1
            continue
        if res["code"] not in RETRY_CODES:
            return res
        time.sleep(delay)
        delay *= 2.5
    return res


# ----------------------------------------------------------------------------- converters
class _Text(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "form", "button", "iframe", "template", "select"}
    BLOCK = {"p", "div", "section", "article", "br", "tr", "table", "ul", "ol", "dl", "dt", "dd", "figure",
             "figcaption", "blockquote", "pre", "main", "aside", "caption", "hr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.meta, self.title, self.in_title = [], 0, [], "", False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP:
            self.skip += 1
        elif tag == "meta" and (a.get("name") or "").startswith(("citation_", "dc.", "DC.")) and a.get("content"):
            self.meta.append(f"{a['name']}: {a['content']}")
        elif tag == "title":
            self.in_title = True
        elif re.fullmatch(r"h[1-6]", tag):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag in ("td", "th"):
            self.out.append(" | ")
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        elif tag == "title":
            self.in_title = False
        elif re.fullmatch(r"h[1-6]", tag) or tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif not self.skip:
            self.out.append(data)


def html_to_text(raw: bytes) -> str:
    text = raw.decode("utf-8", errors="replace")
    p = _Text()
    p.feed(text)
    body = re.sub(r"[ \t\r\f\v]+", " ", "".join(p.out))
    body = re.sub(r" *\n *", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    head = [f"title: {html.unescape(p.title.strip())}"] if p.title.strip() else []
    head += sorted(set(p.meta))[:60]
    return ("\n".join(head) + "\n\n" if head else "") + body


def tidy_pdf_text(text: str) -> str:
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    text = re.sub(r"(\w)-\n(?=[a-z])", r"\1", text)             # re-join words hyphenated at line ends
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def pdf_pdfkit(path: Path) -> str:
    if sys.platform != "darwin":
        return ""
    src = path if path.suffix == ".pdf" else path.with_suffix(".pdf")
    if src != path:
        src.write_bytes(path.read_bytes())
    r = subprocess.run(["osascript", "-l", "JavaScript", str(HERE / "pdf" / "pdfkit_text.js"), str(src)],
                       capture_output=True, text=True, timeout=300)
    return "" if r.stdout.startswith("ERROR") else tidy_pdf_text(r.stdout)


def _pdf_string(s: bytes) -> str:
    out, i = bytearray(), 0
    esc = {b"n": b"\n", b"r": b"\r", b"t": b"\t", b"b": b"\b", b"f": b"\f", b"(": b"(", b")": b")", b"\\": b"\\"}
    while i < len(s):
        c = s[i:i + 1]
        if c == b"\\" and i + 1 < len(s):
            nxt = s[i + 1:i + 2]
            if nxt in esc:
                out += esc[nxt]
                i += 2
                continue
            m = re.match(rb"[0-7]{1,3}", s[i + 1:i + 4])
            if m:
                out.append(int(m.group(0), 8) & 0xFF)
                i += 1 + len(m.group(0))
                continue
            i += 1
            continue
        out += c
        i += 1
    return out.decode("latin-1")


def pdf_stdlib(path: Path) -> str:
    """Minimal text extraction: Flate-decoded content streams, Tj/TJ string operators (no CID fonts)."""
    data = path.read_bytes()
    pages = []
    for m in re.finditer(rb"<<(.{0,400}?)>>\s*stream\r?\n(.*?)\r?\nendstream", data, re.S):
        if b"FlateDecode" not in m.group(1):
            continue
        try:
            content = zlib.decompress(m.group(2))
        except zlib.error:
            continue
        if b"BT" not in content:
            continue
        lines, cur = [], []
        for tok in re.finditer(rb"\((?:\\.|[^\\)])*\)\s*(?:Tj|'|\")|\[(?:[^\]\\]|\\.)*\]\s*TJ|T\*|-?[\d.]+ -?[\d.]+ T[dD]|ET",
                               content, re.S):
            t = tok.group(0)
            if t.endswith((b"Tj", b"'", b'"')):
                cur.append(_pdf_string(re.match(rb"\((.*)\)", t, re.S).group(1)))
            elif t.endswith(b"TJ"):
                parts = re.findall(rb"\((?:\\.|[^\\)])*\)|-?\d+\.?\d*", t[1:t.rfind(b"]")])
                for part in parts:
                    if part.startswith(b"("):
                        cur.append(_pdf_string(part[1:-1]))
                    elif float(part) < -200:
                        cur.append(" ")
            else:
                if cur:
                    lines.append("".join(cur))
                cur = []
        if cur:
            lines.append("".join(cur))
        if lines:
            pages.append("\n".join(lines))
    return tidy_pdf_text("\n\n".join(f"<!-- stream {i + 1} -->\n{p}" for i, p in enumerate(pages)))


def json_to_text(raw: bytes) -> str:
    """Bibliographic record from a Crossref, OpenAlex or Semantic Scholar JSON response."""
    try:
        d = json.loads(raw)
    except ValueError:
        return ""
    d = d.get("message", d)
    lines = []
    if "DOI" in d and "title" in d:                                                     # Crossref
        title = (d.get("title") or [""])[0]
        authors = "; ".join(f"{a.get('family', '')}, {a.get('given', '')}".strip(", ") for a in d.get("author", []))
        date = (d.get("issued", {}).get("date-parts") or [[None]])[0]
        lines += [f"source: Crossref", f"title: {title}", f"authors: {authors}",
                  f"container: {(d.get('container-title') or [''])[0]}", f"published: {'-'.join(map(str, filter(None, date)))}",
                  f"volume: {d.get('volume', '')}", f"issue: {d.get('issue', '')}", f"pages: {d.get('page', '')}",
                  f"article number: {d.get('article-number', '')}", f"publisher: {d.get('publisher', '')}",
                  f"doi: {d['DOI']}", f"type: {d.get('type', '')}",
                  f"is-referenced-by-count (Crossref citations): {d.get('is-referenced-by-count', '')}"]
        if d.get("abstract"):
            lines += ["", "abstract:", re.sub(r"<[^>]+>", " ", d["abstract"]).strip()]
    elif "openalex" in str(d.get("id", "")) or "cited_by_count" in d:                  # OpenAlex
        loc = d.get("primary_location") or {}
        src = (loc.get("source") or {}).get("display_name", "")
        authors = "; ".join(a["author"]["display_name"] for a in d.get("authorships", []))
        insts = sorted({i["display_name"] for a in d.get("authorships", []) for i in a.get("institutions", [])})
        b = d.get("biblio") or {}
        lines += ["source: OpenAlex", f"title: {d.get('display_name', '')}", f"authors: {authors}",
                  f"institutions: {'; '.join(insts)}", f"venue: {src}", f"publication date: {d.get('publication_date', '')}",
                  f"volume: {b.get('volume', '')}", f"issue: {b.get('issue', '')}",
                  f"pages: {b.get('first_page', '')}–{b.get('last_page', '')}", f"doi: {d.get('doi', '')}",
                  f"cited_by_count (OpenAlex): {d.get('cited_by_count', '')}", f"type: {d.get('type', '')}"]
        for loc in d.get("locations", []):
            if loc.get("pdf_url") or loc.get("landing_page_url"):
                lines.append(f"location: {loc.get('pdf_url') or loc.get('landing_page_url')} "
                             f"(open access: {loc.get('is_oa')})")
        inv = d.get("abstract_inverted_index")
        if inv:
            words = sorted((pos, w) for w, ps in inv.items() for pos in ps)
            lines += ["", "abstract:", " ".join(w for _, w in words)]
    elif "paperId" in d:                                                                # Semantic Scholar
        lines += ["source: Semantic Scholar", f"title: {d.get('title', '')}",
                  f"authors: {'; '.join(a.get('name', '') for a in d.get('authors', []))}", f"year: {d.get('year', '')}",
                  f"venue: {d.get('venue', '')}", f"citationCount (Semantic Scholar): {d.get('citationCount', '')}",
                  f"externalIds: {d.get('externalIds', '')}", f"openAccessPdf: {(d.get('openAccessPdf') or {}).get('url', '')}"]
        if d.get("abstract"):
            lines += ["", "abstract:", d["abstract"]]
    return "\n".join(lines)


def pdf_pypdf(path: Path) -> str:
    """Text layer through pypdf, when the project venv has it (reads PDFs that PDFKit returns empty for)."""
    try:
        import pypdf
    except ImportError:
        return ""
    try:
        reader = pypdf.PdfReader(str(path))
        pages = [f"<!-- page {i + 1} -->\n{(pg.extract_text() or '').strip()}" for i, pg in enumerate(reader.pages)]
    except Exception:                                   # a damaged or encrypted file: let the next converter try
        return ""
    return tidy_pdf_text("\n\n".join(pages))


def convert(path: Path, ctype: str = "") -> list[tuple[str, str]]:
    """[(converter name, text)] in preference order for the file's type."""
    head = path.read_bytes()[:1024]
    if head.startswith(b"%PDF") or "pdf" in ctype:
        return [("pdfkit", pdf_pdfkit(path)), ("pypdf", pdf_pypdf(path)), ("pdf-stdlib", pdf_stdlib(path))]
    if "json" in ctype or head.lstrip()[:1] in (b"{", b"["):
        return [("json-metadata", json_to_text(path.read_bytes()))]
    if b"<html" in head.lower() or b"<!doctype" in head.lower() or "html" in ctype or "xml" in ctype:
        return [("html-text", html_to_text(path.read_bytes()))]
    return [("plain-text", path.read_bytes().decode("utf-8", errors="replace"))]


# ----------------------------------------------------------------------------- readability
def readability(text: str, converter: str = "") -> dict:
    """Score converted text: readable (ok), partial, metadata, blocked or unreadable, with the reasons."""
    words = re.findall(r"[^\W\d_]{2,}", text)
    n = len(words)
    chars = re.sub(r"\s", "", text)
    letters = sum(ch.isalpha() for ch in chars)
    lower = [w.lower() for w in words]
    stop = sum(w in STOP or w in STOP_VI for w in lower) / max(1, n)
    bad = text.count("�") + text.count("(cid:") * 5
    lines = [ln for ln in text.splitlines() if ln.strip()]
    short = sum(len(ln.strip()) <= 2 for ln in lines) / max(1, len(lines))
    avg = sum(map(len, words)) / max(1, n)
    reasons = []
    low = text[:3000].lower()
    if n < 400 and any(s in low for s in BLOCK_SIGNS):
        return dict(verdict="blocked", words=n, reasons=["blocking page (" + next(s for s in BLOCK_SIGNS if s in low) + ")"])
    alnum = sum(ch.isalnum() for ch in chars) / max(1, len(chars))
    if alnum < 0.65 or letters / max(1, len(chars)) < 0.3:              # tables of numbers are fine, symbol soup is not
        reasons.append(f"few letters or digits ({alnum:.0%} alphanumeric, {letters / max(1, len(chars)):.0%} letters)")
    if bad / max(1, len(chars)) > 0.01:
        reasons.append("broken encoding (replacement or CID glyphs)")
    if short > 0.35:
        reasons.append(f"exploded layout ({short:.0%} of lines have ≤2 characters)")
    if n >= 50 and stop < 0.04:
        reasons.append(f"few function words ({stop:.1%}): scrambled or non-text")
    if n and not 3 <= avg <= 12:
        reasons.append(f"odd word length ({avg:.1f})")
    if converter == "json-metadata":
        return dict(verdict="metadata" if n >= 8 else "unreadable", words=n, reasons=reasons or ["bibliographic record"])
    if reasons:
        return dict(verdict="unreadable", words=n, reasons=reasons)
    lost = len(LOST_LIGATURE.findall(text))
    if lost >= 3 and lost / max(1, n) > 0.0005:
        return dict(verdict="partial", words=n, reasons=[f"{lost} words lost a ligature (fi/ff/fl): quotes may not match"])
    if n >= 300:
        return dict(verdict="readable", words=n, reasons=[])
    if n >= 40:
        return dict(verdict="partial", words=n, reasons=[f"short text ({n} words)"])
    return dict(verdict="unreadable", words=n, reasons=[f"almost no text ({n} words)"])


LOST_LIGATURE = re.compile(r"\b(?:classication|specication|identication|verication|dierent|dierence|eect|ecient|"
                           r"signicant|benet|denition|dened|gure|rst|eld|nal|oce|aected|suciently|tradeo|"
                           r"conguration|certied|certication|modied|workow|inuence|reect)\w*", re.I)
RANK = {"readable": 4, "partial": 3, "metadata": 2, "blocked": 1, "unreadable": 0, "error": 0}


# ----------------------------------------------------------------------------- candidate ladder
DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s\"<>]+)", re.I)
ARXIV_RE = re.compile(r"(?:arxiv[:/ ]|arxiv\.org/(?:abs|pdf|html)/)(\d{4}\.\d{4,5})(v\d+)?", re.I)


def classify(item: str) -> tuple[str, str]:
    m = ARXIV_RE.search(item)
    if m:
        return "arxiv", m.group(1)
    if not item.startswith("http") or "doi.org/" in item:
        m = DOI_RE.search(item)
        if m:
            return "doi", m.group(1).rstrip(".")
    return "url", item


def api_json(url: str) -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    tmp = CACHE / ("api-" + re.sub(r"\W+", "_", url)[-80:] + ".json")
    res = download(url, tmp, tries=3)
    if res["code"] != 200:
        return {}
    try:
        return json.loads(tmp.read_text(encoding="utf-8"))
    except ValueError:
        return {}


def ladder(items: list[str], alternates: bool = True) -> list[tuple[str, str]]:
    """Candidates [(tier, url)] in the order they are tried."""
    out, meta = [], []
    for item in items:
        kind, value = classify(item)
        if kind == "arxiv":
            if item.startswith("http"):
                out.append(("L1", item))                        # an explicit URL is always tried first
            if alternates or not item.startswith("http"):
                out += [("L1" if not item.startswith("http") else "L2", f"https://arxiv.org/html/{value}"),
                        ("L2", f"https://arxiv.org/pdf/{value}"), ("L2", f"https://arxiv.org/abs/{value}")]
            meta += [("L4", f"https://export.arxiv.org/api/query?id_list={value}")]
        elif kind == "doi":
            out.append(("L1", f"https://doi.org/{value}"))
            if alternates:
                oa = api_json(f"https://api.openalex.org/works/doi:{urllib.parse.quote(value)}")
                for loc in oa.get("locations", []):
                    for key in ("pdf_url", "landing_page_url"):
                        if loc.get(key) and loc.get("is_oa"):
                            out.append(("L2", loc[key]))
                arx = (oa.get("ids") or {}).get("arxiv") or ""
                s2 = api_json(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{value}"
                              "?fields=openAccessPdf,externalIds")
                if (s2.get("openAccessPdf") or {}).get("url"):
                    out.append(("L2", s2["openAccessPdf"]["url"]))
                arx = arx or (s2.get("externalIds") or {}).get("ArXiv", "")
                if arx:
                    a = classify(f"arXiv:{arx.split('/')[-1]}")[1]
                    out += [("L2", f"https://arxiv.org/html/{a}"), ("L2", f"https://arxiv.org/pdf/{a}")]
            meta += [("L4", f"https://api.crossref.org/works/{value}"),
                     ("L4", f"https://api.openalex.org/works/doi:{urllib.parse.quote(value)}")]
        else:
            out.append(("L1", value))
            if alternates:
                m = DOI_RE.search(value)
                if m and "doi.org" not in value:
                    meta.append(("L4", f"https://api.crossref.org/works/{m.group(1)}"))
    if alternates:
        out += [("L3", f"https://web.archive.org/web/2id_/{u}") for t, u in list(out)
                if t == "L1" and "arxiv.org" not in u and "web.archive.org" not in u]
    seen, ordered = set(), []
    for t, u in out + (meta if alternates else []):
        if u not in seen:
            seen.add(u)
            ordered.append((t, u))
    return ordered


def ext_for(path: Path, ctype: str) -> str:
    head = path.read_bytes()[:512]
    if head.startswith(b"%PDF") or "pdf" in ctype:
        return "pdf"
    if "json" in ctype:
        return "json"
    if "xml" in ctype and b"<feed" in head:
        return "xml"
    return "html" if b"<" in head[:200] else "txt"


def run_ladder(items, alternates=True, tries=3, stop_at="readable", verbose=True):
    """Try every candidate; return (best, attempts) where best = dict(url, tier, converter, text, verdict, …)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    attempts, best = [], None
    for i, (tier, url) in enumerate(ladder(items, alternates)):
        tmp = CACHE / f"cand-{i}"
        res = download(url, tmp, tries=tries)
        if not (200 <= res["code"] < 300) or res["size"] == 0:
            attempts.append(dict(tier=tier, url=url, code=res["code"], type=res["type"], size=res["size"],
                                 converter="–", words=0, verdict="error", reasons=[res["error"] or f"HTTP {res['code']}"]))
            if verbose:
                print(f"  {tier} {res['code']:>3} {url[:90]}  → error")
            continue
        for name, text in convert(tmp, res["type"]):
            score = readability(text, name)
            attempts.append(dict(tier=tier, url=res["final"] if tier != "L3" else url, code=res["code"],
                                 type=res["type"].split(";")[0], size=res["size"], converter=name, words=score["words"],
                                 verdict=score["verdict"], reasons=score["reasons"]))
            if verbose:
                print(f"  {tier} {res['code']:>3} {url[:90]}  {name}: {score['verdict']} ({score['words']} words"
                      + (f"; {'; '.join(score['reasons'])}" if score["reasons"] else "") + ")")
            cand = dict(url=res["final"] if tier != "L3" else url, requested=url, tier=tier, converter=name, text=text,
                        verdict=score["verdict"], words=score["words"], file=tmp, ctype=res["type"])
            if best is None or RANK[cand["verdict"]] > RANK[best["verdict"]] or (
                    cand["verdict"] == best["verdict"] and cand["words"] > best["words"]):
                best = cand
            if score["verdict"] == "readable":
                break
        if best and RANK[best["verdict"]] >= RANK[stop_at]:
            break
    return best, attempts


# ----------------------------------------------------------------------------- writing the trail
STATUS = {"readable": "ok", "partial": "partial", "metadata": "partial", "blocked": "blocked", "unreadable": "error",
          "error": "error"}
REGISTER = {"ok": "fetched", "partial": "partial", "blocked": "blocked", "error": "error"}


def write_trail(args, best, attempts, items):
    folder = source_folder(base_dir(args.base), args.id, args.slug)
    folder.mkdir(parents=True, exist_ok=True)
    now = datetime.now().astimezone().isoformat(timespec="minutes")
    status = STATUS[best["verdict"]] if best else "error"
    raw = "none"
    if best and best["verdict"] in ("readable", "partial", "metadata"):
        ext = ext_for(best["file"], best["ctype"])
        name = "raw." + ext
        n = 2
        while args.append and (folder / name).exists():
            name, n = f"raw-{n}.{ext}", n + 1
        (folder / name).write_bytes(best["file"].read_bytes())
        raw = f"{name} ({best['file'].stat().st_size // 1024} KB)"
    note = (f"{best['converter']} of {best['url']} ({best['verdict']}, {best['words']} words)" if best
            else "no candidate returned content")
    body = best["text"] if best and best["verdict"] in ("readable", "partial", "metadata") else (
        "No readable copy was found. Attempts:\n" + "\n".join(
            f"- {a['tier']} {a['url']}: {a['verdict']} ({'; '.join(a['reasons']) or a['code']})" for a in attempts))
    crawl = folder / "crawl.md"
    if args.append and crawl.exists():
        old = crawl.read_text(encoding="utf-8")
        k = old.count("<!-- fetch ") + 2
        old_status = re.search(r"^status: (\w+)", old, re.M)
        rank = ["error", "blocked", "partial", "ok"]
        if old_status and rank.index(status) > rank.index(old_status.group(1)):
            old = old.replace(old_status.group(0), f"status: {status}", 1)
        crawl.write_text(old.rstrip("\n") + f"\n\n<!-- fetch {k}: {best['url'] if best else items[0]} | fetch.py "
                         f"{best['converter'] if best else 'none'} | {now} | {best['verdict'] if best else 'error'} -->\n"
                         + body + "\n", encoding="utf-8")
    else:
        header = ["---", f"id: {args.id}", f"url: {best['url'] if best else items[0]}", f"requested: {' '.join(items)}",
                  f"fetched: {now}", f"tool: fetch.py (curl + {best['converter'] if best else 'none'}; ladder {best['tier'] if best else '–'})",
                  f'fetch_prompt: "none (full text conversion, not a model extract)"', f"status: {status}",
                  f"task: {args.task}", f"part: {args.part}", f"raw: {raw}", f"conversion: {note}", "---"]
        crawl.write_text("\n".join(header) + "\n" + body + "\n", encoding="utf-8")
    log = folder / "attempts.md"
    rows = "" if log.exists() else ("# Fetch attempts\n\n| Run | Tier | URL | HTTP | Type | KB | Converter | Words | "
                                    "Verdict | Reasons |\n| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |\n")
    for a in attempts:
        rows += (f"| {now} | {a['tier']} | {a['url']} | {a['code']} | {a['type'] or '–'} | {a['size'] // 1024} | "
                 f"{a['converter']} | {a['words']} | {a['verdict']} | {'; '.join(a['reasons']).replace('|', '/') or '–'} |\n")
    with log.open("a", encoding="utf-8") as f:
        f.write(rows)
    return folder, status


def append_webfetch(args) -> int:
    """Append WebFetch output as the next fetch block of crawl.md, set the crawl status and keep the register in step."""
    base = base_dir(args.base)
    folder = next(iter(sorted((base / "research" / "sources").glob(f"{args.id}-*"))), None)   # the folder of fetch.py get
    crawl = folder / "crawl.md" if folder else None
    if not crawl or not crawl.exists():
        print(f"{args.id}: no crawl.md yet – run fetch.py get first (its failed attempt documents the gap)")
        return 1
    text = Path(args.text_file).read_text(encoding="utf-8").strip()
    body = crawl.read_text(encoding="utf-8")
    k = len(re.findall(r"<!-- fetch \d+:", body)) + 2
    now = datetime.now().astimezone().isoformat(timespec="minutes")
    rank = {"error": 0, "blocked": 1, "partial": 2, "ok": 3}            # a later block only upgrades the status
    m = re.search(r"^status: (\w+)$", body, re.M)
    if not m or rank[args.status] > rank.get(m.group(1), -1):
        body = re.sub(r"^status: .*$", f"status: {args.status}", body, count=1, flags=re.M)
    prompt = args.prompt.replace('"', "'")
    crawl.write_text(body.rstrip("\n") + f"\n\n<!-- fetch {k}: {args.url} | WebFetch (L5) | {now} | {args.status} -->\n"
                     f"tool: WebFetch\nfetch_prompt: \"{prompt}\"\n\n{text}\n", encoding="utf-8")
    with (folder / "attempts.md").open("a", encoding="utf-8") as f:
        f.write(f"| {now} | L5 | {args.url} | – | WebFetch | – | – | {len(text.split())} | {args.status} | appended |\n")
    reg, _ = load_register(base)
    regrank = {"error": 0, "blocked": 1, "partial": 2, "fetched": 3}
    new = {"ok": "fetched", "partial": "partial"}[args.status]
    if args.id in reg and regrank[new] > regrank.get(reg[args.id]["status"], -1):
        subprocess.run([sys.executable, str(HERE / "trail.py"), "register", "--base", args.base, "--id", args.id,
                        "--status", new])
    print(f"{args.id}: appended fetch {k} ({len(text.split())} words, WebFetch) → {crawl.relative_to(ROOT)}")
    return 0


def ingest_local(args) -> int:
    """Save files of a local git repository at one revision, verbatim, as one source of the trail.

    Each file is read with `git show REV:PATH` (or from disk with --worktree, for files outside version control)
    and written under a `===== PATH @ REV =====` line, so quote anchors match the exact file text."""
    base = base_dir(args.base)
    repo = (ROOT / args.repo).resolve()
    folder = source_folder(base, args.id, args.slug)
    folder.mkdir(parents=True, exist_ok=True)
    now = datetime.now().astimezone().isoformat(timespec="minutes")
    rev = args.rev
    if not args.worktree:
        rev = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", args.rev], capture_output=True,
                             text=True, check=True).stdout.strip()
    blocks, rows, missing = [], [], []
    for path in args.paths:
        if args.worktree:
            p = (ROOT / path) if not (repo / path).exists() else (repo / path)
            ok = p.exists()
            text = p.read_text(encoding="utf-8") if ok else ""
        else:
            r = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"], capture_output=True, text=True)
            ok, text = r.returncode == 0, r.stdout
        if args.strip_images:
            text = re.sub(r"<data:image/[^>]*>", "<image data removed>", text)
        rows.append(f"| {now} | local | {path} @ {rev} | – | text | {len(text.encode()) // 1024} | "
                    f"{'git show' if not args.worktree else 'read'} | {len(text.split())} | "
                    f"{'readable' if ok and text.strip() else 'error'} | {'–' if ok else 'not found'} |\n")
        if not ok or not text.strip():
            missing.append(path)
            continue
        blocks.append(f"===== {path} @ {rev} =====\n{text.rstrip()}\n")
    body = "\n".join(blocks)
    status = "ok" if blocks and not missing else ("partial" if blocks else "error")
    (folder / "raw.txt").write_text(body, encoding="utf-8")
    if args.url_prefix:
        url = args.url_prefix.rstrip("/") + "/" + args.paths[0]
    else:                                   # a path relative to the project, so the trail reads the same on any machine
        try:
            url = (repo.resolve().relative_to(ROOT) / args.paths[0]).as_posix()
        except ValueError:
            url = f"file://{repo}/{args.paths[0]}"
    header = ["---", f"id: {args.id}", f"url: {url}", f"requested: {' '.join(args.paths)}", f"fetched: {now}",
              f"tool: fetch.py local ({'git show ' + rev if not args.worktree else 'working tree read'}; verbatim, "
              f"{len(blocks)} file(s))", 'fetch_prompt: "none (verbatim file copy, not a model extract)"',
              f"status: {status}", f"task: {args.task}", f"part: {args.part}", f"raw: raw.txt ({len(body.encode()) // 1024} KB)",
              f"conversion: verbatim copy of {len(blocks)} file(s) from {repo.name} at {rev}"
              + (f"; missing: {', '.join(missing)}" if missing else ""), "---"]
    (folder / "crawl.md").write_text("\n".join(header) + "\n" + body, encoding="utf-8")
    log = folder / "attempts.md"
    head = "" if log.exists() else ("# Fetch attempts\n\n| Run | Tier | URL | HTTP | Type | KB | Converter | Words | "
                                    "Verdict | Reasons |\n| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |\n")
    with log.open("a", encoding="utf-8") as f:
        f.write(head + "".join(rows))
    reg, _ = load_register(base)
    if args.id in reg:
        new = {"ok": "fetched", "partial": "partial", "error": "error"}[status]
        subprocess.run([sys.executable, str(HERE / "trail.py"), "register", "--base", args.base, "--id", args.id,
                        "--status", new, "--url", url])
    print(f"{args.id}: status {status} → {folder.relative_to(ROOT)}/crawl.md ({len(blocks)} file(s) at {rev}"
          + (f"; missing {len(missing)}" if missing else "") + ")")
    return 0 if status == "ok" else (3 if status == "partial" else 4)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("get", "meta"):
        p = sub.add_parser(name)
        p.add_argument("--base", required=True)
        p.add_argument("--id", required=True)
        p.add_argument("--slug", required=True)
        p.add_argument("--task", required=True)
        p.add_argument("--part", required=True)
        p.add_argument("--append", action="store_true", help="add a fetch block to an existing crawl.md")
        p.add_argument("--no-alternates", action="store_true", help="only the given URLs (L1), no fallbacks")
        p.add_argument("--tries", type=int, default=3)
        p.add_argument("items", nargs="+")
    w = sub.add_parser("webfetch", help="L5: append a saved WebFetch output to a source's crawl.md")
    w.add_argument("--base", required=True)
    w.add_argument("--id", required=True)
    w.add_argument("--url", required=True)
    w.add_argument("--prompt", required=True, help="the exact prompt given to WebFetch")
    w.add_argument("--text-file", required=True, help="file holding the WebFetch output, unedited")
    w.add_argument("--status", default="partial", choices=["ok", "partial"])
    lo = sub.add_parser("local", help="verbatim copy of files from a local git repository at one revision")
    for opt in ("--base", "--id", "--slug", "--task", "--part", "--repo"):
        lo.add_argument(opt, required=True)
    lo.add_argument("--rev", default="HEAD", help="git revision (commit, tag); ignored with --worktree")
    lo.add_argument("--url-prefix", default="", help="public URL of the repository at that revision, e.g. "
                    "https://github.com/OWNER/REPO/blob/COMMIT")
    lo.add_argument("--worktree", action="store_true", help="read files from disk (paths relative to --repo, "
                    "else to the project root) instead of git")
    lo.add_argument("--strip-images", action="store_true", help="replace embedded data:image URIs")
    lo.add_argument("paths", nargs="+")
    sub.add_parser("find").add_argument("title")
    sub.add_parser("convert").add_argument("file")
    sub.add_parser("probe").add_argument("items", nargs="+")
    args = ap.parse_args()

    if args.cmd == "webfetch":
        return append_webfetch(args)
    if args.cmd == "local":
        return ingest_local(args)
    if args.cmd == "find":
        d = api_json("https://api.openalex.org/works?per-page=8&search=" + urllib.parse.quote(args.title))
        for w in d.get("results", []):
            loc = w.get("best_oa_location") or {}
            print(f"- {w.get('display_name')} ({w.get('publication_year')}); "
                  f"{((w.get('primary_location') or {}).get('source') or {}).get('display_name', '')}; "
                  f"doi {w.get('doi')}; cited_by {w.get('cited_by_count')}; oa {loc.get('pdf_url') or loc.get('landing_page_url')}")
        return 0
    if args.cmd == "convert":
        path = Path(args.file)
        for name, text in convert(path):
            score = readability(text, name)
            print(f"===== {name}: {score['verdict']} ({score['words']} words) {'; '.join(score['reasons'])}")
            print(text[:3000])
        return 0
    if args.cmd == "probe":
        best, _ = run_ladder(args.items, stop_at="readable")
        print(f"best: {best['verdict'] if best else 'none'} {best['url'] if best else ''}")
        return 0

    items = args.items
    if args.cmd == "meta":
        kinds = [classify(i) for i in items]
        urls = [u for k, v in kinds for t, u in ladder([v if k != "arxiv" else f"arXiv:{v}"], False) + [
            ("L4", f"https://api.crossref.org/works/{v}"), ("L4", f"https://api.openalex.org/works/doi:{v}")]
            if t == "L4" and (k == "doi" or "arxiv" in u)]
        best, attempts, parts = None, [], []
        for url in dict.fromkeys(urls):                  # every metadata service, combined into one record
            b, a = run_ladder([url], alternates=False, stop_at="metadata")
            attempts += a
            if b and b["verdict"] == "metadata":
                parts.append(b["text"])
                best = best or b
        if best:
            best = {**best, "text": "\n\n".join(parts), "words": sum(len(x.split()) for x in parts),
                    "converter": "json-metadata", "url": " + ".join(dict.fromkeys(urls))}
    else:
        print(f"{args.id}: trying {len(ladder(items, not args.no_alternates))} candidates")
        best, attempts = run_ladder(items, alternates=not args.no_alternates, tries=args.tries)
    folder, status = write_trail(args, best, attempts, items)
    print(f"{args.id}: status {status} → {folder.relative_to(ROOT)}/crawl.md "
          f"({best['converter'] + ', ' + str(best['words']) + ' words, ' + best['url'] if best else 'nothing usable'})")
    trail = [sys.executable, str(HERE / "trail.py")]
    reg, _ = load_register(base_dir(args.base))
    if args.id in reg:                                   # keep the register in step with the crawl
        rank = {"error": 0, "blocked": 1, "partial": 2, "fetched": 3}       # a later fetch block only upgrades
        new = REGISTER[status]
        if not args.append or rank[new] > rank.get(reg[args.id]["status"], -1):
            subprocess.run(trail + ["register", "--base", args.base, "--id", args.id, "--status", new])
    else:
        print(f"register it: trail.py register --base {args.base} --id {args.id} --slug {args.slug} "
              f"--source \"<short description>\" --url \"{items[0]}\" --status {REGISTER[status]}")
    print(f"next: trail.py comprehension --base {args.base} --id {args.id}, then read crawl.md and fill it"
          + ("; trail.py apa --write for the APA entry" if best and best["converter"] == "json-metadata" else ""))
    if status in ("blocked", "error"):
        print("next: L5 – search for another source that states the same facts; log it in search-log.md as "
              f"'replacement for {args.id}', and keep this folder (it documents the failure).")
        return 4
    return 0 if status == "ok" else 3


if __name__ == "__main__":
    sys.exit(main())
