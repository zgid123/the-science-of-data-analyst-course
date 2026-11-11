"""Shared pieces of the AQ4 scripts. AQ4 fits nothing: it cuts the frozen AQ3 scores at the capacity."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import polars as pl

HERE = Path(__file__).resolve().parent
AQ = HERE.parent
sys.path.insert(0, str(AQ.parent / "common"))
import lib  # noqa: E402

AQ3 = AQ.parent / "aq-3"
sys.path.insert(0, str(AQ3 / "code"))
EXTRACT = AQ / "extracted-datasets"
RESULTS = AQ / "results"
FIGURES = AQ / "figures"
CHOSEN = json.loads(lib.FREEZE_FILE.read_text())["chosen_config"] if lib.freeze_exists() else None


def scored(cutoff: int) -> pl.DataFrame:
    return pl.read_csv(AQ3 / "extracted-datasets" / f"aq3_test_scored_d{cutoff}.csv")


def add_ranks(df: pl.DataFrame, col: str, name: str) -> pl.DataFrame:
    """Rank within run (1 = first), list flags at 3 and 5 per 20 and the tier (1 = top 3 per 20, 2 = next 2 per 20)."""
    rank = np.zeros(df.height, dtype=np.int64)
    k3 = np.zeros(df.height, dtype=np.int64)
    k5 = np.zeros(df.height, dtype=np.int64)
    runs = df["run"].to_numpy()
    for run in np.unique(runs):
        m = runs == run
        rank[m] = lib.rank_desc(df[col].to_numpy()[m], df["tiebreak_u"].to_numpy()[m]) + 1
        k3[m], k5[m] = lib.list_len(int(m.sum()), 3), lib.list_len(int(m.sum()), 5)
    return df.with_columns(pl.Series(f"rank_{name}", rank), pl.Series("k3", k3), pl.Series("k5", k5)).with_columns(
        (pl.col(f"rank_{name}") <= pl.col("k3")).alias(f"list3_{name}"), (pl.col(f"rank_{name}") <= pl.col("k5")).alias(f"list5_{name}"),
        pl.when(pl.col(f"rank_{name}") <= pl.col("k3")).then(1).when(pl.col(f"rank_{name}") <= pl.col("k5")).then(2).otherwise(0).alias(f"tier_{name}"))
