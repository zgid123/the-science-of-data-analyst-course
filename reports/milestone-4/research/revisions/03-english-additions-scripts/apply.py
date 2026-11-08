#!/usr/bin/env python3
"""Apply the English additions of fidelity review 2 (2026-11-08) to the Milestone 4 report.

Source: research/vi-review/fidelity-2-2026-11-08.md, section "English additions proposed" (45 rows).
Each edit is an exact-match replacement; the old string must occur exactly once in its file.
Also applies the matching twin edit for row 01-01 (delivery mode).

Run from anywhere:  venv/bin/python reports/milestone-4/research/revision/english-additions-2026-11-08/apply.py
Re-running after a successful run fails on the first assertion (old strings are gone), by design.
"""
from pathlib import Path
import sys

REPORT = Path(__file__).resolve().parents[3] / "report"

F = {
    "00-2": "00-2-glossary.md",
    "01-01": "01-01-goal-decisions-aqs.md",
    "01-01vi": "01-01-goal-decisions-aqs.vi.md",
    "01-02": "01-02-prepared-data-entry-gate.md",
    "02-02": "02-02-technical-tasks.md",
    "03-01": "03-01-criteria-matrix.md",
    "03-02": "03-02-descriptive-diagnostic.md",
    "03-03": "03-03-predictive.md",
    "04-01": "04-01-evaluation-cards.md",
    "04-02": "04-02-validation-strategy.md",
    "04-03": "04-03-metrics-success.md",
    "04-04": "04-04-error-fairness.md",
    "05-00": "05-00-risk-ethics.md",
    "05-01": "05-01-leakage-interpretability.md",
    "05-02": "05-02-causal-fairness-use.md",
    "06-00": "06-00-genai-usage.md",
    "10-01": "10-01-candidate-comparison.md",
    "10-03": "10-03-validation-protocol.md",
    "10-04": "10-04-fairness-spec.md",
    "10-05": "10-05-risk-register.md",
    "10-06": "10-06-ai-critiques.md",
    "10-07": "10-07-traceability-full.md",
}

