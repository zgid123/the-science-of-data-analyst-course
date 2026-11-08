"""Pessimistic page estimate of a built Word document: lay the content out page by page, as Word must.

Usage: python .claude/skills/build-report/scripts/paginate.py DOCX [--blocks] [--optimistic]

estimate_pages.py sums the height of all content and divides by the page height, as if text flowed without gaps. A
real document loses space at every page boundary, and this estimate follows the rules the builder writes into the
document instead:

- every section (the landscape groups of wide tables and figures) starts on a new page, in its own orientation and
  text area; a paragraph with page_break_before (style or direct) or a page break run starts a new page;
- a table row never splits (the builder sets cantSplit on every row); when a table continues on a new page its header
  row is repeated (tblHeader);
- a figure never splits; a heading, a caption and a paragraph holding a figure keep with what follows (keep_with_next),
  so they move to the next page together with at least two lines of the next paragraph, the first two rows of the
  next table or the whole next figure;
- a paragraph split across pages keeps at least two lines on each page (widow and orphan control).

Text is measured pessimistically: average character width 0.50 em in body text and 0.52 em in table cells (against
0.45 em in estimate_pages.py), a line filled to only 92% of its width because lines break at word boundaries, a word
longer than a line taking lines of its own, a line height of 1.17 times the font size times the line spacing, the
paragraph's own space before and after, and per-row cell padding of 6 pt. With --optimistic the same layout runs with
the measures of estimate_pages.py, so the two runs bracket the real length.

Positions are counted in pages (page index plus the filled share of the page), so the length of a part is the
distance between its first and last position, including the space it leaves empty before page breaks. --blocks
reports every heading of levels 1–3 and every table as its own block.
"""

import argparse
import math
import re
import sys

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

PT_PER_TWIP = 1 / 20.0
CAPTION = re.compile(r"^(Table|Bảng) ([A-Z]\.)?[0-9]+(\.[0-9]+)*\. ")   # a table caption, not a sentence about a table
PESSIMISTIC = dict(char_text=0.50, char_table=0.52, fill=0.92, leading=1.17, row_pad=6.0, cell_margin=11.0)
OPTIMISTIC = dict(char_text=0.45, char_table=0.45, fill=1.0, leading=1.15, row_pad=4.0, cell_margin=10.0)


def style_attr(p, name):
    """A paragraph-format attribute set directly or inherited through the style chain."""
    v = getattr(p.paragraph_format, name)
    s = p.style
    while v is None and s is not None:
        v = getattr(s.paragraph_format, name)
        s = s.base_style
    return v


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


def lines(text, size, width, char_w, fill):
    """Lines a text needs at a width: words wrap at boundaries; a word longer than a line takes lines of its own."""
    if not text.strip():
        return 0
    per_line = max(1.0, width * fill / (char_w * size))
    total = 0
    for seg in text.split("\n"):
        n, cur = 0, 0.0
        for word in seg.split():
            w = len(word) + 1
            if w > per_line:                         # long token: breaks on its own lines
                n += (1 if cur else 0) + math.ceil(len(word) / per_line)
                cur = 0.0
                continue
            if cur + w > per_line:
                n, cur = n + 1, 0.0
            cur += w
        total += n + (1 if cur else 0) or 1
    return total


class Layout:
    def __init__(self, m):
        self.m, self.page, self.y, self.h = m, 0, 0.0, 0.0

    def pos(self):
        return self.page + (self.y / self.h if self.h else 0.0)

    def new_page(self):
        if self.y > 0:
            self.page, self.y = self.page + 1, 0.0

    def section(self, height):
        """A section starts on a new page with its own text height."""
        if self.h:
            self.new_page()
        self.h = height

    def room(self):
        return self.h - self.y

    def place(self, height):
        """An unsplittable block: move to a new page if it does not fit (unless the page is empty)."""
        if height > self.room() and self.y > 0:
            self.new_page()
        self.y += height
        while self.y > self.h:                       # taller than a page: overflow onto further pages
            self.page, self.y = self.page + 1, self.y - self.h


def section_geometry(sect):
    pg, mar = sect.find(qn("w:pgSz")), sect.find(qn("w:pgMar"))
    w, h = int(pg.get(qn("w:w"))) * PT_PER_TWIP, int(pg.get(qn("w:h"))) * PT_PER_TWIP
    left, right = int(mar.get(qn("w:left"))) * PT_PER_TWIP, int(mar.get(qn("w:right"))) * PT_PER_TWIP
    top, bottom = int(mar.get(qn("w:top"))) * PT_PER_TWIP, int(mar.get(qn("w:bottom"))) * PT_PER_TWIP
    return w - left - right, h - top - bottom


