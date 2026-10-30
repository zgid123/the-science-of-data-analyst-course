# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.26"]
# ///
"""Exact PDF text for manual takeover, when convert.py cannot handle a part.

Default: one row per text line, labelled with the region it belongs to:
    y   x   size  style  region        text
  style = B (bold) I (italic) M (monospace); region = body, table#N rRcC,
  box, code, running. Copy text from here instead of retyping from images.

--draft: a Markdown draft of the selected pages built only from pdf_layout
(no pymupdf4llm): headings by font size, paragraphs, lists, tables, boxes,
code blocks, image markers. Use it to rebuild a section convert.py garbled,
or a whole document if convert.py fails; then review and run verify.py.

Usage:
  uv run dump_page.py doc.pdf --pages 3,5-6 [--clip x0,y0,x1,y1] [--draft]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pymupdf

import pdf_layout as L


def parse_pages(spec: str | None, n: int) -> list[int]:
    if not spec:
        return list(range(1, n + 1))
    out: list[int] = []
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out += range(int(a), int(b or a) + 1)
    return [p for p in out if 1 <= p <= n]


def region_of(rect: pymupdf.Rect, pno: int, lay: L.DocLayout) -> str:
    if L.in_any(rect, lay.running.get(pno, [])):
        return "running"
    if L.in_any(rect, [c.rect for c in lay.code.get(pno, [])]):
        return "code"
    tables = [g for g in lay.grids.get(pno, []) if not g.is_box]
    for g in lay.grids.get(pno, []):
        if L.in_any(rect, [g.bbox]):
            if g.is_box:
                return "box"
            for row_i, row in enumerate(g.rows):
                for c in row:
                    if L.in_any(rect, [c.rect]):
                        return f"table#{tables.index(g) + 1} r{row_i + 1}c{c.col + 1}"
    return "body"


def style(span: dict) -> str:
    st = L._span_style(span)
    return ("B" if "b" in st else "") + ("I" if "i" in st else "") + ("M" if L.is_mono(span) else "")


def dump(doc, lay, pages, clip):
    for pno in pages:
        page = doc[pno - 1]
        print(f"=== page {pno}  (size {page.rect.width:.0f}x{page.rect.height:.0f}pt)")
        rows = []
        for b in page.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                r = pymupdf.Rect(ln["bbox"])
                if clip and not r.intersects(clip):
                    continue
                text = L.norm_text("".join(s["text"] for s in ln["spans"]))
                if not text.strip():
                    continue
                sp = [s for s in ln["spans"] if s["text"].strip()]
                st = "".join(sorted({c for s in sp for c in style(s)}))
                size = max(s["size"] for s in sp)
                rows.append((r.y0, r.x0, f"{r.y0:6.1f} {r.x0:5.1f} {size:5.1f} {st:3} {region_of(r, pno - 1, lay):14} {text!r}"))
        for _, _, line in sorted(rows):
            print(line)
        for lk in L.page_links(page):
            print(f"  link {[round(v) for v in lk[0]]} {lk[2]!r} -> {lk[1]}")
        for info in page.get_image_info():
            print(f"  image {[round(v) for v in info['bbox']]}")


def draft(doc, lay, pages):
    heads = L.HeadingLevels(doc, lay)
    tables = L.merged_tables(lay)
    for pno in pages:
        page = doc[pno - 1]
        items: list[tuple[float, str]] = []
        skip = lay.running.get(pno - 1, []) + [g.bbox for g in lay.grids.get(pno - 1, [])]
        skip += [c.rect for c in lay.code.get(pno - 1, [])]
        for b in page.get_text("dict")["blocks"]:
            lines = [ln for ln in b.get("lines", []) if not L.in_any(pymupdf.Rect(ln["bbox"]), skip)]
            if not lines:
                continue
            for para in _paragraphs(lines, lay.space_wraps):
                y, md, spans = para
                lvl = heads.levels.get(heads.round(max(s["size"] for s in spans)))
                if lvl and all(L._span_style(s).startswith("b") for s in spans if s["text"].strip()):
                    md = "#" * lvl + " " + md.replace("**", "")
                items.append((y, md))
        for gi, g in enumerate(lay.grids.get(pno - 1, [])):
            if g.is_box:
                items.append((g.bbox.y0, "\n>\n".join("> " + p for p in g.rows[0][0].paragraphs)))
            elif (pno - 1, gi) in lay.continues:
                items.append((g.bbox.y0, "<!-- table continues from previous page: merge rows into it -->"))
            else:
                t = next(t for t in tables if g in t["grids"])
                rows = [[c.replace("|", "\\|") for c in r] for r in t["rows"]]
                md = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * t["n_cols"]]
                md += ["| " + " | ".join(r) + " |" for r in rows[1:]]
                items.append((g.bbox.y0, "\n".join(md)))
        for c in lay.code.get(pno - 1, []):
            items.append((c.rect.y0, "```\n" + "\n".join(c.lines) + "\n```"))
        for info in page.get_image_info():
            r = pymupdf.Rect(info["bbox"])
            if r.width >= 20 and r.height >= 20:
                items.append((r.y0, f"![](IMAGE: page {pno}, bbox {[round(v) for v in r]} - extract and link)"))
        for r in lay.rules.get(pno - 1, []):
            items.append((r.y0, "---"))
        print(f"<!-- page {pno} -->\n")
        for _, md in sorted(items, key=lambda t: t[0]):
            print(md + "\n")


def _paragraphs(lines, space_wraps):
    """Markdown paragraphs of one text block: (y, markdown, spans), list glyphs as "- "."""
    spans = [s for ln in lines for s in ln["spans"]]
    y = lines[0]["bbox"][1]
    out = []
    for i, md in enumerate(L.region_paragraphs(lines, space_wraps)):
        if L.LEADING_BULLET_RE.match(md):
            body = L.LEADING_BULLET_RE.sub("", md, count=1)
            body = re.sub(r"^(\d{1,9})([.)])(?=\s)", r"\1\\\2", body)  # "1)" stays literal text
            md = "- " + body
        md = md.replace("- ☐ ", "- [ ] ").replace("- ☑ ", "- [x] ")
        out.append((y + i * 0.01, md, spans))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--pages", help="e.g. 3,5-6 (default: all)")
    ap.add_argument("--clip", help="x0,y0,x1,y1 in points: only lines intersecting this area")
    ap.add_argument("--draft", action="store_true", help="print a Markdown draft instead of the line table")
    a = ap.parse_args()
    doc = pymupdf.open(a.pdf)
    lay = L.analyse(doc)
    pages = parse_pages(a.pages, doc.page_count)
    if a.draft:
        draft(doc, lay, pages)
    else:
        dump(doc, lay, pages, pymupdf.Rect(*map(float, a.clip.split(","))) if a.clip else None)


if __name__ == "__main__":
    main()
