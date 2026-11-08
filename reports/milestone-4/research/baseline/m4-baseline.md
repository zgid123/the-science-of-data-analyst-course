# Milestone 4 baseline: Milestone 3 as submitted

Verbatim copies of the Milestone 3 report and package files that Milestone 4 starts from.

## Goal, KPIs, decisions and AQ1–AQ4 (Milestone 3, Section 1.1)

Source: `reports/milestone-3/report/01-01-baseline-aqs.md` (SHA-256 3ed6d190f2d108c4)

## 1.1. Baseline and Current Analytical Questions

**Goal and measures.** The Business Goal is to improve successful course completion in a university program's online
and blended courses by identifying students who stop taking part early enough to support them within the semester.
The specific, measurable, achievable, relevant and time-bound (SMART) Goal turns this into a target: the completion
rate of students enrolled after the add-drop period, the first weeks in which students may still register for or
drop a course, rises in the pilot courses from a baseline that the pilot will recount from the university's records,
assumed for now to be 70%, by five percentage points to 75% by the end of the 2027–2028 academic year. Completion means passing the course; a fail or a withdrawal counts as
non-completion.

Three key performance indicators (KPI) track the goal. The primary KPI is the course completion rate itself. The
first secondary KPI, the early-sign contact rate, is the share of students showing early signs of disengagement who
are contacted by the end of week 5; the early signs are defined by the early-sign rule, which in Milestone 1 reads
"two or more assessed tasks missed or submitted late by the end of week 4". The second secondary KPI, the follow-up
rate, is the share of students on a contact list who are contacted within seven days of the list reaching staff.
Both secondary KPIs rely on a contact record, a shared log of who contacted which student, when and with what result,
which the university does not keep yet.

**Decisions.** The proposal supports three decisions. D1 is whom the lecturer-advisors and the support office contact
at each review point, a moment in weeks 3 and 5 of the semester when a contact list reaches staff; each list uses the
data up to its data cut-off, the end of week 2 for the week-3 list and the end of week 4 for the week-5 list,
because data exports take about a week. D2 is where the program manager places the time of the support office and
the lecturer-advisors each semester, and D3 is whether to extend the approach to all courses after the pilot.

**Changes from Milestone 2.** Milestone 2 selected the Open University Learning Analytics Dataset (OULAD) as an open
stand-in for the university's own records, which cannot be used yet, and recorded eight changes, C01 to C08, in the
Controlled Change Log, the list of every change to the baseline with its reason in the data. They set the population
to the OULAD module runs of 2013–2014, time to days from the start of each run with cut-offs at day 13 and day 27, the
KPI denominator to the enrolments still registered on day 14 and the test to the 2014 runs of models built on 2013;
they replace comparisons by delivery mode and year of study with comparisons by module and run, drop the attendance
sign, count one missed or late task in the early-sign rule on OULAD, and leave the choice of contact to the pilot.
Appendix IV gives each change with its reason.

**The questions as they stand.** Table 1.1 gives the four analytical questions (AQ) after the changes of Milestone 2
and the data gap decisions of this milestone, with the type of analytics each belongs to and the decision each
supports.

**Table 1.1. AQ1–AQ4 as they stand**

