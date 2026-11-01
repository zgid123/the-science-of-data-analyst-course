"""Descriptive statistics helpers: intervals, effect sizes, distribution shape, concentration, survival.

Pure functions on polars Series/DataFrames; no file access.
"""

from __future__ import annotations

import math

import polars as pl


def wilson(k: int, n: int, z: float = 1.96) -> dict:
    """Proportion with its Wilson 95% interval."""
    if not n:
        return {"k": k, "n": n, "rate": None, "lo": None, "hi": None}
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return {"k": k, "n": n, "rate": round(p, 4), "lo": round(c - h, 4), "hi": round(c + h, 4)}


def cramers_v(df: pl.DataFrame, a: str, b: str) -> float | None:
    """Bias-corrected Cramer's V (Bergsma 2013) between two categorical columns."""
    t = df.drop_nulls([a, b]).group_by([a, b]).len()
    n = int(t["len"].sum())
    ra = t.group_by(a).agg(pl.col("len").sum().alias("ra"))
    cb = t.group_by(b).agg(pl.col("len").sum().alias("cb"))
    r, k = ra.height, cb.height
    if r < 2 or k < 2 or n < 2:
        return None
    full = (ra.join(cb, how="cross").join(t, on=[a, b], how="left").with_columns(pl.col("len").fill_null(0))
            .with_columns((pl.col("ra") * pl.col("cb") / n).alias("e")))
    chi2 = float(((full["len"] - full["e"]) ** 2 / full["e"]).sum())
    phi2c = max(0.0, chi2 / n - (k - 1) * (r - 1) / (n - 1))
    rc, kc = r - (r - 1) ** 2 / (n - 1), k - (k - 1) ** 2 / (n - 1)
    return round(math.sqrt(phi2c / min(kc - 1, rc - 1)), 4)


def cliffs_delta(a: pl.Series, b: pl.Series) -> float | None:
    """P(a > b) - P(a < b), from average ranks; +1 = every a above every b."""
    a, b = a.drop_nulls().cast(pl.Float64), b.drop_nulls().cast(pl.Float64)
    n1, n2 = a.len(), b.len()
    if not n1 or not n2:
        return None
    ranks = pl.concat([a, b]).rank("average")
    u = float(ranks[:n1].sum()) - n1 * (n1 + 1) / 2
    return round(2 * u / (n1 * n2) - 1, 4)


def shape(s: pl.Series) -> dict:
    """Univariate shape and outlier counts (IQR rule and robust z on the median absolute deviation)."""
    v = s.drop_nulls().cast(pl.Float64)
    q1, q3, med = v.quantile(0.25, "linear"), v.quantile(0.75, "linear"), v.median()
    iqr = q3 - q1
    mad = (v - med).abs().median()
    return {
        "n": v.len(), "mean": round(v.mean(), 3), "median": med, "q1": q1, "q3": q3,
        "skew": round(v.skew(), 3), "excess_kurtosis": round(v.kurtosis(), 3),
        "log1p_skew": round(v.log1p().skew(), 3) if v.min() >= 0 else None,
        "iqr_outliers": int(((v < q1 - 1.5 * iqr) | (v > q3 + 1.5 * iqr)).sum()),
        "robust_z_gt_3_5": int(((v - med).abs() / (1.4826 * mad) > 3.5).sum()) if mad else None,
    }


def concentration(s: pl.Series) -> dict:
    """Gini coefficient and the share held by the top 10% / top 1% of units."""
    v = s.drop_nulls().cast(pl.Float64).sort()
    n, total = v.len(), float(v.sum())
    cum = float((v * pl.Series(range(1, n + 1), dtype=pl.Float64)).sum())
    gini = (2 * cum) / (n * total) - (n + 1) / n
    desc = v.sort(descending=True)
    return {"gini": round(gini, 4), "top10_share": round(float(desc[: n // 10].sum()) / total, 4),
            "top1_share": round(float(desc[: n // 100].sum()) / total, 4)}


def kaplan_meier(time: pl.Series, event: pl.Series, grid: list[int]) -> dict[int, float]:
    """Survival S(t) at each grid day; event = withdrawal, others censored at their time."""
    t = (pl.DataFrame({"t": time, "e": event.cast(pl.Int64)}).group_by("t")
         .agg(pl.col("e").sum().alias("d"), pl.len().alias("c")).sort("t"))
    at_risk, s, gi, out = int(t["c"].sum()), 1.0, 0, {}
    for day, d, c in t.iter_rows():
        while gi < len(grid) and grid[gi] < day:
            out[grid[gi]] = round(s, 4)
            gi += 1
        if d:
            s *= 1 - d / at_risk
        at_risk -= c
    while gi < len(grid):
        out[grid[gi]] = round(s, 4)
        gi += 1
    return out
