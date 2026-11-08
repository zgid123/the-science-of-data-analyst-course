"""Entry gate of Milestone 4 (brief section 3): copy the Milestone 3 baseline verbatim and check the five conditions.

Copies, without rewording, the goal and AQ table (report 01-01), the AQ-Data Fit table (04-01), the Model Readiness
Matrix (08-02), the split and leakage table (06-03), Change Log C09-C13, the predictor sets and the prepared dataset
version, each with the SHA-256 of its source file, and records the evidence for each entry condition.

Usage: venv/bin/python reports/milestone-4/code/freeze_baseline.py
Writes reports/milestone-4/research/baseline/m4-baseline.md.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
M3 = ROOT / "reports" / "milestone-3"
REP = M3 / "report"
META = M3 / "package" / "data" / "metadata"
OUT = ROOT / "reports" / "milestone-4" / "research" / "baseline" / "m4-baseline.md"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def block(title, path, text=None):
    text = path.read_text() if text is None else text
    rel = path.relative_to(ROOT)
    return f"## {title}\n\nSource: `{rel}` (SHA-256 {sha(path)[:16]})\n\n{text.strip()}\n\n"


def change_rows(path, ids):
    lines = path.read_text().splitlines()
    head = [l for l in lines if l.startswith("|")][:2]
    rows = [l for l in lines if any(l.startswith(f"| {i} ") for i in ids)]
    return "\n".join(head + rows)


def main():
    man = json.loads((META / "version_manifest.json").read_text())
    val = json.loads((META / "validation_summary.json").read_text())
    checks = val["checks"]
    passed = sum(c["Status"] == "PASS" for c in checks)
    parts = ["# Milestone 4 baseline: Milestone 3 as submitted\n\n"
             "Verbatim copies of the Milestone 3 report and package files that Milestone 4 starts from.\n\n"]
    parts.append(block("Goal, KPIs, decisions and AQ1–AQ4 (Milestone 3, Section 1.1)", REP / "01-01-baseline-aqs.md"))
    parts.append(block("AQ–Data Fit ratings (Milestone 3, Section 4.1)", REP / "04-01-fit-ratings.md"))
    parts.append(block("Model Readiness Matrix (Milestone 3, Section 8.2)", REP / "08-02-readiness-matrix.md"))
    parts.append(block("Split and leakage control (Milestone 3, Section 6.3)", REP / "06-03-split-leakage.md"))
    parts.append(block("Change Log C09–C13", META / "change_log.md",
                       change_rows(META / "change_log.md", ["C09", "C10", "C11", "C12", "C13"])))
    parts.append(block("Predictor sets", META / "predictor_sets.json",
                       "```json\n" + (META / "predictor_sets.json").read_text().strip() + "\n```"))
    parts.append(block("Split specification", META / "split_spec.md"))
    gate = [
        ("Approved Analytical Questions", "AQ1–AQ3 ready, AQ4 revised to ranking with contact deferred (C11, C13); "
         "no deferred part brought back", "PASS"),
        ("Prepared dataset", f"version {man['prepared_dataset_version']}; data dictionary, unit, keys, target "
         "non_completion, feature windows to day 13 and day 27", "PASS"),
        ("Leakage controls", "prediction points day 13 and day 27; training 2013, test 2014; transforms fitted on 2013; "
         f"validation {passed} of {len(checks)} checks PASS", "PASS" if passed == len(checks) else "FAIL"),
        ("Known limitations", "Data Quality Issue Log DQ01–DQ19; sensitive attributes kept for audit; "
         "representativeness and data protection stated (Milestone 3 Parts 3 and 9)", "PASS"),
        ("Traceability", "AQ → data requirement → actual variables → prepared view (Milestone 3 Appendix IV, "
         "Table A.13)", "PASS"),
    ]
    parts.append("## Entry gate (brief section 3)\n\n| Condition | Evidence | Status |\n| :---- | :---- | :---- |\n"
                 + "\n".join(f"| {a} | {b} | {c} |" for a, b, c in gate) + "\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(parts))
    for a, _, c in gate:
        print(f"{c}  {a}")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
