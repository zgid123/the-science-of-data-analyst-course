"""AQ2 association model (Level 1 report, Section 3.2 and Table 4.2; PROTOCOL.md P16, P17, P21, P22).

Logistic regression of non-completion on five early signs, with a fixed effect per module run, adjustment for
previous attempts and credits, and sign x module terms. It measures association; it makes no causal claim.

Where a sign is defined (P16)
    task missed, any task late   runs with a TMA or CMA due by day 27
    TMA late                     runs with a TMA due by day 27 (the CCC runs have only a CMA due by then)
    the three click signs        every run

Support of a sign (P17)
    Inside the runs where the sign is defined, a module has its own slope when it holds at least MIN_CELL enrolments
    with the sign and MIN_CELL without it. Smaller modules with at least one enrolment on each side share one pooled
    slope. A module with nobody on one side has no term at all. The support is the set of rows that carry a term.

The adjusted risk difference of a sign is the average, over its support and over nothing else, of the predicted risk
with the sign set to 1 minus the predicted risk with the sign set to 0, every other column as observed. Its 95%
interval comes from the delta method with HC1 robust standard errors. Every estimate is returned with the number of
rows it averages over.
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
VARIANT_LABELS = {
    "sign_low_activity_q25": "Clicks below a quarter of the run median",
    "sign_low_activity_median": "Clicks below the run median",
    "sign_low_activity_dedup": "De-duplicated clicks below half the run median",
    "sign_any_task_late": "TMA or CMA submitted late",
}
ANY_TASK_SIGNS = ("sign_task_missed", "sign_any_task_late")      # defined where a TMA or CMA is due by day 27
TMA_SIGNS = ("sign_tma_late",)                                    # defined where a TMA is due by day 27
MIN_CELL = 20
Z = 1.959963984540054
CONTINUOUS_ACTIVITY = "log1p_clicks_0_27"                         # post hoc adjustment column (P22)
ACTIVITY_LEVELS5 = ["1 no click on days 0-27", "2 below half the run median", "3 half the median to the median",
                    "4 median to twice the median", "5 twice the median or more"]


def expit(x):
    return 1.0 / (1.0 + np.exp(-x))


def defined_rows(df: pl.DataFrame, sign: str) -> np.ndarray:
    """Rows of the runs whose calendar lets the sign occur (P16)."""
    if sign in ANY_TASK_SIGNS:
        return df["run_has_task_due"].to_numpy().astype(bool)
    if sign in TMA_SIGNS:
        return df["run_has_tma_due"].to_numpy().astype(bool)
    return np.ones(df.height, bool)


def sign_terms(df: pl.DataFrame, sign: str, interactions: bool = True) -> tuple[list[tuple[str, np.ndarray]], list[dict]]:
    """The model terms of one sign and a note per module (P17).

    Returns ([(label, row mask)], notes). The union of the masks is the support of the sign. A module with no
    enrolment with the sign, or none without it, gets no term: its rows are outside the support.
    """
    x = df[sign].to_numpy().astype(bool)
    d = defined_rows(df, sign)
    module = df["code_module"].to_numpy()
    own, pooled, notes = [], np.zeros(df.height, bool), []
    for m in sorted(set(module)):
        mm = d & (module == m)
        n1, n0 = int((x & mm).sum()), int((~x & mm).sum())
        if not mm.any():
            handling = "sign not defined in this module's runs: no term, outside the support"
        elif n1 == 0 or n0 == 0:
            handling = "sign does not vary in this module: no term, outside the support"
        elif n1 >= MIN_CELL and n0 >= MIN_CELL:
            handling = "own slope"
            own.append((m, mm))
        else:
            handling = f"cell below {MIN_CELL}: pooled slope"
            pooled |= mm
        notes.append({"sign": sign, "code_module": m, "rows_defined": int(mm.sum()), "with_sign": n1, "without_sign": n0, "handling": handling})
    if not interactions:
        mask = np.zeros(df.height, bool)
        for _, mm in own:
            mask |= mm
        mask |= pooled
        return ([("all", mask)] if mask.any() else []), notes
    terms = list(own)
    if pooled.any():
        terms.append(("other", pooled))
    return terms, notes


def support_rows(df: pl.DataFrame, sign: str) -> np.ndarray:
    mask = np.zeros(df.height, bool)
    for _, mm in sign_terms(df, sign)[0]:
        mask |= mm
    return mask


def unadjusted(df: pl.DataFrame, signs: list[str]) -> pl.DataFrame:
    """Plain rate difference with / without the sign, on the support of the sign (Newcombe interval)."""
    y = df["non_completion"].to_numpy().astype(bool)
    rows = []
    for s in signs:
        d = support_rows(df, s)
        x = df[s].to_numpy().astype(bool)
        k1, n1 = int(y[d & x].sum()), int((d & x).sum())
        k0, n0 = int(y[d & ~x].sum()), int((d & ~x).sum())
        if n1 == 0 or n0 == 0:
            rows.append({"sign": s, "enrolments": int(d.sum()), "with_sign": n1, "share_with_sign": float("nan"), "rate_with_sign": float("nan"),
                         "rate_without_sign": float("nan"), "unadjusted_rd": float("nan"), "unadj_ci_low": float("nan"),
                         "unadj_ci_high": float("nan"), "risk_ratio": float("nan")})
            continue
        rd, lo, hi = diff_proportions_ci(k1, n1, k0, n0)
        rows.append({"sign": s, "enrolments": int(d.sum()), "with_sign": n1, "share_with_sign": n1 / d.sum(),
                     "rate_with_sign": k1 / n1, "rate_without_sign": k0 / n0, "unadjusted_rd": rd, "unadj_ci_low": lo,
                     "unadj_ci_high": hi, "risk_ratio": (k1 / n1) / (k0 / n0)})
    return pl.DataFrame(rows)


class AssociationModel:
    def __init__(self, df: pl.DataFrame, signs: list[str], interactions: bool = True, extra: list[str] | None = None):
        self.df, self.signs, self.interactions, self.extra = df, signs, interactions, list(extra or [])
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
        for c in self.extra:
            cols.append(df[c].to_numpy().astype(float)); names.append(c)
        self.sign_cols: dict[str, list[tuple[int, np.ndarray]]] = {}   # sign -> [(column index, row mask of the term)]
        self.sign_modules: dict[str, list[str]] = {}                   # modules with their own slope
        self.support: dict[str, np.ndarray] = {}                       # rows that carry a term of the sign
        self.cell_notes: list[dict] = []
        for s in signs:
            x = df[s].to_numpy().astype(float)
            terms, notes = sign_terms(df, s, interactions)
            self.cell_notes.extend(notes)
            self.sign_modules[s] = [label for label, _ in terms if label not in ("other", "all")]
            self.sign_cols[s] = []
            self.support[s] = np.zeros(n, bool)
            for label, mask in terms:
                col = x * mask
                assert 0 < col.sum() < mask.sum(), f"{s}:{label} does not vary inside its term"
                cols.append(col); names.append(f"{s}:{label}")
                self.sign_cols[s].append((len(cols) - 1, mask))
                self.support[s] |= mask
        self.X = np.column_stack(cols)
        self.names = names
        self.fit = sm.GLM(self.y, self.X, family=sm.families.Binomial()).fit(cov_type="HC1", maxiter=200)
        self.beta = np.asarray(self.fit.params)
        self.V = np.asarray(self.fit.cov_params())
        self.p = expit(self.X @ self.beta)

    # -- average risk difference over rows of the support -------------------------------------------------
    def risk_difference(self, sign: str, rows: np.ndarray | None = None) -> dict:
        """Average of (risk with the sign - risk without it) over the support of the sign, optionally within `rows`."""
        sup = self.support[sign]
        rows = sup if rows is None else (sup & rows)
        n = int(rows.sum())
        x = self.df[sign].to_numpy().astype(bool)
        base = {"n": n, "with_sign": int((x & rows).sum()), "support_modules": len(set(self.module[rows]))}
        if n == 0:
            return {**base, "rd": float("nan"), "se": float("nan"), "ci_low": float("nan"), "ci_high": float("nan"),
                    "risk_with": float("nan"), "risk_without": float("nan")}
        X1, X0 = self.X[rows].copy(), self.X[rows].copy()
        covered = np.zeros(n, bool)
        for j, mask in self.sign_cols[sign]:
            X1[:, j] = mask[rows].astype(float)
            X0[:, j] = 0.0
            covered |= mask[rows]
        assert covered.all(), f"{sign}: a row outside the support entered the average"
        p1, p0 = expit(X1 @ self.beta), expit(X0 @ self.beta)
        est = float(np.mean(p1 - p0))
        grad = ((p1 * (1 - p1))[:, None] * X1 - (p0 * (1 - p0))[:, None] * X0).mean(axis=0)
        se = float(np.sqrt(grad @ self.V @ grad))
        return {**base, "rd": est, "se": se, "ci_low": est - Z * se, "ci_high": est + Z * se,
                "risk_with": float(p1.mean()), "risk_without": float(p0.mean())}

    def table(self) -> pl.DataFrame:
        rows = []
        for s in self.signs:
            r = self.risk_difference(s)
            outside = int(defined_rows(self.df, s).sum()) - r["n"]
            rows.append({"sign": s, "n_support": r["n"], "n_with_sign": r["with_sign"], "support_modules": r["support_modules"],
                         "rows_defined_outside_support": outside, "adjusted_rd": r["rd"], "adj_se": r["se"],
                         "adj_ci_low": r["ci_low"], "adj_ci_high": r["ci_high"],
                         "adj_risk_with": r["risk_with"], "adj_risk_without": r["risk_without"]})
        return pl.DataFrame(rows)

    def by_module(self) -> pl.DataFrame:
        rows = []
        for s in self.signs:
            for m in self.sign_modules[s]:
                r = self.risk_difference(s, self.module == m)
                rows.append({"sign": s, "code_module": m, "enrolments": r["n"], "with_sign": r["with_sign"],
                             "adjusted_rd": r["rd"], "adj_ci_low": r["ci_low"], "adj_ci_high": r["ci_high"],
                             "interval_excludes_0": bool(r["ci_low"] > 0 or r["ci_high"] < 0)})
        return pl.DataFrame(rows)

    def odds_ratios(self) -> pl.DataFrame:
        ci = np.asarray(self.fit.conf_int())
        rows = []
        for s in self.signs:
            for j, mask in self.sign_cols[s]:
                rows.append({"term": self.names[j], "n_support": int(mask.sum()), "odds_ratio": float(np.exp(self.beta[j])),
                             "or_ci_low": float(np.exp(ci[j, 0])), "or_ci_high": float(np.exp(ci[j, 1])), "p_value": float(self.fit.pvalues[j])})
        return pl.DataFrame(rows)

    def support_table(self) -> pl.DataFrame:
        return pl.DataFrame(self.cell_notes)


def verdicts(overall: pl.DataFrame, by_mod: pl.DataFrame) -> pl.DataFrame:
    """Level 1 success criterion (Table 4.2): >= 5 points, interval excluding 0, same direction in >= 2/3 of modules.

    `verdict` applies the criterion as Level 1 words it, with the direction of each module's point estimate.
    `verdict_strict` counts a module only when its own interval excludes 0 on the same side (P17), so that a module
    estimate indistinguishable from 0 is not counted as agreement.
    """
    rows = []
    for r in overall.iter_rows(named=True):
        bm = by_mod.filter(pl.col("sign") == r["sign"])
        direction = np.sign(r["adjusted_rd"])
        est, lo, hi = bm["adjusted_rd"].to_numpy(), bm["adj_ci_low"].to_numpy(), bm["adj_ci_high"].to_numpy()
        same = int((np.sign(est) == direction).sum())
        strict = int((((lo > 0) & (direction > 0)) | ((hi < 0) & (direction < 0))).sum())
        unclear = [m for m, a, b in zip(bm["code_module"].to_list(), lo, hi) if a <= 0 <= b]
        nm = bm.height
        big = abs(r["adjusted_rd"]) >= 0.05
        excl = (r["adj_ci_low"] > 0) or (r["adj_ci_high"] < 0)
        cons, cons_strict = nm > 0 and same / nm >= 2 / 3, nm > 0 and strict / nm >= 2 / 3
        rows.append({"sign": r["sign"], "adjusted_rd": r["adjusted_rd"], "at_least_5_points": bool(big), "interval_excludes_0": bool(excl),
                     "modules_defined": nm, "modules_same_direction": same, "modules_same_direction_interval_excludes_0": strict,
                     "modules_interval_includes_0": ", ".join(unclear) if unclear else "none",
                     "two_thirds_same_direction": bool(cons),
                     "verdict": "consistent association" if (big and excl and cons) else "weak or inconsistent",
                     "verdict_strict": "consistent association" if (big and excl and cons_strict) else "weak or inconsistent"})
    return pl.DataFrame(rows)


def activity_level5(df: pl.DataFrame) -> np.ndarray:
    """Five activity levels on days 0-27 (P21 b); returns the label of each row."""
    clicks, ratio = df["clicks_0c"].to_numpy(), df["activity_ratio_run"].to_numpy()
    out = np.full(df.height, ACTIVITY_LEVELS5[4], dtype=object)
    out[ratio < 2.0] = ACTIVITY_LEVELS5[3]
    out[ratio < 1.0] = ACTIVITY_LEVELS5[2]
    out[ratio < 0.5] = ACTIVITY_LEVELS5[1]
    out[clicks == 0] = ACTIVITY_LEVELS5[0]
    return out


def risk_deciles(p: np.ndarray) -> np.ndarray:
    """Tenths of the predicted risk, 1 = lowest; equal-sized groups by rank (ties by row order)."""
    order = np.argsort(p, kind="stable")
    dec = np.empty(len(p), dtype=np.int64)
    dec[order] = np.arange(len(p)) * 10 // len(p) + 1
    return dec
