"""AQ4 step 3 – fairness audit of the day-27 list, 5 per 20 (Level 1 report, Section 4.4, Table 4.5 FR1, Table A.8).

Confirmatory (rule FR1, fixed in Level 1 before any test outcome was opened):
    groups   declared disability; deprivation band 0–10%; deprivation band missing
    measure  recall at capacity of the group minus that of all other students, counts summed over the 13 runs
    flag     gap below −10 percentage points AND one-sided 95% bootstrap interval, Holm-adjusted over the three groups,
             entirely below 0. A flag leads to review; it does not reject the model.
Students aged 55 or over (118 test enrolments, below the size of 400) get a point gap only: "insufficient data, not cleared".

Descriptive: selection rate, recall and precision for every audit group; calibration by group; ABROCA with a
permutation reference; a proxy check (which predictors differ between groups). The same checks for the rule list.

Writes results/fairness_confirmatory.csv, fairness_descriptive.csv, fairness_calibration.csv, fairness_abroca.csv,
       fairness_proxy.csv
"""

import numpy as np
import polars as pl
from sklearn.metrics import roc_auc_score, roc_curve

from aq4_common import CHOSEN, EXTRACT, RESULTS, lib

lib.open_test_outcomes("aq-4/code/03_fairness.py", "fairness audit of the frozen list")
B_FAIR = 5000
d = pl.read_csv(EXTRACT / "aq4_ranked_d27.csv")
groups = {
    "Declared disability": (d["disability"] == "Y").to_numpy(),
    "Deprivation band 0–10%": (d["imd_band"] == "0-10%").to_numpy(),
    "Deprivation band missing": (d["imd_band"] == "Missing").to_numpy(),
}
small = {"Age 55 or over": (d["age_band"] == "55<=").to_numpy()}
y_all = d["non_completion"].to_numpy().astype(bool)
runs_all = d["run"].to_numpy()
run_names = sorted(set(runs_all))
per_run = []
for r in run_names:
    m = runs_all == r
    per_run.append({"y": y_all[m], "rank": {n: d[f"rank_{n}"].to_numpy()[m] - 1 for n in ("model", "rule")},
                    "g": {k: v[m] for k, v in {**groups, **small}.items()}, "k": lib.list_len(int(m.sum()), 5)})


def gap(on, y, g):
    rg = (on & y & g).sum() / max((y & g).sum(), 1)
    ro = (on & y & ~g).sum() / max((y & ~g).sum(), 1)
    return rg, ro


lib.banner("Confirmatory fairness check FR1: recall at capacity by group, day 27, 5 per 20")
conf = []
for name in ("model", "rule"):
    on_all = d[f"list5_{name}"].to_numpy()
    # two-level bootstrap: runs, then enrolments; each run's list re-formed from its resampled enrolments
    acc = {k: np.zeros((B_FAIR, 4)) for k in {**groups, **small}}
    for b, rep in enumerate(lib.bootstrap_indices([len(p["y"]) for p in per_run], B_FAIR, lib.SEED)):
        for r, idx in rep:
            p = per_run[r]
            y = p["y"][idx]
            on = np.zeros(len(idx), bool)
            on[np.argsort(p["rank"][name][idx], kind="stable")[:p["k"]]] = True
            for k_, g in p["g"].items():
                gg = g[idx]
                acc[k_][b] += [(on & y & gg).sum(), (y & gg).sum(), (on & y & ~gg).sum(), (y & ~gg).sum()]
    rows = []
    for k_, g in {**groups, **small}.items():
        rg, ro = gap(on_all, y_all, g)
        a = acc[k_]
        diff = a[:, 0] / np.maximum(a[:, 1], 1) - a[:, 2] / np.maximum(a[:, 3], 1)
        rows.append({"ranking": name, "group": k_, "confirmatory": k_ in groups, "test_enrolments": int(g.sum()),
                     "group_non_completers": int((y_all & g).sum()), "group_base_rate": float(y_all[g].mean()),
                     "selection_rate_group": float(on_all[g].mean()), "selection_rate_others": float(on_all[~g].mean()),
                     "recall_group": rg, "recall_others": ro, "gap": rg - ro,
                     "boot_ci95_low": float(np.percentile(diff, 2.5)), "boot_ci95_high": float(np.percentile(diff, 97.5)),
                     "p_one_sided": float(np.mean(diff >= 0)), "_diff": diff})
    # Holm step-down over the confirmatory groups
    cf = sorted([r for r in rows if r["confirmatory"]], key=lambda r: r["p_one_sided"])
    m, running = len(cf), 0.0
    for i, r in enumerate(cf):
        running = max(running, min(1.0, (m - i) * r["p_one_sided"]))
        r["p_holm"] = running
        r["holm_upper_bound"] = float(np.percentile(r["_diff"], 100 * (1 - 0.05 / (m - i))))
        r["flagged"] = bool(r["gap"] < -0.10 and r["p_holm"] < 0.05)
        r["status"] = "FLAGGED for review" if r["flagged"] else "not flagged"
    for r in rows:
        if not r["confirmatory"]:
            r.update({"p_holm": None, "holm_upper_bound": None, "flagged": None, "status": "insufficient data, not cleared (point gap only)"})
        r.pop("_diff")
    conf += rows
