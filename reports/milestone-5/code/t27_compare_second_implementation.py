"""T27: compare the AQ2 results of this report with the second, separately written implementation of the same
Milestone 4 design (reports/code/aq-2, read only, never modified).

Both implementations fit the Milestone 4 AQ2 model (logistic regression of non-completion on the five signs at day 27,
run fixed effects, background terms, sign x module terms, mutually adjusted average risk difference, verdict of
Table 4.2) on the 2013 runs and the 2014 runs. Their specifications differ in four points, all written in
reports/code/PROTOCOL.md (P16, P17):
  1. low activity is cut at half the run median there (primary) and at the run median here; that implementation also
     reports the run-median cut as a sensitivity row, which is the like-for-like comparison;
  2. the late-TMA sign is defined there only in runs with a TMA due by day 27, and its difference is averaged only over
     the rows of modules with a late-TMA term, which leaves out module CCC in 2014 (9,064 of 12,585 rows); here it is
     averaged over all 12,585 rows of the runs with a task due, CCC rows taking the average-module effect;
  3. background terms log(1 + previous attempts) and log(1 + credits) there, linear terms here;
  4. a module gets its own sign slope there only with at least 20 enrolments with and 20 without the sign.

Writes results/compare/aq2_second_implementation.csv (one row per year and sign: this report's estimate and verdict,
the other implementation's primary and run-median estimates with their verdicts and row counts, and the differences)
and prints the summary used in Appendix XIII.

Usage (from the repository root): venv/bin/python reports/milestone-5/code/t27_compare_second_implementation.py
"""
import sys
from pathlib import Path

import polars as pl

TASK = Path(__file__).resolve().parents[1]
ROOT = TASK.parents[1]
OTHER = ROOT / "reports" / "code" / "aq-2" / "results"
OUT = TASK / "results" / "compare" / "aq2_second_implementation.csv"
SIGNS = {  # this report -> the other implementation (primary name, run-median variant name)
    "missed_task": ("sign_task_missed", "sign_task_missed"),
    "late_tma": ("sign_tma_late", "sign_tma_late"),
    "inactive_last7": ("sign_inactive_last7", "sign_inactive_last7"),
    "low_relative_activity": ("sign_low_activity", "sign_low_activity_median"),
    "no_pre_start_activity": ("sign_no_pre_activity", "sign_no_pre_activity"),
}
MEDIAN_VARIANT = "low activity = below the run median"
POSTHOC_MEDIAN = "post hoc: low activity = below the run median, + log(1 + clicks on days 0-27)"


