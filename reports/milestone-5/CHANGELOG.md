# Changelog – AQ3 and AQ4 into Milestone 5

This file lists every change made to `reports/milestone-5/` to bring AQ3 and AQ4 from `reports/experiment/` into the Milestone 5 package and report, following the AQ1/AQ2 pattern, so that Khanh can check each one.

## Status

Done (2026-11-13), not committed. Part A (package) and Part B (report, English and Vietnamese, Word build) are complete; every check passes. For Khanh's review: the decisions below, Change Log C18, and the page budget note in B4.

## Decisions taken for this change

| Decision | Choice | Why |
| :---- | :---- | :---- |
| Which AQ3/AQ4 run enters the report | The team's Level 2 experiment (`reports/experiment/`), ported into the package | Independent reviewer, second code path, clean-copy reproduction; same verdicts as the Milestone 4 draft package (`reports/experiment/comparison.md`) |
| Tuning criterion of the penalty and tree settings | Pooled log loss of an inner leave-one-run-out loop (new Change Log entry C18) | The Milestone 4 plan says "tuned by nested cross-validation" without a measure; the Milestone 4 draft tuned on recall at capacity. Log loss is a proper scoring rule and suits the calibration condition S3. Chosen after both results were seen; the draft's result (S3 not met) is reported beside it |
| AQ1 and AQ2 | Unchanged | Khanh's Milestone 5 results stay as they are; nothing from `reports/experiment/` replaces them |
| Existing package steps 00–18 and `results/checksums.csv` | Unchanged | The new work is added after step 18, with its own checksum file |
| Per-enrolment scores and fitted models | Kept in `data/interim/aq3/` (git-ignored, rebuilt by `run_all.sh`), not shipped | Like the raw and interim data; `results/` holds aggregated tables only |

## Part A – package (`package/`)

### A1. Layout of the AQ3/AQ4 results

AQ3 and AQ4 use the same four result folders as AQ1 and AQ2, with files named `aq3_*` and `aq4_*`. Because the two years play different roles in a predictive test, each folder holds scores from a model that did not see its runs:

| Folder | AQ3/AQ4 content | How to read |
| :---- | :---- | :---- |
| `results/2013/` | Model choice (`aq3_dev_folds.csv`, `aq3_dev_choice.csv`, `aq3_final_tuning.csv`, `aq3_choice.json`, `aq3_coefficients.csv`) and the views of the 9 runs of 2013, each run scored by the leave-one-run-out model that left it out | Development estimates; the plan uses them to choose the model, not to state its performance |
| `results/2014/` | The single test of the models frozen on 2013 (`aq3_s1_gate.csv`, `aq3_sensitivity.csv`, `aq3_calibration_bins.csv`, `aq3_lead_time.csv`, `aq4_reasons.csv`, `aq4_fairness_confirmatory.csv`) and the same views | The test; every AQ3/AQ4 number of the report comes from here |
| `results/all_runs/` | The same views on the 22 runs, each scored by a model that did not see it | Description; no model is fitted on all 22 runs |
| `results/compare/` | `aq3_dev_vs_test.csv`, `aq4_dev_vs_test.csv`, `aq3_summary.md` | 2013 development against the 2014 test; cannot change S1 |

The views written for `2013/`, `2014/` and `all_runs/` have the same names: `aq3_by_run.csv`, `aq3_pooled.csv`, `aq3_discrimination_calibration.csv`, `aq3_capacity_curve.csv`, `aq3_model_vs_rule.csv`, `aq3_errors_by_slice.csv`, `aq4_contact_yield.csv`, `aq4_list_summary.csv`, `aq4_reach.csv`, `aq4_fairness_descriptive.csv`, `aq3_summary.md`, `aq4_summary.md`. Every table has a column `scores` naming its basis. In total 50 result files, none with a student identifier.

### A2. New files

