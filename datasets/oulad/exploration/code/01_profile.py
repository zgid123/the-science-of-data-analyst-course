"""Stage 1 - profile: structure, keys, per-column statistics, relationship and business-rule checks,
and the quality follow-ups quoted in the report (explore-data steps 2-5), on the full data.

Run from the repository root: venv/bin/python datasets/oulad/exploration/code/01_profile.py
Writes results/overview.json, columns.json, columns.csv, checks.json, followups.json.
"""

from __future__ import annotations

import json

import polars as pl

from common import ENROLMENT, GRAIN, PRESENTATION, RESULTS, ROLES, TABLES, load, write_json


def column_profile(table: str, raw: pl.DataFrame, df: pl.DataFrame) -> list[dict]:
    n = df.height
    rows = []
    for c in df.columns:
        role = ROLES[table][c]
        s = df[c]
        r = raw[c]
        prof = {
            "table": table, "column": c, "role": role, "rows": n,
            "empty_fields": int(r.is_null().sum() + (r == "").sum()),
            "question_mark": int((r == "?").sum()),
            "missing": int(s.null_count()),
            "missing_rate": round(s.null_count() / n, 6) if n else None,
            "distinct": int(s.n_unique()),
            "cardinality_ratio": round(s.n_unique() / n, 6) if n else None,
        }
        miss = prof["missing_rate"] or 0
        prof["completeness"] = ("complete" if miss < 0.01 else "mostly complete" if miss < 0.05
                                else "incomplete" if miss < 0.20 else "sparse")
        if s.dtype == pl.Float64 and not role.startswith("identifier"):
            v = s.drop_nulls()
            q = {f"p{p}": v.quantile(p / 100, "nearest") for p in (1, 5, 25, 50, 75, 95, 99)}
            prof.update({
                "min": v.min(), "max": v.max(), "mean": round(v.mean(), 4) if v.len() else None,
                "std": round(v.std(), 4) if v.len() > 1 else None, **q,
                "zeros": int((v == 0).sum()), "negatives": int((v < 0).sum()),
                "non_integer": int((v != v.floor()).sum()),
            })
            if prof["mean"] is not None and prof["p50"] not in (None, 0):
                prof["mean_to_median"] = round(prof["mean"] / prof["p50"], 3)
        if s.dtype == pl.String:
            v = s.drop_nulls()
            vc = v.value_counts(sort=True)
            prof["top_values"] = [[row[0], int(row[1])] for row in vc.head(10).iter_rows()]
            if vc.height > 10:
                prof["rare_values"] = [[row[0], int(row[1])] for row in vc.tail(5).iter_rows()]
            prof["whitespace_padded"] = int((v != v.str.strip_chars()).sum())
            lens = v.str.len_chars()
            prof["length_min_max"] = [lens.min(), lens.max()] if v.len() else None
        rows.append(prof)
    return rows


def table_overview(table: str, df: pl.DataFrame) -> dict:
    grain = GRAIN[table]
    out = {
        "table": table, "rows": df.height, "columns": df.width,
        "roles": {r: sum(1 for x in ROLES[table].values() if x.split(" ")[0] == r) for r in
                  sorted({x.split(" ")[0] for x in ROLES[table].values()})},
        "duplicate_full_rows": int(df.height - df.unique().height),
        "grain": grain,
    }
    if grain:
        out["grain_duplicates"] = int(df.height - df.unique(subset=grain).height)
    if all(c in df.columns for c in PRESENTATION):
        out["presentations"] = df.select(PRESENTATION).unique().height
    for c, role in ROLES[table].items():
        if role.startswith("temporal") and df[c].dtype == pl.Float64:
            out.setdefault("temporal_ranges", {})[c] = [df[c].min(), df[c].max()]
    return out


def check(name: str, value, expected: str, ok: bool, note: str = "") -> dict:
    return {"check": name, "observed": value, "expected": expected, "status": "PASS" if ok else "FLAG", "note": note}


