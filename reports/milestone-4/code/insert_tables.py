"""Insert appendix tables into a main-text file, verbatim, under a new caption number (full-draft stage).

A marker line {{A.n -> m.k}} in a report file is replaced by the caption and table of Table A.n from the appendix
files (report/10-0*.md), renumbered as Table m.k. Used to bring the brief's template tables and their supporting
tables into the main text without retyping, so their figures stay exactly as verified.

Usage: venv/bin/python reports/milestone-4/code/insert_tables.py report/FILE.md [...]
"""
import re
import sys
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent / "report"


def appendix_tables():
    out = {}
    for f in sorted(REPORT.glob("10-0*.md")):
        if f.name.endswith(".vi.md"):
            continue
        lines = f.read_text().split("\n")
        for i, l in enumerate(lines):
            m = re.match(r"^\*\*Table (A\.\d+)\. (.*)\*\*$", l)
            if m:
                j = i + 2
                while j < len(lines) and lines[j].startswith("|"):
                    j += 1
                out[m.group(1)] = (m.group(2), "\n".join(lines[i + 2:j]))
    return out


def main():
    tables = appendix_tables()
    for name in sys.argv[1:]:
        p = Path(name)
        s = p.read_text()
        for a, new in re.findall(r"\{\{(A\.\d+) -> (\d+\.\d+)\}\}", s):
            title, body = tables[a]
            s = s.replace(f"{{{{{a} -> {new}}}}}", f"**Table {new}. {title}**\n\n{body}")
            print(f"{p.name}: Table {a} -> Table {new} ({len(body.splitlines()) - 2} rows)")
        p.write_text(s)


if __name__ == "__main__":
    main()
