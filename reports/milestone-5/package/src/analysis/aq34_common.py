"""Shared definitions of AQ3 (predictive) and AQ4 (ranking): loaders with a year guard, the candidate models of the
Milestone 4 plan, list rules and list metrics. Holds no analysis; imported by aq3_develop.py, aq3_test.py,
aq4_lists.py and aq34_checks.py.

Plan items (Milestone 4 report): Section 3.3 (candidates), Section 4.1 (capacity, Table 4.3 and 4.4 cards),
Section 4.3 (S1, S3), Appendix III (validation protocol). Implementation choices that the plan leaves open are those
of the team's Level 2 prototype (results/README.md, "AQ3 and AQ4"); the tuning criterion is Change Log C18.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

HERE = Path(__file__).resolve().parent              # src/analysis
ROOT = HERE.parents[1]                               # the package folder
PROC, META = ROOT / "data" / "processed", ROOT / "data" / "metadata"
WORK = ROOT / "data" / "interim" / "aq3"             # fitted models, freeze record, per-enrolment scores (not shipped)
R2013, R2014 = ROOT / "results" / "2013", ROOT / "results" / "2014"   # AQ3/AQ4 files carry the prefix aq3_ or aq4_
RALL, RCMP = ROOT / "results" / "all_runs", ROOT / "results" / "compare"
SCOPE_DIR = {"2013": R2013, "2014": R2014, "all": RALL}
SEED = 20261112                                      # tie-breaker, bootstrap and boosted trees
KEY = ["code_module", "code_presentation", "id_student"]
YEARS = {"train": 2013, "test": 2014}


# ---------------------------------------------------------------------------------------------------------------
# Loading with a year guard
# ---------------------------------------------------------------------------------------------------------------
def features(cutoff: int, year: int | None = None) -> pd.DataFrame:
    """Enrolments registered at the cut-off (day 13 or 27), optionally one year only (filter pushed to the reader,
    then asserted), sorted by key, with a fixed tie-breaker drawn over the full view in key order."""
    full = pl.read_parquet(PROC / f"features_d{cutoff}.parquet").sort(KEY)
    u = np.random.default_rng(SEED).random(full.height)           # drawn on all rows, so it does not depend on the scope
    full = full.with_columns(pl.Series("tiebreak_u", u))
    if year is not None:
        full = full.filter(pl.col("year") == year)
        assert (full["year"] == year).all() and full.height > 0, f"features_d{cutoff}: rows outside {year}"
    f = pd.DataFrame(full.to_dict(as_series=False))
    f["run"] = f["code_module"] + "-" + f["code_presentation"]
    f["y"] = f["non_completion"].astype(int)
    return f


def enrolment() -> pd.DataFrame:
    e = pl.read_parquet(PROC / "enrolment.parquet")
    return pd.DataFrame(e.to_dict(as_series=False))


def predictor_sets() -> dict:
    return json.loads((META / "predictor_sets.json").read_text())


def write(frame: pd.DataFrame, folder: Path, name: str) -> Path:
    """Write a result table with every float rounded to 6 decimals, so reruns are byte-identical."""
    folder.mkdir(parents=True, exist_ok=True)
    out = frame.copy()
    for c in out.columns:
        if out[c].dtype.kind == "f":
            out[c] = out[c].round(6)
    out.to_csv(folder / name, index=False, lineterminator="\n")
    print(f"wrote {folder.name}/{name} ({len(out)} rows)")
    return folder / name


# ---------------------------------------------------------------------------------------------------------------
# Capacity, lists and list metrics (Section 4.1; normalised recall, Change Log C13)
# ---------------------------------------------------------------------------------------------------------------
def list_size(n: int, per20: int) -> int:
    """k = 3 or 5 contacts per assumed tutor group of 20, capped at the run's size."""
    return min(n, per20 * math.ceil(n / 20))


def rank_in_run(frame: pd.DataFrame, score: str) -> pd.Series:
    """Rank 1 = highest score within the run; exact ties broken by the fixed tie-breaker."""
    order = frame.sort_values(["run", score, "tiebreak_u"], ascending=[True, False, True])
    return (order.groupby("run").cumcount() + 1).reindex(frame.index)


