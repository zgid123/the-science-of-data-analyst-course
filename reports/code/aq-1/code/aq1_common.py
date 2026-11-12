"""Shared pieces of the AQ1 scripts: scope handling, the Wilson interval on a grouped table, the year comparison."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import polars as pl

HERE = Path(__file__).resolve().parent
AQ = HERE.parent
sys.path.insert(0, str(AQ.parent / "common"))
import lib  # noqa: E402
from stats_helpers import diff_proportions_ci, wilson_ci  # noqa: E402  (data-analyst skill helpers)

EXTRACT = AQ / "extracted-datasets"
RESULTS = AQ / "results"
FIGURES = AQ / "figures"


def scope_args(doc: str):
    p = argparse.ArgumentParser(description=doc)
    p.add_argument("--scope", choices=["2013", "all"], required=True,
                   help="2013 = development runs only (before the AQ3 freeze); all = 22 runs (after the freeze)")
    a = p.parse_args()
    years = (2013,) if a.scope == "2013" else (2013, 2014)
    return a.scope, years


def rate_table(df: pl.DataFrame, by: list[str], event: str = "non_completion") -> pl.DataFrame:
    """Events, denominator, rate and Wilson 95% interval per group."""
    g = (df.group_by(by).agg(pl.len().alias("enrolments"), pl.col(event).sum().alias("events")).sort(by)) if by else \
        df.select(pl.len().alias("enrolments"), pl.col(event).sum().alias("events"))
    ci = [wilson_ci(int(k), int(n)) for k, n in zip(g["events"], g["enrolments"])]
    return g.with_columns(
        pl.Series("rate", [c[0] for c in ci]),
        pl.Series("ci_low", [c[1] for c in ci]),
        pl.Series("ci_high", [c[2] for c in ci]),
    )


DENOMINATORS = {"registered at day 14 (KPI population)": pl.col("enrolled_d14"), "all enrolments": pl.lit(True)}


def _counts(df: pl.DataFrame, event: str) -> tuple[int, int]:
    return int(df[event].sum()), df.height


def year_difference(d13: pl.DataFrame, d14: pl.DataFrame, event: str = "non_completion") -> dict:
    """2014 minus 2013 difference of a rate with Newcombe's hybrid score interval (PROTOCOL.md P18)."""
    k13, n13 = _counts(d13, event)
    k14, n14 = _counts(d14, event)
    if n13 == 0 or n14 == 0:
        return {"n_2013": n13, "events_2013": k13, "rate_2013": None, "n_2014": n14, "events_2014": k14, "rate_2014": None,
                "difference_2014_minus_2013": None, "ci_low": None, "ci_high": None, "interval_excludes_0": None}
    d, lo, hi = diff_proportions_ci(k14, n14, k13, n13)
    return {"n_2013": n13, "events_2013": k13, "rate_2013": k13 / n13, "n_2014": n14, "events_2014": k14, "rate_2014": k14 / n14,
            "difference_2014_minus_2013": d, "ci_low": lo, "ci_high": hi, "interval_excludes_0": bool(lo > 0 or hi < 0)}


def paired_keys(enr: pl.DataFrame) -> pl.DataFrame:
    """Module x start-month pairs that have a run in both years."""
    g = enr.group_by("code_module", "start_month").agg(pl.col("year").n_unique().alias("years"))
    return g.filter(pl.col("years") == 2).select("code_module", "start_month").sort("code_module", "start_month")


def year_comparison(enr: pl.DataFrame, event: str = "non_completion") -> pl.DataFrame:
    """The year comparison of P18: one row per scope and denominator.

    Scopes: all runs; the modules that ran in both years; the module x start-month pairs that ran in both years
    (pooled, and Mantel-Haenszel weighted over the pairs); each shared module; each start month; each pair.
    """
    shared = sorted(set(enr.filter(pl.col("year") == 2013)["code_module"]) & set(enr.filter(pl.col("year") == 2014)["code_module"]))
    pairs = paired_keys(enr)
    in_shared = pl.col("code_module").is_in(shared)
    paired = enr.join(pairs, on=["code_module", "start_month"], how="inner")
    scopes: list[tuple[str, str, pl.DataFrame]] = [
        ("overall", f"all runs ({enr.filter(pl.col('year') == 2013)['run'].n_unique()} of 2013, {enr.filter(pl.col('year') == 2014)['run'].n_unique()} of 2014)", enr),
        ("overall", f"{len(shared)} modules run in both years", enr.filter(in_shared)),
        ("overall", f"{pairs.height} module x start-month pairs run in both years", paired),
    ]
    for m in shared:
        scopes.append(("module", m, enr.filter(pl.col("code_module") == m)))
    for sm in sorted(enr["start_month"].unique().to_list()):
        scopes.append(("start month, all modules", sm, enr.filter(pl.col("start_month") == sm)))
        scopes.append(("start month, modules run in both years", sm, enr.filter(in_shared & (pl.col("start_month") == sm))))
        scopes.append(("start month, paired runs", sm, paired.filter(pl.col("start_month") == sm)))
    for m, sm in pairs.iter_rows():
        scopes.append(("pair", f"{m}-{sm}", enr.filter((pl.col("code_module") == m) & (pl.col("start_month") == sm))))
    rows = []
    for den, cond in DENOMINATORS.items():
        for level, label, d in scopes:
            d = d.filter(cond)
            rows.append({"denominator": den, "level": level, "scope": label, "method": "pooled counts, Newcombe interval",
                         **year_difference(d.filter(pl.col("year") == 2013), d.filter(pl.col("year") == 2014), event)})
        strata = []
        for m, sm in pairs.iter_rows():
            d = enr.filter(cond & (pl.col("code_module") == m) & (pl.col("start_month") == sm))
            k13, n13 = _counts(d.filter(pl.col("year") == 2013), event)
            k14, n14 = _counts(d.filter(pl.col("year") == 2014), event)
            strata.append((k14, n14, k13, n13))
        mh = lib.mh_risk_difference(strata)
        tot = [sum(x[i] for x in strata) for i in range(4)]
        rows.append({"denominator": den, "level": "overall", "scope": f"{pairs.height} module x start-month pairs run in both years",
                     "method": "Mantel-Haenszel weighted over the pairs, Wald interval",
                     "n_2013": tot[3], "events_2013": tot[2], "rate_2013": tot[2] / tot[3], "n_2014": tot[1], "events_2014": tot[0], "rate_2014": tot[0] / tot[1],
                     "difference_2014_minus_2013": mh["rd"], "ci_low": mh["ci_low"], "ci_high": mh["ci_high"],
                     "interval_excludes_0": bool(mh["ci_low"] > 0 or mh["ci_high"] < 0)})
    return pl.DataFrame(rows)
