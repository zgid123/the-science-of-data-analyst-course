# Data Requirement Specification (T05, Tasks 1–2)

Written on 2026-11-06 from the frozen Milestone 1 baseline (`research/baseline/m1-baseline.md`) before any candidate
dataset was examined (brief section 5: "Không dùng tên cột của dataset đang xem để 'viết ngược' requirement").
Variables are named as concepts, not as columns of any dataset.

## 1. Specification per analytical question (Task 1 fields)

### AQ1 – Descriptive (pass, fail and withdrawal shares; timing of the first missed task)

| Field | Requirement |
| :---- | :---- |
| Population / scope | Students enrolled after the add-drop period in online and blended courses of one program |
| Unit of analysis | One student's enrolment in one course in one semester (student–course–semester) |
| Outcome / measure | Final result in three classes (pass, including any higher passing grade; fail; withdrawal); week of the first missed assessed task, counting only tasks due before the student's withdrawal date |
| Dimensions | Course; semester; delivery mode (online, blended); year of study |
| Time window and granularity | At least four consecutive semesters; week within the semester for the first missed task |
| Minimum variables | Persistent pseudonymous student identifier; course and semester identifiers; course start date; enrolment start and end dates; final result; withdrawal indicator and date; assessed tasks with due dates; submissions with dates |
| Optional variables | Delivery mode; year of study; student status (approved leave, transfer) to apply the withdrawal definition |
| Availability timing | Outcome known after the semester; fine for a descriptive question |
| Ethics / sensitivity | No sensitive attribute needed; results reported for groups, not names |

### AQ2 – Diagnostic (early signs associated with later non-completion)

