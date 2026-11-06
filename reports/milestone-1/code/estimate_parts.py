"""Estimate the pages of each part of a built Word document (the page budget of the brief: 6–10 pages of main content).

Uses the line model of build-report's estimate_pages.py (paragraph lines at their font size and spacing, table rows at
the stored column widths, images at their printed height) and sums the height per level-1 heading: front pages,
Parts 1–9, references and appendices. The brief counts the main content, Parts 1–9, against its 6–10 pages. Each part
of a full-layout build starts on a new page, so a part also occupies the rest of its last page; the "pages used"
column rounds every part up to a whole page for that case; with part_breaks = false the content total applies.
Landscape pages are not modelled.

With --blocks, the main content is split finer, by heading (levels 1–3), and each table is listed on its own line
under its caption, so that the cost of each block can be weighed when deciding what moves to an appendix.

Usage (from the repository root):
    venv/bin/python reports/milestone-1/code/estimate_parts.py reports/milestone-1/build/N04_Milestone1_EN.docx
    venv/bin/python reports/milestone-1/code/estimate_parts.py reports/milestone-1/build/N04_Milestone1_EN.docx --blocks
"""

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / ".agents" / "skills" / "build-report" / "scripts"))
from docx import Document  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.table import Table  # noqa: E402
from docx.text.paragraph import Paragraph  # noqa: E402
from estimate_pages import TEXT_H_PT, TEXT_W_PT, font_size, line_count  # noqa: E402


def parts(path: str, char_width: float = 0.45, blocks: bool = False) -> list[tuple[str, float]]:
    doc = Document(path)
    body_size = font_size(next((p for p in doc.paragraphs if p.style.name == "Body Text"), doc.paragraphs[0]), 12)
    spacing = doc.styles["Body Text"].paragraph_format.line_spacing or 1.3
    out, name, h = [], None, 0.0
    for el in doc.element.body:
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc)
            style = p.style.name
            split = style.startswith("Heading 1") or style == "Front Heading"
            if blocks and style[:9] in ("Heading 2", "Heading 3"):
                split = True
            if blocks and p.text.strip().startswith(("Table ", "Bảng ")) and name is not None:
                out.append((name, h / TEXT_H_PT))
                name, h = "  [table] " + p.text.strip()[:37], 0.0
                continue
            if split:
                if name is not None:
                    out.append((name, h / TEXT_H_PT))
                name, h = p.text.strip()[:45], 0.0
            if name is None:
                continue
            extents = el.findall(".//" + qn("wp:extent"))
            if extents:
                h += max(int(e.get("cy")) for e in extents) / 12700.0 + 12
            size = font_size(p, body_size)
            n = line_count(p.text, size, TEXT_W_PT, char_width)
            if n:
                after = p.paragraph_format.space_after.pt if p.paragraph_format.space_after is not None else 6
                h += n * size * (1.1 if style.startswith("Heading") else spacing) * 1.15 + after
                h += 16 if style.startswith("Heading") else 0
        elif el.tag == qn("w:tbl") and name is not None:
            grid = [int(g.get(qn("w:w"))) / 20.0 for g in el.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
            for row in Table(el, doc).rows:
                tallest = 0.0
                for cell, w in zip(row.cells, grid):
                    size = next((r.font.size.pt for cp in cell.paragraphs for r in cp.runs if r.font.size), 9.5)
                    n = sum(line_count(cp.text, size, max(w - 10, 20), char_width) for cp in cell.paragraphs)
                    tallest = max(tallest, n * size * 1.05 * 1.15 + 4)
                h += tallest
            h += 12
            if blocks:
                out.append((name, h / TEXT_H_PT))
                name, h = name.replace("  [table] ", "  (text after) "), 0.0
    out.append((name, h / TEXT_H_PT))
    return out


def main() -> int:
    if "--blocks" in sys.argv:
        rows = parts(sys.argv[1], blocks=True)
        start = next(i for i, (n, _) in enumerate(rows) if n[:2].rstrip(".").isdigit())
        end = next(i for i, (n, _) in enumerate(rows) if n.startswith(("References", "Tài liệu")))
        for n, p in rows[start:end]:
            if p >= 0.01:
                print(f"{n:50} {p:5.2f}")
        print(f"main content: {sum(p for _, p in rows[start:end]):.1f} pages")
        return 0
    rows = parts(sys.argv[1])
    main_parts = [(n, p) for n, p in rows if n[:2].rstrip(".").isdigit()]
    print(f"{'part':47} {'pages':>6} {'pages used':>10}")
    for n, p in rows:
        print(f"{n:47} {p:6.1f} {math.ceil(p) if (n, p) in main_parts else '':>10}")
    content = sum(p for _, p in main_parts)
    used = sum(math.ceil(p) for _, p in main_parts)
    print(f"main content (Parts 1–9): {content:.1f} pages when the parts run on ([layout] part_breaks = false); "
          f"about {used} pages if each part started on a new page")
    return 0


if __name__ == "__main__":
    sys.exit(main())
