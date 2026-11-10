"""Part A of the rewrite after the Vietnamese reader test: English source fixes for apparent contradictions.
Each edit must match exactly once; run from the repository root: venv/bin/python <this file>."""
from pathlib import Path

R = Path(__file__).resolve().parents[3] / "report"
EDITS = [
    ("06-01-quality-findings.md", "and the duplicate\nclick rows carry 3.19% of all clicks,",
     "and the duplicate\nclick rows, 7.39% of click rows, carry 3.19% of all clicks,"),
    ("06-01-quality-findings.md", "| Duplicate click rows (7.39%); several rows per day |",
     "| Duplicate click rows (7.39% of rows); several rows per day |"),
    ("11-01-traceability-matrix.md", "For AQ1 and AQ2 every link holds evidence and both meet their criteria;",
     "For AQ1 and AQ2 every link holds evidence, GAP marking only variables OULAD lacks, and both meet their criteria;"),
    ("07-02-prepared-dataset.md", "All 22 validation checks pass:",
     "All 22 validation checks, under the fifteen identifiers V01–V15 (Section 7), pass:"),
    ("03-00-analytical-questions.md", "| D2, D3 | All five met; answered for 2013 | Partial |",
     "| D2, D3 | All five met; 2014 part waits | Partial |"),
    ("03-00-analytical-questions.md", "A question is Answered when real results answer all of it, Partial when they answer its core while a named part waits,",
     "The five criteria judge a question's wording; its status says how much results answer: Answered when they answer all of it, Partial when they answer its core while a named part waits (for AQ1 and AQ2, the 2014 runs),"),
    ("11-03-aq2-findings.md", "Each keeps its direction in every module (Table A.34) and\nunder six sensitivity runs (Table A.35).",
     "Each keeps its direction in every module, though five click-sign estimates in AAA and GGG include 0 (Table A.34),\nand under six sensitivity runs (Table A.35)."),
    ("12-00-limitations.md", "| Year difference within modules; weak click signs in AAA, GGG |",
     "| Year difference within modules; click signs in AAA, GGG (same direction, intervals include 0) |"),
    ("11-02-aq1-findings.md", "and the 2014 outcome counts that Milestone 3 published for the year comparison\n(C15).",
     "and the 2014 outcome counts per run that Milestone 3 published for the year comparison, opening no 2014\nenrolment (C15)."),
    ("06-00-data-understanding.md", "Of the 28,061 enrolments registered at day 14, 54.7% completed;",
     "Of the 28,061 enrolments of all 22 runs registered at day 14, 54.7% completed;"),
    ("06-00-data-understanding.md", "the 13 runs of 2014, whose outcomes stay unopened, for a single test;",
     "the 13 runs of 2014, whose enrolment outcomes stay unopened, for a single test;"),
    ("05-01-requirement-data-fit.md", "| A task-only rule fires in 1 run at day 13 |", "| A task-only rule fires in 1 of 22 runs at day 13 |"),
    ("02-01-kpis-decisions.md", "Sign part only: rule flags 28.8% of 27,535 at day 27 |",
     "Sign part only: rule flags 28.8% of 27,535 (22 runs) at day 27 |"),
]
for name, old, new in EDITS:
    p = R / name
    text = p.read_text()
    if text.count(new) == 1 and text.count(old) == 0:
        print(f"already applied: {name}")
        continue
    assert text.count(old) == 1, (name, old)
    p.write_text(text.replace(old, new))
    print(f"applied: {name}")
