"""AQ4 (prescriptive ranking, decision support): the parts that exist only for the test on the 13 runs of 2014
(Milestone 4 report, Table 4.4 card, Section 4.4 and rule FR1 of Table 4.5).

Reads the day-27 test scores that aq3_test.py saved and the frozen chosen model; fits nothing. Lists hold
k = 5 × ceil(n / 20) students per 2014 run.

- the reason shown beside each name: the predictor group with the largest positive contribution
  (coefficient × standardised value) of the logistic model; module and start month are course context, not reasons;
- the coefficients of the chosen model, fitted on the 2013 runs;
- FR1: recall of each confirmatory group (declared disability, deprivation band 0-10%, band missing) against the
  other students, two-level bootstrap with 5,000 replicates, one-sided p with Holm adjustment, flag when the gap is
  below −10 points and the Holm p below 0.05.

The yield of each contact, the list summary, reach and the descriptive fairness rates are written for every scope
by aq34_scopes.py.

Usage (from the package folder): python src/analysis/aq4_lists.py   (run_all.sh step 21)
Writes results/2014/aq4_reasons.csv, aq4_fairness_confirmatory.csv; results/2013/aq3_coefficients.csv.
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
    c.write(pd.DataFrame(rs).sort_values("listed", ascending=False), c.R2014, "aq4_reasons.csv")
    coef = pd.DataFrame({"predictor": model.prep.names(), "coefficient_per_sd": model.est.coef_[0]})
    coef["reason"] = [REASON.get(n.replace("_missing", ""), "Course context") for n in coef["predictor"]]
    c.write(coef.sort_values("coefficient_per_sd", key=abs, ascending=False), c.R2013, "aq3_coefficients.csv")

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
c.write(fr, c.R2014, "aq4_fairness_confirmatory.csv")

print(fr.round(3).to_string(index=False))
