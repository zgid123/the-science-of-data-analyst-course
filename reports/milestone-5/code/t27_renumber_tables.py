"""T27: renumber the appendix tables after A.30 to make room for the three tables T27 adds.

New order: Appendix XII keeps A.29 and A.30, adds A.31 (February minus October within module), moves the first missed
task by outcome from A.31 to A.32, adds A.33 (first missed task by module) and moves the year comparison from A.32 to
A.34; Appendix XIII moves A.33 to A.35, adds A.36 (number of early signs) and moves A.34-A.36 to A.37-A.39; every later
table moves up by three. Every "A.n" in the report is a table reference (the appendices have no figures), in English and
Vietnamese alike; the map is applied in one pass, so no number is renumbered twice. Also updates the one table reference
in the package's docs/ai_decision_log.md (Table A.43, the AI Decision Log).

Usage (from the repository root): venv/bin/python reports/milestone-5/code/t27_renumber_tables.py [--write]
Without --write it prints the changes per file; it refuses to run twice (stops if any new caption already exists).
"""
import re
import sys
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
MAP = {31: 32, 32: 34, 33: 35, 34: 37, 35: 38, 36: 39}
MAP |= {n: n + 3 for n in range(37, 44)}
PAT = re.compile(r"\bA\.(\d+)\b")


def main() -> int:
    write = "--write" in sys.argv
    files = sorted((TASK / "report").glob("*.md")) + [TASK / "package" / "docs" / "ai_decision_log.md"]
    if any("**Table A.46." in f.read_text(encoding="utf-8") for f in files):
        print("STOP: Table A.46 already exists; the renumbering has been applied")
        return 1
    total = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        changes = []

        def sub(m: re.Match) -> str:
            n = int(m.group(1))
            if n in MAP:
                changes.append(f"A.{n}->A.{MAP[n]}")
                return f"A.{MAP[n]}"
            return m.group(0)

        new = PAT.sub(sub, text)
        if changes:
            total += len(changes)
            print(f"{f.relative_to(TASK)}: {len(changes)} ({', '.join(changes)})")
            if write:
                f.write_text(new, encoding="utf-8")
    print(f"{'written' if write else 'dry run'}: {total} references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
