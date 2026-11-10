"""Gate statistics of Appendix III (S1) and Appendix IV (FR1): pooled normalised recall of two rankers,
paired two-level bootstrap, exact one-sided sign-flip test, wins/ties/losses, and the group recall gap.

A ranker is a list of lexsort keys (last key = primary), e.g. model: [id, -score]; rule: [id, activity, -signs].
"""
from __future__ import annotations

import itertools

import numpy as np

import common as C


def model_keys(df, score_col: str) -> list[np.ndarray]:
    return [df["id_student"].to_numpy(), -df[score_col].to_numpy(dtype=float)]


def rule_keys(df) -> list[np.ndarray]:
    return [df["id_student"].to_numpy(), df["activity_ratio_run"].to_numpy(dtype=float),
            -np.asarray(df["rule_signs"], dtype=float)]


def run_arrays(df, keys_a_fn, keys_b_fn) -> list[dict]:
    out = []
    for run, g in df.groupby(C.RUN, sort=True):
        out.append({"run": run, "y": g["y"].to_numpy().astype(int), "a": keys_a_fn(g), "b": keys_b_fn(g)})
    return out


def _tp(y, keys, idx, k):
    order = np.lexsort([key[idx] for key in keys])
    return int(y[idx][order[:k]].sum())


def run_counts(r: dict, per20: int, idx=None):
    n = len(r["y"])
    idx = np.arange(n) if idx is None else idx
    k = C.list_length(len(idx), per20)
    ya = r["y"][idx]
    return _tp(r["y"], r["a"], idx, k), _tp(r["y"], r["b"], idx, k), min(k, int(ya.sum()))


def sign_flip_p(d: np.ndarray) -> float:
    """Exact one-sided p: share of the 2^m sign assignments whose mean is >= the observed mean."""
    d = np.asarray(d, dtype=float)
    m = len(d)
    signs = np.array(list(itertools.product((1.0, -1.0), repeat=m)))
    stats = (signs * d).mean(axis=1)
    return float(np.mean(stats >= d.mean() - 1e-12))


def bootstrap_diff(runs: list[dict], per20: int, B: int, seed: list[int]) -> np.ndarray:
    """Paired two-level bootstrap of the pooled normalised-recall difference a - b."""
    rng = np.random.default_rng(seed)
    out = np.empty(B)
    m = len(runs)
    for b in range(B):
        ta = tb = mx = 0
        for ri in rng.integers(0, m, m):
            r = runs[ri]
            n = len(r["y"])
            idx = rng.integers(0, n, n)
            a, bb, x = run_counts(r, per20, idx)
            ta, tb, mx = ta + a, tb + bb, mx + x
        out[b] = (ta - tb) / mx if mx else np.nan
    return out


def s1_stats(runs: list[dict], per20: int, B: int = C.BOOT_B, seed=(C.BOOT_SEED, 1)) -> dict:
    counts = [run_counts(r, per20) for r in runs]
    ta, tb, mx = (np.array(x, dtype=float) for x in zip(*counts))
    nr_a, nr_b = ta.sum() / mx.sum(), tb.sum() / mx.sum()
    d = ta / mx - tb / mx
    boot = bootstrap_diff(runs, per20, B, list(seed))
    lo, hi = np.nanpercentile(boot, [2.5, 97.5])
    p = sign_flip_p(d)
    diff = nr_a - nr_b
    met = diff > 0 and lo > 0 and p < 0.05
    return {"pooled_nr_model": nr_a, "pooled_nr_rule": nr_b, "difference": diff, "boot_ci_low": float(lo),
            "boot_ci_high": float(hi), "signflip_p": p, "wins": int((d > 0).sum()), "ties": int((d == 0).sum()),
            "losses": int((d < 0).sum()), "mean_per_run_difference": float(d.mean()),
            "verdict": "S1 met" if met else "S1 not met", "_per_run": d}


# ---------------------------------------------------------------- FR1: recall gap of a group
def group_runs(df, score_col: str, group_mask: np.ndarray) -> list[dict]:
    df = df.assign(_g=group_mask)
    return [{"run": run, "y": g["y"].to_numpy().astype(int), "g": g["_g"].to_numpy().astype(bool),
             "keys": model_keys(g, score_col)} for run, g in df.groupby(C.RUN, sort=True)]


def group_counts(r: dict, per20: int, idx=None):
    n = len(r["y"])
    idx = np.arange(n) if idx is None else idx
    k = C.list_length(len(idx), per20)
    order = np.lexsort([key[idx] for key in r["keys"]])
    listed = np.zeros(len(idx), bool)
    listed[order[:k]] = True
    y, g = r["y"][idx] == 1, r["g"][idx]
    return (int((listed & y & g).sum()), int((y & g).sum()), int((listed & y & ~g).sum()), int((y & ~g).sum()))


def recall_gap(runs: list[dict], per20: int, idx_list=None) -> tuple[float, float, float]:
    tot = np.zeros(4)
    for i, r in enumerate(runs):
        tot += group_counts(r, per20, None if idx_list is None else idx_list[i])
    rg = tot[0] / tot[1] if tot[1] else np.nan
    ro = tot[2] / tot[3] if tot[3] else np.nan
    return rg, ro, rg - ro


def bootstrap_gap(runs: list[dict], per20: int, B: int, seed: list[int]) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out = np.empty(B)
    m = len(runs)
    for b in range(B):
        tot = np.zeros(4)
        for ri in rng.integers(0, m, m):
            r = runs[ri]
            n = len(r["y"])
            tot += group_counts(r, per20, rng.integers(0, n, n))
        out[b] = (tot[0] / tot[1] if tot[1] else np.nan) - (tot[2] / tot[3] if tot[3] else np.nan)
    return out


def holm_upper_bounds(boots: dict, alpha: float = 0.05) -> dict:
    """One-sided upper bounds with Holm levels: groups ordered by bootstrap p (share of diffs >= 0)."""
    p = {g: float(np.nanmean(b >= 0)) for g, b in boots.items()}
    m = len(boots)
    out = {}
    for i, g in enumerate(sorted(boots, key=lambda x: (p[x], x))):
        level = alpha / (m - i)
        out[g] = (float(np.nanquantile(boots[g], 1 - level)), level, p[g])
    return out
