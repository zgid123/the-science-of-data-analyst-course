# Vietnamese fidelity review after rewrite 2 – Milestone 4, 2026-11-08

Stage 5 of build-report reference.md section 4.3: the fixes of `rewrite-2-2026-11-08.md` read again by a reviewer who did not write them. Scope: every unit (paragraph or table row) that `rewrite-2-2026-11-08-scripts/twins.diff` changed, 103 units in 27 twins, compared sentence by sentence with the current English file for meaning, numbers, conditions, hedges, attributions, citations, cross-references and native Vietnamese (review.md section 3, glossary forms). The English files changed after the rewrite (01-01, 10-01, 10-04, 10-06) were checked against their twins in full with `numcheck.py`, then the changed cells by reading.

Method (scripts in `fidelity-2-2026-11-08-scripts/`): `pairs.py` prints each changed Vietnamese unit beside its current English unit; `wdiff.py` shows word by word what the rewrite changed inside each unit, so new content is told apart from content that was already there; `numcheck.py` compares the numbers, citations and identifiers of every unit of the four files whose English changed; `fix.py` applies the corrections (each before-string must occur exactly once or nothing is written). The twins were copied to the session scratchpad before editing (`m4-fidelity2/before/`). Numbers and dates in additions were checked against `code/design_facts.py`, `results/design_facts.json`, the Milestone 3 model-ready matrix and the research trail. Paths are relative to `reports/milestone-4/report/`.

## Result

| Item | Count |
| :---- | :---- |
| Twins in scope / changed units read | 27 / 103 |
| Defects found and fixed | 10 (11 edits in 7 twins) |
| Additions beyond the English: kept, English wording proposed (a) | 45 (table below) |
| Additions beyond the English: removed from the twin (b) | 1 |
| English changes since the rewrite, twin checked | 4 (01-01 fixed; 10-01 and 10-04 already matched; 10-06 fixed) |

