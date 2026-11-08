# Execution Plan: From Understanding to Preparation: Data Understanding, Quality Assessment and Reproducible Data Preparation

Plan date: 2026-11-06. Input outline: [reference.md](reference.md), derived from the instructor brief
`final-project/milestones/03/milestone-3.md`. Outputs: the Milestone 3 report (fine-grained sections in `report/`,
compiled to Word in English and Vietnamese by the build-report skill) and the Prepared Data Package (`package/`).
The machine-readable half of this plan is `plan.toml` (file map, task list, seeds); keep both in step.

## 1. Goal and Scope

The brief asks for one report and one Prepared Data Package, with six deliverables (brief section 16). Each is
mapped to its place in this task:

| Brief deliverable | Content required | Location |
| :---- | :---- | :---- |
| A. Milestone 3 Report | Understanding, profiling, quality issues, AQ–Data fit, preparation decisions, validation, risks, AI use | `report/` → `build/N04_Milestone3_EN.docx`, `N04_Milestone3_VI.docx` |
| B. Updated Traceability | Goal/SMART/KPI → AQ → type → raw variables → preparation → prepared variables/view → decision | Appendix IV (Table A.7) and `package/data/metadata/traceability.md` |
| C. Preparation Pipeline | Scripts that rerun from raw data, no unrecorded manual step | `package/src/` (+ executed notebooks in `package/notebooks/`) |
| D. Prepared Data Package | `data/processed` + dictionary + lineage + version/provenance + validation summary | `package/data/processed/`, `package/data/metadata/` |
| E. Controlled Change Log | Every AQ/scope/claim change caused by data understanding or gaps | Appendix IV (Table A.8, C01–C08 carried, C09… new) and `package/data/metadata/change_log.md` |
| F. AI Decision Log | Prompt/suggestion, team decision, evidence, accepted/rejected | Appendix V and `research/reviews/` |

Outline sections map one to one to report parts (brief section 16.1):

| Outline / brief section | Report part | Included |
| :---- | :---- | :---- |
| 1 Project Baseline & Dataset | Part 1 | yes |
| 2 Data Understanding (Task 1) | Part 2 | yes |
| 3 Data Profiling & Quality (Task 2) | Part 3 | yes |
| 4 AQ–Data Fit & Data Gap Decisions (Task 3) | Part 4 | yes |
| 5 Data Preparation Plan (Task 4) | Part 5 | yes |
| 6 Data Preparation Pipeline (Tasks 5–6) | Part 6 | yes |
| 7 Prepared Data Validation (Task 8) | Part 7 | yes |
| 8 Analytics / Model Readiness (Task 7) | Part 8 | yes |
| 9 Ethics, Bias & Limitations | Part 9 | yes |
| 10 Generative AI Usage & Reflection | Part 10 | yes |

Rules carried over from the project and the brief:

- `CLAUDE.md` style: formal sections, final state only (no process history), cumulative paragraphs, every
  section readable on its own, identifiers paired with their words, tables introduced in the sentence before.
- Every number in the report comes from a script output in `package/data/metadata/`, `package/data/processed/`,
  `results/` or `logs/`, and the file is named next to it in the appendices; the OULAD exploration
  (`datasets/oulad/exploration/`) supports profiling, and its figures are re-computed by the package scripts and
  cross-checked (T08).
- Brief section 4: understand before prepare; raw immutable; question-driven preparation; evidence before
  assumption; reproducibility; no silent revision; no modelling (no model is fitted or tuned).
- AI interviews and critics are AI on both sides, and team members verify; the report never calls them team-run.
- APA 7 references, `[Sxxx]` while drafting, `[n]` after T22. Abbreviations at first use.
- Main text 8–12 pages (brief section 16); appendices, code and data excluded.

### 1.1 Core Rule: Record Every Crawl and Every Run on Disk

