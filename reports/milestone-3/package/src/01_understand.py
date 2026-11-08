"""Task 1 – understand the structure and meaning of the data (brief section 6), before any profiling or change.

For each table the script computes what the Dataset Understanding Map states: unit of analysis, primary key and its
uniqueness, foreign keys with their coverage and cardinality (1–1, 1–N), main variables, time fields and the role in
the analytical questions. It then checks the semantics the report relies on against the data: population (modules,
runs, start months, years), outcome and when it is observed, the meaning of each day field, measurement units
(clicks, scores, weights, credits), categorical codes and the sensitive attributes with their group sizes.

Usage (from the package folder): python src/01_understand.py
Writes data/metadata/understanding.json and data/metadata/understanding_map.md. Reads data/raw only.
"""
from __future__ import annotations

import polars as pl

from common import (AGE, EDU, ENROLMENT, IMD, KEYS, META, OUTCOMES, RUN, SENSITIVE, TABLES, load, load_text,
                    md_table, now_utc, scan, write_json)

UNIT = {
    "courses": "module run (module × presentation)",
    "assessments": "assessment of a module run",
    "vle": "learning-platform resource (site) of a module run",
    "studentInfo": "enrolment (student × module run)",
    "studentRegistration": "enrolment (student × module run)",
    "studentAssessment": "submission (student × assessment)",
    "studentVle": "logged interaction record (student × resource × day; several rows per day possible)",
}
FK = {
    "courses": "–",
    "assessments": "code_module, code_presentation → courses",
    "vle": "code_module, code_presentation → courses",
    "studentInfo": "code_module, code_presentation → courses",
    "studentRegistration": "code_module, code_presentation, id_student → studentInfo (1–1)",
    "studentAssessment": "id_assessment → assessments; id_student (+ run of the assessment) → studentInfo",
    "studentVle": "id_site → vle; code_module, code_presentation, id_student → studentInfo",
}
MAIN = {
    "courses": "module_presentation_length",
    "assessments": "assessment_type, weight",
    "vle": "activity_type",
    "studentInfo": "final_result, gender, region, highest_education, imd_band, age_band, num_of_prev_attempts, "
                   "studied_credits, disability",
    "studentRegistration": "date_registration, date_unregistration",
    "studentAssessment": "score, is_banked",
    "studentVle": "sum_click",
}
TIME = {
    "courses": "module_presentation_length (days)",
    "assessments": "date (due day)",
    "vle": "week_from, week_to (planned weeks)",
    "studentInfo": "– (final_result observed at run end)",
    "studentRegistration": "date_registration, date_unregistration (days)",
    "studentAssessment": "date_submitted (day)",
    "studentVle": "date (day of interaction)",
}
ROLE = {
    "courses": "Run length; run end for exam due days (AQ1–AQ3)",
    "assessments": "Due days of tasks: missed and late tasks (AQ1, AQ2), task-based features and baseline rule (AQ3)",
    "vle": "Resource type of clicks (AQ2 activity mix); planned weeks rarely filled",
    "studentInfo": "Outcome and target (AQ1–AQ3); background and audit attributes (AQ2, AQ3, AQ4 fairness)",
    "studentRegistration": "KPI denominator (registered on day 14), withdrawal day, population at each cut-off",
    "studentAssessment": "Submission and lateness (AQ1, AQ2, AQ3)",
    "studentVle": "Platform activity by day and week (AQ2, AQ3)",
}


def key_unique(df, key):
    return df.height == df.unique(subset=key).height


def cardinality(child: pl.DataFrame, parent: pl.DataFrame, on: list[str]) -> dict:
    """Coverage of a foreign key: orphans in the child, parents without children, children per parent."""
    per = child.group_by(on).len()
    orphans = child.join(parent.select(on).unique(), on=on, how="anti").height
    childless = parent.select(on).unique().join(per.select(on), on=on, how="anti").height
    return {"orphan_rows": orphans, "parents_without_children": childless,
            "children_per_parent_min": int(per["len"].min()), "children_per_parent_max": int(per["len"].max())}