def blocks_of(doc, m):
    """The body as a list of blocks with their geometry: (kind, label, data, section index)."""
    body = doc.element.body
    sections = [el.find(qn("w:pPr")).find(qn("w:sectPr")) for el in body
                if el.tag == qn("w:p") and el.find(qn("w:pPr")) is not None
                and el.find(qn("w:pPr")).find(qn("w:sectPr")) is not None] + [body.find(qn("w:sectPr"))]
    geo = [section_geometry(s) for s in sections]
    body_size = font_size(next((p for p in doc.paragraphs if p.style.name == "Body Text"), doc.paragraphs[0]), 12)
    out, sec = [], 0
    for el in body:
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc)
            width = geo[sec][0]
            size = font_size(p, body_size)
            spacing = style_attr(p, "line_spacing") or 1.15
            spacing = spacing if isinstance(spacing, float) else 1.15
            before = (style_attr(p, "space_before") or 0)
            after = style_attr(p, "space_after")
            before = before.pt if hasattr(before, "pt") else 0.0
            after = after.pt if hasattr(after, "pt") else 6.0
            n = lines(p.text, size, width, m["char_text"], m["fill"])
            image = max((int(e.get("cy")) / 12700.0 for e in el.findall(".//" + qn("wp:extent"))), default=0.0)
            out.append(dict(kind="p", style=p.style.name, text=p.text.strip(), sec=sec, n=n,
                            line_h=size * spacing * m["leading"], before=before, after=after, image=image,
                            keep=bool(style_attr(p, "keep_with_next")), brk=bool(style_attr(p, "page_break_before"))
                            or bool(el.findall(".//" + qn("w:br") + "[@" + qn("w:type") + "='page']"))))
            ppr = el.find(qn("w:pPr"))
            if ppr is not None and ppr.find(qn("w:sectPr")) is not None:
                sec += 1
        elif el.tag == qn("w:tbl"):
            width = geo[sec][0]
            grid = [int(g.get(qn("w:w"))) * PT_PER_TWIP for g in el.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
            scale = min(1.0, width / sum(grid)) if sum(grid) else 1.0
            rows = []
            for row in Table(el, doc).rows:
                tallest = 0.0
                for cell, w in zip(row.cells, grid):
                    size = next((r.font.size.pt for cp in cell.paragraphs for r in cp.runs if r.font.size), 9.5)
                    n = sum(max(1, lines(cp.text, size, max(w * scale - m["cell_margin"], 20), m["char_table"],
                                         m["fill"])) for cp in cell.paragraphs)
                    tallest = max(tallest, n * size * 1.05 * m["leading"])
                rows.append(tallest + m["row_pad"])
            out.append(dict(kind="t", sec=sec, rows=rows, after=12.0))
    return out, geo


def paginate(path, m=PESSIMISTIC, split_blocks=False):
    """[(label, start, end)] in pages for every level-1 heading (or every block with split_blocks)."""
    doc = Document(path)
    blocks, geo = blocks_of(doc, m)
    L = Layout(m)
    cur_sec = -1
    marks = []                                       # (label, position) at each block boundary
    label = None
    for i, b in enumerate(blocks):
        if b["sec"] != cur_sec:
            cur_sec = b["sec"]
            L.section(geo[cur_sec][1])
        if b["kind"] == "p":
            style = b["style"]
            split = style.startswith("Heading 1") or style == "Front Heading" or style == "Title"
            if split_blocks and style[:9] in ("Heading 2", "Heading 3"):
                split = True
            if b["brk"]:
                L.new_page()
            h = b["before"] + b["n"] * b["line_h"] + b["after"] + (b["image"] + 6 if b["image"] else 0)
            if b["keep"] and i + 1 < len(blocks):    # keep with the start of the next block
                nxt = blocks[i + 1]
                if nxt["kind"] == "t":
                    lead = sum(nxt["rows"][:2])
                else:
                    lead = (nxt["image"] + 6) if nxt["image"] else min(nxt["n"], 2) * nxt["line_h"]
                if h + lead > L.room() and L.y > 0:
                    L.new_page()
            # a block starts where its first line lands, after any page break or keep-with-next move
            if split_blocks and CAPTION.match(b["text"]) and label is not None:
                marks.append((f"  [table] {b['text'][:37]}", L.pos()))
                label = "table"
            elif split:
                label = b["text"][:45]
                marks.append((label, L.pos()))
            if b["image"] or b["n"] <= 3:
                L.place(h)
            else:                                    # splittable paragraph with widow and orphan control
                L.y += b["before"]
                left = b["n"]
                while left:
                    fit = int(L.room() // b["line_h"])
                    if fit >= left:
                        L.y += left * b["line_h"]
                        left = 0
                    elif fit >= 2 and left - fit >= 2:
                        L.y += fit * b["line_h"]
                        left -= fit
                        L.new_page()
                    elif fit >= 2 and left - fit < 2 and fit - (2 - (left - fit)) >= 2:
                        take = fit - (2 - (left - fit))
                        L.y += take * b["line_h"]
                        left -= take
                        L.new_page()
                    else:
                        L.new_page()
                L.y = min(L.y + b["after"], L.h)
        else:
            header = b["rows"][0] if b["rows"] else 0.0
            for k, r in enumerate(b["rows"]):
                if r > L.room() and L.y > 0:
                    L.new_page()
                    if k > 0:
                        L.y += header                # repeated header row
                L.place(r)
            L.y = min(L.y + b["after"], L.h)
            if split_blocks and label == "table":
                marks.append((marks[-1][0].replace("  [table] ", "  (text after) "), L.pos()))
                label = "after"
    marks.append(("(end)", L.pos()))
    return [(marks[k][0], marks[k][1], marks[k + 1][1]) for k in range(len(marks) - 1)], L.page + 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("--blocks", action="store_true")
    ap.add_argument("--optimistic", action="store_true")
    a = ap.parse_args()
    parts, total = paginate(a.docx, OPTIMISTIC if a.optimistic else PESSIMISTIC, a.blocks)
    for name, s, e in parts:
        print(f"{name:50} {e - s:5.2f}   (pages {math.floor(s) + 1}–{math.floor(e - 1e-9) + 1})")
    print(f"total about {total} pages ({'optimistic' if a.optimistic else 'pessimistic'} layout)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
