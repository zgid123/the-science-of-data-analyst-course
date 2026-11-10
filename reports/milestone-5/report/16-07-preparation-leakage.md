## Appendix VII – Preparation, Derived Variables and Leakage Controls

This appendix supports Section 7. It gives the Preparation Decision Matrix with the reason of each decision, the population rule, the pipeline steps, the derived variables with their formulas, the predictor sets and encoding, the leakage risks and controls, the before-and-after checks, the prepared views and the reproduction of the prepared dataset.

**Decisions before any change.** Before any record changed, every quality issue and preparation need received a decision with its rationale, its implementation and the validation check that would fail if the decision were not carried out. The Preparation Decision Matrix records these decisions; it covers the eight needs of the course template, from missing values to encoding and scaling, and four further needs of this project: the population of each table, activity after withdrawal, the sensitive attributes and the split into training and test runs. Table A.17 gives the matrix, with the checks V01 to V15 of the validation script named in words.

**Table A.17. Preparation Decision Matrix**

| Need | Decision | Reason | Validation check |
| :---- | :---- | :---- | :---- |
| Population (rule C09) | Keep all 32,593 enrolments in the enrolment view with flags for days 13, 14 and 27; feature views hold only the enrolments enrolled at their cut-off | The KPI counts students enrolled after the add-drop period; a list can only name students enrolled on the day it is drawn | Populations equal the profile (V01) |
| Missing values (DQ04, DQ11–DQ14) | Deprivation band "Missing" as its own category; registration and withdrawal days left empty with an indicator; TMA score left empty; planned weeks not used | Missingness is informative (deprivation band), small or in an unused field; imputing would invent values the data do not hold | Missing counts after equal those before (V02); filling only from training rows (V12) |
| Duplicates and keys (DQ01, DQ02) | Keep every click row; sum clicks by enrolment and day, and by week, before any join; de-duplicated twin of each click feature | The cause of exact duplicates cannot be decided; a row is a logging record, not one student-day | Keys unique in every view (V03); click totals reconcile (V04) |
| Invalid category or type (DQ07, DQ12) | Band label corrected; ordered categories for bands; banked results separated and never timed | Labels must sort and match; day −1 is a placeholder for a carried-over result | Every category in its expected set (V05); no banked row in lateness or missed counts (V06) |
| Outliers (DQ10, DQ16) | Keep every value | Heavy users, students on many modules and very late submissions are real; capping would change real totals | Ranges after equal those before (V07) |
| Activity after withdrawal (DQ03) | Truncate engagement measures at the unregistration day | Activity after leaving is not engagement while enrolled and would blur AQ1 and AQ2 | No click or submission counted after the unregistration day (V08) |
| Table integration (DQ02, DQ17) | Left joins from the enrolment table after summing each table to the target grain; zero counts for no activity | Inner joins would drop 3,365 enrolments; a direct join of submissions and clicks would return 89,347,197 rows | Rows equal the left table after every join (V09); enrolments without activity kept with zero (V10) |
| Derived features (DQ08, DQ09, DQ18) | Task counts over TMA and CMA only, unweighted; lateness from due and submission days; CMA marks known by the cut-off; early-sign rule C10; activity relative to the run's median | No exam results in five modules; weights differ by module; TMA marks have no release day; the rule must fire in every run | Features recomputed from raw by separate code, with unit tests for every formula (V11) |
| Temporal aggregation | Weeks of seven days from day 0; cut-offs at day 13 and day 27; activity before day 0 as its own window | The prediction points are fixed by decision D1; activity before the start is known at the cut-off | Recount without the date filter differs only where later clicks exist (V13) |
| Encoding and scaling | Views keep original scales and labels; transforms learned from training rows only | A test run must never inform a parameter | Parameters unchanged when test rows are altered (V12) |
| Sensitive attributes | Gender, age band, disability, deprivation band and region kept in every view as audit columns, outside every predictor set | The fairness audit needs them; their use as predictors is a policy choice | Every column has a role; no audit column among the predictors (V14) |
| Split | Training on the 2013 runs, test on the 2014 runs; flags for paired runs and for test students seen in 2013 | The claim is prediction for a later run | No run in both partitions; flags recomputed (V15) |

**Three governing decisions.** Three decisions shape the prepared data most. Nothing that was recorded is deleted or imputed in the prepared views, so every count can be traced back to the raw files, and only model fitting fills or scales values. Every feature is built only from events dated on or before its cut-off, so no information from after the moment of prediction reaches a model. And every parameter learned from the data, such as a median or a scale, comes from the training runs alone, so the test runs remain an independent check.

