"""Shared definitions for the OULAD exploration scripts: paths, keys, column roles, category orders, loader.

Imported by the numbered stage scripts in this folder; holds no analysis.
"""

from __future__ import annotations

import json
from pathlib import Path

import polars as pl

HERE = Path(__file__).resolve().parents[1]  # datasets/oulad/exploration
DATA = HERE.parent  # datasets/oulad: the raw CSVs, only read
REPO = HERE.parents[2]
RESULTS = HERE / "results"
TABLES = ["courses", "assessments", "vle", "studentInfo", "studentRegistration", "studentAssessment", "studentVle"]
PRESENTATION = ["code_module", "code_presentation"]
ENROLMENT = PRESENTATION + ["id_student"]


# Column roles (explore-data step 2). Dates in OULAD are integer day offsets from the
# start of the module presentation (day 0), not calendar dates.
ROLES = {
    "courses": {"code_module": "dimension", "code_presentation": "dimension", "module_presentation_length": "metric (days)"},
    "assessments": {"code_module": "dimension", "code_presentation": "dimension", "id_assessment": "identifier",
                    "assessment_type": "dimension", "date": "temporal (day offset)", "weight": "metric (%)"},
    "vle": {"id_site": "identifier", "code_module": "dimension", "code_presentation": "dimension",
            "activity_type": "dimension", "week_from": "temporal (week)", "week_to": "temporal (week)"},
    "studentInfo": {"code_module": "dimension", "code_presentation": "dimension", "id_student": "identifier",
                    "gender": "dimension", "region": "dimension", "highest_education": "dimension",
                    "imd_band": "dimension (ordinal)", "age_band": "dimension (ordinal)",
                    "num_of_prev_attempts": "metric (count)", "studied_credits": "metric (credits)",
                    "disability": "boolean (Y/N)", "final_result": "dimension (outcome)"},
    "studentRegistration": {"code_module": "dimension", "code_presentation": "dimension", "id_student": "identifier",
                            "date_registration": "temporal (day offset)", "date_unregistration": "temporal (day offset)"},
    "studentAssessment": {"id_assessment": "identifier", "id_student": "identifier",
                          "date_submitted": "temporal (day offset)", "is_banked": "boolean (0/1)", "score": "metric (0-100)"},
    "studentVle": {"code_module": "dimension", "code_presentation": "dimension", "id_student": "identifier",
                   "id_site": "identifier", "date": "temporal (day offset)", "sum_click": "metric (count)"},
}


# Declared grain: the columns that should identify one row.
GRAIN = {
    "courses": PRESENTATION,
    "assessments": ["id_assessment"],
    "vle": ["id_site"],
    "studentInfo": ENROLMENT,
    "studentRegistration": ENROLMENT,
    "studentAssessment": ["id_assessment", "id_student"],
    "studentVle": None,  # event log; checked separately for repeated (enrolment, site, day) rows
}


NUMERIC_HINT = ("metric", "temporal", "boolean (0/1)")

# Category orders used across stages
OUTCOMES = ["Withdrawn", "Fail", "Pass", "Distinction"]
EARLY = 28  # early window: days 0-27 (weeks 0-3), the same length for every enrolment
IMD = ["0-10%", "10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "60-70%", "70-80%", "80-90%", "90-100%"]
AGE = ["0-35", "35-55", "55<="]
EDU = ["No Formal quals", "Lower Than A Level", "A Level or Equivalent", "HE Qualification",
       "Post Graduate Qualification"]


def load(table: str) -> tuple[pl.DataFrame, pl.DataFrame]:
    """(raw strings, typed) frames. Empty fields and '?' are missing in the typed frame."""
    raw = pl.read_csv(DATA / f"{table}.csv", infer_schema=False)
    typed = raw.with_columns(
        [pl.when(pl.col(c).is_in(["", "?"])).then(None).otherwise(pl.col(c)).alias(c) for c in raw.columns]
    )
    casts = []
    for c, role in ROLES[table].items():
        if role.startswith(NUMERIC_HINT) or c in ("id_student", "id_site", "id_assessment"):
            casts.append(pl.col(c).cast(pl.Float64, strict=False).alias(c))
    return raw, typed.with_columns(casts)


def load_all() -> dict[str, pl.DataFrame]:
    """Typed frames of all 7 tables."""
    return {table: load(table)[1] for table in TABLES}


def write_json(name: str, obj) -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / name).write_text(json.dumps(obj, indent=2, default=str, ensure_ascii=False))
