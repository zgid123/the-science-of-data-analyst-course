"""AQ4 step 2 – quality of the lists against a random list and the rule-ranked list (Level 1 report, Table 4.4).

Writes  results/list_quality_by_run.csv   per run, cut-off, capacity and ranking: recall, attainable recall, normalised recall,
                                          precision, lift, and the random-list expectation
        results/list_quality_pooled.csv   the same pooled over the 13 runs
        results/tiers.csv                 non-completion by tier (top 3 per 20, next 2 per 20, not listed)
        results/outcome_kind_on_list.csv  Fail and Withdrawn among the listed non-completers
        results/overlap_by_run.csv        places shared by the model list and the rule list
        results/active_vs_inactive.csv    students with no activity (whom every list catches) apart from active students
        results/s1_reference.csv          the S1 gate copied from AQ3 (the list's gate is the same test)
"""

import numpy as np
import polars as pl

from aq4_common import AQ3, CHOSEN, EXTRACT, RESULTS, lib

lib.open_test_outcomes("aq-4/code/02_evaluate.py", "AQ4 list quality on the test runs")
rows = []
for cut in (27, 13):
    d = pl.read_csv(EXTRACT / f"aq4_ranked_d{cut}.csv")
    for run in sorted(d["run"].unique().to_list()):
        s = d.filter(pl.col("run") == run)
        y = s["non_completion"].to_numpy().astype(bool)
        for per20 in (5, 3):
            k = lib.list_len(s.height, per20)
            for name in ("model", "rule"):
                m = lib.run_metrics(s[f"rank_{name}"].to_numpy() - 1, y, k)
                rows.append({"cutoff": cut, "per20": per20, "run": run, "ranking": name, **m})
            base = m["base_rate"]
            rows.append({"cutoff": cut, "per20": per20, "run": run, "ranking": "random (expected)", "n": s.height, "non_completers": int(y.sum()),
                         "list_length": k, "non_completers_on_list": k * base, "max_attainable": m["max_attainable"], "base_rate": base,
                         "recall": k / s.height, "attainable_recall": m["attainable_recall"], "normalised_recall": k * base / m["max_attainable"],
                         "precision": base, "lift": 1.0, "random_expected_tp": k * base, "random_expected_nr": k * base / m["max_attainable"]})
q = pl.DataFrame(rows, infer_schema_length=None)
lib.save_csv(q, RESULTS / "list_quality_by_run.csv")
pool = q.group_by("cutoff", "per20", "ranking").agg(pl.col("n").sum().alias("enrolments"), pl.col("non_completers").sum(), pl.col("list_length").sum().alias("list_places"),
                                                    pl.col("non_completers_on_list").sum(), pl.col("max_attainable").sum()).with_columns(
    (pl.col("non_completers_on_list") / pl.col("non_completers")).alias("recall"),
    (pl.col("max_attainable") / pl.col("non_completers")).alias("attainable_recall"),
    (pl.col("non_completers_on_list") / pl.col("max_attainable")).alias("normalised_recall"),
    (pl.col("non_completers_on_list") / pl.col("list_places")).alias("precision"),
    (pl.col("non_completers") / pl.col("enrolments")).alias("base_rate")).with_columns((pl.col("precision") / pl.col("base_rate")).alias("lift")).sort("cutoff", "per20", "ranking", descending=[True, True, False])
lib.banner("AQ4 list quality, pooled over the 13 test runs")
print(lib.md_table(pool))
lib.save_csv(pool, RESULTS / "list_quality_pooled.csv")

main = q.filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5))
w = main.pivot(on="ranking", index=["run", "n", "list_length", "non_completers", "attainable_recall", "base_rate"], values=["recall", "precision", "lift"]).sort("run")
print("\n**Per run, day 27, 5 per 20**\n\n" + lib.md_table(w))