**Population rule.** The population rule (C09) counts an enrolment as enrolled on a given day when the student registered by that day, or the registration day is unknown, and had not unregistered by it. The rule removes the 58 late registrants from the day-14 population and leaves 28,061 enrolments in the KPI population over the 22 runs; the same rule gives 28,069 enrolments at day 13 and 27,535 at day 27. Applied to the 9 runs of 2013, it gives the 12,076 enrolments of the AQ1 primary denominator and the 11,811 enrolments of the AQ2 population (Table 6.1).

**Missing values and outliers.** Missing values stay missing in the views: the deprivation band keeps "Missing" as a category, the registration and withdrawal days carry indicators, and median filling of the registration lead happens only inside model fitting, with the median taken from training rows. Outliers stay as recorded, including the 6,977-click record, the 655-credit study load and submissions up to day 608, and counts are log-transformed only where a model is sensitive to scale.

**Integration and steps.** Integration starts from the enrolment table, which holds one row for each of the 32,593 enrolments, and adds every other table through left joins after summing it to the enrolment, so that no enrolment is lost and no row is multiplied; all 25 joins kept their input rows. The preparation runs in ten scripted steps with no manual step. They check the raw tables against their checksums, select the populations, correct 3,516 deprivation band labels written in a second form, sum the 10,655,280 click rows into 1,808,119 enrolment-day records, flag the uncertain records, leave out the 98,745 clicks after withdrawal, integrate 286,898 enrolment-task rows, build the features at both cut-offs and write the prepared views with their documentation. Section 7.1 describes the variables these steps derive.

**Timing rule.** Every feature uses only records dated on or before its cut-off c, which is day 13 or day 27. A legitimate model may build only on information that existed before its target was known, so activity after the cut-off, the withdrawal day and the final result never enter a feature. Activity before day 0 is kept as its own window, because it is known before teaching starts. Features that need a mark use only CMA marks for submissions made at least seven days before the cut-off, since a CMA score is expected within seven days, while a TMA mark has no release day in the data and is therefore never used as a feature.

**Derived variables.** Table A.18 defines the main derived variables with their formula and timing rule; c stands for the cut-off day. The names are those of the data dictionary that travels with the Final Project Package.

**Table A.18. Main derived variables**