| AQ | Analytics type | Current question | Decision supported |
| :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | What share of enrolments end in pass, fail or withdrawal, by module, run, start month and year, and in which week non-completers first miss an assessed task? | D2: where to place support time; D3: whether to extend |
| AQ2 | Diagnostic | Which signs recorded by the end of week 4 (missed and late tasks, inactivity, activity against the run's median) go with later non-completion, compared within each module? | D2, and the reasons shown with each name in D1 |
| AQ3 | Predictive | How well can non-completion be estimated from the data up to the end of week 2 and of week 4, compared with the early-sign rule, when a model built on the 2013 runs is applied to the 2014 runs? | D1: who is listed |
| AQ4 | Prescriptive (ranking) | Which enrolments should rank first on a list of an assumed capacity, with what gain over a random list and what recall, overall and by deprivation band and disability? | D1: whom to list first; the choice of contact is deferred to the pilot |

The Business Goal, the SMART Goal and the three decisions are the same as in Milestone 1. The data understanding of
this milestone led to five further changes, C09 to C13, which narrow how the questions are measured on OULAD without
changing what they ask; Section 4 explains each of them, and Appendix IV gives the full Change Log.

## AQ–Data Fit ratings (Milestone 3, Section 4.1)

Source: `reports/milestone-3/report/04-01-fit-ratings.md` (SHA-256 711650822c0bcd58)

## 4.1. AQ–Data Fit Ratings

Each question is rated against the claim it carries after the Milestone 2 changes C01–C08. Table 4.1, the AQ–Data
Fit Decision Log, gives for each question its rating, what the real data support, what is missing or weak, the step
of the decision procedure that settles the gap and the change it leads to.

**Table 4.1. AQ–Data Fit Decision Log**

| AQ | Rating | Supported by real data | Missing or weak | Action (step) | Change |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | YELLOW | Final result of all 32,593 enrolments in 22 runs; due days of 182 TMA and CMA tasks and their submissions | Year of study and delivery mode (all runs are distance learning); exam results in 5 of 7 modules | Derive the first missed task over TMA and CMA (2); keep the comparisons OULAD holds (4) | C09 |
| AQ2 | YELLOW | Daily click records; tasks due by day 27 in 16 of 22 runs; 1,382 enrolments in two runs at once, 1,370 of them in 2014 | Attendance; year of study and delivery mode | Derive each sign with a formula and a window (2); task signs in the 16 runs with a task due; the several-modules sign for 2014 only (4) | C12 |
| AQ3 | YELLOW | Target for every enrolment; 28,069 enrolled at day 13 and 27,535 at day 27; 9 module and start-month pairs in both years | The rule counting missed or late tasks fires in 1 run at day 13 and 16 at day 27; no day on which a TMA mark was released | No marking dates in any field (1); restate the rule (2); CMA marks known by the cut-off only (4) | C10 |
| AQ4 | RED | Ranking from AQ3; enrolment counts for capacity scenarios | Contacts, contact types, staff capacity and outcomes after contact | No compatible open dataset (3); rewrite to the ranking part (4); defer the contact choice (5) | C11, C13 |

Five changes follow from these ratings, and each narrows how a question is measured without changing what it asks.
The population rule (C09) counts an enrolment as enrolled on a given day when the student registered by that day, or
the registration day is unknown, and did not unregister by it; it removes the 58 late registrants from the Milestone 2
count of 28,119, which took every enrolment still registered on day 14, and leaves 28,061 enrolments in the KPI population.

The sign "tasks missed in several modules at once" is described for the 2014 runs only, because only 12 of the 1,382 concurrent enrolments fall in the 2013 training
runs (C12).

The early-sign rule counts one missed or late task on OULAD (C06), but no task falls due by day 27 in 6 runs or
by day 13 in 21, so in those runs it can flag no one; it therefore becomes "a task due by the cut-off not submitted, or a TMA submitted late, or no platform
activity in the seven days before the cut-off" (C10), whose inactivity part can flag students in every run.

AQ4 is rated RED because its contact part has no data
at all; it is rewritten to its ranking part, which rests on AQ3, and the choice of contact
is deferred to the pilot, because no dataset records contacts (C11).

Finally, the Milestone 1 limit of 50% precision,
the share of listed students who later fail or withdraw, says little when 44–45% of students do not complete, since a random list already reaches about 45%, so a
list is judged by its lift, its precision divided by the run's rate of non-completion, and by its recall, the share of
later non-completers it reaches, against the most a list of its length can reach (C13). Appendix IV explains each
rating in full and gives the Controlled Change Log.

## Model Readiness Matrix (Milestone 3, Section 8.2)

Source: `reports/milestone-3/report/08-02-readiness-matrix.md` (SHA-256 5b95c87f8a48677f)

## 8.2. Model Readiness Matrix

Table 8.1, the Model Readiness Matrix of the brief, gives for each question the prepared view, the target or measure,
the feature set or dimensions, the split or time rule and the readiness for Milestone 4 [1]. A question is Ready when
its view, target and rules are fixed and validated, and Revise when part of it still lacks data.

**Table 8.1. Model Readiness Matrix**

| AQ | Analytics type | Prepared view | Target / measure | Feature set / dimensions | Split / time rule | Readiness |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | enrolment, assessment_due | Completion rate; week of the first missed task | Module, run, start month, year | All 22 runs; KPI population enrolled at day 14 | Ready |
| AQ2 | Diagnostic | features_d27, enrolment | non_completion | Missed tasks, late TMA and CMA, inactivity in the last seven days, activity against the run median; concurrent runs for 2014 only | Signs up to day 27; task signs in the 16 runs with a task due | Ready, for association only |
| AQ3 | Predictive | features_d13, features_d27, model_ready | non_completion at the run end | 20 primary and 10 extended predictors and weekly clicks; the early-sign rule as comparison | Train on 2013, test on 2014; tuning by leave-one-run-out folds inside 2013 | Ready; the day-13 list rests on activity only |
| AQ4 | Prescriptive (ranking) | capacity_by_run with AQ3 scores | Lift over the run's rate; recall against the most a list of that size can reach | Lists of 3 or 5 per tutor group of 20, or 30 or 40 per run; audit by deprivation band and disability | Per run and cut-off, test runs only | Revise: the ranking is ready; the choice of contact is deferred |

**Why a ranking is needed.** The early-sign rule flags 20.2% of enrolled students at day 13 and 28.8% at day 27,
while lists of 3 or 5 per group of 20 students hold 15% or 25% of them. The rule names more students than a list of 5
per 20 can hold in 7 of the 22 runs at day 13 and in 10 at day 27, and more than a list of 3 per 20 can hold in 15 runs
at day 13 and in all 22 at day 27. Staff therefore need an order of whom to contact first, which is what AQ3 and AQ4
provide; the rule alone cannot set it.

**Questions not yet feasible.** Three parts of the proposal cannot be answered with OULAD and need the pilot's own
records: which contact, a lecturer's message, a call from the support office or a referral, works best for which
student, and its effect on completion (AQ4, C08, C11); comparisons by year of study, by delivery mode and by attendance
(C04, C05); and the follow-up rate of secondary KPI 2 with the contact part of secondary KPI 1 (C08).

**Entry conditions for Milestone 4.** The brief sets six conditions for starting to model [1]: the core questions
have prepared views with clear traceability; target, features and dimensions are stable; leakage and split are defined
for predictive tasks; important quality issues are handled or kept on purpose; no synthetic data serve as evidence;
and the prepared data can be rebuilt from the raw files. All six hold for AQ1 to AQ3, so Milestone 4 can
start with them; AQ4 enters it as a ranking question, and its contact part waits for the pilot. Appendix VI (Table
A.19) gives the state of each condition.

## Split and leakage control (Milestone 3, Section 6.3)

Source: `reports/milestone-3/report/06-03-split-leakage.md` (SHA-256 c3a4781cdab24cc6)

## 6.3. Split Strategy and Leakage Control

**Leakage.** Leakage is the use of information about the target that would not be available at the moment of
prediction, and it makes a model look better in evaluation than it can be in use [10], [11]. The brief names five
forms of it for education data and asks for a rule against each [1]. Table 6.2 matches each form to its case in
OULAD, the control the pipeline applies and the check that would fail if the control broke.

**Table 6.2. Leakage risks and controls**

| Risk (brief) | Case in OULAD | Control | Check |
| :---- | :---- | :---- | :---- |
| Target leakage | Final result, withdrawal day, activity or submissions after the cut-off, TMA marks, whole-run measures | Feature views built only from events dated up to the cut-off; CMA marks only, seven days after submission; target and whole-run measures outside the predictor lists | V11, V13, V14 |
| Train–test contamination | Medians, scales and category levels computed on all runs | Fitted on the 2013 runs only and applied to the 2014 runs | V12 |
| Student leakage | 1,962 test enrolments of students who also enrolled in 2013 | Kept in the main test and flagged for a strict check; tuning folds keep each student on one side | V15 |
| Temporal leakage | A random split mixing the two years; tuning on 2014 | Training on 2013 (9 runs), test on 2014 (13 runs); tuning only inside 2013 | V15 |
| Augmentation leakage | None: no synthetic augmentation | – | – |
| Cohort statistic (a value computed on the same run) | The activity ratio uses the median of the same run | Only activity up to the cut-off of students enrolled at it; no outcome | V13 |

**Time split.** The data are split by year: the 9 runs of 2013 form the training set and the 13 runs of 2014 the
test set. This follows the OU's own practice of building at-risk models on previous runs of a module and applying
them to the run in progress [12], and the rule that data ordered in time are evaluated on later observations [13]. A
random split would mix the two years and let a model learn from the year it is tested on. Of the 13 test runs, the 9
whose module and start month also ran in 2013 test the claim directly, and the other 4 test a model on a module or
start month it has not seen, so their results are reported separately.

Three further controls complete the split. The 1,962 test enrolments of students who also enrolled in 2013 stay in the
main test set, because a later run of the same modules also contains repeating students, and a flag lets Milestone 4
repeat the test on unseen students; tuning uses leave-one-run-out folds inside 2013, and students who also appear in
the held-out run are removed from that fold's training data [13]. Transforms that learn parameters, such as a median for filling or a scale, are fitted on the training runs
alone [11], and refitting them after the values of every test row had been altered gave the same parameters. The 2014 outcomes are
not looked at while the data are prepared, and test results will also be reported without the test enrolments that are Withdrawn without a withdrawal day, 89 at
day 13 and 90 at day 27. Appendix II explains these controls in full.

## Change Log C09–C13

Source: `reports/milestone-3/package/data/metadata/change_log.md` (SHA-256 d3478a61e8c1e502)

| ID | Milestone | Old content | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C09 | 3 | KPI denominator: enrolments still registered at day 14 (28,119; C03) | Enrolled at day d = registered by day d (or registration day unknown) and not unregistered by day d; day 14 for the KPI (28,061), days 13 and 27 for the lists (28,069; 27,535) | 58 enrolments registered after day 14, up to day 167 (DQ05) | Primary KPI recomputed on 28,061 enrolments; same rule for every population |
| C10 | 3 | AQ3 comparison rule and secondary KPI 1 early-sign rule: two or more assessed tasks missed or late by week 4 (Milestone 1); on OULAD one missed or late task, in the 16 runs with a task due by day 27 (C06) | Early-sign rule: at least one TMA or CMA due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off; CMA lateness only in a sensitivity variant | Two or more tasks are due by day 27 in 1 of 22 runs, one or more in 16, and by day 13 in 1 (DQ18), so a rule on tasks alone cannot fire in 6 runs at day 27 or in 21 at day 13; the meaning of a late CMA in 2013–2014 is undocumented (DQ10) | The rule can fire in every run; secondary KPI 1 (sign part) uses the same rule |
| C11 | 3 | AQ4: whom to list, in what order and with which contact, within capacity | AQ4 (rewritten): ranking under an assumed capacity with recall and precision overall and by deprivation band and disability; the choice of contact and its effect deferred to the pilot | No contact, capacity or outcome-after-contact data (C08; AQ4 RED) | No prescriptive claim; D1 receives an ordered list and its measured quality, not a contact plan |
| C12 | 3 | AQ2 sign "tasks missed in several modules at once", all runs | Described for 2014 runs only; not a predictor in AQ3 | Of 1,382 concurrent enrolments at day 14, 12 fall in 2013 runs (training runs) | AQ2 narrowed; AQ3 feature set excludes it |
| C13 | 3 | AQ4 list limit: precision of at least 50% | List quality measured as lift over the run's base rate and as recall against the most a list of the same size can reach, with a random list and the early-sign rule as baselines | Non-completion is 45.3% at day 13 and 44.2% at day 27, and 24.9–58.3% by run, so a random list already reaches about 45% precision; lists of 3 or 5 per 20 students cap recall | AQ4 limit re-expressed; D1 judges a list by its gain over chance |

## Predictor sets

Source: `reports/milestone-3/package/data/metadata/predictor_sets.json` (SHA-256 0ad6ee292b134a7f)

```json
{
  "rule": "the only columns a model may use; everything else in a feature view is id, split, evaluation, target, rule or audit (data_dictionary.md)",
  "primary": [
    "code_module",
    "start_month",
    "highest_education",
    "num_of_prev_attempts",
    "studied_credits",
    "registration_lead",
    "banked_results",
    "clicks_pre",
    "clicks_0c",
    "active_days_0c",
    "sites_0c",
    "inactive_last7",
    "activity_ratio_run",
    "tasks_due_c",
    "tasks_missed_c",
    "tasks_late_c",
    "tma_late_c",
    "cma_late_c",
    "cma_marked_c",
    "cma_score_mean_c"
  ],
  "extended": [
    "registration_missing",
    "clicks_0c_dedup",
    "clicks_pre14",
    "days_since_last_click",
    "trend_last_week",
    "tasks_submitted_early_c",
    "clicks_oucontent_0c",
    "clicks_forumng_0c",
    "clicks_quiz_0c",
    "clicks_homepage_0c"
  ],
  "weekly_clicks": {
    "d13": [
      "clicks_w1",
      "clicks_w2"
    ],
    "d27": [
      "clicks_w1",
      "clicks_w2",
      "clicks_w3",
      "clicks_w4"
    ]
  },
  "not_used_in_milestone4": {
    "cma_score_mean_c": "known for fewer than 10% of training rows at both cut-offs"
  }
}
```

## Split specification

Source: `reports/milestone-3/package/data/metadata/split_spec.md` (SHA-256 76bd2807a66b403d)

# Split and leakage specification (Task 6, brief section 11)

| Risk (brief 11) | Case in this project | Control | Where | Check |
| :---- | :---- | :---- | :---- | :---- |
| Target leakage | final_result, withdrawal day, activity or submissions after the cut-off, TMA marks (release day unknown), whole-run measures | Feature views computed only from events dated ≤ c; target and whole-run measures kept out of the predictor list; CMA marks only | `prepare_data.py` step 8; dictionary role | V13 (max event day per feature ≤ c), V14 (roles) |
| Train–test contamination | Imputation values, scaling, category levels, log transforms fitted on all runs | Fitted on training runs (2013) only and applied to test runs | `fit_transforms.py` | V12 (parameters unchanged when test rows are altered) |
| Student leakage | 2014 enrolments of students already seen in 2013 runs | Main test keeps them (the claim is a later run of the same modules, where repeaters exist); `student_in_training_runs` marks them for a strict unseen-student check | `prepare_data.py` step 9 | V15 flag recomputed independently |
| Temporal leakage | Random split across years; tuning on 2014 | Split by run year: training 2013B, 2013J (9 runs); test 2014B, 2014J (13 runs); tuning only inside 2013 by leave-one-run-out folds that also keep each student in one fold; intervals by bootstrap clustered by student; 2014 outcomes are not looked at while preparing | `prepare_data.py` step 9; Milestone 4 protocol | V15 (no run in both partitions); validation reports test outcome rates only as counts |
| Cohort statistic | `activity_ratio_run` uses the same run's median up to c | Uses only pre-cut-off activity of students enrolled at c, no outcome; the same value is known to staff on day c | step 8 | V13 |
| Augmentation leakage | None: no synthetic augmentation | – | – | – |

Paired subset: the 9 test runs whose module and start month also ran in 2013 (BBB-B, DDD-B, FFF-B, AAA-J, BBB-J,
DDD-J, EEE-J, FFF-J, GGG-J); the other 4 test runs (CCC-B, CCC-J, EEE-B, GGG-B) test a model trained on other
modules or start months and are reported separately.

## Entry gate (brief section 3)

| Condition | Evidence | Status |
| :---- | :---- | :---- |
| Approved Analytical Questions | AQ1–AQ3 ready, AQ4 revised to ranking with contact deferred (C11, C13); no deferred part brought back | PASS |
| Prepared dataset | version OULAD-N04-prepared-1.0; data dictionary, unit, keys, target non_completion, feature windows to day 13 and day 27 | PASS |
| Leakage controls | prediction points day 13 and day 27; training 2013, test 2014; transforms fitted on 2013; validation 22 of 22 checks PASS | PASS |
| Known limitations | Data Quality Issue Log DQ01–DQ19; sensitive attributes kept for audit; representativeness and data protection stated (Milestone 3 Parts 3 and 9) | PASS |
| Traceability | AQ → data requirement → actual variables → prepared view (Milestone 3 Appendix IV, Table A.13) | PASS |
