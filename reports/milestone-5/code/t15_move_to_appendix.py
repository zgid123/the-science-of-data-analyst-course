"""T15: move detail blocks of the full draft into the appendix files 16-01 … 16-16.

The full draft is read from git commit a6a8d5a (research/revisions/snapshots.md), so the moved blocks are verbatim
copies of the draft; only table numbers (old → new), references to subsections that now live in an appendix, and
references to sections of earlier milestone reports are rewritten. The main-text files are written by hand.

Usage: venv/bin/python reports/milestone-5/code/t15_move_to_appendix.py [--commit a6a8d5a]
Writes reports/milestone-5/report/16-00-appendices.md and 16-01-…md to 16-16-…md and prints each file with its
block count and word count.
"""

import argparse
import re
import subprocess
from pathlib import Path

TASK = Path(__file__).resolve().parents[1]
REPO = TASK.parents[1]
REPORT = TASK / "report"

# Old table number (full draft) -> new number (main text or appendix).
TABLES = {
    "1.1": "A.1", "2.1": "A.2", "2.2": "2.1", "2.3": "A.3",
    "3.1": "3.1", "3.2": "A.4", "3.3": "A.5", "3.4": "A.6",
    "4.1": "A.8", "4.2": "A.9", "4.3": "A.10",
    "5.1": "A.11", "5.2": "5.1", "5.3": "A.12", "5.4": "A.13",
    "6.1": "6.1", "6.2": "A.14", "6.3": "A.15",
    "7.1": "A.16", "7.2": "A.17", "7.3": "A.18", "7.4": "A.19", "7.5": "A.20",
    "8.1": "A.21", "8.2": "8.1",
    "9.1": "9.1", "9.2": "A.22", "9.3": "A.23",
    "10.1": "A.24",
    "11.1": "A.25", "11.2": "A.26", "11.3": "A.27", "11.4": "A.28", "11.5": "A.29", "11.6": "A.30",
    "11.7": "A.31", "11.8": "A.32", "11.9": "A.33", "11.10": "A.34", "11.11": "A.35", "11.12": "A.36",
    "11.13": "A.37", "11.14": "A.38",
    "12.1": "A.39", "12.2": "A.40",
    "13.1": "A.41",
}

# Subsections of Section 11 that exist only in the full draft -> the appendix that now holds them.
SUBSECTIONS = {
    "Section 11.2.2": "Appendix XII", "Section 11.3.3": "Appendix XIII", "Section 11.3.4": "Appendix XIII",
}

# References to sections of earlier milestone reports are kept as "Milestone N" only.
MILESTONE_SECTIONS = re.compile(r"\((Milestone \d), Sections? [\d.–]+\)")

TABLE_REF = re.compile(r"\bTable (\d+\.\d+)\b")


def draft(commit, name):
    return subprocess.run(["git", "show", f"{commit}:reports/milestone-5/report/{name}"], cwd=REPO, check=True,
                          capture_output=True, text=True).stdout


def rewrite(text):
    text = TABLE_REF.sub(lambda m: "Table " + TABLES[m.group(1)], text)
    for old, new in SUBSECTIONS.items():
        text = text.replace(old, new)
    return MILESTONE_SECTIONS.sub(r"(\1)", text)


