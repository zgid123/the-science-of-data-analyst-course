"""Count the raw submissions of OULAD by assessment type and banked flag (Section 6.1, step 7).

Step 7 of the pipeline places every TMA and CMA submission on an enrolment-task row; this count shows what the other
rows of studentAssessment are.
Usage: venv/bin/python reports/milestone-3/code/count_submission_types.py
"""
from pathlib import Path

import polars as pl

RAW = Path(__file__).resolve().parent.parent / "package" / "data" / "raw"
sa = pl.read_csv(RAW / "studentAssessment.csv", null_values=["", "?"])
a = pl.read_csv(RAW / "assessments.csv", null_values=["", "?"])
d = sa.join(a, on="id_assessment", how="left")
t = d.group_by(["assessment_type", "is_banked"]).len().sort(["assessment_type", "is_banked"])
print(t)
tasks = d.filter(pl.col("assessment_type").is_in(["TMA", "CMA"])).height
print(f"all submissions {d.height:,}; TMA and CMA (banked included) {tasks:,}; exam {d.height - tasks:,}")
