"""Step 5 of Appendix III, second freeze: refit the chosen configuration on all 9 runs of 2013 (one model per cut-off),
its setting tuned by leave-one-run-out over the 9 runs, then save the fitted pipeline, its SHA-256 and its spec.

`first_test_access_utc` stays empty: phase 2 (06_test) fills it when the 2014 outcomes are opened.

Run: venv/bin/python reports/milestone-4/package/src/05_freeze.py
Reads results/model_choice.csv; writes models/frozen_<config>_d<cutoff>.joblib, models/frozen_<config>_d<cutoff>.spec.json,
results/freeze_tuning.csv and results/freeze.csv.
"""
import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
import sklearn
from threadpoolctl import threadpool_limits

import common as C


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m3", type=Path, default=C.M3_DEFAULT)
    a = ap.parse_args()
    if C.test_access_time():
        raise SystemExit(f"REFUSED: the test was accessed at {C.test_access_time()}; the freeze cannot be redone")
    C.MODELS.mkdir(parents=True, exist_ok=True)

    choice = pd.read_csv(C.RESULTS / "model_choice.csv")
    chosen = choice.loc[choice["chosen"] == "yes", "config"]
    assert len(chosen) == 1, chosen
    cfg = chosen.iloc[0]
    sets = C.predictor_sets(a.m3)
    rows, tunings = [], []
    for cutoff in C.CUTOFFS:
        df = C.load_view(cutoff, a.m3)
        C.assert_2013(df)
        cols = C.columns_for(cfg, cutoff, sets)
        with threadpool_limits(limits=1):
            params, table = C.tune(cfg, cols, df)
            pipe = C.fit_pipeline(cfg, cols, params, df)
        tunings += [{"config": cfg, "cutoff": cutoff, "grid_index": t["grid_index"],
                     "params": json.dumps(t["params"], sort_keys=True), "inner_pooled_nr": t["inner_pooled_nr"],
                     "chosen": t["params"] == params} for t in table]
        stem = f"frozen_{cfg}_d{cutoff}"
        model_path = C.MODELS / f"{stem}.joblib"
        joblib.dump(pipe, model_path, compress=3)
        digest = C.sha256(model_path)
        spec = {
            "config": cfg, "model": C.CONFIGS[cfg][1], "predictor_set": C.CONFIGS[cfg][2], "cutoff_day": cutoff,
            "columns": cols, "params": params, "seed": C.SEED,
            "training": {"runs": sorted(df[C.RUN].unique()), "rows": len(df), "noncompleters": int(df["y"].sum()),
                         "year": C.DEV_YEAR},
            "tuning": {"method": "leave-one-run-out over the 9 runs of 2013, overlapping students removed from "
                                 "each inner training set", "criterion": "pooled normalised recall, k = 5 per 20",
                       "grid": C.grid_for(cfg)},
            "data_version": C.DATA_VERSION, "sklearn": sklearn.__version__,
            "model_file": f"models/{model_path.name}", "model_sha256": digest,
        }
        if C.CONFIGS[cfg][1] == "logistic":
            names = list(pipe.named_steps["prep"].named_steps["encode"].get_feature_names_out())
            spec["coefficients"] = dict(zip(names, map(float, pipe.named_steps["model"].coef_[0])))
            spec["intercept"] = float(pipe.named_steps["model"].intercept_[0])
        (C.MODELS / f"{stem}.spec.json").write_text(json.dumps(spec, indent=1))
        print(f"day {cutoff}: {cfg} params {params}, {len(df)} rows, sha256 {digest}")
        rows.append({"chosen_config": cfg,
                     "spec": f"{cfg} {C.CONFIGS[cfg][1]} {C.CONFIGS[cfg][2]} cutoff={cutoff} params="
                             f"{json.dumps(params, sort_keys=True)} seed={C.SEED} spec=models/{stem}.spec.json",
                     "parameter_file": f"models/{model_path.name}", "model_sha256": digest,
                     "first_test_access_utc": ""})
    pd.DataFrame(tunings).to_csv(C.RESULTS / "freeze_tuning.csv", index=False, float_format="%.6f")
    pd.DataFrame(rows).to_csv(C.RESULTS / "freeze.csv", index=False)


if __name__ == "__main__":
    main()
