"""AQ3 step 7 – error analysis of the chosen model and the rule on the test runs (Table 4.3; Table A.8; PROTOCOL.md P15).

Main operating point: day 27, 5 per 20. Writes
  results/errors_by_run.csv      missed non-completers and listed completers per run, model and rule
  results/errors_by_slice.csv    recall and precision by activity level, previous attempts, late registration, kind, reach
  results/list_overlap.csv       who is on both lists, only the model's, only the rule's – and how they ended
  results/list_stability.csv     how often an enrolment near rank k stays on the list when the run is resampled
"""

import json

import numpy as np
import polars as pl

from aq3_models import EXTRACT, RESULTS, lib

lib.open_test_outcomes("aq-3/code/07_error_analysis.py", "error analysis of the frozen model")
chosen = json.loads(lib.FREEZE_FILE.read_text())["chosen_config"]
cut = 27
d = pl.read_csv(EXTRACT / f"aq3_test_scored_d{cut}.csv")
M, R = f"on_list5_{chosen}", "on_list5_B2_rule"
d = d.with_columns(
    pl.when(pl.col("clicks_0c") == 0).then(pl.lit("none")).when(pl.col("activity_ratio_run") < 0.5).then(pl.lit("low")).otherwise(pl.lit("normal")).alias("activity_level"),
    pl.when(pl.col("num_of_prev_attempts") == 0).then(pl.lit("first attempt")).otherwise(pl.lit("repeat attempt")).alias("attempts"),
    pl.when(pl.col("registration_lead").is_null()).then(pl.lit("registration day missing")).when(pl.col("registration_lead") < 0).then(pl.lit("registered after the start")).otherwise(pl.lit("registered before the start")).alias("registration"),
    (pl.col("date_unregistration").is_not_null() & (pl.col("date_unregistration") > cut) & (pl.col("date_unregistration") <= cut + 7)).alias("withdrew_within_7_days"),
    pl.col("code_module").alias("module"),
)
d = d.with_columns(pl.when(pl.col("withdrew_within_7_days")).then(pl.lit("left within 7 days of the cut-off")).otherwise(pl.lit("reachable")).alias("reach"))

lib.banner(f"Errors by run – day {cut}, 5 per 20, model {chosen} and rule-ranked list")
by_run = d.group_by("run").agg(
    pl.len().alias("n"), pl.col("non_completion").sum().cast(pl.Int64).alias("non_completers"), pl.col(M).sum().cast(pl.Int64).alias("list_length"),
    (pl.col(M) & pl.col("non_completion")).sum().cast(pl.Int64).alias("model_hits"), (pl.col(M) & ~pl.col("non_completion")).sum().alias("model_listed_completers"),
    (~pl.col(M) & pl.col("non_completion")).sum().alias("model_missed"),
    (pl.col(R) & pl.col("non_completion")).sum().cast(pl.Int64).alias("rule_hits"), (~pl.col(R) & pl.col("non_completion")).sum().alias("rule_missed"),
).with_columns((pl.col("model_hits") - pl.col("rule_hits")).alias("model_minus_rule_hits"),
               (pl.col("model_listed_completers") / pl.col("list_length")).alias("share_of_list_completers"),
               (pl.col("non_completers") - pl.col("list_length")).clip(lower_bound=0).alias("missed_even_by_a_perfect_list")).sort("run")
print(lib.md_table(by_run))
lib.save_csv(by_run, RESULTS / "errors_by_run.csv")
tot = by_run.select(pl.col("non_completers").sum(), pl.col("model_hits").sum(), pl.col("model_missed").sum(), pl.col("missed_even_by_a_perfect_list").sum(), pl.col("model_listed_completers").sum(), pl.col("list_length").sum()).row(0)
print(f"\nAll runs: {tot[0]:,} non-completers; the lists hold {tot[5]:,} places; the model lists {tot[1]:,} of them and misses {tot[2]:,}, "
      f"of whom {tot[3]:,} could not be listed by any ranking because their run has more non-completers than places. {tot[4]:,} listed students completed.")

