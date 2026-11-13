"""Model definitions of AQ3 (frozen with the models before the 2014 test; do not edit after the freeze).

Configurations of the Level 1 Candidate Solution Matrix:
    B3  penalised logistic regression, background predictors only (baseline)
    M1  penalised logistic regression, primary predictors (primary approach)
    M2  penalised logistic regression, primary + extended predictors + weekly clicks (challenger)
    M3  gradient-boosted trees, primary predictors (challenger)
    M4  gradient-boosted trees, primary + extended predictors + weekly clicks (challenger)
Preprocessing, grids and tie rules follow the design (implementation choices P06–P10).
"""

from __future__ import annotations

import itertools
import json

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

SEED = 20261112
EDU = {"No Formal quals": 0, "Lower Than A Level": 1, "A Level or Equivalent": 2,
       "HE Qualification": 3, "Post Graduate Qualification": 4}
NOT_LOGGED = {"registration_lead", "activity_ratio_run", "trend_last_week", "days_since_last_click"}
BACKGROUND = ["code_module", "start_month", "num_of_prev_attempts", "studied_credits", "highest_education",
              "registration_lead"]
CONFIGS = {"B3": ("logistic", "background"), "M1": ("logistic", "primary"), "M2": ("logistic", "extended"),
           "M3": ("trees", "primary"), "M4": ("trees", "extended")}
LR_GRID = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 10]                # ascending C = descending penalty
TREE_GRID = [dict(max_depth=d, max_iter=t, learning_rate=lr)          # ordered from the smallest model
             for d, t, lr in itertools.product([2, 3, 4], [100, 200, 400], [0.05, 0.1])]


def predictor_list(sets: dict, name: str, cutoff: int) -> list[str]:
    primary = [c for c in sets["primary"] if c != "cma_score_mean_c"]     # < 10% filled in training (design)
    if name == "background":
        return BACKGROUND
    if name == "primary":
        return primary
    return primary + sets["extended"] + sets["weekly_clicks"][f"d{cutoff}"]


def _numeric(v: pd.Series) -> pd.Series:
    return pd.to_numeric(v.astype("float64") if v.dtype == bool else v, errors="coerce").astype(float)


class LinearPrep:
    """Deviation coding of module and start month over the training levels (unseen level = all zeros), ordinal
    education, log(1 + x) for counts, training-median fill with a missing indicator, standardisation with training
    mean and SD. Every parameter is learnt in fit() from training rows only."""

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
        # counts are logged; 0/1 columns are not (decided from the training rows)
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


def describe(params: dict) -> str:
    return json.dumps(params, sort_keys=True)
