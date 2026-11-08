"""Estimate the page count of a built Word document when no Word, Pages or LibreOffice is available to render it.

Usage: python .claude/skills/build-report/scripts/estimate_pages.py DOCX [--char-width 0.45]

Word lays out pages only when it opens a file, so this is an estimate from the document's own geometry: every
paragraph is broken into lines at its font size (an average character width of --char-width em for Times New Roman),
with its line spacing and paragraph spacing; every table row takes the height of its tallest cell at the column
widths stored in the table grid; every image takes its printed height. Heights are summed per part (title page,
body up to the reference list, references) and divided by the portrait text height. Page breaks, keep-with-next and
landscape pages are not modelled, so treat the result as a guide within about half a page per part, and as the
lower bound: paginate.py lays the same document out page by page with pessimistic measures, the figure to plan with.
"""

import argparse
import math

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

TEXT_W_PT, TEXT_H_PT = 453.5, 728.5          # 16.0 cm x 25.7 cm (A4 with the builder's margins)


def font_size(p, default):
    for r in p.runs:
        if r.font.size:
            return r.font.size.pt
    s = p.style
    while s is not None:
        if s.font.size:
            return s.font.size.pt
        s = s.base_style
    return default


def line_count(text, size, width, char_width):
    per_line = max(1.0, width / (char_width * size))
    return sum(max(1, math.ceil(len(seg) / per_line)) for seg in text.split("\n")) if text.strip() else 0


def estimate(path, char_width=0.45):
    doc = Document(path)
    body_size = font_size(next((p for p in doc.paragraphs if p.style.name == "Body Text"), doc.paragraphs[0]), 12)
    spacing = (doc.styles["Body Text"].paragraph_format.line_spacing or 1.3)
    heights, part = {"title": 0.0, "body": 0.0, "references": 0.0}, "title"
    for el in doc.element.body:
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc)
            style = p.style.name
            if style.startswith("Heading 1") or style == "Front Heading":
                part = "references" if p.text.strip().lower().startswith(("references", "tài liệu tham khảo")) else \
                    ("body" if part == "title" else part)
            if part == "title":
                continue
            h = 0.0
            extents = el.findall(".//" + qn("wp:extent"))
            if extents:
                h += max(int(e.get("cy")) for e in extents) / 12700.0 + 12
            size = font_size(p, body_size)
            n = line_count(p.text, size, TEXT_W_PT, char_width)
            if n:
                after = p.paragraph_format.space_after.pt if p.paragraph_format.space_after is not None else 6
                h += n * size * (1.1 if style.startswith("Heading") else spacing) * 1.15 + after
                h += 16 if style.startswith("Heading") else 0
            heights[part] += h
        elif el.tag == qn("w:tbl") and part != "title":
            grid = [int(g.get(qn("w:w"))) / 20.0 for g in el.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
            total = 0.0
            for row in Table(el, doc).rows:
                tallest = 0.0
                for cell, w in zip(row.cells, grid):
                    size = next((r.font.size.pt for cp in cell.paragraphs for r in cp.runs if r.font.size), 9.5)
                    n = sum(line_count(cp.text, size, max(w - 10, 20), char_width) for cp in cell.paragraphs)
                    tallest = max(tallest, n * size * 1.05 * 1.15 + 4)
                total += tallest
            heights[part] += total + 12
    return {k: v / TEXT_H_PT for k, v in heights.items()}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("--char-width", type=float, default=0.45, help="average character width in em (default 0.45)")
    args = ap.parse_args()
    pages = estimate(args.docx, args.char_width)
    total = 1 + pages["body"] + pages["references"]
    print(f"title page 1 | body {pages['body']:.1f} | references {pages['references']:.1f} | total about {total:.1f} "
          f"pages (estimate)")


if __name__ == "__main__":
    main()