conf = pl.DataFrame(conf)
print(lib.md_table(conf.select("ranking", "group", "test_enrolments", "group_non_completers", "group_base_rate", "recall_group", "recall_others", "gap",
                               "boot_ci95_low", "boot_ci95_high", "p_one_sided", "p_holm", "holm_upper_bound", "status")))
lib.save_csv(conf, RESULTS / "fairness_confirmatory.csv")
mf = conf.filter((pl.col("ranking") == "model") & pl.col("confirmatory"))
nflag = int(mf["flagged"].sum())
print(f"\n**FR1 verdict for the model list: {nflag} of 3 confirmatory groups flagged.** "
      f"A group is flagged only when its recall is more than 10 points below the others AND the Holm-adjusted interval lies below 0.")

lib.banner("Descriptive: selection rate, recall and precision by audit group (model list and rule list)")
desc = []
for col in ["gender", "disability", "age_band", "imd_band"]:
    for g in sorted(d[col].unique().to_list()):
        s = d.filter(pl.col(col) == g)
        nc = s.filter(pl.col("non_completion"))
        row = {"attribute": col, "group": g, "enrolments": s.height, "non_completers": nc.height, "base_rate": nc.height / s.height,
               "share_of_all_non_completers": nc.height / int(y_all.sum())}
        for name in ("model", "rule"):
            on = s.filter(pl.col(f"list5_{name}"))
            row[f"{name}_selection_rate"] = on.height / s.height
            row[f"{name}_share_of_list"] = on.height / int(d[f"list5_{name}"].sum())
            row[f"{name}_recall"] = nc.filter(pl.col(f"list5_{name}")).height / nc.height
            row[f"{name}_precision"] = on.filter(pl.col("non_completion")).height / on.height if on.height else float("nan")
        desc.append(row)
desc = pl.DataFrame(desc)
print(lib.md_table(desc))
lib.save_csv(desc, RESULTS / "fairness_descriptive.csv")

