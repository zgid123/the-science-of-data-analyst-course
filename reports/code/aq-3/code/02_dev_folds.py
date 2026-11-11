"""AQ3 step 2 – baselines and candidates on the development folds (brief steps 2–4; Appendix III steps 2–3).

Data: the 9 runs of 2013 only. Each run is the validation fold once (leave-one-run-out). Inside each fold:
  - enrolments of students who also appear in the validation run are removed from training;
  - hyperparameters are tuned by an inner leave-one-run-out loop on the training runs (same removal rule);
  - every transform (median filling, coding, scaling) is fitted on the training rows only.
Baselines B1 (random, analytic expectation) and B2 (rule-ranked list) are scored on the same folds, first.

Writes  extracted-datasets/aq3_dev_oof_scores_d<c>.csv   out-of-fold score of every configuration per enrolment
        results/dev_folds.csv        list metrics per ranking, cut-off, capacity and validation run
        results/dev_pooled.csv       the same pooled over the 9 folds
        results/dev_tuning.csv       chosen hyperparameters and inner log loss of every grid point, per fold
        results/dev_fold_design.csv  rows removed per fold
Fold results serve the model choice only; they are not expected performance.
"""

import json
import os
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np
import polars as pl
from joblib import Parallel, delayed

from aq3_models import CONFIGS, EXTRACT, RESULTS, fit_final, lib, metrics_rows, pooled, predict, rule_score, tune, without_students_of


def one_fold(config: str, cutoff: int, run: str):
    dev = pl.read_csv(EXTRACT / f"aq3_dev_d{cutoff}.csv")
    va = dev.filter(pl.col("run") == run)
    other = dev.filter(pl.col("run") != run)
    tr = without_students_of(other, va)
    t0 = time.time()
    hp, table = tune(config, cutoff, tr)
    bundle = fit_final(config, cutoff, tr, hp)
    p = predict(bundle, va)
    return {"config": config, "cutoff": cutoff, "run": run, "hp": hp, "table": table, "seconds": time.time() - t0,
            "train_rows": tr.height, "rows_removed": other.height - tr.height,
            "students_removed": other.filter(pl.col("id_student").is_in(va["id_student"].unique().to_list()))["id_student"].n_unique(),
            "scores": va.select(lib.KEYS).with_columns(pl.Series(config, p))}


if __name__ == "__main__":
    lib.banner("AQ3 development folds (2013 runs only)")
    tasks = [(c, cut, r) for cut in (27, 13) for c in CONFIGS
             for r in sorted(pl.read_csv(EXTRACT / f"aq3_dev_d{cut}.csv")["run"].unique().to_list())]
    print(f"{len(tasks)} fits = 5 configurations x 2 cut-offs x 9 validation runs, each with an inner 8-run tuning loop")
    t0 = time.time()
    res = Parallel(n_jobs=min(10, os.cpu_count() or 1))(delayed(one_fold)(*t) for t in tasks)
    print(f"finished in {time.time() - t0:.0f} s")

    metrics, tuning, design = [], [], []
    for cut in (27, 13):
        dev = pl.read_csv(EXTRACT / f"aq3_dev_d{cut}.csv")
        scores = dev.select(lib.KEYS + ["run", "non_completion", "final_result", "tiebreak_u"]).with_columns(pl.Series("B2_rule", rule_score(dev)))
        for cfg in CONFIGS:
            part = pl.concat([r["scores"] for r in res if r["config"] == cfg and r["cutoff"] == cut])
            scores = scores.join(part, on=lib.KEYS, how="left", validate="1:1")
            assert scores[cfg].null_count() == 0
        lib.save_csv(scores.sort(lib.KEYS), EXTRACT / f"aq3_dev_oof_scores_d{cut}.csv", "out-of-fold scores, 2013 runs")
        metrics.append(metrics_rows(scores, {"B2_rule": "B2_rule", **{c: c for c in CONFIGS}}, cut))
        for r in res:
            if r["cutoff"] != cut:
                continue
            design.append({"cutoff": cut, "config": r["config"], "validation_run": r["run"], "train_rows": r["train_rows"],
                           "students_removed": r["students_removed"], "rows_removed": r["rows_removed"], "seconds": round(r["seconds"], 1)})
            for row in r["table"]:
                hp = {k: v for k, v in row.items() if k != "inner_log_loss"}
                tuning.append({"cutoff": cut, "config": r["config"], "validation_run": r["run"], "grid_point": json.dumps(hp),
                               "inner_log_loss": row["inner_log_loss"], "chosen": hp == r["hp"]})
    metrics = pl.concat(metrics)
    lib.save_csv(metrics, RESULTS / "dev_folds.csv")
    lib.save_csv(pl.DataFrame(tuning), RESULTS / "dev_tuning.csv")
    design = pl.DataFrame(design)
    lib.save_csv(design, RESULTS / "dev_fold_design.csv")
    pool = pooled(metrics)
    lib.save_csv(pool, RESULTS / "dev_pooled.csv")

    d = design.filter((pl.col("config") == "M1") & (pl.col("cutoff") == 27)).select("validation_run", "train_rows", "students_removed", "rows_removed")
    print("\n**Fold design at day 27 (the same for every configuration)**\n\n" + lib.md_table(d))
    chosen = pl.DataFrame(tuning).filter(pl.col("chosen")).group_by("cutoff", "config", "grid_point").agg(pl.len().alias("folds")).sort("cutoff", "config", "folds", descending=[True, False, True])
    print("\n**Hyperparameters chosen by the inner loops (number of outer folds)**\n\n" + lib.md_table(chosen))
    show = pool.select("cutoff", "per20", "ranking", "non_completers_on_list", "max_attainable", "pooled_normalised_recall",
                       "random_list_normalised_recall", "pooled_recall", "pooled_precision", "base_rate", "pooled_lift")
    print("\n**Pooled over the 9 development folds (for the model choice only)**\n\n" + lib.md_table(show))
