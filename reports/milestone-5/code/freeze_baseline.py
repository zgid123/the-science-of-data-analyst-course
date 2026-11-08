"""Entry baseline of Milestone 5 (brief section 1.2): the final state of Milestones 1–4, copied verbatim.

Copies, without rewording, the inputs the brief requires from each milestone: the original goal, KPIs and question
ladder (Milestone 1), the AQ–Data matrix and the dataset selection (Milestone 2), the AQ–Data Fit ratings, the
quality issue log and the prepared dataset version (Milestone 3), and the final goal and AQs, the candidate solution
matrix, the evaluation cards and the traceability and Change Log (Milestone 4), each with the SHA-256 of its source
file, then records the brief's check for each input.

Usage: venv/bin/python reports/milestone-5/code/freeze_baseline.py
Writes reports/milestone-5/research/baseline/m5-baseline.md.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
R = ROOT / "reports"
OUT = R / "milestone-5" / "research" / "baseline" / "m5-baseline.md"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def block(title: str, path: Path, text: str | None = None) -> str:
    text = path.read_text(encoding="utf-8") if text is None else text
    return f"## {title}\n\nSource: `{path.relative_to(ROOT)}` (SHA-256 {sha(path)[:16]})\n\n{text.strip()}\n\n"


def main() -> None:
    m1, m2, m3, m4 = (R / f"milestone-{i}" / "report" for i in (1, 2, 3, 4))
    meta = R / "milestone-3" / "package" / "data" / "metadata"
    man = json.loads((meta / "version_manifest.json").read_text())
    val = json.loads((meta / "validation_summary.json").read_text())
    passed = sum(c["Status"] == "PASS" for c in val["checks"])
    sources = [
        ("Milestone 1: Business Goal (Section 3.1)", m1 / "03-01-business-goal.md"),
        ("Milestone 1: SMART Goal (Section 3.2)", m1 / "03-02-smart-goal.md"),
        ("Milestone 1: KPIs (Section 3.3)", m1 / "03-03-kpis.md"),
        ("Milestone 1: Questions at four levels (Section 4.1)", m1 / "04-01-four-level-questions.md"),
        ("Milestone 1: Decision supported and value (Section 7)", m1 / "07-00-decision-value.md"),
        ("Milestone 2: AQ–Data Requirement Matrix (Section 2.1)", m2 / "02-01-aq-data-matrix.md"),
        ("Milestone 2: Selection matrix and rationale (Section 4.2)", m2 / "04-02-selection-matrix.md"),
        ("Milestone 2: Acquisition and provenance (Section 5)", m2 / "05-00-acquisition-provenance.md"),
        ("Milestone 3: AQ–Data Fit ratings (Section 4.1)", m3 / "04-01-fit-ratings.md"),
        ("Milestone 3: Gap decisions (Section 4.2)", m3 / "04-02-gap-decisions.md"),
        ("Milestone 3: Data Quality Issue Log (Section 3.5)", m3 / "03-05-quality-issue-log.md"),
        ("Milestone 3: Readiness matrix (Section 8.2)", m3 / "08-02-readiness-matrix.md"),
        ("Milestone 4: Goal, decisions and AQs as they stand (Section 1.1)", m4 / "01-01-goal-decisions-aqs.md"),
        ("Milestone 4: Candidate Solution Matrix (Section 3.1)", m4 / "03-01-criteria-matrix.md"),
        ("Milestone 4: Evaluation Design Cards (Section 4.1)", m4 / "04-01-evaluation-cards.md"),
        ("Milestone 4: Updated Traceability Matrix (Section 8)", m4 / "08-00-traceability.md"),
        ("Milestone 4: Full traceability and Change Log (Appendix VII)", m4 / "10-07-traceability-full.md"),
    ]
    parts = ["# Milestone 5 baseline: Milestones 1–4 as submitted\n\n"
             "Verbatim copies of the report sections and package files that Milestone 5 integrates (brief section 1.2).\n\n"]
    parts += [block(t, p) for t, p in sources]
    parts.append(block("Milestone 3: Prepared dataset version", meta / "version_manifest.json",
                       "```json\n" + json.dumps({k: man[k] for k in man if not isinstance(man[k], (list, dict))},
                                                ensure_ascii=False, indent=1) + "\n```"))
    gate = [
        ("Milestone 1", "Business Goal, SMART Goal, KPIs, stakeholder needs, AQs, analytics level",
         "final version with changes recorded (Change Log C01–C14)", "PASS"),
        ("Milestone 2", "open dataset, provenance and licence, data requirements, AQ–Data mapping",
         "OULAD, CC BY 4.0, verified copy with hashes (Milestone 2 Sections 4–5)", "PASS"),
        ("Milestone 3", "data understanding, quality findings, prepared dataset, final AQ status",
         f"prepared dataset {man['prepared_dataset_version']} with pipeline; validation {passed} of "
         f"{len(val['checks'])} checks PASS", "PASS" if passed == len(val["checks"]) else "FAIL"),
        ("Milestone 4", "candidate methods, rationale, evaluation plan; optional experiment",
         "Level 1 complete; Level 2 specified as a protocol, not run", "PASS"),
    ]
    parts.append("## Inputs required by the brief (section 1.2)\n\n| Source | Product | Check | Status |\n"
                 "| :---- | :---- | :---- | :---- |\n" + "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in gate)
                 + "\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(parts), encoding="utf-8")
    for a, _, _, d in gate:
        print(f"{d}  {a}")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(sources) + 1} blocks")


if __name__ == "__main__":
    main()
