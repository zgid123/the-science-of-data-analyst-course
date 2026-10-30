# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.26", "diff-match-patch>=20230430", "markdown-it-py>=3"]
# ///
"""Check that a Markdown file reproduces a PDF's content as-is.

Checks (all deterministic; FAIL unless noted):
  text       Character-level diff of the PDF's raw text lines vs the Markdown
             with markup removed. Whitespace and markdown punctuation
             (* _ | # > `) are ignored on both sides; every missing, extra or
             changed letter, digit or symbol counts. Running headers/footers
             are excluded, except constant ones the converter keeps once
             (headers at the top, footers at the end).
  tables     Every ruled PDF table (page-break continuations merged) has a
             Markdown table with the same header and shape, and every cell
             holds the text of the PDF words inside that cell.
  code       Monospace PDF lines appear line by line, indentation included,
             inside fenced code blocks.
  headings   Every bold PDF line at a heading font size is a Markdown heading.
  links      Every external URL linked in the PDF appears in the Markdown.
  images     Raster image count matches; every linked file exists.
  structure  Balanced ``` fences, no heading inside a fence, no line that
             Markdown would render as an indented code block by accident.
  rendered   The text a reader sees (Markdown parsed by a CommonMark renderer,
             ordered-list numbers kept) equals the PDF text - catches literal
             characters that Markdown silently turns into syntax.
  formatting Bold and italic text in the rendered Markdown equal the PDF's bold
             and italic text, in both directions (headings count as bold).
  rules      Free-standing horizontal rules in the PDF appear as --- breaks.
  artefacts  No leftover placeholders, <mark>, ~~, <u>, U+FFFD.
  WARN       Sizeable vector drawings outside tables (possible lost chart).

Exit code 0 = all checks pass, 1 = differences found.

Usage:
  uv run verify.py input.pdf output.md [--json report.json] [--context 40]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pymupdf
from diff_match_patch import diff_match_patch
from markdown_it import MarkdownIt

import pdf_layout as L

IGNORED = set(" \t\r\n *_|#>`\\") | {"​"}
LEADING_BULLET = L.LEADING_BULLET_RE


# ---------------------------------------------------------------- PDF side


def line_text(ln: dict) -> str:
    return L.norm_text("".join(s["text"] for s in ln["spans"]))


def cell_words(page: pymupdf.Page, rect: pymupdf.Rect) -> str:
    """Raw PDF words whose centre lies in the cell, in reading order."""
    words = [w for w in page.get_text("words", sort=True) if L.in_any(pymupdf.Rect(w[:4]), [rect])]
    return L.norm_text(" ".join(w[4] for w in words))


def pdf_stream(doc: pymupdf.Document, layout: L.DocLayout) -> list[tuple[int, str]]:
    """(page, text) chunks in reading order: page by page, top to bottom.

    Table cells are emitted row by row, cell by cell (the order a Markdown
    table uses); other lines by their position on the page.
    """
    heads, foots = layout.running_kept
    chunks: list[tuple[int, str]] = [(1, h) for h in heads]
    for pno, page in enumerate(doc):
        running = layout.running.get(pno, [])
        grids = layout.grids.get(pno, [])
        items: list[tuple[float, float, str]] = []
        # text blocks stay whole (a column's paragraph is one block), so side-by-side
        # columns are compared column by column instead of interleaved line by line
        for b in page.get_text("dict")["blocks"]:
            texts = []
            for ln in b.get("lines", []):
                r = pymupdf.Rect(ln["bbox"])
                if L.in_any(r, running) or L.in_any(r, [g.bbox for g in grids]):
                    continue
                text = line_text(ln)
                if text.strip():
                    texts.append((r, LEADING_BULLET.sub("", text)))
            if texts:
                items.append((round(texts[0][0].y0), texts[0][0].x0, "\n".join(t for _, t in texts)))
        for gi, g in enumerate(grids):
            # a repeated header row on a continuation page is page furniture
            rows = g.rows[1:] if (pno, gi) in layout.repeated_header else g.rows
            parts = [cell_words(page, c.rect) for row in rows for c in row]
            items.append((round(g.bbox.y0), g.bbox.x0, "\n".join(parts)))
        items.sort(key=lambda t: (t[0], t[1]))
        chunks += [(pno + 1, t) for _, _, t in items]
    chunks += [(doc.page_count, f) for f in foots]
    return chunks


# ----------------------------------------------------------- Markdown side


def md_plain(md: str) -> str:
    md = L.norm_text(md)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)  # images
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)  # links -> text
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = re.sub(r"</?(br|u|mark|sup|sub|b|i|em|strong|span)[^>]*>", "\n", md)
    out = []
    for line in md.splitlines():
        if re.fullmatch(r"\s*\|?(\s*:?-{3,}:?\s*\|)+\s*:?-*:?\s*", line):
            continue  # table separator row
        if re.fullmatch(r" {0,3}([-*_])( *\1){2,} *", line):
            continue  # thematic break (horizontal rule)
        line = re.sub(r"^\s*(>\s*)+", "", line)  # blockquote
        line = re.sub(r"^\s*#{1,6}\s+", "", line)  # heading
        line = re.sub(r"^(\s*[-*+]\s+)\[ \]\s", r"\1☐ ", line)  # task list -> PDF glyph
        line = re.sub(r"^(\s*[-*+]\s+)\[[xX]\]\s", r"\1☑ ", line)
        line = LEADING_BULLET.sub("", line)  # list marker
        line = line.replace("~~", "")
        out.append(line)
    return "\n".join(out)


def fences(md: str) -> list[list[str]]:
    blocks, cur = [], None
    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            if cur is None:
                cur = []
            else:
                blocks.append(cur)
                cur = None
        elif cur is not None:
            cur.append(line)
    return blocks


# ------------------------------------------------------------------ checks


def squeeze(text: str) -> tuple[str, list[int]]:
    """Drop ignored chars; keep a map from squeezed index -> original index."""
    keep, idx = [], []
    for i, ch in enumerate(text):
        if ch not in IGNORED:
            keep.append(ch)
            idx.append(i)
    return "".join(keep), idx


def snippet(text: str, idx: list[int], a: int, b: int, ctx: int) -> str:
    if not idx:
        return ""
    lo = idx[max(0, min(a, len(idx) - 1))]
    hi = idx[min(len(idx) - 1, max(b - 1, a))] + 1
    s = text[max(0, lo - ctx) : lo] + "⟦" + text[lo:hi] + "⟧" + text[hi : hi + ctx]
    return re.sub(r"\s+", " ", s)


def text_check(chunks, md_text: str, ctx: int) -> dict:
    pdf_text = ""
    page_at: list[int] = []
    for page, t in chunks:
        pdf_text += t + "\n"
        page_at += [page] * (len(t) + 1)
    plain = md_plain(md_text)
    g, gi = squeeze(pdf_text)
    m, mi = squeeze(plain)

    dmp = diff_match_patch()
    dmp.Diff_Timeout = 30
    diffs = dmp.diff_main(g, m, False)
    dmp.diff_cleanupSemantic(diffs)

    hunks = []
    pg = pm = 0
    for op, data in diffs:
        n = len(data)
        if op == 0:
            pg += n
            pm += n
            continue
        page = page_at[gi[min(pg, len(gi) - 1)]] if gi else 0
        if op == -1:
            hunks.append({"type": "missing", "page": page, "text": data, "where": snippet(pdf_text, gi, pg, pg + n, ctx)})
            pg += n
        else:
            hunks.append({"type": "extra", "page": page, "text": data, "where": snippet(plain, mi, pm, pm + n, ctx)})
            pm += n
    # a missing chunk that reappears as an extra chunk elsewhere = reordering
    extras = [h for h in hunks if h["type"] == "extra"]
    for h in hunks:
        if h["type"] == "missing" and len(h["text"]) >= 8:
            for e in extras:
                if e["type"] == "extra" and h["text"] in e["text"]:
                    h["type"] = e["type"] = "moved"
                    break
    missing = sum(len(h["text"]) for h in hunks if h["type"] == "missing")
    extra = sum(len(h["text"]) for h in hunks if h["type"] == "extra")
    return {
        "pdf_chars": len(g),
        "md_chars": len(m),
        "missing_chars": missing,
        "extra_chars": extra,
        "moved_hunks": sum(h["type"] == "moved" for h in hunks) // 2,
        "similarity": round(1 - (missing + extra) / max(1, len(g)), 5),
        "hunks": hunks,
    }


def md_tables(md: str) -> list[dict]:
    tables, cur = [], []
    for line in md.splitlines() + [""]:
        if line.lstrip().startswith("|"):
            cur.append(line.strip())
        elif cur:
            rows = [r for r in cur if not re.fullmatch(r"\|?(\s*:?-{3,}:?\s*\|)+\s*", r)]
            cells = [[c.strip() for c in re.split(r"(?<!\\)\|", r.removeprefix("|").removesuffix("|"))] for r in rows]
            tables.append({"rows": cells, "cols": max(len(c) for c in cells)})
            cur = []
    return tables


def cell_key(s: str) -> str:
    return L.squeeze(md_plain(s.replace("<br>", "\n").replace("\\|", "|")))


def table_check(doc: pymupdf.Document, layout: L.DocLayout, md: str) -> dict:
    pdf_t = L.merged_tables(layout)
    md_t = md_tables(md)
    problems = []
    j = 0
    for i, t in enumerate(pdf_t):
        # raw-word text of every cell, independent of the converter's cell logic
        raw_rows = []
        for gi, g in enumerate(t["grids"]):
            idx = layout.grids[g.page].index(g)
            rows = g.rows[1:] if gi and (g.page, idx) in layout.repeated_header else g.rows
            for row in rows:
                cells = [""] * g.n_cols
                for c in row:
                    cells[c.col] = cell_words(doc[g.page], c.rect)
                raw_rows.append(cells)
        head = [L.squeeze(c) for c in raw_rows[0]] if raw_rows else []
        k = next((k for k in range(j, len(md_t)) if [cell_key(c) for c in md_t[k]["rows"][0]] == head), None)
        if k is None:
            problems.append({"pdf_table": i + 1, "pages": t["pages"],
                             "issue": f"no markdown table with header {[c[:20] for c in raw_rows[0]] if raw_rows else []}"})
            continue
        mt = md_t[k]
        j = k + 1
        if (len(mt["rows"]), mt["cols"]) != (len(raw_rows), t["n_cols"]):
            problems.append({"pdf_table": i + 1, "pages": t["pages"],
                             "issue": f"shape pdf {len(raw_rows)}x{t['n_cols']} vs md {len(mt['rows'])}x{mt['cols']}"})
            continue
        for r, (prow, mrow) in enumerate(zip(raw_rows, mt["rows"])):
            for c, (pc, mc) in enumerate(zip(prow, mrow)):
                if L.squeeze(pc) != cell_key(mc):
                    problems.append({"pdf_table": i + 1, "pages": t["pages"],
                                     "issue": f"cell r{r + 1}c{c + 1}: pdf {pc[:40]!r} vs md {mc[:40]!r}"})
    return {"pdf_tables": len(pdf_t), "md_tables": len(md_t), "problems": problems,
            "unmatched_md_tables": max(0, len(md_t) - (len(pdf_t) - sum(p["issue"].startswith("no markdown") for p in problems)))}


def code_check(layout: L.DocLayout, md: str) -> list[str]:
    md_blocks = [[l.rstrip() for l in b if l.strip()] for b in fences(md)]
    problems = []
    for pno, blocks in sorted(layout.code.items()):
        for cb in blocks:
            want = [l for l in cb.lines if l.strip()]
            if want not in md_blocks:
                problems.append(f"p{pno + 1}: code block starting {cb.lines[0].strip()[:40]!r} "
                                f"({len(want)} lines) not found verbatim (with indentation) in a ``` fence")
    return problems


def heading_check(doc: pymupdf.Document, layout: L.DocLayout, md: str) -> list[str]:
    joined = "\n".join(L.squeeze(m.group(1)) for m in re.finditer(r"(?m)^#{1,6} (.+)$", md))
    problems = []
    for pno, _, text in L.HeadingLevels(doc, layout).heading_lines():
        key = L.squeeze(text)
        if key and key not in joined:
            problems.append(f"p{pno + 1}: {text.strip()[:60]!r} is not a heading")
    return problems


def link_check(doc: pymupdf.Document, md: str) -> list[str]:
    """Each URI must be linked in the Markdown at least as often as in the PDF."""
    from collections import Counter

    want: Counter[str] = Counter()
    where: dict[str, list[str]] = {}
    for pno, page in enumerate(doc):
        for _, uri, vis in L.page_links(page):
            want[uri] += 1
            where.setdefault(uri, []).append(f"p{pno + 1} {vis[:30]!r}")
    problems = []
    for uri, n in want.items():
        have = md.count(f"]({uri})") + md.count(f"<{uri}>")
        if have < n:
            problems.append(f"{uri}: linked {n}x in pdf ({', '.join(where[uri])}), {have}x in md")
    return problems


def structure_check(md: str) -> list[str]:
    problems = []
    in_fence = in_list = False
    prev_blank = True
    for n, line in enumerate(md.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            prev_blank = False
            continue
        if in_fence:
            if re.match(r"^#{1,6} \S", line):
                problems.append(f"line {n}: heading inside a code fence: {line[:50]!r}")
            continue
        # 4+ spaces after a blank line is code unless we are already in a list
        if prev_blank and not in_list and re.match(r"^( {4,}|\t)\S", line):
            problems.append(f"line {n}: renders as an indented code block: {line.strip()[:50]!r}")
        if re.match(r"^ {0,3}([-*+]|\d{1,3}[.)]) ", line):
            in_list = True
        elif line.strip() and not line.startswith(" "):
            in_list = False
        if re.match(r"^\s*([-*+]\s+)?[☐☑☒]\s", line):
            problems.append(f"line {n}: checkbox glyph instead of a Markdown task item (- [ ] / - [x]): {line.strip()[:50]!r}")
        prev_blank = not line.strip()
    if in_fence:
        problems.append("unclosed ``` fence")
    return problems


def image_check(doc: pymupdf.Document, md: str, md_path: Path) -> dict:
    placed = []
    for pno, page in enumerate(doc):
        for info in page.get_image_info():
            r = pymupdf.Rect(info["bbox"])
            if r.width >= 20 and r.height >= 20:
                placed.append(pno + 1)
    links = re.findall(r"!\[[^\]]*\]\(([^)\s]+)", md)
    broken = [l for l in links if not re.match(r"^(https?:|data:)", l) and not (md_path.parent / l).exists()]
    return {"pdf_images": len(placed), "pdf_image_pages": placed, "md_images": len(links), "broken_links": broken}


def vector_figure_check(doc: pymupdf.Document, layout: L.DocLayout) -> list[dict]:
    """Sizeable vector drawings outside tables/boxes (possible charts)."""
    found = []
    for pno, page in enumerate(doc):
        grids = [g.bbox for g in layout.grids.get(pno, [])]
        for r in page.cluster_drawings(x_tolerance=3, y_tolerance=3):
            if r.width < 60 or r.height < 40 or any(r in g + (-3, -3, 3, 3) for g in grids):
                continue
            if any(r.intersects(g) for g in grids) and r.height < 60:
                continue
            found.append({"page": pno + 1, "bbox": [round(v) for v in r]})
    return found


def junk_check(md: str) -> list[str]:
    found = []
    for pat, why in [(r"ZZ(GRID|IMG|CODE)\d+ZZ", "unreplaced placeholder"), (r"<mark>", "highlight (often a shaded box misread)"),
                     (r"~~", "strikethrough (often a ruling line misread)"), (r"<u>", "underline (often a ruling line misread)"),
                     (r"�", "replacement char (font decoding failure)")]:
        n = len(re.findall(pat, md))
        if n:
            found.append(f"{n}x {pat}: {why}")
    return found


MDIT = MarkdownIt("commonmark").enable(["table", "strikethrough"])


def rendered(md: str) -> dict:
    """What a reader sees: plain text, bold text, italic text, rule count."""
    text, bold, ital = [], [], []
    rules = 0
    tokens = MDIT.parse(md)
    for i, tok in enumerate(tokens):
        if tok.type == "list_item_open" and tok.info:  # ordered item: HTML shows "3." whatever the source delimiter
            text.append(tok.info + ". ")
        elif tok.type == "hr":
            rules += 1
        elif tok.type in ("fence", "code_block"):
            text.append(tok.content)
        elif tok.type == "inline":
            in_heading = i > 0 and tokens[i - 1].type == "heading_open"
            b = i_ = 0
            for ch in tok.children or []:
                if ch.type == "strong_open":
                    b += 1
                elif ch.type == "strong_close":
                    b -= 1
                elif ch.type == "em_open":
                    i_ += 1
                elif ch.type == "em_close":
                    i_ -= 1
                elif ch.type in ("text", "code_inline"):
                    c = ch.content
                    text.append(c)
                    if b or in_heading:
                        bold.append(c)
                    if i_:
                        ital.append(c)
                elif ch.type in ("softbreak", "hardbreak"):
                    text.append("\n")
            text.append("\n")
    plain = re.sub(r"(?m)^\[ \] ", "☐ ", "".join(text))
    plain = re.sub(r"(?m)^\[[xX]\] ", "☑ ", plain)
    return {"text": plain, "bold": "".join(bold), "italic": "".join(ital), "rules": rules}


def dmp_diff(a: str, b: str) -> list[tuple[int, str]]:
    dmp = diff_match_patch()
    dmp.Diff_Timeout = 30
    d = dmp.diff_main(a, b, False)
    dmp.diff_cleanupSemantic(d)
    return [(op, t) for op, t in d if op]


def pair_moved(hunks: list[tuple[int, str]]) -> tuple[list[tuple[int, str]], list[str]]:
    """Split diff hunks into real differences and text that only moved.

    A deleted chunk that reappears inside an inserted chunk (or vice versa)
    is the same text in a different order, e.g. side-by-side column headings.
    """
    real, moved, used = [], [], set()
    for i, (op, t) in enumerate(hunks):
        if i in used:
            continue
        j = next((j for j, (op2, t2) in enumerate(hunks) if j != i and j not in used and op2 == -op
                  and len(min(t, t2, key=len)) >= 4 and (t in t2 or t2 in t)), None)
        if j is not None and t == hunks[j][1]:
            used |= {i, j}
            moved.append(t)
        else:
            real.append((op, t))
    return real, moved


def rendered_check(chunks, md: str) -> tuple[list[str], list[str]]:
    pdf = "".join(L.squeeze(t) for _, t in chunks)
    seen = L.squeeze(rendered(md)["text"])
    real, moved = pair_moved(dmp_diff(pdf, seen))
    return [f"{'missing' if op < 0 else 'extra'} in rendered output: {t[:60]!r}" for op, t in real], moved


def styled_pdf_text(doc: pymupdf.Document, layout: L.DocLayout) -> tuple[str, str]:
    """Bold and italic PDF text in reading order (repeated table headers excluded)."""
    heads, foots = layout.running_kept
    bold, ital = [], []
    for pno, page in enumerate(doc):
        skip = layout.running.get(pno, []) + [c.rect for c in layout.code.get(pno, [])]
        skip += [g.rows[0][0].rect.__class__(g.bbox.x0, g.rows[0][0].rect.y0, g.bbox.x1, g.rows[0][0].rect.y1)
                 for gi, g in enumerate(layout.grids.get(pno, [])) if (pno, gi) in layout.repeated_header]
        items = []
        for b in page.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                r = pymupdf.Rect(ln["bbox"])
                if L.in_any(r, skip):
                    continue
                for s in ln["spans"]:
                    st = L._span_style(s)
                    items.append((r.y0, r.x0, "b" in st, "i" in st, s["text"]))
        for _, _, b, i, t in items:
            if b:
                bold.append(t)
            if i:
                ital.append(t)
    return "".join(bold), "".join(ital)


def formatting_check(doc: pymupdf.Document, layout: L.DocLayout, md: str) -> list[str]:
    r = rendered(md)
    pb, pi = styled_pdf_text(doc, layout)
    out = []
    for name, a, b in (("bold", pb, r["bold"]), ("italic", pi, r["italic"])):
        for op, t in dmp_diff(L.squeeze(a), L.squeeze(b)):
            out.append(f"{name} {'missing' if op < 0 else 'extra'}: {t[:60]!r}")
    return out


def rule_check(layout: L.DocLayout, md: str) -> list[str]:
    want = sum(len(v) for v in layout.rules.values())
    have = rendered(md)["rules"]
    return [] if want == have else [f"pdf has {want} horizontal rules {[p + 1 for p, v in layout.rules.items() for _ in v]}, markdown has {have} --- breaks"]


def running_examples(doc: pymupdf.Document, layout: L.DocLayout) -> list[str]:
    """One real example per distinct removed header/footer line."""
    seen: dict[str, str] = {}
    for pno, rects in sorted(layout.running.items()):
        for b in doc[pno].get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                if L.in_any(pymupdf.Rect(ln["bbox"]), rects):
                    t = line_text(ln).strip()
                    seen.setdefault(re.sub(r"\d+", "#", t), t)
    return list(seen.values())


# --------------------------------------------------------------------- main


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("md", type=Path)
    ap.add_argument("--json", type=Path, help="write the full report as JSON")
    ap.add_argument("--context", type=int, default=40, help="chars of context per diff hunk")
    ap.add_argument("--max-hunks", type=int, default=40)
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    md = a.md.read_text(encoding="utf-8")
    layout = L.analyse(doc)
    r = {
        "pdf": str(a.pdf),
        "md": str(a.md),
        "pages": doc.page_count,
        "running_lines_removed": running_examples(doc, layout),
        "running_lines_kept_once": layout.running_kept[0] + layout.running_kept[1],
        "text": text_check(pdf_stream(doc, layout), md, a.context),
        "tables": table_check(doc, layout, md),
        "code": code_check(layout, md),
        "headings": heading_check(doc, layout, md),
        "links": link_check(doc, md),
        "images": image_check(doc, md, a.md),
        "structure": structure_check(md),
        "rendered": rendered_check(pdf_stream(doc, layout), md)[0],
        "rendered_moved": rendered_check(pdf_stream(doc, layout), md)[1],
        "formatting": formatting_check(doc, layout, md),
        "rules": rule_check(layout, md),
        "junk": junk_check(md),
        "vector_regions": vector_figure_check(doc, layout),
    }
    t, tb, im = r["text"], r["tables"], r["images"]
    ok = {
        "text": t["missing_chars"] == 0 and t["extra_chars"] == 0,
        # every ruled PDF table must match; extra Markdown tables (e.g. a rebuilt
        # borderless table) are allowed - their text is covered by text/rendered
        "tables": not tb["problems"],
        "code": not r["code"],
        "headings": not r["headings"],
        "links": not r["links"],
        "images": im["pdf_images"] == im["md_images"] and not im["broken_links"],
        "structure": not r["structure"],
        "rendered": not r["rendered"],
        "formatting": not r["formatting"],
        "rules": not r["rules"],
        "artefacts": not r["junk"],
    }
    r["checks"] = ok
    r["pass"] = all(ok.values())

    def mark(k):
        return "PASS" if ok[k] else "FAIL"

    def listing(items, limit=15):
        for x in items[:limit]:
            print(f"    {x}")
        if len(items) > limit:
            print(f"    ... {len(items) - limit} more")

    print(f"{a.pdf.name} -> {a.md.name}  ({doc.page_count} pages)")
    print(f"[{mark('text')}] text: similarity {t['similarity']:.4%}, missing {t['missing_chars']} chars, "
          f"extra {t['extra_chars']} chars, reordered hunks {t['moved_hunks']} (of {t['pdf_chars']} chars)")
    for h in [h for h in t["hunks"] if h["type"] != "moved"][: a.max_hunks]:
        print(f"    p{h['page']} {h['type']:7} {h['text'][:60]!r}  …{h['where']}…")
    for h in [h for h in t["hunks"] if h["type"] == "moved"][:10]:
        print(f"    p{h['page']} moved   {h['text'][:60]!r}")
    print(f"[{mark('tables')}] tables: pdf {tb['pdf_tables']} / md {tb['md_tables']} (header, shape and every cell)")
    listing([f"table #{p['pdf_table']} p{p['pages']}: {p['issue']}" for p in tb["problems"]])
    if tb["unmatched_md_tables"]:
        print(f"    note: {tb['unmatched_md_tables']} markdown table(s) without a ruled PDF table "
              "(borderless tables rebuilt by hand?) - check them in the visual review")
    print(f"[{mark('code')}] code blocks: {sum(len(v) for v in layout.code.values())} in pdf")
    listing(r["code"])
    print(f"[{mark('headings')}] headings")
    listing(r["headings"])
    print(f"[{mark('links')}] links")
    listing(r["links"])
    print(f"[{mark('images')}] images: pdf {im['pdf_images']} (pages {im['pdf_image_pages']}) / md {im['md_images']}"
          + (f", broken: {im['broken_links']}" if im["broken_links"] else ""))
    print(f"[{mark('structure')}] structure")
    listing(r["structure"])
    for k in ("rendered", "formatting", "rules"):
        print(f"[{mark(k)}] {k}")
        listing(r[k])
        if k == "rendered" and r["rendered_moved"]:
            print(f"    note: same text in a different order (not a failure): {[t[:30] for t in r['rendered_moved']][:5]}")
    print(f"[{mark('artefacts')}] artefacts: {', '.join(r['junk']) or 'none'}")
    if r["vector_regions"]:
        print(f"[WARN] vector drawings outside tables (check render: figure or decoration?): "
              f"{[(v['page'], v['bbox']) for v in r['vector_regions']][:8]}")
    print(f"  removed running lines (examples): {r['running_lines_removed']}")
    if r["running_lines_kept_once"]:
        print(f"  constant running lines kept once: {r['running_lines_kept_once']}")
    print("RESULT:", "PASS" if r["pass"] else "FAIL")
    if a.json:
        a.json.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
    sys.exit(0 if r["pass"] else 1)


if __name__ == "__main__":
    main()
