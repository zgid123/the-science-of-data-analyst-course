"""AQ4 (prescriptive ranking, decision support): who tops a list of fixed capacity, with what gain, reasons and fairness.

Reads the saved day-27 test scores of the chosen frozen model; fits nothing.
"""

import json
import pickle

import _tools  # noqa: F401
import numpy as np
import pandas as pd
from holdout_guard import open_holdout
from stats_helpers import wilson_ci

import common as c
import models as m  # noqa: F401

open_holdout(c.FREEZE, c.ACCESS, who="08_aq4_lists.py", why="AQ4 lists, yield, reasons and fairness from saved scores")
CHOSEN = json.loads((c.RESULTS / "aq3_choices.json").read_text())["chosen_configuration"]
rng = np.random.default_rng(c.SEED + 4)

s = pd.read_csv(c.SCORES / "test_scores_d27.csv")
feat = c.features(27)
test = feat[feat["year"] == 2014].reset_index(drop=True)
d = s.merge(test[c.KEY + ["gender", "age_band", "disability", "imd_band", "final_result"]], on=c.KEY, validate="1:1")
d = d.merge(c.enrolment()[c.KEY + ["date_unregistration"]], on=c.KEY, validate="1:1")
d["G"] = d.groupby("run")["run"].transform(lambda x: int(np.ceil(len(x) / 20)))
d["rank"] = c.rank_in_run(d, CHOSEN)
d["rank_rule"] = c.rank_in_run(d, "rule")
d["k5"] = d.groupby("run")["run"].transform(lambda x: c.list_size(len(x), 5))
d["on_list"] = d["rank"] <= d["k5"]

# ------------------------------------------------------------------ yield of each extra contact per tutor group
yld = []
for j in range(1, 11):
    for name, col in [("model", "rank"), ("rule", "rank_rule")]:
        band = d[(d[col] > (j - 1) * d["G"]) & (d[col] <= j * d["G"])]
        p, lo, hi = wilson_ci(int(band["y"].sum()), len(band))
        yld.append({"contact": j, "method": name, "students": len(band), "non_completers": int(band["y"].sum()),
                    "precision": p, "low": lo, "high": hi, "base_rate": d["y"].mean()})
yld = pd.DataFrame(yld)
c.write(yld, "aq4_contact_yield.csv")

# ------------------------------------------------------------------ list summary at 3 and 5 per 20, against baselines
summ = []
for per20 in (3, 5):
    for meth in [CHOSEN, "rule"]:
        p = c.pooled(c.list_metrics(d, meth, per20))
        summ.append({"per20": per20, "method": "model" if meth == CHOSEN else "rule", **p})
    r = c.list_metrics(d, "rule", per20)
    tp = (r["k"] * r["positives"] / r["n"]).sum()
    summ.append({"per20": per20, "method": "random (expected)", "n": int(r["n"].sum()), "k": int(r["k"].sum()),
                 "positives": int(r["positives"].sum()), "tp": tp, "attainable": int(r["attainable"].sum()),
                 "norm_recall": tp / r["attainable"].sum(), "recall": tp / r["positives"].sum(),
                 "precision": tp / r["k"].sum(), "lift": 1.0})
summ = pd.DataFrame(summ)
c.write(summ, "aq4_list_summary.csv")

# reachability: listed non-completers who leave in the week the list is delivered (days 28–34)
listed = d[d["on_list"]]
reach = {"listed": len(listed), "listed_non_completers": int(listed["y"].sum()),
         "withdrew_days_28_34": int((listed["final_result"].eq("Withdrawn") & listed["date_unregistration"].between(28, 34)).sum()),
         "listed_fail": int(listed["final_result"].eq("Fail").sum()),
         "listed_withdrawn": int(listed["final_result"].eq("Withdrawn").sum())}
reach["reachable_non_completers"] = reach["listed_non_completers"] - reach["withdrew_days_28_34"]
c.write(pd.DataFrame([reach]), "aq4_reach.csv")

# ------------------------------------------------------------------ reasons shown beside each name (logistic model)
REASON = {"tasks_missed_c": "Missed a task", "tasks_late_c": "Late submission",
          "tma_late_c": "Late submission", "cma_late_c": "Late submission", "cma_marked_c": "Few marked quizzes",
          "clicks_0c": "Low activity", "active_days_0c": "Low activity", "sites_0c": "Low activity",
          "activity_ratio_run": "Low activity", "inactive_last7": "Inactive last 7 days",
          "clicks_pre": "No activity before start", "num_of_prev_attempts": "Previous attempt",
          "studied_credits": "Study load", "registration_lead": "Late registration",
          "banked_results": "Previous attempt", "highest_education": "Prior education"}
with open(c.MODELS / f"{CHOSEN}_d27.pkl", "rb") as fh:
    model = pickle.load(fh)