| Field | Requirement |
| :---- | :---- |
| Population / scope | As AQ1 |
| Unit of analysis | Student–course–semester, with weekly observations for weeks 1–4 |
| Outcome / measure | Later non-completion (fail or withdrawal) against completion; difference in non-completion rates between students with and without each sign |
| Explanatory factors | Missed and late assessed tasks in weeks 1–4 (only tasks due before the student's withdrawal date); learning-platform activity per week relative to the course's own average; missed tasks in several courses in the same semester; in-class attendance (blended courses) |
| Time window and granularity | Weeks 1–4 of each semester at day or week granularity; same four semesters |
| Minimum variables | AQ1 variables plus dated learning-platform activity per student (day or week) and dated submissions; course membership of each student in the same semester |
| Optional variables | Attendance; delivery mode; year of study; background attributes to check that associations hold across groups |
| Availability timing | Signs observed in weeks 1–4; outcome after the semester |
| Ethics / sensitivity | Background attributes (e.g. disability, socio-economic status) only to check consistency across groups; never to label students |

### AQ3 – Predictive (non-completion estimated at the end of weeks 2 and 4)

| Field | Requirement |
| :---- | :---- |
| Population / scope | Students still enrolled at the data cut-off in the pilot-type courses |
| Unit of analysis | Student–course–semester at each data cut-off |
| Target | Non-completion by the end of the semester: fail or withdrawal (binary) |
| Features | Activity and assessment signs recorded by the cut-off; enrolment start date; background known at enrolment (prior attempts, study load at enrolment) |
| Time window and granularity | Day-level timestamps (or week) counted from the course start date, to apply cut-offs at the end of week 2 and week 4; at least three course runs ordered in time, so that earlier runs train and a later one tests |
| Minimum variables | AQ2 variables with timestamps, plus the date of withdrawal to tell who is still enrolled at each cut-off |
| Optional variables | Year of study (first-year against later-year comparison); other group attributes for the fairness check |
| Availability timing | Features only from data recorded by the cut-off; target after the semester (see section 3) |
| Ethics / sensitivity | Group attributes used to check that recall is similar across groups, not as predictors that label students |

### AQ4 – Prescriptive (whom to list, in which order, with which contact)

| Field | Requirement |
| :---- | :---- |
| Population / scope | Students on the contact lists of weeks 3 and 5 |
| Unit of analysis | Student per review point (list entry) |
| Outcome / measure | Later non-completers reached by the list (recall) and share of listed students who later fail or withdraw (precision), within capacity; for the action: outcome after contact |
| Decision inputs | AQ3 estimates and reasons; weekly contact capacity per lecturer-advisor and support office (a baseline assumption, not data); routing options; assignment of each student to a lecturer-advisor (optional) |
| Time window and granularity | Per review point; per week for capacity |
| Minimum variables | AQ3 outputs, one list entry per student across courses; capacity figures (assumption); a contact record (who contacted whom, when, how, with what result) – declared a data gap now, since no open dataset is expected to hold the team's future contacts |
| Optional variables | Post-contact engagement and outcome; cost of each contact type |
| Availability timing | Capacity known before the list; contact results only after the pilot |
| Ethics / sensitivity | Contact record is personal data under a stated purpose; referrals to student affairs may carry financial or personal information and are sensitive; support only, never grading |

## 2. AQ–Data Requirement Matrix (brief section 5.1)

| AQ | Analytics type | Unit of analysis | Outcome / measure | Required variables | Time / granularity | Decision point |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Student–course–semester | Pass / fail / withdrawal; week of first missed task | Student, course, semester identifiers; final result; withdrawal date; task due and submission dates | Four semesters; week | D2: where to place advisors' time (end of semester) |
| AQ2 | Diagnostic | Student–course–semester with weekly signs | Difference in non-completion rates by sign | AQ1 variables + dated LMS activity, missed and late tasks, concurrent courses | Weeks 1–4; day or week | D2; reasons shown in D1 |
| AQ3 | Predictive | Student–course–semester at each cut-off | Non-completion by semester end | Timestamped activity and submissions, withdrawal date, registration, background at enrolment | Cut-offs end of week 2 and week 4; ≥ 3 semesters | D1: lists in weeks 3 and 5 |
| AQ4 | Prescriptive | Student per review point | Recall and precision within capacity; outcome after contact | AQ3 output, weekly capacity, contact record | Per review point and week | D1: whom to contact, by whom, with which offer |

## 3. Prediction point and leakage (brief section 6.1)

| AQ predictive | Prediction point | Target | Features allowed before the point | Fields unavailable / leakage risk |
| :---- | :---- | :---- | :---- | :---- |
| AQ3, week-3 list | End of week 2 (data cut-off; list reaches staff in week 3) | Fail or withdrawal by the end of the semester | Activity up to the end of week 2; submissions and their timeliness for tasks due by then; registration date; background known at enrolment | Final result; withdrawal date after the cut-off; scores and submissions of tasks due later; activity after the cut-off; exam results; any field updated at the end of the semester |
| AQ3, week-5 list | End of week 4 (list reaches staff in week 5) | Same | As above up to the end of week 4 | As above, after week 4; also activity logged after a student's own withdrawal date |
| Both cut-offs | – | – | Course averages computed only from training runs and only up to the cut-off | Course average over the whole semester or including test-run students |
| Both cut-offs | – | – | Scores only when the mark was known by the cut-off | Marks released after the cut-off for tasks due before it |
| Both cut-offs | – | – | Study load and concurrent courses as at enrolment or the cut-off | Study load measured at the end of the semester (includes later drops) |
| Both cut-offs | – | – | Background values as recorded at enrolment | Background fields updated later in the semester |
| Both cut-offs | – | – | Scaling and encodings fitted on training runs only | Any normalisation fitted on all runs before the time split |

The cut-offs at the ends of weeks 2 and 4 leave one week for the data delay that the data office expects, so the lists
reach staff in weeks 3 and 5.

## 4. Requirements by analytics level (brief section 6, Task 2)

| Level | AQ | Minimum data | Status of evidence the data can give |
| :---- | :---- | :---- | :---- |
| Descriptive | AQ1 | Clear outcome, course and semester dimensions, timestamps of tasks, the right denominator (enrolled after add-drop) | Rates and timing |
| Diagnostic | AQ2 | AQ1 + explanatory signs with dates, comparison groups (completers against non-completers), consistency across groups | Associations, not causes |
| Predictive | AQ3 | Labelled outcome, predictors timestamped before the prediction point, enough semesters for time-based validation | Held-out accuracy at a fixed list length |
| Prescriptive | AQ4 | Actions (contacts), constraints (capacity), outcomes after action | Ranking under constraints only, unless intervention data exist; otherwise a data gap (brief section 6, warning) |

## 5. Gates for the dataset search (derived from sections 1–4)

Must-have (a candidate failing any gate is rejected whatever its score):
- G1 Outcome: one record per student–course enrolment with a final result that separates pass, fail and withdrawal,
  and a dated withdrawal.
- G2a Dated assessed tasks: due dates and dated submissions per student, counted from the course start.
- G2b Dated activity: learning-platform activity per student at day or week granularity.
- G3 History: at least three runs of the same courses, ordered in time, with a later run available for testing.
- G4 Access: an open license that allows academic use, official documentation and verifiable provenance.
- G5 Privacy and linkage: anonymised or pseudonymised data with a persistent student identifier across tables and
  course runs.

Nice-to-have: several courses; assessed tasks due within weeks 1–4; enrolment start and end dates relative to the
course start; leave and transfer distinction; background attributes for consistency and fairness checks; delivery
mode; year of study; attendance; assignment to advisors; at least 100 later non-completers per compared group in the
test run; contact or intervention records.

## 6. Clauses that become Partial when an optional variable is missing

| Missing optional variable | Clauses affected |
| :---- | :---- |
| Delivery mode | AQ1 and AQ2 comparisons by delivery mode |
| Year of study | AQ1 and AQ2 comparisons by year; AQ3 first-year against later-year comparison; AQ4 recall-gap limit (needs another group attribute) |
| Leave and transfer distinction | Primary KPI denominator (recorded as a deviation from Circular 83/2026 counting) |
| Attendance | AQ2 attendance sign (blended courses) |
| Contact record | AQ4 action and outcome; Secondary KPI 2; Secondary KPI 1 contact part |
