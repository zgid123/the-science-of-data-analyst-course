"""AQ4 (prescriptive ranking, decision support): who tops a list of fixed capacity, with what gain, which reasons
and how fairly (Milestone 4 report, Table 4.4 card, Section 4.4 and rule FR1 of Table 4.5).

Reads the day-27 test scores that aq3_test.py saved and the frozen chosen model (for the reasons); fits nothing.
Lists hold k = 5 × ceil(n / 20) students per 2014 run (3 × for the sensitivity view).

- yield of the n-th contact per tutor group of 20, model and rule;
- list summary at 3 and 5 per 20 against the rule and a random list; listed non-completers by when they leave;
- the reason shown beside each name: the predictor group with the largest positive contribution
  (coefficient × standardised value) of the logistic model; module and start month are course context, not reasons;
- FR1: recall of each confirmatory group (declared disability, deprivation band 0-10%, band missing) against the
  other students, two-level bootstrap with 5,000 replicates, one-sided p with Holm adjustment, flag when the gap is
  below −10 points and the Holm p below 0.05; descriptive rates by gender, age band, disability and deprivation band.

Usage (from the package folder): python src/analysis/aq4_lists.py   (run_all.sh step 21)
Writes results/aq4/contact_yield.csv, list_summary.csv, reach.csv, reasons.csv, coefficients.csv,
fairness_confirmatory.csv, fairness_descriptive.csv, aq4_summary.md.
"""
from __future__ import annotations

import hashlib
import json
import math
import pickle
import sys

import numpy as np
import pandas as pd

import aq34_common as c

freeze_path = c.WORK / "freeze.json"
if not freeze_path.exists():
    sys.exit("no freeze record: run src/analysis/aq3_develop.py and aq3_test.py first")
freeze = json.loads(freeze_path.read_text())
CHOSEN = freeze["choices"]["chosen_configuration"]
model_file = c.WORK / f"{CHOSEN}_d27.pkl"
assert hashlib.sha256(model_file.read_bytes()).hexdigest() == freeze["models"][model_file.name], "model changed after the freeze"
rng = np.random.default_rng(c.SEED + 4)
Z = 1.959963984540054


def wilson(k: int, n: int) -> tuple[float, float, float]:
    if n == 0:
        return (math.nan, math.nan, math.nan)
    p = k / n
    den = 1 + Z * Z / n
    mid = (p + Z * Z / (2 * n)) / den
    half = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return (p, max(0.0, mid - half), min(1.0, mid + half))


s = pd.read_csv(c.WORK / "scores_d27.csv")
test = c.features(27, year=2014)
d = s.merge(test[c.KEY + ["gender", "age_band", "disability", "imd_band", "final_result"]], on=c.KEY, validate="1:1")
d = d.merge(c.enrolment()[c.KEY + ["date_unregistration"]], on=c.KEY, validate="1:1")
d["G"] = d.groupby("run")["run"].transform(lambda x: int(np.ceil(len(x) / 20)))
d["rank"] = c.rank_in_run(d, CHOSEN)
d["rank_rule"] = c.rank_in_run(d, "rule")
d["k5"] = d.groupby("run")["run"].transform(lambda x: c.list_size(len(x), 5))
d["on_list"] = d["rank"] <= d["k5"]

# ---------------------------------------------------------------- yield of each extra contact per tutor group
yld = []
for j in range(1, 11):
    for name, col in [("model", "rank"), ("rule", "rank_rule")]:
        band = d[(d[col] > (j - 1) * d["G"]) & (d[col] <= j * d["G"])]
        p, lo, hi = wilson(int(band["y"].sum()), len(band))
        yld.append({"contact": j, "method": name, "students": len(band), "non_completers": int(band["y"].sum()),
                    "precision": p, "low": lo, "high": hi, "base_rate": d["y"].mean()})
c.write(pd.DataFrame(yld), c.RES4, "contact_yield.csv")

# ---------------------------------------------------------------- list summary at 3 and 5 per 20
summ = []
for per20 in (3, 5):
    for meth in [CHOSEN, "rule"]:
        summ.append({"per20": per20, "method": "model" if meth == CHOSEN else "rule", **c.pooled(c.list_metrics(d, meth, per20))})
    r = c.list_metrics(d, "rule", per20)
    tp = (r["k"] * r["positives"] / r["n"]).sum()
    summ.append({"per20": per20, "method": "random (expected)", "n": int(r["n"].sum()), "k": int(r["k"].sum()),
                 "positives": int(r["positives"].sum()), "tp": tp, "attainable": int(r["attainable"].sum()),
                 "norm_recall": tp / r["attainable"].sum(), "recall": tp / r["positives"].sum(),
                 "precision": tp / r["k"].sum(), "lift": 1.0})
c.write(pd.DataFrame(summ), c.RES4, "list_summary.csv")

listed = d[d["on_list"]]
reach = {"listed": len(listed), "listed_non_completers": int(listed["y"].sum()),
         "withdrew_days_28_34": int((listed["final_result"].eq("Withdrawn") & listed["date_unregistration"].between(28, 34)).sum()),
         "listed_fail": int(listed["final_result"].eq("Fail").sum()),
         "listed_withdrawn": int(listed["final_result"].eq("Withdrawn").sum())}
reach["reachable_non_completers"] = reach["listed_non_completers"] - reach["withdrew_days_28_34"]
c.write(pd.DataFrame([reach]), c.RES4, "reach.csv")