# Facts restored after the loss check (code/t15_loss_check.py, logs/T15_loss_check.log): each is a sentence of the full
# draft that sat in an introduction or a table cell kept only in compact form in the main text. (file, anchor, text
# inserted after the anchor).
RESTORED = [
    ("16-01-context-stakeholders.md", "so that every contact remains a decision of a member of staff.",
     " These results support the judgement of the staff who know the students rather than replace it."),
    ("16-04-requirements-selection.md", "**How the search worked.**",
     " The search was therefore led by the requirements: its keywords came from the requirement matrix (student "
     "completion, dropout and withdrawal; interaction with a learning management system or virtual learning "
     "environment; assessment submission; clickstream; higher education; learning analytics; and dropout from massive "
     "open online courses), not from datasets already known to us."),
    ("16-05-dataset-gaps.md", "| studentVle | 10,655,280 | none documented | Daily number of clicks of each student on "
     "each page | Activity signs and features |",
     "\n\n**Key variables.** The key variables of Table 5.1 (Section 5) come from these tables with the following "
     "scales and roles. The final result (final_result) and the background attributes come from studentInfo, and the "
     "module and run codes (code_module, code_presentation) key every student table. The registration and "
     "unregistration days (date_registration, date_unregistration) come from studentRegistration and count from day 0; "
     "the unregistration day is empty for students who did not withdraw. The kind and due day of each task "
     "(assessment_type, date) come from assessments, and the submission day and score (date_submitted, score) from "
     "studentAssessment, where the score runs from 0 to 100 and a score below 40 is read as a fail. Each row of "
     "studentVle gives the clicks of one student on one page in one day (sum_click, date). Earlier attempts at the same "
     "module and the credits studied in the run (num_of_prev_attempts, studied_credits) adjust the AQ2 model and enter "
     "the AQ3 predictors, while the deprivation band of the home area and declared disability (imd_band, disability) "
     "serve only the group checks of AQ2 to AQ4 and are never predictors."),
    ("16-09-evaluation-detail.md", "**One design, two kinds of question.**",
     " The evaluation design was fixed in Milestone 4 before any code ran, which rules out choosing metrics or "
     "thresholds after the results are seen."),
    ("16-10-prototype-protocol.md", "**One logged test.**",
     " The 13 runs of 2014 are the project's only independent test and can be used once, so they are kept for one "
     "complete run of the frozen protocol, from the baselines to the logged test: no 2014 result is seen before the "
     "model is frozen, and a partial early run would spend that test."),
]


def restore(name, text):
    for fname, anchor, insert in RESTORED:
        if fname == name:
            if text.count(anchor) != 1:
                raise SystemExit(f"{name}: restore anchor {anchor[:40]!r} found {text.count(anchor)} times")
            text = text.replace(anchor, anchor + insert)
    return text


class Draft:
    def __init__(self, commit):
        self.commit, self.cache, self.used = commit, {}, set()

    def blocks(self, name):
        if name not in self.cache:
            self.cache[name] = [b.strip() for b in draft(self.commit, name).split("\n\n") if b.strip()]
        return self.cache[name]

    def take(self, name, prefix, n=1):
        bl = self.blocks(name)
        hits = [i for i, b in enumerate(bl) if b.startswith(prefix)]
        if len(hits) != 1:
            raise SystemExit(f"{name}: prefix {prefix!r} matches {len(hits)} blocks")
        i = hits[0]
        for k in range(i, i + n):
            if (name, k) in self.used:
                raise SystemExit(f"{name}: block {k} moved twice")
            self.used.add((name, k))
        return [rewrite(b) for b in bl[i:i + n]]


def change_log():
    """Controlled Change Log C01–C17: C01–C13 from the Milestone 3 report, C14 from Milestone 4, C15–C17 from the
    Milestone 5 design note (research/design/change-log-m5.md)."""
    rows = []
    m3 = (REPO / "reports/milestone-3/report/12-04-traceability-change-log.md").read_text()
    rows += [r for r in m3.splitlines() if re.match(r"^\| C(0\d|1[0-3]) \|", r)]
    m4 = (REPO / "reports/milestone-4/report/10-07-traceability-full.md").read_text()
    rows += [r.replace(" [40]", "") for r in m4.splitlines() if r.startswith("| C14 |")]
    m5 = (TASK / "research/design/change-log-m5.md").read_text()
    rows += [r for r in m5.splitlines() if re.match(r"^\| C1[5-7] \|", r)]
    rows = [r.replace("`", "") for r in rows]
    assert [r.split("|")[1].strip() for r in rows] == [f"C{i:02d}" for i in range(1, 18)], "C01–C17 not complete"
    head = "| ID | Milestone | Before | After | Reason | Effect |\n| :---- | :---- | :---- | :---- | :---- | :---- |"
    return head + "\n" + "\n".join(rows)


