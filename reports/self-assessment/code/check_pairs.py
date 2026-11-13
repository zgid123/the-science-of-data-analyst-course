"""Pair-by-pair check of the self-assessment twins: English source against Vietnamese twin.

For every pair (NN-*.md, NN-*.vi.md) in report order it compares, line by line in document order:
headings (level and number), table captions (number), table rows (count per table) and the numbers each table row and
paragraph carries (Vietnamese decimal comma and thousands dot normalised). Any difference is printed; exit 1 if any.

Usage: venv/bin/python reports/self-assessment/code/check_pairs.py [REPORT_DIR]
"""
import re
import sys
from pathlib import Path

REPORT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "report"
NUM = re.compile(r"\d+(?:[.,]\d+)*")
# Differences reviewed and accepted: (file, kind, row number or None for paragraphs) -> reason.
EXPECTED = {
    ("00-0-title-page.md", "row", 9): "date written 14/11/2026 in Vietnamese (guide section 7)",
    ("00-0-title-page.md", "para", None): "place line 'tháng 11 năm 2026' (guide section 7)",
    ("02-03-assessment-by-criterion.md", "row", 14): "criterion cell quotes the brief's '≥3' verbatim; English writes 'at least three'",
    ("01-00-team-comments.md", "row", 9): "'2013' repeated in the Vietnamese wording of paired and unpaired runs",
}


def norm(tok, vi):
    if vi:                                           # 28.061 -> 28061 ; 45,3 -> 45.3
        if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", tok):
            return tok.replace(".", "")
        return tok.replace(",", ".")
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+", tok):
        return tok.replace(",", "")
    return tok


def units(path, vi):
    """List of (kind, key, numbers) in document order: heading, caption, row, para."""
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            m = re.match(r"(#+)\s*([\d.]*)", s)
            out.append(("heading", f"{m.group(1)} {m.group(2)}", None))
        elif re.match(r"\*\*(Table|Bảng) \d", s):
            out.append(("caption", re.search(r"\d+\.\d+", s).group(), None))
        elif s.startswith("|"):
            if set(s) <= set("|:- "):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            out.append(("row", len(cells), sorted(norm(t, vi) for t in NUM.findall(s))))
        else:
            out.append(("para", None, sorted(norm(t, vi) for t in NUM.findall(s))))
    return out


def main():
    bad = 0
    for en in sorted(p for p in REPORT.glob("*.md") if not p.name.endswith(".vi.md")):
        vi = en.with_name(en.stem + ".vi.md")
        if not vi.exists():
            print(f"MISSING {vi.name}"); bad += 1; continue
        a, b = units(en, False), units(vi, True)
        kinds_a = [(k, key) for k, key, _ in a if k != "para"]
        kinds_b = [(k, key) for k, key, _ in b if k != "para"]
        diffs, notes = [], []
        if kinds_a != kinds_b:
            diffs.append(f"structure differs: {len(kinds_a)} vs {len(kinds_b)} headings/captions/rows")
        rows_a = [n for k, _, n in a if k == "row"]
        rows_b = [n for k, _, n in b if k == "row"]
        for i, (x, y) in enumerate(zip(rows_a, rows_b), 1):
            if x != y:
                why = EXPECTED.get((en.name, "row", i))
                (notes if why else diffs).append(f"table row {i}: numbers EN {x} vs VI {y}" + (f" (expected: {why})" if why else ""))
        pa = sorted(t for k, _, n in a if k == "para" for t in n)
        pb = sorted(t for k, _, n in b if k == "para" for t in n)
        if pa != pb:
            why = EXPECTED.get((en.name, "para", None))
            (notes if why else diffs).append(f"paragraph numbers differ: EN only {sorted(set(pa) - set(pb))}, VI only {sorted(set(pb) - set(pa))}" + (f" (expected: {why})" if why else ""))
        n_rows = len(rows_a)
        print(f"{'FAIL' if diffs else 'PASS'}  {en.name} <-> {vi.name}: {len(kinds_a)} headings/captions/rows, "
              f"{n_rows} table rows compared")
        for d in diffs:
            print(f"      {d}")
        for d in notes:
            print(f"      note {d}")
        bad += bool(diffs)
    print(f"pairs with differences: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