def relationships(t: dict[str, pl.DataFrame]) -> list[dict]:
    """Referential integrity and cross-table/business-rule checks (explore-data steps 4-5)."""
    out = []

    def orphans(child: str, parent: str, keys: list[str], parent_keys: list[str] | None = None) -> int:
        pk = t[parent].select(parent_keys or keys).unique()
        pk.columns = keys
        return t[child].select(keys).unique().join(pk, on=keys, how="anti").height

    for child in ("assessments", "vle", "studentInfo", "studentRegistration", "studentVle"):
        n = orphans(child, "courses", PRESENTATION)
        out.append(check(f"{child} presentations exist in courses", n, "0 orphan presentations", n == 0))
    n = orphans("studentAssessment", "assessments", ["id_assessment"])
    out.append(check("studentAssessment.id_assessment exists in assessments", n, "0 orphan ids", n == 0))
    n = orphans("studentVle", "vle", ["id_site"])
    out.append(check("studentVle.id_site exists in vle", n, "0 orphan sites", n == 0))
    n = orphans("studentVle", "vle", PRESENTATION + ["id_site"])
    out.append(check("studentVle site belongs to the same presentation in vle", n, "0 mismatches", n == 0))

    info_keys = t["studentInfo"].select(ENROLMENT).unique()
    reg_keys = t["studentRegistration"].select(ENROLMENT).unique()
    a, b = info_keys.join(reg_keys, on=ENROLMENT, how="anti").height, reg_keys.join(info_keys, on=ENROLMENT, how="anti").height
    out.append(check("studentInfo and studentRegistration enrolments match 1:1", [a, b], "[0, 0]", a == 0 and b == 0))
    n = t["studentVle"].select(ENROLMENT).unique().join(info_keys, on=ENROLMENT, how="anti").height
    out.append(check("studentVle enrolments exist in studentInfo", n, "0", n == 0))
    sa = t["studentAssessment"].join(t["assessments"].select(["id_assessment"] + PRESENTATION), on="id_assessment")
    n = sa.select(ENROLMENT).unique().join(info_keys, on=ENROLMENT, how="anti").height
    out.append(check("studentAssessment enrolments (via assessment) exist in studentInfo", n, "0", n == 0))

    # enrolment coverage: who never appears in VLE / assessments
    n_enr = info_keys.height
    no_vle = info_keys.join(t["studentVle"].select(ENROLMENT).unique(), on=ENROLMENT, how="anti").height
    no_sub = info_keys.join(sa.select(ENROLMENT).unique(), on=ENROLMENT, how="anti").height
    out.append(check("enrolments with no VLE activity", [no_vle, round(no_vle / n_enr, 4)], "informational", True))
    out.append(check("enrolments with no assessment submission", [no_sub, round(no_sub / n_enr, 4)], "informational", True))

    # business rules
    reg = t["studentRegistration"].join(t["studentInfo"].select(ENROLMENT + ["final_result"]), on=ENROLMENT)
    wd = reg.filter(pl.col("final_result") == "Withdrawn")
    out.append(check("Withdrawn enrolments without date_unregistration", wd["date_unregistration"].null_count(),
                     "0", wd["date_unregistration"].null_count() == 0, f"of {wd.height:,} Withdrawn"))
    not_wd = reg.filter((pl.col("final_result") != "Withdrawn") & pl.col("date_unregistration").is_not_null())
    out.append(check("non-Withdrawn enrolments with a date_unregistration", not_wd.height, "0", not_wd.height == 0,
                     str(not_wd["final_result"].value_counts().rows()) if not_wd.height else ""))
    bad = reg.filter(pl.col("date_unregistration") < pl.col("date_registration")).height
    out.append(check("unregistration before registration", bad, "0", bad == 0))
    unreg_before_start = reg.filter(pl.col("date_unregistration") <= 0).height
    out.append(check("unregistered on or before day 0", unreg_before_start, "informational", True,
                     "withdrew before the presentation started"))

    sc = t["studentAssessment"]["score"]
    out.append(check("score within 0-100", int(((sc < 0) | (sc > 100)).sum()), "0", int(((sc < 0) | (sc > 100)).sum()) == 0))
    out.append(check("submissions with missing score", sc.null_count(), "informational", True))
    banked = t["studentAssessment"].filter(pl.col("is_banked") == 1).height
    out.append(check("banked assessment results (carried from earlier attempt)", banked, "informational", True))

    late = sa.join(t["assessments"].select(["id_assessment", "date"]), on="id_assessment").filter(
        pl.col("date").is_not_null())
    n_late = late.filter(pl.col("date_submitted") > pl.col("date")).height
    out.append(check("submissions after the assessment's due day", [n_late, round(n_late / late.height, 4)],
                     "informational", True, "assessments with a due day only"))
    out.append(check("assessments without a due day (date missing)", t["assessments"]["date"].null_count(),
                     "informational", True, str(t["assessments"].filter(pl.col("date").is_null())["assessment_type"].value_counts().rows())))

    w = t["assessments"].group_by(PRESENTATION + ["assessment_type"]).agg(pl.col("weight").sum().alias("w"))
    exam = w.filter(pl.col("assessment_type") == "Exam")
    non_exam = w.filter(pl.col("assessment_type") != "Exam").group_by(PRESENTATION).agg(pl.col("w").sum())
    out.append(check("exam weight per presentation", sorted(set(exam["w"].to_list())), "100", set(exam["w"].to_list()) <= {100.0}))
    out.append(check("TMA+CMA weight per presentation", sorted(set(non_exam["w"].to_list())), "100",
                     set(non_exam["w"].to_list()) <= {100.0}, "presentations not summing to 100: "
                     + str(non_exam.filter(pl.col("w") != 100).sort(PRESENTATION).rows())))

    length = t["courses"].select(PRESENTATION + ["module_presentation_length"])
    vle_days = t["studentVle"].group_by(PRESENTATION).agg(pl.col("date").min().alias("first"), pl.col("date").max().alias("last")).join(length, on=PRESENTATION)
    beyond = vle_days.filter(pl.col("last") > pl.col("module_presentation_length")).height
    out.append(check("VLE activity after the presentation length", beyond, "0", beyond == 0))
    out.append(check("VLE activity before day 0 (pre-start)", int((t["studentVle"]["date"] < 0).sum()), "informational", True))

    rep = t["studentVle"].group_by(ENROLMENT + ["id_site", "date"]).len().filter(pl.col("len") > 1)
    out.append(check("studentVle rows repeating (enrolment, site, day)", [rep.height, int(rep["len"].sum())],
                     "informational", True, "log has several rows per student-site-day; aggregate sum_click before use"))

    multi = t["studentInfo"].group_by("id_student").len().filter(pl.col("len") > 1).height
    out.append(check("students enrolled in more than one presentation", multi, "informational", True))
    return out


