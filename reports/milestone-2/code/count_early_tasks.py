"""Counts used in the Milestone 2 text that the structural verification does not print: module runs with two or more
non-exam tasks due by day 13 and by day 27 (the early-sign rule needs two missed or late tasks), and how the 32,593
enrolments reduce to the 28,119 still registered on day 14.

Usage: venv/bin/python reports/milestone-2/code/count_early_tasks.py
Reads package/data/raw/{assessments,studentRegistration}.csv (unchanged raw files); prints the counts.
"""
import csv
from collections import Counter
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / "package" / "data" / "raw"

due = Counter()
runs = set()
for r in csv.DictReader(open(RAW / "assessments.csv")):
    run = (r["code_module"], r["code_presentation"])
    runs.add(run)
    if r["assessment_type"] != "Exam" and r["date"] != "":
        due[(run, 13)] += int(r["date"]) <= 13
        due[(run, 27)] += int(r["date"]) <= 27
for day in (13, 27):
    one = sum(due[(run, day)] >= 1 for run in runs)
    two = sum(due[(run, day)] >= 2 for run in runs)
    print(f"runs with >=1 / >=2 non-exam tasks due by day {day}: {one} / {two} of {len(runs)}")

# same definitions as package/src/verify_structure.py: each count is taken on its own, as there
total = before = between = kept = 0
for r in csv.DictReader(open(RAW / "studentRegistration.csv")):
    total += 1
    unreg = r["date_unregistration"]
    if unreg == "" or int(unreg) > 14:
        kept += 1
    elif int(unreg) <= 0:
        before += 1
    else:
        between += 1
print(f"enrolments {total}: unregistered on or before day 0 {before}; unregistered on days 1-14 {between}; "
      f"still registered on day 14 (no unregistration day, or one after day 14) {kept}")
