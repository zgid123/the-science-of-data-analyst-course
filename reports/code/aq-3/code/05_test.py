"""AQ3 step 5 – the single test on the 13 runs of 2014 and the S1 gate (Appendix III step 6; Table 4.5).

Order inside this script:
  1. check that every frozen model file still has the SHA-256 recorded at the freeze;
  2. score the blind 2014 feature tables with every frozen model and the rule, and save the scores;
  3. only then open the 2014 outcomes (the access is appended to logs/test-access.md) and join them;
  4. compute the list metrics per run and the S1 gate: M1 against the rule-ranked list, day 27, 5 per 20.

Writes  extracted-datasets/aq3_test_scores_blind_d<c>.csv   scores before any outcome is read
        extracted-datasets/aq3_test_scored_d<c>.csv         scores + outcome + audit and evaluation columns
        results/test_runs.csv, test_pooled.csv, s1_gate.csv, s1_gate_per_run.csv, s1_bootstrap.csv,
        results/test_context_vs_rule.csv                    every other ranking against the rule (context only)
"""

import json

import joblib
import numpy as np
import polars as pl

from aq3_models import CONFIGS, EXTRACT, MODELS, RESULTS, gate, lib, metrics_rows, pooled, predict, rule_score

freeze = json.loads(lib.FREEZE_FILE.read_text())
chosen = freeze["chosen_config"]
lib.banner(f"AQ3 single test – frozen {freeze['frozen_utc']}, chosen configuration {chosen}")

# 1 -- model files unchanged since the freeze ------------------------------------------------------------
for name, rec in freeze["models"].items():
    got = lib.sha256(MODELS / f"frozen_{name}.joblib")
    assert got == rec["sha256"], f"{name}: model file changed after the freeze"
print(f"{len(freeze['models'])} frozen model files match their SHA-256 at the freeze: PASS")

# 2 -- score the blind tables ------------------------------------------------------------------------------
names = list(CONFIGS) + [f"{chosen}_labels_available"]
for cut in (27, 13):
    blind = pl.read_csv(EXTRACT / f"aq3_test_features_blind_d{cut}.csv")
    assert "non_completion" not in blind.columns and "final_result" not in blind.columns
    sc = blind.select(lib.KEYS + ["run", "start_month", "paired_run", "student_in_training_runs", "tiebreak_u"]).with_columns(pl.Series("B2_rule", rule_score(blind)))
    cma_signs = (blind["rule_missed"].cast(pl.Int64) + blind["rule_tma_late"].cast(pl.Int64) + blind["inactive_last7"].cast(pl.Int64)
                 + ((blind["cma_late_c"] >= 1) & ~blind["rule_tma_late"]).cast(pl.Int64)).to_numpy()
    sc = sc.with_columns(pl.Series("B2_rule_cma", cma_signs + 0.999 / (1 + blind["activity_ratio_run"].to_numpy())))
    for name in names:
        bundle = joblib.load(MODELS / f"frozen_{name}_d{cut}.joblib")
        sc = sc.with_columns(pl.Series(name, predict(bundle, blind)))
    lib.save_csv(sc, EXTRACT / f"aq3_test_scores_blind_d{cut}.csv", "scores written before any 2014 outcome is read")

# 3 -- open the outcomes -----------------------------------------------------------------------------------
metrics = []
for cut in (27, 13):
    full = lib.load_features(cut, "test", "aq-3/code/05_test.py", f"single test of the frozen models, day {cut}")
    enr = lib.load_view("enrolment", (2014,), "aq-3/code/05_test.py", "withdrawal day for the reach analysis").select(lib.KEYS + ["date_unregistration", "date_registration"])
    extra = full.select(lib.KEYS + lib.OUTCOME_COLS + lib.AUDIT_COLS + ["early_sign_rule", "rule_missed", "rule_tma_late", "inactive_last7", "clicks_0c",
                                                                      "activity_ratio_run", "num_of_prev_attempts", "registration_lead", "tasks_due_c"])
    sc = pl.read_csv(EXTRACT / f"aq3_test_scores_blind_d{cut}.csv").join(extra, on=lib.KEYS, how="left", validate="1:1").join(enr, on=lib.KEYS, how="left", validate="1:1")
    assert sc["non_completion"].null_count() == 0
    for col in ["B2_rule", chosen]:                       # list membership at the main capacity, for later steps
        flag = np.zeros(sc.height, bool)
        for run in sc["run"].unique().to_list():
            m = (sc["run"] == run).to_numpy()
            rank = lib.rank_desc(sc[col].to_numpy()[m], sc["tiebreak_u"].to_numpy()[m])
            flag[np.flatnonzero(m)[rank < lib.list_len(int(m.sum()), 5)]] = True
        sc = sc.with_columns(pl.Series(f"on_list5_{col}", flag))
    lib.save_csv(sc.sort(lib.KEYS), EXTRACT / f"aq3_test_scored_d{cut}.csv", "test scores with outcomes")
    metrics.append(metrics_rows(sc, {"B2_rule": "B2_rule", **{c: c for c in CONFIGS}}, cut))
