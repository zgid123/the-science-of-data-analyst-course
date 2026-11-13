"""AQ1 (descriptive): what share of enrolments end in pass, fail or withdrawal, by module, run, start month and year;
when non-completers leave; and in which week they first miss an assessed task.

KPI population: enrolments still registered at day 14 (28,061). Second denominator: all 32,593 enrolments.
Reads 2014 outcomes, so it runs after the AQ3 freeze, through the guard.
"""

import _tools  # noqa: F401
import numpy as np
import pandas as pd
from holdout_guard import open_holdout
from stats_helpers import diff_proportions_ci, wilson_ci

import common as c

open_holdout(c.FREEZE, c.ACCESS, who="11_aq1.py", why="AQ1 descriptive rates over both years")
e = c.enrolment()
e["y"] = e["non_completion"].astype(int)
kpi = e[e["enrolled_d14"]].copy()
MONTH = {"B": "February (B)", "J": "October (J)"}


def rate_row(level, group, g):
    p, lo, hi = wilson_ci(int(g["y"].sum()), len(g))
    return {"level": level, "group": group, "enrolments": len(g), "non_completers": int(g["y"].sum()),
            "rate": p, "low": lo, "high": hi}


# ------------------------------------------------------------------ rates, KPI population and all enrolments
for name, pop in [("kpi", kpi), ("all", e)]:
    rows = [rate_row("All runs", "22 runs", pop)]
    rows += [rate_row("Year", f"{y} ({g['run'].nunique()} runs)", g) for y, g in pop.groupby("year")]
    rows += [rate_row("Start month", MONTH[mth], g) for mth, g in pop.groupby("start_month")]
    rows += [rate_row("Module", mod, g) for mod, g in pop.groupby("code_module")]
    c.write(pd.DataFrame(rows), f"aq1_rates_{name}.csv")
    runs = pd.DataFrame([rate_row("Run", r, g) | {"module": g["code_module"].iloc[0], "year": int(g["year"].iloc[0]),
                                                  "start_month": g["start_month"].iloc[0]} for r, g in pop.groupby("run")])
    c.write(runs.sort_values("rate", ascending=False), f"aq1_rates_by_run_{name}.csv")

flag = kpi[~(kpi["registration_missing"] | kpi["withdrawal_day_missing"])]
c.write(pd.DataFrame([rate_row("All runs", "without enrolments missing a registration or withdrawal day", flag)]),
        "aq1_rates_flag_excluded.csv")

# outcome shares by module (KPI population)
shares = []
for mod, g in [("All runs", kpi)] + list(kpi.groupby("code_module")):
    row = {"module": mod, "enrolments": len(g)}
    for res in ["Distinction", "Pass", "Fail", "Withdrawn"]:
        row[res.lower()] = (g["final_result"] == res).mean()
    shares.append(row)
c.write(pd.DataFrame(shares), "aq1_outcome_shares.csv")

# start-month gap inside each module that runs in both months
gap = []
for mod, g in kpi.groupby("code_module"):
    if g["start_month"].nunique() == 2:
        b, j = g[g["start_month"] == "B"], g[g["start_month"] == "J"]
        d, lo, hi = diff_proportions_ci(int(b["y"].sum()), len(b), int(j["y"].sum()), len(j))
        gap.append({"module": mod, "rate_feb": b["y"].mean(), "rate_oct": j["y"].mean(), "difference": d, "low": lo, "high": hi})
c.write(pd.DataFrame(gap), "aq1_start_month_gap.csv")

# ------------------------------------------------------------------ year comparison, like for like
shared_mod = sorted(set(e.loc[e["year"] == 2013, "code_module"]) & set(e.loc[e["year"] == 2014, "code_module"]))
e["pair"] = e["code_module"] + "-" + e["start_month"]
shared_pair = sorted(set(e.loc[e["year"] == 2013, "pair"]) & set(e.loc[e["year"] == 2014, "pair"]))
yc = []
for denom, pop in [("Registered at day 14", e[e["enrolled_d14"]]), ("All enrolments", e)]:
    for label, sub in [("All runs", pop), (f"{len(shared_mod)} modules run in both years", pop[pop["code_module"].isin(shared_mod)]),
                       (f"{len(shared_pair)} module × start-month pairs run in both years", pop[pop["pair"].isin(shared_pair)])]:
        a, b = sub[sub["year"] == 2013], sub[sub["year"] == 2014]
        d, lo, hi = diff_proportions_ci(int(b["y"].sum()), len(b), int(a["y"].sum()), len(a))
        yc.append({"denominator": denom, "runs": label, "method": "pooled", "n_2013": len(a), "rate_2013": a["y"].mean(),
                   "n_2014": len(b), "rate_2014": b["y"].mean(), "difference": d, "low": lo, "high": hi})
    sub = pop[pop["pair"].isin(shared_pair)]
    num = den = var = 0.0
    for _, g in sub.groupby("pair"):
        a, b = g[g["year"] == 2013], g[g["year"] == 2014]
        w = len(a) * len(b) / (len(a) + len(b))
        pa, pb = a["y"].mean(), b["y"].mean()
        num, den = num + w * (pb - pa), den + w
        var += w**2 * (pa * (1 - pa) / len(a) + pb * (1 - pb) / len(b))
    d, se = num / den, np.sqrt(var) / den
    yc.append({"denominator": denom, "runs": f"{len(shared_pair)} module × start-month pairs run in both years",
               "method": "weighted over pairs (Mantel–Haenszel)", "n_2013": len(sub[sub["year"] == 2013]),
               "rate_2013": np.nan, "n_2014": len(sub[sub["year"] == 2014]), "rate_2014": np.nan,
               "difference": d, "low": d - 1.96 * se, "high": d + 1.96 * se})
