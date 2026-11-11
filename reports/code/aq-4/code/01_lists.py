"""AQ4 step 1 – form the ranked contact lists per test run from the frozen AQ3 scores, with reasons.

List length: 3 or 5 contacts per tutor group of 20 (k = per20 x ceil(n / 20)); tier 1 = the top 3 per 20, tier 2 = the
next 2 per 20 (Level 1 report, Section 3.4). Reasons come from the same frozen logistic equation that ranks the
students: for each listed student, the three predictors that push the risk up most, measured as coefficient x
standardised value. Module and start month are left out of the reasons because they are the same for everyone in a run.

Writes  extracted-datasets/aq4_ranked_d<c>.csv        every test enrolment with ranks, list flags and tiers (model and rule)
        extracted-datasets/aq4_contact_list_d27.csv   the list a tutor would receive at day 27 (5 per 20) with reasons;
                                                      the outcome columns at the end are for evaluation only
        results/reason_frequency.csv                  how often each predictor is a student's first reason
"""

import joblib
import numpy as np
import polars as pl

from aq4_common import AQ3, CHOSEN, EXTRACT, RESULTS, add_ranks, lib, scored

lib.open_test_outcomes("aq-4/code/01_lists.py", "AQ4 lists formed from the frozen scores (outcomes kept for evaluation columns)")
LABEL = {
    "tasks_missed_c": "task(s) due and not submitted", "tma_late_c": "TMA submitted late", "tasks_late_c": "task(s) submitted late",
    "cma_late_c": "CMA submitted late", "tasks_due_c": "task(s) already due in this run", "inactive_last7": "no platform activity in the last 7 days",
    "active_days_0c": "few active days since the start", "clicks_0c": "few clicks since the start", "sites_0c": "few resources opened",
    "activity_ratio_run": "activity below the run median", "clicks_pre": "little activity before the start", "highest_education": "lower prior education",
    "num_of_prev_attempts": "previous attempt(s) at this module", "studied_credits": "high credit load", "registration_lead": "registration timing",
    "banked_results": "banked results", "cma_marked_c": "few CMA marks so far",
}
for cut in (27, 13):
    d = add_ranks(add_ranks(scored(cut), CHOSEN, "model"), "B2_rule", "rule")
    lib.save_csv(d.sort("run", "rank_model"), EXTRACT / f"aq4_ranked_d{cut}.csv", "all test enrolments with ranks and tiers")
    for per20 in (3, 5):
        assert int(d[f"list{per20}_model"].sum()) == int(d[f"list{per20}_rule"].sum()) == sum(lib.list_len(n, per20) for n in d.group_by("run").len()["len"])

cut = 27
d = pl.read_csv(EXTRACT / f"aq4_ranked_d{cut}.csv")
bundle = joblib.load(AQ3 / "results" / "models" / f"frozen_{CHOSEN}_d{cut}.joblib")
blind = pl.read_csv(AQ3 / "extracted-datasets" / f"aq3_test_features_blind_d{cut}.csv")
prep, model = bundle["prep"], bundle["model"]
Z = prep.transform(blind)
contrib = Z * model.coef_[0]
names = prep.names
use = [i for i, n in enumerate(names) if not n.startswith("code_module[") and not n.startswith("start_month[")]
top = np.argsort(-contrib[:, use], axis=1)[:, :3]
reasons = []
for i in range(blind.height):
    out = []
    for j in top[i]:
        col = names[use[j]]
        val = contrib[i, use[j]]
        if val <= 0:
            break
        raw = blind[col][i]
        out.append(f"{LABEL.get(col, col)} ({col} = {raw}; +{val:.2f})")
    reasons.append(out + [""] * (3 - len(out)))
r = blind.select(lib.KEYS).with_columns(pl.Series("reason_1", [x[0] for x in reasons]), pl.Series("reason_2", [x[1] for x in reasons]),
                                        pl.Series("reason_3", [x[2] for x in reasons]),
                                        pl.Series("first_reason_column", [names[use[t[0]]] if contrib[i, use[t[0]]] > 0 else "none" for i, t in enumerate(top)]))
lst = (d.filter(pl.col("list5_model")).join(r, on=lib.KEYS, how="left", validate="1:1")
       .select("run", pl.col("rank_model").alias("rank"), pl.col("tier_model").alias("tier"), "id_student", pl.col(CHOSEN).alias("risk_score"),
               "reason_1", "reason_2", "reason_3", "first_reason_column", pl.col("list5_rule").alias("also_on_rule_list"),
               "rule_missed", "rule_tma_late", "inactive_last7", "clicks_0c", "activity_ratio_run",
               pl.col("final_result").alias("EVALUATION_ONLY_final_result"), pl.col("non_completion").alias("EVALUATION_ONLY_non_completion"))
       .sort("run", "rank"))
lib.save_csv(lst, EXTRACT / "aq4_contact_list_d27.csv", "day-27 list, 5 per 20, with reasons")
lib.banner("AQ4 contact list, day 27, 5 per 20 – first rows of one run (risk score shown as fitted; outcome columns are evaluation only)")
print(lib.md_table(lst.filter(pl.col("run") == "FFF-2014J").select("run", "rank", "tier", "id_student", "risk_score", "reason_1", "reason_2", "also_on_rule_list").head(8)))
freq = lst.group_by("first_reason_column").agg(pl.len().alias("listed_students"), pl.col("EVALUATION_ONLY_non_completion").mean().alias("non_completion_rate")).with_columns(
    (pl.col("listed_students") / lst.height).alias("share_of_list")).sort("listed_students", descending=True)
print("\n**First reason of the listed students**\n\n" + lib.md_table(freq))
lib.save_csv(freq, RESULTS / "reason_frequency.csv")
print(f"\nlisted: {lst.height:,} places in {lst['run'].n_unique()} runs; with at least one reason: {lst.filter(pl.col('reason_1') != '').height:,}")
