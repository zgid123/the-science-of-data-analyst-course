"""Shared code of the Milestone 4 Level 2 prototype (team N04), phase 1: development on 2013 and freeze.

Everything here follows the package contract (README.md) and Milestone 4 report Appendices II-III.
Implementation choices that the contract leaves open are listed in DEVIATIONS and in the experiment log.

The 2014 runs stay closed in phase 1: every loader filters `year == 2013` while scanning, and
`assert_2013` is called on every frame, fold and fit.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

# ---------------------------------------------------------------- paths and constants
PKG = Path(__file__).resolve().parents[1]                       # reports/milestone-4/package
M3_DEFAULT = PKG.parents[1] / "milestone-3" / "package"          # Milestone 3 prepared package
RESULTS = PKG / "results"
MODELS = PKG / "models"
LOGS = PKG / "logs"

DATA_VERSION = "OULAD-N04-prepared-1.0"
DEV_YEAR = 2013
SEED = 20131                     # one seed for every random step of phase 1
B1_DRAWS = 100                   # random-list draws (protocol states none; task default 100)
CUTOFFS = (13, 27)
PER20 = (3, 5)                   # capacity: contacts per tutor group of 20
MAIN_CUTOFF, MAIN_PER20 = 27, 5  # S1 operating point, also the model-choice and tuning point
MARGIN = 0.03                    # Appendix III step 4
MIN_FOLDS_WITH_GAIN = 7

# Tuning grids, ordered simplest first (ties go to the first, i.e. simplest, setting).
C_GRID = (1e-5, 1e-4, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0)           # inverse L2 penalty; smaller C = stronger shrinkage
TREE_GRID = tuple(
    {"max_depth": d, "max_iter": n, "learning_rate": lr}
    for d in (2, 3) for n in (100, 300) for lr in (0.05, 0.1)
)

CONFIGS = {
    # id: (kind, model family, predictor set)
    "B1": ("baseline", "random", None),
    "B2": ("baseline", "rule", None),
    "B3": ("baseline", "logistic", "background"),
    "M1": ("primary", "logistic", "primary"),
    "M2": ("challenger", "logistic", "extended"),
    "M3": ("challenger", "trees", "primary"),
    "M4": ("challenger", "trees", "extended"),
}
SIMPLICITY_ORDER = ("M1", "M2", "M3", "M4")   # ties go to the simpler model

# ---------------------------------------------------------------- column kinds (contract table)
NOMINAL = ("code_module", "start_month")
EDUCATION_ORDER = {  # data_dictionary.md: ordered; transform_params.json ordinal_codes
    "No Formal quals": 0,
    "Lower Than A Level": 1,
    "A Level or Equivalent": 2,
    "HE Qualification": 3,
    "Post Graduate Qualification": 4,
}
BOOLEAN = ("inactive_last7", "registration_missing")
NOT_COUNTS = ("registration_lead", "activity_ratio_run", "trend_last_week", "days_since_last_click")
NO_INDICATOR = ("registration_lead",)   # its indicator is the extended predictor registration_missing
BACKGROUND = ("code_module", "start_month", "num_of_prev_attempts", "studied_credits",
              "highest_education", "registration_lead")
RULE_SIGNS = ("rule_missed", "rule_tma_late", "inactive_last7")   # C10: the three signs

RUN = "run"   # derived id: code_module + "_" + code_presentation


# ---------------------------------------------------------------- input checks and loading
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_hashes(m3: Path = M3_DEFAULT) -> list[dict]:
    """Check every processed file listed in version_manifest.json; raise on any mismatch."""
    manifest = json.loads((m3 / "data/metadata/version_manifest.json").read_text())
    if manifest["prepared_dataset_version"] != DATA_VERSION:
        raise SystemExit(f"STOP: data version {manifest['prepared_dataset_version']} != {DATA_VERSION}")
    rows = []
    for name, spec in sorted(manifest["outputs"].items()):
        got = sha256(m3 / "data/processed" / name)
        rows.append({"file": f"data/processed/{name}", "expected": spec["sha256"], "actual": got,
                     "match": got == spec["sha256"]})
    bad = [r["file"] for r in rows if not r["match"]]
    if bad:
        raise SystemExit(f"STOP: hash mismatch for {bad}")
    return rows


def metadata_hashes(m3: Path = M3_DEFAULT) -> dict:
    """Metadata files the package reads; the manifest carries no hash for them, so they are recorded."""
    return {f"data/metadata/{n}": sha256(m3 / "data/metadata" / n)
            for n in ("version_manifest.json", "predictor_sets.json", "data_dictionary.md")}


def assert_2013(df) -> None:
    """Guard: no 2014 row may enter a frame, a fold or a fit in phase 1."""
    if isinstance(df, pl.DataFrame):
        years = set(df["year"].unique().to_list()) if "year" in df.columns else None
        pres = df["code_presentation"].to_list()
    else:
        years = set(pd.unique(df["year"]).tolist()) if "year" in df.columns else None
        pres = list(df["code_presentation"])
    if years is not None and years - {DEV_YEAR}:
        raise AssertionError(f"2013-only guard: found years {sorted(years)}")
    if any(not str(p).startswith(str(DEV_YEAR)) for p in pres):
        raise AssertionError("2013-only guard: found a presentation outside 2013")


def _to_pandas(df: pl.DataFrame) -> pd.DataFrame:
    out = {}
    for c in df.columns:
        s = df[c]
        if s.dtype == pl.String:
            out[c] = np.array(s.to_list(), dtype=object)
        elif s.dtype == pl.Boolean:
            out[c] = s.to_numpy().astype(bool)
        else:
            out[c] = s.cast(pl.Float64).to_numpy() if s.null_count() else s.to_numpy()
    return pd.DataFrame(out)


def load_view(cutoff: int, m3: Path = M3_DEFAULT) -> pd.DataFrame:
    """Feature view at the cut-off, 2013 rows only (filter applied while scanning)."""
    lf = pl.scan_parquet(m3 / f"data/processed/features_d{cutoff}.parquet")
    df = lf.filter(pl.col("year") == DEV_YEAR).collect()
    assert_2013(df)
    pdf = _to_pandas(df)
    pdf[RUN] = pdf["code_module"] + "_" + pdf["code_presentation"]
    pdf["y"] = pdf["non_completion"].astype(int)
    return pdf


def load_capacity(m3: Path = M3_DEFAULT) -> pd.DataFrame:
    lf = pl.scan_parquet(m3 / "data/processed/capacity_by_run.parquet")
    df = lf.filter(pl.col("code_presentation").str.starts_with(str(DEV_YEAR))).collect()
    assert_2013(df)
    pdf = _to_pandas(df)
    pdf[RUN] = pdf["code_module"] + "_" + pdf["code_presentation"]
    return pdf


def predictor_sets(m3: Path = M3_DEFAULT) -> dict:
    spec = json.loads((m3 / "data/metadata/predictor_sets.json").read_text())
    excluded = set(spec.get("not_used_in_milestone4", {}))
    primary = [c for c in spec["primary"] if c not in excluded]
    extended = primary + list(spec["extended"])
    return {
        "background": list(BACKGROUND),
        "primary": primary,
        "extended": {c: extended + list(spec["weekly_clicks"][f"d{c}"]) for c in CUTOFFS},
    }


def columns_for(config: str, cutoff: int, sets: dict) -> list[str]:
    pset = CONFIGS[config][2]
    if pset == "extended":
        return list(sets["extended"][cutoff])
    return list(sets[pset])


# ---------------------------------------------------------------- per-fold preprocessing (logistic models)
class DeviationCoder(BaseEstimator, TransformerMixin):
    """Deviation (sum) coding over the levels seen in fit; the last level is coded -1 on every column.
    An unseen level gets all zeros, i.e. the average level."""

    def fit(self, X, y=None):
        col = np.asarray(X).ravel()
        self.levels_ = sorted(set(col.tolist()))
        return self

    def transform(self, X):
        col = np.asarray(X).ravel()
        m = len(self.levels_)
        out = np.zeros((len(col), max(m - 1, 0)))
        for j, lev in enumerate(self.levels_[:-1]):
            out[col == lev, j] = 1.0
        if m > 1:
            out[col == self.levels_[-1], :] = -1.0
        return out

    def get_feature_names_out(self, input_features=None):
        name = input_features[0] if input_features is not None else "x"
        return np.array([f"{name}={lev}" for lev in self.levels_[:-1]], dtype=object)


class OrdinalMap(BaseEstimator, TransformerMixin):
    """Fixed ordinal code (no learning); an unknown level is an error."""

    def __init__(self, mapping=None):
        self.mapping = mapping

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        col = np.asarray(X).ravel()
        bad = set(col.tolist()) - set(self.mapping)
        if bad:
            raise ValueError(f"unknown ordinal levels {bad}")
        return np.array([self.mapping[v] for v in col], dtype=float).reshape(-1, 1)

    def get_feature_names_out(self, input_features=None):
        return np.asarray(input_features, dtype=object)


class FoldNumeric(BaseEstimator, TransformerMixin):
    """Training-fold median fill (+ 0/1 indicator for columns with nulls in the training fold, if
    `indicator`), then optional log(1 + x). Indicators are appended after the value columns."""

    def __init__(self, log=False, indicator=True):
        self.log = log
        self.indicator = indicator

    def fit(self, X, y=None):
        A = np.asarray(X, dtype=float)
        self.n_features_in_ = A.shape[1]
        self.feature_names_in_ = np.asarray(getattr(X, "columns", [f"x{i}" for i in range(A.shape[1])]),
                                            dtype=object)
        miss = np.isnan(A)
        self.median_ = np.array([np.median(A[~miss[:, j], j]) if (~miss[:, j]).any() else 0.0
                                 for j in range(A.shape[1])])
        self.missing_cols_ = np.where(miss.any(axis=0))[0] if self.indicator else np.array([], dtype=int)
        if self.log:
            if np.nanmin(A) < 0:
                raise ValueError("log1p on a negative count")
        return self

    def transform(self, X):
        A = np.asarray(X, dtype=float).copy()
        miss = np.isnan(A)
        ind = miss[:, self.missing_cols_].astype(float)
        A[miss] = np.take(self.median_, np.where(miss)[1])
        if self.log:
            A = np.log1p(A)
        return np.hstack([A, ind]) if len(self.missing_cols_) else A

    def get_feature_names_out(self, input_features=None):
        names = list(self.feature_names_in_)
        return np.array(names + [f"{names[j]}_missing" for j in self.missing_cols_], dtype=object)


def split_kinds(cols: list[str]) -> dict:
    nominal = [c for c in cols if c in NOMINAL]
    ordinal = [c for c in cols if c == "highest_education"]
    boolean = [c for c in cols if c in BOOLEAN]
    no_ind = [c for c in cols if c in NO_INDICATOR]
    not_counts = [c for c in cols if c in NOT_COUNTS and c not in NO_INDICATOR]
    counts = [c for c in cols if c not in set(nominal + ordinal + boolean + no_ind + not_counts)]
    return {"nominal": nominal, "ordinal": ordinal, "boolean": boolean, "no_indicator": no_ind,
            "not_counts": not_counts, "counts": counts}


def logistic_preprocessor(cols: list[str]) -> Pipeline:
    k = split_kinds(cols)
    parts = [(f"dev_{c}", DeviationCoder(), [c]) for c in k["nominal"]]
    parts += [("ordinal", OrdinalMap(EDUCATION_ORDER), k["ordinal"])] if k["ordinal"] else []
    parts += [("boolean", FoldNumeric(log=False, indicator=False), k["boolean"])] if k["boolean"] else []
    parts += [("reglead", FoldNumeric(log=False, indicator=False), k["no_indicator"])] if k["no_indicator"] else []
    parts += [("noncount", FoldNumeric(log=False, indicator=True), k["not_counts"])] if k["not_counts"] else []
    parts += [("count", FoldNumeric(log=True, indicator=True), k["counts"])] if k["counts"] else []
    ct = ColumnTransformer(parts, remainder="drop", verbose_feature_names_out=False)
    return Pipeline([("encode", ct), ("scale", StandardScaler())])


def logistic_pipeline(cols: list[str], C: float) -> Pipeline:
    return Pipeline([
        ("prep", logistic_preprocessor(cols)),
        ("model", LogisticRegression(C=C, l1_ratio=0.0, solver="lbfgs", max_iter=10000, tol=1e-8)),
    ])


def tree_pipeline(cols: list[str], params: dict) -> Pipeline:
    """Trees read the predictors untransformed: nominal levels as native categories (unseen -> missing),
    education as its ordinal code, booleans as 0/1, numbers as they are (nulls handled natively)."""
    k = split_kinds(cols)
    nominal = k["nominal"]
    rest = [c for c in cols if c not in nominal and c != "highest_education"]
    parts = [("cat", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan,
                                    encoded_missing_value=np.nan), nominal)]
    if k["ordinal"]:
        parts.append(("ordinal", OrdinalMap(EDUCATION_ORDER), k["ordinal"]))
    parts.append(("raw", "passthrough", rest))
    ct = ColumnTransformer(parts, remainder="drop", verbose_feature_names_out=False)
    model = HistGradientBoostingClassifier(
        max_depth=params["max_depth"], learning_rate=params["learning_rate"], max_iter=params["max_iter"],
        categorical_features=list(range(len(nominal))), early_stopping=False, random_state=SEED)
    return Pipeline([("prep", ct), ("model", model)])


def make_pipeline(config: str, cols: list[str], params) -> Pipeline:
    family = CONFIGS[config][1]
    if family == "logistic":
        return logistic_pipeline(cols, params["C"])
    if family == "trees":
        return tree_pipeline(cols, params)
    raise ValueError(config)


def grid_for(config: str) -> list[dict]:
    family = CONFIGS[config][1]
    return [{"C": c} for c in C_GRID] if family == "logistic" else [dict(p) for p in TREE_GRID]


def fit_pipeline(config: str, cols: list[str], params: dict, train: pd.DataFrame) -> Pipeline:
    assert_2013(train)
    X = train[cols].copy()
    for c in cols:   # booleans to 0/1 floats for every model
        if X[c].dtype == bool:
            X[c] = X[c].astype(float)
    pipe = make_pipeline(config, cols, params)
    pipe.fit(X, train["y"].to_numpy())
    return pipe


def predict(pipe: Pipeline, cols: list[str], df: pd.DataFrame) -> np.ndarray:
    assert_2013(df)
    X = df[cols].copy()
    for c in cols:
        if X[c].dtype == bool:
            X[c] = X[c].astype(float)
    return pipe.predict_proba(X)[:, 1]


# ---------------------------------------------------------------- lists and metrics (Appendix II)
def list_length(n: int, per20: int) -> int:
    """capacity_by_run.parquet: per20 x ceil(n / 20), at most n."""
    return int(min(n, per20 * math.ceil(n / 20)))


def ranked_order(score: np.ndarray, tiebreak_ids: np.ndarray, secondary: np.ndarray | None = None) -> np.ndarray:
    """Indices from highest to lowest score; ties by lower `secondary` (if given), then by ascending id."""
    keys = [np.asarray(tiebreak_ids)]
    if secondary is not None:
        keys.append(np.asarray(secondary, dtype=float))
    keys.append(-np.asarray(score, dtype=float))
    return np.lexsort(keys)


def on_list(order: np.ndarray, k: int) -> np.ndarray:
    mask = np.zeros(len(order), dtype=bool)
    mask[order[:k]] = True
    return mask


def run_metrics(y: np.ndarray, listed: np.ndarray, k: int, auc: float | None) -> dict:
    """Appendix II, Table A.4, for one run. `listed` may be a mean over draws (B1)."""
    y = np.asarray(y).astype(int)
    n, n_nc = len(y), int(y.sum())
    tp = float(np.sum(np.asarray(listed, dtype=float) * y))
    max_att = min(k, n_nc)
    b = n_nc / n if n else float("nan")
    precision = tp / k if k else None
    return {
        "n_enrolments": n, "n_noncompleters": n_nc, "list_length": k,
        "noncompleters_on_list": tp, "max_attainable": max_att,
        "normalised_recall": tp / max_att if max_att else None,
        "precision": precision,
        "lift": precision / b if (precision is not None and b) else None,
        "roc_auc_within_run": auc,
    }


def within_run_auc(y: np.ndarray, score: np.ndarray) -> float | None:
    y = np.asarray(y).astype(int)
    if y.min() == y.max():
        return None
    return float(roc_auc_score(y, score))


def pooled_normalised_recall(tp, max_att) -> float:
    return float(np.sum(tp) / np.sum(max_att))


def rule_signs(df: pd.DataFrame) -> np.ndarray:
    return sum(df[c].astype(int).to_numpy() for c in RULE_SIGNS)


def rule_score(df: pd.DataFrame) -> np.ndarray:
    """A score whose order equals the B2 ranking (signs desc, then lower activity ratio), ties kept,
    used only for the within-run ROC-AUC of B2."""
    signs = rule_signs(df)
    ar = df["activity_ratio_run"].to_numpy(dtype=float)
    pairs = sorted(set(zip(signs.tolist(), (-ar).tolist())))
    rank = {p: i for i, p in enumerate(pairs)}
    return np.array([rank[p] for p in zip(signs.tolist(), (-ar).tolist())], dtype=float)


def b2_order(df: pd.DataFrame) -> np.ndarray:
    return ranked_order(rule_signs(df), df["id_student"].to_numpy(),
                        secondary=df["activity_ratio_run"].to_numpy(dtype=float))


def model_order(df: pd.DataFrame, score: np.ndarray) -> np.ndarray:
    return ranked_order(score, df["id_student"].to_numpy())


# ---------------------------------------------------------------- folds and tuning
def loro_folds(df: pd.DataFrame):
    """Leave-one-run-out: yield (run, train, valid); training rows of students who also appear in the
    validation run are removed (Appendix III, step 2)."""
    for run in sorted(df[RUN].unique()):
        valid = df[df[RUN] == run]
        overlap = set(valid["id_student"])
        train = df[(df[RUN] != run) & (~df["id_student"].isin(overlap))]
        assert_2013(train)
        assert_2013(valid)
        yield run, train, valid


def score_lists(df: pd.DataFrame, score: np.ndarray, per20: int) -> tuple[float, int, int]:
    """(tp, max_attainable, k) of one validation run's list at per20."""
    k = list_length(len(df), per20)
    listed = on_list(model_order(df, score), k)
    y = df["y"].to_numpy()
    return float((listed & (y == 1)).sum()), min(k, int(y.sum())), k


