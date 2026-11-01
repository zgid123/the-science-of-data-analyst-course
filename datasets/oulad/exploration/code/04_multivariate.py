"""Stage 4 - multivariate: how the student characteristics relate to one another, whether the outcome gradients
survive stratification (confounding check) and differ by module or year (interactions), the principal components
of the start-of-presentation measures, and clusters of weekly engagement trajectories.

Run from the repository root, after 02_features.py: venv/bin/python datasets/oulad/exploration/code/04_multivariate.py
Reads results/enrolment_features.csv and studentVle.csv; writes results/multivariate.json and
results/trajectory_clusters.csv (one row per enrolment with its cluster).
"""

from __future__ import annotations

import numpy as np
import polars as pl

from common import ENROLMENT, OUTCOMES, RESULTS, load, write_json
from stats import cliffs_delta, cramers_v, wilson

DIMENSIONS = ["code_module", "year", "semester", "gender", "region", "highest_education", "imd_band", "age_band",
              "disability", "prev_attempts"]
MIN_CELL = 30
WEEKS = 38  # weeks 0-37 (days 0-265), covered by every presentation
K_RANGE = range(2, 7)
SEED = 0
# start-of-presentation measures for PCA: known by day 27, none recorded after the outcome
PCA_MEASURES = ["num_of_prev_attempts", "studied_credits", "date_registration", "clicks_prestart", "clicks_early",
                "active_days_early", "imd_ord", "age_ord", "edu_ord", "first_submitted"]


def read_features() -> pl.DataFrame:
    return pl.read_csv(RESULTS / "enrolment_features.csv", infer_schema_length=None,
                       schema_overrides={c: pl.String for c in ("year", "semester", "prev_attempts", "imd_band")})


def dimension_associations(f: pl.DataFrame) -> dict:
    """Bias-corrected Cramer's V between every pair of student and course dimensions."""
    pairs = []
    for i, a in enumerate(DIMENSIONS):
        for b in DIMENSIONS[i + 1:]:
            pairs.append({"a": a, "b": b, "cramers_v": cramers_v(f, a, b)})
    return {"pairs": sorted(pairs, key=lambda p: -(p["cramers_v"] or 0)),
            "pairs_v_at_least_0_1": sum(1 for p in pairs if (p["cramers_v"] or 0) >= 0.1)}


def gap(d: pl.DataFrame, col: str, g1: list[str], g2: list[str], metric: str = "success") -> dict | None:
    a, b = d.filter(pl.col(col).is_in(g1)), d.filter(pl.col(col).is_in(g2))
    if a.height < MIN_CELL or b.height < MIN_CELL:
        return None
    return {"gap_pp": round((float(a[metric].mean()) - float(b[metric].mean())) * 100, 2), "n1": a.height, "n2": b.height}


DEPRIVED, AFFLUENT = ["0-10%", "10-20%"], ["80-90%", "90-100%"]


def stratified_gradients(f: pl.DataFrame) -> dict:
    """Confounding check: the deprivation and disability success gaps within strata of early engagement
    (tertiles of days 0-27 clicks, students registered on day 28) and of prior education."""
    p = f.filter(pl.col("active_at_28"))
    q1, q2 = p["clicks_early"].quantile(1 / 3, "nearest"), p["clicks_early"].quantile(2 / 3, "nearest")
    p = p.with_columns(pl.when(pl.col("clicks_early") <= q1).then(pl.lit("low"))
                       .when(pl.col("clicks_early") <= q2).then(pl.lit("middle")).otherwise(pl.lit("high")).alias("tertile"))
    out = {"engagement_tertile_cuts": [q1, q2]}
    for name, (col, g1, g2) in {"most_vs_least_deprived": ("imd_band", DEPRIVED, AFFLUENT),
                                "disability_yes_vs_no": ("disability", ["Y"], ["N"])}.items():
        strata = {t: gap(p.filter(pl.col("tertile") == t), col, g1, g2) for t in ("low", "middle", "high")}
        edu = {e: gap(f.filter(pl.col("highest_education") == e), col, g1, g2)
               for e in f["highest_education"].unique().sort()}
        w = [(v["n1"] + v["n2"], v["gap_pp"]) for v in strata.values() if v]
        out[name] = {"crude_gap_pp_active_at_28": gap(p, col, g1, g2)["gap_pp"],
                     "within_engagement_tertile": strata,
                     "engagement_standardised_gap_pp": round(sum(n * g for n, g in w) / sum(n for n, _ in w), 2),
                     "within_education": {k: v for k, v in edu.items() if v}}
    return out