lib.banner("Errors by slice: share of each slice's non-completers on the list (recall) and share of the slice's listed students who did not complete (precision)")
rows = []
for col in ["activity_level", "attempts", "registration", "final_result", "reach", "module", "paired_run", "student_in_training_runs"]:
    for (g,), s in d.group_by([col]):
        nc = s.filter(pl.col("non_completion"))
        if col == "final_result" and nc.height == 0:
            continue
        row = {"slice": col, "group": str(g), "enrolments": s.height, "non_completers": nc.height, "base_rate": nc.height / s.height}
        for tag, flag in (("model", M), ("rule", R)):
            listed = s.filter(pl.col(flag))
            row[f"{tag}_listed"] = listed.height
            row[f"{tag}_selection_rate"] = listed.height / s.height
            row[f"{tag}_recall"] = nc.filter(pl.col(flag)).height / nc.height if nc.height else float("nan")
            row[f"{tag}_precision"] = listed.filter(pl.col("non_completion")).height / listed.height if listed.height else float("nan")
        row["recall_model_minus_rule"] = row["model_recall"] - row["rule_recall"]
        rows.append(row)
sl = pl.DataFrame(rows).sort("slice", "group")
print(lib.md_table(sl))
lib.save_csv(sl, RESULTS / "errors_by_slice.csv")

lib.banner("Who is on which list")
ov = (d.with_columns(pl.when(pl.col(M) & pl.col(R)).then(pl.lit("both lists")).when(pl.col(M)).then(pl.lit("model list only"))
                     .when(pl.col(R)).then(pl.lit("rule list only")).otherwise(pl.lit("neither list")).alias("membership"))
      .group_by("membership").agg(pl.len().alias("enrolments"), pl.col("non_completion").mean().alias("non_completion_rate"),
                                  (pl.col("final_result") == "Withdrawn").mean().alias("share_withdrawn"), (pl.col("final_result") == "Fail").mean().alias("share_fail"),
                                  (pl.col("clicks_0c") == 0).mean().alias("share_no_activity"), pl.col("early_sign_rule").mean().alias("share_flagged_by_rule"),
                                  pl.col("activity_ratio_run").median().alias("median_activity_ratio")).sort("membership"))
print(lib.md_table(ov))
lib.save_csv(ov, RESULTS / "list_overlap.csv")
both = ov.filter(pl.col("membership") == "both lists")["enrolments"][0]
print(f"\nOverlap: {both:,} of {int(d[M].sum()):,} places ({both / int(d[M].sum()):.1%}) are the same enrolments on both lists.")

lib.banner("List stability near rank k (within-run bootstrap of enrolments, 500 replicates)")
rng = np.random.default_rng(lib.SEED)
rows = []
for run in sorted(d["run"].unique().to_list()):
    s = d.filter(pl.col("run") == run)
    n, k = s.height, lib.list_len(s.height, 5)
    rank = lib.rank_desc(s[chosen].to_numpy(), s["tiebreak_u"].to_numpy())
    stay = np.zeros(n)
    for _ in range(500):
        idx = rng.integers(0, n, n)
        edge = np.sort(rank[idx])[k - 1]            # rank of the last listed enrolment in the resampled run
        stay += rank <= edge
    stay /= 500
    rel = (rank - k) / n                            # position relative to the list edge, as a share of the run
    band = np.select([rel < -0.10, rel < -0.05, rel < 0, rel < 0.05, rel < 0.10], ["more than 10% inside", "5–10% inside", "0–5% inside (last places)", "0–5% outside (first not listed)", "5–10% outside"], "more than 10% outside")
    for b_, st in zip(band, stay):
        rows.append({"run": run, "band": b_, "stay": st})
st = pl.DataFrame(rows).group_by("band").agg(pl.len().alias("enrolments"), pl.col("stay").mean().alias("mean_share_of_resamples_on_list"),
                                            pl.col("stay").min().alias("min"), pl.col("stay").max().alias("max"))
order = ["more than 10% inside", "5–10% inside", "0–5% inside (last places)", "0–5% outside (first not listed)", "5–10% outside", "more than 10% outside"]
st = st.with_columns(pl.col("band").replace_strict({b: i for i, b in enumerate(order)}, return_dtype=pl.Int64).alias("o")).sort("o").drop("o")
print(lib.md_table(st))
lib.save_csv(st, RESULTS / "list_stability.csv")