def tune(config: str, cols: list[str], train: pd.DataFrame) -> tuple[dict, list[dict]]:
    """Inner leave-one-run-out over the training runs; criterion: pooled normalised recall at
    k = 5 per 20 over the inner folds; ties go to the simplest setting (first in grid order)."""
    assert_2013(train)
    grid = grid_for(config)
    inner = list(loro_folds(train))
    table = []
    for gi, params in enumerate(grid):
        tps, maxs = [], []
        for _, itr, iva in inner:
            pipe = fit_pipeline(config, cols, params, itr)
            tp, mx, _ = score_lists(iva, predict(pipe, cols, iva), MAIN_PER20)
            tps.append(tp)
            maxs.append(mx)
        table.append({"grid_index": gi, "params": params, "inner_pooled_nr": pooled_normalised_recall(tps, maxs)})
    best = max(table, key=lambda r: (round(r["inner_pooled_nr"], 12), -r["grid_index"]))
    return best["params"], table


def git_commit(cwd: Path = PKG) -> str:
    import subprocess
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=cwd, capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", str(PKG)], cwd=cwd, capture_output=True,
                               text=True).stdout.strip()
        return sha + ("+uncommitted-package-changes" if dirty else "")
    except Exception:
        return "unknown"


DEVIATIONS = [
    "Tuning grids: Appendix III step 3 names the tuned settings but no values; grids are "
    "C (inverse L2 penalty) in {1e-5,1e-4,0.001,0.01,0.1,1,10,100} and trees depth {2,3} x trees {100,300} x "
    "learning rate {0.05,0.1} (depth 2-3 as Appendix I, Table A.2 calls interpretable).",
    "Tuning criterion: not stated; the inner loop maximises pooled normalised recall at k = 5 per 20 at the "
    "fold's cut-off (the S1 metric), ties to the simplest setting (smaller C; shallower, fewer, slower trees).",
    "Penalty type: 'penalised logistic regression' without a type; L2 (ridge), lbfgs.",
    "B3 uses the same penalised logistic pipeline and nested tuning as M1, restricted to its 6 predictors.",
    "Model-score ties and remaining B2 ties (same signs and activity ratio) are broken by ascending "
    "id_student (randomised by the provider); not specified in the contract.",
    "B1: mean over 100 seeded random lists per run (number of draws not specified); noncompleters_on_list "
    "and roc_auc_within_run are those means.",
    "Trees: module and start month enter as native categories of HistGradientBoostingClassifier "
    "(levels learnt in the training fold, unseen level -> missing); education as its ordinal code; "
    "early stopping off so the number of trees is the tuned value.",
    "List length for inner (tuning) folds, whose runs lose the rows of students in the outer validation "
    "run, uses the capacity_by_run formula per20 x ceil(n/20) on the rows present; outer folds use "
    "capacity_by_run itself (equal by construction, asserted).",
    "freeze.csv has one row per cut-off (one frozen model per cut-off, Section 3.3); the key '-' of the "
    "contract is kept and the cut-off is written in the spec column.",
    "Two challengers may both meet the margin: the one with the higher pooled normalised recall is chosen, "
    "ties to the simpler (order M1 < M2 < M3 < M4).",
    "C grid extended to 1e-5–100 after phase-1 development showed the day-27 optimum on the lower boundary "
    "(C=0.001); decided before any 2014 access (results of the first grid kept in results/grid_v1/).",
    "version_manifest.json carries no hash for predictor_sets.json and data_dictionary.md; their SHA-256 "
    "values are recorded in the experiment log instead.",
]


