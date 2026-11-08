"""Which OULAD modules define an exam and which have exam results recorded (raw tables, all runs; no outcome used).
Usage: venv/bin/python reports/milestone-5/code/check_exam_modules.py [OULAD_DIR]   (default: datasets/oulad)
"""
import sys
from pathlib import Path
import polars as pl

d = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3] / "datasets" / "oulad"
ex = pl.read_csv(d / "assessments.csv").filter(pl.col("assessment_type") == "Exam")
rec = pl.read_csv(d / "studentAssessment.csv").join(ex.select("id_assessment", "code_module"), on="id_assessment")
print("modules defining an exam:", sorted(ex["code_module"].unique().to_list()))
print("modules with exam results recorded:", sorted(rec["code_module"].unique().to_list()))