# (row id, file key, old, new)
EDITS = [
    ("1", "00-2",
     "| The coefficient of the score's log-odds in a logistic recalibration; 1 when",
     "| The coefficient of the score's log-odds in a logistic recalibration, a logistic regression of the outcome on that log-odds; 1 when"),
    ("2", "00-2",
     "| The intercept of a logistic model of the outcome with the score's log-odds as offset; 0 when",
     "| The intercept of a logistic model of the outcome with the score's log-odds as offset (a term whose coefficient is fixed at 1); 0 when"),
    ("3", "00-2",
     "trained only on the 2013 February runs (Section 4.2) |",
     "trained only on the 2013 February runs, the runs whose outcomes are known at that time (Section 4.2) |"),
    ("4", "01-01",
     "replace comparisons by delivery mode and year of study with comparisons by module and run;",
     "replace comparisons by delivery mode, which OULAD does not vary because every run is distance learning, and year of study\n"
     "with comparisons by module and run;"),
    ("5", "01-01",
     "and by its gain over the run's\nbase rate, the share of students who do not complete, because a random list already reaches that rate (C13).",
     "and by its gain over the run's\nbase rate (lift), the share of non-completers on the list against the share of students in the whole run who do not\n"
     "complete, because a random list already reaches that base rate (C13)."),
    ("6", "01-02",
     "two\nfeature views, one for each cut-off:",
     "two\nfeature views, the tables of predictors a model reads, one for each cut-off:"),
    ("7", "01-02",
     "A feature view keeps\nonly the enrolments still registered at its cut-off and only",
     "A feature view keeps\nonly the enrolments still registered at its cut-off, that is, not withdrawn by that day, and only"),
    ("8", "02-02",
     "A discrete-time survival model would add when a student leaves [8]",
     "A discrete-time survival model, a form of survival analysis, would add when a student leaves [8]"),
    ("9", "03-01",
     "| Aggregation | Pooled rate; second denominator | Grouped rates with 95% intervals | – |",
     "| Aggregation | Pooled rate; rate over all enrolments, not only those registered at day 14 (second denominator) | Grouped rates with 95% intervals | – |"),
    ("10", "03-01",
     "| All runs of the modules observed; effect sizes within module; no causal claim |",
     "| All runs of the modules observed, not sampled, so fixed effects suit; effect sizes within module; no causal claim |"),
    ("11", "03-01",
     "ample events per parameter; transfer",
     "ample events per parameter, each parameter backed by many non-completers; transfer"),
    ("12", "03-02",
     "it is deterministic and is\nchecked with",
     "it is deterministic, giving the same result on\nevery rerun, and is checked with"),
    ("13", "03-03",
     "module and start month enter as several terms each,\nso the model has 23 parameters in all.",
     "module and start month are categorical and enter\nas dummy terms, one per level except a reference level, so the model has 23 parameters in all."),
    ("14", "03-03",
     "13, about 230 per parameter,",
     "13, about 230 events (non-completers) per parameter,"),
    ("15", "04-01",
     "computed per run with the run's own list and pooled over runs (day 27, k = 5 per 20) |",
     "computed per run with the run's own list and pooled over runs: the non-completers listed in all runs divided by the most the lists could hold, which for each list is k non-completers, or all of the run's non-completers if there are fewer (day 27, k = 5 per 20) |"),
    ("16", "04-01",
     "| Confirmatory check of recall at capacity by group and descriptive checks (Section 4.4) |",
     "| Confirmatory check of recall at capacity by group (a formal test on groups fixed in advance) and descriptive checks (Section 4.4) |"),
    ("17", "04-02",
     "1,586 test enrolments at day 27 of students already seen in 2013 stay in the test,",
     "1,586 test enrolments at day 27 of students already seen in the 2013 development data stay in the test,"),
    ("18", "04-02",
     "in October [2], and the 2013 J runs last 261–268 days, so their outcomes are not yet known when the 2014 B runs reach\n"
     "their cut-offs; a labels-available variant",
     "in October [2]. The 2013 J runs start in October 2013 and last 261–268 days, ending around mid-2014, whereas the 2014 B\n"
     "runs start in February 2014 and reach their cut-offs a few weeks later, when the 2013 J outcomes are not yet known; a\n"
     "labels-available variant"),
    ("19", "04-02",
     "and the overall risk estimated within 0.05.",
     "and the overall risk, the non-completion rate in the development data, estimated within 0.05."),
    ("20", "04-03",
     "the intercept of a recalibration model with the slope\nfixed, whose target is 0",
     "the intercept of a recalibration model (a logistic\nregression of the outcome on the score's log-odds) with the slope fixed at 1, whose target is 0"),
    ("21", "04-04",
     "conflict except in degenerate cases [37].",
     "conflict except in degenerate cases (perfect prediction or equal base rates across groups) [37]."),
    ("22", "04-04",
     "and the rest of the students are many times more numerous, so the gap of 10 points in rule FR1 is about two\n"
     "standard errors of the group's recall, the main source of uncertainty in the gap, and 400 enrolments at the lowest group rate of 28% give about 112 non-completers.",
     "and the rest of the students are many times more numerous, so their recall has a much smaller standard error and the\n"
     "group's recall is the main source of uncertainty in the gap; the gap of 10 points in rule FR1 is therefore about two\n"
     "standard errors of the group's recall. In addition, 400 enrolments at the lowest group rate of 28% give about 112\n"
     "non-completers (400 × 28%), above 100."),
    ("23", "04-04",
     "the threshold-free gap, the proxy check,",
     "the threshold-free gap in discrimination (ABROCA), the proxy check,"),
    ("24", "05-00",
     "can override; flags expire; risk",
     "can override; flags expire with the run; risk"),
    ("25", "05-01",
     "which the dated feature views ensure and the labels-available variant checks.",
     "which the dated feature views ensure and the labels-available variant checks, since the outcomes of the\n"
     "October 2013 runs are not yet known when the February 2014 runs reach their cut-offs."),
    ("26", "05-01",
     "Many different models fit about equally well [5], so no coefficient is read as a cause, and AQ2's\n",
     "Many different models, with different coefficients, fit about equally well [5]; the chosen\n"
     "model's coefficients are one of many sets that fit the data, so no coefficient is read as a cause, and AQ2's\n"),
    ("27", "05-02",
     "Risk and benefit can also diverge, as field experiments in customer retention showed\n[20].",
     "Risk and benefit can also diverge: the students at highest risk do not always benefit\n"
     "most, as field experiments in customer retention showed [20]."),
    ("28", "05-02",
     "a randomised pilot whose time zero is the\ncut-off at which",
     "a randomised pilot whose time zero, the\nmoment from which every student in the pilot is followed, is the cut-off at which"),
    ("29", "06-00",
     "since non-completion is 44–46% |",
     "since non-completion is 44–46% and the classes are therefore not imbalanced |"),
    ("30", "10-01",
     "| Same, with module effects drawn from a population of modules |",
     "| Same, with module effects drawn from a population of modules (random effects) |"),
    ("31", "10-01",
     "all runs of these modules observed, so fixed effects suit the design [12]",
     "all runs of these modules observed, not sampled, so fixed effects suit the design [12]"),
    ("32", "10-01",
     "| Non-informative censoring; a competing-risk",
     "| Non-informative censoring (a student is censored when follow-up stops before withdrawal is observed, and the reason it stops is assumed unrelated to the risk of withdrawal); a competing-risk"),
    ("33", "10-01",
     "maintenance and entanglement risks [10]",
     "maintenance and entanglement risks, entanglement being the dependence of a system's parts on each other [10]"),
    ("34", "10-01",
     "the background-only model shows how much",
     "the background-only model, which uses no activity, shows how much"),
    ("35", "10-03",
     "in outer and inner loops alike |",
     "in outer loops (the cross-validation used to evaluate and choose the model) and inner loops (the cross-validation run inside each training fold to tune hyperparameters, step 3) alike |"),
    ("36", "10-03",
     "tuned by an inner leave-one-run-out loop;",
     "tuned by nested cross-validation, an inner leave-one-run-out loop run on the training runs of each fold;"),
    ("37", "10-03",
     "unattractive, since shrinkage does not rescue small\nsamples [17].",
     "unattractive, since each module's data are small\nand shrinkage does not rescue small samples [17]."),
    ("38", "10-04",
     "a reference from group labels shuffled within run [34] |",
     "a reference from group labels shuffled within run, the ABROCA that chance alone can produce [34] |"),
    ("39", "10-05",
     "| Conformity assessment before use [49];",
     "| Conformity assessment, the procedure that assesses a high-risk AI system before it is put into use [49];"),
    ("40", "10-06",
     "non-informative censoring stated as an assumption |",
     "non-informative censoring (follow-up stopping for reasons unrelated to the risk of withdrawal) stated as an assumption |"),
    ("41", "10-06",
     "| Calibration-in-the-large with offset; pooled bounds;",
     "| Calibration-in-the-large defined as the intercept with the score's log-odds as offset (coefficient fixed at 1); bounds on the estimates pooled over all runs;"),
    ("42", "10-06",
     "removal in all loops |",
     "removal in all loops, outer and inner |"),
    ("43", "10-07",
     "| enrolment, assessment_due; population",
     "| enrolment and assessed-task views (enrolment, assessment_due); population"),
    ("44", "10-07",
     "| features_d13, features_d27, model_ready; 19",
     "| the two feature views (features_d13, features_d27) and the model-ready matrix (model_ready); 19"),
    ("45", "10-07",
     "| AQ3 scores; capacity_by_run |",
     "| AQ3 scores; list lengths by capacity for each run (capacity_by_run) |"),
    # Twin edit matching row 4 (delivery mode)
    ("4-vi", "01-01vi",
     "bỏ phép so sánh theo hình thức học (trực tuyến hoặc kết hợp) và theo năm theo học của sinh viên",
     "bỏ phép so sánh theo hình thức học, vốn không khác nhau trong OULAD vì mọi kỳ mở đều là đào tạo từ xa, và theo năm theo học của sinh viên"),
]


def main() -> int:
    texts = {}
    for row, key, old, new in EDITS:
        path = REPORT / F[key]
        text = texts.get(key) or path.read_text(encoding="utf-8")
        n = text.count(old)
        assert n == 1, f"row {row} ({F[key]}): old string occurs {n} times: {old[:80]!r}"
        texts[key] = text.replace(old, new)
        print(f"row {row:>4}  {F[key]}  applied")
    for key, text in texts.items():
        (REPORT / F[key]).write_text(text, encoding="utf-8")
    print(f"{len(EDITS)} edits in {len(texts)} files written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
