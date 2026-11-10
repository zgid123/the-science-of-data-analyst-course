"""Step 8 of Appendix III (Change Log C14): AQ2 associations re-estimated on the 13 runs of 2014, CCC included, only
after the single AQ3 test. Nothing here changes AQ3.

Method: copied from reports/milestone-5/code/aq_analysis.py (functions build_signs, defined_mask, class Fit, verdict,
constants SIGNS, TASK_SIGNS, Z, helper r); one change, marked in Fit: sign x module terms only for modules where the
sign occurs. That file is read, never edited.
The 2013 estimates are recomputed with the same code and checked against reports/milestone-5/results/
aq2_associations.csv and aq2_module_effects.csv (equality at their rounding), so both years come from one method.

Run: venv/bin/python reports/milestone-4/package/src/11_aq2_replication.py
Writes results/aq2_replication.csv (contract columns) and results/aq2_replication_detail.csv (verdicts, sizes).
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
import polars as pl
import statsmodels.api as sm

import common as C

M5_RESULTS = C.PKG.parents[1] / "milestone-5" / "results"

# ---------------------------------------------------------------- copied from milestone-5/code/aq_analysis.py
Z = 1.959963984540054
SIGNS = {
    "missed_task": "a task (TMA or CMA) due by day 27 not submitted by day 27",
    "late_tma": "a TMA due by day 27 submitted late by day 27",
    "inactive_last7": "no click on days 21-27",
    "low_relative_activity": "clicks on days 0-27 below the run median",
    "no_pre_start_activity": "no click before day 0",
}
TASK_SIGNS = {"missed_task", "late_tma"}


def r(v, k=4):
    return None if v is None or (isinstance(v, float) and math.isnan(v)) else round(float(v), k) + 0.0


def build_signs(f: pl.DataFrame, variant: str = "primary") -> pl.DataFrame:
    f = f.with_columns(
        (pl.col("code_module") + " " + pl.col("code_presentation")).alias("run"),
        pl.col("tasks_due_c").max().over("code_module", "code_presentation").alias("run_tasks_due"),
    )
    ratio = pl.col("activity_ratio_run")
    thr = 1.0
    late = pl.col("tma_late_c") >= 1
    return f.with_columns(
        (pl.col("tasks_missed_c") >= 1).cast(pl.Int8).alias("missed_task"),
        late.cast(pl.Int8).alias("late_tma"),
        pl.col("inactive_last7").cast(pl.Int8).alias("inactive_last7"),
        (ratio < thr).cast(pl.Int8).alias("low_relative_activity"),
        (pl.col("clicks_pre") == 0).cast(pl.Int8).alias("no_pre_start_activity"),
        pl.col("non_completion").cast(pl.Int8).alias("y"),
        (pl.col("run_tasks_due") >= 1).alias("task_run"),
    )


def defined_mask(f: pl.DataFrame, s: str) -> np.ndarray:
    return f["task_run"].to_numpy() if s in TASK_SIGNS else np.ones(f.height, bool)


class Fit:
    """Logistic regression of non-completion with run fixed effects, background adjustment, signs and sign x module
    terms coded as deviations from the average module. Robust (HC1) covariance, no clustering."""

    def __init__(self, f: pl.DataFrame, signs: list[str], interactions: bool = True):
        self.f, self.signs, self.interactions = f, signs, interactions
        runs = sorted(f["run"].unique().to_list())
        cols, names = [np.ones(f.height)], ["const"]
        for rn in runs[1:]:
            cols.append((f["run"] == rn).to_numpy().astype(float))
            names.append(f"run[{rn}]")
        cols.append(f["num_of_prev_attempts"].to_numpy().astype(float))
        names.append("num_of_prev_attempts")
        cols.append(f["studied_credits"].to_numpy().astype(float) / 30.0)
        names.append("studied_credits_per30")
        self.mods: dict[str, list[str]] = {}
        mod = f["code_module"].to_numpy()
        for s in signs:
            sv = f[s].to_numpy().astype(float)
            cols.append(sv)
            names.append(s)
            # one change to the copied code: a module gets a sign x module term only if the sign occurs there
            # (in 2014, no CCC enrolment has a late TMA, so its term would be an all-zero column and the model
            # singular); such a module receives the average-module effect. In 2013 the sets are identical.
            ms = sorted(set(mod[defined_mask(f, s) & (sv > 0)]))
            self.mods[s] = ms
            if interactions and len(ms) > 1:
                ref = ms[-1]
                for m in ms[:-1]:
                    z = (mod == m).astype(float) - (mod == ref).astype(float)
                    cols.append(sv * z)
                    names.append(f"{s}:dev[{m}]")
        self.X = np.column_stack(cols)
        self.names = names
        self.idx = {n: i for i, n in enumerate(names)}
        self.y = f["y"].to_numpy().astype(float)
        res = sm.Logit(self.y, self.X).fit(method="newton", maxiter=100, disp=0, cov_type="HC1")
        self.converged = bool(res.mle_retvals["converged"])
        self.b, self.V, self.res = np.asarray(res.params), np.asarray(res.cov_params()), res
        self.mod = mod

    def _set(self, rows: np.ndarray, s: str, val: float) -> np.ndarray:
        X = self.X[rows].copy()
        X[:, self.idx[s]] = val
        if self.interactions:
            for m in self.mods[s][:-1]:
                j = self.idx[f"{s}:dev[{m}]"]
                ref = self.mods[s][-1]
                z = (self.mod[rows] == m).astype(float) - (self.mod[rows] == ref).astype(float)
                X[:, j] = val * z
        return X

    def ame(self, s: str, rows: np.ndarray) -> tuple[float, float, float, float]:
        X1, X0 = self._set(rows, s, 1.0), self._set(rows, s, 0.0)
        p1, p0 = 1 / (1 + np.exp(-X1 @ self.b)), 1 / (1 + np.exp(-X0 @ self.b))
        est = float(np.mean(p1 - p0))
        g = (X1 * (p1 * (1 - p1))[:, None] - X0 * (p0 * (1 - p0))[:, None]).mean(axis=0)
        se = float(np.sqrt(g @ self.V @ g))
        return est, est - Z * se, est + Z * se, se


def verdict(ame_pp: float, lo_pp: float, same: int, defined: int) -> str:
    ok = ame_pp >= 5 and lo_pp > 0 and same >= math.ceil(2 * defined / 3)
    return "consistent association" if ok else "weak or inconsistent"
# ---------------------------------------------------------------- end of copied code


def load_year(year: int) -> pl.DataFrame:
    if year == C.TEST_YEAR and not C.test_access_time():
        raise PermissionError("2014 rows refused: no test access recorded")
    lf = pl.scan_parquet(C.M3_DEFAULT / "data/processed/features_d27.parquet")
    df = lf.filter(pl.col("year") == year).collect()
    assert set(df["year"].unique().to_list()) == {year}
    return df


def estimate(f: pl.DataFrame) -> dict:
    main = Fit(f, list(SIGNS), interactions=True)
    assert main.converged
    out = {}
    for s in SIGNS:
        mask = defined_mask(f, s)
        mu = main.ame(s, np.where(mask)[0])
        mods = main.mods[s]
        mod_est = {m: main.ame(s, np.where(mask & (main.mod == m))[0]) for m in mods}
        same = sum(1 for m in mods if math.copysign(1, mod_est[m][0]) == math.copysign(1, mu[0]))
        out[(s, "all")] = (mu, int(mask.sum()), verdict(100 * mu[0], 100 * mu[1], same, len(mods)), same, len(mods))
        for m in mods:
            out[(s, m)] = (mod_est[m], int((mask & (main.mod == m)).sum()), None, None, None)
    return out


def fmt_ci(e) -> str:
    return f"[{r(100 * e[1], 2)}, {r(100 * e[2], 2)}]"


def main() -> None:
    e13 = estimate(build_signs(load_year(2013)))
    e14 = estimate(build_signs(load_year(C.TEST_YEAR)))

    # check: the 2013 recomputation equals the Milestone 5 results at their rounding
    a13 = pd.read_csv(M5_RESULTS / "aq2_associations.csv")
    m13 = pd.read_csv(M5_RESULTS / "aq2_module_effects.csv")
    checked = 0
    for _, row in a13.iterrows():
        e = e13[(row["sign"], "all")][0]
        assert (r(100 * e[0], 2), r(100 * e[1], 2), r(100 * e[2], 2)) == \
               (row.rd_adj_mutual_pp, row.rd_adj_mutual_ci_low, row.rd_adj_mutual_ci_high), row["sign"]
        checked += 1
    for _, row in m13.iterrows():
        e = e13[(row["sign"], row["module"])][0]
        assert (r(100 * e[0], 2), r(100 * e[1], 2), r(100 * e[2], 2)) == \
               (row.rd_adj_mutual_pp, row.rd_adj_mutual_ci_low, row.rd_adj_mutual_ci_high), (row["sign"], row["module"])
        checked += 1
    print(f"2013 recomputation equals the Milestone 5 results in {checked} of {len(a13) + len(m13)} estimates")

    rows, detail = [], []
    keys = sorted(set(e13) | set(e14), key=lambda k: (list(SIGNS).index(k[0]), k[1] != "all", k[1]))
    for s, m in keys:
        a, b = e13.get((s, m)), e14.get((s, m))
        rows.append({"sign": s, "module": m,
                     "estimate_2013": r(100 * a[0][0], 2) if a else None, "ci_2013": fmt_ci(a[0]) if a else None,
                     "estimate_2014": r(100 * b[0][0], 2) if b else None, "ci_2014": fmt_ci(b[0]) if b else None})
        holds = None
        if a and b:
            holds = "same direction, interval excludes 0" if (np.sign(a[0][0]) == np.sign(b[0][0]) and
                                                              (b[0][1] > 0 or b[0][2] < 0)) else "not replicated"
        detail.append({"sign": s, "module": m, "n_2013": a[1] if a else None, "n_2014": b[1] if b else None,
                       "verdict_2013": a[2] if a else None, "verdict_2014": b[2] if b else None,
                       "modules_same_direction_2014": f"{b[3]}/{b[4]}" if b and b[3] is not None else None,
                       "replication": holds if holds else ("2014 only (no 2013 estimate)" if b else "2013 only")})
    pd.DataFrame(rows).to_csv(C.RESULTS / "aq2_replication.csv", index=False)
    det = pd.DataFrame(detail)
    det[["n_2013", "n_2014"]] = det[["n_2013", "n_2014"]].astype("Int64")
    det.to_csv(C.RESULTS / "aq2_replication_detail.csv", index=False)
    print(pd.DataFrame(rows).merge(pd.DataFrame(detail), on=["sign", "module"]).to_string(index=False))


if __name__ == "__main__":
    main()
