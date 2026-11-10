"""Checks of the AQ1 and AQ2 results on the 2014 runs and on all 22 runs (Change Log C15).

1. The 2014 outcome counts per run and outcome, computed from the prepared enrolment view, equal the counts that
   Milestone 3 published (data/metadata/fig_outcome_by_run.csv), cell by cell.
2. The 22-run totals equal the figures Milestone 3 reported: 32,593 enrolments, 28,061 registered at day 14 and
   54.7% completion among them.
3. The two aggregation paths (prepared view and raw tables) agree in every cell for 2014 and for all 22 runs, and the
   first missed week matches its recount for every enrolment.
4. Each scope's result files hold only its own runs.
5. The AQ2 model of each scope converged.
6. The year comparison reproduces each year's own overall rates (results/2013/aq1_rates.csv, results/2014/aq1_rates.csv).
7. The enrolments registered at day 14 whose student holds another enrolment registered at day 14 in the same
   presentation number 1,382, 12 of them in 2013 runs (Change Log C12).

Usage (from the package folder): python src/analysis/aq_checks_years.py   (run_all.sh step 17). Exit status 1 on any FAIL.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import polars as pl

PKG = Path(__file__).resolve().parents[2]
RES, PROC, META = PKG / "results", PKG / "data" / "processed", PKG / "data" / "metadata"
OUTCOMES = ["Pass", "Distinction", "Fail", "Withdrawn"]
RESULTS: list[tuple[str, str, str]] = []


def check(name: str, expected, observed) -> None:
    ok = expected == observed
    RESULTS.append(("PASS" if ok else "FAIL", name, f"expected {expected}, observed {observed}"))


def main() -> int:
    enr = pl.read_parquet(PROC / "enrolment.parquet")

    # 1. 2014 counts against the counts Milestone 3 published
    pub = pl.read_csv(META / "fig_outcome_by_run.csv").filter(pl.col("code_presentation").str.starts_with("2014"))
    own = (enr.filter(pl.col("year") == 2014).group_by("code_module", "code_presentation", "final_result").len()
           .pivot(on="final_result", index=["code_module", "code_presentation"], values="len").fill_null(0))
    j = pub.join(own, on=["code_module", "code_presentation"], suffix="_own", how="full", coalesce=True)
    cells = sum(int(x[o] == x[f"{o}_own"]) for x in j.iter_rows(named=True) for o in OUTCOMES)
    check("2014 outcome counts per run equal the Milestone 3 published counts (cells)", 13 * 4, cells)

    # 2. 22-run totals
    d14 = enr.filter(pl.col("enrolled_d14"))
    check("22-run enrolments", 32593, enr.height)
    check("22-run enrolments registered at day 14", 28061, d14.height)
    check("22-run completion among them (Milestone 3: 54.7%)", 0.547, round(float(d14["completed"].mean()), 3))
    allj = json.loads((RES / "all_runs" / "aq_results.json").read_text())
    check("results/all_runs day-14 n", 28061, allj["aq1"]["day14_registered"]["n"])

    # 3. two aggregation paths and first missed week, 2014 and all runs
    for scope, n in [("2014", 19064), ("all_runs", 32593)]:
        v = pl.read_csv(RES / scope / "aq1_validation_two_paths.csv")
        check(f"{scope}: prepared view and raw tables agree in every cell", True, bool(v["agree"].all()))
        js = json.loads((RES / scope / "aq_results.json").read_text())
        check(f"{scope}: first missed week equals its recount", f"{n}/{n}", js["aq1"]["validation"]["first_missed_week_agree"])
        check(f"{scope}: AQ2 model converged", True, js["aq2"]["model"]["converged"])

    # 4. scope purity of the result files
    for p in sorted((RES / "2014").glob("aq*")):
        txt = p.read_text()
        check(f"2014/{p.name} holds no 2013 run", False, "2013B" in txt or "2013J" in txt)
    for p in sorted((RES / "2013").glob("aq*")):
        txt = p.read_text()
        check(f"2013/{p.name} holds no 2014 run", False, "2014B" in txt or "2014J" in txt)

    # 6. year comparison against each year's own rates
    yc = pl.read_csv(RES / "compare" / "aq1_year_comparison_computed.csv").filter(pl.col("level") == "overall")
    for scope, col in [("2013", "2013"), ("2014", "2014")]:
        r = pl.read_csv(RES / scope / "aq1_rates.csv").filter(
            (pl.col("level") == "overall") & (pl.col("measure") == "non_completion"))
        for den in ["day14_registered", "all_enrolments"]:
            a = r.filter(pl.col("denominator") == den).row(0, named=True)
            b = yc.filter(pl.col("denominator") == den).row(0, named=True)
            check(f"year comparison {col} {den} equals aq1_rates", (a["events"], a["n"]), (b[f"nc_{col}"], b[f"n_{col}"]))

    # 7. concurrent enrolments (C12)
    # an enrolment counts when the same student holds another enrolment in the same presentation, both registered
    # at day 14 (the count Milestone 3 published; concurrent_runs alone also counts enrolments cancelled earlier)
    c = d14.with_columns(pl.len().over("code_presentation", "id_student").alias("k")).filter(pl.col("k") >= 2)
    check("concurrent enrolments at day 14 (C12: 1,382)", 1382, c.height)
    check("of them in 2013 runs (C12: 12)", 12, c.filter(pl.col("year") == 2013).height)

    width = max(len(x[1]) for x in RESULTS)
    for st, name, txt in RESULTS:
        print(f"{st:4}  {name:<{width}}  {txt}")
    nfail = sum(x[0] == "FAIL" for x in RESULTS)
    print(f"SUMMARY: {len(RESULTS) - nfail} PASS, {nfail} FAIL")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
