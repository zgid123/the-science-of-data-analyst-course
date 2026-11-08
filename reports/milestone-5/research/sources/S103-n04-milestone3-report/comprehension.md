# S103 – N04 (2026). Milestone 3 report: data understanding, quality and preparation (team's own submitted report)

## Summary in my own words

The Milestone 3 report is the team's own record of how OULAD was understood, profiled and prepared. It sets the enrolment (one student in one module run) as the unit of analysis, profiles all 10.9 million rows of the seven raw tables and gathers nineteen quality issues (DQ01–DQ19) into a Data Quality Issue Log with severity and decision, three of them High (missing exam results, few tasks due by the cut-offs, narrow population). It rates the four questions against the data (AQ1–AQ3 YELLOW, AQ4 RED), records changes C09–C13, and builds a scripted, rerunnable pipeline that produces the prepared dataset OULAD-N04-prepared-1.0 with views per analytics level, a 2013/2014 time split and leakage controls validated by 22 checks (V01–V15), all passing. It closes with ethics (sensitive attributes kept for audit, k-anonymity, Vietnamese data-protection law), the limits of the claims and an AI Decision Log of thirteen entries.

## Key facts

- Scale and grain – "The dataset holds 22 module runs of seven Open University (OU) modules from 2013 and 2014, with 32,593 student"
- Unit of analysis – "The unit of analysis is the enrolment, one student in one module run, because the outcome, the"
- Keys – "The six tables with a key have no duplicate key, and no row of a child table lacks its parent row"
- Profile coverage – "It ran on all 10.9" and "all thirteen agree"
- Duplicate click rows (DQ01) – "rows (7.39%) repeat another row exactly, 3.19% of all clicks"
- Missing deprivation band (DQ12) – "The deprivation band is blank for 1,111"
- Skewed activity (DQ16) – "per enrolment the median is 602 clicks, 3,365 enrolments have none, 2,503 lie beyond the"
- Outcome balance – "Of the 28,061 enrolments registered by day 14 and not unregistered by it,"
- Tasks due by the cut-offs (DQ18) – "a TMA or CMA falls due by day 13 in only 1 of the 22 runs and by day 27 in 16"
- Representativeness (DQ19) – "OULAD is a subset of OU students of 2013–2014, reduced by anonymisation"
- Severity rule – "High marks an issue that would change a reported rate, the target or a feature at a cut-off if it were"
- Early-sign rule restated (C10) – "a task due by the cut-off not submitted, or a TMA submitted late, or no platform"
- Timing rule – "Every feature uses only records dated on or before its cut-off."
- Validation – "runs 22 checks under fifteen identifiers, V01 to V15, against the raw files and the"
- Reproducibility – "Run twice from the raw files, it wrote byte-identical outputs in all eight data files,"
- Version – "The version manifest names the prepared dataset OULAD-N04-prepared-1.0 and records the SHA-256 checksum"
- CMA score not used – "marks known by the cut-off exist for only 1.4% of training rows at day 13 and 5.2% at day 27, below the 10% coverage"
- Readiness – "Revise: the ranking is ready; the choice of contact is deferred"
- Privacy – "OULAD was anonymised with k-anonymity, k = 5"
- Riazy S., Simbeck K. & Schreck V. (CSEDU 2020; not registered here) reported for OULAD "a disparate impact of five to six percentage points in favour of male students"
- AI use – "AI was never treated as a source of data"
- AI reviews – "The preparation critic raised 12 critiques, of which we accepted 9 and"

## Used in

06-00-data-understanding.md, 06-01-quality-findings.md, 06-02-representativeness-sensitive.md, 07-00-preparation-pipeline.md, 07-01-features-leakage.md, 07-02-prepared-dataset.md, 08-00-modeling-strategy.md, 12-00-limitations.md, 12-01-future-work.md, 13-00-genai-reflection.md.

## Against reference.md

Confirms the outline's Part 6 list ("Distributions, missingness, duplicates, invalid values, outliers, imbalance, temporal coverage, representativeness, sensitive fields; the quality findings that could change a conclusion"): every aspect is covered, and the three High issues (DQ08, DQ18, DQ19) are the ones that could change a conclusion. Confirms Part 7 ("Cleaning, transformations, joins, derived variables, encoding, missing handling, leakage control; final prepared dataset and version; reproducible pipeline") with the Preparation Decision Matrix, Table 6.1 and the version manifest. Extends the outline's baseline "Change Log C01–C14 and onwards": Milestone 3 itself ends at C13; C14 is added in Milestone 4 (S104).

## Reliability

Primary: the team's own submitted report (N04, MTH045, University of Science, VNU-HCM), copied verbatim from the repository at commit 19d35a4. Its numbers come from scripts (profile, pipeline, validation) recorded in the Prepared Data Package (S105). No external citation traction applies (team coursework; as of 2026-11-08).

## Open questions

- The rerun time is stated as "about 20 seconds" here and "about 15 seconds" in the package README (S105); the writer should avoid quoting a run time or pick one.
- The 1,962 test enrolments of repeat students (all test enrolments) differ from the 1,586 at day 27 quoted in Milestone 4 (S104); both are correct for different populations and must be named with their population.
