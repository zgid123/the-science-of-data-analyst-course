"""Audit the tables of a built report: how each is laid out on the page, and a to-scale preview image of each.

Reads the Word file the build wrote (column widths from w:tblGrid, font size from the runs, page orientation from the
section that holds the table) and counts the lines of every cell with the same measurement the build uses
(table_layout.py). Reports, per table: orientation, font size, columns, rows, height in lines, tallest row, rows of
8 lines or more, and the fill of each column (how much of its width the longest line uses). Draws each table as a PNG
at its printed width, wrapped like Word, so the layout can be looked at without a word processor.

Usage: venv/bin/python reports/milestone-3/code/table_audit.py BUILD.docx OUT_DIR
Writes OUT_DIR/table_audit.md and OUT_DIR/table-NN.png.
"""
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / ".agents" / "skills" / "build-report" / "scripts"))
from table_layout import count_lines, text_pt, unbroken, word_widths  # noqa: E402

PAD_PT = 8.0                       # left + right cell margins (80 twips each)
SCALE = 3                          # pixels per point in the preview
FONT = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
FONT_B = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"


def caption_before(el):
    p = el.getprevious()
    while p is not None and p.tag == qn("w:p") and not "".join(t.text or "" for t in p.iter(qn("w:t"))).strip():
        p = p.getprevious()
    return "".join(t.text or "" for t in p.iter(qn("w:t"))).strip() if p is not None else ""


def section_orientations(doc):
    """Orientation of the section each body element belongs to (sections end at a sectPr)."""
    body = doc.element.body
    out, pending = {}, []
    for el in body:
        pending.append(el)
        sect = el.find(f"{qn('w:pPr')}/{qn('w:sectPr')}") if el.tag == qn("w:p") else None
        if el.tag == qn("w:sectPr"):
            sect = el
        if sect is not None:
            pg = sect.find(qn("w:pgSz"))
            land = pg is not None and pg.get(qn("w:orient")) == "landscape"
            for e in pending:
                out[e] = land
            pending = []
    for e in pending:
        out[e] = False
    return out


def cell_size(cell, default=9.5):
    for p in cell.paragraphs:
        for r in p.runs:
            if r.font.size:
                return r.font.size.pt
    return default


def wrap(text, width_pt, size, bold):
    """Lines of a cell, greedy like Word, using the build's measurement: a word breaks only at its break points
    (after a hyphen between letters, or a zero-width space), and its parts join without a space."""
    out = []
    for para in text.split("\n"):
        line = ""
        for w in para.split():
            for k, part in enumerate(unbroken(w)):
                glue = "" if k else " "
                trial = (line + glue + part) if line else part
                if text_pt(trial, size, bold) <= width_pt * 0.97 or not line:
                    line = trial
                else:
                    out.append(line)
                    line = part
        out.append(line)
    return out


def audit(path, outdir):
    doc = Document(path)
    land = section_orientations(doc)
    outdir.mkdir(parents=True, exist_ok=True)
    rows_md = ["| # | Caption | Page | Pt | Cols × rows | Height (lines) | Tallest row | Rows ≥ 8 lines | Lowest column fill |",
               "| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |"]
    n = 0
    overflow = ["| # | Table | Word wider than its column | Word pt | Column pt |", "| :-- | :-- | :-- | :-- | :-- |"]
    for el in doc.element.body.iter(qn("w:tbl")):
        cap = caption_before(el)
        if not cap.startswith(("Table", "Bảng")):
            continue
        n += 1
        t = Table(el, doc)
        grid = [int(g.get(qn("w:w"))) / 20.0 for g in el.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
        rows = [[c.text for c in r.cells] for r in t.rows]
        size = cell_size(t.rows[min(1, len(t.rows) - 1)].cells[0])
        heights, fills = [], []
        for i, r in enumerate(rows):
            heights.append(max(count_lines(word_widths(c, size, i == 0), w - PAD_PT, size) for c, w in zip(r, grid)))
        for j, w in enumerate(grid):
            longest = max(text_pt(line, size, False) for r in rows[1:] for line in r[j].split("\n")) if len(rows) > 1 else 0
            fills.append(min(1.0, longest / max(1.0, w - PAD_PT)))
        tall = sum(h >= 8 for h in heights[1:])
        for i, r in enumerate(rows):
            for c, w in zip(r, grid):
                for tok in (part for w in c.split() for part in unbroken(w)):
                    if text_pt(tok, size, i == 0) > w - PAD_PT:
                        overflow.append(f"| {n} | {cap[:40]} | `{tok}` | {text_pt(tok, size, i == 0):.0f} | {w - PAD_PT:.0f} |")
        orient = "landscape" if land.get(el) else "portrait"
        rows_md.append(f"| {n} | {cap[:60]} | {orient} | {size} | {len(grid)} × {len(rows) - 1} | {sum(heights)} | "
                       f"{max(heights[1:] or [0])} | {tall} | {min(fills):.2f} |")
        # preview
        line_h = size * 1.15
        font = ImageFont.truetype(FONT, int(size * SCALE))
        fontb = ImageFont.truetype(FONT_B, int(size * SCALE))
        wrapped = [[wrap(c, w - PAD_PT, size, i == 0) for c, w in zip(r, grid)] for i, r in enumerate(rows)]
        row_h = [max(len(c) for c in r) * line_h + 4 for r in wrapped]
        W, H = int(sum(grid) * SCALE) + 2, int((sum(row_h) + 30) * SCALE)
        img = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(img)
        d.text((4, 4), cap[:120], fill="black", font=fontb)
        y = 22 * SCALE
        for i, r in enumerate(wrapped):
            x = 0
            if i == 0:
                d.rectangle([0, y, W - 1, y + row_h[i] * SCALE], fill="#DCE3EE")
            for c, w in zip(r, grid):
                for k, line in enumerate(c):
                    d.text((x + 4 * SCALE, y + (2 + k * line_h) * SCALE), line.replace("\u200b", ""), fill="black", font=fontb if i == 0 else font)
                d.rectangle([x, y, x + w * SCALE, y + row_h[i] * SCALE], outline="#9AA5B4")
                x += w * SCALE
            y += row_h[i] * SCALE
        img.save(outdir / f"table-{n:02d}.png")
    (outdir / "table_audit.md").write_text(f"# Table audit: {Path(path).name}\n\n" + "\n".join(rows_md) + "\n\n## Words wider than their column (Word breaks them mid-word)\n\n" + "\n".join(overflow) + "\n")
    print(f"words wider than their column: {len(overflow) - 2}")
    print("\n".join(rows_md))


if __name__ == "__main__":
    audit(sys.argv[1], Path(sys.argv[2]))
