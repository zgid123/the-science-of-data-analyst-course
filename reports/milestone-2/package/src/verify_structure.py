"""Initial structural verification of the collected OULAD files (brief section 10, Task 6).

Usage (from the package folder, after src/collect.py):
    python src/verify_structure.py

Reads every table in data/raw/ as text (no type coercion, nothing changed) and records, per table: rows, columns,
headers against data/metadata/data_dictionary.md, key uniqueness, inferred types, missing values, and the value ranges of
the target and time fields. It then checks the conditions the dataset selection depends on (G1 result values, G3 runs
per module, G5 identifier persistence, assessed tasks due in weeks 1–4, unregistration on or before day 0,
registration after day 14). This is a structural check, not an exploratory analysis: no row is dropped, cleaned,
imputed or transformed. Writes data/metadata/structure_report.md and metadata/structure_results.json.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import polars as pl

PKG = Path(__file__).resolve().parents[1]
RAW = PKG / "data" / "raw"
META = PKG / "data" / "metadata"
TABLES = ["courses", "assessments", "vle", "studentInfo", "studentRegistration", "studentAssessment", "studentVle"]
KEYS = {
    "courses": ["code_module", "code_presentation"],
    "assessments": ["id_assessment"],
    "vle": ["id_site"],
    "studentInfo": ["code_module", "code_presentation", "id_student"],
    "studentRegistration": ["code_module", "code_presentation", "id_student"],
    "studentAssessment": ["id_assessment", "id_student"],
    "studentVle": None,  # no documented key: one row per logged interaction
}
TIME_FIELDS = {"courses": ["module_presentation_length", "length"], "assessments": ["date"],
               "studentRegistration": ["date_registration", "date_unregistration"],
               "studentAssessment": ["date_submitted"], "studentVle": ["date"], "vle": ["week_from", "week_to"]}


def documented():
    cols = {}
    for line in (META / "data_dictionary.md").read_text().splitlines():
        m = re.match(r"\| (\w+) \| (\w+) \|", line)
        if m and m.group(1) in TABLES:
            cols.setdefault(m.group(1), []).append(m.group(2))
    return cols


def infer(s: pl.Series) -> str:
    v = s.drop_nulls()
    if v.len() == 0:
        return "empty"
    if v.str.contains(r"^-?\d+$").all():
        return "integer"
    if v.str.contains(r"^-?\d+(\.\d+)?$").all():
        return "decimal"
    return "text"


def main():
    doc = documented()
    res, md = {}, []
    frames = {}
    for t in TABLES:
        df = pl.read_csv(RAW / f"{t}.csv", infer_schema_length=0)  # every column read as text
        df = df.with_columns([pl.when(pl.col(c).str.strip_chars() == "").then(None).otherwise(pl.col(c)).alias(c)
                              for c in df.columns])
        frames[t] = df
        key = KEYS[t]
        dup_key = None if key is None else int(df.height - df.select(key).unique().height)
        exact_dup = int(df.height - df.unique().height)
        missing = {c: int(df[c].null_count()) for c in df.columns if df[c].null_count()}
        types = {c: infer(df[c]) for c in df.columns}
        undocumented = [c for c in df.columns if c not in doc.get(t, [])]
        not_in_file = [c for c in doc.get(t, []) if c not in df.columns]
        ranges = {}
        for c in TIME_FIELDS.get(t, []):
            if c in df.columns:
                v = df[c].drop_nulls().cast(pl.Int64)
                ranges[c] = [int(v.min()), int(v.max())] if v.len() else None
        res[t] = {"rows": df.height, "columns": df.width, "headers": df.columns, "key": key,
                  "duplicate_keys": dup_key, "exact_duplicate_rows": exact_dup, "missing": missing, "types": types,
                  "columns_not_documented": undocumented, "documented_not_in_file": not_in_file, "time_ranges": ranges}

    si, sr, a, sa, c = (frames[k] for k in ["studentInfo", "studentRegistration", "assessments",
                                            "studentAssessment", "courses"])
    enrol = ["code_module", "code_presentation", "id_student"]
    checks = {}
    # target: values and distribution
    checks["final_result_values"] = {r[0]: r[1] for r in si.group_by("final_result").len().sort("len", descending=True).iter_rows()}
    # G1: dated withdrawal
    j = si.join(sr, on=enrol, how="left")
    wd = j.filter(pl.col("final_result") == "Withdrawn")
    checks["withdrawn_with_date"] = int(wd["date_unregistration"].is_not_null().sum())
    checks["withdrawn_without_date"] = int(wd["date_unregistration"].is_null().sum())
    checks["date_but_not_withdrawn"] = int(j.filter((pl.col("final_result") != "Withdrawn")
                                                    & pl.col("date_unregistration").is_not_null()).height)
    checks["studentInfo_registration_match"] = int(si.join(sr, on=enrol, how="anti").height) == 0 and \
        int(sr.join(si, on=enrol, how="anti").height) == 0
    # G3: runs per module, B and J separately, ordered by year
    runs = c.with_columns(pl.col("code_presentation").str.slice(0, 4).alias("year"),
                          pl.col("code_presentation").str.slice(4, 1).alias("start"))
    per = runs.group_by(["code_module", "start"]).agg(pl.col("code_presentation").sort().alias("runs"))
    checks["runs_per_module"] = {f"{m}-{s}": r for m, s, r in per.sort(["code_module", "start"]).iter_rows()}
    allruns = runs.group_by("code_module").agg(pl.col("code_presentation").sort().alias("runs"))
    checks["runs_per_module_all"] = {m: r for m, r in allruns.sort("code_module").iter_rows()}
    # G5: same identifier across runs, and consistency with the attempt counter
    multi = si.group_by("id_student").agg(pl.len().alias("n"), pl.col("code_module").n_unique().alias("modules"))
    checks["students_total"] = int(multi.height)
    checks["students_in_more_than_one_run"] = int(multi.filter(pl.col("n") > 1).height)
    rep = (si.with_columns(pl.col("num_of_prev_attempts").cast(pl.Int64))
             .sort(["id_student", "code_module", "code_presentation"])
             .with_columns(pl.col("num_of_prev_attempts").shift(1).over(["id_student", "code_module"]).alias("prev"))
             .filter(pl.col("prev").is_not_null()))
    checks["same_module_repeats"] = int(rep.height)
    checks["repeats_with_higher_attempt_counter"] = int((rep["num_of_prev_attempts"] > rep["prev"]).sum())
    # tasks due in weeks 1-4 (non-exam tasks with a cut-off day)
    nx = a.filter((pl.col("assessment_type") != "Exam") & pl.col("date").is_not_null()).with_columns(pl.col("date").cast(pl.Int64))
    first = nx.group_by(["code_module", "code_presentation"]).agg(pl.col("date").min().alias("first_due"))
    checks["first_task_due_day"] = {f"{m}-{p}": d for m, p, d in first.sort(["code_module", "code_presentation"]).iter_rows()}
    checks["runs_with_task_due_by_day_13"] = int((first["first_due"] <= 13).sum())
    checks["runs_with_task_due_by_day_27"] = int((first["first_due"] <= 27).sum())
    checks["exams_without_cutoff_day"] = int(a.filter((pl.col("assessment_type") == "Exam") & pl.col("date").is_null()).height)
    # denominator: unregistration on or before day 0, registration after day 14
    srd = sr.with_columns(pl.col("date_registration").cast(pl.Int64), pl.col("date_unregistration").cast(pl.Int64))
    checks["unregistered_on_or_before_day_0"] = int(srd.filter(pl.col("date_unregistration") <= 0).height)
    checks["registered_after_day_14"] = int(srd.filter(pl.col("date_registration") > 14).height)
    checks["registration_day_missing"] = int(srd["date_registration"].null_count())
    checks["still_registered_at_day_14"] = int(srd.filter((pl.col("date_unregistration").is_null())
                                                          | (pl.col("date_unregistration") > 14)).height)
    # referential links used by the AQs
    checks["assessment_rows_without_parent"] = int(sa.join(a, on="id_assessment", how="anti").height)
    checks["submissions_without_enrolment"] = int(sa.join(a.select(["id_assessment", "code_module", "code_presentation"]),
                                                          on="id_assessment").join(si, on=enrol, how="anti").height)
    v = frames["studentVle"]
    checks["click_rows_without_enrolment"] = int(v.select(enrol).unique().join(si, on=enrol, how="anti").height)
    checks["click_rows_without_site"] = int(v.select("id_site").unique().join(frames["vle"], on="id_site", how="anti").height)

    out = {"generated": f"{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ}", "tables": res, "checks": checks}
    (META / "structure_results.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))

    md.append("# Initial structural verification (Task 6)\n")
    md.append(f"Generated {out['generated']} by `src/verify_structure.py` from `data/raw/` (files read as text, nothing changed).\n")
    md.append("| File | Rows | Columns | Key(s) | Duplicate keys | Exact duplicate rows | Time fields (min–max day) | Headers not in the dictionary | Dictionary columns not in file |")
    md.append("| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |")
    for t, r in res.items():
        tr = "; ".join(f"{k} {v[0]}–{v[1]}" for k, v in r["time_ranges"].items() if v) or "–"
        md.append(f"| {t}.csv | {r['rows']:,} | {r['columns']} | {', '.join(r['key']) if r['key'] else 'none documented'} | "
                  f"{'–' if r['duplicate_keys'] is None else r['duplicate_keys']} | {r['exact_duplicate_rows']:,} | {tr} | "
                  f"{', '.join(r['columns_not_documented']) or '–'} | {', '.join(r['documented_not_in_file']) or '–'} |")
    md.append("\n## Missing values (empty cells, by column)\n")
    md.append("| File | Column | Missing |\n| :---- | :---- | :---- |")
    for t, r in res.items():
        for col, n in r["missing"].items():
            md.append(f"| {t}.csv | {col} | {n:,} |")
    md.append("\n## Inferred types\n")
    for t, r in res.items():
        md.append(f"- {t}.csv: " + ", ".join(f"{k} ({v})" for k, v in r["types"].items()))
    md.append("\n## Selection conditions and denominators\n")
    md.append("```json\n" + json.dumps(checks, indent=1) + "\n```")
    (META / "structure_report.md").write_text("\n".join(md) + "\n")
    print(json.dumps({t: [r["rows"], r["columns"], r["duplicate_keys"], r["exact_duplicate_rows"]] for t, r in res.items()}))
    print(json.dumps(checks, indent=1))


if __name__ == "__main__":
    main()
