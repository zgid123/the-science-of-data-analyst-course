"""Task 6 – transforms that learn from data, fitted on the training runs only (brief section 11).

For linear models in Milestone 4, the feature views are turned into numeric matrices: ordered categories as ordinal
codes, nominal categories one-hot with the levels seen in training runs (a level that appears only in test runs,
such as module CCC, becomes all zeros), booleans as 0/1, counts log1p, missing values filled with the training
median next to a missing indicator, and every numeric column standardised with the training mean and standard
deviation. Every parameter comes from rows with split = "train" (2013 runs). Tree models read the feature views
directly, but only the columns named in data/metadata/predictor_sets.json (primary and extended predictors): the
identifier, target, evaluation and audit columns of a view are never model inputs (audit F2).

Self-check (V12): the parameters are fitted a second time after every test row has been altered; they must be
identical.

Usage (from the package folder): python src/fit_transforms.py   (after prepare_data.py)
Writes data/metadata/transform_params.json and data/processed/model_ready_d13.parquet, model_ready_d27.parquet.
"""
from __future__ import annotations

import math

import polars as pl

from common import CUTOFFS, EDU, ENROLMENT, META, PROCESSED, now_utc, write_json
from prepare_data import EXTENDED, PREDICTORS

KEEP = [*ENROLMENT, "year", "split", "paired_run", "student_in_training_runs", "eval_withdrawal_day_unknown",
        "final_result", "non_completion",
        "early_sign_rule", "early_sign_rule_cma", "gender", "age_band", "disability", "imd_band", "region"]
NOMINAL = ["code_module", "start_month"]
ORDINAL = {"highest_education": EDU}
NO_INDICATOR = {"registration_lead"}   # its missing flag is the extended predictor registration_missing (audit F3)
NOT_COUNTS = {"registration_lead", "activity_ratio_run", "cma_score_mean_c", "trend_last_week", "days_since_last_click"}


def fit(df: pl.DataFrame, cols: list[str], c: int) -> dict:
    """All parameters from training rows only."""
    tr = df.filter(pl.col("split") == "train")
    p = {"cutoff": c, "nominal_levels": {n: sorted(tr[n].unique().to_list()) for n in NOMINAL},
         "ordinal_codes": {k: {v: i for i, v in enumerate(order)} for k, order in ORDINAL.items()},
         "fill_median": {}, "log1p": [], "mean": {}, "std": {}}
    num = [x for x in cols if x not in NOMINAL and x not in ORDINAL]
    for x in num:
        if df[x].dtype == pl.Boolean:
            continue
        med = tr[x].median()                                   # training median of every numeric column,
        p["fill_median"][x] = None if med is None else float(med)   # applied wherever a value is null
        if tr[x].null_count() and x not in NO_INDICATOR:       # indicator decided on training rows only (audit F4)
            p.setdefault("indicator", []).append(x)
        if x not in NOT_COUNTS and (tr[x].drop_nulls() >= 0).all():
            p["log1p"].append(x)
    X = encode(tr, cols, p, scale=False)
    for x in X.columns:
        if x in KEEP:
            continue
        p["mean"][x] = float(X[x].mean())
        s = float(X[x].std())
        p["std"][x] = s if s and not math.isnan(s) else 1.0
    return p


def encode(df: pl.DataFrame, cols: list[str], p: dict, scale: bool = True) -> pl.DataFrame:
    exprs = []
    for n in NOMINAL:
        exprs += [(pl.col(n) == lv).cast(pl.Int8).alias(f"{n}={lv}") for lv in p["nominal_levels"][n]]
    for k, codes in p["ordinal_codes"].items():
        exprs.append(pl.col(k).replace_strict(codes, default=None, return_dtype=pl.Float64).alias(k))
    for x in cols:
        if x in NOMINAL or x in ORDINAL:
            continue
        e = pl.col(x).cast(pl.Float64)
        if x in p.get("indicator", []):
            exprs.append(pl.col(x).is_null().cast(pl.Int8).alias(f"{x}_missing"))
        if p["fill_median"].get(x) is not None:
            e = e.fill_null(p["fill_median"][x])
        if x in p["log1p"]:
            e = e.log1p()
        exprs.append(e.alias(x))
    X = df.select([*[pl.col(k) for k in KEEP if k in df.columns], *exprs])
    if scale:
        X = X.with_columns([((pl.col(x) - p["mean"][x]) / p["std"][x]).alias(x) for x in p["mean"]])
    return X


def main():
    params = {"generated": now_utc(), "fitted_on": "split = train (2013B, 2013J runs)", "cutoffs": {}}
    for name, c in CUTOFFS.items():
        df = pl.read_parquet(PROCESSED / f"features_{name}.parquet")
        cols = [x for x in [*PREDICTORS, *EXTENDED] if x in df.columns] + sorted(
            x for x in df.columns if x.startswith("clicks_w"))
        p = fit(df, cols, c)
        # V12 self-check: alter every test row (numbers x 3 + 7, booleans flipped, nominal levels renamed) and refit
        altered = df.with_columns([
            pl.when(pl.col("split") == "test").then(
                (pl.col(x) * 3 + 7) if df[x].dtype.is_numeric() else (~pl.col(x)) if df[x].dtype == pl.Boolean
                else pl.lit("ZZZ")).otherwise(pl.col(x)).alias(x)
            for x in cols if x not in ORDINAL])
        p2 = fit(altered, cols, c)
        assert p == p2, "a test row changed a fitted parameter"
        X = encode(df, cols, p)
        X.write_parquet(PROCESSED / f"model_ready_{name}.parquet")
        tr = X.filter(pl.col("split") == "train")
        feats = [x for x in X.columns if x not in KEEP]
        print(f"{name}: {X.height:,} rows, {len(feats)} model columns; parameters fitted on {tr.height:,} training "
              f"rows; V12 self-check identical parameters after altering {X.height - tr.height:,} test rows: PASS")
        print(f"   training means of standardised columns within 1e-9 of 0: "
              f"{all(abs(float(tr[x].mean())) < 1e-9 for x in p['mean'])}; test rows of an unseen module "
              f"(code_module levels {p['nominal_levels']['code_module']})")
        params["cutoffs"][name] = {**p, "columns": feats, "primary": [x for x in PREDICTORS if x in cols]}
    write_json(META / "transform_params.json", params)
    write_json(META / "predictor_sets.json", {
        "rule": "the only columns a model may use; everything else in a feature view is id, split, evaluation, target, "
                "rule or audit (data_dictionary.md)",
        "primary": PREDICTORS, "extended": EXTENDED,
        "weekly_clicks": {n: [f"clicks_w{w}" for w in range(1, (c + 1) // 7 + 1)] for n, c in CUTOFFS.items()},
        "not_used_in_milestone4": {"cma_score_mean_c": "known for fewer than 10% of training rows at both cut-offs"}})


if __name__ == "__main__":
    main()
