"""T26: why fewer non-completers missed a task by week 4 in 2014 than in 2013 (Appendix XII). Day-14 non-completers per
year: share in the EEE and GGG runs (no task due by day 27 in any of their runs) and the share with a missed task by
week 4 within the other runs.
Usage (from the repository root): venv/bin/python reports/milestone-5/code/t26_week4_composition.py
"""
import sys
from pathlib import Path

import polars as pl

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "package" / "src" / "analysis"))
import aq_analysis as A  # noqa: E402

e = pl.read_parquet(A.PROC / "enrolment.parquet").filter(pl.col("enrolled_d14") & pl.col("non_completion"))
for y in (2013, 2014):
    d = e.filter(pl.col("year") == y)
    nt = d.filter(pl.col("code_module").is_in(["EEE", "GGG"]))
    w = d.filter(~pl.col("code_module").is_in(["EEE", "GGG"]))
    print(f"{y}: non-completers {d.height}; in EEE/GGG {nt.height} ({100 * nt.height / d.height:.1f}%); "
          f"missed a task by week 4 within the other runs {int((w['first_missed_week'] <= 4).sum())} of {w.height} "
          f"({100 * (w['first_missed_week'] <= 4).sum() / w.height:.1f}%)")
