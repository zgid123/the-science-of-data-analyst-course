"""Freeze the Milestone 1 baseline (brief section 4, step 1): copy its key elements verbatim from the Milestone 1
report and record a SHA-256 of every source file, so later changes to Milestone 1 are visible.

Usage: venv/bin/python reports/milestone-2/code/freeze_baseline.py
Writes reports/milestone-2/research/baseline/m1-baseline.md.
"""
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
M1 = HERE.parents[1] / "milestone-1" / "report"
OUT = HERE.parent / "research" / "baseline" / "m1-baseline.md"
FILES = ["03-01-business-goal.md", "03-02-smart-goal.md", "03-03-kpis.md", "04-01-four-level-questions.md",
         "05-00-analytic-approach.md", "06-01-data-requirements.md", "07-00-decision-value.md",
         "09-00-traceability-matrix.md"]


def block(text, start, stop=None):
    i = text.index(start)
    j = text.index(stop, i) if stop else len(text)
    return text[i:j].strip()


def table(text, caption):
    i = text.index(caption)
    rows = [l for l in text[i:].split("\n")[1:] if l.startswith("|") or not l.strip()]
    out = []
    for l in rows:
        if not l.strip():
            if out:
                break
            continue
        out.append(l)
    return caption + "\n\n" + "\n".join(out)


def main():
    src = {f: (M1 / f).read_text() for f in FILES}
    goal = re.search(r"\*\*(improve successful course completion[^*]+)\*\*", src["03-01-business-goal.md"]).group(1)
    parts = [
        "# Frozen Milestone 1 baseline",
        f"Frozen {datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ} from `reports/milestone-1/report/` by "
        "`code/freeze_baseline.py`. Text below is copied verbatim; any later change to Milestone 1 goes into the "
        "Controlled Change Log.",
        "## Source files (SHA-256)",
        "| File | SHA-256 |\n| :---- | :---- |\n" + "\n".join(
            f"| {f} | {hashlib.sha256((M1 / f).read_bytes()).hexdigest()} |" for f in FILES),
        "## Business Goal", goal,
        "## SMART Goal", block(src["03-02-smart-goal.md"], "> **SMART Goal.**", "\n\n"),
        "## KPIs", block(src["03-03-kpis.md"], "**Primary KPI: course completion rate.**", "\n\nBoth secondary KPIs"),
        "## Analytical questions", block(src["04-01-four-level-questions.md"], "**AQ1 – Descriptive.**",
                                         "\n\n**How the questions connect.**"),
        "## Analytics types and technique families",
        table(src["05-00-analytic-approach.md"], "**Table 5.1. Analytics type, candidate technique family and expected output per question**"),
        "## Preliminary data requirements", table(src["06-01-data-requirements.md"], "**Table 6.1. Preliminary data requirements**"),
        "## Decisions supported", table(src["07-00-decision-value.md"], "**Table 7.1. Decisions supported and their classification**"),
    ]
    OUT.write_text("\n\n".join(parts) + "\n")
    print(f"wrote {OUT.relative_to(HERE.parents[2])}: {len(FILES)} source files hashed")


if __name__ == "__main__":
    main()
