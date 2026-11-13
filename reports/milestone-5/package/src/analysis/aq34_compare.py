"""AQ3 and AQ4: 2013 against 2014, as aq_year_compare.py does for AQ1 and AQ2.

For AQ3/AQ4 the two years play different roles: the 2013 numbers are development estimates (each run scored by the
leave-one-run-out model that left it out), the 2014 numbers the single test of the model frozen on 2013. Their
difference shows how much the model keeps on a later year; it is a description, not a test, and it cannot change
gate S1, which is judged on 2014 alone.

Reads results/2013/ and results/2014/ (aq3_pooled.csv, aq3_discrimination_calibration.csv, aq4_contact_yield.csv),
written by aq34_scopes.py.

Usage (from the package folder): python src/analysis/aq34_compare.py   (run_all.sh step 25)
Writes results/compare/aq3_dev_vs_test.csv, aq4_dev_vs_test.csv, aq3_summary.md.
"""
from __future__ import annotations

import pandas as pd

import aq34_common as c

KEEP = ["method", "name"]
dev = pd.read_csv(c.R2013 / "aq3_pooled.csv").query("cutoff == 27 and per20 == 5").set_index("method")
test = pd.read_csv(c.R2014 / "aq3_pooled.csv").query("cutoff == 27 and per20 == 5").set_index("method")
ddev = pd.read_csv(c.R2013 / "aq3_discrimination_calibration.csv").query("cutoff == 27").set_index("method")
dtest = pd.read_csv(c.R2014 / "aq3_discrimination_calibration.csv").query("cutoff == 27").set_index("method")
rows = []
for m in dev.index:
    row = {"method": m, "name": dev.loc[m, "name"], "n_2013": int(dev.loc[m, "n"]), "n_2014": int(test.loc[m, "n"])}
    for col in ["norm_recall", "recall", "precision", "lift"]:
        row[f"{col}_2013_dev"], row[f"{col}_2014_test"] = dev.loc[m, col], test.loc[m, col]
        row[f"{col}_test_minus_dev"] = test.loc[m, col] - dev.loc[m, col]
    if m in ddev.index:
        for col in ["roc_auc_within_run", "citl", "slope"]:
            if col in ddev.columns and pd.notna(ddev.loc[m, col]):
                row[f"{col}_2013_dev"], row[f"{col}_2014_test"] = ddev.loc[m, col], dtest.loc[m, col]
    rows.append(row)
out = pd.DataFrame(rows)
c.write(out, c.RCMP, "aq3_dev_vs_test.csv")

ydev = pd.read_csv(c.R2013 / "aq4_contact_yield.csv").query("method == 'model'").set_index("contact")
ytest = pd.read_csv(c.R2014 / "aq4_contact_yield.csv").query("method == 'model'").set_index("contact")
y = pd.DataFrame({"contact": ydev.index, "precision_2013_dev": ydev["precision"].to_numpy(),
                  "precision_2014_test": ytest.loc[ydev.index, "precision"].to_numpy(),
                  "base_rate_2013": ydev["base_rate"].to_numpy(), "base_rate_2014": ytest.loc[ydev.index, "base_rate"].to_numpy()})
y["test_minus_dev"] = y["precision_2014_test"] - y["precision_2013_dev"]
c.write(y, c.RCMP, "aq4_dev_vs_test.csv")

r = out.set_index("method")
lines = ["# AQ3 and AQ4: 2013 development estimates against the 2014 test", "",
         "2013: each run scored by the leave-one-run-out model that left it out (development estimate). 2014: the single "
         "test of the model frozen on 2013. Gate S1 is judged on 2014 alone.", ""]
for m in ["M1", "RULE", "B3"]:
    lines.append(f"- {r.loc[m, 'name']}: normalised recall {r.loc[m, 'norm_recall_2013_dev']:.3f} (2013) against "
                 f"{r.loc[m, 'norm_recall_2014_test']:.3f} (2014), {r.loc[m, 'norm_recall_test_minus_dev']:+.3f}.")
lines.append(f"- Yield of the 1st, 5th and 7th contact per 20 (model): {ydev.loc[1, 'precision']:.1%}, {ydev.loc[5, 'precision']:.1%}, "
             f"{ydev.loc[7, 'precision']:.1%} in 2013; {ytest.loc[1, 'precision']:.1%}, {ytest.loc[5, 'precision']:.1%}, "
             f"{ytest.loc[7, 'precision']:.1%} in 2014.")
(c.RCMP / "aq3_summary.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