Web research follows the research-report trail (search log, crawl, comprehension, claims with verbatim anchors).
Data work follows the same rule: every script run writes its console output to `logs/<task>_<step>.log` with UTC
timestamp, command and exit status, and its results to `package/data/metadata/` or `results/`.

```
report sentence [n] → reference n → sources.md Sxxx → claim → comprehension.md → crawl.md
report number       → appendix / metadata file → script in package/src → logs/<task>.log
```

## 2. Tools Used

| Tool | Purpose in this task |
| :---- | :---- |
| `WebSearch`, `fetch.py`, `WebFetch`, `trail.py` | Research tasks T05, T06 (one foreground subagent each, run as a wave) |
| polars 2.1 (`./venv`) | All data work, including the 10.6M-row `studentVle.csv`; Parquet written natively |
| `package/src/*.py` | Understanding, profiling, preparation, validation (deterministic, rerunnable) |
| Jupyter (`nbformat`, `nbclient`, `ipykernel`, added to the package's `requirements.txt`) | Executed notebooks of brief section 10.1 |
| `Agent` (isolated, foreground) | AI preparation critic (T11) and AI leakage auditor (T14): read files, return critiques; the main agent records decisions |
| build-report (`make precheck/all TASK=milestone-3`, figure toolkit, VI flow) | Checks, figures, Word build, Vietnamese twin |
| `progress.py`, `check_trail.py`, `check_drafts.py`, `finalize_refs.py`, `spot_check.py` | Ledger and gates |

## 3. Target File Map (`report/`)

Section, table and figure numbers are fixed here before writing.

### 3.1 Front Matter

| File | Content |
| :---- | :---- |
| `00-0-title-page.md` | Brief's info table: team, members, project title, M1 version, M2 dataset/version, prepared dataset version, date |
| `00-1-abbreviations.md` | Abbreviations as used |
| `00-2-glossary.md` | Defined terms (enrolment, module run, cut-off, prepared view, GREEN/YELLOW/RED, missing variable, …) |

### 3.2 Parts

| File | Content | Tables / figures | Evidence |
| :---- | :---- | :---- | :---- |
| `01-00` | Part 1 intro: Milestone 3 question and entry gate result | – | T04 |
| `01-01` | Business Goal, SMART, KPIs; AQ1–AQ4 as revised by C01–C08 | Table 1.1 current AQs | `research/baseline/m3-baseline.md` |
| `01-02` | OULAD version, checksums, the six required inputs and their status; entry gate | Table 1.2 inputs from Milestone 2 | T04 log |
| `02-00` | Part 2 intro | – | – |
| `02-01` | Population (who, level, modules, years), unit per table, keys, cardinalities | Table 2.1 Dataset Understanding Map; Figure 2.1 table relationships | T07, S002, S2xx |
| `02-02` | Outcome definition and observation time; day offsets, due vs submission vs registration; clicks, scores, weights, banked | Table 2.2 semantics of key fields | T07, S002, S2xx |
| `02-03` | Codes (`imd_band`, `age_band`, `highest_education`, presentation codes, assessment types); sensitive attributes | Table 2.3 codes and sensitive attributes | T07, S2xx |
| `03-00` | Part 3 intro: what was checked, on full data | – | T08 |
| `03-01` | Shape vs documentation, key uniqueness, duplicates (exact and repeated grain), orphans, join explosion | – | T08 |
| `03-02` | Missingness by variable/group/time; validity (ranges, codes, impossible dates, inconsistencies) | – | T08 |
| `03-03` | Distributions, zero inflation, outliers by statistics and domain, outcome balance by run | Figure 3.1 outcome mix by module run | T08 |
| `03-04` | Temporal coverage (weeks, gaps, cut-off feasibility), representativeness | Figure 3.2 weekly activity coverage | T08 |
| `03-05` | Data Quality Issue Log DQ01… | Table 3.1 | T08, T10, T11 |
| `04-00` | Part 4 intro | – | T09 |
| `04-01` | GREEN/YELLOW/RED per AQ with evidence and action | Table 4.1 AQ–Data fit decision log | T09 |
| `04-02` | Decision procedure (brief 8.1), missing value vs missing variable vs missing label, synthetic-data decision | Table 4.2 missing values vs variables | T09 |
| `05-00` | Preparation Decision Matrix (brief rows: missing, duplicates, categories, outliers, integration, derived, temporal, encoding/scaling, + population, sensitive) | Table 5.1 | T10, T11 |
| `06-00` | Part 6 intro with pipeline overview | Figure 6.1 pipeline from raw to prepared views | T12 |
| `06-01` | Ten steps (brief 10) mapped to scripts; folder structure; run command | Table 6.1 steps → scripts → outputs | T12 |
| `06-02` | Integration (joins, row checks), derived variables with formulas, windows, timestamp rules | Table 6.2 derived features | T12 |
| `06-03` | Split (time, entity), prediction points, train-only fitted transforms, leakage rules | Table 6.3 leakage risks and controls | T12, T14, S6xx |
| `07-00` | Part 7 intro | – | T13 |
| `07-01` | Rows, entities, outcome distribution before/after; keys, ranges, temporal order; manual feature checks | Table 7.1 before/after | T13 |
| `07-02` | Lineage (excerpt), dictionary, version manifest | Table 7.2 lineage excerpt | T13 |
| `07-03` | Residual risks kept on purpose | – | T13, T14 |
| `08-00` | Part 8 intro | – | T15 |
| `08-01` | Views per analytics level: descriptive, diagnostic, predictive, prescriptive | Table 8.1 views by level | T15 |
| `08-02` | Model Readiness Matrix AQ1–AQ4; questions not yet feasible | Table 8.2 | T15 |
| `09-00` | Sensitive variables, fairness audit use, representativeness, data protection, limits of claims | – | T08, S9xx |
| `10-00` | AI roles, accepted/rejected suggestions, verification | Table 10.1 | T11, T14, T15 |
| `11-references` | APA 7, first-citation order | – | T22 |
| `12-00…12-06` | Appendices I–VI (generated by `code/build_appendices.py` from package and research files) | Tables A.1… | T20 |

## 4. Prepared Data Package (`package/`, brief section 10.1)

```
package/
  README.md                 run commands, versions, contents
  requirements.txt          polars, nbformat, nbclient, ipykernel, matplotlib
  data/
    raw/                    the seven OULAD CSVs, hard-linked from the Milestone 2 package; never modified (git-ignored)
    interim/                reproducible intermediates (git-ignored)
    processed/              analytic-ready views, Parquet (git-ignored; rebuilt by run_all.sh)
    metadata/               understanding map, profile, quality log, decision matrix, dictionary, lineage,
                            transformation log, validation summary, version manifest, traceability, change log
  notebooks/                02_data_understanding.ipynb, 03_data_preparation.ipynb (executed)
  src/                      01_understand.py, 02_profile.py, prepare_data.py (+ steps), validate_prepared.py,
                            common.py, run_all.sh
```

Prepared views (fixed names, refined in T10): `enrolment` (one row per enrolment), `assessment_due` (enrolment ×
non-exam assessment), `student_week` (enrolment × week, truncated at withdrawal), `features_d13` and `features_d27`
(one row per enrolment still registered at the cut-off, pre-cut-off features, target, split, audit columns),
`capacity_by_run` (eligible list sizes per run and cut-off for the AQ4 requirement).

## 5. Sequential Task Protocol

LOAD → DO → WRITE → VERIFY → DECIDE (stop and ask on any failed item) → CLOSE → FREE, as in the research-report
skill's reference.md section 1. Resume with `progress.py --base reports/milestone-3 next`. Source IDs: seeds
S001–S002; Part 2 S200–S299 (T05); Part 6 S600–S699 and Part 9 S900–S999 (T06).

**Waves (reference.md section 1.4).** Wave 1 runs T05, T06 and T07 together: T05 and T06 write disjoint source
blocks and claims files (part 2 vs parts 6 and 9) through `trail.py`; T07 writes only `package/src/01_understand.py`,
`package/data/metadata/understanding*` and its log, and reads no research file. Everything else runs one at a time.

## 6. Task Cards

**T01: Scaffold and register.** `scaffold.py build`, `scaffold.py register`; tasks.toml block like milestone-2.
- [ ] `scaffold.py check` 0 errors; `tasks.toml` has `[milestone-3]`.

**T02: HC, scope inputs.** Decided in conversation 2026-11-06 (record under Decisions).

**T03: R, seeds.** S001 brief (local, verbatim copy); S002 OULAD data descriptor (crawl reused from the Milestone 2
trail, header updated). R1–R8.

**T04: Entry gate.** `code/freeze_baseline.py`: copy goal, SMART, KPIs, AQ1–AQ4 (M1) and C01–C08, Table A.10 (M2)
verbatim, hash the source files; `package/src/link_raw.py`: hard-link the seven CSVs from the Milestone 2 package,
check SHA-256 against `raw_manifest.csv`, set them read-only.
- [ ] `research/baseline/m3-baseline.md` written; `logs/T04_*.log` shows 7/7 MATCH; six brief inputs listed with status.

**T05: R, OULAD semantics (Part 2–3).** Questions: (1) what are TMA, CMA and Exam at the OU, who marks them and when
are marks released; (2) what do `code_presentation` B/J and the run-start mean; (3) how is `imd_band` defined, and
does it exist for Scotland, Wales and Ireland; (4) what do `is_banked`, `weight`, `date` = due day, `sum_click`,
`activity_type`, `week_from/week_to` mean according to the descriptor or the OU; (5) any documented known issues
(duplicates, missing exam scores). R1–R8.

**T06: R, practice and ethics (Parts 6, 9).** Questions: (1) how published OULAD/OU Analyse early-warning work sets
the prediction point and training data (previous presentation vs current, e.g. Hlosta et al. 2017); (2) data
leakage definitions (target, train–test, temporal) from a primary source; (3) fairness auditing with sensitive
attributes in learning analytics (keep for audit vs use as predictor); (4) Vietnam's Personal Data Protection Law
91/2025/QH15 on sensitive personal data, reused from the Milestone 1 trail (S267). R1–R8.

**T07: Task 1 understanding.** `package/src/01_understand.py` → `data/metadata/understanding_map.md`,
`understanding.json`: per table unit, PK, FK and cardinality (1–1, 1–N), main variables, time fields, role in AQ;
semantics checks on data (banked submissions' dates, due-day vs run length, negative days, outcome vs unregistration,
codes and their counts, sensitive attributes present).
- [ ] Every table has all seven Map columns, each key/cardinality claim backed by a computed check; log saved.

**T08: Task 2 profiling and quality.** `package/src/02_profile.py` → `data/metadata/profile.json`,
`quality_issue_log.md` (DQ01…, draft decisions), figure data. All ten brief aspects (shape, missingness incl. by
group and time, duplicates/keys, validity, distribution, outliers, outcome balance, temporal coverage, join
integrity incl. explosion test, representativeness). Cross-check ≥ 10 numbers against `datasets/oulad/exploration/results/`.
- [ ] Every brief aspect has ≥ 1 computed result; every DQ row has evidence, impact on AQ, severity; cross-check log equal.

**T09: Task 3 AQ–Data fit.** `research/fit/aq-data-fit.md`: per AQ the rating, evidence, procedure step reached
(brief 8.1, steps 1–6), action; missing value vs missing variable table; synthetic-data decision; new Change Log
entries from C09.
- [ ] Each AQ rated with evidence from T07/T08 files; no rating rests on AI statements; change log rows complete.

**T10: Task 4 decision matrix and specification.** `research/preparation/decision-matrix.md` (all brief rows plus
population and sensitive attributes), `feature-spec.md` (each derived variable: formula, source fields, window,
timestamp rule, AQ), `split-spec.md` (time split, entity rule, fitted transforms).
- [ ] Every DQ issue maps to one matrix row; every feature has a cut-off rule; no rule uses test outcomes.

**T11: AI preparation critic.** Isolated agent reads the DQ log, matrix and specifications only; returns numbered
critiques. Main agent decides each (accept / reject / partly) with evidence, updates the files.
- [ ] Prompt, critiques and decisions saved in `research/reviews/`; each decision cites evidence.

**T12: Tasks 5–6 pipeline.** `package/src/prepare_data.py` with the ten brief steps as functions, transformation
log, row-count checks at each join, writes `interim/` and `processed/`; `fit_transforms.py` fits imputation and
scaling parameters on the training partition only and stores them; `run_all.sh`.
- [ ] Full run from raw exits 0; `logs/T12_prepare.log` shows each step's row counts; rerun gives identical hashes.

**T13: Task 8 validation and package metadata.** `package/src/validate_prepared.py`: before/after rows, entities,
outcome distribution; missingness; key uniqueness; join coverage; ranges; temporal order; cut-off compliance
(no event after the cut-off in feature views); manual recomputation of ≥ 5 sampled enrolments from raw; writes
`validation_summary.md/json`; `data_dictionary.md`, `lineage.md`, `version_manifest.json`.
- [ ] All checks PASS or are explained; dictionary covers every prepared column with source, transformation, type,
  role and sensitivity.

**T14: AI leakage auditor.** Isolated agent reads the code, feature spec and processed schemas and recomputes a
sample; returns findings. Main agent decides and fixes; rerun T12–T13 if code changes.
- [ ] Findings and decisions saved; validation reruns clean after fixes.

**T15: Task 7 and deliverables B, E, F.** `research/readiness/readiness.md` (views per level, Model Readiness
Matrix), `package/data/metadata/traceability.md`, `change_log.md`, `research/ai-decision-log.md`.
- [ ] Every AQ has a view, target/measure, features, split rule, readiness; traceability uses real prepared columns.

**T16: Notebooks.** `package/notebooks/02_data_understanding.ipynb`, `03_data_preparation.ipynb`, built by
`package/src/build_notebooks.py`, executed with nbclient; they call the package functions and display the results.
- [ ] Both execute without error; outputs agree with metadata files.

**T17: F, figures.** Builders in `figures/milestone_3/`: Figure 2.1 table relationships, 3.1 outcome mix by module
run, 3.2 weekly activity coverage, 6.1 pipeline. F1–F5.

**T18–T20: W, writing.** Parts 1–3; Parts 4–6; Parts 7–10 and appendices (`code/build_appendices.py`). W1–W10.

**T21–T29: finishing.** Front matter; references; full gates; spot-check; style read-through; build EN; Vietnamese
twin (build-report flow 4.3: terms, front matter, translators, native review by another agent, consistency, reader
test, rewrite, second review, retest); build every language; final review.

## 7. Human Checkpoints

| When | Why it stops |
| :---- | :---- |
| Any unticked checklist item | The user decides how to continue |
| Any conflict between a source and the brief or baseline | The user decides |
| Final review (T29) | Acceptance |

The user asked for the plan to be executed straight through (2026-11-06); part reviews are folded into the final
review unless a check fails.

## 8. Deliverables

| Deliverable | Location |
| :---- | :---- |
| Plan and ledger | `EXECUTION_PLAN.md`, `plan.toml`, `PROGRESS.md` |
| Report sections | `report/*.md`, `report/*.vi.md` |
| Word reports | `build/N04_Milestone3_EN.docx`, `build/N04_Milestone3_VI.docx` |
| Prepared Data Package | `package/` |
| Research trail and reviews | `research/` |
| Run logs | `logs/` |
