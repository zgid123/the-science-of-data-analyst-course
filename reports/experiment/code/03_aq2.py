"""AQ2 (diagnostic): which signs recorded by day 27 go with later non-completion, compared within module run?

    python code/03_aq2.py 2013     estimation year (before the AQ3 freeze)
    python code/03_aq2.py 2014     replication year (reads test outcomes: after the freeze, through the guard)

Model (Level 1 card, Table 4.2): logistic regression of non-completion on the five signs, run fixed effects,
log(1 + previous attempts), log(1 + credits) and sign × module terms, HC1 standard errors. A module gets its own
slope for a sign when it holds >= 20 enrolments with and >= 20 without the sign (inside the runs where the sign is
defined); smaller modules with at least one on each side share a pooled slope; otherwise no term. The adjusted risk
difference averages predicted risk with minus without the sign over the rows that carry one of its terms (the
support), with a delta-method 95% interval. The unadjusted difference is computed on the same rows.
"""

import sys

import _tools  # noqa: F401
import numpy as np
import pandas as pd
import statsmodels.api as sm
from holdout_guard import open_holdout
from stats_helpers import diff_proportions_ci, wilson_ci

import common as c

YEAR = int(sys.argv[1])
if YEAR == 2014:
    open_holdout(c.FREEZE, c.ACCESS, who="03_aq2.py 2014", why="AQ2 replication on the 2014 runs")

base = c.features(27)
base = base[base["year"] == YEAR].reset_index(drop=True)


def design(f: pd.DataFrame, signs: list[str], extra: list[str], interactions: bool = True):
    """Columns of the model and, per sign, the term column of each supported row."""
    cols = {}
    runs = sorted(f["run"].unique())
    for r in runs[1:]:
        cols[f"run={r}"] = (f["run"] == r).astype(float)
    cols["log_prev"] = np.log1p(f["num_of_prev_attempts"].astype(float))
    cols["log_credits"] = np.log1p(f["studied_credits"].astype(float))
    for x in extra:
        cols[x] = f[x].astype(float)
    term_of = {}
    for s in signs:
        defined = f[f"def_{s}"].to_numpy()
        val = f[s].to_numpy() * defined
        term = pd.Series("", index=f.index, dtype=object)
        if not interactions:
            if defined.any() and f.loc[defined, s].nunique() == 2:
                cols[s] = val.astype(float)
                term[defined] = s
            term_of[s] = term
            continue
        small = []
        for m, g in f[defined].groupby("code_module"):
            with_, without = int(g[s].sum()), int((1 - g[s]).sum())
            if with_ >= 20 and without >= 20:
                name = f"{s}:{m}"
                mask = defined & (f["code_module"] == m).to_numpy()
                cols[name] = np.where(mask, val, 0).astype(float)
                term[mask] = name
            elif with_ >= 1 and without >= 1:
                small.append(m)
        if small:
            name = f"{s}:pooled_small"
            mask = defined & f["code_module"].isin(small).to_numpy()
            cols[name] = np.where(mask, val, 0).astype(float)
            term[mask] = name
        term_of[s] = term
    x = sm.add_constant(pd.DataFrame(cols, index=f.index))
    return x, term_of


def fit(f: pd.DataFrame, signs: list[str], extra: list[str] = (), interactions: bool = True):
    x, term_of = design(f, signs, list(extra), interactions)
    res = sm.GLM(f["y"].to_numpy(), x, family=sm.families.Binomial()).fit(cov_type="HC1")
    return res, x, term_of