# ---------------------------------------------------------------- one outer fold (used by 02 and 03)
def evaluate_outer_fold(config: str, cutoff: int, run: str, m3: Path = M3_DEFAULT) -> dict:
    """Nested evaluation of one fitted configuration on one outer validation run."""
    from threadpoolctl import threadpool_limits
    with threadpool_limits(limits=1):
        df = load_view(cutoff, m3)
        sets = predictor_sets(m3)
        cols = columns_for(config, cutoff, sets)
        (_, train, valid), = [f for f in loro_folds(df) if f[0] == run]
        params, table = tune(config, cols, train)
        pipe = fit_pipeline(config, cols, params, train)
        score = predict(pipe, cols, valid)
    rows = []
    y = valid["y"].to_numpy()
    auc = within_run_auc(y, score)
    order = model_order(valid, score)
    for per20 in PER20:
        k = list_length(len(valid), per20)
        rows.append({"config": config, "cutoff": cutoff, "k": per20, "validation_run": run,
                     **run_metrics(y, on_list(order, k), k, auc)})
    tuning = [{"config": config, "cutoff": cutoff, "validation_run": run, "grid_index": t["grid_index"],
               "params": json.dumps(t["params"], sort_keys=True), "inner_pooled_nr": t["inner_pooled_nr"],
               "chosen": t["params"] == params} for t in table]
    return {"rows": rows, "tuning": tuning}


