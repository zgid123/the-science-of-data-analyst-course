"""Stage 3 - describe: outcome segments and the deeper descriptive analysis, following the data-analyst skill's
EDA workflow (references/eda.md, steps 3-8) with effect sizes and intervals in place of significance tests
(n is large, so almost any difference is "significant"; size and direction carry the information).

Analyses: segments for the report charts; shape and outliers, concentration, zero-variance / case / redundancy
checks, correlations, outcome by every dimension (Wilson intervals, bias-corrected Cramer's V, within-module V),
Simpson's paradox check (crude vs module-standardised gaps), early-window engagement by outcome (Cliff's delta,
raw and de-duplicated clicks), temporal structure (daily gaps, weekly cycle, assessment peaks, presentation drift),
withdrawal survival (Kaplan-Meier), assessment behaviour, activity mix, missingness mechanism of imd_band.

Run from the repository root, after 02_features.py: venv/bin/python datasets/oulad/exploration/code/03_describe.py
Reads results/enrolment_features.csv and the raw tables; writes results/segments.json and results/descriptive.json.
"""

from __future__ import annotations

import polars as pl

from common import EARLY, ENROLMENT, OUTCOMES, PRESENTATION, RESULTS, load_all, write_json
from stats import cliffs_delta, concentration, cramers_v, kaplan_meier, shape, wilson


SURVIVAL_DAYS = [0, 14, 28, 60, 90, 120, 180, 240, 269]
MIN_CELL = 30  # smallest group size used in a per-module comparison

NUMERIC = ["num_of_prev_attempts", "studied_credits", "date_registration", "clicks_total", "active_days",
           "clicks_early", "active_days_early", "clicks_prestart", "n_submitted", "n_late", "mean_score",
           "first_score", "first_days_late", "imd_ord", "age_ord", "edu_ord", "outcome_ord"]
DIMENSIONS = ["code_module", "year", "semester", "gender", "region", "highest_education", "imd_band", "age_band",
              "disability", "prev_attempts"]
ORDINAL = {"highest_education": "edu_ord", "imd_band": "imd_ord", "age_band": "age_ord",
           "prev_attempts": "num_of_prev_attempts"}


def read_features() -> pl.DataFrame:
    """Stage 2 output with the string columns that look numeric kept as strings."""
    return pl.read_csv(RESULTS / "enrolment_features.csv", infer_schema_length=None,
                       schema_overrides={c: pl.String for c in ("year", "semester", "prev_attempts", "imd_band")})