def followups(t: dict[str, pl.DataFrame]) -> dict:
    """Follow-up measurements behind the report's issue table (Section 3) and highlights (Section 4)."""
    vle = t["studentVle"]
    keys = ENROLMENT + ["id_site", "date", "sum_click"]
    groups = vle.group_by(keys).len()
    dup = groups.filter(pl.col("len") > 1)
    clicks_raw = int(vle["sum_click"].sum())
    clicks_collapsed = int(groups["sum_click"].sum())
    si, reg = t["studentInfo"], t["studentRegistration"]
    withdrawn = si.filter(pl.col("final_result") == "Withdrawn").join(reg, on=ENROLMENT)
    sub = (t["studentAssessment"]
           .join(t["assessments"].select(["id_assessment", "assessment_type"] + PRESENTATION), on="id_assessment")
           .join(t["courses"], on=PRESENTATION))
    post_end = sub.filter(pl.col("date_submitted") > pl.col("module_presentation_length"))
    imd = si["imd_band"].drop_nulls().unique().sort().to_list()
    return {
        "duplicate_click_impact": {
            "duplicated_groups": dup.height,
            "extra_rows": int((dup["len"] - 1).sum()),
            "extra_row_share": round(int((dup["len"] - 1).sum()) / vle.height, 5),
            "single_click_groups": int((dup["sum_click"] == 1).sum()),
            "single_click_group_share": round(int((dup["sum_click"] == 1).sum()) / dup.height, 4),
            "clicks_raw": clicks_raw,
            "clicks_exact_duplicates_collapsed": clicks_collapsed,
            "clicks_share_removed": round(1 - clicks_collapsed / clicks_raw, 5),
        },
        "withdrawn_unregistration": {
            "withdrawn": withdrawn.height,
            "with_date_unregistration": int(withdrawn["date_unregistration"].is_not_null().sum()),
        },
        "submissions_after_presentation_end": {
            "count": post_end.height,
            "max_date_submitted": post_end["date_submitted"].max(),
            "by_assessment_type": dict(post_end["assessment_type"].value_counts().rows()),
            "by_is_banked": {str(k): v for k, v in post_end["is_banked"].value_counts().rows()},
        },
        "imd_band_labels": imd,
        "imd_band_labels_without_percent": [x for x in imd if not x.endswith("%")],
        "vle_sites_with_week_from": int(t["vle"]["week_from"].is_not_null().sum()),
        "first_attempt_share": round(float((si["num_of_prev_attempts"] == 0).mean()), 4),
        "activity_after_unregistration": after_unregistration(t),
        "score_heaping": score_heaping(t),
    }


