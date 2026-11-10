"""Tasks 5–6 – reproducible data preparation from raw OULAD files to analytic-ready views (brief sections 10–11).

The ten steps of brief section 10 are the ten functions below, run in order. Every decision implemented here is a
row of the Preparation Decision Matrix (data/metadata/decision_matrix.md); every derived variable follows
data/metadata/feature_spec.md. Raw files are only read; intermediates go to data/interim, views to data/processed.
Each step records its row counts in data/metadata/transformation_log.json, and every join is checked so that it
neither loses nor multiplies rows.

Usage (from the package folder): python src/prepare_data.py
Outputs (data/processed): enrolment, assessment_due, student_week, features_d13, features_d27, capacity_by_run
(.parquet). Run fit_transforms.py next for the model-ready matrices.
"""
from __future__ import annotations

import csv
import math

import polars as pl

from common import (CUTOFFS, ENROLMENT, IMD, INTERIM, KPI_DAY, META, PROCESSED, RAW, RUN, TABLES, enrolled_at, load,
                    now_utc, sha256, write_json)

LOG: list[dict] = []
EXPECTED_HEADERS = {
    "courses": ["code_module", "code_presentation", "module_presentation_length"],
    "assessments": ["code_module", "code_presentation", "id_assessment", "assessment_type", "date", "weight"],
    "vle": ["id_site", "code_module", "code_presentation", "activity_type", "week_from", "week_to"],
    "studentInfo": ["code_module", "code_presentation", "id_student", "gender", "region", "highest_education",
                    "imd_band", "age_band", "num_of_prev_attempts", "studied_credits", "disability", "final_result"],
    "studentRegistration": ["code_module", "code_presentation", "id_student", "date_registration",
                            "date_unregistration"],
    "studentAssessment": ["id_assessment", "id_student", "date_submitted", "is_banked", "score"],
    "studentVle": ["code_module", "code_presentation", "id_student", "id_site", "date", "sum_click"],
}
TYPES = ["oucontent", "forumng", "quiz", "homepage"]   # resource types carrying most clicks (critique 8)
TUTOR_GROUP = 20          # students per OU tutor group (data descriptor)
GAP_WEEKS = {}            # (module, presentation) -> weeks holding a day without any click (DQ15), filled in step 4


def log(step: str, what: str, rows_in=None, rows_out=None, note: str = ""):
    LOG.append({"step": step, "what": what, "rows_in": rows_in, "rows_out": rows_out, "note": note})
    print(f"[{step}] {what}: {rows_in} -> {rows_out} {note}")


def left_join_checked(left: pl.DataFrame, right: pl.DataFrame, on, step: str, what: str) -> pl.DataFrame:
    """Left join that must keep exactly the left rows (the right side is unique on the key)."""
    assert right.height == right.unique(subset=on).height, f"{what}: right side not unique on {on}"
    out = left.join(right, on=on, how="left")
    assert out.height == left.height, f"{what}: join changed rows {left.height} -> {out.height}"
    log(step, what, left.height, out.height, "left join, rows kept")
    return out


# 1 ------------------------------------------------------------------------------------------------------------------
def step1_load_validate() -> dict[str, pl.DataFrame]:
    pins = {r["file"]: r["pinned_sha256"] for r in csv.DictReader((META / "raw_check.csv").open())}
    t = {}
    for name in TABLES:
        digest = sha256(RAW / f"{name}.csv")
        assert digest == pins[f"{name}.csv"], f"{name}: raw file differs from the Milestone 2 pin"
        df = load(name)
        assert df.columns == EXPECTED_HEADERS[name], f"{name}: unexpected columns {df.columns}"
        t[name] = df
        log("1 load", f"{name}.csv (SHA-256 pinned, columns as documented)", None, df.height)
    return t


# 2 ------------------------------------------------------------------------------------------------------------------
def step2_population(t) -> pl.DataFrame:
    info, reg, crs = t["studentInfo"], t["studentRegistration"], t["courses"]
    e = left_join_checked(info, reg.select([*ENROLMENT, "date_registration", "date_unregistration"]), ENROLMENT,
                          "2 population", "studentInfo + studentRegistration")
    e = left_join_checked(e, crs, RUN, "2 population", "+ courses (run length)")
    e = e.with_columns(enrolled_at(13).alias("enrolled_d13"), enrolled_at(KPI_DAY).alias("enrolled_d14"),
                       enrolled_at(27).alias("enrolled_d27"))
    for c in ("enrolled_d13", "enrolled_d14", "enrolled_d27"):
        log("2 population", f"flag {c}", e.height, int(e[c].sum()), "enrolled at the day (C09)")
    return e


