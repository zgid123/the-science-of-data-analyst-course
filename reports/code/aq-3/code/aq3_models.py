"""AQ3 models: predictor sets, fold-wise preprocessing, tuning and fitting (Level 1 Sections 3.3, 4.2; PROTOCOL.md P06–P12).

Configurations
    B3  background-only penalised logistic regression (baseline)
    M1  penalised logistic regression, primary predictor set (primary approach)
    M2  penalised logistic regression, extended predictor set
    M3  gradient-boosted trees, primary predictor set
    M4  gradient-boosted trees, extended predictor set
The rule-ranked list (B2) and the random list (B1) need no fitting; see `rule_score` and lib.run_metrics.

Every transform is fitted on the training rows it is given and on nothing else.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import polars as pl
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

HERE = Path(__file__).resolve().parent
AQ = HERE.parent
sys.path.insert(0, str(AQ.parent / "common"))
import lib  # noqa: E402

EXTRACT = AQ / "extracted-datasets"
RESULTS = AQ / "results"
FIGURES = AQ / "figures"
MODELS = RESULTS / "models"

_sets = json.loads((lib.PREPARED / "metadata" / "predictor_sets.json").read_text())
PRIMARY = [c for c in _sets["primary"] if c not in _sets["not_used_in_milestone4"]]
EXTENDED_ONLY = _sets["extended"]
WEEKLY = {13: _sets["weekly_clicks"]["d13"], 27: _sets["weekly_clicks"]["d27"]}
BACKGROUND = ["code_module", "start_month", "num_of_prev_attempts", "studied_credits", "highest_education", "registration_lead"]
NOMINAL = ["code_module", "start_month"]
BOOLEAN = ["inactive_last7", "registration_missing"]
NOT_LOGGED = ["registration_lead", "activity_ratio_run", "trend_last_week", "days_since_last_click"]
NO_INDICATOR = ["registration_lead"]

CONFIGS = {
    "B3": {"kind": "logit", "set": "background", "label": "Background-only logistic model (baseline)"},
    "M1": {"kind": "logit", "set": "primary", "label": "Penalised logistic regression, primary set (primary approach)"},
    "M2": {"kind": "logit", "set": "extended", "label": "Penalised logistic regression, extended set"},
    "M3": {"kind": "gbt", "set": "primary", "label": "Gradient-boosted trees, primary set"},
    "M4": {"kind": "gbt", "set": "extended", "label": "Gradient-boosted trees, extended set"},
}
CHALLENGERS = ["M2", "M3", "M4"]          # in order of simplicity (PROTOCOL.md P11)
C_GRID = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 10.0]
GBT_DEPTH, GBT_LR, GBT_TREES = [2, 3, 4], [0.05, 0.1], [100, 200, 400]


def predictors(config: str, cutoff: int) -> list[str]:
    s = CONFIGS[config]["set"]
    if s == "background":
        return list(BACKGROUND)
    if s == "primary":
        return list(PRIMARY)
    return PRIMARY + EXTENDED_ONLY + WEEKLY[cutoff]


def model_columns(cutoff: int) -> list[str]:
    return PRIMARY + EXTENDED_ONLY + WEEKLY[cutoff]


def rule_score(df: pl.DataFrame) -> np.ndarray:
    """Early-sign rule as a ranking: number of signs, ties by lower activity relative to the run (PROTOCOL.md P04)."""
    signs = (df["rule_missed"].cast(pl.Int64) + df["rule_tma_late"].cast(pl.Int64) + df["inactive_last7"].cast(pl.Int64)).to_numpy()
    ratio = df["activity_ratio_run"].to_numpy()
    return signs + 0.999 / (1.0 + ratio)


def _numeric(df: pl.DataFrame, col: str) -> np.ndarray:
    if col == "highest_education":
        return df[col].replace_strict({v: i for i, v in enumerate(lib.EDUCATION_ORDER)}, return_dtype=pl.Float64).to_numpy()
    if col in BOOLEAN:
        return df[col].cast(pl.Float64).to_numpy()
    x = df[col].cast(pl.Float64).to_numpy().astype(float)
    return x


class LogitPrep:
    """Preprocessing of the logistic models, fitted on training rows only."""

    def __init__(self, cols: list[str]):
        self.cols = cols

    def _raw(self, df: pl.DataFrame) -> tuple[np.ndarray, list[str]]:
        blocks, names = [], []
        for c in self.cols:
            if c in NOMINAL:
                levels = self.levels[c]
                v = df[c].to_numpy()
                for lev in levels[:-1]:                      # deviation coding: last level = -1 on every column
                    col = (v == lev).astype(float) - (v == levels[-1]).astype(float)
                    blocks.append(col); names.append(f"{c}[{lev}]")
                continue                                    # a level unseen in training keeps 0 on every column
            x = _numeric(df, c)
            if c not in NOT_LOGGED and c not in BOOLEAN and c != "highest_education":
                x = np.log1p(x)
            if c in self.medians:
                miss = np.isnan(x)
                if c not in NO_INDICATOR:
                    blocks.append(miss.astype(float)); names.append(f"{c}_missing")
                x = np.where(miss, self.medians[c], x)
            blocks.append(x); names.append(c)
        return np.column_stack(blocks), names

    def fit(self, df: pl.DataFrame) -> "LogitPrep":
        self.levels = {c: sorted(df[c].unique().to_list()) for c in self.cols if c in NOMINAL}
        self.medians = {}
        for c in self.cols:
            if c in NOMINAL:
                continue
            x = _numeric(df, c)
            if np.isnan(x).any():
                if c not in NOT_LOGGED and c not in BOOLEAN and c != "highest_education":
                    x = np.log1p(x)
                self.medians[c] = float(np.nanmedian(x))
        X, self.names = self._raw(df)
        self.mean = X.mean(axis=0)
        sd = X.std(axis=0)
        self.constant = [n for n, s in zip(self.names, sd) if s == 0]
        self.sd = np.where(sd == 0, 1.0, sd)
        return self

    def transform(self, df: pl.DataFrame) -> np.ndarray:
        X, names = self._raw(df)
        assert names == self.names
        return (X - self.mean) / self.sd


class TreePrep:
    """Inputs of the boosted trees: untransformed predictors, module as a category, education as ordered code."""

    def __init__(self, cols: list[str]):
        self.cols = cols

    def fit(self, df: pl.DataFrame) -> "TreePrep":
        self.levels = sorted(df["code_module"].unique().to_list()) if "code_module" in self.cols else []
        self.names = list(self.cols)
        self.cat_idx = [self.cols.index("code_module")] if "code_module" in self.cols else []
        return self

    def transform(self, df: pl.DataFrame) -> np.ndarray:
        blocks = []
        for c in self.cols:
            if c == "code_module":
                code = {m: float(i) for i, m in enumerate(self.levels)}
                blocks.append(np.array([code.get(v, np.nan) for v in df[c].to_list()]))   # unseen module -> missing
            elif c == "start_month":
                blocks.append((df[c] == "J").cast(pl.Float64).to_numpy())
            else:
                blocks.append(_numeric(df, c))
        return np.column_stack(blocks)


def _logloss(y: np.ndarray, p: np.ndarray) -> float:
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return float(-(y * np.log(p) + (1 - y) * np.log(1 - p)).sum())


def without_students_of(train: pl.DataFrame, val: pl.DataFrame) -> pl.DataFrame:
    """Remove from the training rows every enrolment of a student who also appears in the validation run."""
    return train.filter(~pl.col("id_student").is_in(val["id_student"].unique().to_list()))


def hp_grid(kind: str) -> list[dict]:
    if kind == "logit":
        return [{"C": c} for c in C_GRID]                                     # ordered: strongest penalty first
    return [{"max_depth": d, "learning_rate": lr, "trees": t} for d in GBT_DEPTH for t in GBT_TREES for lr in GBT_LR]


def _fit_predict_grid(kind: str, cols: list[str], tr: pl.DataFrame, va: pl.DataFrame) -> dict[str, np.ndarray]:
    """Fit on tr for every grid point and return validation probabilities keyed by the JSON of the grid point."""
    ytr = tr["non_completion"].to_numpy().astype(int)
    out = {}
    if kind == "logit":
        prep = LogitPrep(cols).fit(tr)
        Xtr, Xva = prep.transform(tr), prep.transform(va)
        for C in C_GRID:
            m = LogisticRegression(C=C, max_iter=5000, tol=1e-8).fit(Xtr, ytr)
            out[json.dumps({"C": C})] = m.predict_proba(Xva)[:, 1]
    else:
        prep = TreePrep(cols).fit(tr)
        Xtr, Xva = prep.transform(tr), prep.transform(va)
        for d in GBT_DEPTH:
            for lr in GBT_LR:
                m = HistGradientBoostingClassifier(max_depth=d, learning_rate=lr, max_iter=max(GBT_TREES), early_stopping=False,
                                                   categorical_features=prep.cat_idx or None, random_state=lib.SEED).fit(Xtr, ytr)
                for i, p in enumerate(m.staged_predict_proba(Xva), start=1):
                    if i in GBT_TREES:
                        out[json.dumps({"max_depth": d, "learning_rate": lr, "trees": i})] = p[:, 1]
    return out


def tune(config: str, cutoff: int, train: pl.DataFrame) -> tuple[dict, list[dict]]:
    """Leave-one-run-out tuning inside `train`; criterion = pooled log loss; ties go to the earlier grid point."""
    kind, cols = CONFIGS[config]["kind"], predictors(config, cutoff)
    total: dict[str, float] = {}
    n = 0
    for run in sorted(train["run"].unique().to_list()):
        va = train.filter(pl.col("run") == run)
        tr = without_students_of(train.filter(pl.col("run") != run), va)
        yva = va["non_completion"].to_numpy().astype(float)
        for key, p in _fit_predict_grid(kind, cols, tr, va).items():
            total[key] = total.get(key, 0.0) + _logloss(yva, p)
        n += va.height
    table = [{**hp, "inner_log_loss": total[json.dumps(hp)] / n} for hp in hp_grid(kind)]
    best = min(table, key=lambda r: round(r["inner_log_loss"], 6))            # min keeps the first of equal values
    return {k: v for k, v in best.items() if k != "inner_log_loss"}, table


def fit_final(config: str, cutoff: int, train: pl.DataFrame, hp: dict) -> dict:
    kind, cols = CONFIGS[config]["kind"], predictors(config, cutoff)
    y = train["non_completion"].to_numpy().astype(int)
    if kind == "logit":
        prep = LogitPrep(cols).fit(train)
        model = LogisticRegression(C=hp["C"], max_iter=5000, tol=1e-8).fit(prep.transform(train), y)
    else:
        prep = TreePrep(cols).fit(train)
        model = HistGradientBoostingClassifier(max_depth=hp["max_depth"], learning_rate=hp["learning_rate"], max_iter=hp["trees"],
                                               early_stopping=False, categorical_features=prep.cat_idx or None,
                                               random_state=lib.SEED).fit(prep.transform(train), y)
    return {"config": config, "cutoff": cutoff, "kind": kind, "hp": hp, "prep": prep, "model": model,
            "train_rows": train.height, "train_runs": sorted(train["run"].unique().to_list())}


def predict(bundle: dict, df: pl.DataFrame) -> np.ndarray:
    return bundle["model"].predict_proba(bundle["prep"].transform(df))[:, 1]


def metrics_rows(df: pl.DataFrame, score_cols: dict[str, str], cutoff: int, per20s=(5, 3)) -> pl.DataFrame:
    """Per-run list metrics for each ranking in score_cols (name -> column); df needs run, non_completion, tiebreak_u."""
    rows = []
    for run in sorted(df["run"].unique().to_list()):
        d = df.filter(pl.col("run") == run)
        y, tie = d["non_completion"].to_numpy().astype(bool), d["tiebreak_u"].to_numpy()
        for name, col in score_cols.items():
            rank = lib.rank_desc(d[col].to_numpy(), tie)
            for per20 in per20s:
                k = lib.list_len(d.height, per20)
                rows.append({"ranking": name, "cutoff": cutoff, "per20": per20, "run": run, **lib.run_metrics(rank, y, k)})
    return pl.DataFrame(rows)


def pooled(metrics: pl.DataFrame) -> pl.DataFrame:
    g = metrics.group_by("ranking", "cutoff", "per20").agg(
        pl.len().alias("runs"), pl.col("n").sum().alias("enrolments"), pl.col("non_completers").sum(), pl.col("list_length").sum(),
        pl.col("non_completers_on_list").sum(), pl.col("max_attainable").sum(), pl.col("random_expected_tp").sum())
    return g.with_columns(
        (pl.col("non_completers_on_list") / pl.col("max_attainable")).alias("pooled_normalised_recall"),
        (pl.col("non_completers_on_list") / pl.col("non_completers")).alias("pooled_recall"),
        (pl.col("non_completers_on_list") / pl.col("list_length")).alias("pooled_precision"),
        (pl.col("non_completers") / pl.col("enrolments")).alias("base_rate"),
        (pl.col("max_attainable") / pl.col("list_length")).alias("max_attainable_precision"),
        (pl.col("random_expected_tp") / pl.col("max_attainable")).alias("random_list_normalised_recall"),
    ).with_columns((pl.col("pooled_precision") / pl.col("base_rate")).alias("pooled_lift")).sort("cutoff", "per20", "ranking")


def gate(df: pl.DataFrame, col_a: str, col_b: str, per20: int, B: int = lib.B_BOOT) -> dict:
    """Ranking a against ranking b on the same runs: the S1 quantities of the Level 1 report (Table 4.5).

    Pooled normalised recall of both, their difference with a paired two-level bootstrap interval, the exact
    one-sided sign-flip test on per-run differences, wins / ties / losses and the unweighted mean difference.
    """
    runs, per_run = [], []
    for run in sorted(df["run"].unique().to_list()):
        d = df.filter(pl.col("run") == run)
        y, tie = d["non_completion"].to_numpy().astype(bool), d["tiebreak_u"].to_numpy()
        ra, rb = lib.rank_desc(d[col_a].to_numpy(), tie), lib.rank_desc(d[col_b].to_numpy(), tie)
        k = lib.list_len(d.height, per20)
        ma, mb = lib.run_metrics(ra, y, k), lib.run_metrics(rb, y, k)
        runs.append({"y": y, "rank_a": ra, "rank_b": rb})
        per_run.append({"run": run, "n": d.height, "list_length": k, "non_completers": ma["non_completers"], "max_attainable": ma["max_attainable"],
                        "tp_a": ma["non_completers_on_list"], "tp_b": mb["non_completers_on_list"],
                        "nr_a": ma["normalised_recall"], "nr_b": mb["normalised_recall"],
                        "tp_a_expected_ties": lib.expected_tp_with_ties(d[col_a].to_numpy(), y, k),
                        "tp_b_expected_ties": lib.expected_tp_with_ties(d[col_b].to_numpy(), y, k)})
    pr = pl.DataFrame(per_run).with_columns((pl.col("nr_a") - pl.col("nr_b")).alias("difference"))
    tot = pr["max_attainable"].sum()
    a, b = pr["tp_a"].sum() / tot, pr["tp_b"].sum() / tot
    boot = lib.paired_bootstrap_nr(runs, per20, B=B)
    diffs = pr["difference"].to_numpy()
    p, cnt, total = lib.sign_flip_p(diffs)
    out = {
        "runs": pr.height, "enrolments": int(pr["n"].sum()), "list_places": int(pr["list_length"].sum()),
        "tp_a": int(pr["tp_a"].sum()), "tp_b": int(pr["tp_b"].sum()), "max_attainable": int(tot),
        "pooled_nr_a": a, "pooled_nr_b": b, "difference": a - b,
        "boot_ci_low": float(boot["ci_diff"][0]), "boot_ci_high": float(boot["ci_diff"][1]),
        "ci_a_low": float(boot["ci_a"][0]), "ci_a_high": float(boot["ci_a"][1]),
        "ci_b_low": float(boot["ci_b"][0]), "ci_b_high": float(boot["ci_b"][1]),
        "boot_share_diff_le_0": boot["share_diff_le_0"],
        "signflip_p": p, "signflip_count": cnt, "signflip_total": total,
        "wins": int((diffs > 0).sum()), "ties": int((diffs == 0).sum()), "losses": int((diffs < 0).sum()),
        "mean_per_run_difference": float(diffs.mean()),
        "pooled_nr_a_expected_ties": float(pr["tp_a_expected_ties"].sum() / tot),
        "pooled_nr_b_expected_ties": float(pr["tp_b_expected_ties"].sum() / tot),
    }
    out["passes"] = bool(out["difference"] > 0 and out["boot_ci_low"] > 0 and out["signflip_p"] < 0.05)
    return {"summary": out, "per_run": pr, "boot": boot}