def run_folds(configs, n_jobs: int, m3: Path = M3_DEFAULT) -> tuple[pd.DataFrame, pd.DataFrame]:
    from joblib import Parallel, delayed
    runs = {c: sorted(load_view(c, m3)[RUN].unique()) for c in CUTOFFS}
    jobs = [(cfg, c, r) for cfg in configs for c in CUTOFFS for r in runs[c]]
    out = Parallel(n_jobs=n_jobs, backend="loky", verbose=5)(
        delayed(evaluate_outer_fold)(cfg, c, r, m3) for cfg, c, r in jobs)
    rows = pd.DataFrame([r for o in out for r in o["rows"]])
    tuning = pd.DataFrame([t for o in out for t in o["tuning"]])
    return rows, tuning


DEV_COLUMNS = ["config", "cutoff", "k", "validation_run", "n_enrolments", "n_noncompleters", "list_length",
               "noncompleters_on_list", "max_attainable", "normalised_recall", "precision", "lift",
               "roc_auc_within_run"]


def write_dev(df: pd.DataFrame, path: Path) -> None:
    df = df[DEV_COLUMNS].sort_values(["config", "cutoff", "k", "validation_run"]).reset_index(drop=True)
    df.to_csv(path, index=False, float_format="%.6f")


# ---------------------------------------------------------------- phase 2: guarded test access (2014)
TEST_YEAR = 2014
FREEZE_CSV = RESULTS / "freeze.csv"
B3_FIT_CSV = RESULTS / "b3_fit.csv"
BOOT_B = 2000            # bootstrap resamples (Appendix III fixes none)
BOOT_SEED = SEED         # bootstrap seed stream: default_rng([BOOT_SEED, <purpose code>])