def main():
    t = {name: load(name) for name in TABLES if name != "studentVle"}
    sv = scan("studentVle")
    out: dict = {"generated": now_utc(), "tables": {}}

    # --- table level: rows, columns, key uniqueness
    sv_rows = sv.select(pl.len()).collect().item()
    sv_cols = len(sv.collect_schema())
    for name in TABLES:
        rows = sv_rows if name == "studentVle" else t[name].height
        cols = sv_cols if name == "studentVle" else t[name].width
        key = KEYS[name]
        uniq = None if key is None else key_unique(t[name], key)
        out["tables"][name] = {"rows": rows, "columns": cols, "unit": UNIT[name],
                               "primary_key": ", ".join(key) if key else "none documented",
                               "key_unique": uniq, "foreign_keys": FK[name], "main_variables": MAIN[name],
                               "time_fields": TIME[name], "role_in_aq": ROLE[name]}

    # --- relationships and cardinality
    info, reg, asm, sa, vle, crs = (t["studentInfo"], t["studentRegistration"], t["assessments"],
                                    t["studentAssessment"], t["vle"], t["courses"])
    sa_run = sa.join(asm.select(["id_assessment", *RUN]), on="id_assessment", how="left")
    sv_enrol = sv.select(ENROLMENT).unique().collect()
    sv_site = sv.select("id_site").unique().collect()
    rel = {
        "courses→assessments": cardinality(asm, crs, RUN),
        "courses→vle": cardinality(vle, crs, RUN),
        "courses→studentInfo": cardinality(info, crs, RUN),
        "studentInfo↔studentRegistration": {
            "info_without_registration": info.join(reg, on=ENROLMENT, how="anti").height,
            "registration_without_info": reg.join(info, on=ENROLMENT, how="anti").height},
        "assessments→studentAssessment": cardinality(sa, asm, ["id_assessment"]),
        "studentInfo→studentAssessment (enrolment)": {
            "orphan_rows": sa_run.join(info, on=ENROLMENT, how="anti").height,
            "enrolments_with_submissions": sa_run.select(ENROLMENT).unique().height},
        "vle→studentVle": {"orphan_sites": sv_site.join(vle, on="id_site", how="anti").height,
                           "sites_never_used": vle.join(sv_site, on="id_site", how="anti").height},
        "studentInfo→studentVle (enrolment)": {
            "orphan_enrolments": sv_enrol.join(info, on=ENROLMENT, how="anti").height,
            "enrolments_with_activity": sv_enrol.height,
            "enrolments_without_activity": info.join(sv_enrol, on=ENROLMENT, how="anti").height},
    }
    out["relationships"] = rel

    # --- population
    runs = crs.with_columns(pl.col("code_presentation").str.slice(0, 4).alias("year"),
                            pl.col("code_presentation").str.slice(4, 1).alias("start_month"))
    per_student = info.group_by("id_student").len()
    out["population"] = {
        "modules": sorted(crs["code_module"].unique().to_list()),
        "runs": runs.height,
        "runs_by_year": runs.group_by("year").len().sort("year").rows(),
        "runs_by_start_month": runs.group_by("start_month").len().sort("start_month").rows(),
        "runs_per_module": runs.group_by("code_module").len().sort("code_module").rows(),
        "run_length_days": [int(crs["module_presentation_length"].min()), int(crs["module_presentation_length"].max())],
        "enrolments": info.height,
        "students": per_student.height,
        "students_with_several_enrolments": per_student.filter(pl.col("len") > 1).height,
        "enrolments_per_run": [int(info.group_by(RUN).len()["len"].min()), int(info.group_by(RUN).len()["len"].max())],
    }

    # --- outcome semantics: final_result against the withdrawal day
    fr = info.join(reg, on=ENROLMENT).join(crs, on=RUN)
    out["outcome"] = {
        "values": fr.group_by("final_result").len().sort("len", descending=True).rows(),
        "withdrawn_without_unregistration_day": fr.filter((pl.col("final_result") == "Withdrawn")
                                                          & pl.col("date_unregistration").is_null()).height,
        "not_withdrawn_with_unregistration_day": fr.filter((pl.col("final_result") != "Withdrawn")
                                                           & pl.col("date_unregistration").is_not_null())
                                                   .group_by("final_result").len().rows(),
        "unregistration_on_or_before_day0": fr.filter(pl.col("date_unregistration") <= 0).height,
        "unregistration_after_run_end": fr.filter(pl.col("date_unregistration")
                                                  > pl.col("module_presentation_length")).height,
        "unregistration_before_registration": fr.filter(pl.col("date_unregistration")
                                                        < pl.col("date_registration")).height,
    }

    # --- time semantics
    asm_r = asm.join(crs, on=RUN)
    sa_d = sa.join(asm.select(["id_assessment", "assessment_type", "date"]), on="id_assessment")
    banked = sa_d.filter(pl.col("is_banked") == 1)
    sv_days = sv.select(pl.col("date").min().alias("min"), pl.col("date").max().alias("max"),
                        (pl.col("date") < 0).sum().alias("before_day0")).collect()
    sv_after_end = (sv.join(crs.lazy(), on=RUN).filter(pl.col("date") > pl.col("module_presentation_length"))
                    .select(pl.len()).collect().item())
    out["time"] = {
        "day_zero": "start of the module run; all day fields are offsets from it (negative = before the start)",
        "registration_day_range": [int(reg["date_registration"].min()), int(reg["date_registration"].max())],
        "registration_after_day14": reg.filter(pl.col("date_registration") > 14).height,
        "registration_missing": reg["date_registration"].null_count(),
        "assessment_due_range": [int(asm["date"].min()), int(asm["date"].max())],
        "assessments_without_due_day": asm.filter(pl.col("date").is_null()).group_by("assessment_type").len().rows(),
        "due_after_run_end": asm_r.filter(pl.col("date") > pl.col("module_presentation_length")).height,
        "submission_day_range": [int(sa["date_submitted"].min()), int(sa["date_submitted"].max())],
        "banked_submissions": banked.height,
        "banked_submission_day_range": [int(banked["date_submitted"].min()), int(banked["date_submitted"].max())],
        "banked_submitted_after_due": banked.filter(pl.col("date_submitted") > pl.col("date")).height,
        "interaction_day_range": [int(sv_days["min"][0]), int(sv_days["max"][0])],
        "interaction_rows_before_day0": int(sv_days["before_day0"][0]),
        "interaction_rows_after_run_end": sv_after_end,
        "vle_sites_with_planned_week": vle.filter(pl.col("week_from").is_not_null()).height,
        "vle_planned_week_max": int(vle["week_to"].max()),
    }

    # --- measurement semantics
    w = asm.group_by([*RUN, "assessment_type"]).agg(pl.col("weight").sum().alias("w"), pl.len().alias("n"))
    clicks = sv.select(pl.col("sum_click").min().alias("min"), pl.col("sum_click").median().alias("median"),
                       pl.col("sum_click").max().alias("max"), pl.col("sum_click").sum().alias("total")).collect()
    out["measurement"] = {
        "sum_click_per_row": {k: float(clicks[k][0]) for k in clicks.columns},
        "score_range": [float(sa["score"].min()), float(sa["score"].max())],
        "score_non_integer": sa.filter(pl.col("score") != pl.col("score").round(0)).height,
        "score_missing": sa["score"].null_count(),
        "weights_by_type": w.group_by("assessment_type").agg(pl.col("w").unique().sort().alias("sums"))
                            .sort("assessment_type").rows(),
        "runs_with_zero_coursework_total": w.filter(pl.col("assessment_type") != "Exam").group_by(RUN)
                                            .agg(pl.col("w").sum()).filter(pl.col("w") == 0).select(RUN)
                                            .sort(RUN).rows(),
        "run_types_with_zero_weight": w.filter((pl.col("assessment_type") != "Exam") & (pl.col("w") == 0))
                                       .select([*RUN, "assessment_type"]).sort(RUN).rows(),
        "runs_with_two_exams": w.filter((pl.col("assessment_type") == "Exam") & (pl.col("n") > 1))
                                .select(RUN).sort(RUN).rows(),
        "assessments_by_type": asm.group_by("assessment_type").len().sort("assessment_type").rows(),
        "studied_credits_range": [int(info["studied_credits"].min()), int(info["studied_credits"].max())],
        "studied_credits_top": info.group_by("studied_credits").len().sort("len", descending=True).head(5).rows(),
        "num_of_prev_attempts_range": [int(info["num_of_prev_attempts"].min()),
                                       int(info["num_of_prev_attempts"].max())],
    }

    # --- categorical codes (raw text, so labels are seen exactly as stored)
    txt = load_text("studentInfo")
    codes = {}
    for c in ["gender", "region", "highest_education", "imd_band", "age_band", "disability", "final_result"]:
        codes[c] = txt.group_by(c).len().sort("len", descending=True).rows()
    codes["code_presentation"] = load_text("courses").group_by("code_presentation").len().sort("code_presentation").rows()
    codes["assessment_type"] = load_text("assessments").group_by("assessment_type").len().sort("assessment_type").rows()
    codes["activity_type"] = load_text("vle").group_by("activity_type").len().sort("len", descending=True).rows()
    expected = {"imd_band": IMD, "age_band": AGE, "highest_education": EDU, "final_result": OUTCOMES}
    codes["labels_outside_expected_order"] = {
        c: sorted({v for v, _ in codes[c] if v not in exp}) for c, exp in expected.items()}
    out["codes"] = codes

    # --- sensitive attributes: groups and the smallest group per module run (fairness audit feasibility)
    sens = {}
    for c in SENSITIVE:
        groups = info.group_by(c).len().sort("len")
        per_run = info.group_by([*RUN, c]).len()
        sens[c] = {"groups": groups.height, "smallest_group": groups.row(0), "largest_group": groups.row(-1),
                   "run_groups_below_20": per_run.filter(pl.col("len") < 20).height}
    out["sensitive"] = sens

    write_json(META / "understanding.json", out)

    # --- Dataset Understanding Map (brief section 6.1)
    rows = [{"File/Table": f"{n}.csv", "Unit of Analysis": v["unit"], "Primary Key":
             f"{v['primary_key']} ({'unique' if v['key_unique'] else 'not unique' if v['key_unique'] is False else 'no key'})",
             "Foreign Key": v["foreign_keys"], "Main Variables": v["main_variables"], "Time Field": v["time_fields"],
             "Role in AQ": v["role_in_aq"], "Rows": f"{v['rows']:,}"} for n, v in out["tables"].items()]
    md = ["# Dataset Understanding Map (Task 1)", f"Generated {out['generated']} by `src/01_understand.py` from "
          "`data/raw/`. Every key and relationship below is a computed check; full results in `understanding.json`.",
          md_table(rows, ["File/Table", "Rows", "Unit of Analysis", "Primary Key", "Foreign Key", "Main Variables",
                          "Time Field", "Role in AQ"]),
          "## Relationships", md_table([{"Relationship": k, **{"Result": ", ".join(f"{a}={b}" for a, b in v.items())}}
                                        for k, v in rel.items()])]
    (META / "understanding_map.md").write_text("\n\n".join(md) + "\n")

    p = out["population"]
    print(f"tables: {len(out['tables'])}; keys unique: "
          f"{sum(1 for v in out['tables'].values() if v['key_unique'])} of 6 keyed tables")
    print(f"population: {p['runs']} runs, {len(p['modules'])} modules, {p['enrolments']:,} enrolments, "
          f"{p['students']:,} students ({p['students_with_several_enrolments']:,} with several enrolments)")
    for k, v in rel.items():
        print(f"  {k}: {v}")
    for k in ("outcome", "time", "measurement"):
        print(k, {a: b for a, b in out[k].items() if not isinstance(b, list) or len(b) < 8})
    print("labels outside expected order:", codes["labels_outside_expected_order"])
    print("sensitive:", {c: (v["groups"], v["smallest_group"], v["run_groups_below_20"]) for c, v in sens.items()})


if __name__ == "__main__":
    main()