## Findings

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 01-01 | 7 | 3.6 identifiers; English sync | điều chỉnh cách đo của hai câu hỏi AQ3 và AQ4, qua hai định nghĩa trình bày ở cuối mục này | xác định lại cách đo của hai câu hỏi, AQ3 (C10) và AQ4 (C13), như trình bày dưới đây (English: "restate how two questions are measured, AQ3 (C10) and AQ4 (C13), as described below") |
| 2 | 03-03 | 7 | 3.6 meaning complete (addition inaccurate) | Module và tháng bắt đầu là biến phân loại, nên mỗi biến đi vào mô hình dưới dạng nhiều số hạng (biến giả) | … là biến phân loại nên được đưa vào mô hình dưới dạng biến giả, mỗi mức (trừ một mức tham chiếu) là một số hạng. Start month has two levels (B, J) and gives one term; module has 6 training levels and gives 5; 17 + 5 + 1 = 23 (`design_facts.py` `n_params`; `model_ready_d27` columns) |
| 3 | 04-01 | 14 | 3.6 meaning (ambiguous) | các lượt đăng ký học đã bỏ lỡ bài được chấm điểm đầu tiên | các lượt đăng ký học đã lần đầu bỏ lỡ một bài được chấm điểm ("đầu tiên" read as the first task of the run, not the first miss) |
| 4 | 04-01 | 46 | 3.3 English term | Kiểm định khẳng định (confirmatory test) | Kiểm định khẳng định (confirmatory check), the English word of the card and of the glossary row |
| 5 | 04-02 | 16 | 3.3 glossary form | trên cùng mẫu lặp đó | trên cùng mẫu lấy lại đó (glossary "paired two-level bootstrap": "cùng một mẫu lấy lại") |
| 6 | 04-02 | 18 | 3.6 meaning (addition too broad) | nguy cơ chung, tức tỷ lệ không hoàn thành tính trên toàn bộ dữ liệu | … tính trên toàn bộ dữ liệu phát triển (Riley criterion iii uses the development prevalence, `design_facts.py` `riley(p, prev)` with the 2013 rate) |
| 7 | 04-03 | 9 | 3.3 one term per concept | lợi ích ròng chỉ là thông tin bối cảnh | lợi ích ròng chỉ dùng để tham khảo (the same "context only" as the AQ3 card in 04-01) |
| 8 | 06-00 | 3 | 3.5 no empty words (gloss repeated the role name) | AI phản biện lựa chọn mô hình (model-selection critic), tức một AI đóng vai người phản biện, dùng để chất vấn …; AI rà soát thiết kế đánh giá (evaluation reviewer), tức một AI đóng vai người rà soát, dùng để phản biện … | … (model-selection critic), là vai trò trong đó AI chất vấn …; … (evaluation reviewer), là vai trò trong đó AI phản biện … (two edits; the role is stated without adding content) |
| 9 | 06-00 | 19 | 3.6 meaning (addition, type b) | lấy từ 6 module của các kỳ mở huấn luyện, để không dùng đến dữ liệu của tập kiểm thử; | lấy từ 6 module của các kỳ mở huấn luyện; (the reason is not the English's: the critique was that the 2013 runs hold 6 modules, not 7, Table A.11 row 1) |
| 10 | 10-06 | 33 | 3.6 English sync | trên một kỳ mở diễn ra sau | trên một kỳ mở diễn ra sau các kỳ mở năm 2014 của tập kiểm thử (English row 6: "on a run after the 2014 test runs") |

Checked and correct, no edit: 01-01 (C13 definitions), 10-01 (after Table A.2: "Khi so với mô hình chính, …" matches "Compared with the primary model, …"), 10-04 (Table A.7 header matches "Fewest enrolments of the group in one test run"; values female 66 and male 139 at day 27 are `test_rows_min_per_run` in `results/design_facts.json`), 10-05 R4 ("a run after the 2014 test runs"), and proxy as "biến đại diện (proxy)" / "kiểm tra biến đại diện (proxy check)" in every twin (no "biến thay thế" or "chỉ số đại diện" left).

Structure note for the lead: 03-03 has 7 paragraphs against 4 in the English (the "Primary approach" paragraph is split into four in the twin; rewrite 2 added one split, the extended set). The parity check does not count paragraphs and passes; the order of content matches the English.

## Additions beyond the English

Type (b), removed from the twin: 06-00 line 19, "để không dùng đến dữ liệu của tập kiểm thử" (finding 9).

Type (a), kept: each is a brief definition or a restatement of what the report says elsewhere, checked against the report and, where numbers or dates are involved, the code. The lead adds the English wording below so both files carry the same content.

## English additions proposed

| File | English sentence or cell to change | Exact new English | Source in the report or code |
| :---- | :---- | :---- | :---- |
| 00-2 | Calibration slope: "The coefficient of the score's log-odds in a logistic recalibration; 1 when …" | The coefficient of the score's log-odds in a logistic recalibration, a logistic regression of the outcome on that log-odds; 1 when risks are neither too extreme nor too flat (Section 4.3) | 10-02 Table A.4; 04-03 |
| 00-2 | Calibration-in-the-large: "… with the score's log-odds as offset; 0 when …" | The intercept of a logistic model of the outcome with the score's log-odds as offset (a term whose coefficient is fixed at 1); 0 when the average predicted risk is right (Section 4.3) | 10-02 Table A.4; definition of an offset |
| 00-2 | Labels-available variant: "… trained only on the 2013 February runs (Section 4.2)" | A sensitivity analysis that scores the 2014 February runs with a model trained only on the 2013 February runs, the runs whose outcomes are known at that time (Section 4.2) | 04-02 "the only runs whose outcomes a university would hold at that time" |
| 01-01 | "they replace comparisons by delivery mode and year of study" | they replace comparisons by delivery mode (online or blended) and year of study | Milestones 1–2 delivery modes; glossary "delivery mode" |
| 01-01 | "and by its gain over the run's base rate, the share of students who do not complete, because a random list already reaches that rate (C13)" | and by its gain over the run's base rate (lift), the share of non-completers on the list against the share of students who do not complete in the whole run, because a random list already reaches that rate (C13) | 10-02 Table A.4 (lift = precision / b); 00-2 Lift |
| 01-02 | "and two feature views, one for each cut-off" | and two feature views, the tables of predictors a model reads, one for each cut-off | 08-00; 10-07 Table A.12 |
| 01-02 | "A feature view keeps only the enrolments still registered at its cut-off" | A feature view keeps only the enrolments still registered at its cut-off, that is, not withdrawn by that day | glossary "registered at day d"; 01-02 KPI definition |
| 02-02 | "A discrete-time survival model would add when a student leaves [8]" | A discrete-time survival model, a form of survival analysis, would add when a student leaves [8] | same paragraph ("survival stays an extension") |
| 03-01 | Table 3.1, AQ1 baseline: "Pooled rate; second denominator" | Pooled rate; rate over all enrolments, not only those registered at day 14 (second denominator) | 03-02 (32,593 instead of 28,061) |
| 03-01 | Table 3.1, AQ2 rationale: "All runs of the modules observed; effect sizes within module; no causal claim" | All runs of the modules observed, not sampled, so fixed effects suit; effect sizes within module; no causal claim | 03-02 "since every run is observed rather than sampled" |
| 03-01 | Table 3.1, AQ3 rationale: "ample events per parameter" | ample events per parameter, each parameter backed by many non-completers | 03-03 (about 230 non-completers per parameter) |
| 03-02 | "it is deterministic and is checked with robust standard errors and sensitivity runs" | it is deterministic, a rerun always gives the same result, and is checked with robust standard errors and sensitivity runs | definition of deterministic |
| 03-03 | "module and start month enter as several terms each, so the model has 23 parameters in all" | module and start month are categorical and enter as dummy terms, one per level except a reference level, so the model has 23 parameters in all | `code/design_facts.py` `n_params` (one-hot minus one reference level); `model_ready_d27`: 6 module and 2 start-month levels; `results/design_facts.json` `params_primary` = 23 |
| 03-03 | "about 230 per parameter" | about 230 events (non-completers) per parameter | glossary "events per parameter"; 5,245 / 23 ≈ 228 |
| 04-01 | AQ4 card, primary metric: "computed per run with the run's own list and pooled over runs (day 27, k = 5 per 20)" | computed per run with the run's own list and pooled over runs as the non-completers listed in all runs divided by the most the lists could hold, each list holding at most k non-completers, or all of the run's if fewer (day 27, k = 5 per 20) | 10-02 Table A.4, "Pooled normalised recall: Σ\|L ∩ Y\| / Σ min(k, \|Y\|)" |
| 04-01 | AQ4 card, fairness: "Confirmatory check of recall at capacity by group and descriptive checks (Section 4.4)" | Confirmatory check, a formal test on groups fixed in advance, of recall at capacity by group, and descriptive checks (Section 4.4) | 04-04 (three groups fixed from enrolment counts before any test outcome) |
| 04-02 | "The 1,586 test enrolments at day 27 of students already seen in 2013 stay in the test" | The 1,586 test enrolments at day 27 of students already seen in 2013, the development data, stay in the test | 01-02 (2013 runs for development) |
| 04-02 | "and the 2013 J runs last 261–268 days, so their outcomes are not yet known when the 2014 B runs reach their cut-offs;" | and the 2013 J runs start in October 2013 and last 261–268 days, ending around mid-2014, whereas the 2014 B runs start in February 2014 and reach their cut-offs a few weeks later, when the 2013 J outcomes are not yet known; | same sentence (B = February, J = October [2]); `results/design_facts.json` `run_length_days` 2013J = 261–268; cut-offs at days 13 and 27 (01-02) |
| 04-02 | "and the overall risk estimated within 0.05" | and the overall risk, the non-completion rate of the development data, estimated within 0.05 | `code/design_facts.py` `riley()` criterion (iii) on the 2013 prevalence |
| 04-03 | "the calibration-in-the-large, the intercept of a recalibration model with the slope fixed," | the calibration-in-the-large, the intercept of a recalibration model, a logistic regression of the outcome on the score's log-odds, with the slope fixed at 1, | 10-02 Table A.4 (log-odds as offset) |
| 04-04 | "conflict except in degenerate cases [37]" | conflict except in degenerate cases, perfect prediction or equal base rates across groups [37] | research claim C5-012 (Kleinberg et al. [37]: "except in special cases of perfect prediction and equal base rates") |
| 04-04 | "and the rest of the students are many times more numerous, so the gap of 10 points in rule FR1 is about two standard errors of the group's recall, the main source of uncertainty in the gap, and 400 enrolments at the lowest group rate of 28% give about 112 non-completers." | and the rest of the students are many times more numerous, so their recall has a much smaller standard error and the group's is the main source of uncertainty in the gap; the gap of 10 points in rule FR1 is therefore about two standard errors of the group's recall. In addition, 400 enrolments at the lowest group rate of 28% give about 112 non-completers (400 × 28%), above 100. | same paragraph; arithmetic |
| 04-04 | Table A.8 list: "the threshold-free gap," | the threshold-free gap in discrimination (ABROCA), | same paragraph (ABROCA defined); 10-04 Table A.8 |
| 05-00 | Table 5.1, high-stakes controls: "flags expire" | flags expire with the run | 05-02 "expires with the run" |
| 05-01 | "which the dated feature views ensure and the labels-available variant checks." | which the dated feature views ensure and the labels-available variant checks, since the outcomes of the October 2013 runs are not yet known when the February 2014 runs reach their cut-offs. | 04-02 |
| 05-01 | "Many different models fit about equally well [5], so no coefficient is read as a cause," | Many different models, with different coefficients, fit about equally well [5]; the chosen model's coefficients are one of many sets that fit the data, so no coefficient is read as a cause, | same sentence, its reasoning made explicit |
| 05-02 | "Risk and benefit can also diverge, as field experiments in customer retention showed [20]." | Risk and benefit can also diverge: the students at highest risk do not always benefit most, as field experiments in customer retention showed [20]. | 03-04 ("the customers at the highest predicted risk were not the best targets of an intervention [20]") |
| 05-02 | "a randomised pilot whose time zero is the cut-off at which students become eligible for the list [44]" | a randomised pilot whose time zero, the moment from which every student in the pilot is followed, is the cut-off at which students become eligible for the list [44] | definition of time zero (target trial [44]) |
| 06-00 | Table 6.1, literature row: "since non-completion is 44–46%" | since non-completion is 44–46%, so the classes are not imbalanced | 03-03 ("The two classes are close in size") |
| 10-01 | Table A.1, AQ2 fit to question, mixed-effects cell: "Same, with module effects drawn from a population of modules" | Same, with module effects drawn from a population of modules (random effects) | Table A.1, same column, Assumptions "Normal random effects" |
| 10-01 | Table A.1, AQ2 assumptions: "all runs of these modules observed, so fixed effects suit the design [12]" | all runs of these modules observed, not sampled, so fixed effects suit the design [12] | 03-02 |
| 10-01 | Table A.2, survival assumptions: "Non-informative censoring;" | Non-informative censoring (a student is censored when follow-up stops before withdrawal is observed, and the reason it stops is assumed unrelated to the risk of withdrawal); | definition of non-informative censoring |
| 10-01 | Table A.2, boosted trees complexity: "maintenance and entanglement risks [10]" | maintenance and entanglement risks, entanglement being the dependence of a system's parts on each other [10] | definition (Sculley et al. [10]) |
| 10-01 | after Table A.2: "the background-only model shows how much of the ranking comes from engagement" | the background-only model, which uses no activity, shows how much of the ranking comes from engagement | 03-03 ("but no activity") |
| 10-03 | Table A.5 step 2: "in outer and inner loops alike" | in outer loops (the cross-validation used to evaluate and choose the model) and inner loops (the cross-validation run inside each training fold to tune hyperparameters, step 3) alike | Table A.5 steps 3 and 4 |
| 10-03 | Table A.5 step 3: "tuned by an inner leave-one-run-out loop" | tuned by nested cross-validation, an inner leave-one-run-out loop run on the training runs of each fold | Table A.5 step 3 |
| 10-03 | after Table A.6: "and why per-module models remain unattractive, since shrinkage does not rescue small samples [17]" | and why per-module models remain unattractive, since each module's data are small and shrinkage does not rescue small samples [17] | 03-03 |
| 10-04 | Table A.8, threshold-free gap: "a reference from group labels shuffled within run [34]" | a reference from group labels shuffled within run, the ABROCA that chance alone can produce [34] | definition of a permutation reference |
| 10-05 | R16: "Conformity assessment before use [49]" | Conformity assessment, the procedure that assesses a high-risk AI system before it is put into use [49] | R16 row ("listed as high-risk in Vietnam [50]"); glossary "conformity assessment" |
| 10-06 | Table A.10 row 7: "non-informative censoring stated as an assumption" | non-informative censoring (follow-up stopping for reasons unrelated to the risk of withdrawal) stated as an assumption | as 10-01 |
| 10-06 | Table A.11 row 6: "Calibration-in-the-large with offset; pooled bounds;" | Calibration-in-the-large defined as the intercept with the score's log-odds as offset (coefficient fixed at 1); bounds on the estimates pooled over all runs; | 10-02 Table A.4; 04-01 S3 ("pooled point estimates") |
| 10-06 | Table A.11 row 7: "removal in all loops" | removal in all loops, outer and inner | 10-03 Table A.5 step 2 |
| 10-07 | Table A.12 AQ1 data: "enrolment, assessment_due;" | enrolment and assessed-task views (enrolment, assessment_due); | 08-00 ("the enrolment and task views") |
| 10-07 | Table A.12 AQ3 data: "features_d13, features_d27, model_ready;" | the two feature views (features_d13, features_d27) and the model-ready matrix (model_ready); | 08-00 |
| 10-07 | Table A.12 AQ4 data: "capacity_by_run" | list lengths by capacity for each run (capacity_by_run) | `capacity_by_run.parquet` columns `list_tutor_3`, `list_tutor_5` per run and cut-off (`code/design_facts.py`) |

When the lead adds a row's English, the twin needs no change except where the proposed English differs from the twin's wording; the Vietnamese already carries each addition. Rows 01-01 (delivery mode), 01-02, 03-01 (AQ1), 05-01 (leakage), 06-00 and 10-03 (after Table A.6) are additions that predate rewrite 2 and sit in units it changed.

## Check results

| Command | Result |
| :---- | :---- |
| `fix.py` | 11 edits applied to 7 twins, exit 0 |
| `check_parity.py --report reports/milestone-4/report --lang vi` | 0 errors, 24 warnings: 23 in the verbatim English prompts of 10-06 and 1 loanword on the English term of the terms page (00-2:37); the same 24 as after rewrite 2, none new |
| `check_parity.py … <9 English files>` | 0 errors, 23 warnings (the 10-06 prompts); a first run passed the twins instead of the sources and reported their twins missing, rerun |
| `check_abbreviations.py --report reports/milestone-4/report --lang vi` | 17 abbreviations, 0 violations |
| `numcheck.py 01-01 10-01 10-04 10-06` | units aligned (13, 42, 25, 37); differences only in trailing punctuation, B/J months written as "tháng 2", "tháng 10", glossary first-use glosses and "Ứng viên 1" |
| `translation_status.py --report reports/milestone-4/report --lang vi --mark` 01-01, 03-03, 04-01, 04-02, 04-03, 06-00, 10-06 (edited), 10-01, 10-04 (English changed, twin verified) | recorded 9 files |
| `translation_status.py --report reports/milestone-4/report --lang vi` | 34 sections, 0 need translation, 0 orphaned, exit 0 |

Console output with UTC timestamps, commands and exit codes: `fidelity-2-2026-11-08-scripts/checks.log`.

Per file: 27 twins reviewed; findings fixed in 01-01, 03-03, 04-01 (2), 04-02 (2), 04-03, 06-00 (3 edits), 10-06; no defect in the other 20; parity 0 errors for all.

## Still to run

- The lead adds the proposed English (or rejects a row, after which the twin's addition is removed).
- A third reader test on the rewritten passages has not been run.