| File | What it does |
| :---- | :---- |
| `src/analysis/aq34_common.py` | Shared definitions: loaders with a year filter pushed to the reader and asserted, fixed tie-breaker, list size k = 3 or 5 × ⌈n/20⌉, rule-ranked list, list metrics, the five candidate configurations (B3, M1–M4) with their preprocessing and grids, calibration, result folders |
| `src/analysis/aq3_develop.py` | Step 19: development on the 9 runs of 2013 only (leave-one-run-out, nested tuning on log loss, choice rule of Appendix III), out-of-fold scores of the 2013 runs, final models at days 13 and 27, freeze record with the SHA-256 of every model |
| `src/analysis/aq3_test.py` | Step 20: refuses to run without the freeze; scores the 13 runs of 2014 once; gate S1 (bootstrap 2,000, exact sign-flip), context comparisons, sensitivity views, calibration bins, timing of listed non-completers |
| `src/analysis/aq4_lists.py` | Step 21: the reason shown beside each name, the coefficients of the chosen model, rule FR1 (bootstrap 5,000, Holm) |
| `src/analysis/aq34_scopes.py` | Steps 22–24: the AQ3/AQ4 views of one scope (`--scope 2013 | 2014 | all`), like `aq_analysis.py --scope` for AQ1/AQ2 |
| `src/analysis/aq34_compare.py` | Step 25: 2013 development estimates against the 2014 test |
| `src/analysis/aq34_checks.py` | Step 26: populations, freeze before scores, second count of the listed non-completers, agreement with the Milestone 4 draft package, no student identifier in the 42 AQ3/AQ4 CSV files; writes `data/metadata/aq34_checks.csv` |
| `data/metadata/aq34_reference_m4.csv` | Reference values from the Milestone 4 draft package used by step 26 |
| `results/checksums_aq34.csv` | Reference SHA-256 of the 50 AQ3/AQ4 result files, for step 27 |
| `data/metadata/rebuild_check_results_aq34.csv` | Output of step 27 |
| `logs/19_aq3_develop.log` … `logs/27_check_results_aq34.log` | Logs of the new steps, same format as steps 00–18 |

### A3. Edited files

| File | Change | Effect on existing steps |
| :---- | :---- | :---- |
| `run_all.sh` | Header comment extended; nine steps appended after step 18: `19_aq3_develop`, `20_aq3_test`, `21_aq4_lists`, `22_aq34_2013`, `23_aq34_2014`, `24_aq34_all_runs`, `25_aq34_compare`, `26_aq34_checks` (check), `27_check_results_aq34` (check) | Steps 00–18 unchanged, same names and order |
| `requirements.txt` | Added, pinned: `scikit-learn==1.9.1`, `joblib==1.6.0`, `threadpoolctl==3.8.0` | Existing pins unchanged |
| `src/checks/check_rebuild.py` | New mode `results_aq34` (patterns `aq3_*` and `aq4_*` in the four folders; reference `results/checksums_aq34.csv`). The pattern of mode `results` (step 18) for `compare/` narrowed from `compare/aq*.csv` to `compare/aq1_*.csv` and `compare/aq2_*.csv`, so that the new AQ3/AQ4 files are not counted as files without a reference | Step 18 selects exactly the same 63 files as before (checked: identical sets) |
| `README.md` | Intro (AQ3 Answered, AQ4 Partial); run time; structure tree (new scripts, `data/interim/aq3/`, AQ3/AQ4 files in the four folders); steps table rows 19–27; reproducibility (seed, steps 26–27, development estimates); dependencies; documentation map; C01–C18 | – |
| `results/README.md` | Title and intro; new section "AQ3 and AQ4" (plan items, populations, year split, the four scopes, output map, methods, deviations, items not computed); the row "Any AQ3 or AQ4 result" of "Items not computed" replaced; two bullets in "Results in brief" | – |
| `data/metadata/change_log.md` | New entry C18 (tuning criterion: log loss); title and intro C01–C18 and C15–C18 | – |
| `docs/traceability_matrix.md` | Intro paragraph; Table 1 AQ3 row (Answered) and a new AQ4 row (Partial; the table had no AQ4 row); reading paragraph; Table 2 statuses; Table 3 compact rows; evidence table rows pointing to `2013/aq3_dev_choice.csv`, `2014/aq3_s1_gate.csv`, `2014/aq3_discrimination_calibration.csv`, `2014/aq3_pooled.csv`, `2014/aq4_fairness_confirmatory.csv` | – |
| `docs/ai_decision_log.md` | New row "M5: AQ3 and AQ4 analysis code" (final decision "proposed for our decision"); one closing sentence | – |

### A4. Runs and checks

| Run or check | Result |
| :---- | :---- |
| Steps 19–27 only (a copy of `run_all.sh` with steps 00–18 left out, same logging) | Every step ok, every check passed: 9 of 9 AQ3/AQ4 checks; 50 of 50 AQ3/AQ4 result files byte-identical to `results/checksums_aq34.csv` on a second run |
| 2014 tables against `reports/experiment/results/` | 13 tables, every numeric cell equal within 5 × 10⁻⁷ (the package rounds to 6 decimals) |
| Khanh's checks run as scripts (steps 11 and 17, no log written) | 0 failures; their scope-purity loops now also cover the AQ3/AQ4 files of `2013/` and `2014/` (110 and 88 checks instead of 96 and 53). His logs keep his own run |
| Clean-copy test (package copied without data, logs or interim files; new download; `bash run_all.sh`), before the four-folder layout | Exit 0, every step and check passed. Run outside the package, so Khanh's `logs/clean_copy_test.md` and logs stay unchanged |
| Logs 00–18 and Khanh's metadata files | Not rerun after the first two full runs of the day; they are left exactly as in commit `4b83229` (Khanh's original run times are in `23bf7b6`) |