# 3 ------------------------------------------------------------------------------------------------------------------
def step3_standardise(e: pl.DataFrame, t) -> tuple[pl.DataFrame, pl.DataFrame]:
    bad = e.filter(pl.col("imd_band") == "10-20").height
    e = e.with_columns(
        pl.when(pl.col("imd_band") == "10-20").then(pl.lit("10-20%")).otherwise(pl.col("imd_band")).alias("imd_band"),
        pl.col("code_presentation").str.slice(0, 4).cast(pl.Int64).alias("year"),
        pl.col("code_presentation").str.slice(4, 1).alias("start_month"),
        pl.col("module_presentation_length").alias("run_length"),
        pl.col("final_result").is_in(["Pass", "Distinction"]).alias("completed"),
        pl.col("final_result").is_in(["Fail", "Withdrawn"]).alias("non_completion"),
    ).drop("module_presentation_length")
    e = e.with_columns(pl.when(pl.col("year") == 2013).then(pl.lit("train")).otherwise(pl.lit("test")).alias("split"))
    log("3 standardise", "imd_band label '10-20' -> '10-20%'", bad, e.filter(pl.col("imd_band") == "10-20").height)
    log("3 standardise", "year, start_month, completed, non_completion, split derived", e.height, e.height)
    asm = t["assessments"]
    tasks = asm.filter(pl.col("assessment_type") != "Exam").rename({"date": "due_day"})
    log("3 standardise", "tasks = TMA and CMA (exams excluded, DQ08)", asm.height, tasks.height)
    return e, tasks


