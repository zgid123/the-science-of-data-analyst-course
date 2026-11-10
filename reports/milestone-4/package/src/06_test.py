"""Step 6 of Appendix III: the single test on the 13 runs of 2014.

Order: (1) refuse if the test access is already recorded (unless --reproduce); (2) re-verify both frozen model hashes
against results/freeze.csv; (3) fit B3 on all 2013 runs (M1 procedure) and record its hash; (4) write
first_test_access_utc into freeze.csv and an experiment-log entry; (5) only then load the 2014 rows and score them.
--reproduce recomputes test_runs.csv with the same frozen models (no refit, no tuning) and checks byte identity.

Run: venv/bin/python reports/milestone-4/package/src/06_test.py [--reproduce]
Writes results/test_runs.csv, results/b3_fit.csv, models/fitted_B3_d<cutoff>.joblib.
"""
import argparse
import datetime as dt
import io
import json
import platform
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import common as C


def guard(reproduce: bool) -> str:
    t = C.test_access_time()
    if t and not reproduce:
        raise SystemExit(f"REFUSED: the 2014 test was already accessed at {t}; use --reproduce to recompute")
    if reproduce and not t:
        raise SystemExit("REFUSED: --reproduce needs a recorded test access; none found")
    return t


def verify_frozen() -> list[tuple[str, str]]:
    out = []
    for _, r in C.read_freeze().iterrows():
        got = C.sha256(C.PKG / r["parameter_file"])
        if got != r["model_sha256"]:
            raise SystemExit(f"STOP: frozen model {r['parameter_file']} hash {got} != freeze.csv {r['model_sha256']}")
        out.append((r["parameter_file"], got))
    return out


def fit_b3(m3: Path) -> None:
    sets = C.predictor_sets(m3)
    rows = []
    for cutoff in C.CUTOFFS:
        df = C.load_view(cutoff, m3)
        cols = C.columns_for("B3", cutoff, sets)
        with threadpool_limits(limits=1):
            params, _ = C.tune("B3", cols, df)
            pipe = C.fit_pipeline("B3", cols, params, df)
        path = C.MODELS / f"fitted_B3_d{cutoff}.joblib"
        joblib.dump(pipe, path, compress=3)
        rows.append({"cutoff": cutoff, "params": json.dumps(params, sort_keys=True), "columns": json.dumps(cols),
                     "parameter_file": f"models/{path.name}", "model_sha256": C.sha256(path)})
        print(f"B3 day {cutoff}: {params} sha256 {rows[-1]['model_sha256']}")
    pd.DataFrame(rows).to_csv(C.B3_FIT_CSV, index=False)


def record_access(hashes) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fr = C.read_freeze()
    fr["first_test_access_utc"] = now
    fr.to_csv(C.FREEZE_CSV, index=False)
    b3 = pd.read_csv(C.B3_FIT_CSV, dtype=str)
    lines = [f"## Test access {now} (phase 2, step 6: single test on the 13 runs of 2014)", "",
             f"- first_test_access_utc: {now} (written to results/freeze.csv before any 2014 row was read)",
             f"- Command: `{' '.join(sys.argv)}`", f"- Git commit: {C.git_commit()}",
             f"- Python {platform.python_version()}",
             "- Frozen models re-verified against results/freeze.csv: "
             + "; ".join(f"{p} sha256 {h} OK" for p, h in hashes),
             "- B3 (fitted on all 2013 runs before access): "
             + "; ".join(f"{r.parameter_file} sha256 {r.model_sha256}" for r in b3.itertuples()),
             f"- Seeds: SEED={C.SEED}; B1 draws default_rng([SEED, 2014, cutoff, run index]), {C.B1_DRAWS} draws", ""]
    with open(C.LOGS / "experiment_log.md", "a") as f:
        f.write("\n".join(lines) + "\n")
    print(f"test access recorded at {now}")
    return now


def score(m3: Path) -> pd.DataFrame:
    rows = []
    for cutoff in C.CUTOFFS:
        df = C.test_scores(cutoff, m3)
        print(f"day {cutoff}: {len(df)} test enrolments in {df[C.RUN].nunique()} runs of 2014")
        for ri, (run, g) in enumerate(df.groupby(C.RUN, sort=True)):
            y = g["y"].to_numpy()
            n = len(g)
            rng = np.random.default_rng([C.SEED, C.TEST_YEAR, cutoff, ri])
            draws = [rng.permutation(n) for _ in range(C.B1_DRAWS)]
            aucs = []
            for d in draws:
                s = np.empty(n)
                s[d] = np.arange(n, 0, -1)
                aucs.append(C.within_run_auc(y, s))
            orders = {"B2": (C.b2_order(g), C.within_run_auc(y, C.rule_score(g)))}
            for cfg in ("B3", "M1"):
                sc = g[f"score_{cfg}"].to_numpy()
                orders[cfg] = (C.model_order(g, sc), C.within_run_auc(y, sc))
            for per20 in C.PER20:
                k = C.list_length(n, per20)
                rows.append({"config": "B1", "cutoff": cutoff, "k": per20, "test_run": run,
                             **C.run_metrics(y, np.mean([C.on_list(d, k) for d in draws], axis=0), k,
                                             float(np.mean(aucs)))})
                for cfg, (order, auc) in orders.items():
                    rows.append({"config": cfg, "cutoff": cutoff, "k": per20, "test_run": run,
                                 **C.run_metrics(y, C.on_list(order, k), k, auc)})
    out = pd.DataFrame(rows)
    cols = ["config", "cutoff", "k", "test_run"] + C.DEV_COLUMNS[4:]
    return out[cols].sort_values(["config", "cutoff", "k", "test_run"]).reset_index(drop=True)


def to_csv_bytes(df: pd.DataFrame) -> bytes:
    buf = io.StringIO()
    df.to_csv(buf, index=False, float_format="%.6f")
    return buf.getvalue().encode()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m3", type=Path, default=C.M3_DEFAULT)
    ap.add_argument("--reproduce", action="store_true")
    a = ap.parse_args()
    t = guard(a.reproduce)
    hashes = verify_frozen()
    for p, h in hashes:
        print(f"frozen {p} sha256 {h} OK")
    if not a.reproduce:
        fit_b3(a.m3)
        t = record_access(hashes)
    else:
        for cutoff in C.CUTOFFS:
            C.fitted_b3(cutoff)   # verifies the B3 hash; never refits
        print(f"reproduce mode: access recorded at {t}; no refit, no tuning")
    out = to_csv_bytes(score(a.m3))
    path = C.RESULTS / "test_runs.csv"
    if a.reproduce and not path.exists():
        path.write_bytes(out)
        print(f"reproduce: {path} was missing (interrupted first run); written from the frozen models")
    elif a.reproduce:
        same = path.read_bytes() == out
        print("reproduce: test_runs.csv byte-identical" if same else "reproduce: test_runs.csv DIFFERS")
        if not same:
            raise SystemExit(1)
    else:
        path.write_bytes(out)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
