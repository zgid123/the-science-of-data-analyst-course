"""Shared helpers for the Milestone 4 Level 2 prototype (team N04).

Everything here is deterministic. It covers four jobs:

1. loading the Milestone 3 prepared dataset (OULAD-N04-prepared-1.0) after a hash check;
2. a guard that keeps the 2014 (test) outcomes closed until the AQ3 model is frozen;
3. the list metrics of the Level 1 report (Appendix II) and their uncertainty;
4. small utilities: Markdown tables, run labels, tie-breaking.

Paths are relative to this file, so the folder runs on any machine that holds the repository.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import itertools
import json
import math
import os
import sys
from pathlib import Path

import numpy as np
import polars as pl

CODE_ROOT = Path(__file__).resolve().parents[1]          # reports/code
REPO = CODE_ROOT.parents[1]                              # repository root
PREPARED = Path(os.environ.get("OULAD_PREPARED_DIR", REPO / "reports" / "milestone-3" / "package" / "data"))
RAW = Path(os.environ.get("OULAD_RAW_DIR", REPO / "datasets" / "oulad"))
SKILL_SCRIPTS = REPO / ".agents" / "skills" / "data-analyst" / "scripts"
if str(SKILL_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SKILL_SCRIPTS))

PREPARED_VERSION = "OULAD-N04-prepared-1.0"
SEED = 20261112                      # one seed for every random step of the prototype
KEYS = ["code_module", "code_presentation", "id_student"]
OUTCOME_COLS = ["final_result", "non_completion", "eval_withdrawal_day_unknown"]
AUDIT_COLS = ["gender", "age_band", "disability", "imd_band", "region"]
FREEZE_FILE = CODE_ROOT / "aq-3" / "results" / "freeze.json"
TEST_ACCESS_LOG = CODE_ROOT / "aq-3" / "logs" / "test-access.md"

MAIN_CUTOFF = 27                     # main operating point of the Level 1 report (Section 4.1)
MAIN_PER20 = 5
B_BOOT = 2000                        # bootstrap replicates for the S1 gate
EDUCATION_ORDER = [
    "No Formal quals",
    "Lower Than A Level",
    "A Level or Equivalent",
    "HE Qualification",
    "Post Graduate Qualification",
]


# --------------------------------------------------------------------------------------
# time, hashing, input checks
# --------------------------------------------------------------------------------------
def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prepared(files: list[str]) -> dict[str, str]:
    """Compare the SHA-256 of each prepared file with the Milestone 3 manifest; stop on a mismatch."""
    manifest = json.loads((PREPARED / "metadata" / "version_manifest.json").read_text())
    if manifest["prepared_dataset_version"] != PREPARED_VERSION:
        raise SystemExit(f"prepared version is {manifest['prepared_dataset_version']}, expected {PREPARED_VERSION}")
    out = {}
    for name in files:
        got = sha256(PREPARED / "processed" / name)
        want = manifest["outputs"][name]["sha256"]
        if got != want:
            raise SystemExit(f"HASH MISMATCH for {name}: {got} != {want}")
        out[name] = got
    return out


# --------------------------------------------------------------------------------------
# test-outcome guard
# --------------------------------------------------------------------------------------
def freeze_exists() -> bool:
    return FREEZE_FILE.exists()


def open_test_outcomes(script: str, purpose: str) -> None:
    """Allow a script to read 2014 outcomes only after the second freeze, and record the access."""
    if not freeze_exists():
        raise SystemExit(
            "2014 outcomes are closed: aq-3/results/freeze.json does not exist yet. "
            "Run the AQ3 development and freeze steps first (Level 1 report, Appendix III, steps 2-5)."
        )
    TEST_ACCESS_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not TEST_ACCESS_LOG.exists():
        TEST_ACCESS_LOG.write_text(
            "# Test-access record (2014 outcomes)\n\n"
            "Every read of a 2014 outcome by a script of this prototype is appended here. "
            "The first row is the first test access; the freeze it follows is `aq-3/results/freeze.json`.\n\n"
            "| UTC time | Script | Purpose | Freeze time (UTC) |\n| :---- | :---- | :---- | :---- |\n"
        )
    frozen = json.loads(FREEZE_FILE.read_text())["frozen_utc"]
    with open(TEST_ACCESS_LOG, "a") as fh:
        fh.write(f"| {utc_now()} | `{script}` | {purpose} | {frozen} |\n")


# --------------------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------------------
def with_run(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns((pl.col("code_module") + "-" + pl.col("code_presentation")).alias("run"))


def add_tiebreak(df: pl.DataFrame) -> pl.DataFrame:
    """A fixed pseudo-random number per enrolment, used only to break exact score ties at the list edge.

    It is drawn once from the seed in key order, so it never depends on the outcome or on the order of rows.
    """
    order = df.select(KEYS).sort(KEYS)
    u = np.random.default_rng(SEED).random(order.height)
    return df.join(order.with_columns(pl.Series("tiebreak_u", u)), on=KEYS, how="left")


def load_features(cutoff: int, part: str, script: str = "", purpose: str = "") -> pl.DataFrame:
    """Feature view of one cut-off.

    part = "train"       2013 rows with outcomes (development);
           "test_blind"  2014 rows with the outcome columns removed (allowed before the freeze);
           "test"        2014 rows with outcomes (after the freeze only; the access is recorded);
           "all"         every row with outcomes (after the freeze only; the access is recorded).
    """
    name = f"features_d{cutoff}.parquet"
    verify_prepared([name])
    df = add_tiebreak(with_run(pl.read_parquet(PREPARED / "processed" / name)))
    if part == "train":
        return df.filter(pl.col("split") == "train")
    if part == "test_blind":
        return df.filter(pl.col("split") == "test").drop(OUTCOME_COLS)
    if part in ("test", "all"):
        open_test_outcomes(script, purpose)
        return df if part == "all" else df.filter(pl.col("split") == "test")
    raise ValueError(part)


def load_view(name: str, years: tuple[int, ...], script: str = "", purpose: str = "") -> pl.DataFrame:
    """enrolment / assessment_due / student_week / capacity_by_run, restricted to run years."""
    fname = f"{name}.parquet"
    verify_prepared([fname])
    df = with_run(pl.read_parquet(PREPARED / "processed" / fname))
    if name == "capacity_by_run":
        return df
    if 2014 in years:
        open_test_outcomes(script, purpose)
    return df.filter(pl.col("code_presentation").str.slice(0, 4).cast(pl.Int64).is_in(list(years)))


# --------------------------------------------------------------------------------------
# list metrics (Level 1 report, Appendix II, Table A.4)
# --------------------------------------------------------------------------------------
def list_len(n: int, per20: int) -> int:
    """Capacity: per20 contacts per tutor group of 20 -> per20 x ceil(n / 20), never above n."""
    return min(n, per20 * math.ceil(n / 20))


def rank_desc(score: np.ndarray, tie: np.ndarray) -> np.ndarray:
    """Rank 0 = first on the list: higher score first, exact ties by the fixed tie-break number."""
    order = np.lexsort((tie, -np.asarray(score, float)))
    rank = np.empty(len(order), dtype=np.int64)
    rank[order] = np.arange(len(order))
    return rank


def run_metrics(rank: np.ndarray, y: np.ndarray, k: int) -> dict:
    y = np.asarray(y, bool)
    n, pos = len(y), int(y.sum())
    tp = int(y[rank < k].sum())
    max_att = min(k, pos)
    base = pos / n
    return {
        "n": n,
        "non_completers": pos,
        "list_length": k,
        "non_completers_on_list": tp,
        "max_attainable": max_att,
        "base_rate": base,
        "recall": tp / pos if pos else float("nan"),
        "attainable_recall": max_att / pos if pos else float("nan"),
        "normalised_recall": tp / max_att if max_att else float("nan"),
        "precision": tp / k,
        "lift": (tp / k) / base if base else float("nan"),
        "random_expected_tp": k * base,
        "random_expected_nr": (k * base) / max_att if max_att else float("nan"),
    }


def pooled_nr(tp: np.ndarray, max_att: np.ndarray) -> float:
    return float(np.sum(tp) / np.sum(max_att))


def expected_tp_with_ties(score: np.ndarray, y: np.ndarray, k: int) -> float:
    """Expected non-completers on a list of k when exact score ties at the edge are broken at random."""
    score = np.asarray(score, float)
    y = np.asarray(y, float)
    order = np.argsort(-score, kind="stable")
    s, yy = score[order], y[order]
    edge = s[k - 1]
    above = s > edge
    tied = s == edge
    slots = k - int(above.sum())
    return float(yy[above].sum() + slots * yy[tied].mean())


# --------------------------------------------------------------------------------------
# uncertainty: paired two-level bootstrap and exact sign-flip test
# --------------------------------------------------------------------------------------
def bootstrap_indices(run_sizes: list[int], B: int, seed: int, resample_runs: bool = True):
    """Yield, for each replicate, a list of (run position, row indices): runs first, then enrolments."""
    rng = np.random.default_rng(seed)
    R = len(run_sizes)
    for _ in range(B):
        chosen = rng.integers(0, R, R) if resample_runs else np.arange(R)
        yield [(int(r), rng.integers(0, run_sizes[r], run_sizes[r])) for r in chosen]


def paired_bootstrap_nr(runs: list[dict], per20: int, B: int = B_BOOT, seed: int = SEED) -> dict:
    """Pooled normalised recall of two rankings on the same resamples.

    runs: one dict per run with arrays y (bool), rank_a, rank_b (0 = first).
    Each resampled run forms its list again as its k first-ranked resampled enrolments.
    """
    sizes = [len(r["y"]) for r in runs]
    ks = [list_len(n, per20) for n in sizes]
    a, b = np.empty(B), np.empty(B)
    for i, rep in enumerate(bootstrap_indices(sizes, B, seed)):
        tpa = tpb = mx = 0
        for r, idx in rep:
            y = runs[r]["y"][idx]
            k = ks[r]
            tpa += y[np.argsort(runs[r]["rank_a"][idx], kind="stable")[:k]].sum()
            tpb += y[np.argsort(runs[r]["rank_b"][idx], kind="stable")[:k]].sum()
            mx += min(k, int(y.sum()))
        a[i], b[i] = tpa / mx, tpb / mx
    d = a - b
    return {
        "boot_a": a,
        "boot_b": b,
        "diff": d,
        "ci_a": tuple(np.percentile(a, [2.5, 97.5])),
        "ci_b": tuple(np.percentile(b, [2.5, 97.5])),
        "ci_diff": tuple(np.percentile(d, [2.5, 97.5])),
        "share_diff_le_0": float(np.mean(d <= 0)),
    }


def sign_flip_p(diffs: np.ndarray) -> tuple[float, int, int]:
    """One-sided exact sign-flip test on per-run differences; statistic = their mean.

    Returns (p-value, sign assignments at least as favourable, all assignments).
    """
    diffs = np.asarray(diffs, float)
    obs = diffs.sum()
    count = total = 0
    for signs in itertools.product((1.0, -1.0), repeat=len(diffs)):
        total += 1
        if np.dot(signs, diffs) >= obs - 1e-12:
            count += 1
    return count / total, count, total


# --------------------------------------------------------------------------------------
# discrimination and calibration
# --------------------------------------------------------------------------------------
def within_run_auc(run_labels: np.ndarray, y: np.ndarray, score: np.ndarray) -> tuple[float, float]:
    """Unweighted mean over runs of ROC-AUC and PR-AUC (average precision) computed inside each run."""
    from sklearn.metrics import average_precision_score, roc_auc_score

    rocs, prs = [], []
    for r in np.unique(run_labels):
        m = run_labels == r
        rocs.append(roc_auc_score(y[m], score[m]))
        prs.append(average_precision_score(y[m], score[m]))
    return float(np.mean(rocs)), float(np.mean(prs))


def calibration(y: np.ndarray, prob: np.ndarray) -> dict:
    """Calibration-in-the-large (intercept with the log-odds as offset), slope, Brier score."""
    import statsmodels.api as sm

    p = np.clip(np.asarray(prob, float), 1e-6, 1 - 1e-6)
    lo = np.log(p / (1 - p))
    y = np.asarray(y, float)
    citl_fit = sm.GLM(y, np.ones((len(y), 1)), family=sm.families.Binomial(), offset=lo).fit()
    slope_fit = sm.GLM(y, sm.add_constant(lo), family=sm.families.Binomial()).fit()
    return {
        "citl": float(citl_fit.params[0]),
        "citl_se": float(citl_fit.bse[0]),
        "slope": float(slope_fit.params[1]),
        "slope_se": float(slope_fit.bse[1]),
        "brier": float(np.mean((p - y) ** 2)),
        "mean_predicted": float(p.mean()),
        "observed_rate": float(y.mean()),
    }


# --------------------------------------------------------------------------------------
# output helpers
# --------------------------------------------------------------------------------------
def fmt(v, digits: int = 3) -> str:
    if v is None:
        return ""
    if isinstance(v, (bool, np.bool_)):
        return "yes" if v else "no"
    if isinstance(v, (int, np.integer)):
        return f"{int(v):,}"
    if isinstance(v, (float, np.floating)):
        if math.isnan(v):
            return "–"
        return f"{v:.{digits}f}"
    return str(v)


def md_table(df: pl.DataFrame, digits: int = 3, max_rows: int | None = None) -> str:
    """A polars frame as a GitHub Markdown table (printed into the Markdown logs)."""
    rows = df.head(max_rows).rows() if max_rows else df.rows()
    head = "| " + " | ".join(df.columns) + " |"
    sep = "| " + " | ".join(":----" for _ in df.columns) + " |"
    body = ["| " + " | ".join(fmt(v, digits) for v in row) + " |" for row in rows]
    return "\n".join([head, sep, *body])


def save_csv(df: pl.DataFrame, path: Path, note: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(path, float_precision=6)
    rel = path.relative_to(CODE_ROOT)
    print(f"[saved] {rel}  ({df.height:,} rows x {df.width} columns){'  – ' + note if note else ''}")


def banner(title: str) -> None:
    print(f"\n### {title}\n")