def after_unregistration(t: dict[str, pl.DataFrame]) -> dict:
    """Cross-table consistency: clicks and submissions dated after the enrolment's unregistration day."""
    reg = t["studentRegistration"].drop_nulls("date_unregistration").select(ENROLMENT + ["date_unregistration"])
    clicks = t["studentVle"].join(reg, on=ENROLMENT).filter(pl.col("date") > pl.col("date_unregistration"))
    subs = (t["studentAssessment"].join(t["assessments"].select(["id_assessment"] + PRESENTATION), on="id_assessment")
            .join(reg, on=ENROLMENT).filter(pl.col("date_submitted") > pl.col("date_unregistration")))
    return {"unregistered_enrolments": reg.height,
            "click_rows_after": clicks.height, "clicks_after": int(clicks["sum_click"].sum()),
            "enrolments_with_clicks_after": clicks.select(ENROLMENT).unique().height,
            "max_days_after_click": (clicks["date"] - clicks["date_unregistration"]).max(),
            "submissions_after": subs.height,
            "enrolments_with_submissions_after": subs.select(ENROLMENT).unique().height}


def score_heaping(t: dict[str, pl.DataFrame]) -> dict:
    """Round-number bias: share of scores on multiples of 10 and 5, and heaping index (count at a multiple of 10
    divided by the mean count at its two neighbours) by assessment type; banked results excluded."""
    sc = (t["studentAssessment"].filter(pl.col("is_banked") == 0).drop_nulls("score")
          .join(t["assessments"].select(["id_assessment", "assessment_type"]), on="id_assessment"))
    out = {}
    for typ in sorted(sc["assessment_type"].unique()):
        v = sc.filter(pl.col("assessment_type") == typ)["score"]
        counts = dict(v.value_counts().rows())
        idx = [counts.get(m, 0) / ((counts.get(m - 1, 0) + counts.get(m + 1, 0)) / 2)
               for m in range(10, 100, 10) if counts.get(m - 1, 0) + counts.get(m + 1, 0)]
        out[typ] = {"n": v.len(), "non_integer": int((v != v.floor()).sum()),
                    "share_multiple_of_10": round(float((v % 10 == 0).mean()), 4),
                    "share_multiple_of_5": round(float((v % 5 == 0).mean()), 4),
                    "median_heaping_index_10_to_90": round(sorted(idx)[len(idx) // 2], 3) if idx else None,
                    "distinct_values": v.n_unique()}
    return out


def main() -> None:
    raw_and_typed = {table: load(table) for table in TABLES}
    typed = {table: df for table, (_, df) in raw_and_typed.items()}
    overviews, columns = [], []
    for table, (raw, df) in raw_and_typed.items():
        overviews.append(table_overview(table, df))
        columns += column_profile(table, raw, df)
        print(f"profiled {table}: {df.height:,} rows")
    rel = relationships(typed)
    fol = followups(typed)
    write_json("overview.json", overviews)
    write_json("columns.json", columns)
    write_json("checks.json", rel)
    write_json("followups.json", fol)
    flat = [{k: v for k, v in c.items() if not isinstance(v, list)} for c in columns]
    pl.DataFrame(flat, infer_schema_length=None).write_csv(RESULTS / "columns.csv")
    print(f"checks: {sum(r['status'] == 'FLAG' for r in rel)} flagged of {len(rel)}")
    print("followups:", json.dumps(fol, default=str))


if __name__ == "__main__":
    main()