def ame(res, x: pd.DataFrame, term: pd.Series, rows: np.ndarray) -> tuple[float, float, float, int]:
    """Average of p(sign = 1) − p(sign = 0) over `rows`, delta-method 95% interval."""
    idx = np.where(rows & (term != "").to_numpy())[0]
    if len(idx) == 0:
        return (np.nan, np.nan, np.nan, 0)
    beta, cov = res.params.to_numpy(), res.cov_params().to_numpy()
    xs = x.to_numpy()[idx]
    tcol = np.array([x.columns.get_loc(t) for t in term.to_numpy()[idx]])
    x1, x0 = xs.copy(), xs.copy()
    x1[np.arange(len(idx)), tcol], x0[np.arange(len(idx)), tcol] = 1.0, 0.0
    p1, p0 = 1 / (1 + np.exp(-x1 @ beta)), 1 / (1 + np.exp(-x0 @ beta))
    d = float(np.mean(p1 - p0))
    grad = ((p1 * (1 - p1))[:, None] * x1 - (p0 * (1 - p0))[:, None] * x0).mean(axis=0)
    se = float(np.sqrt(grad @ cov @ grad))
    return (d, d - 1.96 * se, d + 1.96 * se, len(idx))


def associations(f: pd.DataFrame, label: str, extra: list[str] = ()) -> tuple[pd.DataFrame, pd.DataFrame]:
    res, x, term_of = fit(f, c.SIGNS, extra)
    main, _, main_terms = fit(f, c.SIGNS, extra, interactions=False)
    rows, mods = [], []
    for s in c.SIGNS:
        term = term_of[s]
        sup = (term != "").to_numpy()
        d, lo, hi, n = ame(res, x, term, np.ones(len(f), bool))
        g = f[sup]
        k1, n1 = int(g.loc[g[s] == 1, "y"].sum()), int((g[s] == 1).sum())
        k0, n0 = int(g.loc[g[s] == 0, "y"].sum()), int((g[s] == 0).sum())
        u, ulo, uhi = diff_proportions_ci(k1, n1, k0, n0)
        ok = main.params.get(s)
        orr = float(np.exp(ok)) if ok is not None else np.nan
        orl, orh = (np.exp(main.conf_int().loc[s]).tolist() if ok is not None else [np.nan, np.nan])
        per = []
        for m in sorted(g["code_module"].unique()):
            md, mlo, mhi, mn = ame(res, x, term, (f["code_module"] == m).to_numpy())
            kind = "own slope" if term[(f["code_module"] == m).to_numpy() & sup].iloc[0].endswith(m) else "pooled slope"
            per.append({"variant": label, "sign": s, "module": m, "slope": kind, "n": mn, "rd": md, "low": mlo, "high": mhi,
                        "rate_with": g.loc[(g["code_module"] == m) & (g[s] == 1), "y"].mean(),
                        "rate_without": g.loc[(g["code_module"] == m) & (g[s] == 0), "y"].mean(),
                        "with_sign": int(((g["code_module"] == m) & (g[s] == 1)).sum())})
        per = pd.DataFrame(per)
        positive = int((per["rd"] > 0).sum())
        excl = int(((per["low"] > 0) | (per["high"] < 0)).sum())
        consistent = positive >= np.ceil(2 / 3 * len(per))
        rows.append({"variant": label, "sign": s, "label": c.SIGN_LABEL[s], "n_support": n, "with_sign": n1,
                     "share_with": n1 / n if n else np.nan, "rate_with": k1 / n1 if n1 else np.nan,
                     "rate_without": k0 / n0 if n0 else np.nan, "unadj_rd": u, "unadj_low": ulo, "unadj_high": uhi,
                     "adj_rd": d, "adj_low": lo, "adj_high": hi, "odds_ratio": orr, "or_low": orl, "or_high": orh,
                     "modules": len(per), "modules_positive": positive, "modules_ci_excludes_0": excl,
                     "meets_criterion": bool(d >= 0.05 and lo > 0 and consistent)})
        mods.append(per)
    return pd.DataFrame(rows), pd.concat(mods, ignore_index=True)


