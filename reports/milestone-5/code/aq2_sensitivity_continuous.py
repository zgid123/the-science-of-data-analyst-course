"""Post-hoc AQ2 sensitivity: the main AQ2 model with a continuous activity adjustment added (task T14).

Not in the Milestone 4 plan. Prompted by the binned-residual check of `aq_analysis.py` (residuals by activity level
outside the +-2 SE band in all five levels), which shows that the binary click signs do not capture the full
activity gradient. The question is whether the mutually adjusted risk differences of the five signs still clear the
5-point criterion once activity on days 0-27 enters as a continuous term, log(1 + clicks on days 0-27).

Same population as the main model: the 11,811 enrolments of the 9 module runs of 2013 registered at day 27 (task
signs on the 7 runs with a task due by day 27). Rows are read with `aq_analysis.load_view` (2013 filter pushed down to
the reader, `assert_2013`) and asserted again here.

Usage (from the repository root): venv/bin/python reports/milestone-5/code/aq2_sensitivity_continuous.py
Writes reports/milestone-5/results/2013/aq2_sensitivity_continuous.csv
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import polars as pl
import statsmodels.api as sm

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aq_analysis as A  # noqa: E402

ADJ = "log1p_clicks_0_27"


class FitAdj(A.Fit):
    """The main AQ2 model of `aq_analysis.Fit` with extra continuous adjustment columns (no module terms)."""

    def __init__(self, f: pl.DataFrame, signs: list[str], extra: list[str], interactions: bool = True):
        super().__init__(f, signs, interactions)        # design of the main model (signs, run, background)
        self.X = np.hstack([self.X] + [f[c].cast(pl.Float64).to_numpy()[:, None] for c in extra])
        self.names = self.names + extra
        self.idx = {n: i for i, n in enumerate(self.names)}
        res = sm.Logit(self.y, self.X).fit(method="newton", maxiter=100, disp=0, cov_type="HC1")
        self.converged = bool(res.mle_retvals["converged"])
        self.b, self.V, self.res = np.asarray(res.params), np.asarray(res.cov_params()), res


def module_same_direction(fit: A.Fit, f: pl.DataFrame, s: str, overall: float) -> tuple[int, int]:
    mask = A.defined_mask(f, s)
    mods = fit.mods[s]
    same = sum(1 for m in mods
               if math.copysign(1, fit.ame(s, np.where(mask & (fit.mod == m))[0])[0]) == math.copysign(1, overall))
    return same, len(mods)


def main() -> None:
    f27 = A.load_view("features_d27")
    A.assert_2013(f27, "features_d27")
    assert set(f27["code_presentation"].unique().to_list()) == {"2013B", "2013J"}
    f = A.build_signs(f27).with_columns(pl.col("clicks_0c").cast(pl.Float64).log1p().alias(ADJ))
    assert f.height == 11811, f.height
    signs = list(A.SIGNS)

    main_fit = A.Fit(f, signs, interactions=True)
    adj_fit = FitAdj(f, signs, [ADJ], interactions=True)
    assert main_fit.converged and adj_fit.converged
    b, se = adj_fit.b[adj_fit.idx[ADJ]], math.sqrt(adj_fit.V[adj_fit.idx[ADJ], adj_fit.idx[ADJ]])
    print(f"2013 rows: {f.height}; presentations {sorted(f['code_presentation'].unique().to_list())}")
    print(f"main model: {len(main_fit.b)} parameters, pseudo-R2 {main_fit.res.prsquared:.4f}")
    print(f"with {ADJ}: {len(adj_fit.b)} parameters, pseudo-R2 {adj_fit.res.prsquared:.4f}; "
          f"coef {b:.4f} (robust SE {se:.4f}), OR per unit {math.exp(b):.3f}")

    rows = []
    for s in signs:
        idx = np.where(A.defined_mask(f, s))[0]
        for label, fit in [("main model (as reported)", main_fit), (f"main model + {ADJ}", adj_fit)]:
            est, lo, hi, _ = fit.ame(s, idx)
            same, defined = module_same_direction(fit, f, s, est)
            rows.append(dict(sign=s, model=label, n=len(idx), rd_adj_mutual_pp=A.r(100 * est, 2),
                             rd_adj_mutual_ci_low=A.r(100 * lo, 2), rd_adj_mutual_ci_high=A.r(100 * hi, 2),
                             modules_same_direction=same, modules_defined=defined,
                             verdict=A.verdict(100 * est, 100 * lo, same, defined),
                             pseudo_r2=A.r(fit.res.prsquared), n_params=len(fit.b)))
    out = pl.DataFrame(rows)
    out.write_csv(A.RES / "aq2_sensitivity_continuous.csv")
    with pl.Config(tbl_rows=-1, tbl_cols=-1, tbl_width_chars=200):
        print(out)

    # check of the refit on the same five activity levels as the binned-residual check of aq_analysis.py
    p = adj_fit.predict()
    act = (pl.when(pl.col("clicks_0c") == 0).then(pl.lit("1 no clicks days 0-27"))
           .when(pl.col("activity_ratio_run") < 0.5).then(pl.lit("2 below half the run median"))
           .when(pl.col("activity_ratio_run") < 1).then(pl.lit("3 half to the run median"))
           .when(pl.col("activity_ratio_run") < 2).then(pl.lit("4 median to twice the median"))
           .otherwise(pl.lit("5 twice the run median or more")))
    g = (f.with_columns(pl.Series("p", p), act.alias("level")).group_by("level")
         .agg(pl.len().alias("n"), pl.col("y").mean().alias("obs"), pl.col("p").mean().alias("pred"),
              (pl.col("p") * (1 - pl.col("p"))).sum().alias("v")).sort("level"))
    print("binned residuals of the refit by activity level (observed - predicted, pp; band +-2 SE):")
    for x in g.iter_rows(named=True):
        band = 200 * math.sqrt(x["v"]) / x["n"]
        res = 100 * (x["obs"] - x["pred"])
        print(f"  {x['level']}: n={x['n']} residual {res:.2f} band {band:.2f} outside={abs(res) > band}")
    print("written results/2013/aq2_sensitivity_continuous.csv")


if __name__ == "__main__":
    main()
