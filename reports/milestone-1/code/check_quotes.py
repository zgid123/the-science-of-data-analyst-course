"""Check that every quoted fragment in an interview table occurs verbatim in its transcript.

Usage: venv/bin/python reports/milestone-1/code/check_quotes.py [table.md ...]
Default table: research/interviews/key-statements.md. Rows: | ID | Role | ... | "quote" | ...; the role code (PM, CL,
AD, ST, DO, or V-prefixed IDs for validation) selects the transcript. Exit 1 on any missing quote.
"""
import re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "research" / "interviews"
FILES = {"PM": "program-manager", "CL": "lecturer", "AD": "advisor", "ST": "student", "DO": "data-officer"}

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace('\\"', '"')
    return re.sub(r"\s+", " ", s).strip()

def main(tables):
    bad = n = 0
    for t in tables:
        for line in Path(t).read_text().splitlines():
            m = re.match(r"\| (V?[A-Z]{2}\d+) \| (\w\w) \|", line)
            if not m:
                continue
            role = m.group(2)
            src = BASE / ("validation" if m.group(1).startswith("V") else "transcripts") / f"{FILES[role]}.md"
            text = norm(src.read_text())
            for q in re.findall(r'\| "((?:[^"\\]|\\")+)" \|', line):
                n += 1
                if norm(q) not in text:
                    bad += 1
                    print(f"MISSING {m.group(1)} in {src.name}: {q[:70]}")
    print(f"checked {n} quotes: {bad} missing")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or [BASE / "key-statements.md"]))