def interactions(f: pl.DataFrame) -> dict:
    """Whether the main gradients differ by module and by year."""
    p = f.filter(pl.col("active_at_28"))
    out = {}
    for by in ("code_module", "year", "semester"):
        rows = []
        for v in f[by].unique().sort():
            d, dp = f.filter(pl.col(by) == v), p.filter(pl.col(by) == v)
            rows.append({by: v, "n": d.height,
                         "deprivation_gap_pp": (gap(d, "imd_band", DEPRIVED, AFFLUENT) or {}).get("gap_pp"),
                         "disability_gap_pp": (gap(d, "disability", ["Y"], ["N"]) or {}).get("gap_pp"),
                         "early_clicks_cliffs_delta": cliffs_delta(dp.filter(pl.col("success"))["clicks_early"],
                                                                   dp.filter(~pl.col("success"))["clicks_early"])})
        out[by] = rows
    return out


def pca(f: pl.DataFrame) -> dict:
    """PCA on rank-transformed, standardised start-of-presentation measures (missing values at the median rank)."""
    cols = []
    for c in PCA_MEASURES:
        s = f[c].cast(pl.Float64)
        r = s.rank("average").fill_null(s.rank("average").median())
        cols.append(((r - r.mean()) / r.std()).to_numpy())
    x = np.column_stack(cols)
    _, sv, vt = np.linalg.svd(x - x.mean(axis=0), full_matrices=False)
    var = sv ** 2 / (sv ** 2).sum()
    scores = x @ vt.T
    succ = f["success"].to_numpy()
    comps = []
    for i in range(4):
        sign = 1 if vt[i][np.abs(vt[i]).argmax()] > 0 else -1  # orient so the largest loading is positive
        load_i = vt[i] * sign
        comps.append({"component": i + 1, "explained_variance": round(float(var[i]), 4),
                      "loadings": {c: round(float(v), 3) for c, v in sorted(zip(PCA_MEASURES, load_i), key=lambda t: -abs(t[1]))},
                      "cliffs_delta_success_vs_not": cliffs_delta(pl.Series(scores[succ, i] * sign), pl.Series(scores[~succ, i] * sign))})
    return {"measures": PCA_MEASURES, "n": x.shape[0], "explained_variance_all": [round(float(v), 4) for v in var],
            "components": comps}