def read_freeze() -> pd.DataFrame:
    return pd.read_csv(FREEZE_CSV, keep_default_na=False, dtype=str)


def test_access_time() -> str:
    """The recorded first test access (UTC), or '' if the 2014 outcomes were never opened."""
    if not FREEZE_CSV.exists():
        return ""
    vals = set(read_freeze()["first_test_access_utc"])
    if len(vals) != 1:
        raise SystemExit(f"STOP: inconsistent first_test_access_utc values {vals}")
    return vals.pop()


def assert_2014(df) -> None:
    years = set(pd.unique(df["year"]).tolist()) if not isinstance(df, pl.DataFrame) else set(df["year"].unique().to_list())
    if years - {TEST_YEAR}:
        raise AssertionError(f"test loader: found years {sorted(years)}")


def load_test_view(cutoff: int, m3: Path = M3_DEFAULT) -> pd.DataFrame:
    """2014 rows; refused unless the test access is already recorded in freeze.csv."""
    if not test_access_time():
        raise PermissionError("2014 rows refused: no first_test_access_utc recorded in results/freeze.csv")
    lf = pl.scan_parquet(m3 / f"data/processed/features_d{cutoff}.parquet")
    df = lf.filter(pl.col("year") == TEST_YEAR).collect()
    assert_2014(df)
    pdf = _to_pandas(df)
    pdf[RUN] = pdf["code_module"] + "_" + pdf["code_presentation"]
    pdf["y"] = pdf["non_completion"].astype(int)
    return pdf


