"""T19 number spot-check: draw a seeded sample of main-text sentences and table rows that state numbers.

Usage: venv/bin/python reports/milestone-5/code/t19_number_sample.py [--n 25] [--seed 20261109]

Pool: the abstract (00-1) and the main-text sections (01-* to 14-*) of report/. Each body sentence and each table
row counts once when it still holds a digit after identifiers are removed (Section/Table/Figure/Appendix
references, AQ1, C15, D1, DQ08, V01, G2a, S1, FR1, B2, citations [n], bare years such as 2013 or
2027–2028, headings). The sample is printed as a
Markdown table with file, line and text, for tracing each number to results/, the baseline, claims or design files.
"""

import argparse
import random
import re
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent / "report"
IDS = re.compile(
    r"(Sections?|Tables?|Figures?|Appendix|Appendices)\s+[A-Z]?[\dIVXL.]+(\s*(–|to|and)\s*[A-Z]?[\dIVXL.]+)?"
    r"|\b(AQ|C|D|DQ|V|G|S|FR|B|KPI)\d+[a-z]?\b|\[\d+(\s*[,–-]\s*\d+)*\]|\bMilestones?\s+\d(\s*(–|to)\s*\d)?"
    r"|\b20\d\d(\s*[–-]\s*20\d\d)?\b|\bLevel\s+\d|\bCircular\s+\d+/\d+|\bdoi:\S+|SHA-256|\bweeks?\s+\d\s+(and|or)\s+\d")


def units(path):
    """Yield (line, text) for body sentences and table rows of one section file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    para, start = [], None
    for i, raw in enumerate(lines + [""], 1):
        s = raw.strip()
        if s.startswith("|"):
            if not re.fullmatch(r"\|[\s:|-]+\|", s) and not s.startswith("| AQ |") and "| :" not in s:
                yield i, s
            continue
        if not s or s.startswith("#") or s.startswith("![") or s.startswith("**Table"):
            if para:
                text = " ".join(para)
                for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z])", text):
                    yield start, sent
            para, start = [], None
            if s.startswith("!["):
                yield i, s
            continue
        if start is None:
            start = i
        para.append(s.lstrip("> "))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=25)
    ap.add_argument("--seed", type=int, default=20261109)
    args = ap.parse_args()
    files = [REPORT / "00-1-abstract.md"] + sorted(
        p for p in REPORT.glob("*.md") if re.match(r"(0[1-9]|1[0-4])-", p.name))
    pool = []
    for f in files:
        for line, text in units(f):
            if re.search(r"\d", IDS.sub("", text)):
                pool.append((f.name, line, text))
    sample = random.Random(args.seed).sample(pool, min(args.n, len(pool)))
    print(f"pool: {len(pool)} numbered units in {len(files)} files; sample: {len(sample)} (seed {args.seed})\n")
    print("| # | File | Line | Sentence or row |\n| :-- | :-- | :-- | :-- |")
    for k, (name, line, text) in enumerate(sample, 1):
        print(f"| {k} | {name} | {line} | {text.replace('|', '/')} |")


if __name__ == "__main__":
    main()
