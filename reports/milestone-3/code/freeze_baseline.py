"""Freeze the baseline Milestone 3 starts from (brief section 3, step 1 of section 5).

The Milestone 1 proposal as revised by Milestone 2: the frozen Milestone 1 elements, the Controlled Change Log
C01–C08, the full traceability matrix and the prediction-point and leakage table are copied verbatim from the
Milestone 2 report; every source file is hashed (SHA-256). The Milestone 1 hashes recorded by Milestone 2 are
re-checked, so an edit to Milestone 1 since then is visible. The six inputs the brief requires from Milestone 2 are
listed with the file that holds each.

Usage: venv/bin/python reports/milestone-3/code/freeze_baseline.py
Writes reports/milestone-3/research/baseline/m3-baseline.md; exit 1 if a Milestone 1 file changed or an input is
missing.
"""
import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPORTS = HERE.parents[1]
M1 = REPORTS / "milestone-1" / "report"
M2 = REPORTS / "milestone-2"
OUT = HERE.parent / "research" / "baseline" / "m3-baseline.md"

M2_FILES = ["report/01-01-frozen-baseline.md", "report/02-03-prediction-point-leakage.md",
            "report/07-01-traceability.md", "report/07-02-gaps-revisions.md", "report/11-05-change-log.md",
            "research/baseline/m1-baseline.md", "research/requirements/data-requirements.md",
            "package/metadata/source.md", "package/metadata/data_dictionary.md",
            "package/metadata/raw_manifest.csv", "package/metadata/structure_report.md"]

# The six inputs of brief section 3 and the Milestone 2 file that provides each.
INPUTS = [
    ("Milestone 1 baseline", "research/baseline/m1-baseline.md",
     "Business Goal, SMART Goal, KPIs, AQ1–AQ4, analytics types, decisions (frozen with SHA-256)"),
    ("Updated Traceability Matrix", "report/11-05-change-log.md",
     "Table A.10: KPI → AQ → requirement → file → actual variables → coverage → decision"),
    ("Raw Data Package", "package/metadata/raw_manifest.csv",
     "archive and seven CSVs, SHA-256 pinned; re-created by package/src/collect.py"),
    ("Metadata / Data Dictionary", "package/metadata/data_dictionary.md",
     "column definitions from the data descriptor; source.md holds license and citation"),
    ("Collection Evidence", "package/metadata/source.md",
     "DOI 10.6084/m9.figshare.5081998.v1, access date, version, checksums, collection log"),
    ("Controlled Change Log", "report/11-05-change-log.md", "C01–C08 with old and new content and data evidence"),
]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def section(text, start, stop):
    i = text.index(start)
    j = text.index(stop, i + len(start)) if stop else len(text)
    return text[i:j].strip()


def table(text, caption):
    i = text.index(caption)
    out = []
    for line in text[i:].split("\n")[1:]:
        if line.startswith("|"):
            out.append(line)
        elif out:
            break
    return caption + "\n\n" + "\n".join(out)


def main():
    errors = []
    log = M2 / "report" / "11-05-change-log.md"
    a8 = dict(re.findall(r"^\| (\S+\.md) \| ([0-9a-f]{64}) \|$", log.read_text(), re.M))
    m1_rows = []
    for f, pinned in a8.items():
        now = sha(M1 / f)
        state = "unchanged" if now == pinned else "CHANGED"
        if now != pinned:
            errors.append(f"Milestone 1 file changed since Milestone 2: {f}")
        m1_rows.append(f"| {f} | {now} | {state} |")
    m2_rows = [f"| {f} | {sha(M2 / f)} |" for f in M2_FILES]
    input_rows = []
    for name, f, content in INPUTS:
        ok = (M2 / f).exists()
        if not ok:
            errors.append(f"missing input: {f}")
        input_rows.append(f"| {name} | reports/milestone-2/{f} | {content} | {'present' if ok else 'MISSING'} |")

    m1b = (M2 / "research/baseline/m1-baseline.md").read_text()
    clog = log.read_text()
    parts = [
        "# Frozen baseline for Milestone 3",
        f"Frozen {datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ} by `code/freeze_baseline.py`. The Milestone 1 "
        "elements, the Milestone 2 Controlled Change Log, the traceability matrix and the prediction-point table are "
        "copied verbatim; any later change goes into the Milestone 3 Change Log (C09 onwards).",
        "## Inputs required by the brief (section 3)",
        "| Input | File | Content | Status |\n| :---- | :---- | :---- | :---- |\n" + "\n".join(input_rows),
        "## Milestone 1 files re-checked against the hashes pinned in Milestone 2 (Table A.8)",
        "| File | SHA-256 now | State |\n| :---- | :---- | :---- |\n" + "\n".join(m1_rows),
        "## Milestone 2 files this baseline is copied from (SHA-256)",
        "| File | SHA-256 |\n| :---- | :---- |\n" + "\n".join(m2_rows),
        "## Milestone 1 baseline (verbatim from Milestone 2)",
        section(m1b, "## Business Goal", None).replace("\n## ", "\n### ").replace("## Business Goal", "### Business Goal", 1),
        "## Controlled Change Log C01–C08 (verbatim)", table(clog, "**Table A.9. Controlled Change Log**"),
        "## Traceability matrix (verbatim)", table(clog, "**Table A.10. Full traceability from goal to decision with coverage**"),
        "## Prediction points and leakage rules (verbatim)",
        table((M2 / "report/02-03-prediction-point-leakage.md").read_text(),
              "**Table 2.3. Prediction points, allowed features and leakage risks**"),
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n\n".join(parts) + "\n")
    print(f"wrote {OUT.relative_to(REPORTS.parent)}")
    print(f"Milestone 1 files: {len(m1_rows)} re-checked, "
          f"{sum('unchanged' in r for r in m1_rows)} unchanged")
    print(f"Milestone 2 files hashed: {len(m2_rows)}; brief inputs present: "
          f"{sum('present' in r for r in input_rows)} of {len(INPUTS)}")
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
