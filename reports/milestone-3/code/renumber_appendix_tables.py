"""Shift appendix table numbers (A.n) by a fixed amount from a given number on, in every place that writes them:
the report sections in both languages, the moved-block sources in research/appendix/ and the appendix generator.
Used when a table moves into an appendix ahead of later appendix tables (docs/appendix-move-brief.md, rule 5).

Usage: venv/bin/python reports/milestone-3/code/renumber_appendix_tables.py --start 13 --by 1 [--write]
Without --write it lists every change it would make.
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = sorted((ROOT / "report").glob("*.md")) + sorted((ROOT / "research" / "appendix").glob("*.md")) \
    + [ROOT / "code" / "build_appendices.py"]
# "A.n" as a table or figure label: not part of a longer token such as a version string.
PAT = re.compile(r"(?<![\w.])A\.(\d+)(?![\d])")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, required=True)
    ap.add_argument("--by", type=int, required=True)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    total = 0
    for f in FILES:
        text = f.read_text()
        hits = []

        def sub(m):
            n = int(m.group(1))
            if n < args.start:
                return m.group(0)
            ctx = text[max(0, m.start() - 12):m.start()]
            if "Figure" in ctx or "Hình" in ctx:          # figures are numbered separately
                return m.group(0)
            hits.append(f"A.{n} -> A.{n + args.by}")
            return f"A.{n + args.by}"

        new = PAT.sub(sub, text)
        if hits:
            total += len(hits)
            print(f"{f.relative_to(ROOT)}: {', '.join(hits)}")
            if args.write:
                f.write_text(new)
    print(f"{total} change(s){'' if args.write else ' (dry run)'}")


if __name__ == "__main__":
    main()
