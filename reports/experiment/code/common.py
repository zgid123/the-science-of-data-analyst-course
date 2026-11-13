"""Shared definitions for AQ1–AQ4: inputs, populations, signs, model pipelines and list metrics.

Every rule here comes from the Milestone 4 Level 1 design (populations, signs, predictor sets, capacities,
baselines, preprocessing, tuning grids and success criteria). Nothing is chosen from test outcomes.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path

import _tools  # noqa: F401  (puts ../tools on the import path)
import numpy as np
import pandas as pd
import polars as pl
from data_manifest import checked

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data-manifest.json"
PREPARED = Path(os.environ.get("OULAD_PREPARED_DIR", ROOT.parent / "milestone-3" / "package" / "data"))
RESULTS, FIGURES, MODELS, SCORES = ROOT / "results", ROOT / "figures", ROOT / "models", ROOT / "scores"
FREEZE, ACCESS = RESULTS / "freeze.json", ROOT / "logs" / "holdout-access.md"
SEED = 20261112

KEY = ["code_module", "code_presentation", "id_student"]
RUN = ["code_module", "code_presentation"]


# ---------------------------------------------------------------- inputs
def _parquet(name: str) -> pd.DataFrame:
    path = checked(PREPARED / "processed" / name, MANIFEST)
    frame = pl.read_parquet(path)
    return pd.DataFrame(frame.to_dict(as_series=False))      # pyarrow-free conversion


def raw_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(checked(PREPARED / "raw" / name, MANIFEST), na_values=["?", ""], keep_default_na=True)


def predictor_sets() -> dict:
    return json.loads(checked(PREPARED / "metadata" / "predictor_sets.json", MANIFEST).read_text())


def enrolment() -> pd.DataFrame:
    e = _parquet("enrolment.parquet")
    e["run"] = e["code_module"] + "-" + e["code_presentation"]
    return e


def features(cutoff: int) -> pd.DataFrame:
    """Enrolments registered at the cut-off (day 13 or 27) with pre-cut-off features, signs and a fixed tie-breaker."""
    f = _parquet(f"features_d{cutoff}.parquet").sort_values(KEY).reset_index(drop=True)
    f["run"] = f["code_module"] + "-" + f["code_presentation"]
    f["y"] = f["non_completion"].astype(int)
    f["tiebreak_u"] = np.random.default_rng(SEED).random(len(f))   # outcome-independent, drawn in key order
    return f


def assessment_due() -> pd.DataFrame:
    return _parquet("assessment_due.parquet")


def capacity() -> pd.DataFrame:
    return _parquet("capacity_by_run.parquet")


def write(frame: pd.DataFrame, name: str) -> Path:
    RESULTS.mkdir(exist_ok=True)
    path = RESULTS / name
    frame.to_csv(path, index=False)
    print(f"wrote {path.relative_to(ROOT)} ({len(frame)} rows)")
    return path


# ---------------------------------------------------------------- AQ2 signs (day 27)
SIGNS = ["missed_task", "late_tma", "inactive_7d", "low_activity", "no_prestart"]
SIGN_LABEL = {"missed_task": "Missed a task due", "late_tma": "Submitted a TMA late",
              "inactive_7d": "No activity in the last 7 days", "low_activity": "Clicks below half the run median",
              "no_prestart": "No activity before the start"}


def runs_with_tasks(cutoff: int = 27) -> pd.DataFrame:
    """Per run: any TMA or CMA due by the cut-off (missed-task sign defined) and any TMA due (late-TMA sign defined)."""
    a = assessment_due()
    a = a[a["due_day"] <= cutoff]
    out = a.groupby(RUN).agg(any_task=("id_assessment", "size"),
                             any_tma=("assessment_type", lambda s: (s == "TMA").any())).reset_index()
    out["any_task"] = out["any_task"] > 0
    return out


def add_signs(f: pd.DataFrame, low_cut: float = 0.5) -> pd.DataFrame:
    """The five binary signs of AQ2 and where each is defined (run level, from the calendar, not from outcomes)."""
    f = f.copy()
    tasks = runs_with_tasks()
    f = f.merge(tasks, on=RUN, how="left")
    f["any_task"] = f["any_task"].fillna(False).astype(bool)
    f["any_tma"] = f["any_tma"].fillna(False).astype(bool)
    f["missed_task"] = (f["tasks_missed_c"] >= 1).astype(int)
    f["late_tma"] = (f["tma_late_c"] >= 1).astype(int)
    f["inactive_7d"] = f["inactive_last7"].astype(int)
    f["low_activity"] = (f["activity_ratio_run"] < low_cut).astype(int)
    f["no_prestart"] = (f["clicks_pre"] == 0).astype(int)
    f["def_missed_task"], f["def_late_tma"] = f["any_task"], f["any_tma"]
    for s in ["inactive_7d", "low_activity", "no_prestart"]:
        f[f"def_{s}"] = True
    return f


# ---------------------------------------------------------------- capacity and lists
def list_size(n: int, per20: int) -> int:
    return min(n, per20 * math.ceil(n / 20))


def rank_in_run(frame: pd.DataFrame, score: str) -> pd.Series:
    """Rank 1 = highest score within the run; exact ties broken by the fixed tie-breaker."""
    order = frame.sort_values(["run", score, "tiebreak_u"], ascending=[True, False, True])
    ranks = order.groupby("run").cumcount() + 1
    return ranks.reindex(frame.index)


def rule_score(frame: pd.DataFrame) -> np.ndarray:
    """Rule-ranked list (C10): number of signs (task missed, TMA late, inactive 7 days), ties by lower activity."""
    n = (frame["rule_missed"].astype(int) + frame["rule_tma_late"].astype(int) + frame["inactive_last7"].astype(int))
    # activity_ratio_run is > 0; a lower ratio ranks higher inside the same sign count
    return n.to_numpy() + 1.0 / (1.0 + frame["activity_ratio_run"].to_numpy())


def list_metrics(frame: pd.DataFrame, score: str, per20: int = 5) -> pd.DataFrame:
    """Per run: n, k, non-completers, listed non-completers (tp), attainable maximum, recall, normalised recall."""
    ranks = rank_in_run(frame, score)
    rows = []
    for run, g in frame.groupby("run", sort=True):
        n, pos = len(g), int(g["y"].sum())
        k = list_size(n, per20)
        tp = int(g["y"][ranks[g.index] <= k].sum())
        best = min(k, pos)
        rows.append({"run": run, "n": n, "k": k, "positives": pos, "tp": tp, "attainable": best,
                     "recall": tp / pos if pos else np.nan, "precision": tp / k, "base_rate": pos / n,
                     "lift": (tp / k) / (pos / n) if pos else np.nan, "norm_recall": tp / best if best else np.nan})
    return pd.DataFrame(rows)


def pooled(m: pd.DataFrame) -> dict:
    tp, best, pos, k, n = m["tp"].sum(), m["attainable"].sum(), m["positives"].sum(), m["k"].sum(), m["n"].sum()
    return {"n": int(n), "k": int(k), "positives": int(pos), "tp": tp, "attainable": int(best),
            "norm_recall": tp / best, "recall": tp / pos, "precision": tp / k, "lift": (tp / k) / (pos / n)}


# ---------------------------------------------------------------- calibration
def calibration(y: np.ndarray, p: np.ndarray) -> dict:
    """Calibration-in-the-large (intercept with the slope fixed at 1) and calibration slope, by logistic fits."""
    import statsmodels.api as sm
    p = np.clip(p, 1e-6, 1 - 1e-6)
    lp = np.log(p / (1 - p))
    citl = sm.GLM(y, np.ones((len(y), 1)), family=sm.families.Binomial(), offset=lp).fit().params[0]
    slope = sm.GLM(y, sm.add_constant(lp), family=sm.families.Binomial()).fit().params[1]
    return {"citl": float(citl), "slope": float(slope), "mean_pred": float(p.mean()), "observed": float(y.mean()),
            "brier": float(np.mean((p - y) ** 2))}