def weekly_matrix(f: pl.DataFrame) -> np.ndarray:
    log = (load("studentVle")[1].filter(pl.col("date").is_between(0, WEEKS * 7 - 1))
           .with_columns((pl.col("date") // 7).cast(pl.Int32).alias("week"))
           .group_by(ENROLMENT + ["week"]).agg(pl.col("sum_click").sum().alias("c")))
    keys = f.select(ENROLMENT).with_row_index("row")
    cells = log.join(keys, on=ENROLMENT)
    m = np.zeros((f.height, WEEKS))
    m[cells["row"].to_numpy(), cells["week"].to_numpy()] = cells["c"].to_numpy()
    return np.log1p(m)


def kmeans(x: np.ndarray, k: int, rng: np.random.Generator, n_init: int = 4, iters: int = 100):
    best = None
    for _ in range(n_init):
        centres = [x[rng.integers(len(x))]]  # k-means++ initialisation
        for _ in range(k - 1):
            d2 = np.min(((x[:, None, :] - np.array(centres)[None]) ** 2).sum(-1), axis=1)
            centres.append(x[rng.choice(len(x), p=d2 / d2.sum())])
        c = np.array(centres)
        for _ in range(iters):
            lab = ((x[:, None, :] - c[None]) ** 2).sum(-1).argmin(1)
            new = np.array([x[lab == j].mean(0) if (lab == j).any() else c[j] for j in range(k)])
            if np.allclose(new, c):
                break
            c = new
        inertia = float(((x - c[lab]) ** 2).sum())
        if best is None or inertia < best[2]:
            best = (lab, c, inertia)
    return best


def silhouette(x: np.ndarray, lab: np.ndarray, rng: np.random.Generator, n: int = 3000) -> float:
    idx = rng.choice(len(x), size=min(n, len(x)), replace=False)
    xs, ls = x[idx], lab[idx]
    d = np.sqrt(((xs[:, None, :] - xs[None]) ** 2).sum(-1))
    s = []
    for i in range(len(xs)):
        same = ls == ls[i]
        if same.sum() < 2:
            continue
        a = d[i, same].sum() / (same.sum() - 1)
        b = min(d[i, ls == j].mean() for j in np.unique(ls) if j != ls[i])
        s.append((b - a) / max(a, b))
    return float(np.mean(s))


def trajectories(f: pl.DataFrame) -> tuple[dict, pl.DataFrame]:
    """K-means clusters of log weekly clicks, weeks 0-37. k = highest silhouette among 3-6, chosen before
    looking at the clusters (k = 2 only separates active from inactive)."""
    x = weekly_matrix(f)
    rng = np.random.default_rng(SEED)
    fits = {}
    for k in K_RANGE:
        lab, c, inertia = kmeans(x, k, rng)
        fits[k] = {"labels": lab, "centres": c, "inertia": round(inertia, 1),
                   "silhouette": round(silhouette(x, lab, np.random.default_rng(SEED)), 4)}
    k = max((k for k in K_RANGE if k >= 3), key=lambda k: fits[k]["silhouette"])
    lab, c = fits[k]["labels"], fits[k]["centres"]
    order = np.argsort(c.sum(1))  # cluster 1 = least active overall
    relabel = {old: new + 1 for new, old in enumerate(order)}
    lab = np.vectorize(relabel.get)(lab)
    fc = f.select(ENROLMENT + ["final_result", "success"]).with_columns(pl.Series("cluster", lab))
    clusters = []
    for j in range(1, k + 1):
        g = fc.filter(pl.col("cluster") == j)
        centre = c[order[j - 1]]
        clusters.append({"cluster": j, "n": g.height, "share": round(g.height / fc.height, 4),
                         "centre_weekly_clicks": [round(float(np.expm1(v)), 2) for v in centre],
                         "outcomes": {o: int((g["final_result"] == o).sum()) for o in OUTCOMES},
                         "success": wilson(int(g["success"].sum()), g.height),
                         "module_share": {m: round(float((g["code_module"] == m).mean()), 3)
                                          for m in sorted(fc["code_module"].unique())}})
    res = {"k_selected": k, "selection": "highest silhouette (sample of 3,000, seed 0) among k = 3-6",
           "by_k": {kk: {"inertia": v["inertia"], "silhouette": v["silhouette"]} for kk, v in fits.items()},
           "clusters": clusters,
           "cramers_v_cluster_vs_outcome": cramers_v(fc.with_columns(pl.col("cluster").cast(pl.String)), "cluster", "final_result"),
           "note": "centre_weekly_clicks = expm1 of the mean log1p weekly clicks (a geometric-type mean, a typical enrolment of the cluster); trajectories cover the whole presentation, so clusters partly record withdrawal itself"}
    return res, fc.select(ENROLMENT + ["cluster"])


def main() -> None:
    f = read_features()
    traj, assign = trajectories(f)
    assign.write_csv(RESULTS / "trajectory_clusters.csv")
    res = {"dimension_associations": dimension_associations(f), "stratified_gradients": stratified_gradients(f),
           "interactions": interactions(f), "pca": pca(f), "trajectories": traj}
    write_json("multivariate.json", res)
    print("wrote results/multivariate.json and results/trajectory_clusters.csv")
    print("  strongest dimension pairs:", [(p["a"], p["b"], p["cramers_v"]) for p in res["dimension_associations"]["pairs"][:5]])
    for name in ("most_vs_least_deprived", "disability_yes_vs_no"):
        s = res["stratified_gradients"][name]
        print(f"  {name}: crude {s['crude_gap_pp_active_at_28']} pp, engagement-standardised {s['engagement_standardised_gap_pp']} pp")
    print("  PCA explained variance:", res["pca"]["explained_variance_all"][:4])
    print("  trajectories: k =", traj["k_selected"], {k: v["silhouette"] for k, v in traj["by_k"].items()},
          "sizes", [c["n"] for c in traj["clusters"]], "success", [c["success"]["rate"] for c in traj["clusters"]])


if __name__ == "__main__":
    main()