def main() -> int:
    rows = []
    for y in ["2013", "2014"]:
        own = pl.read_csv(TASK / "results" / y / "aq2_associations.csv")
        own_half = pl.read_csv(TASK / "results" / y / "aq2_sensitivity.csv").filter(
            pl.col("variant") == "below_half_median")
        sens = pl.read_csv(OTHER / f"sensitivity_{y}.csv")
        main_ = sens.filter(pl.col("variant") == "main")
        med = sens.filter(pl.col("variant") == MEDIAN_VARIANT)
        post = sens.filter(pl.col("variant") == POSTHOC_MEDIAN)
        own_post = pl.read_csv(TASK / "results" / y / "aq2_sensitivity_continuous.csv")
        assert main_.height == 5 and med.height == 5, f"{y}: unexpected sensitivity rows"
        for s, (o_main, o_med) in SIGNS.items():
            a = own.filter(pl.col("sign") == s).row(0, named=True)
            h = own_half.filter(pl.col("sign") == s).row(0, named=True)
            b = main_.filter(pl.col("sign") == o_main).row(0, named=True)
            c = med.filter(pl.col("sign") == o_med).row(0, named=True)
            d = post.filter(pl.col("sign") == o_med).row(0, named=True)
            e = own_post.filter((pl.col("sign") == s) & (pl.col("model") != "main model (as reported)")).row(
                0, named=True)
            rows.append(dict(
                year=y, sign=s,
                report_n=a["n"], report_rd_pp=a["rd_adj_mutual_pp"], report_ci_low=a["rd_adj_mutual_ci_low"],
                report_ci_high=a["rd_adj_mutual_ci_high"], report_verdict=a["verdict"],
                report_half_median_rd_pp=h["rd_adj_mutual_pp"],
                other_n=b["n"], other_rd_pp=round(100 * b["adjusted_rd"], 2),
                other_ci_low=round(100 * b["adj_ci_low"], 2), other_ci_high=round(100 * b["adj_ci_high"], 2),
                other_verdict=b["verdict"],
                other_run_median_n=c["n"], other_run_median_rd_pp=round(100 * c["adjusted_rd"], 2),
                other_run_median_verdict=c["verdict"],
                other_posthoc_run_median_rd_pp=round(100 * d["adjusted_rd"], 2),
                other_posthoc_run_median_modules=f'{d["modules_same_direction"]} of {d["modules_defined"]}',
                other_posthoc_run_median_verdict=d["verdict"],
                report_posthoc_rd_pp=e["rd_adj_mutual_pp"],
                report_posthoc_modules=f'{e["modules_same_direction"]} of {e["modules_defined"]}',
                report_posthoc_verdict=e["verdict"],
            ))
    df = pl.DataFrame(rows).with_columns(
        (pl.col("other_rd_pp") - pl.col("report_rd_pp")).round(2).alias("diff_primary_pp"),
        (pl.col("other_run_median_rd_pp") - pl.col("report_rd_pp")).round(2).alias("diff_same_cut_pp"),
        (pl.col("report_verdict") == pl.col("other_verdict")).alias("same_verdict"),
    )
    late = pl.read_csv(OTHER / "late_tma_average_check.csv").row(0, named=True)
    df.write_csv(OUT)
    with pl.Config(tbl_rows=20, tbl_cols=20, tbl_width_chars=250):
        print(df.select("year", "sign", "report_n", "report_rd_pp", "report_verdict", "other_n", "other_rd_pp",
                        "other_verdict", "other_run_median_rd_pp", "diff_primary_pp", "diff_same_cut_pp"))
    same = int(df["same_verdict"].sum())
    print(f"verdicts equal: {same} of {df.height} (both implementations: "
          f"{sorted(set(df['report_verdict']) | set(df['other_verdict']))})")
    nolate = df.filter(pl.col("sign") != "late_tma")
    print(f"max |difference|, primary against primary: {df['diff_primary_pp'].abs().max()} pp; "
          f"without the low-activity sign (different cut): "
          f"{df.filter(pl.col('sign') != 'low_relative_activity')['diff_primary_pp'].abs().max()} pp")
    print(f"max |difference|, same run-median cut: {df['diff_same_cut_pp'].abs().max()} pp; "
          f"without the late-TMA sign: {nolate['diff_same_cut_pp'].abs().max()} pp")
    print(f"late TMA, other implementation: 2013 {df.filter((pl.col('year') == '2013') & (pl.col('sign') == 'late_tma'))['other_rd_pp'][0]} "
          f"pp over {df.filter((pl.col('year') == '2013') & (pl.col('sign') == 'late_tma'))['other_n'][0]} rows; "
          f"2014 {df.filter((pl.col('year') == '2014') & (pl.col('sign') == 'late_tma'))['other_rd_pp'][0]} pp over "
          f"{late['n_support']} of {late['rows_of_runs_with_any_task_due']} rows (CCC's {late['rows_without_a_slope']} "
          f"left out); counted as 0 they would give {round(100 * late['average_if_those_rows_counted_as_0'], 2)} pp")
    print(f"low activity at half the run median: other {df.filter(pl.col('sign') == 'low_relative_activity')['other_rd_pp'].to_list()} "
          f"pp; this report's half-median sensitivity run {df.filter(pl.col('sign') == 'low_relative_activity')['report_half_median_rd_pp'].to_list()} pp")
    print("post hoc continuous-click check, run-median cut (this report | other implementation):")
    for x in df.iter_rows(named=True):
        print(f"  {x['year']} {x['sign']:<22} {x['report_posthoc_rd_pp']:>6} {x['report_posthoc_modules']} "
              f"{x['report_posthoc_verdict']:<22} | {x['other_posthoc_run_median_rd_pp']:>6} "
              f"{x['other_posthoc_run_median_modules']} {x['other_posthoc_run_median_verdict']}")
    print(f"post hoc verdicts equal: {int((df['report_posthoc_verdict'] == df['other_posthoc_run_median_verdict']).sum())}"
          f" of {df.height}")
    print(f"written {OUT.relative_to(ROOT)}")
    return 0 if same == df.height else 1


if __name__ == "__main__":
    sys.exit(main())
