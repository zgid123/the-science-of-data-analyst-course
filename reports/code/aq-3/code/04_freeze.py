"""AQ3 step 4 – second freeze (Appendix III step 5; PROTOCOL.md P12).

For each cut-off, every configuration is tuned by leave-one-run-out on all 9 runs of 2013 and refitted on all 2013
rows. The fitted models, their specification and SHA-256 are written, and `results/freeze.json` records the time.
From this moment the library allows 2014 outcomes to be read, and each read is appended to logs/test-access.md.

Also frozen here: the labels-available variant (chosen configuration trained only on the 2013 February runs).

This script refuses to run when a freeze already exists: a model cannot be refrozen after the test was opened.

Rerun (PROTOCOL.md P23): the present freeze reproduces the freeze of the first run of this folder, whose 2014 results
were known when the rerun started. Nothing in the tuning or fitting below differs from the first run; only the record
written to freeze.json says so and keeps the first run's freeze time as history.
"""

import json
import platform
import subprocess
import sys

import joblib
import numpy as np
import polars as pl
import sklearn

from aq3_models import CONFIGS, EXTRACT, MODELS, RESULTS, fit_final, lib, predict, tune

if lib.freeze_exists():
    sys.exit("freeze.json already exists – the model is frozen; delete nothing, rerun nothing.")
choice = pl.read_csv(RESULTS / "model_choice.csv")
chosen = choice.filter(pl.col("chosen"))["config"][0]
MODELS.mkdir(parents=True, exist_ok=True)
lib.banner(f"AQ3 second freeze – chosen configuration {chosen}")

records, tuning = [], []
for cut in (27, 13):
    dev = pl.read_csv(EXTRACT / f"aq3_dev_d{cut}.csv")
    jobs = [(c, dev, c) for c in CONFIGS]
    b_runs = dev.filter(pl.col("start_month") == "B")
    jobs.append((chosen, b_runs, f"{chosen}_labels_available"))
    for cfg, train, name in jobs:
        hp, table = tune(cfg, cut, train)
        bundle = fit_final(cfg, cut, train, hp)
        path = MODELS / f"frozen_{name}_d{cut}.joblib"
        joblib.dump(bundle, path)
        spec = {"name": name, "config": cfg, "label": CONFIGS[cfg]["label"], "cutoff": cut, "hyperparameters": hp,
                "train_runs": bundle["train_runs"], "train_rows": bundle["train_rows"], "columns": bundle["prep"].names}
        if bundle["kind"] == "logit":
            prep, model = bundle["prep"], bundle["model"]
            spec.update({"intercept": float(model.intercept_[0]), "coefficients": dict(zip(prep.names, map(float, model.coef_[0]))),
                         "standardise_mean": dict(zip(prep.names, map(float, prep.mean))), "standardise_sd": dict(zip(prep.names, map(float, prep.sd))),
                         "median_fill": prep.medians, "levels": prep.levels, "constant_columns": prep.constant,
                         "parameters_excluding_intercept": len(prep.names)})
        (MODELS / f"frozen_{name}_d{cut}.spec.json").write_text(json.dumps(spec, indent=1))
        p = predict(bundle, train)
        records.append({"name": name, "config": cfg, "cutoff": cut, "hyperparameters": json.dumps(hp), "train_runs": len(bundle["train_runs"]),
                        "train_rows": bundle["train_rows"], "columns": len(bundle["prep"].names), "mean_fitted_risk_train": float(p.mean()),
                        "train_rate": float(train["non_completion"].mean()), "file": path.name, "sha256": lib.sha256(path)})
        for row in table:
            tuning.append({"name": name, "cutoff": cut, **{"grid_point": json.dumps({k: v for k, v in row.items() if k != 'inner_log_loss'})},
                           "loro_log_loss": row["inner_log_loss"]})
rec = pl.DataFrame(records)
print(lib.md_table(rec.select("name", "cutoff", "hyperparameters", "train_runs", "train_rows", "columns", "mean_fitted_risk_train", "train_rate", "sha256"), digits=4))
lib.save_csv(rec, RESULTS / "frozen_models.csv")
lib.save_csv(pl.DataFrame(tuning), RESULTS / "freeze_tuning.csv")

spec = json.loads((MODELS / f"frozen_M1_d27.spec.json").read_text())
coef = pl.DataFrame({"column": list(spec["coefficients"]), "coefficient_per_sd": list(spec["coefficients"].values())}).sort(pl.col("coefficient_per_sd").abs(), descending=True)
print(f"\n**Frozen M1 at day 27: {spec['parameters_excluding_intercept']} parameters besides the intercept (Level 1 expected 23); "
      f"coefficients per training standard deviation, log-odds scale**\n\n" + lib.md_table(coef))
lib.save_csv(coef, RESULTS / "frozen_M1_d27_coefficients.csv")

commit = subprocess.run(["git", "-C", str(lib.REPO), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
freeze = {"frozen_utc": lib.utc_now(), "chosen_config": chosen, "chosen_label": CONFIGS[chosen]["label"],
          "prepared_dataset": lib.PREPARED_VERSION, "seed": lib.SEED, "git_commit": commit,
          "python": platform.python_version(), "scikit_learn": sklearn.__version__, "numpy": np.__version__, "polars": pl.__version__,
          "models": {f"{r['name']}_d{r['cutoff']}": {"sha256": r["sha256"], "hyperparameters": json.loads(r["hyperparameters"])} for r in records},
          "run_kind": lib.RUN_KIND,
          "test_outcomes_read_by_scripts_of_this_rerun_before_this_freeze": False,
          "test_outcomes_known_to_the_analyst_before_this_freeze": True,
          "first_run": {"git_commit": lib.FIRST_RUN_COMMIT, "frozen_utc": lib.FIRST_RUN_FREEZE_UTC,
                        "first_test_access_utc": lib.FIRST_RUN_FIRST_TEST_ACCESS_UTC}}
lib.FREEZE_FILE.write_text(json.dumps(freeze, indent=1))
print(f"\n**Frozen at {freeze['frozen_utc']}** – written to aq-3/results/freeze.json. No script of this rerun has read a 2014 outcome "
      f"before this line. This freeze reproduces the first run's freeze of {lib.FIRST_RUN_FREEZE_UTC}, whose test results were "
      f"known to the analyst when the rerun started; it is not a second blind test.")
