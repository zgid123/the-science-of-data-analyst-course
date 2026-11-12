"""T27: words of prose (outside tables, captions and headings) per changed file, at a git commit and in the working tree.

Usage (from the repository root): venv/bin/python reports/milestone-5/code/t27_prose_words.py [--rev HEAD] [--vi]
"""
import subprocess
import sys
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
FILES = ["11-02-aq1-findings", "11-03-aq2-findings", "16-12-aq1-results", "16-13-aq2-results"]


def words(text: str) -> tuple[int, int]:
    prose = tables = 0
    for line in text.splitlines():
        n = len(line.split())
        if line.startswith("|") or line.startswith("**Table") or line.startswith("**Bảng"):
            tables += n
        elif not line.startswith("#") and not line.startswith("!["):
            prose += n
    return prose, tables


rev = sys.argv[sys.argv.index("--rev") + 1] if "--rev" in sys.argv else "HEAD"
ext = ".vi.md" if "--vi" in sys.argv else ".md"
print(f"{'file':<28} {'prose ' + rev:>12} {'prose now':>10} {'tables ' + rev:>12} {'tables now':>11}")
for f in FILES:
    rel = f"reports/milestone-5/report/{f}{ext}"
    old = subprocess.run(["git", "show", f"{rev}:{rel}"], cwd=TASK.parents[1], capture_output=True, text=True,
                         check=True).stdout
    new = (TASK / "report" / f"{f}{ext}").read_text(encoding="utf-8")
    (po, to), (pn, tn) = words(old), words(new)
    print(f"{f + ext:<28} {po:>12} {pn:>10} {to:>12} {tn:>11}")
