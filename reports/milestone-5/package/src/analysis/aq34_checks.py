"""Checks of the AQ3 and AQ4 results (run_all.sh step 22; exit 1 on any failed check).

1. Populations: 2013 training rows (11,811 at day 27; 12,080 at day 13) and 2014 test rows (15,724; 15,989).
2. Order of work: the freeze record exists and was written before the 2014 scores.
3. Second code path: the non-completers on the lists of the chosen model and of the rule, recounted from the saved
   scores with a separate ranking routine (pandas sort), equal results/aq3/test_pooled.csv.
4. Agreement with the Milestone 4 draft package (data/metadata/aq34_reference_m4.csv): same chosen configuration,
   identical rule-ranked list at day 27 and 5 per 20, model list within the stated tolerance.
5. No result file of results/aq3/ or results/aq4/ holds a student identifier.

Usage (from the package folder): python src/analysis/aq34_checks.py
Writes data/metadata/aq34_checks.csv.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import pandas as pd

import aq34_common as c

rows = []


def check(name: str, ok: bool, detail: str) -> None:
    rows.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})


freeze = json.loads((c.WORK / "freeze.json").read_text())
chosen = freeze["choices"]["chosen_configuration"]
pooled = pd.read_csv(c.RES3 / "test_pooled.csv")

# 1. populations
for cut, n13, n14 in [(27, 11811, 15724), (13, 12080, 15989)]:
    a, b = len(c.features(cut, year=2013)), len(c.features(cut, year=2014))
    check(f"populations at day {cut}", (a, b) == (n13, n14), f"2013: {a} (plan {n13}); 2014: {b} (plan {n14})")

# 2. order of work
scores = c.WORK / "scores_d27.csv"
frozen = pd.Timestamp(freeze["frozen_utc"])
written = pd.Timestamp(scores.stat().st_mtime, unit="s", tz="UTC")
check("freeze before the 2014 scores", frozen <= written, f"frozen {frozen}, scores written {written.floor('s')}")

# 3. second code path for the list counts
s = pd.read_csv(scores)
for col, method in [(chosen, chosen), ("rule", "RULE")]:
    tp = 0
    for _, g in s.groupby("run"):
        k = min(len(g), 5 * math.ceil(len(g) / 20))
        tp += int(g.sort_values([col, "tiebreak_u"], ascending=[False, True]).head(k)["y"].sum())
    ref = pooled.query("cutoff == 27 and per20 == 5 and method == @method")["tp"].iloc[0]
    check(f"listed non-completers recounted, {method}", tp == ref, f"recount {tp}, results {ref:.0f}")

# 4. agreement with the Milestone 4 draft package
with open(c.META / "aq34_reference_m4.csv", newline="") as fh:
    ref = {r["quantity"]: r for r in csv.DictReader(fh)}
check("same chosen configuration as Milestone 4", chosen == ref["chosen configuration"]["value"], f"{chosen}")
for key, method in [("rule-ranked list: non-completers listed at day 27 and 5 per 20 (13 runs of 2014)", "RULE"),
                    ("M1 list: non-completers listed at day 27 and 5 per 20 (13 runs of 2014)", "M1")]:
    mine = pooled.query("cutoff == 27 and per20 == 5 and method == @method")["tp"].iloc[0]
    want, tol = float(ref[key]["value"]), float(ref[key]["tolerance"])
    check(f"{method} list against Milestone 4", abs(mine - want) <= tol, f"{mine:.0f} against {want:.0f} (tolerance {tol:.0f})")

# 5. no student identifier in the shipped results
leaks = [str(p.relative_to(c.ROOT)) for d in (c.RES3, c.RES4) for p in d.glob("*.csv")
         if "id_student" in Path(p).read_text().splitlines()[0]]
check("no student identifier in results/aq3 and results/aq4", not leaks, ", ".join(leaks) or "none")

out = pd.DataFrame(rows)
out.to_csv(c.META / "aq34_checks.csv", index=False, lineterminator="\n")
print(out.to_string(index=False))
failed = int((out["status"] == "FAIL").sum())
print(f"{len(out) - failed} of {len(out)} AQ3/AQ4 checks passed")
sys.exit(1 if failed else 0)
