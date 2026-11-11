"""AQ3 step 6 – secondary metrics, S2 and the calibration condition S3 (Tables 4.3 and 4.5; PROTOCOL.md P19).

Reads the scored test tables written by 05_test.py. Writes
  results/secondary.csv          within-run ROC-AUC and PR-AUC, precision against base rate and attainable maximum (S2)
  results/calibration.csv        calibration-in-the-large, slope, Brier score; S3 verdict for the chosen model
  results/calibration_bins.csv   observed against predicted risk in tenths of the predicted risk (chosen model, day 27)
  results/calibration_by_run.csv calibration-in-the-large per run (shows where the average risk is off)
  results/net_benefit.csv        net benefit of the model, of contacting everyone and of the rule's flags (context)
"""

import json

import numpy as np
import polars as pl

from aq3_models import CONFIGS, EXTRACT, RESULTS, lib

lib.open_test_outcomes("aq-3/code/06_secondary.py", "secondary metrics and calibration of the frozen models")
chosen = json.loads(lib.FREEZE_FILE.read_text())["chosen_config"]
pool = pl.read_csv(RESULTS / "test_pooled.csv")

sec, cal = [], []
for cut in (27, 13):
    d = pl.read_csv(EXTRACT / f"aq3_test_scored_d{cut}.csv")
    y, runs = d["non_completion"].to_numpy().astype(int), d["run"].to_numpy()
    for name in ["B2_rule", *CONFIGS]:
        roc, pr = lib.within_run_auc(runs, y, d[name].to_numpy())
        for per20 in (5, 3):
            p = pool.filter((pl.col("cutoff") == cut) & (pl.col("per20") == per20) & (pl.col("ranking") == name)).row(0, named=True)
            sec.append({"cutoff": cut, "per20": per20, "ranking": name, "precision": p["pooled_precision"], "base_rate": p["base_rate"],
                        "max_attainable_precision": p["max_attainable_precision"],
                        "share_of_way_from_base_to_max": (p["pooled_precision"] - p["base_rate"]) / (p["max_attainable_precision"] - p["base_rate"]),
                        "lift": p["pooled_lift"], "recall": p["pooled_recall"], "normalised_recall": p["pooled_normalised_recall"],
                        "roc_auc_within_run": roc, "pr_auc_within_run": pr, "pr_auc_chance_level": float(np.mean([y[runs == r].mean() for r in np.unique(runs)]))})
        if name in CONFIGS:
            c = lib.calibration(y, d[name].to_numpy())
            ok = (-0.2 <= c["citl"] <= 0.2) and (0.8 <= c["slope"] <= 1.2)
            cal.append({"cutoff": cut, "model": name, **c, "s3_bounds_met": ok})
sec, cal = pl.DataFrame(sec), pl.DataFrame(cal)
lib.banner("Secondary metrics on the 13 test runs")
print(lib.md_table(sec.filter(pl.col("per20") == 5)))
lib.save_csv(sec, RESULTS / "secondary.csv")

lib.banner("S2 (reported, not a gate): precision at capacity, day 27, 5 per 20")
s2 = sec.filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5) & pl.col("ranking").is_in([chosen, "B2_rule", "B3"]))
print(lib.md_table(s2.select("ranking", "precision", "base_rate", "max_attainable_precision", "share_of_way_from_base_to_max", "lift")))

lib.banner("Calibration of the frozen models on the test runs (no recalibration)")
print(lib.md_table(cal))
lib.save_csv(cal, RESULTS / "calibration.csv")
main = cal.filter((pl.col("cutoff") == 27) & (pl.col("model") == chosen)).row(0, named=True)
print(f"\n**S3, chosen model {chosen}, day 27:** calibration-in-the-large {main['citl']:+.3f} (bounds −0.2 to 0.2), slope {main['slope']:.3f} "
      f"(bounds 0.8 to 1.2); mean predicted risk {main['mean_predicted']:.3f} against observed {main['observed_rate']:.3f}. "
      f"**{'Met: probabilities may be shown' if main['s3_bounds_met'] else 'Not met: tutors see ranks and reasons only'}**.")

d = pl.read_csv(EXTRACT / "aq3_test_scored_d27.csv")
y, p = d["non_completion"].to_numpy().astype(float), d[chosen].to_numpy()
edges = np.linspace(0, 1, 11)
rows = []
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (p >= lo) & (p < hi) if hi < 1 else (p >= lo)
    if m.sum():
        rows.append({"predicted_from": lo, "predicted_to": hi, "enrolments": int(m.sum()), "mean_predicted": float(p[m].mean()),
                     "observed_rate": float(y[m].mean()), "gap_observed_minus_predicted": float(y[m].mean() - p[m].mean())})
bins = pl.DataFrame(rows)
print("\n**Observed against predicted risk, chosen model, day 27**\n\n" + lib.md_table(bins))
lib.save_csv(bins, RESULTS / "calibration_bins.csv")

byrun = []
for run in sorted(d["run"].unique().to_list()):
    m = (d["run"] == run).to_numpy()
    c = lib.calibration(y[m], p[m])
    byrun.append({"run": run, "enrolments": int(m.sum()), "observed_rate": c["observed_rate"], "mean_predicted": c["mean_predicted"], "citl": c["citl"], "slope": c["slope"]})
byrun = pl.DataFrame(byrun)
print("\n**Calibration per run, chosen model, day 27**\n\n" + lib.md_table(byrun))
lib.save_csv(byrun, RESULTS / "calibration_by_run.csv")

lib.banner("Net benefit (context: a threshold policy, not the fixed-capacity list)")
n = len(y)
rule = d["early_sign_rule"].to_numpy()
nb = []
for pt in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
    w = pt / (1 - pt)
    sel = p >= pt
    nb.append({"threshold_probability": pt,
               "model": float((y[sel].sum() - w * (1 - y[sel]).sum()) / n), "share_contacted_model": float(sel.mean()),
               "contact_all": float((y.sum() - w * (1 - y).sum()) / n), "contact_none": 0.0,
               "rule_flags": float((y[rule].sum() - w * (1 - y[rule]).sum()) / n), "share_contacted_rule": float(rule.mean())})
nb = pl.DataFrame(nb)
print(lib.md_table(nb))
lib.save_csv(nb, RESULTS / "net_benefit.csv")