metrics = pl.concat(metrics)
lib.save_csv(metrics, RESULTS / "test_runs.csv")
pool = pooled(metrics)
lib.save_csv(pool, RESULTS / "test_pooled.csv")
print("\n**Test, pooled over the 13 runs of 2014**\n\n" + lib.md_table(pool.select(
    "cutoff", "per20", "ranking", "enrolments", "non_completers", "list_length", "non_completers_on_list", "max_attainable",
    "pooled_normalised_recall", "random_list_normalised_recall", "pooled_recall", "pooled_precision", "base_rate", "max_attainable_precision", "pooled_lift")))

# 4 -- the S1 gate -------------------------------------------------------------------------------------------
lib.banner("S1 gate: chosen model against the rule-ranked list, all 13 test runs, all eligible enrolments, day 27, 5 per 20")
d27 = pl.read_csv(EXTRACT / "aq3_test_scored_d27.csv")
g = gate(d27, chosen, "B2_rule", 5)
s = g["summary"]
print(lib.md_table(g["per_run"].select("run", "n", "list_length", "non_completers", "max_attainable", pl.col("tp_a").alias("model_on_list"),
                                       pl.col("tp_b").alias("rule_on_list"), pl.col("nr_a").alias("model_nr"), pl.col("nr_b").alias("rule_nr"), "difference")))
print(f"""
| Quantity | Value |
| :---- | :---- |
| Pooled normalised recall, model ({chosen}) | {s['pooled_nr_a']:.4f} ({s['tp_a']:,} of {s['max_attainable']:,}); bootstrap 95% interval {s['ci_a_low']:.4f} to {s['ci_a_high']:.4f} |
| Pooled normalised recall, rule-ranked list | {s['pooled_nr_b']:.4f} ({s['tp_b']:,} of {s['max_attainable']:,}); bootstrap 95% interval {s['ci_b_low']:.4f} to {s['ci_b_high']:.4f} |
| Difference (model − rule) | {s['difference']:+.4f} = {s['tp_a'] - s['tp_b']:+,} non-completers on lists of {s['list_places']:,} places |
| 95% paired two-level bootstrap interval of the difference | {s['boot_ci_low']:+.4f} to {s['boot_ci_high']:+.4f} ({lib.B_BOOT:,} replicates; share of replicates ≤ 0: {s['boot_share_diff_le_0']:.4f}) |
| Sign-flip test on the 13 per-run differences, one-sided | p = {s['signflip_p']:.4f} ({s['signflip_count']:,} of {s['signflip_total']:,} sign assignments) |
| Wins / ties / losses of the model over runs | {s['wins']} / {s['ties']} / {s['losses']} |
| Unweighted mean of per-run differences | {s['mean_per_run_difference']:+.4f} |
| Same point estimates with exact ties broken in expectation | model {s['pooled_nr_a_expected_ties']:.4f}, rule {s['pooled_nr_b_expected_ties']:.4f} |
| **S1 verdict** | **{'PASS' if s['passes'] else 'NOT MET'}** (needs difference > 0, interval above 0 and p < 0.05) |
""")
lib.save_csv(pl.DataFrame([{**s, "model": chosen, "comparison": "B2_rule", "verdict": "PASS" if s["passes"] else "NOT MET"}]), RESULTS / "s1_gate.csv")
lib.save_csv(g["per_run"], RESULTS / "s1_gate_per_run.csv")
lib.save_csv(pl.DataFrame({"model_nr": g["boot"]["boot_a"], "rule_nr": g["boot"]["boot_b"], "difference": g["boot"]["diff"]}), RESULTS / "s1_bootstrap.csv")

# context: every other ranking against the rule, and the model against the background-only baseline ------------
lib.banner("Context only (cannot change the verdict): other rankings against the rule, day 27, 5 per 20")
rows = []
for a, b in [("B3", "B2_rule"), ("M2", "B2_rule"), ("M3", "B2_rule"), ("M4", "B2_rule"), (chosen, "B3"), ("M3", chosen), ("M2", chosen), ("M4", chosen)]:
    r = gate(d27, a, b, 5)["summary"]
    rows.append({"ranking_a": a, "ranking_b": b, **{k: r[k] for k in ["pooled_nr_a", "pooled_nr_b", "difference", "boot_ci_low", "boot_ci_high", "signflip_p", "wins", "ties", "losses"]}})
ctx = pl.DataFrame(rows)
print(lib.md_table(ctx, digits=4))
lib.save_csv(ctx, RESULTS / "test_context_vs_rule.csv")
