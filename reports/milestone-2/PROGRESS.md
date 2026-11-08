# Progress: From Requirements to Collection: Data Requirements, Open Dataset Selection and Reproducible Collection

Current task: none       Last checkpoint: none

Protocol: LOAD → DO → WRITE → VERIFY → DECIDE (stop and ask on any failed item) → CLOSE → FREE (EXECUTION_PLAN.md Section 4). Resume with `progress.py --base reports/milestone-2 next`.

| ID | Task | Status | Outputs | Verified by | Handoff note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| T01 | Scaffold workspace and register the task | done (2026-11-06) | plan.toml, EXECUTION_PLAN.md, report/, research/, tasks.toml [milestone-2] | scaffold.py check: 29 files, 24 tasks, 0 errors | Same layout and VI glossaries as milestone-1. |
| T02 | Scope inputs – decided in conversation | done (2026-11-06) | Decisions in PROGRESS.md | User instruction 2026-11-06 | Follow brief M2 strictly; drive decision to OULAD through a fair search; use OULAD exploration as support; M1 report = baseline; old M2 docx ignored; sequential, parallel only when independent. |
| T03 | Seeds: brief, OULAD sources, Milestone 1 baseline | done (2026-11-06) | S001 brief (local), S002-S003 OULAD | check_trail --all: 0 errors | S001 fetched from repository worktree. |
| T04 | Freeze the Milestone 1 baseline (step 1) | done (2026-11-06) | research/baseline/m1-baseline.md, code/freeze_baseline.py | logs/T04_freeze.log: 8 M1 files hashed; goal, SMART, KPI table, AQ1-AQ4, Tables 5.1, 6.1, 7.1 copied verbatim | Baseline frozen; any change goes to Change Log (Appendix V). |
| T05 | Data Requirement Specification, levels, leakage table (Tasks 1-2) | done (2026-11-06) | research/requirements/data-requirements.md | 9 Task-1 fields per AQ (4), AQ-Data matrix, leakage table, level table, gates G1-G5; written before any dataset was examined | Gates: G1 outcome incl. withdrawal; G2 within-semester timing; G3 >=3 semesters; G4 open license+docs; G5 anonymised. |
| T06 | Dataset search: at least 3 candidates, official pages, licenses (Task 3; S300-S399) | done (2026-11-06) | S300-S309, part3 claims, search/candidates.md, search/search-log-brief.md | check_trail --task T06: 10 sources, 0 errors; 7 candidates; 16 log rows | Only OULAD passes G1-G4; G5 partly (persistence of id across runs to check in data). |
| T07 | AI requirement critic on the data requirements | done (2026-11-06) | research/reviews/02-ai-requirement-critic-prompt.md, requirement-critic.md, requirement-critic-decisions.md; data-requirements.md revised | 12 critiques: 10 accepted, 2 partly; applied before scoring | Gates now G1 (incl. dated withdrawal), G2a, G2b, G3 (ordered runs), G4, G5 (persistent id). Section 6 lists clauses that become Partial. |
| T08 | Scoring and selection matrix (Task 4) | done (2026-11-06) | research/selection/selection.md | 10-criteria scoring with claim IDs for 7 candidates; brief matrix; gates | OULAD 12/20, only candidate meeting G1/G2/G4 on documentation; conditional on Task 6. |
| T09 | AI selection reviewer on the matrix | done (2026-11-06) | research/reviews/03-ai-selection-reviewer-*.md | 10 critiques, all accepted; selection.md revised | Scores rescaled to recorded evidence; Task 6 must confirm G1 values, G3 per module, G5 linkage, early tasks, day<=0 unregistration. |
| T10 | Acquisition plan and Data Collection Package (Task 5) | done (2026-11-06) | package/README.md, src/collect.py, metadata/{source.md,citation.bib,data_dictionary.md,raw_manifest.csv,collection_log.txt}; code/compare_mirrors.py | logs/T10_collect.log: archive + 7 tables SHA-256 MATCH; logs/T10_mirrors.log: UCI copy same data ('?' for missing), OU page link 404 | Primary copy figshare v1 DOI 10.6084/m9.figshare.5081998.v1; access 2026-11-05. |
| T11 | Initial structural verification script and results (Task 6) | done (2026-11-06) | package/src/verify_structure.py, metadata/structure_report.md, structure_results.json | logs/T11_structure.log: 7 tables read; keys unique; 0 orphans; selection conditions computed | G1 confirmed (Pass/Distinction/Fail/Withdrawn; 10,063 dated). G5 confirmed (1,309/1,309 repeats). G3: >=3 runs for BBB,DDD,FFF(4),EEE,GGG(3); AAA,CCC 2; B/J separate: max 2 per type. Docs vs file: length->module_presentation_length; Withdrawal->Withdrawn; 787,170 exact dup click rows. Early tasks: 16/22 by day 27, 1/22 by day 13. Day-14 registered 28,119; 3,097 unregistered <=0. |
| T12 | Coverage, traceability, gaps and Change Log (Task 7) | done (2026-11-06) | research/coverage/coverage.md | facts from structure_results.json; matrices use only real variables; C01-C08 each with data evidence | All AQs Partial; AQ4 action None. Cut-offs day 13 and 27; denominator day 14 (28,119); time test on 9 module-start pairs 2013->2014; fairness via imd_band, disability. |
| T13 | Write Parts 1-2 | done (2026-11-06) | report/01-00..02-03 | check_drafts 0 errors | Tables 1.1, 2.1 (with gates G1-G5), 2.2, 2.3. Part 2 is dataset-agnostic. |
| T14 | Write Parts 3-6 | done (2026-11-06) | report/03-00..06-00 | check_drafts 0 errors | Tables 3.1, 4.1, 5.1, 6.1. Selection conditional; Section 6 confirms G1, G5; G3 partial. |
| T15 | Write Parts 7-9 and appendices | done (2026-11-06) | report/07-00..09-00, 11-00..11-06, code/build_appendices.py | check_drafts all 29 files: 0 errors; appendices generated, no trail IDs | Tables 7.1-7.3, 9.1, A.1-A.11. |
| T16 | Front matter | done (2026-11-06) | 00-0, 00-1 (12 rows), 00-2 (10 terms), tasks.toml abbreviations | check_abbreviations en: 12, 0 violations | Official title marked '(official title)' to avoid a repeated full form. |
| T17 | References | done (2026-11-06) | report/10-references.md | finalize_refs: 12 sources | first-citation order. |
| T18 | Full gates | done (2026-11-06) | logs/T18_gates.log | EN precheck 7/7 PASS; check_trail 13 sources, 95 claims, 0 errors | VI steps pending T22. |
| T19 | Fact spot-check | done (2026-11-06) | research/spot-check.md | spot_check.py: 10 rows, 0 anchors missing; 10/10 match | Own measurements cited by log/appendix, not references. |
| T20 | Style read-through | done (2026-11-06) | research/style-review.md; fixes across 00-2..11-06; appendix sources | 30 findings applied; EN precheck 7/7 | Terms: course (university) vs module/module run (OULAD), start month; secondary KPI 1/2 named; dates in UTC+7; search prompt added to Appendix VI. |
| T21 | Build and post-check the English Word document | done (2026-11-06) | build/N04_Milestone2_EN.docx | logs/T21_build_en.log: precheck EN 7/7, build, postcheck; 11.0 pages main text | Deliverable B moved to Appendix V (Table A.10); Table 7.3 replaced by a pointer. |
| T22 | Vietnamese twin: terms, front matter, translators, review, consistency, reader test | done (2026-11-06) | report/*.vi.md (29), glossary rows, research/reviews/04-…10-vi-*.md | 4 translators + 4 reviewers; consistency (32 edits); reader test 62 (3/33/26) -> rewrite + 2nd review -> retest 47 (1/26/20) -> targeted rewrite 19 edits; parity 29/29 | Remaining retest findings beyond the ten hardest not re-tested. |
| T23 | Build and post-check every language | done (2026-11-06) | build/N04_Milestone2_EN.docx, N04_Milestone2_VI.docx | logs/T23_make_all.log: 13/13 + tests 2/2; validate.py both PASSED; pages EN 11.2, VI 13.5 | Awaiting user review (T24). |
| T24 | Final review | done (2026-11-06) | build/N04_Milestone2_EN.docx, N04_Milestone2_VI.docx | User review 2026-11-06: 'looks sound for milestone 2' | Accepted at ~11 pages EN. Package and change log C01-C08 are the inputs of Milestone 3. |
| T27 | Tables, lists and Vietnamese rewrite after the user's review | done (2026-11-07) | build/N04_Milestone2_EN.docx, N04_Milestone2_VI.docx; report/*.vi.md (29); research/reviews/11-…16-vi-*.md | Full rewrite from English by 4 translators; 4 native reviews (180 edits); consistency (51 edits); reader test 68 (3/55/10): 45 fixed, 18 in the English, 5 rejected; 45 fixes re-read: 38 pass, 4 rewritten, 3 in the English; logs/fix_tables_lists.log, logs/vi_rewrite_build.log | 18 English problems and the term questions in rewrite2-flags.md await the user. English not changed. |

| T40 | Full rewrite, then move to appendix (user, 2026-11-07) | done (2026-11-07) | report/01-00..09-00 rewritten; front matter; research/revisions/{snapshots.md,01-appendix-decisions.md}; baseline re-frozen; code/build_appendices.py (moved text, Appendix VI kept) | logs/R0..R6: full draft 14.7 → 14.1 pages, 15.1 after reader fixes (VI 16.5); reader test 19 items, 17 fixed; code/count_early_tasks.py (logs/R3); make all 13/13 + tests 2/2 (logs/R5); table audit: overflow only in appendix URLs and checksums | Found: the early-sign rule (two tasks by day 27) applies in 1 of 22 runs, not 16; C06 and Section 7.2 corrected. Awaiting user review. |

## Decisions

- (none yet)

## Blocked

- (none)

## Decisions (T02, 2026-11-06)

- Follow `final-project/milestones/02/milestone-2.md` strictly, task by task; report structure from its section 15.1.
- Baseline: the Milestone 1 proposal in `reports/milestone-1/report/` (English source). The team's earlier
  `milestones/02/N04_Milestone2.*` documents are outdated and not used.
- Datasets: the search covers at least three candidates fairly; the repository's `datasets/` screening folders give
  only names and basic facts. The decision is expected to go to OULAD, but only through the requirements, the gates
  and the matrix. The OULAD exploration (`datasets/oulad/exploration/`) may support statements; the report stays at
  Milestone 2 depth (structure, not analysis).
- Work sequentially; run tasks in parallel only when they do not depend on each other.
- English first, then the complete build-report Vietnamese flow; no _GoogleDocs copy.