lib.banner("Descriptive: calibration by group (frozen model, no recalibration)")
cal = []
p_all = d[CHOSEN].to_numpy()
for label, g in {**groups, **small, "Female": (d["gender"] == "F").to_numpy(), "Male": (d["gender"] == "M").to_numpy(), "All test enrolments": np.ones(d.height, bool)}.items():
    c = lib.calibration(y_all[g], p_all[g])
    events, non_events = int(y_all[g].sum()), int((~y_all[g]).sum())
    cal.append({"group": label, "enrolments": int(g.sum()), "events": events, "non_events": non_events, "observed_rate": c["observed_rate"],
                "mean_predicted": c["mean_predicted"], "citl": c["citl"], "citl_ci_low": c["citl"] - 1.96 * c["citl_se"], "citl_ci_high": c["citl"] + 1.96 * c["citl_se"],
                "slope": c["slope"], "slope_ci_low": c["slope"] - 1.96 * c["slope_se"], "slope_ci_high": c["slope"] + 1.96 * c["slope_se"],
                "enough_for_a_curve": events >= 200 and non_events >= 200})
cal = pl.DataFrame(cal)
print(lib.md_table(cal))
lib.save_csv(cal, RESULTS / "fairness_calibration.csv")

lib.banner("Descriptive: ABROCA within run (area between the group's ROC curve and the others'), with a shuffled-label reference")
grid = np.linspace(0, 1, 501)


def abroca(score, y, g):
    """Weighted mean over runs of the absolute area between ROC curves, and of the signed AUC difference."""
    tot_w = area = signed = 0.0
    for r in run_names:
        m = runs_all == r
        gy, oy = y[m & g], y[m & ~g]
        if min(gy.sum(), (~gy).sum()) < 10 or min(oy.sum(), (~oy).sum()) < 10:
            continue
        f1, t1, _ = roc_curve(gy, score[m & g])
        f0, t0, _ = roc_curve(oy, score[m & ~g])
        w = (m & g).sum()
        area += w * np.trapezoid(np.abs(np.interp(grid, f1, t1) - np.interp(grid, f0, t0)), grid)
        signed += w * (roc_auc_score(gy, score[m & g]) - roc_auc_score(oy, score[m & ~g]))
        tot_w += w
    return (area / tot_w, signed / tot_w) if tot_w else (float("nan"), float("nan"))


rng = np.random.default_rng(lib.SEED)
ab = []
for label, g in {**groups, "Female (against male)": (d["gender"] == "F").to_numpy()}.items():
    a, sdiff = abroca(p_all, y_all, g)
    ref = []
    for _ in range(200):
        gs = g.copy()
        for r in run_names:
            m = np.flatnonzero(runs_all == r)
            gs[m] = g[m][rng.permutation(len(m))]
        ref.append(abroca(p_all, y_all, gs)[0])
    ab.append({"group": label, "abroca": a, "auc_group_minus_others": sdiff, "shuffled_mean": float(np.mean(ref)),
               "shuffled_p95": float(np.percentile(ref, 95)), "above_chance_reference": bool(a > np.percentile(ref, 95))})
ab = pl.DataFrame(ab)
print(lib.md_table(ab, digits=4))
lib.save_csv(ab, RESULTS / "fairness_abroca.csv")

lib.banner("Proxy check: mean score and predictor values by group (which predictors carry group information)")
cols = [CHOSEN, "clicks_0c", "activity_ratio_run", "num_of_prev_attempts", "early_sign_rule", "rule_missed", "inactive_last7"]
px = []
for label, g in {**groups, **small, "Female": (d["gender"] == "F").to_numpy(), "All test enrolments": np.ones(d.height, bool)}.items():
    s = d.filter(pl.Series(g))
    px.append({"group": label, "enrolments": s.height, "mean_risk_score": s[CHOSEN].mean(), "median_clicks_0c": s["clicks_0c"].median(),
               "median_activity_ratio": s["activity_ratio_run"].median(), "share_repeat_attempt": (s["num_of_prev_attempts"] > 0).mean(),
               "share_flagged_by_rule": s["early_sign_rule"].mean(), "share_task_missed": s["rule_missed"].mean(), "share_inactive_last7": s["inactive_last7"].mean(),
               "observed_non_completion": s["non_completion"].mean()})
px = pl.DataFrame(px)
print(lib.md_table(px))
lib.save_csv(px, RESULTS / "fairness_proxy.csv")