def rule_score(frame: pd.DataFrame) -> np.ndarray:
    """Rule-ranked list (baseline B2, C10): number of signs (task missed, TMA late, inactive 7 days), then lower
    activity relative to the run median; students with no sign follow, also by lower activity."""
    n = frame["rule_missed"].astype(int) + frame["rule_tma_late"].astype(int) + frame["inactive_last7"].astype(int)
    return n.to_numpy() + 1.0 / (1.0 + frame["activity_ratio_run"].to_numpy())


def list_metrics(frame: pd.DataFrame, score: str, per20: int = 5) -> pd.DataFrame:
    ranks = rank_in_run(frame, score)
    rows = []
    for run, g in frame.groupby("run", sort=True):
        n, pos = len(g), int(g["y"].sum())
        k = list_size(n, per20)
        tp = int(g["y"][ranks[g.index] <= k].sum())
        best = min(k, pos)
        rows.append({"run": run, "n": n, "k": k, "positives": pos, "tp": tp, "attainable": best,
                     "recall": tp / pos if pos else np.nan, "precision": tp / k, "base_rate": pos / n,
                     "lift": (tp / k) / (pos / n) if pos else np.nan, "norm_recall": tp / best if best else np.nan})
    return pd.DataFrame(rows)


def pooled(m: pd.DataFrame) -> dict:
    tp, best, pos, k, n = m["tp"].sum(), m["attainable"].sum(), m["positives"].sum(), m["k"].sum(), m["n"].sum()
    return {"n": int(n), "k": int(k), "positives": int(pos), "tp": tp, "attainable": int(best),
            "norm_recall": tp / best, "recall": tp / pos, "precision": tp / k, "lift": (tp / k) / (pos / n)}


# ---------------------------------------------------------------------------------------------------------------
# Candidate models (Section 3.3): B3 background-only baseline, M1 primary approach, M2-M4 challengers
# ---------------------------------------------------------------------------------------------------------------
EDU = {"No Formal quals": 0, "Lower Than A Level": 1, "A Level or Equivalent": 2,
       "HE Qualification": 3, "Post Graduate Qualification": 4}
NOT_LOGGED = {"registration_lead", "activity_ratio_run", "trend_last_week", "days_since_last_click"}
BACKGROUND = ["code_module", "start_month", "num_of_prev_attempts", "studied_credits", "highest_education",
              "registration_lead"]
CONFIGS = {"B3": ("logistic", "background"), "M1": ("logistic", "primary"), "M2": ("logistic", "extended"),
           "M3": ("trees", "primary"), "M4": ("trees", "extended")}
LR_GRID = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 10]                 # ascending C = descending penalty
TREE_GRID = [dict(max_depth=d, max_iter=t, learning_rate=lr)            # from the smallest model
             for d, t, lr in itertools.product([2, 3, 4], [100, 200, 400], [0.05, 0.1])]


def predictor_list(sets: dict, name: str, cutoff: int) -> list[str]:
    primary = [c for c in sets["primary"] if c != "cma_score_mean_c"]   # known for < 10% of training rows
    if name == "background":
        return BACKGROUND
    if name == "primary":
        return primary
    return primary + sets["extended"] + sets["weekly_clicks"][f"d{cutoff}"]


def _numeric(v: pd.Series) -> pd.Series:
    return pd.to_numeric(v.astype("float64") if v.dtype == bool else v, errors="coerce").astype(float)


