"""Stage 5 - cross-check: independent recount of the gender Simpson's-paradox result in results/descriptive.json
(simpson["female_vs_male:withdrawn"]), computed straight from the raw studentInfo.csv without stages 1-3.

Run from the repository root: venv/bin/python datasets/oulad/exploration/code/05_crosscheck.py
Prints only; run_all.sh keeps the output in logs/.
"""

from __future__ import annotations

import polars as pl

from common import DATA

si = pl.read_csv(DATA / "studentInfo.csv")
w = si.with_columns((pl.col("final_result") == "Withdrawn").alias("w"))
print("crude withdrawal rate by gender:", w.group_by("gender").agg(pl.col("w").mean().round(4)).sort("gender").rows())
per = w.group_by(["code_module", "gender"]).agg(pl.col("w").mean().round(4)).sort(["code_module", "gender"])
print(per.pivot(on="gender", index="code_module", values="w")
      .with_columns(((pl.col("F") - pl.col("M")) * 100).round(2).alias("gap_pp")))
print(w.group_by("code_module").agg(pl.col("w").mean().round(4).alias("module_withdrawal"),
                                    (pl.col("gender") == "F").mean().round(3).alias("female_share")).sort("code_module"))