f = c.add_signs(base)
main, modules = associations(f, "primary")
c.write(main, f"aq2_associations_{YEAR}.csv")
c.write(modules, f"aq2_modules_{YEAR}.csv")
print(main[["sign", "n_support", "unadj_rd", "adj_rd", "adj_low", "adj_high", "modules", "modules_positive",
            "meets_criterion"]].round(3).to_string(index=False))

# ---- sensitivity: low-activity cut at the run median and a quarter of it; clicks as a continuous adjustment
f["log_clicks"] = np.log1p(f["clicks_0c"].astype(float))
sens = [main.assign(variant="primary")]
for label, cut, extra in [("low cut = run median", 1.0, []), ("low cut = quarter of median", 0.25, []),
                          ("+ log clicks (continuous)", 0.5, ["log_clicks"]),
                          ("+ log clicks, low cut = run median", 1.0, ["log_clicks"])]:
    g = c.add_signs(base, low_cut=cut)
    g["log_clicks"] = np.log1p(g["clicks_0c"].astype(float))
    sens.append(associations(g, label, extra)[0])
sens = pd.concat(sens, ignore_index=True)
c.write(sens, f"aq2_sensitivity_{YEAR}.csv")

# ---- how the signs stack and overlap (runs where all five are defined)
full = f[f["def_missed_task"] & f["def_late_tma"]].copy()
full["n_signs"] = full[c.SIGNS].sum(axis=1)
stack = []
for k, g in full.groupby("n_signs"):
    p, lo, hi = wilson_ci(int(g["y"].sum()), len(g))
    stack.append({"n_signs": int(k), "enrolments": len(g), "share": len(g) / len(full), "non_completers": int(g["y"].sum()),
                  "rate": p, "low": lo, "high": hi})
c.write(pd.DataFrame(stack), f"aq2_sign_count_{YEAR}.csv")
corr = full[c.SIGNS].corr().reset_index().rename(columns={"index": "sign"})
c.write(corr, f"aq2_sign_correlation_{YEAR}.csv")

# ---- fit check: observed − predicted by five activity levels (no click; < half median; half to median; median to
# twice; twice or more) and by tenths of predicted risk; band = 2 standard errors
res, x, _ = fit(f, c.SIGNS)
f["p"] = res.predict(x)
r = f["activity_ratio_run"]
f["activity_level"] = np.select([f["clicks_0c"] == 0, r < 0.5, r < 1.0, r < 2.0], ["1 no click", "2 below half median",
                                "3 half to median", "4 median to twice"], "5 twice median or more")
f["risk_tenth"] = pd.qcut(f["p"], 10, labels=False) + 1
fitc = []
for by in ["activity_level", "risk_tenth"]:
    for lev, g in f.groupby(by):
        se = np.sqrt((g["p"] * (1 - g["p"])).sum()) / len(g)
        fitc.append({"by": by, "level": str(lev), "n": len(g), "observed": g["y"].mean(), "predicted": g["p"].mean(),
                     "residual": g["y"].mean() - g["p"].mean(), "band": 2 * se,
                     "outside_band": bool(abs(g["y"].mean() - g["p"].mean()) > 2 * se)})
c.write(pd.DataFrame(fitc), f"aq2_fit_check_{YEAR}.csv")

# ---- subgroups (described, not adjusted away): main-effects model within each group
sub = []
for col, levels in [("gender", ["F", "M"]), ("disability", ["Y", "N"]), ("imd_band", ["0-10%", "90-100%"])]:
    for lev in levels:
        g = f[f[col] == lev].reset_index(drop=True)
        res_g, x_g, term_g = fit(g, c.SIGNS, interactions=False)
        for s in c.SIGNS:
            d, lo, hi, n = ame(res_g, x_g, term_g[s], np.ones(len(g), bool))
            sub.append({"group": f"{col}={lev}", "sign": s, "n": n, "adj_rd": d, "low": lo, "high": hi})
c.write(pd.DataFrame(sub), f"aq2_subgroups_{YEAR}.csv")