# 4 ------------------------------------------------------------------------------------------------------------------
def step4_keys(t) -> tuple[pl.DataFrame, pl.DataFrame]:
    sv = t["studentVle"].join(t["vle"].select(["id_site", "activity_type"]), on="id_site", how="left")
    assert sv.height == t["studentVle"].height and sv["activity_type"].null_count() == 0
    dedup = t["studentVle"].unique()
    daily = sv.group_by([*ENROLMENT, "date"]).agg(
        pl.len().alias("records"), pl.col("sum_click").sum().alias("clicks"),
        *[pl.col("sum_click").filter(pl.col("activity_type") == a).sum().alias(f"clicks_{a}") for a in TYPES])
    daily_d = dedup.group_by([*ENROLMENT, "date"]).agg(pl.col("sum_click").sum().alias("clicks_dedup"))
    n = daily.height
    daily = daily.join(daily_d, on=[*ENROLMENT, "date"], how="left")
    assert daily.height == n and daily["clicks_dedup"].null_count() == 0
    site_days = t["studentVle"].select([*ENROLMENT, "id_site", "date"]).unique()
    log("4 keys", "studentVle rows -> enrolment x day (records, clicks, clicks_dedup)", sv.height, daily.height,
        f"clicks {int(daily['clicks'].sum()):,}, de-duplicated {int(daily['clicks_dedup'].sum()):,}")
    log("4 keys", "studentVle rows -> distinct enrolment x site x day", sv.height, site_days.height)
    # logging gap (DQ15): days within a run without any click by anyone
    run_days = daily.group_by([*RUN, "date"]).len().join(t["courses"], on=RUN)
    for m, p, length in t["courses"].iter_rows():
        days = set(run_days.filter((pl.col("code_module") == m) & (pl.col("code_presentation") == p))["date"].to_list())
        GAP_WEEKS[(m, p)] = sorted({d // 7 + 1 for d in range(0, length + 1) if d not in days})
    daily.write_parquet(INTERIM / "clicks_daily.parquet")
    site_days.write_parquet(INTERIM / "site_days.parquet")
    return daily, site_days


# 5 ------------------------------------------------------------------------------------------------------------------
def step5_missing(e: pl.DataFrame) -> pl.DataFrame:
    before = e["imd_band"].null_count()
    e = e.with_columns(
        pl.col("imd_band").fill_null("Missing"),
        pl.col("date_registration").is_null().alias("registration_missing"),
        ((pl.col("final_result") == "Withdrawn") & pl.col("date_unregistration").is_null()).alias("withdrawal_day_missing"),
        ((pl.col("final_result") != "Withdrawn") & pl.col("date_unregistration").is_not_null())
        .alias("unregistered_not_withdrawn"),
        (pl.col("date_unregistration") > pl.col("run_length")).alias("unregistered_after_run_end"),
        (-pl.col("date_registration")).alias("registration_lead"),
    )
    log("5 missing", "imd_band missing -> category 'Missing' (no imputation)", before, int((e["imd_band"] == "Missing").sum()))
    for c in ("registration_missing", "withdrawal_day_missing", "unregistered_not_withdrawn", "unregistered_after_run_end"):
        log("5 missing", f"flag {c}", e.height, int(e[c].sum()))
    return e


# 6 ------------------------------------------------------------------------------------------------------------------
def step6_truncate(e: pl.DataFrame, daily: pl.DataFrame, site_days: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
    """Activity after the unregistration day is not engagement while enrolled (DQ03). Submissions after it are kept
    in the assessment view with their day; counts of tasks consider only tasks due while enrolled (step 8)."""
    u = e.select([*ENROLMENT, "date_unregistration"])
    out = []
    for frame, what in ((daily, "enrolment x day click records"), (site_days, "enrolment x site x day records")):
        d = frame.join(u, on=ENROLMENT, how="left")
        kept = d.filter(pl.col("date_unregistration").is_null() | (pl.col("date") <= pl.col("date_unregistration")))
        note = f"clicks removed {int(d['clicks'].sum() - kept['clicks'].sum()):,}" if "clicks" in d.columns else ""
        log("6 truncate", f"{what} up to the unregistration day", d.height, kept.height, note)
        out.append(kept.drop("date_unregistration"))
    return out[0], out[1]


# 7 ------------------------------------------------------------------------------------------------------------------
def step7_integrate(e: pl.DataFrame, tasks: pl.DataFrame, sa: pl.DataFrame) -> pl.DataFrame:
    """Enrolment x task grid (every task of the run), then the student's submission if any."""
    grid = e.select([*ENROLMENT, "date_registration", "date_unregistration"]).join(
        tasks.select([*RUN, "id_assessment", "assessment_type", "due_day", "weight"]), on=RUN, how="inner")
    expected = e.join(tasks.group_by(RUN).len(), on=RUN)["len"].sum()
    assert grid.height == expected
    log("7 integrate", "enrolment x task grid (TMA, CMA of the run)", e.height, grid.height)
    subs = sa.select(["id_assessment", "id_student", "date_submitted", "is_banked", "score"])
    ad = left_join_checked(grid, subs, ["id_assessment", "id_student"], "7 integrate", "+ submission (if any)")
    matched = ad.filter(pl.col("date_submitted").is_not_null()).height
    task_subs = sa.join(tasks.select("id_assessment"), on="id_assessment").height
    assert matched == task_subs, "every TMA/CMA submission must land in the grid"
    log("7 integrate", "TMA/CMA submissions placed in the grid", task_subs, matched)
    return ad


# 8 ------------------------------------------------------------------------------------------------------------------
def assessment_status(ad: pl.DataFrame) -> pl.DataFrame:
    return ad.with_columns(
        pl.when(pl.col("is_banked") == 1).then(pl.lit("banked"))
        .when(pl.col("date_submitted").is_null()).then(pl.lit("not_submitted"))
        .when(pl.col("date_submitted") <= pl.col("due_day")).then(pl.lit("on_time"))
        .otherwise(pl.lit("late")).alias("status"),
        pl.when(pl.col("is_banked") == 0).then(pl.col("date_submitted") - pl.col("due_day")).alias("lateness_days"),
        ((pl.col("date_registration").is_null() | (pl.col("date_registration") <= pl.col("due_day")))
         & (pl.col("date_unregistration").is_null() | (pl.col("due_day") < pl.col("date_unregistration"))))
        .alias("due_while_enrolled"),
        (pl.col("due_day") // 7 + 1).alias("due_week"),
    )


def cutoff_features(e, ad, daily, site_days, c: int) -> pl.DataFrame:
    pop = e.filter(enrolled_at(c)).select(ENROLMENT)
    d = daily.join(pop, on=ENROLMENT, how="inner").filter(pl.col("date") <= c)
    act = d.group_by(ENROLMENT).agg(
        pl.col("clicks").filter(pl.col("date") < 0).sum().alias("clicks_pre"),
        pl.col("clicks").filter(pl.col("date") >= 0).sum().alias("clicks_0c"),
        pl.col("clicks_dedup").filter(pl.col("date") >= 0).sum().alias("clicks_0c_dedup"),
        (pl.col("date") >= 0).sum().alias("active_days_0c"),
        *[pl.col("clicks").filter((pl.col("date") >= 7 * (w - 1)) & (pl.col("date") <= 7 * w - 1)).sum()
          .alias(f"clicks_w{w}") for w in range(1, (c + 1) // 7 + 1)],
        pl.col("clicks").filter(pl.col("date") >= c - 6).sum().alias("clicks_last7"),
        pl.col("clicks").filter((pl.col("date") >= -14) & (pl.col("date") <= -1)).sum().alias("clicks_pre14"),
        pl.col("date").max().alias("_last_event_day"),
        pl.col("date").filter(pl.col("date") >= 0).max().alias("_last_active_day"),
        *[pl.col(f"clicks_{a}").filter(pl.col("date") >= 0).sum().alias(f"clicks_{a}_0c")
          for a in TYPES if f"clicks_{a}" in daily.columns],
    )
    sites = site_days.join(pop, on=ENROLMENT, how="inner").filter((pl.col("date") >= 0) & (pl.col("date") <= c)) \
                     .group_by(ENROLMENT).agg(pl.col("id_site").n_unique().alias("sites_0c"))
    # a task counts at the cut-off only if it fell due while the student was registered (audit F5)
    a = ad.join(pop, on=ENROLMENT, how="inner").filter(
        (pl.col("due_day") <= c) & (pl.col("date_registration").is_null() | (pl.col("due_day") >= pl.col("date_registration"))))
    nb = pl.col("is_banked").fill_null(0) == 0
    submitted_by_c = pl.col("date_submitted").is_not_null() & (pl.col("date_submitted") <= c) & nb
    late_by_c = submitted_by_c & (pl.col("date_submitted") > pl.col("due_day"))
    missed_by_c = nb & ~submitted_by_c
    early = ad.join(pop, on=ENROLMENT, how="inner").filter(
        (pl.col("due_day") > c) & nb & pl.col("date_submitted").is_not_null() & (pl.col("date_submitted") <= c)) \
        .group_by(ENROLMENT).agg(pl.len().alias("tasks_submitted_early_c"))
    tasks = a.group_by(ENROLMENT).agg(
        pl.len().alias("tasks_due_c"),
        missed_by_c.sum().alias("tasks_missed_c"),
        late_by_c.sum().alias("tasks_late_c"),
        (late_by_c & (pl.col("assessment_type") == "TMA")).sum().alias("tma_late_c"),
        (late_by_c & (pl.col("assessment_type") == "CMA")).sum().alias("cma_late_c"),
    )
    cma = ad.join(pop, on=ENROLMENT, how="inner").filter(
        (pl.col("assessment_type") == "CMA") & nb & (pl.col("date_submitted") <= c - 7) & pl.col("score").is_not_null())
    cma = cma.group_by(ENROLMENT).agg(pl.col("score").mean().alias("cma_score_mean_c"),
                                      pl.len().alias("cma_marked_c"),
                                      pl.col("date_submitted").max().alias("_last_cma_day"))
    step = f"8 features d{c}"
    f = e.filter(enrolled_at(c))
    n = f.height
    f = left_join_checked(f, act, ENROLMENT, step, "+ activity up to the cut-off")
    f = left_join_checked(f, sites, ENROLMENT, step, "+ distinct resources")
    f = left_join_checked(f, tasks, ENROLMENT, step, "+ tasks due by the cut-off")
    f = left_join_checked(f, cma, ENROLMENT, step, "+ CMA marks known by the cut-off")
    f = left_join_checked(f, early, ENROLMENT, step, "+ tasks submitted before their due day (due after the cut-off)")
    counts = ["clicks_pre", "clicks_pre14", "clicks_0c", "clicks_0c_dedup", "active_days_0c", "clicks_last7",
              "sites_0c", "tasks_due_c", "tasks_missed_c", "tasks_late_c", "tma_late_c", "cma_late_c",
              "cma_marked_c", "tasks_submitted_early_c", *[x for x in act.columns if x.endswith("_0c") and
                                                           x.startswith("clicks_") and x not in ("clicks_0c",
                                                                                                  "clicks_0c_dedup")],
              *[f"clicks_w{w}" for w in range(1, (c + 1) // 7 + 1)]]
    f = f.with_columns([pl.col(x).fill_null(0) for x in counts])
    med = f.group_by(RUN).agg(pl.col("clicks_0c").median().alias("_run_median"))
    f = left_join_checked(f, med, RUN, step, "+ run median of clicks up to the cut-off (same run, no outcome)")
    last_w, prev_w = f"clicks_w{(c + 1) // 7}", f"clicks_w{(c + 1) // 7 - 1}"
    f = f.with_columns(
        (pl.col("clicks_last7") == 0).alias("inactive_last7"),
        ((pl.col("clicks_0c") + 1) / (pl.col("_run_median") + 1)).alias("activity_ratio_run"),
        (c - pl.col("_last_active_day")).fill_null(c + 1).alias("days_since_last_click"),   # never active: c + 1 (F6)
        (pl.col(last_w) - pl.col(prev_w)).alias("trend_last_week"),
        (pl.col("tasks_missed_c") >= 1).alias("rule_missed"),
        (pl.col("tma_late_c") >= 1).alias("rule_tma_late"),
    ).with_columns(
        (pl.col("rule_missed") | pl.col("rule_tma_late") | pl.col("inactive_last7")).alias("early_sign_rule"),
    ).with_columns(
        (pl.col("early_sign_rule") | (pl.col("cma_late_c") >= 1)).alias("early_sign_rule_cma"))
    assert f.height == n
    # leakage guard: no activity or mark later than the cut-off contributed
    assert (f["_last_event_day"].drop_nulls() <= c).all() and (f["_last_cma_day"].drop_nulls() <= c - 7).all()
    log(step, "features built; max event day <= cut-off", n, f.height,
        f"early_sign_rule {int(f['early_sign_rule'].sum()):,}")
    return f.drop(["_run_median", "_last_active_day"])


# 9 ------------------------------------------------------------------------------------------------------------------
PREDICTORS = ["code_module", "start_month", "highest_education", "num_of_prev_attempts", "studied_credits",
              "registration_lead", "banked_results", "clicks_pre", "clicks_0c", "active_days_0c", "sites_0c",
              "inactive_last7", "activity_ratio_run", "tasks_due_c", "tasks_missed_c", "tasks_late_c", "tma_late_c",
              "cma_late_c", "cma_marked_c", "cma_score_mean_c"]
EXTENDED = ["registration_missing", "clicks_0c_dedup", "clicks_pre14", "days_since_last_click", "trend_last_week",
            "tasks_submitted_early_c", *[f"clicks_{a}_0c" for a in TYPES]]
RULE = ["early_sign_rule", "early_sign_rule_cma", "rule_missed", "rule_tma_late"]
AUDIT = ["gender", "age_band", "disability", "imd_band", "region"]


def step9_views(e, ad, daily, site_days, sa, t) -> dict[str, pl.DataFrame]:
    # enrolment-level descriptors known at registration
    banked = sa.filter(pl.col("is_banked") == 1).join(t["assessments"].select(["id_assessment", *RUN]),
                                                      on="id_assessment").group_by(ENROLMENT).len("banked_results")
    conc = e.group_by(["id_student", "code_presentation"]).len().with_columns((pl.col("len") - 1).alias("concurrent_runs"))
    e = left_join_checked(e, banked, ENROLMENT, "9 views", "+ banked results")
    e = left_join_checked(e, conc.drop("len"), ["id_student", "code_presentation"], "9 views", "+ concurrent runs")
    train_students = e.filter(pl.col("split") == "train").select("id_student").unique().with_columns(
        pl.lit(True).alias("student_in_training_runs"))
    e = left_join_checked(e, train_students, "id_student", "9 views", "+ student seen in training runs")
    years = t["courses"].with_columns(pl.col("code_presentation").str.slice(4, 1).alias("start_month"),
                                      pl.col("code_presentation").str.slice(0, 4).alias("y")) \
                        .group_by(["code_module", "start_month"]).agg((pl.col("y").n_unique() == 2).alias("paired_run"))
    e = left_join_checked(e, years, ["code_module", "start_month"], "9 views", "+ paired run flag")
    e = e.with_columns(pl.col("banked_results").fill_null(0),
                       (pl.col("student_in_training_runs").fill_null(False) & (pl.col("split") == "test"))
                       .alias("student_in_training_runs"))
    # assessment_due view
    ad = assessment_status(ad)
    first = ad.filter((pl.col("status") == "not_submitted") & pl.col("due_while_enrolled")).group_by(ENROLMENT) \
              .agg(pl.col("due_week").min().alias("first_missed_week"))
    whole = ad.filter(pl.col("due_while_enrolled") & (pl.col("status") != "banked")).group_by(ENROLMENT).agg(
        pl.len().alias("tasks_due_while_enrolled"),
        (pl.col("status") == "not_submitted").sum().alias("tasks_missed_while_enrolled"),
        (pl.col("status") == "late").sum().alias("tasks_late_while_enrolled"))
    act = daily.group_by(ENROLMENT).agg(pl.col("clicks").sum().alias("total_clicks"),
                                        pl.col("clicks_dedup").sum().alias("total_clicks_dedup"),
                                        pl.col("date").n_unique().alias("active_days"))
    for frame, what in ((first, "+ first missed task week"), (whole, "+ tasks while enrolled"),
                        (act, "+ whole-run activity (truncated at withdrawal)")):
        e = left_join_checked(e, frame, ENROLMENT, "9 views", what)
    e = e.with_columns([pl.col(c).fill_null(0) for c in ("tasks_due_while_enrolled", "tasks_missed_while_enrolled",
                                                         "tasks_late_while_enrolled", "total_clicks",
                                                         "total_clicks_dedup", "active_days")])
    # student_week view: weeks -3 .. last week of the run, up to the withdrawal week, zero-filled
    wk = daily.with_columns((pl.col("date") // 7 + 1).alias("week")).group_by([*ENROLMENT, "week"]).agg(
        pl.col("clicks").sum(), pl.col("clicks_dedup").sum(), pl.col("records").sum(),
        pl.col("date").n_unique().alias("active_days"))
    sw_sites = site_days.with_columns((pl.col("date") // 7 + 1).alias("week")).group_by([*ENROLMENT, "week"]) \
                        .agg(pl.col("id_site").n_unique().alias("sites"))
    weeks = pl.DataFrame({"week": list(range(-3, 40))})
    grid = e.select([*ENROLMENT, "run_length", "date_unregistration"]).join(weeks, how="cross").filter(
        (pl.col("week") <= pl.col("run_length") // 7 + 1)
        & (pl.col("date_unregistration").is_null() | (pl.col("week") <= pl.col("date_unregistration") // 7 + 1)))
    sw = left_join_checked(grid.drop(["run_length", "date_unregistration"]), wk, [*ENROLMENT, "week"], "9 views",
                           "student_week grid + weekly clicks")
    sw = left_join_checked(sw, sw_sites, [*ENROLMENT, "week"], "9 views", "+ weekly distinct resources")
    sw = sw.with_columns([pl.col(c).fill_null(0) for c in ("clicks", "clicks_dedup", "records", "active_days", "sites")])
    gaps = pl.DataFrame([{"code_module": m, "code_presentation": p, "week": w, "logging_gap": True}
                         for (m, p), ws in GAP_WEEKS.items() for w in ws],
                        schema={"code_module": pl.String, "code_presentation": pl.String, "week": pl.Int64,
                                "logging_gap": pl.Boolean})
    sw = left_join_checked(sw, gaps, [*RUN, "week"], "9 views", "+ logging-gap flag (DQ15)") \
        .with_columns(pl.col("logging_gap").fill_null(False))
    clicks_in_weeks = int(sw["clicks"].sum())
    assert clicks_in_weeks == int(daily.filter(pl.col("date") >= -28)["clicks"].sum()), "weekly clicks must add up"
    log("9 views", "student_week rows (weeks -3..run end, cut at withdrawal)", None, sw.height,
        f"clicks before week -3 not in this view: {int(daily.filter(pl.col("date") < -28)['clicks'].sum()):,}")
    # feature views
    feats = {}
    keep_e = [*ENROLMENT, "year", "start_month", "split", "paired_run", "student_in_training_runs",
              "withdrawal_day_missing", "final_result",
              "non_completion", "highest_education", "num_of_prev_attempts", "studied_credits", "registration_lead",
              "registration_missing", "banked_results", *AUDIT, "date_registration", "date_unregistration"]
    for name, c in CUTOFFS.items():
        f = cutoff_features(e.select(keep_e), ad, daily, site_days, c)
        f = f.drop(["date_registration", "date_unregistration", "_last_event_day", "_last_cma_day"])
        f = f.rename({"withdrawal_day_missing": "eval_withdrawal_day_unknown"})
        cols = [*ENROLMENT, "year", "split", "paired_run", "student_in_training_runs", "eval_withdrawal_day_unknown",
                "final_result",
                "non_completion", *RULE, *PREDICTORS, *EXTENDED, *AUDIT]
        cols = list(dict.fromkeys(x for x in cols if x in f.columns))
        feats[name] = f.select(cols + sorted(x for x in f.columns if x.startswith("clicks_w")))
    # capacity_by_run (AQ4 requirement; assumed capacities)
    cap = []
    for name, c in CUTOFFS.items():
        g = feats[name].group_by(RUN).agg(pl.len().alias("enrolled"), pl.col("non_completion").sum().alias("_nc"))
        for m, p, n, _ in g.sort(RUN).iter_rows():
            groups = math.ceil(n / TUTOR_GROUP)
            cap.append({"code_module": m, "code_presentation": p, "cutoff_day": c, "enrolled": n,
                        "tutor_groups_est": groups, "list_tutor_3": min(n, 3 * groups),
                        "list_tutor_5": min(n, 5 * groups), "list_office_30": min(n, 30), "list_office_40": min(n, 40)})
    views = {"enrolment": e,
             "assessment_due": ad.drop(["date_registration", "date_unregistration"]),
             "student_week": sw, "features_d13": feats["d13"], "features_d27": feats["d27"],
             "capacity_by_run": pl.DataFrame(cap)}
    return views


# 10 -----------------------------------------------------------------------------------------------------------------
def step10_persist(views: dict[str, pl.DataFrame]):
    PROCESSED.mkdir(parents=True, exist_ok=True)
    out = {}
    keys = {"enrolment": ENROLMENT, "assessment_due": [*ENROLMENT, "id_assessment"],
            "student_week": [*ENROLMENT, "week"], "features_d13": ENROLMENT, "features_d27": ENROLMENT,
            "capacity_by_run": [*RUN, "cutoff_day"]}
    for name, df in views.items():
        df = df.sort(keys[name])           # fixed row order, so a rerun writes identical files
        path = PROCESSED / f"{name}.parquet"
        df.write_parquet(path)
        out[name] = {"rows": df.height, "columns": df.width, "sha256": sha256(path)}
        log("10 persist", f"processed/{name}.parquet", None, df.height, f"{df.width} columns")
    write_json(META / "transformation_log.json", {"generated": now_utc(), "steps": LOG, "outputs": out})
    lines = ["# Transformation log", f"Written by `src/prepare_data.py` at {now_utc()}. One row per operation, in "
             "the order run; every join is a checked left join (rows in = rows out).", "",
             "| Step | Operation | Rows in | Rows out | Note |", "| :---- | :---- | :---- | :---- | :---- |"]
    fmt = lambda v: "" if v is None else f"{v:,}"
    lines += [f"| {r['step']} | {r['what']} | {fmt(r['rows_in'])} | {fmt(r['rows_out'])} | {r['note']} |" for r in LOG]
    (META / "transformation_log.md").write_text("\n".join(lines) + "\n")


def main():
    INTERIM.mkdir(parents=True, exist_ok=True)
    t = step1_load_validate()
    e = step2_population(t)
    e, tasks = step3_standardise(e, t)
    daily, site_days = step4_keys(t)
    e = step5_missing(e)
    daily, site_days = step6_truncate(e, daily, site_days)
    sa = t["studentAssessment"]
    ad = step7_integrate(e, tasks, sa)
    views = step9_views(e, ad, daily, site_days, sa, t)   # step 8 (features) runs inside, per cut-off
    step10_persist(views)


if __name__ == "__main__":
    main()