def build(d):
    T = lambda s: [s]  # noqa: E731  (glue text written for the appendix)
    A = {}

    A["16-01-context-stakeholders.md"] = (
        "## Appendix I – Educational Context, Stakeholders and Scope",
        T("This appendix supports Section 1. It gives the regulatory and published background of the problem, the "
          "stakeholders with their needs and decisions, how those needs were established and settled, and the areas "
          "that lie outside the scope of the project.")
        + d.take("01-00-introduction-context.md", "**The educational setting.**")
        + d.take("01-00-introduction-context.md", "**Regulation raises the stakes.**")
        + d.take("01-00-introduction-context.md", "**What published studies report.**")
        + d.take("01-00-introduction-context.md", "**The problem.**")
        + d.take("01-01-motivation-stakeholders.md", "**Who uses the results.**", 3)
        + d.take("01-01-motivation-stakeholders.md", "**How the needs were established.**")
        + d.take("01-01-motivation-stakeholders.md", "**What the stakeholders need.**")
        + d.take("01-01-motivation-stakeholders.md", "**How the conflicts were settled.**")
        + d.take("01-01-motivation-stakeholders.md", "**Published practice points the same way.**")
        + d.take("01-02-scope-objective.md", "**Scope in the university.**")
        + d.take("01-02-scope-objective.md", "**Outside the scope.**")
        + d.take("01-02-scope-objective.md", "**Data that stand in for the university's records.**"))

    A["16-02-goal-kpis-decisions.md"] = (
        "## Appendix II – Goal, Indicators and Decisions",
        T("This appendix supports Section 2. It gives the pilot design behind the SMART Goal with its check against "
          "the five SMART criteria, the full definition of each key performance indicator, and the classification of "
          "the three decisions with the evidence each needs.")
        + d.take("02-00-business-understanding.md", "**Business Goal.**")
        + d.take("02-00-business-understanding.md", "The pilot courses are about four", 3)
        + d.take("02-00-business-understanding.md", "**Why the target remains an assumption.**")
        + d.take("02-00-business-understanding.md", "**What the goal can and cannot show.**")
        + d.take("02-01-kpis-decisions.md", "**Primary KPI: course completion rate.**")
        + d.take("02-01-kpis-decisions.md", "**Secondary KPI 1: early-sign contact rate.**")
        + d.take("02-01-kpis-decisions.md", "**Secondary KPI 2: follow-up rate.**")
        + d.take("02-01-kpis-decisions.md", "**Decisions supported.**", 3)
        + d.take("02-01-kpis-decisions.md", "**How the level of a decision sets the evidence.**"))

    A["16-03-aq-quality-revision.md"] = (
        "## Appendix III – Analytical Questions: Quality Check, Revision Log and Change Log",
        T("This appendix supports Section 3. It gives how the four questions connect, the quality check of the final "
          "wording with the reason in each cell, the AQ Revision Log with every cell written out, the mapping of the "
          "milestones' status scales onto the final scales, and the Controlled Change Log C01–C17.")
        + d.take("03-00-analytical-questions.md", "**How the questions connect.**")
        + d.take("03-00-analytical-questions.md", "**The levels and how each answer may be read.**")
        + d.take("03-00-analytical-questions.md", "**Two definitions used by every question.**")
        + d.take("03-00-analytical-questions.md", "**What the final status means.**")
        + d.take("03-01-aq-quality-check.md", "**The check.**", 3)
        + d.take("03-01-aq-quality-check.md", "**What the check shows.**")
        + d.take("03-01-aq-quality-check.md", "**How refinement made the questions checkable.**")
        + d.take("03-02-aq-revision-log.md", "**The changes that touch every question.**")
        + d.take("03-02-aq-revision-log.md", "**The log.**", 3)
        + d.take("03-02-aq-revision-log.md", "**Reading the actions.**", 4)
        + d.take("03-02-aq-revision-log.md", "**Three entries recorded in the final integration.**")
        + d.take("03-02-aq-revision-log.md", "**What did not change.**")
        + T("**The Controlled Change Log.** Table A.7 gives every entry of the Controlled Change Log: C01 to C08 from "
            "the data search of Milestone 2, C09 to C13 from the data understanding of Milestone 3, C14 from the "
            "evaluation design of Milestone 4 and C15 to C17 from the final integration, each with the content "
            "before and after the change, its reason in the data and its effect on the questions, the KPIs or the "
            "decisions.")
        + T("**Table A.7. Controlled Change Log, entries C01–C17**")
        + T(change_log()))

    A["16-04-requirements-selection.md"] = (
        "## Appendix IV – Data Requirements and Dataset Selection",
        T("This appendix supports Section 4. It gives the sources of the requirements, the full AQ–Data Requirement "
          "Matrix, the six must-have gates with their reasons, the search procedure, the ten scores of each candidate "
          "dataset, the reasons for each rejection, and the provenance record of our copy of OULAD.")
        + d.take("04-00-data-requirements.md", "**Where the requirements come from.**")
        + d.take("04-00-data-requirements.md", "**What every question shares.**")
        + d.take("04-00-data-requirements.md", "**Time and the prediction point.**")
        + d.take("04-00-data-requirements.md", "**The requirement matrix.**", 3)
        + d.take("04-00-data-requirements.md", "**Must-have gates.**", 2)
        + d.take("04-00-data-requirements.md", "**Optional variables and declared gaps.**")
        + d.take("04-01-dataset-selection.md", "**How the search worked.**")
        + d.take("04-01-dataset-selection.md", "**How the candidates were judged.**", 3)
        + d.take("04-01-dataset-selection.md", "**Why OULAD, and why not the others.**")
        + d.take("04-01-dataset-selection.md", "**A modest total, made conditional.**")
        + d.take("04-01-dataset-selection.md", "**Limits that come with the choice.**")
        + d.take("04-01-dataset-selection.md", "**Provenance, version and licence.**", 3)
        + d.take("04-01-dataset-selection.md", "**Reproducible collection and privacy.**"))

    A["16-05-dataset-gaps.md"] = (
        "## Appendix V – Dataset Tables, Coverage and Gaps",
        T("This appendix supports Section 5. It gives the seven tables of OULAD with their keys, the coverage of runs "
          "and tasks, the gaps visible in the raw files, the AQ–Data Fit Matrix with every cell written out, and the "
          "four classes of gap with their handling.")
        + d.take("05-00-dataset-description.md", "**Population and unit.**")
        + d.take("05-00-dataset-description.md", "**Files, keys and links.**", 3)
        + d.take("05-00-dataset-description.md", "**Sample and outcome.**")
        + d.take("05-00-dataset-description.md", "**Coverage.**")
        + d.take("05-00-dataset-description.md", "**Gaps visible in the raw files.**")
        + d.take("05-01-requirement-data-fit.md", "The tables of Section 5 meet")
        + d.take("05-01-requirement-data-fit.md", "**The fit matrix.**", 3)
        + d.take("05-01-requirement-data-fit.md", "**Kinds of gap and how each is handled.**", 3)
        + d.take("05-01-requirement-data-fit.md", "**Why no other dataset is added.**")
        + d.take("05-01-requirement-data-fit.md", "**Status entering the analysis.**")
        + d.take("05-01-requirement-data-fit.md", "**Which questions the data cannot support.**"))

    A["16-06-profile-quality.md"] = (
        "## Appendix VI – Data Profile and Data Quality Issue Log",
        T("This appendix supports Section 6. It gives the keys and distributions of the profile, the Data Quality "
          "Issue Log with the evidence of each issue, the findings on duplicates, missing values, validity and "
          "outliers, and the temporal coverage, representativeness and sensitive attributes of OULAD.")
        + d.take("06-00-data-understanding.md", "**Unit and keys.**")
        + d.take("06-00-data-understanding.md", "**Outcome and time.**")
        + d.take("06-00-data-understanding.md", "**Outcome balance.**")
        + d.take("06-00-data-understanding.md", "**Distributions.**")
        + d.take("06-01-quality-findings.md", "The profile of Section 6 shows", 3)
        + d.take("06-01-quality-findings.md", "**Duplicates and grain.**")
        + d.take("06-01-quality-findings.md", "**Missing values.**")
        + d.take("06-01-quality-findings.md", "**Validity.**")
        + d.take("06-01-quality-findings.md", "**Outliers.**")
        + d.take("06-01-quality-findings.md", "**Issues that could change a conclusion.**")
        + d.take("06-01-quality-findings.md", "Two Medium issues")
        + d.take("06-01-quality-findings.md", "These findings produced")
        + d.take("06-02-representativeness-sensitive.md", "**Temporal coverage.**")
        + d.take("06-02-representativeness-sensitive.md", "The structure of the runs over time")
        + d.take("06-02-representativeness-sensitive.md", "**Representativeness.**")
        + d.take("06-02-representativeness-sensitive.md", "**Sensitive fields.**", 3)
        + d.take("06-02-representativeness-sensitive.md", "We set 20 students")
        + d.take("06-02-representativeness-sensitive.md", "All six attributes stay")
        + d.take("06-02-representativeness-sensitive.md", "**Privacy.**"))

    A["16-07-preparation-leakage.md"] = (
        "## Appendix VII – Preparation, Derived Variables and Leakage Controls",
        T("This appendix supports Section 7. It gives the Preparation Decision Matrix with the reason of each "
          "decision, the population rule, the pipeline steps, the derived variables with their formulas, the predictor "
          "sets and encoding, the leakage risks and controls, the before-and-after checks, the prepared views and the "
          "reproduction of the prepared dataset.")
        + d.take("07-00-preparation-pipeline.md", "**Decisions before any change.**", 3)
        + d.take("07-00-preparation-pipeline.md", "**Three governing decisions.**")
        + d.take("07-00-preparation-pipeline.md", "**Population rule.**")
        + d.take("07-00-preparation-pipeline.md", "**Missing values and outliers.**")
        + d.take("07-00-preparation-pipeline.md", "**Integration and steps.**")
        + d.take("07-01-features-leakage.md", "**Timing rule.**")
        + d.take("07-01-features-leakage.md", "**Derived variables.**", 4)
        + d.take("07-01-features-leakage.md", "**Predictor sets.**")
        + d.take("07-01-features-leakage.md", "**Encoding.**")
        + d.take("07-01-features-leakage.md", "**Leakage controls.**", 4)
        + d.take("07-01-features-leakage.md", "**Split.**")
        + d.take("07-02-prepared-dataset.md", "**Validation.**", 4)
        + d.take("07-02-prepared-dataset.md", "**Documentation.**")
        + d.take("07-02-prepared-dataset.md", "**Version and views.**", 3)
        + d.take("07-02-prepared-dataset.md", "**Reproducibility.**")
        + d.take("07-02-prepared-dataset.md", "**Sensitivity of the KPI to flagged records.**")
        + d.take("07-02-prepared-dataset.md", "**Synthetic data.**"))

    A["16-08-modeling-briefs.md"] = (
        "## Appendix VIII – Modeling Briefs and Method Rationale",
        T("This appendix supports Section 8. It gives the readiness of each question at entry, the development data, "
          "the Modeling Briefs, the technical tasks, the eight selection criteria and the rationale for the baseline, "
          "candidates and primary proposal of each question, including the specification with which AQ2 was run.")
        + d.take("08-00-modeling-strategy.md", "**Readiness at entry.**")
        + d.take("08-00-modeling-strategy.md", "**Why a ranking is needed.**")
        + d.take("08-00-modeling-strategy.md", "**Development data.**")
        + d.take("08-00-modeling-strategy.md", "**Purpose first.**")
        + d.take("08-00-modeling-strategy.md", "**Modeling Briefs.**", 3)
        + d.take("08-00-modeling-strategy.md", "**Technical tasks.**")
        + d.take("08-01-candidate-methods.md", "**Criteria.**")
        + d.take("08-01-candidate-methods.md", "**AQ1: grouped rates.**")
        + d.take("08-01-candidate-methods.md", "**AQ2: association within module run.**")
        + d.take("08-01-candidate-methods.md", "In Milestone 5 we ran this specification")
        + d.take("08-01-candidate-methods.md", "**AQ3: proposed predictive model.**")
        + d.take("08-01-candidate-methods.md", "The rationale for the primary proposal")
        + d.take("08-01-candidate-methods.md", "**AQ4: proposed ranking.**")
        + d.take("08-01-candidate-methods.md", "**Traceability of the choices.**"))

    A["16-09-evaluation-detail.md"] = (
        "## Appendix IX – Evaluation Design in Detail",
        T("This appendix supports Section 9. It gives the validation of each question, the full list of metrics, "
          "the success criteria of the proposed model and ranking, the validation design with its handling of the run "
          "structure, the fairness audit groups and rule, and the planned error analysis and interpretability checks.")
        + d.take("09-00-evaluation-design.md", "**One design, two kinds of question.**")
        + d.take("09-00-evaluation-design.md", "**Capacity and the main operating point.**")
        + d.take("09-00-evaluation-design.md", "**Metric definitions.**")
        + d.take("09-01-validation-success.md", "**AQ1.**")
        + d.take("09-01-validation-success.md", "**AQ2.**")
        + d.take("09-01-validation-success.md", "**AQ3: metrics.**")
        + d.take("09-01-validation-success.md", "**AQ3 and AQ4: success criteria.**", 4)
        + d.take("09-01-validation-success.md", "**AQ3 and AQ4: validation design.**")
        + d.take("09-01-validation-success.md", "A challenger,")
        + d.take("09-01-validation-success.md", "The test covers all 13")
        + d.take("09-02-fairness-interpretability.md", "**Leakage in the evaluation.**")
        + d.take("09-02-fairness-interpretability.md", "**Fairness: what is audited and why.**")
        + d.take("09-02-fairness-interpretability.md", "**One primary criterion.**")
        + d.take("09-02-fairness-interpretability.md", "**The audit groups.**", 4)
        + d.take("09-02-fairness-interpretability.md", "The descriptive checks")
        + d.take("09-02-fairness-interpretability.md", "**Error analysis.**")
        + d.take("09-02-fairness-interpretability.md", "**Interpretability.**"))

    A["16-10-prototype-protocol.md"] = (
        "## Appendix X – Specification of the Level 2 Prototype",
        T("This appendix supports Section 10. It gives what the specification of the unrun Level 2 prototype fixes, "
          "the configurations it would compare, its eight steps, the single logged test and the places in the project "
          "record that a run would change.")
        + d.take("10-00-experimental-status.md", "**What the prototype specification fixes.**", 4)
        + d.take("10-00-experimental-status.md", "**One logged test.**")
        + d.take("10-00-experimental-status.md", "**What would change in this report.**"))

    A["16-11-reading-traceability.md"] = (
        "## Appendix XI – Reading the Findings and Detailed Traceability",
        T("This appendix supports Sections 11 and 11.1. It gives how each answer is read by its analytics level, the "
          "rule behind each final status, the Final Project Traceability Matrix with every cell written out, and the "
          "justification of each final status.")
        + d.take("11-00-findings-overview.md", "Each answer is read according")
        + d.take("11-00-findings-overview.md", "Table 11.1 sets out", 3)
        + d.take("11-01-traceability-matrix.md", "The four final questions can only support decisions")
        + d.take("11-01-traceability-matrix.md", "The status of each row follows one rule.")
        + T("Table A.26 gives the Final Project Traceability Matrix with each cell written out, one row per final "
            "Analytical Question, in the columns of the course brief.")
        + [b.replace("(compact)", "with detailed cells")
           for b in d.take("11-01-traceability-matrix.md", "**Table 11.2. Final Project Traceability Matrix", 2)]
        + d.take("11-01-traceability-matrix.md", "Reading the rows across")
        + d.take("11-01-traceability-matrix.md", "Table 11.3 justifies", 3))

    A["16-12-aq1-results.md"] = (
        "## Appendix XII – AQ1 Results in Detail",
        T("This appendix supports Section 11.2. It gives the definitions behind the AQ1 results, the outcome shares "
          "under both denominators, the rates by module and start month, the effect of the denominator by run, the "
          "rates by group of students, the week of the first missed task by outcome and the comparison between 2013 "
          "and the published 2014 counts.")
        + d.take("11-02-aq1-findings.md", "The first question is descriptive")
        + d.take("11-02-aq1-findings.md", "Three definitions carry")
        + T("### Outcome shares and the success criterion")
        + d.take("11-02-aq1-findings.md", "The Milestone 4 success criterion for AQ1", 4)
        + T("### Differences by module, start month and run")
        + d.take("11-02-aq1-findings.md", "Non-completion differs widely", 4)
        + d.take("11-02-aq1-findings.md", "The run rates span")
        + d.take("11-02-aq1-findings.md", "The choice of denominator")
        + d.take("11-02-aq1-findings.md", "The same day-14 population also")
        + T("### Week of the first missed assessed task")
        + d.take("11-02-aq1-findings.md", "The second half of AQ1", 4)
        + T("### Comparison between 2013 and 2014")
        + d.take("11-02-aq1-findings.md", "AQ1 also asks for differences by year.", 4)
        + T("### What AQ1 means for the project")
        + d.take("11-02-aq1-findings.md", "AQ1 answers its descriptive question"))

    A["16-13-aq2-results.md"] = (
        "## Appendix XIII – AQ2 Results in Detail",
        T("This appendix supports Section 11.3. It gives the population, signs and model of AQ2, the association of "
          "each sign with its prevalence and odds ratio, the estimates by module, the sensitivity runs and model "
          "checks, the estimates by group of students, the parts that remain open and what the results mean for the "
          "project.")
        + d.take("11-03-aq2-findings.md", "Section 11.2 showed that nearly half")
        + T("### Population, signs and model")
        + d.take("11-03-aq2-findings.md", "We estimated AQ2 on the 9 runs of 2013")
        + d.take("11-03-aq2-findings.md", "The model follows the Milestone 4 plan.")
        + T("### Associations of the five signs")
        + d.take("11-03-aq2-findings.md", "Table 11.8 gives, for each sign", 3)
        + d.take("11-03-aq2-findings.md", "All five signs meet the consistent-association criterion. A missed task")
        + d.take("11-03-aq2-findings.md", "The gap between the unadjusted")
        + T("### Consistency across modules")
        + d.take("11-03-aq2-findings.md", "The criterion asks that each sign", 4)
        + T("### Sensitivity runs and model checks")
        + d.take("11-03-aq2-findings.md", "Six sensitivity runs", 4)
        + d.take("11-03-aq2-findings.md", "Two further checks", 4)
        + T("### Groups of students and the 2014 replication")
        + d.take("11-03-aq2-findings.md", "The Milestone 4 plan asks that the associations")
        + d.take("11-03-aq2-findings.md", "Two parts of AQ2 remain open.")
        + T("### What AQ2 means for the project")
        + d.take("11-03-aq2-findings.md", "AQ2 answers its diagnostic question"))

    A["16-14-aq3-aq4-answers.md"] = (
        "## Appendix XIV – Expected Outputs, Final Answers and Decision Support in Detail",
        T("This appendix supports Sections 11.4 and 11.5. It gives the expected outputs of AQ3 and AQ4 with the "
          "conditions that frame their reading, the final answers by Analytical Question with every cell written out, "
          "and the decision support for D1–D3 with the hypothesis each option leaves to test.")
        + d.take("11-04-aq3-aq4-expected.md", "Sections 11.2 and 11.3 answered")
        + T("### AQ3: estimating non-completion at the end of weeks 2 and 4")
        + d.take("11-04-aq3-aq4-expected.md", "AQ3 asks how well")
        + d.take("11-04-aq3-aq4-expected.md", "The question would be answered by a single gate")
        + d.take("11-04-aq3-aq4-expected.md", "Several conditions frame")
        + T("### AQ4: a ranked list under assumed capacity")
        + d.take("11-04-aq3-aq4-expected.md", "AQ4 asks which enrolments")
        + d.take("11-04-aq3-aq4-expected.md", "AQ4 would be answered when four conditions")
        + T("### What the expected outputs can and cannot support")
        + d.take("11-04-aq3-aq4-expected.md", "Table 11.12 sums up", 4)
        + T("### Final answers by Analytical Question")
        + d.take("11-05-decision-support.md", "Table 11.13 gives the final answer")
        + [b.replace("**Table A.37. Final answers by Analytical Question**",
                     "**Table A.37. Final answers by Analytical Question with detailed cells**")
           for b in d.take("11-05-decision-support.md", "**Table 11.13.", 2)]
        + d.take("11-05-decision-support.md", "Read across its rows")
        + T("### Why recommendations remain options to test")
        + d.take("11-05-decision-support.md", "All four answers rest on observational data")
        + T("### Decision support for D1, D2 and D3")
        + d.take("11-05-decision-support.md", "Table 11.14 relates", 3)
        + d.take("11-05-decision-support.md", "For D1, the evidence")
        + d.take("11-05-decision-support.md", "For D2, the AQ1 rates")
        + d.take("11-05-decision-support.md", "Taken together, the answers"))

    A["16-15-limitations-future.md"] = (
        "## Appendix XV – Limitations and Future Work in Detail",
        T("This appendix supports Section 12. It discusses each kind of limit, gives the limitation log with the "
          "effect of each limit on the conclusions, and sets out the future work in order with the data each step "
          "needs, the legal duties of use at the university and the design of the pilot.")
        + d.take("12-00-limitations.md", "Section 11 answered AQ1 and AQ2")
        + d.take("12-00-limitations.md", "**Generalisability.**")
        + d.take("12-00-limitations.md", "**Measurement.**")
        + d.take("12-00-limitations.md", "**Observational and causal limits.**")
        + d.take("12-00-limitations.md", "**Model and analysis limits.**")
        + d.take("12-00-limitations.md", "**Ethical limits.**")
        + d.take("12-00-limitations.md", "Table 12.1 brings these limits", 3)
        + d.take("12-01-future-work.md", "The limitation log of Section 12", 3)
        + d.take("12-01-future-work.md", "The first five steps")
        + d.take("12-01-future-work.md", "The remaining steps")
        + d.take("12-01-future-work.md", "Use at the university")
        + d.take("12-01-future-work.md", "Finally, a working model"))

    A["16-16-ai-decision-log.md"] = (
        "## Appendix XVI – AI Decision Log and Reflection",
        T("This appendix supports Section 13. It gives the AI Decision Log of Milestones 1–5 in the columns of the "
          "course brief and the full reflection on how the output of each AI role was verified.")
        + d.take("13-00-genai-reflection.md", "Section 12 stated the limits")
        + d.take("13-00-genai-reflection.md", "Table 13.1 gives the AI Decision Log.", 3)
        + d.take("13-00-genai-reflection.md", "Across the five milestones")
        + d.take("13-00-genai-reflection.md", "Verification took a different form")
        + d.take("13-00-genai-reflection.md", "The reviews helped most")
        + d.take("13-00-genai-reflection.md", "Human ownership shows"))
    return A


