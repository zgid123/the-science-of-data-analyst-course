"""AQ2 association model (Level 1 report, Section 3.2 and Table 4.2; PROTOCOL.md P16–P17).

Logistic regression of non-completion on five early signs, with a fixed effect per module run, adjustment for
previous attempts and credits, and sign x module terms. It measures association; it makes no causal claim.

The adjusted risk difference of a sign is the average, over the enrolments where the sign is defined, of the
predicted risk with the sign set to 1 minus the predicted risk with the sign set to 0, every other column as
observed. Its 95% interval comes from the delta method with HC1 robust standard errors.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import polars as pl
import statsmodels.api as sm

HERE = Path(__file__).resolve().parent
AQ = HERE.parent
sys.path.insert(0, str(AQ.parent / "common"))
import lib  # noqa: E402
from stats_helpers import diff_proportions_ci  # noqa: E402

EXTRACT = AQ / "extracted-datasets"
RESULTS = AQ / "results"
FIGURES = AQ / "figures"

SIGNS = {
    "sign_task_missed": "Task due by day 27 not submitted",
    "sign_tma_late": "TMA submitted late",
    "sign_inactive_last7": "No platform activity in the last 7 days",
    "sign_low_activity": "Clicks below half the run median",
    "sign_no_pre_activity": "No activity before the start",
}
TASK_SIGNS = ("sign_task_missed", "sign_tma_late", "sign_any_task_late")
MIN_CELL = 20
Z = 1.959963984540054


def expit(x):
    return 1.0 / (1.0 + np.exp(-x))


def defined_rows(df: pl.DataFrame, sign: str) -> np.ndarray:
    """A task sign is defined only in runs with a task due by day 27; activity signs everywhere."""
    if sign in TASK_SIGNS:
        return df["run_has_task_due"].to_numpy()
    return np.ones(df.height, bool)


def unadjusted(df: pl.DataFrame, signs: list[str]) -> pl.DataFrame:
    y = df["non_completion"].to_numpy().astype(bool)
    rows = []
    for s in signs:
        d = defined_rows(df, s)
        x = df[s].to_numpy().astype(bool)
        k1, n1 = int(y[d & x].sum()), int((d & x).sum())
        k0, n0 = int(y[d & ~x].sum()), int((d & ~x).sum())
        rd, lo, hi = diff_proportions_ci(k1, n1, k0, n0)
        rows.append({"sign": s, "enrolments_defined": int(d.sum()), "with_sign": n1, "share_with_sign": n1 / d.sum(),
                     "rate_with_sign": k1 / n1, "rate_without_sign": k0 / n0, "unadjusted_rd": rd, "unadj_ci_low": lo,
                     "unadj_ci_high": hi, "risk_ratio": (k1 / n1) / (k0 / n0)})
    return pl.DataFrame(rows)


class AssociationModel:
    def __init__(self, df: pl.DataFrame, signs: list[str], interactions: bool = True):
        self.df, self.signs, self.interactions = df, signs, interactions
        self.y = df["non_completion"].to_numpy().astype(float)
        self.module = df["code_module"].to_numpy()
        self.run = df["run"].to_numpy()
        n = df.height
        cols, names = [np.ones(n)], ["intercept"]
        runs = sorted(set(self.run))
        for r in runs[1:]:
            cols.append((self.run == r).astype(float)); names.append(f"run[{r}]")
        cols.append(np.log1p(df["num_of_prev_attempts"].to_numpy().astype(float))); names.append("log1p_prev_attempts")
        cols.append(np.log1p(df["studied_credits"].to_numpy().astype(float))); names.append("log1p_credits")
        self.sign_cols: dict[str, list[tuple[int, np.ndarray]]] = {}   # sign -> [(column index, row mask of the term)]
        self.sign_modules: dict[str, list[str]] = {}
        self.cell_notes = []
        for s in signs:
            x = df[s].to_numpy().astype(float)
            d = defined_rows(df, s)
            terms = []
            if interactions:
                ok, pooled = [], np.zeros(n, bool)
                for m in sorted(set(self.module[d])):
                    mm = d & (self.module == m)
                    n1, n0 = int(x[mm].sum()), int((1 - x[mm]).sum())
                    if n1 >= MIN_CELL and n0 >= MIN_CELL:
                        ok.append(m); terms.append((m, mm))
                    else:
                        pooled |= mm
                        self.cell_notes.append({"sign": s, "module": m, "with_sign": n1, "without_sign": n0, "handling": "not defined (cell below 20); pooled slope"})
                self.sign_modules[s] = ok
                if pooled.any() and x[pooled].sum() > 0:
                    terms.append(("other", pooled))
            else:
                terms.append(("all", d))
                self.sign_modules[s] = []
            self.sign_cols[s] = []
            for label, mask in terms:
                cols.append(x * mask); names.append(f"{s}:{label}")
                self.sign_cols[s].append((len(cols) - 1, mask))
        self.X = np.column_stack(cols)
        self.names = names
        self.fit = sm.GLM(self.y, self.X, family=sm.families.Binomial()).fit(cov_type="HC1", maxiter=200)
        self.beta = np.asarray(self.fit.params)
        self.V = np.asarray(self.fit.cov_params())
        self.p = expit(self.X @ self.beta)

    # -- average risk difference over a set of rows -----------------------------------------------------
    def risk_difference(self, sign: str, rows: np.ndarray | None = None) -> dict:
        d = defined_rows(self.df, sign)
        rows = d if rows is None else (d & rows)
        X1, X0 = self.X[rows].copy(), self.X[rows].copy()
        for j, mask in self.sign_cols[sign]:
            X1[:, j] = mask[rows].astype(float)
            X0[:, j] = 0.0
        p1, p0 = expit(X1 @ self.beta), expit(X0 @ self.beta)
        est = float(np.mean(p1 - p0))
        grad = ((p1 * (1 - p1))[:, None] * X1 - (p0 * (1 - p0))[:, None] * X0).mean(axis=0)
        se = float(np.sqrt(grad @ self.V @ grad))
        return {"rd": est, "se": se, "ci_low": est - Z * se, "ci_high": est + Z * se, "n": int(rows.sum()),
                "risk_with": float(p1.mean()), "risk_without": float(p0.mean())}

    def table(self) -> pl.DataFrame:
        rows = []
        for s in self.signs:
            r = self.risk_difference(s)
            rows.append({"sign": s, "enrolments_defined": r["n"], "adjusted_rd": r["rd"], "adj_ci_low": r["ci_low"],
                         "adj_ci_high": r["ci_high"], "adj_risk_with": r["risk_with"], "adj_risk_without": r["risk_without"]})
        return pl.DataFrame(rows)

    def by_module(self) -> pl.DataFrame:
        rows = []
        for s in self.signs:
            x = self.df[s].to_numpy().astype(bool)
            for m in self.sign_modules[s]:
                mm = self.module == m
                r = self.risk_difference(s, mm)
                d = defined_rows(self.df, s) & mm
                rows.append({"sign": s, "code_module": m, "enrolments": r["n"], "with_sign": int(x[d].sum()),
                             "adjusted_rd": r["rd"], "adj_ci_low": r["ci_low"], "adj_ci_high": r["ci_high"]})
        return pl.DataFrame(rows)

    def odds_ratios(self) -> pl.DataFrame:
        ci = np.asarray(self.fit.conf_int())
        rows = []
        for s in self.signs:
            for j, _ in self.sign_cols[s]:
                rows.append({"term": self.names[j], "odds_ratio": float(np.exp(self.beta[j])), "or_ci_low": float(np.exp(ci[j, 0])),
                             "or_ci_high": float(np.exp(ci[j, 1])), "p_value": float(self.fit.pvalues[j])})
        return pl.DataFrame(rows)


def verdicts(overall: pl.DataFrame, by_mod: pl.DataFrame) -> pl.DataFrame:
    """Level 1 success criterion (Table 4.2): >= 5 points, interval excluding 0, same direction in >= 2/3 of modules."""
    rows = []
    for r in overall.iter_rows(named=True):
        bm = by_mod.filter(pl.col("sign") == r["sign"])
        direction = np.sign(r["adjusted_rd"])
        same = int((np.sign(bm["adjusted_rd"].to_numpy()) == direction).sum())
        nm = bm.height
        big = abs(r["adjusted_rd"]) >= 0.05
        excl = (r["adj_ci_low"] > 0) or (r["adj_ci_high"] < 0)
        cons = nm > 0 and same / nm >= 2 / 3
        rows.append({"sign": r["sign"], "adjusted_rd": r["adjusted_rd"], "at_least_5_points": big, "interval_excludes_0": excl,
                     "modules_defined": nm, "modules_same_direction": same, "two_thirds_same_direction": cons,
                     "verdict": "consistent association" if (big and excl and cons) else "weak or inconsistent"})
    return pl.DataFrame(rows)
