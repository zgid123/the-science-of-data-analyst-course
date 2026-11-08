"""Measure the main content of a built report in pages: from the heading of Part 1 to the reference list.

The brief counts 8–12 pages of main content, without front matter, appendices, code and data (section 16). This uses
the build-report estimator's geometry (estimate_pages.py) but splits its "body" into front matter (contents, lists,
abbreviations, glossary) and main content (Parts 1 to 10).

Usage: venv/bin/python reports/milestone-4/code/measure_pages.py reports/milestone-4/build/N04_Milestone4_EN.docx
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / ".claude" / "skills" / "build-report" / "scripts"))
import estimate_pages as ep  # noqa: E402
from docx import Document  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.table import Table  # noqa: E402
from docx.text.paragraph import Paragraph  # noqa: E402


def measure(path, char_width=0.45):
    doc = Document(path)
    body_size = ep.font_size(next((p for p in doc.paragraphs if p.style.name == "Body Text"), doc.paragraphs[0]), 12)
    spacing = doc.styles["Body Text"].paragraph_format.line_spacing or 1.3
    h = {"front": 0.0, "main": 0.0, "back": 0.0}
    per = {}
    part, cur = "front", None
    for el in doc.element.body:
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc)
            if p.style.name.startswith("Heading 1"):
                t = p.text.strip().lower()
                if t.startswith(("references", "tài liệu tham khảo")):
                    part = "back"
                elif t[:2] in ("1.", "1 ") and part == "front":
                    part = "main"
                if part == "main":
                    cur = p.text.strip()[:40]
            x = 0.0
            ext = el.findall(".//" + qn("wp:extent"))
            if ext:
                x += max(int(e.get("cy")) for e in ext) / 12700.0 + 12
            size = ep.font_size(p, body_size)
            n = ep.line_count(p.text, size, ep.TEXT_W_PT, char_width)
            if n:
                after = p.paragraph_format.space_after.pt if p.paragraph_format.space_after is not None else 6
                x += n * size * (1.1 if p.style.name.startswith("Heading") else spacing) * 1.15 + after
                x += 16 if p.style.name.startswith("Heading") else 0
            h[part] += x
            if part == "main":
                per[cur] = per.get(cur, 0) + x
        elif el.tag == qn("w:tbl"):
            grid = [int(g.get(qn("w:w"))) / 20.0 for g in el.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
            total = 0.0
            for row in Table(el, doc).rows:
                tallest = 0.0
                for cell, w in zip(row.cells, grid):
                    size = next((r.font.size.pt for cp in cell.paragraphs for r in cp.runs if r.font.size), 9.5)
                    n = sum(ep.line_count(cp.text, size, max(w - 10, 20), char_width) for cp in cell.paragraphs)
                    tallest = max(tallest, n * size * 1.05 * 1.15 + 4)
                total += tallest
            h[part] += total + 12
            if part == "main":
                per[cur] = per.get(cur, 0) + total + 12
    out = {k: v / ep.TEXT_H_PT for k, v in h.items()}
    out["parts"] = {k: round(v / ep.TEXT_H_PT, 2) for k, v in per.items()}
    return out


if __name__ == "__main__":
    for f in sys.argv[1:]:
        m = measure(f)
        print(f"{Path(f).name}: front matter {m['front']:.1f} | main content (Parts 1–end) {m['main']:.1f} | "
              f"references and appendices {m['back']:.1f} pages (estimate)")
        for k, v in m["parts"].items():
            print(f"   {v:5.2f}  {k}")