def segments(t: dict[str, pl.DataFrame]) -> dict:
    si = t["studentInfo"]
    by_mod = si.group_by(["code_module", "final_result"]).len().pivot(on="final_result", index="code_module", values="len").sort("code_module").fill_null(0)
    by_pres = si.group_by(["code_presentation", "final_result"]).len().pivot(on="final_result", index="code_presentation", values="len").sort("code_presentation").fill_null(0)
    clicks = (t["studentVle"].group_by(ENROLMENT).agg(pl.col("sum_click").sum().alias("clicks"))
              .join(si.select(ENROLMENT + ["final_result"]), on=ENROLMENT, how="right")
              .with_columns(pl.col("clicks").fill_null(0)))
    by_result = clicks.group_by("final_result").agg(
        pl.len().alias("enrolments"), pl.col("clicks").median().alias("median_clicks"),
        pl.col("clicks").quantile(0.25, "nearest").alias("p25"), pl.col("clicks").quantile(0.75, "nearest").alias("p75"),
        (pl.col("clicks") == 0).sum().alias("zero_click")).sort("median_clicks")
    sizes = si.group_by(PRESENTATION).len().sort(PRESENTATION)
    # clicks per enrolment per week (week 0 = days 0-6), averaged over every enrolment in the outcome group
    group_n = si.group_by("final_result").len().rename({"len": "n"})
    weekly = (t["studentVle"].join(si.select(ENROLMENT + ["final_result"]), on=ENROLMENT)
              .with_columns((pl.col("date") // 7).cast(pl.Int32).alias("week"))
              .group_by(["final_result", "week"]).agg(pl.col("sum_click").sum().alias("clicks"))
              .join(group_n, on="final_result")
              .with_columns((pl.col("clicks") / pl.col("n")).round(3).alias("clicks_per_enrolment"))
              .sort(["final_result", "week"]))
    # exact duplicate rows of the click log, per presentation
    vle = t["studentVle"]
    keys = ENROLMENT + ["id_site", "date", "sum_click"]
    dup = (vle.group_by(keys).len().filter(pl.col("len") > 1)
           .group_by(PRESENTATION).agg((pl.col("len") - 1).sum().alias("duplicate_rows")))
    dup_share = (vle.group_by(PRESENTATION).len().rename({"len": "rows"}).join(dup, on=PRESENTATION, how="left")
                 .with_columns(pl.col("duplicate_rows").fill_null(0),
                               (pl.col("duplicate_rows").fill_null(0) / pl.col("rows")).round(5).alias("share"))
                 .sort(PRESENTATION))
    return {"final_result_by_module": by_mod.to_dicts(), "final_result_by_presentation": by_pres.to_dicts(),
            "clicks_by_final_result": by_result.to_dicts(), "enrolments_per_presentation": sizes.to_dicts(),
            "weekly_clicks_by_final_result": weekly.select(["final_result", "week", "clicks_per_enrolment"]).to_dicts(),
            "duplicate_rows_by_presentation": dup_share.to_dicts()}


def univariate(f: pl.DataFrame) -> dict:
    return {
        "shape": {c: shape(f[c]) for c in NUMERIC if c != "outcome_ord"},
        "clicks_total_concentration": concentration(f["clicks_total"]),
        "clicks_early_concentration": concentration(f["clicks_early"]),
    }


def structure_checks(t: dict[str, pl.DataFrame], f: pl.DataFrame) -> dict:
    zero_var, case_collisions = [], []
    for name, df in t.items():
        for c in df.columns:
            if df[c].n_unique() == 1:
                zero_var.append(f"{name}.{c}")
            if df[c].dtype == pl.String:
                v = df[c].drop_nulls()
                if v.n_unique() != v.str.strip_chars().str.to_lowercase().n_unique():
                    case_collisions.append(f"{name}.{c}")
    vle = t["vle"].drop_nulls(["week_from", "week_to"])
    corr = correlations(f)
    return {
        "zero_variance_columns": zero_var,
        "case_or_whitespace_collisions": case_collisions,
        "vle_week_from_equals_week_to": wilson(int((vle["week_from"] == vle["week_to"]).sum()), vle.height),
        "redundant_feature_pairs_abs_spearman_ge_0_9": [p for p in corr["strong_pairs"] if abs(p["spearman"]) >= 0.9],
    }


def correlations(f: pl.DataFrame) -> dict:
    cols = [c for c in NUMERIC]
    pairs = []
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            d = f.select(a, b).drop_nulls()
            if d.height < 3:
                continue
            r = d.select(pl.corr(a, b).alias("p"), pl.corr(a, b, method="spearman").alias("s")).row(0)
            pairs.append({"a": a, "b": b, "n": d.height, "pearson": round(r[0], 3), "spearman": round(r[1], 3)})
    return {"columns": cols, "pairs": pairs,
            "strong_pairs": sorted([p for p in pairs if abs(p["spearman"]) >= 0.5], key=lambda p: -abs(p["spearman"]))}


def outcome_by_dimension(f: pl.DataFrame) -> dict:
    out = {}
    modules = f["code_module"].unique().sort().to_list()
    for dim in DIMENSIONS:
        d = f.with_columns(pl.col(dim).fill_null("(missing)"))
        rows = []
        for (val,), g in d.group_by([dim], maintain_order=False):
            counts = {o: int((g["final_result"] == o).sum()) for o in OUTCOMES}
            rows.append({"value": val, "n": g.height, **counts,
                         "success": wilson(int(g["success"].sum()), g.height),
                         "withdrawn": wilson(int(g["withdrawn"].sum()), g.height)})
        within = [cramers_v(f.filter(pl.col("code_module") == m), dim, "final_result") for m in modules] \
            if dim != "code_module" else []
        within = [v for v in within if v is not None]
        entry = {"rows": sorted(rows, key=lambda r: str(r["value"])),
                 "cramers_v": cramers_v(f, dim, "final_result"),
                 "cramers_v_within_module": {"min": min(within), "median": sorted(within)[len(within) // 2],
                                             "max": max(within)} if within else None}
        if dim in ORDINAL:
            g = f.select(ORDINAL[dim], "outcome_ord").drop_nulls()
            entry["spearman_with_outcome_order"] = round(g.select(pl.corr(ORDINAL[dim], "outcome_ord",
                                                                          method="spearman")).item(), 4)
        out[dim] = entry
    return out


CONTRASTS = {  # name: (column, group 1 values, group 2 values)
    "female_vs_male": ("gender", ["F"], ["M"]),
    "disability_yes_vs_no": ("disability", ["Y"], ["N"]),
    "most_vs_least_deprived_imd": ("imd_band", ["0-10%", "10-20%"], ["80-90%", "90-100%"]),
    "repeat_vs_first_attempt": ("prev_attempts", ["1", "2+"], ["0"]),
    "age_35plus_vs_under35": ("age_band", ["35-55", "55<="], ["0-35"]),
    "B_vs_J_presentation": ("semester", ["B"], ["J"]),
}


def simpson(f: pl.DataFrame) -> dict:
    """Crude gap (group 1 minus group 2, percentage points) against the module-standardised gap."""
    out = {}
    for name, (col, g1, g2) in CONTRASTS.items():
        for metric in ("success", "withdrawn"):
            rate = lambda d: float(d[metric].mean()) if d.height else None
            a, b = f.filter(pl.col(col).is_in(g1)), f.filter(pl.col(col).is_in(g2))
            crude = (rate(a) - rate(b)) * 100
            per, wsum, wgap = [], 0, 0.0
            for m in f["code_module"].unique().sort():
                am, bm = a.filter(pl.col("code_module") == m), b.filter(pl.col("code_module") == m)
                if am.height < MIN_CELL or bm.height < MIN_CELL:
                    continue
                gap = (rate(am) - rate(bm)) * 100
                w = am.height + bm.height
                per.append({"module": m, "gap_pp": round(gap, 2), "n1": am.height, "n2": bm.height})
                wsum += w
                wgap += w * gap
            std = wgap / wsum if wsum else None
            out[f"{name}:{metric}"] = {
                "crude_gap_pp": round(crude, 2), "module_standardised_gap_pp": round(std, 2) if std is not None else None,
                "modules_compared": len(per),
                "modules_opposite_sign": sum(1 for p in per if p["gap_pp"] * crude < 0),
                "group1_share_by_module": {m: round(float((f.filter(pl.col("code_module") == m)[col].is_in(g1)).mean()), 3)
                                           for m in f["code_module"].unique().sort()},
                "per_module": per}
    return out


def early_engagement(f: pl.DataFrame) -> dict:
    """Days 0-27 engagement by outcome among enrolments still registered on day 28 (equal exposure)."""
    p = f.filter(pl.col("active_at_28"))
    by_outcome = []
    for o in OUTCOMES:
        g = p.filter(pl.col("final_result") == o)
        by_outcome.append({"final_result": o, "n": g.height,
                           "median_clicks": g["clicks_early"].median(),
                           "p25": g["clicks_early"].quantile(0.25, "nearest"),
                           "p75": g["clicks_early"].quantile(0.75, "nearest"),
                           "median_active_days": g["active_days_early"].median(),
                           "zero_click_share": round(float((g["clicks_early"] == 0).mean()), 4)})
    delta = lambda d, c: cliffs_delta(d.filter(pl.col("success"))[c], d.filter(~pl.col("success"))[c])
    per_module = []
    for m in p["code_module"].unique().sort():
        d = p.filter(pl.col("code_module") == m)
        per_module.append({"module": m, "n": d.height, "success_rate": round(float(d["success"].mean()), 4),
                           "delta_clicks": delta(d, "clicks_early"), "delta_clicks_dedup": delta(d, "clicks_early_dedup"),
                           "delta_active_days": delta(d, "active_days_early")})
    lc = p.with_columns(pl.col("clicks_early").log1p().alias("lc"))
    grand = lc["lc"].mean()
    between = float(lc.group_by("code_module").agg(pl.len().alias("n"), pl.col("lc").mean().alias("m"))
                    .select((pl.col("n") * (pl.col("m") - grand) ** 2).sum()).item())
    total = float(((lc["lc"] - grand) ** 2).sum())
    return {
        "population": {"enrolments": f.height, "active_at_28": p.height,
                       "excluded_unregistered_before_28": f.height - p.height},
        "by_outcome": by_outcome,
        "cliffs_delta_success_vs_not": {"clicks_early": delta(p, "clicks_early"),
                                        "clicks_early_dedup": delta(p, "clicks_early_dedup"),
                                        "active_days_early": delta(p, "active_days_early"),
                                        "clicks_prestart": delta(p, "clicks_prestart")},
        "per_module": per_module,
        "eta_squared_log_early_clicks_by_module": round(between / total, 4),
    }


def temporal(t: dict[str, pl.DataFrame], f: pl.DataFrame) -> dict:
    vle, courses, a = t["studentVle"], t["courses"], t["assessments"]
    daily = vle.group_by(PRESENTATION + ["date"]).agg(pl.col("sum_click").sum().alias("clicks"))
    rows = []
    for mod, pres, length in courses.sort(PRESENTATION).iter_rows():
        d = daily.filter((pl.col("code_module") == mod) & (pl.col("code_presentation") == pres))
        series = dict(zip(d["date"].cast(pl.Int64).to_list(), d["clicks"].to_list()))
        days = list(range(0, int(length) + 1))
        x = [series.get(day, 0) for day in days]
        m = sum(x) / len(x)
        den = sum((v - m) ** 2 for v in x)
        acf = lambda k: sum((x[i] - m) * (x[i + k] - m) for i in range(len(x) - k)) / den
        dues = [int(v) for v in a.filter((pl.col("code_module") == mod) & (pl.col("code_presentation") == pres)
                                         & (pl.col("assessment_type") != "Exam"))["date"].drop_nulls()]
        near = {day for due in dues for day in range(due - 2, due + 1)}
        in_w = [x[i] for i in range(len(x)) if days[i] in near]
        out_w = [x[i] for i in range(len(x)) if days[i] not in near]
        rows.append({"presentation": f"{mod} {pres}", "length": int(length),
                     "zero_click_days_0_to_end": sum(1 for v in x if v == 0),
                     "zero_click_day_list": [days[i] for i, v in enumerate(x) if v == 0],
                     "acf_lag1": round(acf(1), 3), "acf_lag7": round(acf(7), 3), "acf_lag14": round(acf(14), 3),
                     "assessment_window_ratio": round((sum(in_w) / len(in_w)) / (sum(out_w) / len(out_w)), 3)
                     if in_w and out_w else None})
    drift = []
    for (mod, pres), g in f.group_by(PRESENTATION):
        drift.append({"presentation": f"{mod} {pres}", "module": mod, "year": pres[:4], "semester": pres[4],
                      "n": g.height, "success_rate": round(float(g["success"].mean()), 4),
                      "withdrawal_rate": round(float(g["withdrawn"].mean()), 4),
                      "median_clicks_early": g.filter(pl.col("active_at_28"))["clicks_early"].median()})
    drift.sort(key=lambda r: r["presentation"])
    yoy = []
    idx = {(r["module"], r["year"], r["semester"]): r for r in drift}
    for (mod, year, sem), r in idx.items():
        if year == "2013" and (mod, "2014", sem) in idx:
            r2 = idx[(mod, "2014", sem)]
            yoy.append({"module": mod, "semester": sem,
                        "success_change_pp": round((r2["success_rate"] - r["success_rate"]) * 100, 2),
                        "withdrawal_change_pp": round((r2["withdrawal_rate"] - r["withdrawal_rate"]) * 100, 2)})
    med = lambda k: sorted(r[k] for r in rows)[len(rows) // 2]
    return {"per_presentation": rows, "median_acf_lag7": med("acf_lag7"), "median_acf_lag1": med("acf_lag1"),
            "median_assessment_window_ratio": med("assessment_window_ratio"),
            "presentations_with_zero_click_days": sum(1 for r in rows if r["zero_click_days_0_to_end"]),
            "drift": drift, "year_on_year": sorted(yoy, key=lambda r: (r["module"], r["semester"]))}


def survival(f: pl.DataFrame) -> dict:
    """Kaplan-Meier time to withdrawal from day 0. Event = Withdrawn with an unregistration day > 0;
    everyone else is censored at the presentation length. Withdrawn without a date are excluded."""
    before = f.filter(pl.col("date_unregistration") <= 0)
    p = f.filter(~((pl.col("withdrawn")) & pl.col("date_unregistration").is_null())
                 & (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") > 0)))
    p = p.with_columns((pl.col("withdrawn") & pl.col("date_unregistration").is_not_null()).alias("event"),
                       pl.when(pl.col("withdrawn") & pl.col("date_unregistration").is_not_null())
                       .then(pl.col("date_unregistration")).otherwise(pl.col("module_presentation_length")).alias("time"))
    weekly = list(range(0, 270, 7))
    curves = {"All": kaplan_meier(p["time"], p["event"], weekly)}
    for m in p["code_module"].unique().sort():
        g = p.filter(pl.col("code_module") == m)
        curves[m] = kaplan_meier(g["time"], g["event"], weekly)
    ev = p.filter(pl.col("event"))
    before_first = ev.filter(pl.col("time") < pl.col("first_due")).height
    return {
        "population": {"from_day_0": p.height, "events": ev.height,
                       "unregistered_on_or_before_day_0": before.height,
                       "withdrawn_without_date_excluded": int((f["withdrawn"] & f["date_unregistration"].is_null()).sum())},
        "survival_at": {k: kaplan_meier(p.filter(pl.col("code_module") == k)["time"] if k != "All" else p["time"],
                                        p.filter(pl.col("code_module") == k)["event"] if k != "All" else p["event"],
                                        SURVIVAL_DAYS) for k in curves},
        "weekly_curves": curves,
        "withdrawal_day_quantiles": {q: ev["time"].quantile(q / 100, "nearest") for q in (10, 25, 50, 75, 90)},
        "withdrawals_before_first_assessment_due": wilson(before_first, ev.height),
    }


def assessments(t: dict[str, pl.DataFrame], f: pl.DataFrame) -> dict:
    a = t["assessments"]
    sub = t["studentAssessment"].join(a, on="id_assessment")
    graded = sub.filter(pl.col("is_banked") == 0)
    score = (graded.group_by(["code_module", "assessment_type"])
             .agg(pl.len().alias("n"), pl.col("score").median().alias("median"),
                  pl.col("score").quantile(0.25, "nearest").alias("p25"),
                  pl.col("score").quantile(0.75, "nearest").alias("p75"),
                  (pl.col("score") < 40).mean().round(4).alias("below_40_share"))
             .sort(["code_module", "assessment_type"]))
    enrol = f.group_by(PRESENTATION).len().rename({"len": "enrolments"})
    rate = (a.join(sub.group_by("id_assessment").len().rename({"len": "submissions"}), on="id_assessment", how="left")
            .join(enrol, on=PRESENTATION).with_columns(pl.col("submissions").fill_null(0))
            .with_columns((pl.col("submissions") / pl.col("enrolments")).alias("rate")))
    by_type = (rate.group_by("assessment_type").agg(pl.len().alias("assessments"),
                                                    pl.col("rate").median().round(4).alias("median_submission_rate"),
                                                    (pl.col("submissions") == 0).sum().alias("with_no_submissions"))
               .sort("assessment_type"))
    exams_scored = (rate.filter(pl.col("assessment_type") == "Exam").group_by("code_module")
                    .agg((pl.col("submissions") > 0).sum().alias("exams_with_scores"), pl.len().alias("exams")).sort("code_module"))
    late = sub.filter(pl.col("date").is_not_null()).with_columns((pl.col("date_submitted") - pl.col("date")).alias("dl"))
    first = f.group_by("final_result").agg(pl.len().alias("n"), (~pl.col("first_submitted")).mean().round(4).alias("first_not_submitted"),
                                           pl.col("first_score").median().alias("median_first_score"))
    return {
        "score_by_module_and_type": score.to_dicts(),
        "submission_rate_by_type": by_type.to_dicts(),
        "exams_with_scores_by_module": exams_scored.to_dicts(),
        "days_late_quantiles_among_late": {q: late.filter(pl.col("dl") > 0)["dl"].quantile(q / 100, "nearest")
                                           for q in (50, 75, 90, 99)},
        "first_assessment_by_outcome": sorted(first.to_dicts(), key=lambda r: OUTCOMES.index(r["final_result"])),
        "cliffs_delta_first_score_success_vs_not": cliffs_delta(f.filter(pl.col("success"))["first_score"],
                                                                f.filter(~pl.col("success"))["first_score"]),
    }


def activity_mix(t: dict[str, pl.DataFrame], f: pl.DataFrame) -> dict:
    """Share of early-window clicks by activity type, successful vs not, among enrolments active at day 28."""
    p = f.filter(pl.col("active_at_28")).select(ENROLMENT + ["success"])
    v = (t["studentVle"].filter(pl.col("date").is_between(0, EARLY - 1))
         .join(t["vle"].select(["id_site", "activity_type"]), on="id_site")
         .join(p, on=ENROLMENT)
         .group_by(["success", "activity_type"]).agg(pl.col("sum_click").sum().alias("clicks")))
    tot = v.group_by("success").agg(pl.col("clicks").sum().alias("total"))
    s = v.join(tot, on="success").with_columns((pl.col("clicks") / pl.col("total")).alias("share"))
    wide = (s.with_columns(pl.when(pl.col("success")).then(pl.lit("successful")).otherwise(pl.lit("unsuccessful")).alias("g"))
            .pivot(on="g", index="activity_type", values="share").fill_null(0)
            .with_columns(((pl.col("successful") - pl.col("unsuccessful")) * 100).round(2).alias("diff_pp"),
                          pl.col("successful").round(4), pl.col("unsuccessful").round(4))
            .sort("diff_pp"))
    return {"rows": wide.to_dicts(), "clicks_per_group": {str(k): v for k, v in tot.rows()}}


def imd_missingness(f: pl.DataFrame) -> dict:
    d = f.with_columns(pl.col("imd_band").is_null().alias("imd_missing"))
    by_region = (d.group_by("region").agg(pl.len().alias("n"), pl.col("imd_missing").sum().alias("missing"))
                 .with_columns((pl.col("missing") / pl.col("n")).round(4).alias("rate")).sort("rate", descending=True))
    miss = d.filter(pl.col("imd_missing"))
    return {"by_region": by_region.to_dicts(),
            "cramers_v_missing_vs_region": cramers_v(d, "imd_missing", "region"),
            "cramers_v_missing_vs_outcome": cramers_v(d, "imd_missing", "final_result"),
            "success_missing": wilson(int(miss["success"].sum()), miss.height),
            "success_present": wilson(int(d.filter(~pl.col("imd_missing"))["success"].sum()),
                                      d.filter(~pl.col("imd_missing")).height)}


# measured over the whole presentation, so partly a consequence of the outcome (withdrawn students stop)
FULL_WINDOW = {"clicks_total", "active_days", "n_submitted", "n_late", "mean_score"}


def signal_ranking(f: pl.DataFrame) -> dict:
    """Every numeric enrolment measure ranked by how strongly it separates success from non-success
    (Cliff's delta overall and the median of the per-module deltas)."""
    rows = []
    modules = f["code_module"].unique().sort()
    for c in NUMERIC:
        if c == "outcome_ord":
            continue
        overall = cliffs_delta(f.filter(pl.col("success"))[c], f.filter(~pl.col("success"))[c])
        within = [d for d in (cliffs_delta(f.filter((pl.col("code_module") == m) & pl.col("success"))[c],
                                           f.filter((pl.col("code_module") == m) & ~pl.col("success"))[c])
                              for m in modules) if d is not None]
        rows.append({"measure": c, "n": int(f[c].is_not_null().sum()), "cliffs_delta": overall,
                     "median_within_module": sorted(within)[len(within) // 2] if within else None,
                     "measured_over": "whole presentation" if c in FULL_WINDOW else "before or at the start" if c in
                     {"num_of_prev_attempts", "studied_credits", "date_registration", "imd_ord", "age_ord", "edu_ord"}
                     else "early window or first assessment"})
    return {"rows": sorted(rows, key=lambda r: -abs(r["cliffs_delta"] or 0))}


def registration_timing(f: pl.DataFrame) -> dict:
    """Registration day by outcome and outcome by registration band."""
    by_outcome = [{"final_result": o, **{f"p{q}": f.filter(pl.col("final_result") == o)["date_registration"]
                                         .quantile(q / 100, "nearest") for q in (10, 25, 50, 75, 90)}} for o in OUTCOMES]
    bands = f.with_columns(pl.when(pl.col("date_registration").is_null()).then(pl.lit("(missing)"))
                           .when(pl.col("date_registration") < -100).then(pl.lit("over 100 days early"))
                           .when(pl.col("date_registration") < -30).then(pl.lit("31-100 days early"))
                           .when(pl.col("date_registration") <= 0).then(pl.lit("0-30 days early"))
                           .otherwise(pl.lit("after day 0")).alias("band"))
    rows = []
    for band in ["over 100 days early", "31-100 days early", "0-30 days early", "after day 0", "(missing)"]:
        g = bands.filter(pl.col("band") == band)
        rows.append({"band": band, "n": g.height, "success": wilson(int(g["success"].sum()), g.height),
                     "withdrawn": wilson(int(g["withdrawn"].sum()), g.height)})
    return {"quantiles_by_outcome": by_outcome, "by_band": rows}


def repeat_transitions(f: pl.DataFrame) -> dict:
    """Students with several enrolments: outcome of one enrolment against the student's next one."""
    order = {"2013B": 0, "2013J": 1, "2014B": 2, "2014J": 3}
    e = (f.select(["id_student", "code_module", "code_presentation", "final_result", "num_of_prev_attempts"])
         .with_columns(pl.col("code_presentation").replace_strict(order).alias("t"))
         .sort(["id_student", "t", "code_module"]))
    nxt = e.with_columns([pl.col(c).shift(-1).over("id_student").alias(f"next_{c}")
                          for c in ("code_module", "t", "final_result", "num_of_prev_attempts")]).drop_nulls("next_t")
    concurrent = nxt.filter(pl.col("t") == pl.col("next_t"))
    seq = nxt.filter(pl.col("t") < pl.col("next_t"))
    same = seq.filter(pl.col("code_module") == pl.col("next_code_module"))
    table = (seq.group_by(["final_result", "next_final_result"]).len()
             .pivot(on="next_final_result", index="final_result", values="len").fill_null(0))
    return {"students_with_several_enrolments": e.group_by("id_student").len().filter(pl.col("len") > 1).height,
            "pairs_same_presentation_period": concurrent.height,
            "pairs_sequential": seq.height,
            "pairs_sequential_same_module": same.height,
            "same_module_next_attempt_count_increases": wilson(
                int((same["next_num_of_prev_attempts"] > same["num_of_prev_attempts"]).sum()), same.height),
            "same_module_after_withdrawn_or_fail_next_success": wilson(
                int(same.filter(pl.col("final_result").is_in(["Withdrawn", "Fail"]))["next_final_result"]
                    .is_in(["Pass", "Distinction"]).sum()),
                same.filter(pl.col("final_result").is_in(["Withdrawn", "Fail"])).height),
            "sequential_transitions": sorted(table.to_dicts(), key=lambda r: OUTCOMES.index(r["final_result"]))}


def course_design(t: dict[str, pl.DataFrame]) -> dict:
    """What each presentation offers: VLE sites by type, sites never used, click concentration across sites,
    assessment schedule."""
    vle, log, a = t["vle"], t["studentVle"], t["assessments"]
    site_clicks = log.group_by("id_site").agg(pl.col("sum_click").sum().alias("clicks"))
    sites = vle.join(site_clicks, on="id_site", how="left").with_columns(pl.col("clicks").fill_null(0))
    per_pres = (sites.group_by(PRESENTATION).agg(pl.len().alias("sites"), (pl.col("clicks") == 0).sum().alias("never_clicked"),
                                                 pl.col("activity_type").n_unique().alias("activity_types"))
                .sort(PRESENTATION))
    by_type = (sites.group_by("activity_type").agg(pl.len().alias("sites"), (pl.col("clicks") == 0).sum().alias("never_clicked"),
                                                   pl.col("clicks").sum().alias("clicks"))
               .with_columns((pl.col("never_clicked") / pl.col("sites")).round(4).alias("never_clicked_share"),
                             (pl.col("clicks") / pl.col("clicks").sum()).round(4).alias("click_share"))
               .sort("clicks", descending=True))
    sched = (a.filter(pl.col("assessment_type") != "Exam").group_by(PRESENTATION)
             .agg(pl.len().alias("tma_cma"), pl.col("date").min().alias("first_due"), pl.col("date").max().alias("last_due"))
             .sort(PRESENTATION))
    return {"sites_per_presentation": per_pres.to_dicts(), "by_activity_type": by_type.to_dicts(),
            "sites_never_clicked": wilson(int((sites["clicks"] == 0).sum()), sites.height),
            "site_click_concentration": concentration(sites["clicks"]),
            "assessment_schedule": sched.to_dicts()}


def main() -> None:
    t = load_all()
    f = read_features()
    write_json("segments.json", segments(t))
    res = {
        "definitions": {"early_window_days": [0, EARLY - 1], "success": "Pass or Distinction",
                        "active_at_28": "no unregistration day, or unregistration on day 28 or later",
                        "cliffs_delta": "P(successful > unsuccessful) - P(successful < unsuccessful)",
                        "min_cell_per_module": MIN_CELL},
        "univariate": univariate(f),
        "structure": structure_checks(t, f),
        "correlations": correlations(f),
        "outcome_by_dimension": outcome_by_dimension(f),
        "simpson": simpson(f),
        "early_engagement": early_engagement(f),
        "temporal": temporal(t, f),
        "survival": survival(f),
        "assessments": assessments(t, f),
        "activity_mix": activity_mix(t, f),
        "imd_missingness": imd_missingness(f),
        "signal_ranking": signal_ranking(f),
        "registration_timing": registration_timing(f),
        "repeat_transitions": repeat_transitions(f),
        "course_design": course_design(t),
    }
    write_json("descriptive.json", res)
    print("wrote results/descriptive.json; headline values:")
    e, s, o = res["early_engagement"], res["survival"], res["outcome_by_dimension"]
    print("  early engagement Cliff's delta:", e["cliffs_delta_success_vs_not"])
    print("  survival All:", s["survival_at"]["All"])
    print("  Cramer's V with final_result:", {k: v["cramers_v"] for k, v in o.items()})
    print("  Simpson (crude vs standardised, pp):",
          {k: (v["crude_gap_pp"], v["module_standardised_gap_pp"], v["modules_opposite_sign"]) for k, v in res["simpson"].items()})
    print("  temporal: median acf lag7", res["temporal"]["median_acf_lag7"], "assessment window ratio",
          res["temporal"]["median_assessment_window_ratio"])


if __name__ == "__main__":
    main()
