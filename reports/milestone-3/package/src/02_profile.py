"""Task 2 – data profiling and data quality assessment on the full raw data (brief section 7).

Covers the ten aspects of the brief: shape and schema, missingness (by variable, group and time, co-occurrence),
duplicates and key integrity, validity and consistency, distributions, outliers, outcome balance, temporal coverage,
join integrity and representativeness. Nothing is changed: every result describes data/raw. The results are the
evidence of the Data Quality Issue Log (data/metadata/quality_issue_log.md), whose rows cite the keys of
profile.json. Twelve numbers are cross-checked against the earlier OULAD exploration
(datasets/oulad/exploration/results), when that folder is present.

Usage (from the package folder): python src/02_profile.py
Writes data/metadata/profile.json, profile_crosscheck.csv, fig_outcome_by_run.csv, fig_weekly_activity.csv.
"""
from __future__ import annotations

import csv
import json

import polars as pl

from common import (CUTOFFS, ENROLMENT, EXPLORATION, KPI_DAY, META, RUN, TABLES, enrolled_at, load, now_utc,
                    write_json)

DOCUMENTED_ROWS = {"courses": 22, "assessments": 206, "vle": 6364, "studentInfo": 32593,
                   "studentRegistration": 32593, "studentAssessment": 173912, "studentVle": 10655280}


def rate(n, d):
    return round(n / d, 4) if d else None


def quantiles(s: pl.Series, qs=(0.01, 0.25, 0.5, 0.75, 0.95, 0.99)):
    return {f"p{int(q * 100)}": float(s.quantile(q, "nearest")) for q in qs}


def gini(values: pl.Series) -> float:
    v = values.sort().cast(pl.Float64)
    n = v.len()
    cum = (v * pl.Series(range(1, n + 1), dtype=pl.Float64)).sum()
    return round(float((2 * cum) / (n * v.sum()) - (n + 1) / n), 3)


