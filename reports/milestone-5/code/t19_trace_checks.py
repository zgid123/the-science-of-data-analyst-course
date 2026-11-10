"""T19 trace checks: recount the task-due runs that the main text states without a results file.

Usage: venv/bin/python reports/milestone-5/code/t19_trace_checks.py [path/to/assessments.csv]

Default input: datasets/oulad/assessments.csv of the repository. Prints the runs with a TMA or CMA (exam excluded)
due on or before day 13 and day 27, and how many of them are 2013 runs (Sections 5 and 6.1).
"""

import sys
from pathlib import Path

import pandas as pd

default = Path(__file__).resolve().parents[3] / "datasets" / "oulad" / "assessments.csv"
path = Path(sys.argv[1]) if len(sys.argv) > 1 else default
a = pd.read_csv(path)
a = a[a.assessment_type != "Exam"].assign(date=lambda d: pd.to_numeric(d.date, errors="coerce"))
runs_all = a.groupby(["code_module", "code_presentation"]).ngroups
for day in (13, 27):
    runs = sorted(a[a.date <= day].groupby(["code_module", "code_presentation"]).groups)
    n2013 = sum(p.startswith("2013") for _, p in runs)
    print(f"day {day}: task due in {len(runs)} of {runs_all} runs ({n2013} of them in 2013): "
          + ", ".join(f"{m} {p}" for m, p in runs))
