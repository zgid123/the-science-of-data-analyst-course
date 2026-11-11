"""Shared pieces of the AQ1 scripts: scope handling and the Wilson interval on a grouped table."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import polars as pl

HERE = Path(__file__).resolve().parent
AQ = HERE.parent
sys.path.insert(0, str(AQ.parent / "common"))
import lib  # noqa: E402
from stats_helpers import wilson_ci  # noqa: E402  (data-analyst skill helper)

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