| Variable | Formula | Timing rule | Used by |
| :---- | :---- | :---- | :---- |
| non_completion (target) | Final result is Fail or Withdrawn | Observed at the run end; never a feature | AQ1–AQ4 |
| enrolled_d13, enrolled_d14, enrolled_d27 | Registered by day d, or registration day unknown, and not unregistered by day d | Day d (rule C09) | Populations |
| clicks_pre | Clicks before day 0 | Before the start | AQ2 sign, AQ3 |
| clicks_0c, active_days_0c | Clicks, and days with at least one click, from day 0 to c | Days 0 to c | AQ3 |
| activity_ratio_run | (clicks_0c + 1) ÷ (median clicks_0c of the run's enrolled students + 1) | Same run, days 0 to c; no outcome used | AQ2 sign, AQ3 |
| inactive_last7 | No click on days c − 6 to c | Seven days ending at c | AQ2 sign, rule |
| tasks_missed_c | TMA or CMA due by c, due on or after the registration day, not submitted by c | Submissions up to c; banked results excluded | AQ2 sign, rule, AQ3 |
| tma_late_c, cma_late_c | Tasks due by c submitted after the due day but by c, by type | Submissions up to c | AQ2 sign, rule, AQ3 |
| cma_score_mean_c | Mean score of CMAs submitted by c − 7 | Marks known by c | Prepared, not used |
| early_sign_rule | A task missed, or a TMA late, or inactive in the last seven days | At c (rule C10) | AQ3 and AQ4 baseline; secondary KPI 1 |
| early_sign_rule_cma | The rule, or a CMA late | At c | Sensitivity variant |
| first_missed_week | Week of the earliest TMA or CMA not submitted that fell due while the student was enrolled | Whole run | AQ1 only |

A task counts as missed only if it fell due on or after the student's registration day, so a late registrant is not charged with tasks set before joining. The activity ratio compares a student with the median of the same run up to the same day and uses no outcome, so it is a cohort statistic that is still known at the cut-off. The early-sign rule (C10) flags an enrolment with a task due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off; it is the one early-sign rule of the project, on OULAD and in the pilot (Change Log C17, Section 3.2).

**Predictor sets.** The feature views hold 20 primary and 10 extended predictors plus the weekly click counts; every other column is an identifier, the target, a flag for evaluation, the rule or an audit attribute. The primary set covers module, start month, highest education, previous attempts, credits studied, registration lead, banked results, the click, activity and task measures and the mean CMA mark. Of these 20, the mean CMA mark is prepared but set aside, because marks known by the cut-off exist for only 1.4% of training rows at day 13 and 5.2% at day 27, below the 10% coverage required for a predictor. The final primary set therefore holds 19 usable predictors, which become 23 parameters once module and start month are coded (Section 8.1). Raw clicks are the declared primary measure, and the de-duplicated twin is a sensitivity variant that may be chosen only on the 2013 folds, before any 2014 evaluation; the duplicate share differs between the years, 6.82% of rows in 2013 against 7.87% in 2014, which makes this rule necessary. Only the columns of the declared predictor list may enter a model: identifier, split, evaluation, target, rule and audit columns never do.

**Encoding.** The prepared views keep original scales and labels, so the views show recorded values only. Milestone 3 also wrote model-ready matrices for linear models, with ordinal codes and a missing indicator for ordered categories, one-hot levels for nominal ones, and counts transformed by the logarithm of one plus the count, median-filled and standardised, all learned from the 2013 training rows. The final modeling protocol applies the same rule more strictly: every transform that learns a parameter is refitted inside each development fold and once on all 2013 runs before the test, and module terms are deviation-coded so that a module unseen in training receives the average effect (Section 9.1). The model-ready matrices therefore remain the reference encoding and the evidence that no test row informs a parameter, while models read the feature views and fit their own transforms. Tree models read the predictors untransformed. The AQ2 analysis reads the day-27 feature view of 2013 directly (Section 8.1).

**Leakage controls.** Leakage is the use of information about the target that would not be available at the moment of prediction, and it makes a model look better in evaluation than it can be in use. Table A.19 matches each form of leakage named for education data to its case in OULAD and to the control applied.

**Table A.19. Leakage risks and controls**

| Form | Case in OULAD | Control | Check |
| :---- | :---- | :---- | :---- |
| Target leakage | Final result, withdrawal day, activity or submissions after the cut-off, TMA marks, whole-run measures | Features built only from events dated up to the cut-off; CMA marks only, seven days after submission; target and whole-run measures outside the predictor lists | Features recomputed by separate code (V11); recount without the date filter (V13); column roles (V14) |
| Train–test contamination | Medians, scales and category levels computed on all runs | Learned from the 2013 runs only; refitted inside each fold | Parameters unchanged when test rows are altered (V12) |
| Student leakage | 1,962 enrolments in the 2014 runs belong to students who also enrolled in 2013, 1,586 of them registered at day 27 | Kept in the main test and flagged for a strict check; tuning folds keep each student on one side | Flags recomputed (V15) |
| Temporal leakage | A random split mixing the two years; tuning on 2014 | Training on the 9 runs of 2013, test on the 13 runs of 2014; tuning only inside 2013 | No run in both partitions (V15) |
| Augmentation leakage | None: no synthetic augmentation | – | – |
| Cohort statistic | The activity ratio uses the median of the same run | Only activity up to the cut-off of students enrolled at it; no outcome | Recount without the date filter (V13) |

The date-filter check (V13) is built so that it can fail: recounting the click features without any date filter changes them only for the enrolments that clicked after the cut-off, 26,755 at day 13 and 25,663 at day 27, which shows that the filter removes exactly the later clicks and nothing else.

**Split.** The data are split by year, following the Open University's practice of building at-risk models on previous runs of a module and applying them to the run in progress: the 9 runs of 2013 form the development data and the 13 runs of 2014 the test set. Of the 13 test runs, the 9 paired runs, BBB, DDD and FFF of February and AAA, BBB, DDD, EEE, FFF and GGG of October, test the claim directly, and the 4 unpaired runs, CCC of February and October, EEE of February and GGG of February, test transfer to a module or start month not seen in training and are reported apart (Change Log C16, Section 9.1). Tuning uses leave-one-run-out folds inside 2013, and students who also appear in the held-out run are removed from that fold's training data. The 2014 outcomes are not looked at while the data are prepared, nor in the AQ1 and AQ2 analyses (Change Log C14 and C15), and test results are to be reported also without the test enrolments that are Withdrawn without a withdrawal day, 89 at day 13 and 90 at day 27. Section 7.2 describes the prepared dataset these rules produce and how it is checked and rebuilt.

**Validation.** The validation script runs 22 checks under fifteen identifiers, V01 to V15, against the raw files and the profile of Section 6, and all 22 pass. Table A.20 gives the main before-and-after comparisons, each with the value in the raw data and in the prepared data.

**Table A.20. Before-and-after checks of the prepared data**

| Check | Before (raw) | After (prepared) | Result |
| :---- | :---- | :---- | :---- |
| Enrolments, students, outcome mix | 32,593 enrolments; 28,785 students; 12,361 Pass, 10,156 Withdrawn, 7,052 Fail, 3,024 Distinction | Identical; no row dropped | Pass |
| Populations (rule C09) | 32,593 enrolments | 28,061 at day 14; 28,069 at day 13; 27,535 at day 27, equal to the profile | Pass |
| Clicks | All click rows | 39,506,354 clicks kept plus 98,745 after withdrawal left out; the weekly view sums to the same total | Pass |
| De-duplicated clicks | – | 38,247,422, below the 39,506,354 kept clicks | Pass |
| Missing values | Deprivation band 1,111; registration day 45; TMA score 173 | Identical, not imputed | Pass |
| Joins | – | 25 joins, rows in equal rows out | Pass |
| Derived features | – | Six features recomputed from raw by separate code for all 55,604 feature rows: 0 differences | Pass |
| Leakage (date filter) | – | Recount without the filter differs only for the 26,755 (day 13) and 25,663 (day 27) enrolments that clicked after the cut-off | Pass |
| Repeat students | – | 1,962 enrolments of the 2014 runs (all enrolments, before any cut-off) of students seen in 2013, with 0 flag mismatches | Pass |

The comparisons show that preparation changed no outcome and no count except by a stated rule: clicks after withdrawal are left out by the truncation decision, and every other total is equal before and after.

**Documentation.** Every prepared column is documented in a data dictionary with its source field, transformation, type, role and sensitivity, and the lineage table gives one row for each of the 88 prepared variables. The dictionary is also a guard: validation fails if a column lacks an entry or if a predictor list holds an audit, target or descriptive column (V14), so the dictionary cannot drift from the data. Such documentation follows the practice that every dataset should come with a datasheet of its motivation and composition [9], and that reusable data carry a clear licence and detailed provenance [25].

**Version and views.** The prepared dataset is named OULAD-N04-prepared-1.0. Its version manifest records the SHA-256 checksum of every raw file, every script and every prepared file, the row counts, the code commit and the Python (3.12.7) and polars (2.1.0) versions. Table A.21 gives the prepared views, stored as Parquet files, with the unit of each and the questions that read it.

**Table A.21. Prepared views of OULAD-N04-prepared-1.0**

| View | Unit | Read by |
| :---- | :---- | :---- |
| enrolment | Enrolment, with outcome, population flags and audit attributes | AQ1; populations of every question |
| assessment_due | Enrolment and assessed task, with due day, submission and lateness | AQ1 first missed week |
| student_week | Enrolment and week, with clicks | Weekly activity series; source of the weekly click counts |
| features_d13, features_d27 | Enrolment registered at the cut-off, with predictors, rule, target and audit columns | AQ2 (day 27); AQ3 and AQ4 |
| capacity_by_run | Run and cut-off, with list lengths at 3 and 5 per 20 | AQ4 |
| model_ready_d13, model_ready_d27 | Reference encoding for linear models | Leakage evidence; not model input |

**Reproducibility.** The raw tables are read-only copies checked against their checksums at every run, so the raw data stay immutable. The Prepared Data Package rebuilds the prepared data from raw with an install of its listed requirements and one command that runs the preparation stages in order, logs the command, the time in UTC and the exit status of each stage, and stops at the first failure. When the raw files are absent, the first stage downloads the OULAD archive from its figshare record (DOI 10.6084/m9.figshare.5081998.v1) and checks every table against its pinned SHA-256. Run twice from the raw files, the pipeline writes byte-identical outputs: the SHA-256 of all eight prepared files is equal across runs. The data are licensed under CC BY 4.0 [5], which requires citing the dataset's descriptor by Kuzilek, Hlosta and Zdrahal and allows the prepared views to be shared with that attribution. The Final Project Package therefore carries the access instructions, the pinned download, the pipeline and the data dictionary, so that the prepared data can be rebuilt outside our repository.

**Sensitivity of the KPI to flagged records.** The 138 enrolments flagged for an unknown withdrawal day (93) or registration day (45) barely move the KPI: completion in the day-14 population is 54.74% on all 28,061 enrolments and 54.93% without the flagged ones. In the 9 runs of 2013, 21 enrolments carry such a flag, 8 of them in the day-14 population, so the AQ1 rate without them serves as a baseline check (Section 9.1). The early-sign rule, computed without any outcome, flags between 8.4% and 44.0% of enrolments per run at day 13 and between 17.9% and 54.8% at day 27, so its reach differs widely between runs.

**Synthetic data.** Synthetic data are used only at the lowest level: a few hand-made test enrolments check the feature formulas in unit tests, and they never enter a prepared view, a statistic or a finding. Every number in this report therefore comes from the recorded OULAD data. With the data prepared, versioned and reproducible, Section 8 maps each question to the analysis that answers it.
