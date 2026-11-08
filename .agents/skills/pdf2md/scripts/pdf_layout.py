"""Shared PDF layout analysis used by convert.py and verify.py.

Deterministic helpers built directly on PyMuPDF:
  * running header/footer detection (lines repeated in page margins)
  * ruled-table ("grid") detection from vector cell borders
  * cell text extraction with bold/italic runs
  * cross-page table continuation detection

Kept separate so the converter and the verifier agree on what counts as
header/footer noise, while the verifier still compares against raw PDF words.
"""

from __future__ import annotations

import re
import unicodedata
from collections import Counter
from dataclasses import dataclass, field

import pymupdf

# Word/Symbol-font bullets come through as Private Use Area glyphs.
BULLET_MAP = {"": "•", "": "▪", "": "➢", "": "❖", "": "✓", "": "◦",
              "☒": "☑"}  # both checked-box glyphs become Markdown "[x]"
BULLET_CHARS = set("•▪◦‣●○■□➢❖✓·–-*") | set(BULLET_MAP)
NUMBERED_RE = re.compile(r"^\(?([0-9]{1,3}|[a-zA-Z]|[ivxIVX]{1,4})[.)]\s")

MARGIN_FRACTION = 0.12  # top/bottom band searched for running headers/footers
SEG_TOL = 1.6  # pt: max thickness of a filled rect treated as a ruling line
SNAP = 2.0  # pt: clustering tolerance for line coordinates