c.write(pd.DataFrame(yc), "aq1_year_comparison.csv")

# why the two denominators disagree: share not registered at day 14, by year, shared modules
sm = e[e["code_module"].isin(shared_mod)]
nr = []
for y, g in sm.groupby("year"):
    gone = ~g["enrolled_d14"]
    nr.append({"year": int(y), "enrolments": len(g), "not_registered_d14": int(gone.sum()), "share": gone.mean(),
               "non_completion_of_those": g.loc[gone, "y"].mean()})
c.write(pd.DataFrame(nr), "aq1_not_registered_d14.csv")

# ------------------------------------------------------------------ when non-completers leave (all enrolments)
nc = e[e["y"] == 1].copy()
u = nc["date_unregistration"]
w = nc["final_result"] == "Withdrawn"
bands = [("Withdrew before the start (day < 0)", w & (u < 0)),
         ("Withdrew days 0–13 (before the week-3 list)", w & u.between(0, 13)),
         ("Withdrew days 14–27 (before the week-5 list)", w & u.between(14, 27)),
         ("Withdrew days 28–90", w & u.between(28, 90)),
         ("Withdrew after day 90", w & (u > 90)),
         ("Withdrawn, day not recorded", w & u.isna()),
         ("Failed at the end of the run", nc["final_result"] == "Fail")]
exit_ = [{"band": lab, "non_completers": int(mk.sum()), "share": mk.mean()} for lab, mk in bands]
assert sum(r["non_completers"] for r in exit_) == len(nc)
c.write(pd.DataFrame(exit_), "aq1_exit_timing.csv")
# the same by week (cumulative share of non-completers who have withdrawn), weeks −4 to 40
weeks = []
wk = np.floor(u / 7) + 1
for week in range(-4, 41):
    weeks.append({"week": week, "withdrawn_by_week": int((w & (wk <= week)).sum()),
                  "share_of_non_completers": float((w & (wk <= week)).sum() / len(nc))})
c.write(pd.DataFrame(weeks), "aq1_exit_by_week.csv")

# ------------------------------------------------------------------ first missed assessed task (KPI population)
task_runs = c.runs_with_tasks(27)
task_runs = set((task_runs.loc[task_runs["any_task"], "code_module"] + "-" + task_runs.loc[task_runs["any_task"], "code_presentation"]))
fm = []
for week in range(1, 41):
    for outcome, g in [("Non-completers", kpi[kpi["y"] == 1]), ("Completers", kpi[kpi["y"] == 0])]:
        fm.append({"week": week, "group": outcome, "share_missed_by_week": (g["first_missed_week"] <= week).mean()})
c.write(pd.DataFrame(fm), "aq1_first_missed_cumulative.csv")
summ = []
for label, pop in [("All 22 runs", kpi), ("16 runs with a task due by day 27", kpi[kpi["run"].isin(task_runs)])]:
    for outcome, g in [("Non-completers", pop[pop["y"] == 1]), ("Completers", pop[pop["y"] == 0])]:
        summ.append({"runs": label, "group": outcome, "enrolments": len(g),
                     "missed_by_week_4": (g["first_missed_week"] <= 4).mean(),
                     "missed_by_week_8": (g["first_missed_week"] <= 8).mean(),
                     "missed_ever": g["first_missed_week"].notna().mean(),
                     "median_first_missed_week": g["first_missed_week"].median()})
c.write(pd.DataFrame(summ), "aq1_first_missed_summary.csv")

# ------------------------------------------------------------------ subgroups (description only)
sub = []
for col in ["gender", "disability", "imd_band", "age_band"]:
    for lev, g in kpi.groupby(col):
        sub.append(rate_row(col, lev, g))
c.write(pd.DataFrame(sub), "aq1_subgroup_rates.csv")
print(pd.DataFrame(exit_).round(3).to_string(index=False))

# ------------------------------------------------------------------ the blind spot of AQ3: when normally active
# non-completers of 2014 (clicks > 0 and at least half the run median at day 27) first miss a task
f27 = c.features(27)
act = f27[(f27["year"] == 2014) & (f27["clicks_0c"] > 0) & (f27["activity_ratio_run"] >= 0.5) & (f27["y"] == 1)]
act = act.merge(e[c.KEY + ["first_missed_week"]], on=c.KEY, how="left", validate="1:1")
bs = [{"group": "2014 non-completers with normal activity at day 27", "non_completers": len(act),
       "median_first_missed_week": act["first_missed_week"].median(),
       "share_never_missed": act["first_missed_week"].isna().mean(),
       "share_missed_by_week_8": (act["first_missed_week"] <= 8).mean()}]
c.write(pd.DataFrame(bs), "aq1_blind_spot_timing.csv")
print(pd.DataFrame(bs).round(3).to_string(index=False))