## Part B – report (`report/`, English and Vietnamese)

Rule followed: Appendix X of the report itself says that when the prototype runs, "the project record changes in four places only: the results part and its appendix, the verdict of the comparison with Level 1, the Change Log only if a choice changes, and the AI Decision Log". Those four places were updated. Besides them, only sentences that would otherwise be false ("not run", "Deferred", "expected outputs") were corrected, each in its AQ3/AQ4 clause only. The design sections (Sections 8 and 9, Appendices VIII–X) stay as frozen; they describe the plan, in the proposal tense. No AQ1 or AQ2 sentence, number or table row was changed: Sections 11.2 and 11.3 and Appendices XII and XIII are untouched, and in Appendix XIV the AQ1/AQ2 rows and the D2 row are byte-identical.

### B1. English sections

| File | Change |
| :---- | :---- |
| `10-00-experimental-status.md` | Rewritten: Level 2 run for AQ3/AQ4 (tools, development on 2013, freeze, single test on 2014, C18), model choice, new Table 10.1 (lists of 5 per 20: model, rule, background-only, random), gate S1 met, calibration S3 and the main error, the verdict against Level 1, the agreement with the Milestone 4 draft, the note that the 2014 runs had been described for AQ1/AQ2 before the test |
| `11-04-aq3-aq4-expected.md` | Heading "Expected Outputs" → "Early Warning and Ranked Lists"; text rewritten with the AQ3 and AQ4 results (file name kept, so the build order and the Vietnamese sync stay unchanged) |
| `16-14-aq3-aq4-answers.md` | Title, opening, AQ3 and AQ4 subsections rewritten with the results; Table A.37 becomes "AQ3 and AQ4 results against the criteria fixed in Milestone 4" (same number, new columns); AQ3/AQ4 rows of Tables A.38 and A.39; AQ3/AQ4 parts of the D1 and D3 rows of Table A.40 and of the paragraphs after it |
| `11-00-findings-overview.md` | One clause: AQ3 and AQ4 answered by the single test (Section 10) |
| `11-01-traceability-matrix.md` | Intro sentence; Table 11.2 AQ3 row (Answered) and AQ4 row (Partial) |
| `11-05-decision-support.md` | Table 11.3 header "Main finding or expected output" → "Main finding"; AQ3 and AQ4 rows; the D1 sentence (the model ranks the list, the rule is the fallback) |
| `12-00-limitations.md` | "Three situations" → two ("not yet tested" no longer applies); the row "AQ3 and AQ4 results – Not yet tested" replaced by two rows (calibration by run and the active non-completers; 2014 described before the test, C15, C18) |
| `12-01-future-work.md` | First sentence: the remaining OULAD step is a later review point (the prototype and the AQ4 audit are done) |
| `14-00-conclusion.md` | AQ3/AQ4 sentence with the result; "that a model ranks students better than the rule" removed from what cannot be concluded and replaced by "that a model's risk is a reliable probability for each run"; "The next step is the single AQ3 test …" → "The next step is a recount …" |
| `00-1-abstract.md` | AQ3/AQ4 clause; one result sentence; last clause. Length 285 words by `wc` (Khanh's version 267); the AQ1/AQ2 sentences are unchanged |
| `00-0-title-page.md` | Milestone 4 status "Level 2 specified, not run" → "Level 2 run for AQ3 and AQ4"; Change Log "C01–C17" → "C01–C18" |
| `00-3-glossary.md`, `03-02-aq-revision-log.md` | "C01–C17" → "C01–C18" |
| `01-02-scope-objective.md`, `03-01-aq-quality-check.md`, `08-00-modeling-strategy.md`, `13-00-genai-reflection.md`, `16-00-appendices.md` | One AQ3/AQ4 clause each ("not run" / "designs" / "expected outputs" → the run) |
| `03-00-analytical-questions.md`, `05-01-requirement-data-fit.md` | Status column: AQ3 Deferred → Answered, AQ4 Deferred → Partial |
| `16-03-aq-quality-revision.md` | AQ3/AQ4 status sentences; "Answerable" row cells of AQ3/AQ4; final-status row; one sentence on Ready vs Partial; Table A.8 title C01–C18 and new row C18 (same text as `package/data/metadata/change_log.md`) |
| `16-11-reading-traceability.md` | AQ3/AQ4 rows of the reading table, of Table A.27 and of the status table; one sentence |
| `16-15-limitations-future.md` | Opening and model-limits paragraph (two situations; calibration by run; active non-completers; C15 and C18); Table A.41: two "Not yet tested" rows replaced by three rows; Table A.42 steps 1 and 2 (done) replaced by "Later review point" and "Model check on the university's records", so steps 3–5 keep their numbers; the paragraph after it |
| `16-16-ai-decision-log.md` | New row "M5: AQ3 and AQ4 analysis code" in Table A.43 (decision "proposed for our decision"); one sentence on human ownership |

Checks on the English: `make precheck TASK=milestone-5`: format, structure, abbreviations, citations, names and research trail pass; style passed after three "the team's" were changed to "our".

### B2. Further English fixes found while translating

The translators checked each English change against its context and found stale or unclear sentences, all corrected in the English first:

| File | Change |
| :---- | :---- |
| `03-00-analytical-questions.md` | Table 3.1, AQ3 quality-check cell: "Answerable by design, not yet run" → "Answered by a single test on 2014" |
| `16-03-aq-quality-revision.md` | Intro "C01–C17" → "C01–C18"; Change Log paragraph "C15 to C17" → "C15 to C18"; "Three entries recorded in the final integration" → "Four entries…", with a sentence on C18 |
| `03-02-aq-revision-log.md` | "added three entries … (C17)" → "added four entries … (C17), and the AQ3 penalty is tuned by log loss (C18)" |
| `10-00-experimental-status.md` | C18 sentence now states that the choice was made after the tuning results of both measures were known; "lists within 4 students" → "counts of listed non-completers differing by at most 4" |
| `11-04-aq3-aq4-expected.md` | The 59.7% against 50.6% comparison now names the rule's own picks |
| `16-14-aq3-aq4-answers.md` | "listed the same students within 4 places" → "counts of listed non-completers differ by at most 4"; Table A.40 D1 hypothesis: "students flagged by the rule" → "the students on the list" |
| `16-11-reading-traceability.md` | "AQ3 carries no performance figure until the single test … has been run" → the figures come only from the single test, never from the development folds |
| `16-15-limitations-future.md` | Paragraph before Table A.42: two kinds of limit instead of three; the remaining OULAD step is a later review point |
| `16-16-ai-decision-log.md` | Row "M4 / M5": "keeps the frozen Level 1 design … unchanged" + "and runs it once as the Level 2 prototype". The row "M5: integration design" (AQ3 and AQ4 Deferred at that time) is kept as history |

### B3. Vietnamese twins

All 24 twins whose English changed were updated, following the build-report procedure (`languages/vi/guide.md`, lessons, the task glossary, `check_parity.py` to 0 errors, `translation_status.py --mark`), and only in the passages whose English changed; every other Vietnamese sentence, and the AQ1/AQ2 rows and the D2 row of Appendix XIV, are unchanged. Terms with no glossary row yet, used consistently: "log loss" (kept in English), "fallback" → "phương án thay thế", tutor group → "nhóm hướng dẫn", "tutors see ranks" → "cán bộ", "Scope" (limit kind) → "Phạm vi". Khanh may want to add these to the topic glossary.

### B4. Build

`make all TASK=milestone-5`: 21 of 21 steps pass (format, structure, style, abbreviations, citations, names, research trail, translation 0 stale, parity 0 errors with 1 warning that predates this change, figures, Word build EN and VI, postcheck of both `.docx`); build-report self-tests 162/162 and research-report 64/64.

Side effects of `make all` that were undone: it also rebuilds the four slide decks in `build/` (Khanh's presentation work), so `N04_Milestone5_Slides-30_EN.pptx`, `-30_VI.pptx`, `-Full_EN.pptx` and `-Split_EN.pptx` were restored to commit `23bf7b6`; and its self-tests created an untracked `build/.cache/` folder at the repository root, which was removed. Changed build files: `build/N04_Milestone5_EN.docx` and `build/N04_Milestone5_VI.docx` only.

Page budget (`make pages TASK=milestone-5`), main text of the English report: 19.4 pages optimistic, 27.0 pessimistic; Section 10 is 1.35 pages (the brief allows 0–4 for it). The pessimistic figure is above the brief's 15–25 pages, a decision for the team (shortening other sections was outside this change).

## Not changed

- AQ1 and AQ2: no number, sentence, table row, result file, script or log of theirs (Sections 11.2, 11.3; Appendices XII, XIII; `package/results/2013`, `2014`, `all_runs`, `compare`; package steps 00–18 and their logs).
- The design sections (Sections 8 and 9; Appendices VIII–X) and the presentation folder and slide decks.
- `package/logs/clean_copy_test.md` (the new clean-copy test is recorded here instead).