def predict_any(pipe: Pipeline, cols: list[str], df: pd.DataFrame) -> np.ndarray:
    """Scoring without the 2013 guard (test rows); the pipeline itself is never refitted here."""
    X = df[cols].copy()
    for c in cols:
        if X[c].dtype == bool:
            X[c] = X[c].astype(float)
    return pipe.predict_proba(X)[:, 1]


def load_verified(path_rel: str, sha: str):
    import joblib
    p = PKG / path_rel
    got = sha256(p)
    if got != sha:
        raise SystemExit(f"STOP: hash mismatch for {path_rel}: {got} != {sha}")
    return joblib.load(p)


def frozen_m1(cutoff: int):
    fr = read_freeze()
    row = fr[fr["spec"].str.contains(f"cutoff={cutoff} ")].iloc[0]
    spec = json.loads((PKG / row["parameter_file"].replace(".joblib", ".spec.json")).read_text())
    return load_verified(row["parameter_file"], row["model_sha256"]), spec["columns"], row["chosen_config"]


def fitted_b3(cutoff: int):
    b3 = pd.read_csv(B3_FIT_CSV, keep_default_na=False, dtype=str)
    row = b3[b3["cutoff"] == str(cutoff)].iloc[0]
    return load_verified(row["parameter_file"], row["model_sha256"]), json.loads(row["columns"])


