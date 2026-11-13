"""Second code path for the headline numbers. Exits 1 on any difference.

(a) AQ1 from the raw OULAD tables (studentInfo, studentRegistration), not the prepared views: the KPI population
    (still registered at day 14), non-completers per run, and the exit-timing counts.
(b) AQ3/AQ4 list counts from the saved test scores with a separate ranking routine (pandas sort, no shared helper).
"""

import json
import math
import sys

import _tools  # noqa: F401
import pandas as pd
from holdout_guard import open_holdout

import common as c

open_holdout(c.FREEZE, c.ACCESS, who="12_recompute.py", why="independent recomputation of headline numbers")
checks = []


def check(name, mine, theirs, tol=0):
    ok = abs(float(mine) - float(theirs)) <= tol
    checks.append({"check": name, "recomputed": mine, "reported": theirs, "status": "PASS" if ok else "FAIL"})


# ---------------------------------------------------------------- (a) AQ1 from raw tables
info = c.raw_csv("studentInfo.csv")
reg = c.raw_csv("studentRegistration.csv")
raw = info.merge(reg, on=c.KEY, how="left", validate="1:1")
check("raw enrolments", len(raw), 32593)
raw["nc"] = raw["final_result"].isin(["Fail", "Withdrawn"]).astype(int)
kpi = raw[(raw["date_registration"].isna() | (raw["date_registration"] <= 14))
          & (raw["date_unregistration"].isna() | (raw["date_unregistration"] > 14))]
rates = pd.read_csv(c.RESULTS / "aq1_rates_kpi.csv")
check("KPI population (registered at day 14)", len(kpi), rates.loc[rates["level"] == "All runs", "enrolments"].iloc[0])
check("KPI non-completers", kpi["nc"].sum(), rates.loc[rates["level"] == "All runs", "non_completers"].iloc[0])
by_run = kpi.assign(run=kpi["code_module"] + "-" + kpi["code_presentation"]).groupby("run")["nc"].agg(["size", "sum"])
rep = pd.read_csv(c.RESULTS / "aq1_rates_by_run_kpi.csv").set_index("group")
diff_runs = sum(int(by_run.loc[r, "size"] != rep.loc[r, "enrolments"] or by_run.loc[r, "sum"] != rep.loc[r, "non_completers"])
                for r in rep.index)
check("runs whose KPI counts differ between the two paths (of 22)", diff_runs, 0)
w = raw[(raw["final_result"] == "Withdrawn")]
u = w["date_unregistration"]
exit_ = pd.read_csv(c.RESULTS / "aq1_exit_timing.csv").set_index("band")["non_completers"]
check("withdrew before day 14", int((u < 14).sum()),
      exit_["Withdrew before the start (day < 0)"] + exit_["Withdrew days 0–13 (before the week-3 list)"])
check("failed at the end", int((raw["final_result"] == "Fail").sum()), exit_["Failed at the end of the run"])

# ---------------------------------------------------------------- (b) list counts from saved scores, separate routine
CHOSEN = json.loads((c.RESULTS / "aq3_choices.json").read_text())["chosen_configuration"]
s = pd.read_csv(c.SCORES / "test_scores_d27.csv")
pooled = pd.read_csv(c.RESULTS / "aq3_test_pooled.csv")
for col, method in [(CHOSEN, CHOSEN), ("rule", "RULE")]:
    tp = 0
    for _, g in s.groupby("run"):
        k = min(len(g), 5 * math.ceil(len(g) / 20))
        top = g.sort_values([col, "tiebreak_u"], ascending=[False, True]).head(k)
        tp += int(top["y"].sum())
    ref = pooled[(pooled["cutoff"] == 27) & (pooled["per20"] == 5) & (pooled["method"] == method)]
    check(f"listed non-completers, {method}, day 27, 5 per 20", tp, ref["tp"].iloc[0])

out = pd.DataFrame(checks)
c.write(out, "check_recompute.csv")
print(out.to_string(index=False))
sys.exit(0 if (out["status"] == "PASS").all() else 1)
