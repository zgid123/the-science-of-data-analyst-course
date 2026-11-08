# Part 7 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 07-00-preparation-pipeline.md

**Milestone evidence (T06):**
- Claims: C7-001, C7-005, C7-002, C7-003, C7-004, C7-007, C7-025.
- Brief requirement (section 2, Part 7): cleaning, transformations, joins, derived variables, encoding, missing handling, leakage control, final dataset/version; evidence = Preparation Decision Matrix + reproducible pipeline; self-check "every step has a reason and leaks nothing".
- Outline: (1) the Preparation Decision Matrix: every issue and need decided before any record changed, checks V01–V15 (C7-001); (2) the three governing decisions: nothing recorded deleted or imputed in the views, features dated on or before the cut-off, parameters from training runs only (C7-005); (3) population rule C09 and the populations 28,061 / 28,069 / 27,535 (C7-002); (4) missing values and outliers kept with indicators, filling and logs only in matrices (C7-003, C7-004); (5) integration by left joins after summing to the enrolment, 25 joins kept their rows; the ten scripted steps with their counts (C7-007, C7-025).
- Conflicts with the outline: None.
- Gaps: None.

## 07-01-features-leakage.md

**Milestone evidence (T06):**
- Claims: C7-008, C7-009, C7-010, C7-011, C7-012, C7-033, C7-023, C7-027, C7-013, C7-026, C7-032, C7-014, C7-035, C7-015, C7-034, C7-016, C7-019.
- Brief requirement: derived variables, encoding, leakage control.
- Outline: (1) timing rule and the CMA-mark rule (C7-008); (2) derived variables table: target, enrolled flags, click and activity features, activity ratio, missed and late tasks, early-sign rule C10, first missed week (C7-009–C7-011); (3) predictor sets: 20 primary (19 usable, CMA score below 10% coverage), 10 extended, weekly clicks; raw clicks primary, de-duplicated twin as sensitivity (C7-012, C7-033, C7-023, C7-027); (4) encoding: views keep original scales; linear-model matrices with ordinal/one-hot/log/median/standardise from training rows; only predictor_sets columns are model inputs (C7-013, C7-026, C7-032); (5) leakage controls by form and the 2013/2014 split with the paired subset and in-2013 tuning; V13 can fail (C7-014, C7-035, C7-015, C7-034, C7-016, C7-019).
- Conflicts with the outline: None. Between milestones: (a) Milestone 3 counts 20 primary predictors, Milestone 4 uses 19 (the mean CMA score left out) with 23 parameters (C7-012 vs C8-011, C8-025); (b) Milestone 3 fitted the model-ready matrices once on all 2013 runs with one-hot modules (C7-026), whereas the Milestone 4 protocol refits every transform inside each fold with deviation-coded modules and does not use those matrices as model input (C10-011; S106). The final text should state the Milestone 4 rule for modeling and present the Milestone 3 matrices as prepared artefacts. (c) Students seen in 2013: 1,962 test enrolments overall (C7-016, C7-036) against 1,586 at day 27 (C9-015); name the population with each number.
- Gaps: None.

## 07-02-prepared-dataset.md

**Milestone evidence (T06):**
- Claims: C7-017, C7-018, C7-036, C7-020, C7-021, C7-038, C7-030, C7-022, C7-028, C7-006, C7-029, C7-031, C7-037, C7-024.
- Brief requirement: final dataset/version, reproducible pipeline; Final Project Package (section 7): source + provenance/licence, prepared dataset or access instructions, data dictionary, README.
- Outline: (1) validation: 22 checks V01–V15 all pass; before-and-after table; 0 differences on 55,604 recomputed feature rows (C7-017, C7-018, C7-036); (2) dictionary with roles and the 88-variable lineage; V14 guards drift (C7-020); (3) version OULAD-N04-prepared-1.0: manifest with SHA-256 of raw, code and outputs, Python 3.12.7, polars 2.1.0; views and their row counts (C7-021, C7-038, C7-030); (4) reproducibility: read-only raw files checked by hash, download from the figshare DOI when absent, one command, byte-identical reruns; licence CC BY 4.0 (C7-022, C7-028, C7-006, C7-029, C7-031); (5) KPI sensitivity without the 138 flagged enrolments (C7-037) and synthetic data only at level A (C7-024).
- Conflicts with the outline: None. Between milestones: rerun time "about 20 seconds" (Milestone 3 report) against "about 15 seconds" (package README); do not quote a run time.
- Gaps: the manifest records that the package had uncommitted changes when it was created (C7-038); the Final Project Package (T21) should rebuild the prepared data from a committed state and state the version and hashes it ships with.