INTRO = """# Appendices

The appendices hold the detail behind the main text, in the order of the sections they support: the context and
stakeholders (Appendix I), the goal, indicators and decisions (Appendix II), the quality check, AQ Revision Log and
Controlled Change Log (Appendix III), the data requirements and dataset selection (Appendix IV), the dataset tables
and gaps (Appendix V), the data profile and quality issue log (Appendix VI), the preparation and leakage controls
(Appendix VII), the Modeling Briefs and method rationale (Appendix VIII), the evaluation design (Appendix IX), the
specification of the Level 2 prototype (Appendix X), the reading of the findings with the detailed traceability
(Appendix XI), the AQ1 results (Appendix XII), the AQ2 results (Appendix XIII), the expected outputs, final answers
and decision support (Appendix XIV), the limitations and future work (Appendix XV), and the AI Decision Log
(Appendix XVI). Counts come from OULAD and its prepared version OULAD-N04-prepared-1.0; outcome counts use the 2013
runs, and 2014 outcomes only as Milestone 3 published them.
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--commit", default="a6a8d5a")
    a = ap.parse_args()
    d = Draft(a.commit)
    (REPORT / "16-00-appendices.md").write_text(INTRO)
    print(f"16-00-appendices.md: intro, {len(re.findall(r'[A-Za-z]+', INTRO))} words")
    for name, (heading, blocks) in build(d).items():
        text = restore(name, heading + "\n\n" + "\n\n".join(blocks) + "\n")
        (REPORT / name).write_text(text)
        print(f"{name}: {len(blocks)} blocks, {len(re.findall(r'[A-Za-z]+', text))} words")
    print(f"moved blocks: {len(d.used)}")


if __name__ == "__main__":
    main()
