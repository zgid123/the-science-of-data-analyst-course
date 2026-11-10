"""T16: one-off edits that make every abbreviation of the report follow the first-use convention
(check_abbreviations.py is line-based: a definition must sit on the same line as the first use).
Each replacement must match exactly the expected number of times; run from the project root."""
import re, sys, pathlib
R = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "reports/milestone-5/report")
EDITS = [  # (file, old, new, count)
 ("01-01-motivation-stakeholders.md", "generative AI took both sides", "generative artificial intelligence (AI) took both sides", 1),
 ("01-02-scope-objective.md", "analysis uses the Open\nUniversity Learning Analytics Dataset (OULAD)", "analysis uses the\nOpen University Learning Analytics Dataset (OULAD)", 1),
 ("02-00-business-understanding.md", "The SMART Goal (specific,\nmeasurable, achievable, relevant and time-bound) makes", "The\nSMART Goal (specific, measurable, achievable, relevant and time-bound) makes", 1),
 ("03-00-analytical-questions.md", "Four questions (AQ1–AQ4) supply", "Four analytical questions (AQ), AQ1–AQ4, supply", 1),
 ("04-01-dataset-selection.md", "pinned SHA-256 checksums", "pinned SHA-256 (Secure Hash Algorithm, 256-bit) checksums", 1),
 ("04-01-dataset-selection.md", "Milestone 2 searched data repositories", "Milestone 2 searched data repositories, among them the University of California, Irvine (UCI) Machine Learning\nRepository,", 1),
 ("05-00-dataset-description.md", "modules of the Open University, coded AAA", "modules of the Open University in the United Kingdom (UK), coded AAA", 1),
 ("09-00-evaluation-design.md", "following the\nTRIPOD+AI guideline, which", "following the\nTRIPOD+AI guideline (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis, updated for AI),\nwhich", 1),
 ("11-05-decision-support.md", "Final answers by Analytical Question", "Final answers by question", 1),
 ("13-00-genai-reflection.md", "This follows the UNESCO guidance on generative AI", "This follows the guidance of the United Nations Educational, Scientific and Cultural Organization (UNESCO)\non generative AI", 1),
 ("16-01-context-stakeholders.md", "learning management system (LMS), the web platform", "LMS, the web platform", 1),
 ("16-01-context-stakeholders.md", "so the analysis uses the Open University Learning Analytics Dataset\n(OULAD), selected", "so the analysis uses OULAD, selected", 1),
 ("16-01-context-stakeholders.md", "Open University in the United Kingdom in", "Open University in the UK in", 1),
 ("16-01-context-stakeholders.md", "narrowed how the analytical questions are measured", "narrowed how the questions are measured", 1),
 ("16-01-context-stakeholders.md", "In massive open\nonline courses (MOOCs)", "In\nmassive open online courses (MOOCs)", 1),
 ("03-00-analytical-questions.md", "**Table 3.1. Final analytical questions**", "**Table 3.1. Final questions AQ1–AQ4**", 1),
 ("16-02-goal-kpis-decisions.md", "the full definition of each key performance indicator,", "the full definition of each KPI,", 1),
 ("16-02-goal-kpis-decisions.md", "(a\ntutor-marked or computer-marked assessment)", "(a TMA\nor CMA)", 1),
 ("16-02-goal-kpis-decisions.md", "a tutor-marked assignment (TMA) late", "a TMA late", 1),
 ("16-02-goal-kpis-decisions.md", "Section 3 states the analytical questions that supply", "Section 3 states the four questions, AQ1–AQ4, that supply", 1),
 ("16-03-aq-quality-revision.md", "a tutor-marked assignment (TMA) and a computer-marked assessment (CMA) are", "a TMA and a CMA are", 1),
 ("16-03-aq-quality-revision.md", "checked across IMD band and disability", "checked across deprivation band and disability", 1),
 ("16-04-requirements-selection.md", "interaction with a learning management system or virtual", "interaction with an LMS or virtual", 1),
 ("16-04-requirements-selection.md", "and dropout from massive open online courses)", "and dropout from MOOCs)", 1),
 ("16-04-requirements-selection.md", "Milestone 2 searched the University of California, Irvine (UCI) Machine Learning", "Milestone 2 searched the UCI Machine Learning", 1),
 ("16-04-requirements-selection.md", "A, the Open University Learning Analytics Dataset (OULAD); B,", "A, OULAD; B,", 1),
 ("16-04-requirements-selection.md", "the XuetangX MOOC dropout data", "the XuetangX dropout data from MOOCs", 1),
 ("16-04-requirements-selection.md", "(Vietnam time, UTC+7)", "(Vietnam time, UTC+7, seven hours ahead of Coordinated Universal Time)", 1),
 ("16-06-profile-quality.md", "the primary key performance indicator (KPI),", "the primary KPI,", 1),
 ("16-06-profile-quality.md", "computer-marked assessment (CMA) scores against 17.4% of tutor-marked assignment (TMA) scores", "CMA scores against 17.4% of TMA scores", 1),
 ("16-06-profile-quality.md", "seven Open University (OU) modules", "seven Open University modules", 1),
 ("16-06-profile-quality.md", "subset of OU students", "subset of Open University students", 1),
 ("16-06-profile-quality.md", "The deprivation band (IMD band) is blank", "The deprivation band, from the Index of Multiple Deprivation (IMD), is blank", 1),
 ("16-07-preparation-leakage.md", "the time in Coordinated Universal Time (UTC) and", "the time in UTC and", 1),
 ("16-07-preparation-leakage.md", "following the OU practice", "following the Open University's practice", 1),
 ("16-09-evaluation-detail.md", "the areas under the ROC and precision-recall curves", "the areas under the receiver operating characteristic (ROC) and precision-recall curves", 1),
 ("16-11-reading-traceability.md", "one row per final Analytical Question", "one row per final question", 2),
 ("16-11-reading-traceability.md", "Final status of each Analytical Question and", "Final status of each question and", 1),
 ("16-12-aq1-results.md", "a tutor-marked assignment (TMA) or computer-marked assessment (CMA) that", "a TMA or CMA that", 1),
 ("16-13-aq2-results.md", "±2 SE band |", "±2 standard-error band |", 1),
 ("16-13-aq2-results.md", "±2 SE bands", "±2 standard-error bands", 1),
 ("16-14-aq3-aq4-answers.md", "the final answers by Analytical Question with", "the final answers by question with", 1),
 ("16-14-aq3-aq4-answers.md", "the final answer to each Analytical Question,", "the final answer to each question,", 1),
 ("16-14-aq3-aq4-answers.md", "Final answers by Analytical Question with", "Final answers by question with", 1),
 ("16-14-aq3-aq4-answers.md", "outside ±2 SE in all", "outside ±2 standard errors in all", 1),
 ("16-15-limitations-future.md", "Residuals outside ±2 SE by", "Residuals outside ±2 standard errors by", 1),
 ("16-15-limitations-future.md", "the Open University in the United Kingdom", "the Open University in the UK", 0),
 ("16-05-dataset-gaps.md", "distance learning in the United Kingdom", "distance learning in the UK", 1),
 ("16-16-ai-decision-log.md", "the phases of CRISP-DM,", "the phases of the Cross-Industry Standard Process for Data Mining (CRISP-DM),", 1),
]
bad = 0
for f, old, new, n in EDITS:
    p = R / f; s = p.read_text(encoding="utf-8"); c = s.count(old)
    if new in s and (c == 0 or old in new):
        print(f"done already  {f}: {old[:50]!r}"); continue
    if c != n:
        print(f"MISMATCH {c}!={n}  {f}: {old[:60]!r}"); bad += 1; continue
    if n:
        p.write_text(s.replace(old, new), encoding="utf-8"); print(f"edited x{n}  {f}: {old[:50]!r}")
sys.exit(1 if bad else 0)
