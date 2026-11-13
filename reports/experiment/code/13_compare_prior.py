"""Reconcile with the team's earlier implementation of the same design (git commit 7516b83, folder reports/code).

Copies the earlier result tables into evidence/prior/ (read from git, so no file outside this folder is needed
once copied), harmonises names and compares with tools/compare_results.py. Every difference is listed in
results/compare_prior.csv and explained in NOTES.md; the step does not fail on an explained difference.
"""

import subprocess
from pathlib import Path

import _tools  # noqa: F401
import pandas as pd
from compare_results import compare

import common as c

COMMIT = "7516b83"
PRIOR = c.ROOT / "evidence" / "prior"
FILES = ["aq-1/results/denominators_by_run_all.csv", "aq-2/results/replication.csv", "aq-3/results/test_pooled.csv",
         "aq-4/results/fairness_confirmatory.csv", "aq-3/results/dev_pooled.csv"]
for f in FILES:
    dest = PRIOR / f.replace("/", "__")
    if not dest.exists():
        PRIOR.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(subprocess.run(["git", "show", f"{COMMIT}:reports/code/{f}"], check=True,
                                        capture_output=True, cwd=c.ROOT).stdout)
prior = {f: PRIOR / f.replace("/", "__") for f in FILES}
tmp = c.ROOT / "evidence" / "harmonised"
tmp.mkdir(parents=True, exist_ok=True)
summary = []


def run(name: str, mine: pd.DataFrame, theirs: Path, keys: list[str], cols: list[str], tol: float, mapping=None):
    path = tmp / f"{name}.csv"
    mine.to_csv(path, index=False)
    cells = compare(path, theirs, keys, cols, tol, mapping)
    diffs = [d for d in cells if d["status"] != "EQUAL"]
    summary.append({"comparison": name, "rows_compared": len(mine), "columns": ",".join(cols), "tolerance": tol,
                    "cells_compared": len(cells), "differences": len(diffs),
                    "detail": "; ".join(f"{d['key']} {d['column']}: mine {d['mine']}, earlier {d['theirs']}" for d in diffs)})


# AQ1: KPI population and rate per run (22 runs)
a = pd.read_csv(c.RESULTS / "aq1_rates_by_run_kpi.csv").rename(columns={"group": "run", "enrolments": "n_kpi", "rate": "rate_kpi"})
run("aq1_rate_by_run", a[["run", "n_kpi", "rate_kpi"]], prior[FILES[0]], ["run"], ["n_kpi", "rate_kpi"], 1e-6)

# AQ2: adjusted risk differences, both years
names = {"missed_task": "sign_task_missed", "late_tma": "sign_tma_late", "inactive_7d": "sign_inactive_last7",
         "low_activity": "sign_low_activity", "no_prestart": "sign_no_pre_activity"}
b = pd.read_csv(c.RESULTS / "aq2_replication.csv")
b = pd.DataFrame({"sign": b["sign"].map(names), "adjusted_rd": b["rd_2013"], "adjusted_rd_2014": b["rd_2014"],
                  "n_support": b["n_2013"], "n_support_2014": b["n_2014"]})
run("aq2_adjusted_rd", b, prior[FILES[1]], ["sign"], ["n_support", "n_support_2014", "adjusted_rd", "adjusted_rd_2014"], 0.0005)

# AQ3: development choice and listed non-completers on the 2014 test, every method, cut-off and capacity
d = pd.read_csv(c.RESULTS / "aq3_test_pooled.csv")
d = d[d["method"] != "RANDOM"].assign(ranking=lambda x: x["method"].replace({"RULE": "B2_rule"}))
d = d.rename(columns={"tp": "non_completers_on_list", "k": "list_length"})
d[["cutoff", "per20"]] = d[["cutoff", "per20"]].astype(str)
run("aq3_test_listed", d[["ranking", "cutoff", "per20", "list_length", "non_completers_on_list"]], prior[FILES[2]],
    ["ranking", "cutoff", "per20"], ["list_length", "non_completers_on_list"], 0)
dev = pd.read_csv(c.RESULTS / "aq3_dev_summary.csv").rename(columns={"norm_recall": "pooled_normalised_recall"})
dev["ranking"] = dev["config"].replace({"RULE": "B2_rule"})
pd_ = pd.read_csv(prior[FILES[4]])
pd_[(pd_["cutoff"] == 27) & (pd_["per20"] == 5)].to_csv(tmp / "prior_dev_d27_k5.csv", index=False)
run("aq3_dev_choice", dev[["ranking", "pooled_normalised_recall"]], tmp / "prior_dev_d27_k5.csv",
    ["ranking"], ["pooled_normalised_recall"], 0.0005)

# AQ4: confirmatory fairness recalls
names4 = {"Declared disability": "Declared disability", "Most deprived band (0–10%)": "Deprivation band 0–10%",
          "Deprivation band missing": "Deprivation band missing"}
f = pd.read_csv(c.RESULTS / "aq4_fairness_confirmatory.csv")
f = f.assign(group=f["group"].map(names4), ranking="model")
theirs = pd.read_csv(prior[FILES[3]])
theirs[theirs["confirmatory"].astype(str).str.lower() == "true"].to_csv(tmp / "prior_fairness.csv", index=False)
run("aq4_fairness", f[["ranking", "group", "recall_group", "recall_others"]], tmp / "prior_fairness.csv",
    ["ranking", "group"], ["recall_group", "recall_others"], 0.0005)

out = pd.DataFrame(summary)
c.write(out, "compare_prior.csv")
print(out[["comparison", "rows_compared", "differences"]].to_string(index=False))
for _, r in out[out["differences"] > 0].iterrows():
    print(r["comparison"], "->", r["detail"][:600])