def norm_text(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    for k, v in BULLET_MAP.items():
        s = s.replace(k, v)
    return s.replace(" ", " ")


# --------------------------------------------------------------------------
# Running headers / footers
# --------------------------------------------------------------------------


def _line_key(text: str) -> str:
    return re.sub(r"\d+", "#", text.strip().lower())


def detect_running_lines(doc: pymupdf.Document) -> dict[int, list[pymupdf.Rect]]:
    """Return {page_index: [rects]} of header/footer lines to drop.

    A line counts as running text when it sits in the top/bottom margin band
    and its digit-normalised text recurs on at least half the pages (min 2).
    """
    if doc.page_count < 2:
        return {}
    candidates: dict[int, list[tuple[str, pymupdf.Rect]]] = {}
    counts: Counter[str] = Counter()
    for pno, page in enumerate(doc):
        h = page.rect.height
        seen = set()
        lst = []
        for b in page.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                r = pymupdf.Rect(ln["bbox"])
                cy = (r.y0 + r.y1) / 2
                if h * MARGIN_FRACTION < cy < h * (1 - MARGIN_FRACTION):
                    continue
                text = "".join(s["text"] for s in ln["spans"]).strip()
                if not text:
                    continue
                key = ("T" if cy <= h * MARGIN_FRACTION else "B") + _line_key(text)
                lst.append((key, r))
                if key not in seen:
                    counts[key] += 1
                    seen.add(key)
        candidates[pno] = lst
    threshold = max(2, doc.page_count // 2)
    running = {k for k, c in counts.items() if c >= threshold}
    out: dict[int, list[pymupdf.Rect]] = {}
    for pno, lst in candidates.items():
        rects = [r for k, r in lst if k in running]
        if rects:
            out[pno] = rects
    return out


def in_any(rect: pymupdf.Rect, rects: list[pymupdf.Rect]) -> bool:
    c = (rect.tl + rect.br) / 2
    return any(c in r for r in rects)


# --------------------------------------------------------------------------
# Grid (ruled table) detection
# --------------------------------------------------------------------------


@dataclass
class Seg:
    pos: float  # y for horizontal, x for vertical
    a: float  # start along the line
    b: float  # end along the line


@dataclass
class Cell:
    rect: pymupdf.Rect
    col: int  # first grid column
    span: int  # number of grid columns covered
    paragraphs: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return " ".join(self.paragraphs)


@dataclass
class Grid:
    page: int
    bbox: pymupdf.Rect
    col_xs: list[float]
    rows: list[list[Cell]]

    @property
    def n_cols(self) -> int:
        return len(self.col_xs) - 1

    @property
    def n_rows(self) -> int:
        return len(self.rows)

    @property
    def is_box(self) -> bool:
        """A single-cell bordered region: a callout/note box, not a table."""
        return self.n_rows == 1 and self.n_cols == 1

    def row_texts(self, i: int) -> list[str]:
        return [c.text for c in self.rows[i]]


def _segments(page: pymupdf.Page) -> tuple[list[Seg], list[Seg]]:
    hs, vs = [], []
    for d in page.get_drawings():
        fill = d.get("fill")
        stroked = "s" in (d.get("type") or "")
        if fill is not None and all(c > 0.97 for c in fill) and not stroked:
            continue  # white fills are invisible
        for it in d["items"]:
            if it[0] == "re":
                r = it[1]
                if r.width <= SEG_TOL and r.height > SEG_TOL:
                    vs.append(Seg((r.x0 + r.x1) / 2, r.y0, r.y1))
                elif r.height <= SEG_TOL and r.width > SEG_TOL:
                    hs.append(Seg((r.y0 + r.y1) / 2, r.x0, r.x1))
                elif stroked and r.width > SEG_TOL and r.height > SEG_TOL:
                    hs += [Seg(r.y0, r.x0, r.x1), Seg(r.y1, r.x0, r.x1)]
                    vs += [Seg(r.x0, r.y0, r.y1), Seg(r.x1, r.y0, r.y1)]
            elif it[0] == "l":
                p, q = it[1], it[2]
                if abs(p.x - q.x) < 1:
                    vs.append(Seg(p.x, min(p.y, q.y), max(p.y, q.y)))
                elif abs(p.y - q.y) < 1:
                    hs.append(Seg(p.y, min(p.x, q.x), max(p.x, q.x)))
    return _merge(hs), _merge(vs)


def _merge(segs: list[Seg]) -> list[Seg]:
    """Snap collinear segments to a common position and join touching pieces."""
    groups: list[list[Seg]] = []
    for s in sorted(segs, key=lambda s: s.pos):
        if groups and s.pos - groups[-1][-1].pos <= SNAP / 2:
            groups[-1].append(s)
        else:
            groups.append([s])
    out: list[Seg] = []
    for grp in groups:
        pos = sum(s.pos for s in grp) / len(grp)
        cur = None
        for s in sorted(grp, key=lambda s: s.a):
            if cur and s.a <= cur.b + SNAP:
                cur.b = max(cur.b, s.b)
            else:
                cur = Seg(pos, s.a, s.b)
                out.append(cur)
    return out


def _cluster(values: list[float]) -> list[float]:
    out: list[list[float]] = []
    for v in sorted(values):
        if out and v - out[-1][-1] <= SNAP:
            out[-1].append(v)
        else:
            out.append([v])
    return [sum(c) / len(c) for c in out]


def detect_grids(page: pymupdf.Page, pno: int) -> list[Grid]:
    hs, vs = _segments(page)
    hs = [s for s in hs if s.b - s.a >= 8]
    vs = [s for s in vs if s.b - s.a >= 3]
    n = len(hs) + len(vs)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, h in enumerate(hs):
        for j, v in enumerate(vs):
            if h.a - SNAP <= v.pos <= h.b + SNAP and v.a - SNAP <= h.pos <= v.b + SNAP:
                parent[find(i)] = find(len(hs) + j)
    comps: dict[int, tuple[list[Seg], list[Seg]]] = {}
    for i in range(n):
        hl, vl = comps.setdefault(find(i), ([], []))
        (hl if i < len(hs) else vl).append(hs[i] if i < len(hs) else vs[i - len(hs)])

    grids = []
    for hl, vl in comps.values():
        if len(hl) < 2 or len(vl) < 2:
            continue
        ys = _cluster([h.pos for h in hl])
        xs = _cluster([v.pos for v in vl])
        # collapse near-coincident rules (shading edges next to borders)
        xs = [x for i, x in enumerate(xs) if i == 0 or x - xs[i - 1] >= 4]
        ys = [y for i, y in enumerate(ys) if i == 0 or y - ys[i - 1] >= 2]
        # tables drawn without outer side (or top/bottom) borders: the rules
        # of the other direction overhang the last line - add virtual edges
        virtual_x: set[float] = set()
        hx0, hx1 = min(h.a for h in hl), max(h.b for h in hl)
        if xs[0] - hx0 > 6:
            xs.insert(0, hx0)
            virtual_x.add(hx0)
        if hx1 - xs[-1] > 6:
            xs.append(hx1)
            virtual_x.add(hx1)
        vy0, vy1 = min(v.a for v in vl), max(v.b for v in vl)
        if ys[0] - vy0 > 6:
            ys.insert(0, vy0)
        if vy1 - ys[-1] > 6:
            ys.append(vy1)
        if len(ys) < 2 or len(xs) < 2:
            continue
        bbox = pymupdf.Rect(xs[0], ys[0], xs[-1], ys[-1])
        if bbox.width < 20 or bbox.height < 8:
            continue
        rows: list[list[Cell]] = []
        for y0, y1 in zip(ys, ys[1:]):
            if y1 - y0 < 4:  # double rules / border padding, not a row
                continue
            mid = (y0 + y1) / 2
            active = [
                i for i, x in enumerate(xs)
                if x in virtual_x or any(abs(v.pos - x) <= SNAP and v.a - SNAP <= mid <= v.b + SNAP for v in vl)
            ]
            if len(active) < 2:
                continue
            cells = [Cell(pymupdf.Rect(xs[a], y0, xs[b], y1), a, b - a) for a, b in zip(active, active[1:])]
            rows.append(cells)
        if not rows:
            continue
        g = Grid(pno, bbox, xs, rows)
        grids.append(g)
    # discard grids nested inside another grid (e.g. shading boxes in cells)
    grids = [g for g in grids if not any(o is not g and g.bbox in o.bbox and o.bbox != g.bbox for o in grids)]
    grids.sort(key=lambda g: (g.bbox.y0, g.bbox.x0))
    return grids


# --------------------------------------------------------------------------
# Styled text runs inside a region
# --------------------------------------------------------------------------


def _span_style(span) -> str:
    font = span["font"].lower()
    bold = bool(span["flags"] & 16) or "bold" in font or "black" in font or "heavy" in font
    italic = bool(span["flags"] & 2) or "italic" in font or "oblique" in font
    return ("b" if bold else "") + ("i" if italic else "")


def _wrap(text: str, style: str) -> str:
    core = text.strip()
    if not core or not style:
        return text
    lead = text[: len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()) :]
    mark = {"b": "**", "i": "_", "bi": "**_"}[style]
    end = {"b": "**", "i": "_", "bi": "_**"}[style]
    return f"{lead}{mark}{core}{end}{trail}"


def _runs_to_md(runs: list[tuple[str, str]]) -> str:
    merged: list[list[str]] = []
    for text, style in runs:
        if merged and (merged[-1][1] == style or not text.strip()):
            merged[-1][0] += text
        else:
            merged.append([text, style])
    md = "".join(_wrap(t, s) for t, s in merged)
    return re.sub(r"\s+", " ", md).strip()


def _starts_list_item(text: str) -> bool:
    t = text.lstrip()
    return bool(t) and (t[0] in BULLET_CHARS and (len(t) == 1 or t[1] == " ")) or bool(NUMBERED_RE.match(t))


def wraps_with_space(doc: pymupdf.Document) -> bool:
    """True if the producer (e.g. MS Word) leaves a trailing space at soft wraps.

    In such PDFs a wrapped line *without* a trailing space is a mid-word break
    ("Answerab|le") or a hyphen break ("Data-|oriented") and must be joined
    without inserting a space.
    """
    ends = total = 0
    for page in doc:
        for b in page.get_text("dict")["blocks"]:
            for ln in b.get("lines", [])[:-1]:  # all but the last line wrap
                t = "".join(s["text"] for s in ln["spans"])
                if t.strip():
                    total += 1
                    ends += t.endswith(" ")
    return total > 0 and ends / total > 0.6


def region_paragraphs(lines: list[dict], space_wraps: bool = False) -> list[str]:
    """Group PDF text lines (from page.get_text('dict')) into markdown paragraphs.

    Soft wraps are joined with a space; a new paragraph starts at a list
    marker, a large vertical gap, or a switch between all-bold and plain lines
    (e.g. a callout title followed by its body).
    """
    # merge pieces of the same visual line (Word often emits several)
    lines = sorted(lines, key=lambda l: (round(l["bbox"][1]), l["bbox"][0]))
    vlines: list[dict] = []
    for ln in lines:
        if vlines and abs(ln["bbox"][1] - vlines[-1]["bbox"][1]) < 2 and ln["bbox"][0] >= vlines[-1]["bbox"][2] - 2:
            prev = vlines[-1]
            gap = ln["bbox"][0] - prev["bbox"][2]
            if gap > 1.5 and not prev["spans"][-1]["text"].endswith(" "):
                prev["spans"].append({"text": " ", "flags": 0, "font": "", "size": 0})
            prev["spans"] += ln["spans"]
            prev["bbox"] = (prev["bbox"][0], min(prev["bbox"][1], ln["bbox"][1]), ln["bbox"][2], max(prev["bbox"][3], ln["bbox"][3]))
        else:
            vlines.append({"bbox": tuple(ln["bbox"]), "spans": list(ln["spans"])})

    paras: list[list[tuple[str, str]]] = []
    prev = None
    for ln in vlines:
        runs = [(norm_text(s["text"]), _span_style(s) if s["font"] else "") for s in ln["spans"]]
        text = "".join(t for t, _ in runs)
        if not text.strip():
            continue
        styles = {s for t, s in runs if t.strip()}
        all_bold = styles and all("b" in s for s in styles)
        size = max((s.get("size", 0) for s in ln["spans"]), default=10) or 10
        new_para = prev is None
        if prev is not None:
            advance = ln["bbox"][1] - prev["bbox"][1]
            if _starts_list_item(text) or advance > 1.6 * size or all_bold != prev["all_bold"]:
                new_para = True
        if new_para:
            paras.append(list(runs))
        else:
            if not (space_wraps and not prev["text"].endswith(" ")):
                paras[-1].append((" ", ""))
            paras[-1].extend(runs)
        prev = {"bbox": ln["bbox"], "all_bold": all_bold, "text": text}
    return [p for p in (_runs_to_md(r) for r in paras) if p]


def _cell_lines(lines: list[dict], cells: list[Cell]) -> dict[int, list[dict]]:
    """Assign text to cells span by span.

    Word sometimes emits a row's cells as one PDF line, and a trailing-space
    span can overhang the column border, so line-level assignment would put
    text in the wrong column. Whitespace-only spans follow their neighbour.
    """
    out: dict[int, list[dict]] = {}
    for ln in lines:
        cur_id, cur = None, None
        for sp in ln["spans"]:
            if sp["text"].strip():
                r = pymupdf.Rect(sp["bbox"])
                c = (r.tl + r.br) / 2
                cid = next((i for i, cell in enumerate(cells) if c in cell.rect), None)
            else:
                cid = cur_id
            if cid is None:
                cur_id, cur = None, None
                continue
            if cid != cur_id:
                cur = {"bbox": tuple(sp["bbox"]), "spans": []}
                out.setdefault(cid, []).append(cur)
                cur_id = cid
            cur["spans"].append(sp)
            b = cur["bbox"]
            cur["bbox"] = (min(b[0], sp["bbox"][0]), min(b[1], sp["bbox"][1]), max(b[2], sp["bbox"][2]), max(b[3], sp["bbox"][3]))
    return out


def link_text(page: pymupdf.Page, rect: pymupdf.Rect) -> str:
    return norm_text(page.get_textbox(rect)).strip()


def page_links(page: pymupdf.Page) -> list[tuple[pymupdf.Rect, str, str]]:
    """(rect, uri, visible text) for every external hyperlink on the page."""
    out = []
    for lk in page.get_links():
        uri = lk.get("uri")
        if uri:
            r = pymupdf.Rect(lk["from"])
            out.append((r, uri, link_text(page, r)))
    return out


def add_links(text: str, links: list[tuple[pymupdf.Rect, str, str]]) -> str:
    for _, uri, vis in links:
        if vis and vis in text and f"[{vis}]" not in text:
            text = text.replace(vis, f"[{vis}]({uri})", 1)
    return text


def fill_grid_text(page: pymupdf.Page, grids: list[Grid], space_wraps: bool = False) -> None:
    all_lines = [ln for b in page.get_text("dict")["blocks"] for ln in b.get("lines", [])]
    links = page_links(page)
    for g in grids:
        cells = [c for row in g.rows for c in row]
        per_cell = _cell_lines(all_lines, cells)
        for i, cell in enumerate(cells):
            mine = [lk for lk in links if in_any(lk[0], [cell.rect])]
            cell.paragraphs = [add_links(p, mine) for p in region_paragraphs(per_cell.get(i, []), space_wraps)]


# --------------------------------------------------------------------------
# Whole-document analysis
# --------------------------------------------------------------------------


def content_bounds(page: pymupdf.Page, running: list[pymupdf.Rect]) -> tuple[float, float]:
    """Y-extent of real content (text/images) on the page, ignoring running lines."""
    ys = []
    for b in page.get_text("dict")["blocks"]:
        r = pymupdf.Rect(b["bbox"])
        if b.get("type") == 0:
            for ln in b["lines"]:
                lr = pymupdf.Rect(ln["bbox"])
                if "".join(s["text"] for s in ln["spans"]).strip() and not in_any(lr, running):
                    ys += [lr.y0, lr.y1]
        else:
            ys += [r.y0, r.y1]
    return (min(ys), max(ys)) if ys else (0, 0)


@dataclass
class DocLayout:
    running: dict[int, list[pymupdf.Rect]]
    grids: dict[int, list[Grid]]
    continues: set[tuple[int, int]]  # (page, grid index) that continue the previous page's last grid
    repeated_header: set[tuple[int, int]]  # continuations whose first row repeats the table header
    space_wraps: bool
    hyphen_breaks: list[tuple[str, str]]  # ("event", "level") for "event-" + newline + "level"
    code: dict[int, list["CodeBlock"]] = field(default_factory=dict)
    para_starts: set[str] = field(default_factory=set)  # squeezed openings of PDF paragraphs
    checkbox_starts: dict[str, str] = field(default_factory=dict)  # squeezed text after a line-start checkbox -> "[ ]"/"[x]"
    running_kept: tuple[list[str], list[str]] = ([], [])  # constant header / footer lines, kept once
    rules: dict[int, list[pymupdf.Rect]] = field(default_factory=dict)  # horizontal rules -> "---"


def analyse(doc: pymupdf.Document) -> DocLayout:
    running = detect_running_lines(doc)
    space_wraps = wraps_with_space(doc)
    grids: dict[int, list[Grid]] = {}
    bounds = {}
    for pno, page in enumerate(doc):
        gs = detect_grids(page, pno)
        fill_grid_text(page, gs, space_wraps)
        # ruled regions without any text are drawings (bar charts, frames), not tables
        grids[pno] = [g for g in gs if any(c.paragraphs for row in g.rows for c in row)]
        bounds[pno] = content_bounds(page, running.get(pno, []))
    continues = set()
    for pno in range(1, doc.page_count):
        prev, cur = grids.get(pno - 1, []), grids.get(pno, [])
        if not prev or not cur:
            continue
        a, b = prev[-1], cur[0]
        if a.is_box or b.is_box:
            continue
        last_ok = a.bbox.y1 >= bounds[pno - 1][1] - 3  # nothing below table a
        first_ok = b.bbox.y0 <= bounds[pno][0] + 3  # nothing above table b
        same_cols = a.n_cols == b.n_cols and all(abs(x - y) <= 3 for x, y in zip(a.col_xs, b.col_xs))
        if last_ok and first_ok and same_cols:
            continues.add((pno, 0))
    # a continuation repeating the header row of the table it continues
    repeated = set()
    for pno, gi in continues:
        start = pno - 1
        while (start, 0) in continues and len(grids[start]) == 1:
            start -= 1  # table spanning 3+ pages: header lives further back
        head = grid_row_cells(grids[start][-1], 0)
        if grid_row_cells(grids[pno][gi], 0) == head:
            repeated.add((pno, gi))
    lay = DocLayout(running, grids, continues, repeated, space_wraps, hyphen_breaks(doc, running, space_wraps))
    lay.code = {pno: code_blocks(page, running.get(pno, []) + [g.bbox for g in grids[pno]]) for pno, page in enumerate(doc)}
    lay.para_starts = paragraph_starts(doc, lay)
    lay.checkbox_starts = checkbox_starts(doc, lay)
    lay.running_kept = constant_running_lines(doc, running)
    lay.rules = {pno: horizontal_rules(page, running.get(pno, []), grids[pno]) for pno, page in enumerate(doc)}
    return lay


def horizontal_rules(page: pymupdf.Page, running: list[pymupdf.Rect], grids: list[Grid]) -> list[pymupdf.Rect]:
    """Free-standing horizontal lines spanning at least half the page width.

    Excludes table/box borders, running-header/footer rules, and underlines
    (of links or of a text line sitting directly on the line).
    """
    width = page.rect.width
    links = [pymupdf.Rect(lk["from"]) for lk in page.get_links()]
    lines = [pymupdf.Rect(ln["bbox"]) for b in page.get_text("dict")["blocks"] for ln in b.get("lines", [])]
    hs, _ = _segments(page)
    out = []
    for h in hs:
        r = pymupdf.Rect(h.a, h.pos - 0.5, h.b, h.pos + 0.5)
        if r.width < width * 0.5:
            continue
        pad = r + (-3, -3, 3, 3)
        if any(pad.intersects(g.bbox) for g in grids) or any(pad.intersects(x) for x in running + links):
            continue
        if any(0 <= r.y0 - l.y1 <= 2 and l.x0 <= r.x0 + 2 and l.x1 >= r.x1 - 2 for l in lines):
            continue  # underline of a text line
        out.append(r)
    return out


# --------------------------------------------------------------------------
# Monospace (code / directory tree) blocks
# --------------------------------------------------------------------------

MONO_RE = re.compile(r"courier|mono|consol|menlo|inconsolata|source ?code|fira ?code|lucida ?console", re.I)


def is_mono(span: dict) -> bool:
    return bool(span["flags"] & 8) or bool(MONO_RE.search(span["font"]))


@dataclass
class CodeBlock:
    rect: pymupdf.Rect
    lines: list[str]  # indentation preserved, trailing spaces stripped


def code_blocks(page: pymupdf.Page, skip: list[pymupdf.Rect]) -> list[CodeBlock]:
    """Runs of whole-line monospace text, with indentation rebuilt from x offsets."""
    lines = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            spans = [s for s in ln["spans"] if s["text"].strip()]
            if spans and all(is_mono(s) for s in spans) and not in_any(pymupdf.Rect(ln["bbox"]), skip):
                lines.append(ln)
    lines.sort(key=lambda l: (round(l["bbox"][1]), l["bbox"][0]))
    groups: list[list[dict]] = []
    for ln in lines:
        size = ln["spans"][0]["size"]
        if groups and ln["bbox"][1] - groups[-1][-1]["bbox"][1] <= 2.2 * size:
            groups[-1].append(ln)
        else:
            groups.append([ln])
    out = []
    for grp in groups:
        widths = [
            (s["bbox"][2] - s["bbox"][0]) / len(s["text"]) for ln in grp for s in ln["spans"] if len(s["text"]) >= 3
        ]
        cw = sorted(widths)[len(widths) // 2] if widths else grp[0]["spans"][0]["size"] * 0.6
        x0 = min(ln["bbox"][0] for ln in grp)
        text_lines = []
        for ln in grp:
            text = "".join(s["text"] for s in ln["spans"])
            first = next(s for s in ln["spans"] if s["text"])
            lead = round((first["bbox"][0] - x0) / cw)
            text_lines.append((" " * lead + norm_text(text)).rstrip())
        rect = pymupdf.Rect(x0, grp[0]["bbox"][1], max(l["bbox"][2] for l in grp), grp[-1]["bbox"][3])
        out.append(CodeBlock(rect, text_lines))
    return out


# --------------------------------------------------------------------------
# Paragraph starts and running lines worth keeping
# --------------------------------------------------------------------------

SQUEEZE_DROP = set(" \t\r\n\u00a0*_|#>`\\")
KEY_LEN = 24


def squeeze(text: str) -> str:
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", norm_text(text))
    text = LEADING_BULLET_RE.sub("", text)
    return "".join(ch for ch in text if ch not in SQUEEZE_DROP)


LEADING_BULLET_RE = re.compile(r"^\s*([•▪◦‣●○■□➢❖✓·]|[-–*+](?=\s))\s*")


def paragraph_starts(doc: pymupdf.Document, lay: "DocLayout") -> set[str]:
    """Squeezed openings of every PDF line that begins a paragraph or list item.

    A line starts a paragraph when it opens a text block, follows a bullet
    glyph, starts with a list number, follows an unusually large vertical gap,
    or moves left of the hanging indent of the list item above it (Word puts
    a list and the paragraph after it in one block). Everything else is a
    wrapped continuation that the converter may join to the previous line.
    """
    keys = set()
    for pno, page in enumerate(doc):
        skip = lay.running.get(pno, []) + [g.bbox for g in lay.grids.get(pno, [])] + [c.rect for c in lay.code.get(pno, [])]
        for b in page.get_text("dict")["blocks"]:
            lines = [ln for ln in b.get("lines", []) if not in_any(pymupdf.Rect(ln["bbox"]), skip)]
            texts = [norm_text("".join(s["text"] for s in ln["spans"])) for ln in lines]
            item_x = None  # x of the current list item's text, if inside one
            after_glyph = False
            prev = None
            for i, (ln, text) in enumerate(zip(lines, texts)):
                if not text.strip():
                    continue
                if LEADING_BULLET_RE.sub("", text).strip() == "":
                    after_glyph = True  # bullet glyph on its own line; the text follows
                    continue
                x0, y0 = ln["bbox"][0], ln["bbox"][1]
                size = max((s["size"] for s in ln["spans"]), default=10)
                start = prev is None or after_glyph or _starts_list_item(text)
                if prev is not None and y0 - prev[1] > 1.6 * size:
                    start = True
                if item_x is not None and x0 < item_x - 3:
                    start, item_x = True, None
                if after_glyph or _starts_list_item(text):
                    item_x = x0 if after_glyph else None
                if start:
                    k = squeeze(text + "".join(texts[i + 1 : i + 2]))[:KEY_LEN]
                    if k:
                        keys.add(k)
                after_glyph = False
                prev = (x0, y0)
    return keys


# Empty and checked box glyphs. □ ▢ (U+25A1/2, "white square") serve as empty checkboxes in many Word templates;
# pymupdf4llm reads the whole U+25A0-25FF block as bullets, so their lines are found here and marked by the converter.
CHECKBOX_EMPTY = "☐□▢"
CHECKBOX_DONE = "☑"  # ☒ is mapped to ☑ by norm_text


def checkbox_starts(doc: pymupdf.Document, lay: "DocLayout") -> dict[str, str]:
    """Squeezed text of every line outside tables, code and running lines that starts with a checkbox glyph.

    The glyph may stand alone on its line with the text on the next one. Values are the task-list marks.
    """
    keys: dict[str, str] = {}
    for pno, page in enumerate(doc):
        skip = lay.running.get(pno, []) + [g.bbox for g in lay.grids.get(pno, [])] + [c.rect for c in lay.code.get(pno, [])]
        for b in page.get_text("dict")["blocks"]:
            lines = [ln for ln in b.get("lines", []) if not in_any(pymupdf.Rect(ln["bbox"]), skip)]
            texts = [norm_text("".join(s["text"] for s in ln["spans"])).strip() for ln in lines]
            for i, text in enumerate(texts):
                if not text or text[0] not in CHECKBOX_EMPTY + CHECKBOX_DONE:
                    continue
                rest = text[1:].strip() or (texts[i + 1] if i + 1 < len(texts) else "")
                k = squeeze(rest)[:KEY_LEN]
                if k:
                    keys[k] = "[ ]" if text[0] in CHECKBOX_EMPTY else "[x]"
    return keys


def constant_running_lines(doc: pymupdf.Document, running: dict) -> tuple[list[str], list[str]]:
    """Running lines whose text never changes (e.g. course code, project title).

    They carry document metadata that appears nowhere else, so the converter
    keeps one copy (headers at the top, footers at the end). Lines that vary
    from page to page (page numbers) are dropped.
    """
    seen: dict[tuple[str, str], set[str]] = {}
    order: list[tuple[str, str]] = []
    for pno, rects in sorted(running.items()):
        h = doc[pno].rect.height
        for b in doc[pno].get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                r = pymupdf.Rect(ln["bbox"])
                if not in_any(r, rects):
                    continue
                text = norm_text("".join(s["text"] for s in ln["spans"])).strip()
                key = ("T" if (r.y0 + r.y1) / 2 < h / 2 else "B", _line_key(text))
                if key not in seen:
                    seen[key] = set()
                    order.append(key)
                seen[key].add(text)
    heads = [next(iter(seen[k])) for k in order if k[0] == "T" and len(seen[k]) == 1]
    foots = [next(iter(seen[k])) for k in order if k[0] == "B" and len(seen[k]) == 1]
    return heads, foots


def hyphen_breaks(doc: pymupdf.Document, running: dict, space_wraps: bool) -> list[tuple[str, str]]:
    """Words broken across lines at a real hyphen (only knowable in space-wrap PDFs)."""
    if not space_wraps:
        return []
    pairs = []
    for pno, page in enumerate(doc):
        skip = running.get(pno, [])
        for b in page.get_text("dict")["blocks"]:
            lines = [
                "".join(s["text"] for s in ln["spans"])
                for ln in b.get("lines", [])
                if not in_any(pymupdf.Rect(ln["bbox"]), skip)
            ]
            for cur, nxt in zip(lines, lines[1:]):
                m1 = re.search(r"(\w+)-$", norm_text(cur))
                m2 = re.match(r"(\w+)", norm_text(nxt))
                if m1 and m2:
                    pairs.append((m1.group(1), m2.group(1)))
    return pairs


def merged_tables(layout: DocLayout) -> list[dict]:
    """Document-order list of tables after joining page-break continuations.

    Each entry: {"pages": [...], "rows": [[cell text, ...], ...], "n_cols": int, "grids": [Grid]}.
    A repeated header row on the continuation page is dropped.
    """
    out: list[dict] = []
    for pno in sorted(layout.grids):
        for gi, g in enumerate(layout.grids[pno]):
            if g.is_box:
                continue
            rows = [grid_row_cells(g, i) for i in range(g.n_rows)]
            if (pno, gi) in layout.continues and out:
                t = out[-1]
                if (pno, gi) in layout.repeated_header:
                    rows = rows[1:]
                t["rows"] += rows
                t["pages"].append(pno + 1)
                t["grids"].append(g)
            else:
                out.append({"pages": [pno + 1], "rows": rows, "n_cols": g.n_cols, "grids": [g]})
    return out


def grid_row_cells(g: Grid, i: int) -> list[str]:
    """Row as a list of n_cols strings; spanned columns become empty cells."""
    cells = [""] * g.n_cols
    for c in g.rows[i]:
        cells[c.col] = "<br>".join(c.paragraphs)
    return cells


# --------------------------------------------------------------------------
# Heading levels from font size
# --------------------------------------------------------------------------


class HeadingLevels:
    """Deterministic heading levels (also pymupdf4llm's `hdr_info` hook).

    Body size = font size carrying the most characters outside tables, boxes
    and code. Bold text >= body + 1pt is a heading; distinct sizes ranked
    largest-first give levels 1..6. Sizes that appear only on the first page
    (cover styling, e.g. a kicker above the title) are not headings, except
    the single largest size, which is the document title.
    """

    def __init__(self, doc: pymupdf.Document, layout: DocLayout):
        from collections import Counter, defaultdict

        chars: Counter[float] = Counter()
        pages: dict[float, set[int]] = defaultdict(set)
        bold_sizes: set[float] = set()
        self.lines: list[tuple[int, float, str]] = []  # (page, size, text) of bold lines
        for pno, page in enumerate(doc):
            skip = (
                layout.running.get(pno, [])
                + [g.bbox for g in layout.grids.get(pno, [])]
                + [c.rect for c in layout.code.get(pno, [])]
            )
            for b in page.get_text("dict")["blocks"]:
                for ln in b.get("lines", []):
                    if in_any(pymupdf.Rect(ln["bbox"]), skip):
                        continue
                    spans = [s for s in ln["spans"] if s["text"].strip()]
                    for s in spans:
                        size = self.round(s["size"])
                        chars[size] += len(s["text"])
                        pages[size].add(pno)
                        if _span_style(s).startswith("b"):
                            bold_sizes.add(size)
                    if spans and all(_span_style(s).startswith("b") for s in spans):
                        self.lines.append((pno, self.round(max(s["size"] for s in spans)),
                                           norm_text("".join(s["text"] for s in spans))))
        self.body = chars.most_common(1)[0][0] if chars else 10.0
        cands = sorted((s for s in bold_sizes if s >= self.body + 1), reverse=True)
        if doc.page_count > 2:
            cands = [s for i, s in enumerate(cands) if i == 0 or pages[s] != {0}]
        self.levels = {s: min(i + 1, 6) for i, s in enumerate(cands)}

    @staticmethod
    def round(size: float) -> float:
        return round(size * 2) / 2

    def get_header_id(self, span: dict, page=None) -> str:
        if not _span_style(span).startswith("b"):
            return ""
        lvl = self.levels.get(self.round(span["size"]))
        return "#" * lvl + " " if lvl else ""

    def heading_lines(self) -> list[tuple[int, int, str]]:
        """(page, level, text) for every PDF line that should be a heading."""
        return [(p, self.levels[s], t) for p, s, t in self.lines if s in self.levels]
