"""Stage 2 - features: one row per enrolment (outcome, demographics with ordinal codes, registration,
total and early-window clicks and active days, raw and de-duplicated, submissions, scores, first assessment).

Run from the repository root: venv/bin/python datasets/oulad/exploration/code/02_features.py
Writes results/enrolment_features.csv, the input of stage 3.
"""

from __future__ import annotations

import polars as pl

from common import AGE, EARLY, EDU, ENROLMENT, IMD, OUTCOMES, PRESENTATION, RESULTS, load_all


def features(t: dict[str, pl.DataFrame]) -> pl.DataFrame:
    si = t["studentInfo"].with_columns(
        pl.when(pl.col("imd_band") == "10-20").then(pl.lit("10-20%")).otherwise(pl.col("imd_band")).alias("imd_band"))
    assert set(si["imd_band"].drop_nulls().unique()) <= set(IMD)
    assert set(si["age_band"].unique()) <= set(AGE) and set(si["highest_education"].unique()) <= set(EDU)
    reg = t["studentRegistration"].select(ENROLMENT + ["date_registration", "date_unregistration"])
    length = t["courses"]
    vle = t["studentVle"]
    early = pl.col("date").is_between(0, EARLY - 1)
    clicks = vle.group_by(ENROLMENT).agg(
        pl.col("sum_click").sum().alias("clicks_total"),
        pl.col("date").n_unique().alias("active_days"),
        pl.col("sum_click").filter(early).sum().alias("clicks_early"),
        pl.col("date").filter(early).n_unique().alias("active_days_early"),
        pl.col("sum_click").filter(pl.col("date") < 0).sum().alias("clicks_prestart"),
    )
    clicks_dedup = vle.unique().group_by(ENROLMENT).agg(
        pl.col("sum_click").filter(early).sum().alias("clicks_early_dedup"))

    a = t["assessments"]
    sub = t["studentAssessment"].join(a.select(["id_assessment", "assessment_type", "date"] + PRESENTATION),
                                      on="id_assessment")
    per = sub.group_by(ENROLMENT).agg(
        pl.len().alias("n_submitted"),
        pl.col("score").filter(pl.col("is_banked") == 0).mean().round(2).alias("mean_score"),
        (pl.col("date_submitted") > pl.col("date")).sum().alias("n_late"),
    )
    # first assessment of each presentation: the earliest-due TMA/CMA (ties: lowest id)
    first = (a.filter(pl.col("assessment_type") != "Exam").drop_nulls("date")
             .sort(["date", "id_assessment"]).group_by(PRESENTATION).first()
             .select(PRESENTATION + [pl.col("id_assessment").alias("first_id"), pl.col("date").alias("first_due")]))
    first_sub = (sub.join(first, left_on=PRESENTATION + ["id_assessment"], right_on=PRESENTATION + ["first_id"])
                 .select(ENROLMENT + [pl.col("score").alias("first_score"),
                                      (pl.col("date_submitted") - pl.col("first_due")).alias("first_days_late")]))

    f = (si.join(reg, on=ENROLMENT, how="left").join(length, on=PRESENTATION, how="left")
         .join(clicks, on=ENROLMENT, how="left").join(clicks_dedup, on=ENROLMENT, how="left")
         .join(per, on=ENROLMENT, how="left").join(first, on=PRESENTATION, how="left").drop("first_id")
         .join(first_sub, on=ENROLMENT, how="left"))
    zero_fill = ["clicks_total", "active_days", "clicks_early", "active_days_early", "clicks_prestart",
                 "clicks_early_dedup", "n_submitted", "n_late"]
    return f.with_columns(
        [pl.col(c).fill_null(0) for c in zero_fill]
        + [pl.col("first_score").is_not_null().alias("first_submitted"),
           pl.col("final_result").is_in(["Pass", "Distinction"]).alias("success"),
           (pl.col("final_result") == "Withdrawn").alias("withdrawn"),
           pl.col("final_result").replace_strict({o: i for i, o in enumerate(OUTCOMES)}).alias("outcome_ord"),
           pl.col("imd_band").replace_strict({b: i for i, b in enumerate(IMD)}, default=None).alias("imd_ord"),
           pl.col("age_band").replace_strict({b: i for i, b in enumerate(AGE)}).alias("age_ord"),
           pl.col("highest_education").replace_strict({b: i for i, b in enumerate(EDU)}).alias("edu_ord"),
           pl.col("code_presentation").str.slice(0, 4).alias("year"),
           pl.col("code_presentation").str.slice(4, 1).alias("semester"),
           pl.when(pl.col("num_of_prev_attempts") >= 2).then(pl.lit("2+"))
             .otherwise(pl.col("num_of_prev_attempts").cast(pl.Int64).cast(pl.String)).alias("prev_attempts"),
           # still registered at the end of the early window (exposure-fair population for engagement)
           (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") >= EARLY)).alias("active_at_28")])


def main() -> None:
    f = features(load_all())
    RESULTS.mkdir(parents=True, exist_ok=True)
    f.write_csv(RESULTS / "enrolment_features.csv")
    print(f"enrolment features: {f.height:,} rows x {f.width} columns -> results/enrolment_features.csv")


if __name__ == "__main__":
    main()