# ---------------------------------------------------------------- reasons shown beside each name
REASON = {"tasks_missed_c": "Missed a task", "tasks_late_c": "Late submission", "tma_late_c": "Late submission",
          "cma_late_c": "Late submission", "cma_marked_c": "Few marked quizzes", "clicks_0c": "Low activity",
          "active_days_0c": "Low activity", "sites_0c": "Low activity", "activity_ratio_run": "Low activity",
          "inactive_last7": "Inactive last 7 days", "clicks_pre": "No activity before start",
          "num_of_prev_attempts": "Previous attempt", "studied_credits": "Study load",
          "registration_lead": "Late registration", "banked_results": "Previous attempt",
          "highest_education": "Prior education"}
with open(model_file, "rb") as fh:
    model = pickle.load(fh)
if model.kind == "logistic":
    x = test.set_index(c.KEY).loc[pd.MultiIndex.from_frame(d[c.KEY])].reset_index()
    contrib = model.contributions(x)
    grouped = pd.DataFrame(index=contrib.index)
    for col in contrib.columns:
        reason = REASON.get(col.replace("_missing", ""), "Course context")
        grouped[reason] = grouped.get(reason, 0) + contrib[col]
    grouped = grouped.drop(columns=["Course context"], errors="ignore")
    d["top_reason"] = grouped.idxmax(axis=1).where(grouped.max(axis=1) > 0, "No single reason")
    rs = []
    for reason, g in d[d["on_list"]].groupby("top_reason"):
        p, lo, hi = wilson(int(g["y"].sum()), len(g))
        rs.append({"top_reason": reason, "listed": len(g), "share_of_list": len(g) / d["on_list"].sum(),
                   "non_completers": int(g["y"].sum()), "rate": p, "low": lo, "high": hi})
    c.write(pd.DataFrame(rs).sort_values("listed", ascending=False), c.RES4, "reasons.csv")
    coef = pd.DataFrame({"predictor": model.prep.names(), "coefficient_per_sd": model.est.coef_[0]})
    coef["reason"] = [REASON.get(n.replace("_missing", ""), "Course context") for n in coef["predictor"]]
    c.write(coef.sort_values("coefficient_per_sd", key=abs, ascending=False), c.RES4, "coefficients.csv")

# ---------------------------------------------------------------- fairness rule FR1 and descriptive rates
d["grp_disability"] = d["disability"] == "Y"
d["grp_imd_0_10"] = d["imd_band"] == "0-10%"
d["grp_imd_missing"] = d["imd_band"] == "Missing"
CONF = {"grp_disability": "Declared disability", "grp_imd_0_10": "Most deprived band (0–10%)",
        "grp_imd_missing": "Deprivation band missing"}
runs = [(g["y"].to_numpy(), g[CHOSEN].to_numpy(), g["tiebreak_u"].to_numpy(), g[list(CONF)].to_numpy())
        for _, g in d.groupby("run", sort=True)]


def group_recall(sample):
    hit_g, nc_g, hit_o, nc_o = (np.zeros(len(CONF)) for _ in range(4))
    for y, sc, u, grp in sample:
        on = np.zeros(len(y), bool)
        on[np.lexsort((u, -sc))[:c.list_size(len(y), 5)]] = True
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
holm, running = np.empty(len(CONF)), 0.0
for rank, j in enumerate(np.argsort(p_one)):
    running = max(running, min(1.0, (len(CONF) - rank) * p_one[j]))
    holm[j] = running
fr = []
for j, (col, label) in enumerate(CONF.items()):
    g = d[d[col]]
    fr.append({"group": label, "enrolments": len(g), "non_completers": int(g["y"].sum()), "recall_group": rg[j],
               "recall_others": ro[j], "gap": rg[j] - ro[j], "low": np.quantile(reps[:, j], 0.025),
               "high": np.quantile(reps[:, j], 0.975), "p_one_sided": p_one[j], "p_holm": holm[j],
               "flagged": bool(rg[j] - ro[j] < -0.10 and holm[j] < 0.05)})
fr = pd.DataFrame(fr)
c.write(fr, c.RES4, "fairness_confirmatory.csv")

desc = []
for col in ["gender", "age_band", "disability", "imd_band"]:
    for lev, g in d.groupby(col):
        pos = g[g["y"] == 1]
        r, rlo, rhi = wilson(int(pos["on_list"].sum()), len(pos))
        lg = g[g["on_list"]]
        desc.append({"attribute": col, "group": lev, "enrolments": len(g), "base_rate": g["y"].mean(),
                     "selection_rate": g["on_list"].mean(), "recall": r, "recall_low": rlo, "recall_high": rhi,
                     "precision": lg["y"].mean() if len(lg) else np.nan,
                     "note": "insufficient data, not cleared" if len(g) < 400 else ""})
c.write(pd.DataFrame(desc), c.RES4, "fairness_descriptive.csv")

y5 = pd.DataFrame(yld).query("method == 'model'").set_index("contact")
lines = ["# AQ4: ranked contact lists, 13 runs of 2014, day 27", "",
         f"- Yield of the n-th contact per tutor group of 20 (model): 1st {y5.loc[1, 'precision']:.1%}, "
         f"5th {y5.loc[5, 'precision']:.1%}, 7th {y5.loc[7, 'precision']:.1%}; base rate {y5.loc[1, 'base_rate']:.1%}.",
         f"- Listed non-completers at 5 per 20: {reach['listed_non_completers']:,} of {reach['listed']:,} listed; "
         f"{reach['withdrew_days_28_34']} withdraw in days 28–34; {reach['listed_fail']:,} fail at the end.",
         f"- Rule FR1: {int(fr['flagged'].sum())} of {len(fr)} confirmatory groups flagged."]
(c.RES4 / "aq4_summary.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