if model.kind == "logistic":
    x = test.set_index(c.KEY).loc[pd.MultiIndex.from_frame(d[c.KEY])].reset_index()
    contrib = model.contributions(x)
    grouped = pd.DataFrame(index=contrib.index)
    for col in contrib.columns:
        base = col.replace("_missing", "")
        reason = REASON.get(base, "Course context")
        grouped[reason] = grouped.get(reason, 0) + contrib[col]
    grouped = grouped.drop(columns=["Course context"], errors="ignore")
    d["top_reason"] = grouped.idxmax(axis=1).where(grouped.max(axis=1) > 0, "No single reason")
    d["second_reason"] = grouped.apply(lambda r: r.nlargest(2).index[1] if r.nlargest(2).iloc[1] > 0 else "", axis=1)
    rs = []
    for reason, g in d[d["on_list"]].groupby("top_reason"):
        p, lo, hi = wilson_ci(int(g["y"].sum()), len(g))
        rs.append({"top_reason": reason, "listed": len(g), "share_of_list": len(g) / d["on_list"].sum(),
                   "non_completers": int(g["y"].sum()), "rate": p, "low": lo, "high": hi})
    c.write(pd.DataFrame(rs).sort_values("listed", ascending=False), "aq4_reasons.csv")
    coef = pd.DataFrame({"predictor": model.prep.names(), "coefficient_per_sd": model.est.coef_[0]})
    coef["reason"] = [REASON.get(n.replace("_missing", ""), "Course context") for n in coef["predictor"]]
    c.write(coef.sort_values("coefficient_per_sd", key=abs, ascending=False), "aq3_coefficients.csv")
    # an anonymised example of what a tutor would see: the first five names of one run (no student identifiers)
    ex = d[d["run"] == "FFF-2014J"].sort_values("rank").head(5)
    c.write(pd.DataFrame({"rank": ex["rank"], "risk_rank_in_run": ex["rank"].astype(str) + " of " + str((d["run"] == "FFF-2014J").sum()),
                          "reason_1": ex["top_reason"], "reason_2": ex["second_reason"]}), "aq4_example_list.csv")

# ------------------------------------------------------------------ fairness: rule FR1 (confirmatory) and descriptive
d["grp_disability"] = d["disability"] == "Y"
d["grp_imd_0_10"] = d["imd_band"] == "0-10%"
d["grp_imd_missing"] = d["imd_band"] == "Missing"
CONF = {"grp_disability": "Declared disability", "grp_imd_0_10": "Most deprived band (0–10%)",
        "grp_imd_missing": "Deprivation band missing"}

runs = [(g["y"].to_numpy(), g[CHOSEN].to_numpy(), g["tiebreak_u"].to_numpy(), g[list(CONF)].to_numpy())
        for _, g in d.groupby("run", sort=True)]


def group_recall(sample):
    """Recall at 5 per 20 of each group and of the other students, summed over runs."""
    hit_g, nc_g, hit_o, nc_o = (np.zeros(len(CONF)) for _ in range(4))
    for y, sc, u, grp in sample:
        k = c.list_size(len(y), 5)
        on = np.zeros(len(y), bool)
        on[np.lexsort((u, -sc))[:k]] = True
        pos = y == 1
        hit_g += ((on & pos)[:, None] & grp).sum(0)
        nc_g += (pos[:, None] & grp).sum(0)
        hit_o += ((on & pos)[:, None] & ~grp).sum(0)
        nc_o += (pos[:, None] & ~grp).sum(0)
    return hit_g / nc_g, hit_o / nc_o


rg, ro = group_recall(runs)
reps = np.empty((5000, len(CONF)))
for i in range(5000):
    sample = []
    for j in rng.integers(0, len(runs), len(runs)):
        y, sc, u, grp = runs[j]
        idx = rng.integers(0, len(y), len(y))
        sample.append((y[idx], sc[idx], u[idx], grp[idx]))
    a, b = group_recall(sample)
    reps[i] = a - b
p_one = (reps >= 0).mean(axis=0)
order = np.argsort(p_one)
holm = np.empty(len(CONF))
running = 0.0
for rank, j in enumerate(order):
    running = max(running, min(1.0, (len(CONF) - rank) * p_one[j]))
    holm[j] = running
fr = []
for j, (col, label) in enumerate(CONF.items()):
    g = d[d[col]]
    fr.append({"group": label, "enrolments": len(g), "non_completers": int(g["y"].sum()), "recall_group": rg[j],
               "recall_others": ro[j], "gap": rg[j] - ro[j], "low": np.quantile(reps[:, j], 0.025),
               "high": np.quantile(reps[:, j], 0.975), "p_one_sided": p_one[j], "p_holm": holm[j],
               "flagged": bool(rg[j] - ro[j] < -0.10 and holm[j] < 0.05)})
c.write(pd.DataFrame(fr), "aq4_fairness_confirmatory.csv")
print(pd.DataFrame(fr).round(3).to_string(index=False))

desc = []
for col in ["gender", "age_band", "disability", "imd_band"]:
    for lev, g in d.groupby(col):
        pos = g[g["y"] == 1]
        r, rlo, rhi = wilson_ci(int(pos["on_list"].sum()), len(pos))
        listed_g = g[g["on_list"]]
        desc.append({"attribute": col, "group": lev, "enrolments": len(g), "base_rate": g["y"].mean(),
                     "selection_rate": g["on_list"].mean(), "recall": r, "recall_low": rlo, "recall_high": rhi,
                     "precision": listed_g["y"].mean() if len(listed_g) else np.nan,
                     "note": "insufficient data, not cleared" if len(g) < 400 else ""})
c.write(pd.DataFrame(desc), "aq4_fairness_descriptive.csv")
