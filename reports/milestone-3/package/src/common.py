"""Shared definitions of the Milestone 3 Prepared Data Package: paths, tables, keys, types, category orders, loaders.

Imported by every script in src/; holds no analysis. Paths are relative to this file, so the package runs on any
machine. Raw files are only read (brief principle "raw is immutable").
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import polars as pl

PKG = Path(__file__).resolve().parents[1]           # the package folder
RAW = PKG / "data" / "raw"                            # immutable, checked against data/metadata/raw_pins.csv
INTERIM = PKG / "data" / "interim"                    # reproducible intermediates
PROCESSED = PKG / "data" / "processed"                # analytic-ready views
META = PKG / "data" / "metadata"                      # dictionary, lineage, quality logs, validation
EXPLORATION = PKG.parents[2] / "datasets" / "oulad" / "exploration"  # earlier exploration, for cross-checks only

TABLES = ["courses", "assessments", "vle", "studentInfo", "studentRegistration", "studentAssessment", "studentVle"]
RUN = ["code_module", "code_presentation"]            # a module run ("module-presentation" in OULAD)
ENROLMENT = RUN + ["id_student"]                      # one student in one module run

# Declared keys (grain); studentVle has no documented key.
KEYS = {
    "courses": RUN,
    "assessments": ["id_assessment"],
    "vle": ["id_site"],
    "studentInfo": ENROLMENT,
    "studentRegistration": ENROLMENT,
    "studentAssessment": ["id_assessment", "id_student"],
    "studentVle": None,
}

# Integer columns (identifiers, day offsets, counts); score and weight are kept as floats.
INTS = {"module_presentation_length", "id_assessment", "date", "id_student", "num_of_prev_attempts",
        "studied_credits", "date_registration", "date_unregistration", "date_submitted", "is_banked", "id_site",
        "sum_click", "week_from", "week_to"}
FLOATS = {"weight", "score"}

# Category orders
OUTCOMES = ["Withdrawn", "Fail", "Pass", "Distinction"]
IMD = ["0-10%", "10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "60-70%", "70-80%", "80-90%", "90-100%"]
AGE = ["0-35", "35-55", "55<="]
EDU = ["No Formal quals", "Lower Than A Level", "A Level or Equivalent", "HE Qualification",
       "Post Graduate Qualification"]
SENSITIVE = ["gender", "age_band", "disability", "imd_band", "region", "highest_education"]

# Prediction points fixed in Milestone 2 (Change Log C02): end of week 2 and end of week 4, day 0 = run start.
CUTOFFS = {"d13": 13, "d27": 27}
KPI_DAY = 14                                          # enrolled on day 14 = KPI denominator (C03, C09)


def enrolled_at(day: int) -> pl.Expr:
    """Enrolled at the end of `day`: registered by then (or registration day unknown) and not yet unregistered.

    Used for the KPI denominator (day 14) and for the population of each prediction point (days 13 and 27)."""
    return ((pl.col("date_registration").is_null() | (pl.col("date_registration") <= day))
            & (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") > day)))


def schema(columns):
    return {c: pl.Int64 if c in INTS else pl.Float64 if c in FLOATS else pl.String for c in columns}


def header(table: str) -> list[str]:
    with open(RAW / f"{table}.csv") as f:
        return [c.strip('"') for c in f.readline().strip().split(",")]


def scan(table: str) -> pl.LazyFrame:
    """Typed lazy frame of a raw table; empty fields become missing (null)."""
    sch = schema(header(table))
    text = [c for c, t in sch.items() if t == pl.String]
    return pl.scan_csv(RAW / f"{table}.csv", schema=sch).with_columns(
        [pl.when(pl.col(c) == "").then(None).otherwise(pl.col(c)).alias(c) for c in text])


def load(table: str) -> pl.DataFrame:
    return scan(table).collect()


def load_text(table: str) -> pl.DataFrame:
    """Raw table with every column as text, nothing converted (for format and code checks)."""
    return pl.read_csv(RAW / f"{table}.csv", infer_schema=False)


def start_month(code_presentation: str) -> str:
    """'2013J' -> 'J' (October start), '2014B' -> 'B' (February start)."""
    return code_presentation[-1]


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str, ensure_ascii=False))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md_table(rows: list[dict], cols: list[str] | None = None) -> str:
    cols = cols or list(rows[0])
    out = ["| " + " | ".join(cols) + " |", "| " + " | ".join(":----" for _ in cols) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(r.get(c, "")).replace("|", "\\|") for c in cols) + " |")
    return "\n".join(out)