class LinearPrep:
    """Deviation coding of module and start month over the training levels (unseen level = all zeros), ordinal
    education, log(1 + x) for counts, training-median fill with a missing indicator, standardisation. Every parameter
    is learnt in fit() from training rows only (Appendix III, step 3)."""

    def __init__(self, columns: list[str], indicator_for_lead: bool):
        self.columns, self.indicator_for_lead = columns, indicator_for_lead

    def _base(self, f: pd.DataFrame) -> pd.DataFrame:
        out = {}
        for c in self.columns:
            if c in ("code_module", "start_month"):
                continue
            v = f[c].map(EDU).astype(float) if c == "highest_education" else _numeric(f[c])
            if c not in NOT_LOGGED and c != "highest_education" and c in self.logged:
                v = np.log1p(v.clip(lower=0))
            out[c] = v
        return pd.DataFrame(out, index=f.index)

    def fit(self, f: pd.DataFrame) -> "LinearPrep":
        self.levels = {c: sorted(f[c].unique()) for c in ("code_module", "start_month") if c in self.columns}
        self.logged = {c for c in self.columns if c not in ("code_module", "start_month", "highest_education")
                       and not set(np.unique(_numeric(f[c]).dropna())) <= {0.0, 1.0}}
        base = self._base(f)
        self.median = base.median()
        self.missing_cols = [c for c in base.columns if base[c].isna().any()
                             and (self.indicator_for_lead or c != "registration_lead")]
        x = self._assemble(f, base)
        self.mean, self.sd = x.mean(), x.std(ddof=0).replace(0, 1.0)
        return self

    def _assemble(self, f: pd.DataFrame, base: pd.DataFrame) -> pd.DataFrame:
        x = {}
        for c, levels in self.levels.items():
            ref = levels[-1]
            for lev in levels[:-1]:
                x[f"{c}={lev}"] = np.where(f[c] == lev, 1.0, np.where(f[c] == ref, -1.0, 0.0))
        for c in base.columns:
            if c in self.missing_cols:
                x[f"{c}_missing"] = base[c].isna().astype(float)
            x[c] = base[c].fillna(self.median[c])
        return pd.DataFrame(x, index=f.index)

    def transform(self, f: pd.DataFrame) -> np.ndarray:
        x = self._assemble(f, self._base(f))[self.mean.index]
        return ((x - self.mean) / self.sd).to_numpy()

    def names(self) -> list[str]:
        return list(self.mean.index)


class Model:
    """One configuration with fixed hyperparameters: fit on training rows, score any rows."""

    def __init__(self, config: str, cutoff: int, sets: dict, params: dict):
        self.config, self.cutoff, self.params = config, cutoff, params
        self.kind, pset = CONFIGS[config]
        self.columns = predictor_list(sets, pset, cutoff)
        self.extended = pset == "extended"

    def _trees_x(self, f: pd.DataFrame) -> np.ndarray:
        cols = []
        for c in self.columns:
            if c == "code_module":
                cols.append(f[c].map({m: i for i, m in enumerate(self.modules)}).astype(float).to_numpy())
            elif c == "start_month":
                cols.append((f[c] == "J").astype(float).to_numpy())
            elif c == "highest_education":
                cols.append(f[c].map(EDU).astype(float).to_numpy())
            else:
                cols.append(_numeric(f[c]).to_numpy())
        return np.column_stack(cols)

    def fit(self, f: pd.DataFrame, y: np.ndarray) -> "Model":
        if self.kind == "logistic":
            self.prep = LinearPrep(self.columns, indicator_for_lead=self.extended).fit(f)
            self.est = LogisticRegression(C=self.params["C"], max_iter=5000).fit(self.prep.transform(f), y)
        else:
            self.modules = sorted(f["code_module"].unique())
            cat = np.array([c == "code_module" for c in self.columns])
            self.est = HistGradientBoostingClassifier(categorical_features=cat, early_stopping=False,
                                                      random_state=SEED, **self.params).fit(self._trees_x(f), y)
        return self

    def predict(self, f: pd.DataFrame) -> np.ndarray:
        x = self.prep.transform(f) if self.kind == "logistic" else self._trees_x(f)
        return self.est.predict_proba(x)[:, 1]

    def contributions(self, f: pd.DataFrame) -> pd.DataFrame:
        """Logistic models only: coefficient × standardised value per predictor (the reasons behind a score)."""
        x = self.prep.transform(f)
        return pd.DataFrame(x * self.est.coef_[0], columns=self.prep.names(), index=f.index)


def grid(config: str) -> list[dict]:
    return [{"C": c} for c in LR_GRID] if CONFIGS[config][0] == "logistic" else TREE_GRID


def calibration(y: np.ndarray, p: np.ndarray) -> dict:
    """Calibration-in-the-large (slope fixed at 1) and calibration slope, by logistic fits (Section 4.3, S3)."""
    import statsmodels.api as sm
    p = np.clip(p, 1e-6, 1 - 1e-6)
    lp = np.log(p / (1 - p))
    citl = sm.GLM(y, np.ones((len(y), 1)), family=sm.families.Binomial(), offset=lp).fit().params[0]
    slope = sm.GLM(y, sm.add_constant(lp), family=sm.families.Binomial()).fit().params[1]
    return {"citl": float(citl), "slope": float(slope), "mean_pred": float(p.mean()), "observed": float(y.mean()),
            "brier": float(np.mean((p - y) ** 2))}