def main():
    t = {n: load(n) for n in TABLES if n != "studentVle"}
    sv = load("studentVle")
    info, reg, asm, sa, vle, crs = (t["studentInfo"], t["studentRegistration"], t["assessments"],
                                    t["studentAssessment"], t["vle"], t["courses"])
    enrol = info.join(reg.select([*ENROLMENT, "date_registration", "date_unregistration"]), on=ENROLMENT) \
                .join(crs, on=RUN)
    enrol = enrol.with_columns(
        pl.col("code_presentation").str.slice(0, 4).alias("year"),
        pl.col("code_presentation").str.slice(4, 1).alias("start_month"),
        pl.col("final_result").is_in(["Fail", "Withdrawn"]).alias("non_completion"))
    P: dict = {"generated": now_utc()}

    # 1. Shape and schema ------------------------------------------------------------------------------------------
    P["shape"] = {n: {"rows": (sv if n == "studentVle" else t[n]).height,
                      "columns": (sv if n == "studentVle" else t[n]).width,
                      "documented_rows": DOCUMENTED_ROWS[n],
                      "rows_match_documentation": (sv if n == "studentVle" else t[n]).height == DOCUMENTED_ROWS[n]}
                  for n in TABLES}
    P["shape"]["schema_differences"] = [
        "courses: column module_presentation_length, documented as length",
        "studentInfo: outcome value Withdrawn, documented as Withdrawal",
        "studentVle: no key; several rows per student, site and day, while the descriptor calls the table daily "
        "summaries of clicks"]
    grain = sv.group_by([*ENROLMENT, "id_site", "date"]).agg(pl.len().alias("n"), pl.col("sum_click").n_unique()
                                                              .alias("distinct_clicks"))
    rep = grain.filter(pl.col("n") > 1)
    P["shape"]["studentVle_grain"] = {
        "student_site_day_groups": grain.height,
        "groups_with_several_rows": rep.height,
        "rows_in_such_groups": int(rep["n"].sum()),
        "groups_with_several_rows_and_different_clicks": rep.filter(pl.col("distinct_clicks") > 1).height,
        "max_rows_in_one_group": int(grain["n"].max())}

    # 2. Missingness -----------------------------------------------------------------------------------------------
    miss = {}
    for n in TABLES:
        df = sv if n == "studentVle" else t[n]
        miss[n] = {c: {"missing": df[c].null_count(), "rate": rate(df[c].null_count(), df.height)}
                   for c in df.columns if df[c].null_count()}
    P["missing"] = {"by_column": miss}
    imd_by_region = enrol.group_by("region").agg(pl.col("imd_band").is_null().sum().alias("missing"), pl.len().alias("n")) \
                         .with_columns((pl.col("missing") / pl.col("n")).round(4).alias("rate")) \
                         .sort("rate", descending=True)
    imd_by_run = enrol.group_by(RUN).agg(pl.col("imd_band").is_null().mean().round(4).alias("rate"))
    imd_outcome = enrol.group_by(pl.col("imd_band").is_null().alias("imd_missing")) \
                       .agg(pl.col("final_result").is_in(["Pass", "Distinction"]).mean().round(4).alias("success"),
                            pl.len().alias("n")).sort("imd_missing")
    reg_missing = enrol.filter(pl.col("date_registration").is_null()).group_by("final_result").len().sort("final_result")
    sa_t = sa.join(asm.select(["id_assessment", *RUN, "assessment_type", "date"]), on="id_assessment")
    score_missing = sa_t.filter(pl.col("score").is_null()).group_by("assessment_type").len().sort("assessment_type")
    exam_rows = sa_t.filter(pl.col("assessment_type") == "Exam")
    exams = asm.filter(pl.col("assessment_type") == "Exam")
    exams_with_scores = exams.join(exam_rows.select("id_assessment").unique(), on="id_assessment")
    sv_enrol = sv.select(ENROLMENT).unique()
    sa_enrol = sa_t.select(ENROLMENT).unique()
    no_act = enrol.join(sv_enrol, on=ENROLMENT, how="anti")
    no_sub = enrol.join(sa_enrol, on=ENROLMENT, how="anti")
    both = no_act.join(no_sub.select(ENROLMENT), on=ENROLMENT)
    P["missing"].update({
        "imd_band_by_region_top3": imd_by_region.head(3).rows(),
        "imd_band_by_region_zero": imd_by_region.filter(pl.col("missing") == 0)["region"].to_list(),
        "imd_band_rate_by_run_range": [float(imd_by_run["rate"].min()), float(imd_by_run["rate"].max())],
        "imd_band_success_missing_vs_present": imd_outcome.rows(),
        "date_registration_missing_by_outcome": reg_missing.rows(),
        "date_unregistration_missing_structural": "empty for every enrolment that did not unregister "
                                                  "(the descriptor's rule); not a missing value",
        "score_missing_by_type": score_missing.rows(),
        "exams": exams.height, "exams_with_any_score": exams_with_scores.height,
        "exams_with_scores_by_module": exams_with_scores.group_by("code_module").len().sort("code_module").rows(),
        "vle_week_from_missing_rate": rate(vle["week_from"].null_count(), vle.height),
        "enrolments_without_activity": no_act.height,
        "enrolments_without_activity_by_outcome": no_act.group_by("final_result").len().sort("final_result").rows(),
        "enrolments_without_activity_unregistered_by_day0": no_act.filter(pl.col("date_unregistration") <= 0).height,
        "enrolments_without_submission": no_sub.height,
        "enrolments_without_both": both.height,
        "enrolments_without_both_by_outcome": both.group_by("final_result").len().sort("final_result").rows(),
    })

    # 3. Duplicates and keys ---------------------------------------------------------------------------------------
    dup_rows = sv.height - sv.unique().height
    dup_groups = sv.group_by(sv.columns).len().filter(pl.col("len") > 1)
    by_run = sv.group_by(RUN).agg(pl.len().alias("rows")).join(
        dup_groups.group_by(RUN).agg((pl.col("len") - 1).sum().alias("extra")), on=RUN, how="left") \
        .with_columns((pl.col("extra") / pl.col("rows")).round(4).alias("share"))
    clicks_raw = int(sv["sum_click"].sum())
    clicks_dedup = int(sv.unique()["sum_click"].sum())
    P["duplicates"] = {
        "exact_duplicate_rows": {n: (sv.height - sv.unique().height if n == "studentVle"
                                     else t[n].height - t[n].unique().height) for n in TABLES},
        "studentVle_extra_rows": dup_rows, "studentVle_extra_row_share": rate(dup_rows, sv.height),
        "studentVle_duplicated_groups": dup_groups.height,
        "studentVle_single_click_group_share": rate(dup_groups.filter(pl.col("sum_click") == 1).height, dup_groups.height),
        "studentVle_extra_share_by_run_range": [float(by_run["share"].min()), float(by_run["share"].max())],
        "studentVle_extra_share_by_year": by_run.with_columns(pl.col("code_presentation").str.slice(0, 4).alias("y"))
            .group_by("y").agg((pl.col("extra").sum() / pl.col("rows").sum()).round(4).alias("share"))
            .sort("y").rows(),
        "clicks_raw": clicks_raw, "clicks_exact_duplicates_collapsed": clicks_dedup,
        "clicks_share_removed_by_collapsing": rate(clicks_raw - clicks_dedup, clicks_raw),
        "key_duplicates": {n: t[n].height - t[n].unique(subset=k).height for n, k in
                           {"courses": RUN, "assessments": ["id_assessment"], "vle": ["id_site"],
                            "studentInfo": ENROLMENT, "studentRegistration": ENROLMENT,
                            "studentAssessment": ["id_assessment", "id_student"]}.items()},
        "studentVle_site_in_other_run": sv.join(vle.select(["id_site", pl.col("code_module").alias("m"),
                                                            pl.col("code_presentation").alias("p")]), on="id_site")
                                          .filter((pl.col("m") != pl.col("code_module"))
                                                  | (pl.col("p") != pl.col("code_presentation"))).height,
    }

    # Are exact duplicates copies or separate records that happen to share a click count? Among student-site-day
    # groups with exactly two rows, compare the share with equal counts to the share expected by chance from each
    # resource's own click distribution (and from each activity type's).
    g2 = sv.group_by([*ENROLMENT, "id_site", "date"]).agg(pl.len().alias("n"), pl.col("sum_click").n_unique()
                                                           .alias("u"), pl.col("sum_click")).filter(pl.col("n") == 2)
    g2 = g2.join(vle.select(["id_site", "activity_type"]), on="id_site")
    long = g2.select(["id_site", "activity_type", "sum_click"]).explode("sum_click")
    def expected(level):
        p = long.group_by([level, "sum_click"]).len().with_columns(
            (pl.col("len") / pl.col("len").sum().over(level)).alias("p"))
        e = p.group_by(level).agg((pl.col("p") ** 2).sum().alias("exp"))
        w = g2.group_by(level).len().join(e, on=level)
        return round(float((w["exp"] * w["len"]).sum() / w["len"].sum()), 4)
    by_type = g2.group_by("activity_type").agg((pl.col("u") == 1).mean().round(4).alias("observed"),
                                               pl.len().alias("groups")).sort("groups", descending=True).head(6)
    P["duplicates"]["chance_test_two_row_groups"] = {
        "groups": g2.height, "observed_equal_share": round(float((g2["u"] == 1).mean()), 4),
        "expected_by_site": expected("id_site"), "expected_by_activity_type": expected("activity_type"),
        "observed_by_activity_type_top6": by_type.rows()}

    # 4. Validity and consistency ----------------------------------------------------------------------------------
    sa_e = sa_t.join(enrol.select([*ENROLMENT, "date_unregistration", "date_registration",
                                   "module_presentation_length"]), on=ENROLMENT)
    nb = sa_e.filter(pl.col("is_banked") == 0)
    sv_e = sv.join(enrol.select([*ENROLMENT, "date_unregistration"]), on=ENROLMENT)
    after_unreg = sv_e.filter(pl.col("date_unregistration").is_not_null()
                              & (pl.col("date") > pl.col("date_unregistration")))
    sub_after_unreg = nb.filter(pl.col("date_unregistration").is_not_null()
                                & (pl.col("date_submitted") > pl.col("date_unregistration")))
    late = nb.filter(pl.col("date").is_not_null())
    lateness = (late["date_submitted"] - late["date"])
    P["validity"] = {
        "score_out_of_range": sa.filter((pl.col("score") < 0) | (pl.col("score") > 100)).height,
        "submissions_before_registration": nb.filter(pl.col("date_registration").is_not_null()
                                                     & (pl.col("date_submitted") < pl.col("date_registration"))).height,
        "submissions_after_run_end": nb.filter(pl.col("date_submitted") > pl.col("module_presentation_length")).height,
        "submissions_after_run_end_by_type": nb.filter(pl.col("date_submitted") > pl.col("module_presentation_length"))
                                               .group_by("assessment_type").len().sort("assessment_type").rows(),
        "submissions_late": int((lateness > 0).sum()), "submissions_with_due_day": late.height,
        "late_share": rate(int((lateness > 0).sum()), late.height),
        "late_by_type": late.group_by("assessment_type").agg((pl.col("date_submitted") > pl.col("date")).sum()
                                                             .alias("late"), pl.len().alias("submissions"))
                            .sort("assessment_type").rows(),
        "lateness_days_of_late": quantiles(lateness.filter(lateness > 0), (0.5, 0.9, 0.99)),
        "banked_rows": sa.filter(pl.col("is_banked") == 1).height,
        "banked_day_values": sa.filter(pl.col("is_banked") == 1)["date_submitted"].unique().to_list(),
        "click_rows_after_unregistration": after_unreg.height,
        "clicks_after_unregistration": int(after_unreg["sum_click"].sum()),
        "enrolments_with_clicks_after_unregistration": after_unreg.select(ENROLMENT).unique().height,
        "max_days_clicking_after_unregistration": int((after_unreg["date"] - after_unreg["date_unregistration"]).max()),
        "submissions_after_unregistration": sub_after_unreg.height,
        "submissions_after_unregistration_incl_banked": sa_e.filter(
            pl.col("date_unregistration").is_not_null()
            & (pl.col("date_submitted") > pl.col("date_unregistration"))).height,
        "enrolments_with_submissions_after_unregistration": sub_after_unreg.select(ENROLMENT).unique().height,
        "registration_after_day14": enrol.filter(pl.col("date_registration") > KPI_DAY).height,
        "registration_after_day14_by_outcome": enrol.filter(pl.col("date_registration") > KPI_DAY)
                                                    .group_by("final_result").len().sort("final_result").rows(),
        "unregistration_after_run_end": enrol.filter(pl.col("date_unregistration")
                                                     > pl.col("module_presentation_length")).height,
        "withdrawn_without_day": enrol.filter((pl.col("final_result") == "Withdrawn")
                                              & pl.col("date_unregistration").is_null()).height,
        "withdrawn_without_day_by_presentation": enrol.filter((pl.col("final_result") == "Withdrawn")
                                                              & pl.col("date_unregistration").is_null())
                                                      .group_by("code_presentation").len().sort("code_presentation").rows(),
        "fail_with_unregistration_day": enrol.filter((pl.col("final_result") != "Withdrawn")
                                                     & pl.col("date_unregistration").is_not_null()).height,
        "imd_label_without_percent": sorted(set(info["imd_band"].drop_nulls().to_list())
                                            - {f"{a}-{a + 10}%" for a in range(0, 100, 10)}),
        "coursework_weight_total_by_run_values": asm.filter(pl.col("assessment_type") != "Exam").group_by(RUN)
                                                    .agg(pl.col("weight").sum()).get_column("weight").unique().sort().to_list(),
        "exam_weight_total_by_run_values": asm.filter(pl.col("assessment_type") == "Exam").group_by(RUN)
                                              .agg(pl.col("weight").sum()).get_column("weight").unique().sort().to_list(),
    }

    # 5. Distributions and 6. outliers ------------------------------------------------------------------------------
    clicks_enr = enrol.select(ENROLMENT).join(sv.group_by(ENROLMENT).agg(pl.col("sum_click").sum().alias("clicks")),
                                              on=ENROLMENT, how="left").with_columns(pl.col("clicks").fill_null(0))
    ce = clicks_enr["clicks"]
    q1, q3 = ce.quantile(0.25, "nearest"), ce.quantile(0.75, "nearest")
    score = sa["score"].drop_nulls()
    sc_q1, sc_q3 = score.quantile(0.25, "nearest"), score.quantile(0.75, "nearest")
    cr = info["studied_credits"]
    P["distribution"] = {
        "sum_click_per_row": {**quantiles(sv["sum_click"]), "max": int(sv["sum_click"].max()),
                              "skew": round(float(sv["sum_click"].skew()), 2)},
        "clicks_per_enrolment": {**quantiles(ce), "max": int(ce.max()), "zero": int((ce == 0).sum()),
                                 "skew": round(float(ce.skew()), 2), "gini": gini(ce),
                                 "iqr_fence_upper": float(q3 + 1.5 * (q3 - q1)),
                                 "beyond_iqr_fence": int((ce > q3 + 1.5 * (q3 - q1)).sum())},
        "score": {**quantiles(score), "mean": round(float(score.mean()), 1), "zeros": int((score == 0).sum()),
                  "below_iqr_fence": int((score < sc_q1 - 1.5 * (sc_q3 - sc_q1)).sum()),
                  "below_40": int((score < 40).sum())},
        "score_multiple_of_10_share_by_type": sa_t.filter(pl.col("score").is_not_null()).group_by("assessment_type")
            .agg(((pl.col("score") % 10) == 0).mean().round(4).alias("share")).sort("assessment_type").rows(),
        "studied_credits": {**quantiles(cr), "max": int(cr.max()), "above_p99": int((cr > cr.quantile(0.99, "nearest")).sum())},
        "date_registration": quantiles(reg["date_registration"].drop_nulls()),
        "num_of_prev_attempts_zero_share": rate(int((info["num_of_prev_attempts"] == 0).sum()), info.height),
        "rare_categories": {c: info.group_by(c).len().sort("len").head(2).rows()
                            for c in ["age_band", "highest_education", "region", "disability"]},
    }
    P["outliers"] = {
        "largest_sum_click_rows": sv.sort("sum_click", descending=True).head(3)
                                    .select([*ENROLMENT, "id_site", "date", "sum_click"]).rows(),
        "studied_credits_max_rows": info.filter(pl.col("studied_credits") >= 400).height,
        "submission_day_max": int(sa["date_submitted"].max()),
    }

    # 7. Outcome balance -------------------------------------------------------------------------------------------
    kpi = enrol.filter(enrolled_at(KPI_DAY))
    def pop(day):
        return enrol.filter(enrolled_at(day))
    by_run = enrol.group_by([*RUN, "final_result"]).len().pivot("final_result", index=RUN, values="len") \
                  .fill_null(0).sort(RUN)
    P["outcome"] = {
        "overall": enrol.group_by("final_result").len().sort("len", descending=True).rows(),
        "kpi_population_day14": kpi.height,
        "kpi_population_day14_milestone2_rule": enrol.filter(pl.col("date_unregistration").is_null()
                                                             | (pl.col("date_unregistration") > KPI_DAY)).height,
        "kpi_non_completion_rate": round(float(kpi["non_completion"].mean()), 4),
        "kpi_completion_rate": round(1 - float(kpi["non_completion"].mean()), 4),
        "population_at_cutoff": {k: {"enrolments": pop(d).height,
                                     "non_completion": int(pop(d)["non_completion"].sum()),
                                     "rate": round(float(pop(d)["non_completion"].mean()), 4),
                                     "withdrawn": pop(d).filter(pl.col("final_result") == "Withdrawn").height,
                                     "fail": pop(d).filter(pl.col("final_result") == "Fail").height}
                                 for k, d in CUTOFFS.items()},
        "kpi_non_completion_by_run_range": [
            round(float(v), 4) for v in kpi.group_by(RUN).agg(pl.col("non_completion").mean())["non_completion"]
            .sort().gather([0, -1])],
        "kpi_non_completion_by_year": kpi.group_by("year").agg(pl.col("non_completion").mean().round(4), pl.len())
                                         .sort("year").rows(),
        "smallest_minority_class_in_a_run": int(kpi.group_by(RUN).agg((~pl.col("non_completion")).sum().alias("c"),
                                                                      pl.col("non_completion").sum().alias("n"))
                                                   .select(pl.min_horizontal("c", "n")).min().item()),
    }
    by_run.write_csv(META / "fig_outcome_by_run.csv")

    # 8. Temporal coverage -----------------------------------------------------------------------------------------
    weekly = sv.with_columns((pl.col("date").floordiv(7)).alias("week")).group_by([*RUN, "week"]) \
               .agg(pl.col("sum_click").sum().alias("clicks"), pl.col("id_student").n_unique().alias("students")) \
               .sort([*RUN, "week"])
    weekly.write_csv(META / "fig_weekly_activity.csv")
    daily = sv.group_by([*RUN, "date"]).agg(pl.col("sum_click").sum()).join(crs, on=RUN)
    gaps = []
    for m, p, length in crs.iter_rows():
        days = set(daily.filter((pl.col("code_module") == m) & (pl.col("code_presentation") == p))["date"].to_list())
        missing = [d for d in range(0, length + 1) if d not in days]
        if missing:
            gaps.append([m, p, missing])
    nonexam = asm.filter(pl.col("assessment_type") != "Exam")
    due = {}
    for k, d in CUTOFFS.items():
        per = crs.select(RUN).join(nonexam.filter(pl.col("date") <= d).group_by(RUN).len(), on=RUN, how="left") \
                 .with_columns(pl.col("len").fill_null(0))
        due[k] = {"runs_with_task_due": per.filter(pl.col("len") >= 1).height,
                  "runs_with_two_or_more_due": per.filter(pl.col("len") >= 2).height,
                  "tasks_due_per_run_values": per["len"].value_counts().sort("len").rows()}
    first_due = nonexam.group_by(RUN).agg(pl.col("date").min().alias("first_due"))
    hist = crs.with_columns(pl.col("code_presentation").str.slice(4, 1).alias("sm"),
                            pl.col("code_presentation").str.slice(0, 4).alias("yr"))
    pairs = hist.group_by(["code_module", "sm"]).agg(pl.col("yr").n_unique().alias("years"))
    P["temporal"] = {
        "years": sorted(enrol["year"].unique().to_list()),
        "days_without_any_click_within_run": gaps,
        "tasks_due_by_cutoff": due,
        "first_non_exam_due_day_range": [int(first_due["first_due"].min()), int(first_due["first_due"].max())],
        "module_start_month_pairs_with_both_years": pairs.filter(pl.col("years") == 2).height,
        "module_start_month_with_one_year_only": pairs.filter(pl.col("years") == 1)
                                                   .select(["code_module", "sm"]).sort(["code_module", "sm"]).rows(),
        "weeks_with_activity_range": [int(weekly["week"].min()), int(weekly["week"].max())],
    }

    conc_keys = kpi.group_by(["id_student", "code_presentation"]).len().filter(pl.col("len") > 1)
    conc = kpi.join(conc_keys.select(["id_student", "code_presentation"]), on=["id_student", "code_presentation"])
    P["temporal"]["concurrent_enrolments_day14"] = {
        "enrolments": conc.height, "share": rate(conc.height, kpi.height),
        "by_presentation": conc.group_by("code_presentation").len().sort("code_presentation").rows()}

    # 9. Join integrity --------------------------------------------------------------------------------------------
    j1 = sa.join(asm, on="id_assessment", how="inner")
    j2 = j1.join(info, on=ENROLMENT, how="inner")
    agg_sv = sv.group_by(ENROLMENT).agg(pl.col("sum_click").sum())
    naive = sa_t.select(ENROLMENT).group_by(ENROLMENT).len().join(sv.group_by(ENROLMENT).len(), on=ENROLMENT) \
                .select((pl.col("len") * pl.col("len_right")).sum()).item()
    left_lost = enrol.join(agg_sv, on=ENROLMENT, how="inner").height
    P["joins"] = {
        "studentAssessment→assessments rows": [sa.height, j1.height],
        "…→studentInfo rows": [j1.height, j2.height],
        "studentVle→vle rows": [sv.height, sv.join(vle.select(["id_site", "activity_type"]), on="id_site").height],
        "enrolment⋈aggregated clicks (inner) rows": [enrol.height, left_lost],
        "enrolments lost by an inner join with activity": enrol.height - left_lost,
        "naive submissions×click-rows join rows (many-to-many)": int(naive),
        "rule": "aggregate studentVle and studentAssessment to the enrolment (or enrolment-week) grain before joining "
                "them; use left joins from the enrolment table so enrolments without activity are kept",
    }

    # 10. Representativeness ---------------------------------------------------------------------------------------
    share = lambda c: [(k, n, round(n / enrol.height, 3)) for k, n in
                       enrol.group_by(c).len().sort("len", descending=True).rows()]
    P["representativeness"] = {
        "age_band": share("age_band"), "highest_education": share("highest_education"),
        "gender": share("gender"), "disability": share("disability"),
        "studied_credits_60_or_less_share": rate(int((info["studied_credits"] <= 60).sum()), info.height),
        "female_share_by_module": enrol.group_by("code_module").agg((pl.col("gender") == "F").mean().round(3))
                                       .sort("code_module").rows(),
        "kpi_completion_by_module": kpi.group_by("code_module").agg((~pl.col("non_completion")).mean().round(3))
                                       .sort("code_module").rows(),
        "regions": enrol["region"].n_unique(),
    }
    write_json(META / "profile.json", P)

    # Cross-check against the earlier exploration --------------------------------------------------------------------
    rows = []
    if (EXPLORATION / "results").exists():
        r = EXPLORATION / "results"
        ov = {d["table"]: d for d in json.loads((r / "overview.json").read_text())}
        ck = {d["check"]: d["observed"] for d in json.loads((r / "checks.json").read_text())}
        fu = json.loads((r / "followups.json").read_text())
        pairs = [
            ("studentVle exact duplicate rows", ov["studentVle"]["duplicate_full_rows"], P["duplicates"]["studentVle_extra_rows"]),
            ("clicks raw", fu["duplicate_click_impact"]["clicks_raw"], clicks_raw),
            ("clicks after collapsing duplicates", fu["duplicate_click_impact"]["clicks_exact_duplicates_collapsed"], clicks_dedup),
            ("repeated student-site-day groups", ck["studentVle rows repeating (enrolment, site, day)"][0],
             P["shape"]["studentVle_grain"]["groups_with_several_rows"]),
            ("rows in repeated groups", ck["studentVle rows repeating (enrolment, site, day)"][1],
             P["shape"]["studentVle_grain"]["rows_in_such_groups"]),
            ("enrolments without activity", ck["enrolments with no VLE activity"][0], P["missing"]["enrolments_without_activity"]),
            ("enrolments without submission", ck["enrolments with no assessment submission"][0], P["missing"]["enrolments_without_submission"]),
            ("late submissions", ck["submissions after the assessment's due day"][0], P["validity"]["submissions_late"]),
            ("submissions after run end", fu["submissions_after_presentation_end"]["count"], P["validity"]["submissions_after_run_end"]),
            ("click rows after unregistration", fu["activity_after_unregistration"]["click_rows_after"], P["validity"]["click_rows_after_unregistration"]),
            ("enrolments with clicks after unregistration", fu["activity_after_unregistration"]["enrolments_with_clicks_after"],
             P["validity"]["enrolments_with_clicks_after_unregistration"]),
            ("submissions after unregistration (incl. 13 banked rows dated day -1)", fu["activity_after_unregistration"]["submissions_after"],
             P["validity"]["submissions_after_unregistration_incl_banked"]),
            ("click rows before day 0", ck["VLE activity before day 0 (pre-start)"], int((sv["date"] < 0).sum())),
        ]
        rows = [{"measure": a, "exploration": b, "milestone3": c, "equal": b == c} for a, b, c in pairs]
        with (META / "profile_crosscheck.csv").open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)

    # Console summary ---------------------------------------------------------------------------------------------
    print("shape match documentation:", {n: v["rows_match_documentation"] for n, v in P["shape"].items()
                                          if isinstance(v, dict) and "rows" in v})
    print("studentVle grain:", P["shape"]["studentVle_grain"])
    for k in ("duplicates", "validity", "outcome", "temporal", "joins"):
        print(f"--- {k}")
        for a, b in P[k].items():
            s = str(b)
            print(f"  {a}: {s[:300]}")
    print("--- missing (selected)")
    for a in ("imd_band_by_region_top3", "imd_band_success_missing_vs_present", "date_registration_missing_by_outcome",
              "score_missing_by_type", "exams_with_any_score", "exams_with_scores_by_module",
              "enrolments_without_activity_by_outcome", "enrolments_without_activity_unregistered_by_day0",
              "enrolments_without_both_by_outcome"):
        print(f"  {a}: {P['missing'][a]}")
    print("--- distribution:", json.dumps(P["distribution"], default=str)[:1200])
    print("--- representativeness:", json.dumps(P["representativeness"], default=str)[:900])
    if rows:
        print(f"--- cross-check with exploration: {sum(r['equal'] for r in rows)} of {len(rows)} equal")
        for r in rows:
            if not r["equal"]:
                print("  DIFF", r)


if __name__ == "__main__":
    main()