def test_scores(cutoff: int, m3: Path = M3_DEFAULT) -> pd.DataFrame:
    """2014 view with the frozen M1 score, the B3 score and the rule signs (guarded by the access record)."""
    df = load_test_view(cutoff, m3)
    m1, m1_cols, cfg = frozen_m1(cutoff)
    b3, b3_cols = fitted_b3(cutoff)
    df["score_M1"] = predict_any(m1, m1_cols, df)
    df["score_B3"] = predict_any(b3, b3_cols, df)
    df["rule_signs"] = rule_signs(df)
    return df


TEST_DEVIATIONS = [
    f"Bootstrap: {BOOT_B} resamples, seeded default_rng([{BOOT_SEED}, purpose]); percentile intervals "
    "(Appendix III fixes neither the number nor the interval type). Sign-flip test: exact over all 2^m sign "
    "assignments, statistic = mean of per-run normalised-recall differences, one-sided, p counts ties.",
    "B3 on the test runs: refitted on all 9 runs of 2013 with the M1 tuning procedure (leave-one-run-out, extended C "
    "grid) before the test access; saved as models/fitted_B3_d<cutoff>.joblib with its hash in results/b3_fit.csv.",
    "Net benefit: thresholds 0.05-0.95 by 0.05, pooled over the test runs; the rule as a policy contacts every "
    "flagged student (early_sign_rule); B1 has no probability and is omitted.",
    "Calibration: statsmodels GLM Binomial on the pooled test rows; CITL with logit(p) as offset, slope from "
    "logit(y) ~ 1 + logit(p); S3 is judged on M1 at day 27 only, other rows are descriptive.",
    "Fairness: recall pooled within run as sum of listed non-completers over sum of non-completers per group; "
    "Holm applied to one-sided bootstrap p-values (share of resamples with difference >= 0), each group's upper "
    "bound taken at its Holm level; gender and age rows are descriptive.",
    "Sensitivity 'module CCC apart' is run as two variants: CCC runs only and the runs without CCC.",
    "AQ2 replication: the copied Milestone 5 model gives a sign x module term only to modules where the sign occurs "
    "(no 2014 CCC enrolment has a late TMA, which made the copied model singular); a module without the sign gets the "
    "average-module effect. The 2013 estimates still equal the Milestone 5 results exactly (31 of 31).",
    "Labels-available variant: M1 specification tuned (leave-one-run-out) and fitted on the 3 runs of 2013B only, "
    "scored on the 6 runs of 2014B, compared with the rule on the same runs.",
]