d = pl.read_csv(EXTRACT / "aq4_ranked_d27.csv")
lib.banner("Risk tiers at day 27 (tier 1 = top 3 per 20, tier 2 = next 2 per 20; both cut points come from capacity)")
tiers = []
for name in ("model", "rule"):
    t = d.group_by(f"tier_{name}").agg(pl.len().alias("enrolments"), pl.col("non_completion").sum().alias("non_completers"),
                                      (pl.col("final_result") == "Withdrawn").sum().alias("withdrawn"), (pl.col("final_result") == "Fail").sum().alias("fail")).with_columns(
        (pl.col("non_completers") / pl.col("enrolments")).alias("non_completion_rate"), pl.lit(name).alias("ranking"),
        pl.col(f"tier_{name}").replace_strict({1: "tier 1 (top 3 per 20)", 2: "tier 2 (next 2 per 20)", 0: "not listed"}, return_dtype=pl.Utf8).alias("tier")).sort(f"tier_{name}", descending=True)
    tiers.append(t.select("ranking", "tier", "enrolments", "non_completers", "non_completion_rate", "withdrawn", "fail"))
tiers = pl.concat(tiers)
print(lib.md_table(tiers))
lib.save_csv(tiers, RESULTS / "tiers.csv")

lib.banner("Kind of non-completion on the list, day 27, 5 per 20")
kind = []
for name in ("model", "rule"):
    for res in ("Fail", "Withdrawn"):
        allk = d.filter(pl.col("final_result") == res)
        kind.append({"ranking": name, "final_result": res, "in_test_runs": allk.height, "on_list": allk.filter(pl.col(f"list5_{name}")).height,
                     "recall": allk.filter(pl.col(f"list5_{name}")).height / allk.height})
kind = pl.DataFrame(kind)
print(lib.md_table(kind))
lib.save_csv(kind, RESULTS / "outcome_kind_on_list.csv")

lib.banner("Overlap of the model list with the rule list, day 27, 5 per 20")
ov = d.group_by("run").agg(pl.col("list5_model").sum().alias("list_places"), (pl.col("list5_model") & pl.col("list5_rule")).sum().alias("on_both"),
                           pl.col("early_sign_rule").sum().alias("flagged_by_rule"), pl.len().alias("n")).with_columns(
    (pl.col("on_both") / pl.col("list_places")).alias("overlap_share"), (pl.col("flagged_by_rule") / pl.col("n")).alias("share_flagged_by_rule")).sort("run")
print(lib.md_table(ov))
print(f"\nall runs: {int(ov['on_both'].sum()):,} of {int(ov['list_places'].sum()):,} places shared ({ov['on_both'].sum() / ov['list_places'].sum():.1%})")
lib.save_csv(ov, RESULTS / "overlap_by_run.csv")

lib.banner("Students with no activity at all (every list catches them) apart from active students, day 27, 5 per 20")
d2 = d.with_columns(pl.when(pl.col("clicks_0c") == 0).then(pl.lit("no activity since the start")).otherwise(pl.lit("some activity")).alias("activity"))
act = []
for name in ("model", "rule"):
    for (g,), s in d2.group_by(["activity"]):
        nc = s.filter(pl.col("non_completion"))
        on = s.filter(pl.col(f"list5_{name}"))
        act.append({"ranking": name, "activity": g, "enrolments": s.height, "non_completers": nc.height, "listed": on.height,
                    "share_of_all_list_places": on.height / int(d[f"list5_{name}"].sum()), "recall": nc.filter(pl.col(f"list5_{name}")).height / nc.height,
                    "precision": on.filter(pl.col("non_completion")).height / on.height})
act = pl.DataFrame(act).sort("ranking", "activity")
print(lib.md_table(act))
lib.save_csv(act, RESULTS / "active_vs_inactive.csv")

s1 = pl.read_csv(AQ3 / "results" / "s1_gate.csv")
lib.save_csv(s1, RESULTS / "s1_reference.csv", "copied from aq-3/results/s1_gate.csv")
r = s1.row(0, named=True)
print(f"\nGate S1 (shared with AQ3): model {r['pooled_nr_a']:.4f} against rule {r['pooled_nr_b']:.4f}, difference {r['difference']:+.4f} "
      f"[{r['boot_ci_low']:+.4f}, {r['boot_ci_high']:+.4f}], sign-flip p = {r['signflip_p']:.4f}: {r['verdict']}")
