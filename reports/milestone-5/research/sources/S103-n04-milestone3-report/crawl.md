---
id: S103
url: reports/milestone-3/report/00-1-abbreviations.md
requested: reports/milestone-3/report/00-1-abbreviations.md reports/milestone-3/report/00-2-glossary.md reports/milestone-3/report/01-00-baseline-dataset.md reports/milestone-3/report/01-01-baseline-aqs.md reports/milestone-3/report/01-02-dataset-entry-gate.md reports/milestone-3/report/02-00-data-understanding.md reports/milestone-3/report/02-01-population-unit-keys.md reports/milestone-3/report/02-02-outcome-time-measures.md reports/milestone-3/report/02-03-codes-sensitive.md reports/milestone-3/report/03-00-profiling-quality.md reports/milestone-3/report/03-01-shape-keys-joins.md reports/milestone-3/report/03-02-missingness-validity.md reports/milestone-3/report/03-03-distributions-outcome.md reports/milestone-3/report/03-04-temporal-representativeness.md reports/milestone-3/report/03-05-quality-issue-log.md reports/milestone-3/report/04-00-aq-data-fit.md reports/milestone-3/report/04-01-fit-ratings.md reports/milestone-3/report/04-02-gap-decisions.md reports/milestone-3/report/05-00-preparation-plan.md reports/milestone-3/report/06-00-preparation-pipeline.md reports/milestone-3/report/06-01-pipeline-steps.md reports/milestone-3/report/06-02-integration-features.md reports/milestone-3/report/06-03-split-leakage.md reports/milestone-3/report/07-00-prepared-validation.md reports/milestone-3/report/07-01-before-after.md reports/milestone-3/report/07-02-lineage-dictionary.md reports/milestone-3/report/07-03-residual-risks.md reports/milestone-3/report/08-00-readiness.md reports/milestone-3/report/08-01-views-by-level.md reports/milestone-3/report/08-02-readiness-matrix.md reports/milestone-3/report/09-00-ethics-limitations.md reports/milestone-3/report/10-00-genai-reflection.md reports/milestone-3/report/11-references.md reports/milestone-3/report/12-00-appendices.md reports/milestone-3/report/12-01-profiling-details.md reports/milestone-3/report/12-02-pipeline-package.md reports/milestone-3/report/12-03-dictionary-lineage.md reports/milestone-3/report/12-04-traceability-change-log.md reports/milestone-3/report/12-05-ai-decision-log.md reports/milestone-3/report/12-06-validation-ledger.md
fetched: 2026-11-08T23:22+07:00
tool: fetch.py local (git show 19d35a4; verbatim, 40 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T05
part: 1
raw: raw.txt (166 KB)
conversion: verbatim copy of 40 file(s) from milestone-da at 19d35a4
---
===== reports/milestone-3/report/00-1-abbreviations.md @ 19d35a4 =====
# List of Abbreviations

The abbreviations below are listed in alphabetical order, each with its full form and its role in this report.

| Abbreviation | Full form | Role in this report |
| :---- | :---- | :---- |
| AI | Artificial intelligence | Generative AI agents served as interpreters, critics, code and documentation assistants (Section 10) |
| AQ | Analytical question | The four questions AQ1 to AQ4 (Section 1.1) |
| CMA | Computer-marked assessment | Automatically marked task of an OU module (Section 2.2) |
| CSV | Comma-separated values | Format of the raw OULAD tables (Section 1.2) |
| DOI | Digital object identifier | Persistent identifier of the collected dataset version (Section 1.2) |
| EDA | Exploratory data analysis | One of the AI roles the brief allows: exploratory data analysis and quality checklist partner (Section 10) |
| IMD | Index of Multiple Deprivation | Area-level deprivation measure behind imd_band (Section 2.3) |
| KPI | Key performance indicator | Primary and secondary measures of the SMART Goal (Section 1.1) |
| OU | Open University | UK distance-learning university that published OULAD (Section 1.2) |
| OULAD | Open University Learning Analytics Dataset | The dataset prepared in this milestone (Section 1.1) |
| SHA-256 | Secure Hash Algorithm 256 | Checksum that pins every raw file (Section 1.2) |
| SMART | Specific, measurable, achievable, relevant and time-bound | The criteria of the project goal (Section 1.1) |
| TMA | Tutor-marked assessment | Task marked by the student's tutor (Section 2.2) |
| UK | United Kingdom | Country of the OULAD population (Section 2.1) |
| UTC | Coordinated Universal Time | Time standard of the pipeline logs and the version manifest (Section 6.1) |

===== reports/milestone-3/report/00-2-glossary.md @ 19d35a4 =====
# List of Terms

The terms below are listed in alphabetical order with their meaning in this report and the section that defines them.

| Term | Meaning in this report |
| :---- | :---- |
| Add-drop period | The first weeks of a course in which students may still register for or drop it (Section 1.1) |
| Audit attribute | A sensitive attribute kept in every view to check fairness, outside both predictor sets (Section 9) |
| Banked result | An assessment result carried over from an earlier run of the module, dated −1 in the data (Section 2.2) |
| Checksum | A fingerprint of a file's exact content, which changes if a single byte changes (Section 1.2) |
| Concurrent enrolment | An enrolment of a student who is also enrolled in another module run of the same year and start month (Section 4.1; C12) |
| Contact record | A shared log of who contacted which student, when and with what result; not yet kept by the university (Section 1.1) |
| Data cut-off | The last day whose data a list may use: day 13 (end of week 2) or day 27 (end of week 4) (Section 1.1) |
| Early-sign rule | A task due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off (Section 4.1) |
| Enrolled at day d | Registered by day d, or registration day unknown, and not unregistered by day d (Section 4.1; C09) |
| Enrolment | One student in one module run, the unit of analysis (Section 2.1) |
| Fit rating (GREEN, YELLOW, RED) | Full, partial or no support of a question by the real data (Section 4) |
| Grain | The level of detail that one row of a table represents (Section 3.1) |
| Leakage | Use of information about the target that would not be available at the moment of prediction (Section 6.3) |
| Leave-one-run-out folds | Tuning folds inside the 2013 runs in which each run is held out once (Section 6.3) |
| Lift | The precision of a list divided by the run's rate of non-completion; 1 means no better than a random list (Section 4.1) |
| Missing variable | A concept the dataset never collected, as opposed to a missing value of a collected field (Section 4.2) |
| Model-ready matrix | A copy of a feature view with encoded and scaled columns, its parameters fitted on the 2013 runs (Section 6.1) |
| Module run | One presentation of an OU module, named by year and start month, B for February and J for October (Section 2.1) |
| Non-completion | A final result of Fail or Withdrawn; the target of AQ1 to AQ3 (Section 2.2) |
| Paired run | A 2014 test run whose module and start month also ran in 2013 (Section 6.3) |
| Precision | The share of listed students who later fail or withdraw (Section 4.1) |
| Prepared Data Package | The submitted folder of raw links, scripts, prepared views, metadata and logs that rebuilds the prepared data (Section 6.1) |
| Prepared view | An analytic-ready table of the Prepared Data Package with a fixed grain and population (Section 8.1) |
| Primary and extended predictors | The 20 columns a model may use by default and 10 further columns for comparison in Milestone 4 (Section 6.2) |
| Recall | The share of later non-completers who appear on the list (Section 4.1) |
| Recorded absence | A missing row that records an event, such as no click or no submission, counted as zero (Section 4.2) |
| Review point | A moment in weeks 3 and 5 when a contact list reaches staff (Section 1.1) |
| Time split | Training on the 2013 runs and testing on the 2014 runs (Section 6.3) |
| Tutor group | A group of students with one OU tutor; 20 students are assumed to stand for one advisor's caseload (Section 7.3) |

===== reports/milestone-3/report/01-00-baseline-dataset.md @ 19d35a4 =====
# 1. Project Baseline and Dataset

Milestone 3 is the step from understanding the collected data to preparing them for analysis. Its central question,
in the words of the brief, is what the data really contain, how good they are, how they must be prepared and whether
they can still answer the questions we committed to [1]. Its output is an analytic-ready dataset, a set of
tables that the analyses of Milestone 4 can use without further cleaning, built by a pipeline that anyone can rerun
from the raw files [1]. Every preparation decision must therefore have a reason tied to an analytical question, to
the type of analysis, to the structure of the dataset or to a risk of biasing the results, rather than to a wish to
make the data look clean [1].

Section 1.1 restates the baseline and the questions as they stand, and Section 1.2 the dataset and the entry gate.

===== reports/milestone-3/report/01-01-baseline-aqs.md @ 19d35a4 =====
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

===== reports/milestone-3/report/01-02-dataset-entry-gate.md @ 19d35a4 =====
## 1.2. Dataset, Version and Entry Gate

The brief admits a team to Milestone 3 only when its Data Collection Package from Milestone 2 is complete: the
Milestone 1 baseline in force, an updated traceability matrix, raw files kept unchanged, a data dictionary,
collection evidence and the Controlled Change Log [1]. All six inputs are complete; Appendix I (Table A.1) states the
content and status of each.

The raw data are the seven comma-separated values (CSV) tables of OULAD, figshare version 1, with the
digital object identifier (DOI) 10.6084/m9.figshare.5081998.v1. A checksum is a fingerprint of a file's exact content:
the Secure Hash Algorithm 256 (SHA-256) gives a different value if a single byte changes. Each raw table matches the SHA-256 value
pinned in Milestone 2, and the eight files of the Milestone 1 proposal from which the baseline was copied are also
unchanged. In the Prepared Data Package, the raw tables are hard links to those collected files, set to read-only and
checked against their checksums at every run, so they cannot change unnoticed; this meets the brief's rule that raw
data stay immutable and every change produces a new file [1].

The dataset holds 22 module runs of seven Open University (OU) modules from 2013 and 2014, with 32,593 student
records [2]; each record is an enrolment, one student in one run, and the enrolments belong to 28,785 distinct
students (Section 2.1). The brief warns that a team should not continue to cleaning and modelling when the dataset
supports only a very small part of the proposal [1]. OULAD supports AQ1 to AQ3 in part and the ranking part of AQ4,
with a real outcome for every enrolment, assessment dates and daily activity records; only the contact part of AQ4
lacks data, and it is deferred to the pilot (Section 4.1). Every question thus keeps a core that the data answer,
which is far from the very small part the brief warns about, so the entry gate holds, and preparation is
justified.

===== reports/milestone-3/report/02-00-data-understanding.md @ 19d35a4 =====
# 2. Data Understanding

The brief requires the dataset to be described in the terms of the education domain before any profiling or
cleaning, and not by its column names alone [1]. A few facts about the OU frame that description. The
OU teaches courses called modules, each taught in runs, which the data call presentations and which are named by the
year and month they start [2]. Assessment takes three forms: tutor-marked assessments (TMA), marked by the student's
tutor; computer-marked assessments (CMA), marked automatically; and a final exam [2]. Every time field in the data is
a count of days from the start of the run, not a calendar date [2]. The seven tables join through four identifiers:
the student, the module run, the assessment and the learning resource on the virtual learning platform [2].

Building on these facts, Section 2.1 sets the population, the unit of analysis and the keys; Section 2.2 the meaning
of the outcome, of time and of the measures; and Section 2.3 the categorical codes and the sensitive attributes.
Every statement about the data in this part rests on a computed check written by the first script of the Prepared
Data Package, `src/01_understand.py`, to `data/metadata/understanding.json`.

===== reports/milestone-3/report/02-01-population-unit-keys.md @ 19d35a4 =====
## 2.1. Population, Unit of Analysis and Keys

**Population.** The data describe the students enrolled in 22 runs of seven OU modules, four in science, technology,
engineering and mathematics and three in the social sciences, taught by distance learning in the United Kingdom (UK)
in 2013 and 2014 [2]. The modules carry anonymised codes, AAA to GGG [2].
They hold 32,593 enrolments of 28,785 students; 3,538 students enrolled in more than one run,
either in two modules at once or in a later run of the same module. A run code such as 2013J ends in B for a run that
starts in February and in J for one that starts in October, and the authors of the dataset advise analysing B and J
runs separately [2]. The students learn at a distance, which differs from the program's online and blended courses in
Vietnam; Section 3.4 returns to what this difference means for the claims.

**Unit of analysis.** The unit of analysis is the enrolment, one student in one module run, because the outcome, the
KPI denominator and the contact decision all concern a student in a particular course. Some tables hold finer units,
such as one submission or one day's clicks on one resource; these are summed to the enrolment before they are joined
(Section 6.2), so that every prepared table has a single, stated grain.

**Keys and relationships.** Table 2.1, the Dataset Understanding Map that the brief requires, gives for each table its
unit, primary key, foreign key and relationship to its parent table, its main variables, its time field and its role
in the questions [1]. A primary key is the column or set of columns that identifies a row uniquely; a foreign key
points to the row of another table that a row belongs to. Each key in the table was checked on the data.

**Table 2.1. Dataset Understanding Map**

| File / table (rows) | Unit of analysis | Primary key | Foreign key and relationship | Main variables | Time field | Role in AQ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses (22) | module run | module + run | – | run length in days | run length | run end and start month |
| assessments (206) | assessment | id_assessment | → courses, many to one | type (TMA, CMA, exam), weight | due day | tasks due by each cut-off (AQ1–AQ3) |
| vle (6,364) | learning resource | id_site | → courses, many to one | activity type | planned weeks | resource type (AQ2) |
| studentInfo (32,593) | enrolment | run + student | → courses, many to one | final_result, background attributes | – | target; audit attributes (AQ1–AQ4) |
| studentRegistration (32,593) | enrolment | run + student | → studentInfo, one to one | registration and unregistration days | days | populations at each day; KPI denominator |
| studentAssessment (173,912) | submission | assessment + student | → assessments and studentInfo, many to one | submission day, score, banked flag | submission day | missed and late tasks |
| studentVle (10,655,280) | click record | none | → vle and studentInfo, many to one | number of clicks | interaction day | activity (AQ2, AQ3) |

The six tables with a key have no duplicate key, and no row of a child table lacks its parent row, so every
submission, click record and registration belongs to a known enrolment, assessment or resource (Appendix I, Figure
A.1). The click table, studentVle, has no key: the same student, resource and day can appear in several rows, which
Section 3.1 examines.

===== reports/milestone-3/report/02-02-outcome-time-measures.md @ 19d35a4 =====
## 2.2. Outcome, Time and Measurement Semantics

**Outcome.** The outcome is final_result, recorded at the end of each run as Pass (12,361 enrolments), Withdrawn
(10,156), Fail (7,052) or Distinction (3,024); the data descriptor calls the withdrawn value "Withdrawal" [2]. It is
a real outcome, not a proxy, but it is observed only when the run ends, so every feature must be dated before the
moment of prediction. Non-completion, the target of AQ1 to AQ3, is a final result of Fail or Withdrawn, and
completion is Pass or Distinction, which matches the proposal's definition of completion as passing the course.

**Time.** Time is a count of days from day 0, the official start of the run. Students may register from a few months
before the start until two weeks after it [2], so negative days are valid and mean "before the start". Week n covers
days 7(n−1) to 7n−1, so week 1 is days 0 to 6. On this scale the two data cut-offs fall on day 13, the end of week 2,
and day 27, the end of week 4. Each date field has its own meaning: the registration and unregistration days record
when a student joined and left, an empty unregistration day means the student did not withdraw, the assessment date
is the task's due day, which the OU calls its cut-off date [2], and the submission day records when the student
submitted. A field may only feed a prediction once it is known, and Appendix I (Table A.2) gives the meaning, unit
and moment of knowledge of every key field.

**Measures.** Three issues need care before the fields become measures: all 1,909 banked results, carried over from an
earlier run, carry the placeholder submission day −1 and cannot time a submission; a TMA mark is returned by the
tutor, usually within ten working days, and a CMA score within 7 days under the OU's policy of 2025 [3], which is assumed
to hold for 2013–2014, but OULAD holds no day on which a mark was released; and weights and studied credits depart from a simple reading, since coursework weighs zero in the GGG runs
and credits count every module taken at once [2], 60 a year being part-time and 120 full-time study [4]. Appendix I
explains these measures in full.

===== reports/milestone-3/report/02-03-codes-sensitive.md @ 19d35a4 =====
## 2.3. Categorical Codes and Sensitive Attributes

**Codes.** The categorical fields use codes that the data descriptor explains, and none holds an "unknown" or "not
applicable" value. The only gap is a blank deprivation band, and one band label, "10-20", lacks the percent sign that
the other nine labels carry. The deprivation band, imd_band, is the band of the Index of Multiple Deprivation (IMD)
of the student's home area [2]. The English index ranks 32,844 small areas of England into ten deciles, and it
describes the area where the student lives rather than the student [5]. Scotland, Wales and Northern Ireland use their
own indices, which are not directly comparable with the English one [6], so a band does not mean the same thing in
every nation of the UK.

**Sensitive attributes.** The brief asks us to identify attributes such as gender, age, disability,
socioeconomic status and location, which describe protected or vulnerable groups [1]. OULAD holds six of them:
gender, age band, declared disability, deprivation band, region and highest education. We set 20 students as
the lower limit for reporting a group rate run by run, and smaller groups are audited across runs; Appendix I (Table
A.3) gives each attribute with its codes, its smallest group and its groups below 20.

The smallest groups are students aged 55 or over (216 enrolments) and postgraduates (313), and 18 age groups and 29
education groups within single runs hold fewer than 20 students. All six stay in every prepared view: five as audit
attributes outside both predictor sets, and highest education as a predictor whose groups are audited as
well; Section 9 explains why.

===== reports/milestone-3/report/03-00-profiling-quality.md @ 19d35a4 =====
# 3. Data Profiling and Quality

Data understanding must rest on evidence from the data, and the brief lists ten aspects to examine: shape and schema,
missingness, duplicates and key integrity, validity and consistency, distributions, outliers, the balance of the
outcome, temporal coverage, join integrity and representativeness [1]. The profile covers all ten. It ran on all 10.9
million rows of the seven raw tables rather than on a sample, so no rare pattern is missed, and it is written by the
second script of the package, `src/02_profile.py`, to `data/metadata/profile.json`. To guard against an error in that
script, thirteen of its figures were recounted from the same raw files by separate code, our exploration of
the dataset, and all thirteen agree (Appendix I, Table A.5).

Sections 3.1 to 3.4 report the findings by aspect, and each finding that needs a decision receives an issue
identifier, DQ01 to DQ19. Section 3.5 gathers the nineteen issues into the Data Quality Issue Log, with the evidence,
the impact on the questions, a severity and the decision taken.

===== reports/milestone-3/report/03-01-shape-keys-joins.md @ 19d35a4 =====
## 3.1. Shape, Keys, Duplicates and Joins

Every table holds the number of rows that its documentation states [2], and the six tables with a key have no
duplicate key; two stored names differ from the documentation, module_presentation_length for the run length and
"Withdrawn" for "Withdrawal", without changing any value. The click table differs in grain, the level of detail that
one row represents: documented as one student's interactions with a resource on a day [7], it holds several rows for
1,614,505 student-resource-days, so clicks are summed by enrolment and day before any use (DQ02). In addition, 787,170
rows (7.39%) repeat another row exactly, 3.19% of all clicks. If these rows were only separate visits that
happen to carry the same count, two rows of the same student, resource and day would carry equal counts as often as
chance gives from each resource's own counts, 24.0% of such pairs; they do so in 31.5%, more often for forums and
content pages and less often for quizzes. Some rows may therefore be copies made by the logging system and others
real repeated visits, and the data cannot tell which, so every row is kept and a de-duplicated twin of each click feature allows a sensitivity check (DQ01).

Joins need care too: a
direct join of submissions with click rows would return 89,347,197 rows, and an inner join, which keeps only rows
found in both tables, would drop the 3,365 enrolments without any click; tables are therefore summed to the enrolment
and joined to the enrolment table with left joins, which keep every enrolment (DQ17). Appendix I gives the full
evidence of this section.

===== reports/milestone-3/report/03-02-missingness-validity.md @ 19d35a4 =====
## 3.2. Missingness and Validity

Missing values are few, and their pattern shows where they come from. The deprivation band is blank for 1,111
enrolments (3.41%), concentrated in North Region and Ireland, and across all 32,593 enrolments these students pass, with or without
distinction, in 65.7% of cases against 46.6% of the others, so the blanks relate to the outcome and are kept as their own group rather than filled (DQ12);
45 registration days and 173 TMA scores are also missing (DQ13, DQ11). Over time, the share of blank
bands ranges from 0.13% to 5.89% between runs; whether gaps co-occur in the same record was not examined, because
the three gaps are few and sit in different tables. Three other gaps are structural rather than lost
values: an empty unregistration day marks a student who did not withdraw, a missing submission row a task not
submitted, and exam results are absent by design, so 18 of the 24 exams have no result row (DQ08) [2].

The validity checks found scores within 0 to 100 and no submission before registration, but six inconsistencies:
93 Withdrawn enrolments without an unregistration day, 87 of them in October 2014 runs (DQ04); 58 registrations after
the two-week sign-up window [2] (DQ05); 1,909 banked results dated −1 (DQ07); 98,745 clicks and 588 submissions
dated after the student unregistered (DQ03); 32,991 of the 69,956 CMA submissions after their due day, although the
OU's policy of 2025 accepts no late CMA [3] (DQ10); and one band label without its percent sign (DQ12). None is
corrected by changing a recorded value; each receives a flag or a rule in Section 5. Appendix I gives the full
evidence of this section.

===== reports/milestone-3/report/03-03-distributions-outcome.md @ 19d35a4 =====
## 3.3. Distributions, Outliers and Outcome Balance

Activity is strongly skewed: per enrolment the median is 602 clicks, 3,365 enrolments have none, 2,503 lie beyond the
upper fence of the interquartile range, the usual statistical boundary for an outlier, and a single click record, one student on one resource on one day, reaches
6,977 clicks. These are heavy users rather than errors, so no value is removed or capped, and models sensitive to
scale receive the logarithm of the counts instead (DQ16). Scores lean the other way, with a median of 80, and 45.8% of
CMA scores fall on a multiple of ten against 17.4% of TMA scores, a sign of coarse marking steps; study load reaches
655 credits against a 99th percentile of 240.

The two outcome classes are close in size. Of the 28,061 enrolments registered by day 14 and not unregistered by it,
the KPI population, 54.7% completed, a value of OULAD that is not the university's assumed baseline of
70%; non-completion reaches 45.3% among those enrolled at day 13 and 44.2% at day 27,
ranges from 24.9% to 58.3% between runs in the KPI population, and the smaller class holds at least 92 enrolments in every run, so no
resampling is needed. Figure 3.1 shows the final results of every run: withdrawal is highest in the CCC runs
(43–46%), while GGG has the fewest withdrawals but the most failures. Appendix I gives the full evidence of this
section.

![Figure 3.1. Final result of every enrolment, by module run](assets/figures/fig-3-1-outcomes.png)

===== reports/milestone-3/report/03-04-temporal-representativeness.md @ 19d35a4 =====
## 3.4. Temporal Coverage and Representativeness

The data cover the February and October runs of 2013 and 2014, with activity from about four weeks before the start
to week 39; weekly clicks per enrolled student peak in week 3, just after the first cut-off (Appendix I, Figure A.2),
and two days near the end of all six February 2014 runs carry no click at all, a logging gap treated as missing
(DQ15). The cut-offs sit early: a TMA or CMA falls due by day 13 in only 1 of the 22 runs and by day 27 in 16, so a
rule that counts missed tasks has nothing to count at the first cut-off in 21 runs (DQ18). For prediction on a later
run, 9 pairs of module and start month ran in both years, while CCC and the February runs of EEE and GGG ran only in
2014, and only withdrawals dated by a cut-off can be known at it [8].

Representativeness limits every claim. OULAD is a subset of OU students of 2013–2014, reduced by anonymisation, with
modules chosen partly because many students failed them [2]. The students learn at a distance, 70.4% are under 35
and 63.1% study 60 credits or fewer at once; women form 11.5% of EEE and 88.4% of BBB, and completion in the KPI population
ranges from 45.7% in CCC to 73.8% in AAA. Results therefore describe OULAD runs, groups are compared within module, and every result
must be checked on the university's own records before it informs decisions D1 to D3 (DQ19). Appendix I gives the
full evidence of this section.

===== reports/milestone-3/report/03-05-quality-issue-log.md @ 19d35a4 =====
## 3.5. Data Quality Issue Log

The findings of Sections 3.1 to 3.4 become nineteen issues, each with its evidence, its impact on the questions, a
severity and a decision, in the format of the brief's Data Quality Issue Log [1]. The severity is judged against the
questions: High marks an issue that would change a reported rate, the target or a feature at a cut-off if it were
ignored; Medium one that would change a measure by a known amount; and Low one that touches few records or a field
that no question uses. Table 3.1 gives all nineteen issues in order with their key evidence; Appendix I (Table A.4)
gives the evidence in full with the profile entry behind each number.

**Table 3.1. Data Quality Issue Log**

| ID | Variable / table | Evidence | Impact on AQ | Severity | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle: exact duplicate rows | 787,170 rows (7.39%); 3.19% of clicks | Click measures (AQ2, AQ3) | Medium | Keep every row; de-duplicated twin of each click feature for sensitivity |
| DQ02 | studentVle: grain | 1,614,505 student-resource-days with several rows | Counts and joins at row level | Medium | Sum clicks by enrolment and day before any join; count active days, not rows |
| DQ03 | Activity after unregistration | 98,745 clicks and 588 submissions after unregistering | Engagement up to withdrawal (AQ1, AQ2) | Medium | Truncate engagement at the unregistration day |
| DQ04 | final_result and unregistration day | 93 Withdrawn without a day; 9 Fail with one | Populations at each day; time to withdrawal | Low | Keep both as recorded; flag the 93 and the 9 |
| DQ05 | Registration after day 14 | 58 registered on days 16–167 | KPI denominator; populations at the cut-offs | Low | Enrolled at day d requires registration by day d (C09) |
| DQ06 | Departures before teaching | 3,097 unregistered by day 0; one on day 444 of a 268-day run | KPI denominator | Low | Not an error; outside the day-14 population; the day-444 record kept with a flag |
| DQ07 | Banked results | 1,909 dated −1 | Timing and missed-task measures (AQ1–AQ3) | Medium | Never timed; counted as banked results, known at registration |
| DQ08 | Exams | 18 of 24 exams without a result row | First missed task (AQ1); task signs (AQ2, AQ3) | High | Tasks are TMA and CMA only; exam scores not used |
| DQ09 | Weights | Coursework weight 0 in GGG; two exams in CCC 2014 | Weighted score features | Medium | No weighted grade; tasks counted unweighted |
| DQ10 | Late submissions | 32,991 of 69,956 CMA and 16,320 of 97,088 TMA late | Late-task signs (AQ1, AQ2, early-sign rule) | Medium | Lateness kept by task type; the rule uses TMA lateness (C10) |
| DQ11 | Scores | 173 TMA scores missing | Score features | Low | Score left missing; only marks known at the cut-off used |
| DQ12 | imd_band | 1,111 missing; 65.7% against 46.6% success | Fairness audit (AQ4); background features | Medium | Label corrected; "Missing" kept as its own group; no imputation |
| DQ13 | Registration day | 45 missing, 39 Withdrawn | Registration-lead feature | Low | Kept missing with an indicator |
| DQ14 | Planned weeks of resources | Missing for 82.4% of resources | None | Low | Not used |
| DQ15 | Days without any click | Days 218–219 of all February 2014 runs | Daily series after week 30 | Low | Treated as missing, not zero |
| DQ16 | Outliers in clicks and credits | 2,503 beyond the fence; 655 credits | Scale-sensitive methods | Low | Every value kept; logarithm in model matrices |
| DQ17 | Enrolments without activity | 3,365 without clicks; 6,750 without submissions | Inner joins would drop them | Medium | Left joins from the enrolment table; zero counts |
| DQ18 | Tasks due by the cut-offs | Task due by day 13 in 1 run, by day 27 in 16 | AQ3 comparison rule; secondary KPI 1 | High | Rule restated on the tasks actually due (C10) |
| DQ19 | Representativeness | Seven UK modules of 2013–2014 | Every claim; group comparisons | High | Scope stated; comparisons within module; results checked on the university's data |

Three issues are rated High. The missing exam results (DQ08) would count the exam as missed for every student of the
five modules without exam results if exams were counted as tasks, so only TMA and CMA count as tasks. The few tasks due by the cut-offs (DQ18) would leave the
early-sign rule silent in most runs, so the rule is restated (Section 4.1). The narrow population (DQ19) limits every
claim, so the scope is stated with each result.

===== reports/milestone-3/report/04-00-aq-data-fit.md @ 19d35a4 =====
# 4. AQ–Data Fit and Data Gap Decisions

After data understanding, the brief requires every question to be rated again against the real data,
because not every question of Milestone 1 should be kept unchanged when the data do not support it [1]. A question is
rated GREEN when the variables, population, time window and quality are enough to answer it at the level of claim it
makes; YELLOW when related data exist but scope, a secondary variable, granularity or quality falls short, so the
question must be narrowed, its claim changed or a compatible dataset added; and RED when a key concept, variable,
target or intervention is missing, so the question must be revised, dropped or deferred [1].

When the data do not meet a question, the brief sets an order of steps: (1) check the documentation and meaning of
the fields, in case the variable exists under another name or in another table; (2) derive the variable validly from
real fields, stating the formula and its assumptions; (3) add a compatible open dataset, but only if population, time,
granularity and join logic match; (4) narrow the scope, lower the claim or rewrite the question; and (5) defer or drop
the question if it is core but wholly unsupported [1]. Synthetic data are not a sixth step to rescue a question: they
may test code or illustrate a method, but they never replace evidence that the real data lack [1].

Section 4.1 rates the four questions and explains the changes that follow, and Section 4.2 records how each kind of
gap is handled, including the decision on synthetic data.

===== reports/milestone-3/report/04-01-fit-ratings.md @ 19d35a4 =====
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

===== reports/milestone-3/report/04-02-gap-decisions.md @ 19d35a4 =====
## 4.2. Data Gap Decisions and Synthetic Data

**Kinds of gap.** The brief separates three kinds of gap [1]. A missing value is a variable that exists but is empty
for some records, which can be analysed, kept as a category or imputed with a reason. A missing variable or concept is
something the dataset never collected, which must not be imputed or generated as if it were real; it calls for another
valid source or a revised question. A missing target means no outcome for supervised prediction. OULAD adds a fourth
case that looks like missing data but is not: a recorded absence, where a missing row itself records an event, such as
no click or no submission. Table 4.2 sorts the gaps of OULAD into these classes with the handling of each.

**Table 4.2. Missing values, recorded absences and missing variables**

| Class | Cases in OULAD | Evidence | Handling |
| :---- | :---- | :---- | :---- |
| Missing value | imd_band (1,111); registration day (45); TMA score (173); withdrawal day of 93 Withdrawn; due day of 11 exams | DQ04, DQ08, DQ11–DQ13 | "Missing" category for imd_band; indicators; no imputation in the prepared views; filling fitted on training runs only in model matrices; exams left out of task counts |
| Recorded absence | No click row; no submission row; empty unregistration day of students who stayed | DQ17; data descriptor | Zero counts after left joins; an empty unregistration day means the student did not withdraw |
| Missing variable | Year of study, delivery mode, attendance, leave or transfer status, contacts and their outcomes, staff capacity, the day a TMA mark was released | C04, C05, C08 | Not imputed or simulated; questions narrowed (AQ1–AQ3) or the contact part deferred (AQ4) |
| Missing target | None: final_result is present for every enrolment | Section 2.2 | Supervised target available |

**Adding another dataset.** The third step of the procedure, adding a compatible open dataset, does not close any
gap. None of the seven candidate datasets screened in Milestone 2 records contacts, attendance or year of study for
the same students, and joining a dataset of other students only because it shares a variable name is what the brief
rules out [1]. The questions were therefore narrowed and the contact part of AQ4 deferred, which is the brief's order
of priority [1].

**Synthetic data.** Of the five levels of synthetic data in the brief's policy, this project uses only level A, small
labelled test data for code [1]: a few hand-made test enrolments in the `tests/` folder of the Prepared Data Package
check that each feature formula gives the expected value. They never enter a prepared view, a statistic or a finding,
and no augmentation is planned; Appendix IV sets out the five levels and their conditions.

===== reports/milestone-3/report/05-00-preparation-plan.md @ 19d35a4 =====
# 5. Data Preparation Plan

Before any record was changed, each issue of the Data Quality Issue Log (Table 3.1) and each need of the questions
received a decision with its rationale, its implementation and the check that validates it, as the brief requires
[1]. The plan avoids the habits the brief names as wrong first moves: imputing every gap with a mean or zero without
analysis, dropping every duplicate without checking the grain, deleting every value outside the interquartile range,
merging rare categories at will, using future data to compute past features, and removing the sensitive attributes
that a bias audit needs [1].

Table 5.1 gives the Preparation Decision Matrix. It covers the eight needs of the brief's template, from missing values
to encoding and scaling, and four further needs of this project: the population of each table, activity after
withdrawal, the sensitive attributes and the split into training and test runs. The Validation column names the
checks V01 to V15 of the validation script, which Section 7 reports.

**Table 5.1. Preparation Decision Matrix**

| Issue / need | Decision | Rationale | Implementation | Validation |
| :---- | :---- | :---- | :---- | :---- |
| Population (C09) | Keep all 32,593 enrolments in the enrolment view with flags for days 13, 14 and 27; feature views hold only the enrolments enrolled at their cut-off | The KPI counts students enrolled after the add-drop period; a list can only name students enrolled on the day it is drawn | Enrolled at day d: registered by day d, or registration day unknown, and not unregistered by day d | V01: populations of 32,593, 28,061, 28,069 and 27,535 equal the profile |
| Missing values (DQ04, DQ11–DQ14) | imd_band "Missing" as its own category; registration day and withdrawal day left empty with an indicator; TMA score left empty; planned weeks not used | Missingness is informative (imd_band), small (45, 93, 173) or in an unused field; imputing would invent values the data do not hold | Indicators in the views; median filling of the registration lead only in the model matrices, fitted on training runs | V02: missing counts after equal those before; V12 |
| Duplicates and keys (DQ01, DQ02) | Keep every click row; sum clicks by enrolment and day, and by week, before any join; de-duplicated twin of each click feature | The cause of exact duplicates cannot be decided; a row is a logging record, not one student-day; the twin allows a sensitivity check | Daily aggregation with record count, clicks and de-duplicated clicks | V03: keys unique in every view; V04: click totals reconcile |
| Invalid category or type (DQ07, DQ12) | Label "10-20" corrected to "10-20%"; ordered categories for bands; banked results separated and never timed | Labels must sort and match; day −1 is a placeholder for a carried-over result, not a submission day | Standardisation step; status "banked" | V05: every category in its expected set; V06: no banked row in lateness or missed counts |
| Outliers (DQ10, DQ16) | Keep every value: 6,977-click record, 655 credits, submissions up to day 608 | Heavy users, students on many modules and very late submissions are real; capping would change real totals | No deletion; logarithm of counts only in the model matrices | V07: ranges after equal those before |
| Activity after withdrawal (DQ03) | Truncate engagement measures at the unregistration day | Activity after leaving is not engagement while enrolled and would blur AQ1 and AQ2 | Filter by day in the enrolment, task and week views | V08: no click or submission counted after the unregistration day |
| Table integration (DQ02, DQ17) | Left joins from the enrolment table after summing each table to the target grain; zero counts for no activity | Inner joins would drop 3,365 enrolments; a direct join of submissions and clicks returns 89 million rows | Row count asserted after every join | V09: rows equal the left table after each of 25 joins; V10: enrolments without activity kept with zero |
| Derived features (DQ08, DQ09, DQ18) | Task counts over TMA and CMA only, unweighted; lateness from due and submission days; CMA marks known by the cut-off; early-sign rule of C10; activity relative to the run's median | No exam results in five modules; weights differ by module; TMA marks have no release day; the rule must fire in every run | Formulas of Table 6.1; target-derived flags kept out of feature views | V11: six features recomputed from raw by separate code; unit tests for every formula |
| Temporal aggregation | Weeks of seven days from day 0; cut-offs at day 13 and day 27; activity before day 0 as its own window | The prediction points are fixed in Milestone 2 (C02); activity before the start is known at the cut-off | Filter every event to on or before the cut-off | V13: a recount of the click features without the date filter changes them only for students who clicked after the cut-off, which shows the filter works; V11 and unit tests for task features |
| Encoding and scaling | Views keep original scales and labels; model matrices for linear models fitted on 2013 runs | A test run must never inform a parameter [1] | Ordinal codes with missing indicator, one-hot levels, logarithm, median filling and standardisation from training rows | V12: parameters unchanged when test rows are altered |
| Sensitive attributes | Gender, age band, disability, imd_band and region kept in every view as audit columns, outside both predictor sets | The fairness audit of AQ3 and AQ4 needs them; their use as predictors is a policy choice | Role "audit" in the data dictionary | V14: every column has a role; no audit column among the predictors |
| Split | Training on the 2013 runs, test on the 2014 runs; flags for paired runs and for test students seen in 2013 | The claim is prediction for a later run (C07) | Split flag at run level | V15: no run in both partitions; flags recomputed |

Three decisions shape the prepared data most. Nothing that was recorded is deleted or imputed in the prepared views,
so every count can be traced back to the raw files, and the model matrices alone hold filled and scaled values.
Every feature is built only from events dated on or before its cut-off, so no information from after the moment of
prediction reaches a model. And every parameter learned from the data, such as a median or a scale, comes from the
training runs alone, so the test runs remain an independent check. The full matrix, with the function of the
pipeline that carries out each decision, is `data/metadata/decision_matrix.md` in the Prepared Data Package.

===== reports/milestone-3/report/06-00-preparation-pipeline.md @ 19d35a4 =====
# 6. Data Preparation Pipeline

The pipeline turns the raw files into prepared views with scripts only, with no manual step, so that anyone can rerun
it and obtain the same data, as the brief requires [1]. It carries out the decisions of Table 5.1 in the ten steps
that the brief recommends, from loading the raw files to persisting the prepared data with their documentation [1].
Section 6.1 maps the steps to the code and describes the package; Section 6.2 covers the integration of the tables
and the construction of features; and Section 6.3 sets the split into training and test runs and the controls against
leakage.

===== reports/milestone-3/report/06-01-pipeline-steps.md @ 19d35a4 =====
## 6.1. Pipeline Steps and Package Structure

**Steps.** The ten steps are functions of one script, `src/prepare_data.py`, run in order; Appendix II (Table A.7)
gives each step with its function and its result. They check the raw tables against their checksums, select the
populations of Section 4.1, correct the 3,516 "10-20" band labels, sum the 10,655,280 click rows into 1,808,119
enrolment-day records, flag the uncertain records, leave out the 98,745 clicks after withdrawal, integrate 286,898
enrolment-task rows, build the features at both cut-offs and write six views and two model-ready matrices with their
documentation.

**Stages.** The preparation script is one of eight stages that a single command, `bash src/run_all.sh`, runs in order,
from linking and checking the raw files to the validation of Section 7 and the two notebooks that show the work
(Appendix II, Table A.8). Each stage writes its console output, its command, its time in
Coordinated Universal Time (UTC) and its exit status to a log file, and the run stops at the first failed stage. The
whole run takes about 20 seconds, as the time stamps of its logs show. Run twice from the raw files, it wrote byte-identical outputs in all eight data files,
and every join kept exactly its input rows.

**Package structure.** The package follows the folder layout that the brief recommends, with immutable raw files,
intermediate and processed data, metadata, notebooks and scripts kept apart [1]; Appendix II describes the layout,
the stages, the transformation log and every prepared file.

===== reports/milestone-3/report/06-02-integration-features.md @ 19d35a4 =====
## 6.2. Integration and Feature Construction

**Integration.** Integration starts from the enrolment table, which holds one row for each of the 32,593 enrolments,
and adds every other table through left joins after summing it to the enrolment, so that no enrolment is lost and no
row is multiplied. Each join is checked: the pipeline asserts that the number of rows after the join equals the
number before it, and all 25 joins kept their input rows. Clicks are summed by enrolment and day, then by week, as
the OU itself summarises clicks by week and by type of content for its early-warning work [9].

**Timing rule.** Every feature uses only records dated on or before its cut-off. A legitimate model may only build on
information that existed before its target was known, and records that are updated later without a time stamp are a
common route for information from the future to reach a model [10]. Activity before day 0 is kept as its own window,
because it is known before teaching starts. Features that need a mark use only CMA marks, for submissions made at
least seven days before the cut-off, since a CMA score is expected within seven days [3], a rule of 2025 assumed to hold for 2013–2014, while a TMA mark has no
release day in the data.

**Derived variables.** Table 6.1 defines the main derived variables with their formula, source fields and timing rule;
c stands for the cut-off day, 13 or 27.

**Table 6.1. Main derived variables**

| Variable | Formula | Source fields | Window / timing rule |
| :---- | :---- | :---- | :---- |
| non_completion (target) | final_result is Fail or Withdrawn | studentInfo | Observed at the run end; never a feature |
| enrolled_d13, enrolled_d14, enrolled_d27 | Registered by day d, or registration day unknown, and not unregistered by day d | studentRegistration | Day d (C09) |
| clicks_pre | Clicks before day 0 | studentVle | Before the start |
| clicks_0c, active_days_0c | Clicks, and days with at least one click, from day 0 to c | studentVle | Days 0 to c |
| activity_ratio_run | (clicks_0c + 1) ÷ (median clicks_0c of the run's enrolled students + 1) | studentVle | Same run, days 0 to c; no outcome used |
| inactive_last7 | No click on days c − 6 to c | studentVle | Seven days ending at c |
| tasks_missed_c | TMA or CMA due by c, due on or after the registration day, not submitted by c | assessments, studentAssessment | Submissions up to c; banked results excluded |
| tma_late_c, cma_late_c | Tasks due by c submitted after the due day but by c, by type | assessments, studentAssessment | Submissions up to c |
| cma_score_mean_c | Mean score of CMAs submitted by c − 7; empty if none | studentAssessment | Marks known by c; prepared, not a predictor (Section 7.3) |
| early_sign_rule | A task missed, or a TMA late, or inactive in the last seven days | derived | At c (C10) |
| early_sign_rule_cma | early_sign_rule, or a CMA late | derived | At c; sensitivity variant |
| first_missed_week | Week of the earliest task not submitted that fell due while the student was enrolled | assessment_due view | Whole run (AQ1 only) |

A task counts as missed only if it fell due on or after the student's registration day, and the activity ratio
compares a student with the median of the same run up to the same day, without any outcome. The feature views hold 20
primary and 10 extended predictors plus the weekly click counts; every other column is an identifier, the target, a
flag for evaluation, the rule or an audit attribute, and demographic attributes serve mainly the fairness audit,
because adding them to activity and assessment data did not significantly improve the prediction of students at risk
at the OU [9]. Appendix III explains these choices and lists the predictor sets.

===== reports/milestone-3/report/06-03-split-leakage.md @ 19d35a4 =====
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

===== reports/milestone-3/report/07-00-prepared-validation.md @ 19d35a4 =====
# 7. Prepared Data Validation

The brief asks us to show that the prepared data serve the analysis better while staying correct and
traceable: row, entity and outcome counts compared before and after preparation, missingness, keys, joins, ranges and
time order checked again, derived features checked against their formulas and by hand, no leakage against the
prediction point, an updated data dictionary and a recorded version [1]. The validation script,
`src/validate_prepared.py`, runs 22 checks under fifteen identifiers, V01 to V15, against the raw files and the
profile, and all 22 pass; each check states its expected and observed value (Appendix VI). Section 7.1 reports the
comparisons, Section 7.2 the lineage, dictionary and version, and Section 7.3 the risks that remain in the data on
purpose.

===== reports/milestone-3/report/07-01-before-after.md @ 19d35a4 =====
## 7.1. Before-and-After Checks

Preparation changes no outcome and no count without an explicit rule. Table 7.1 shows each comparison that the brief
asks for, with the value in the raw data, the value in the prepared data and the result.

**Table 7.1. Before-and-after checks**

| Check | Before (raw) | After (prepared) | Status |
| :---- | :---- | :---- | :---- |
| Enrolments, students, outcome mix (V01) | 32,593 enrolments; 28,785 students; 12,361 Pass, 10,156 Withdrawn, 7,052 Fail, 3,024 Distinction | Identical; no row dropped | PASS |
| Populations (V01, C09) | 32,593 enrolments | 28,061 at day 14; 28,069 at day 13; 27,535 at day 27, equal to the profile | PASS |
| Non-completion in the feature views (V01) | 12,708 at day 13; 12,156 at day 27 in the profile | Identical | PASS |
| Clicks (V04) | 39,605,099 | 39,506,354 kept plus 98,745 after withdrawal; weekly view sums to the same total | PASS |
| Missing values (V02) | imd_band 1,111; registration day 45; score 173 | Identical, not imputed | PASS |
| Keys (V03) | Unique in the six keyed tables | Unique in every prepared view | PASS |
| Categories and ranges (V05, V07) | Score 0–100; credits 30–655 | Same ranges; every label in its expected set | PASS |
| Time order (V08) | Activity after withdrawal present | No week counted after the withdrawal week | PASS |
| Joins (V09, V10) | – | 25 joins, rows in equal rows out; 3,554 enrolments without a click row kept with zero | PASS |
| Derived features (V11) | – | 6 features (clicks before and after day 0, active days, resources, missed and late tasks) recomputed from raw by separate code for all 55,604 feature rows: 0 differences | PASS |
| Leakage (V13) | – | A recount of the click features without the date filter changes them only for the 26,755 (day 13) and 25,663 (day 27) enrolments that clicked after the cut-off, so the filter works; no target-derived column in a view | PASS |
| Fitted transforms (V12) | – | Parameters identical with test rows altered | PASS |
| Documentation and split (V14, V15) | – | Every column documented with a role; 9 training and 13 test runs, none in both | PASS |

The number of enrolments without a click rises from 3,365 to 3,554 because the 189 students whose only clicks came
after they unregistered now show none, and the leakage check is built so that it would fail if any feature used a
later click. Beyond the recount of every feature row, nine unit tests on synthetic test enrolments confirm each formula,
and one row recounted by hand from the raw files matches the prepared view; Appendix VI explains these checks in full.

===== reports/milestone-3/report/07-02-lineage-dictionary.md @ 19d35a4 =====
## 7.2. Lineage, Dictionary and Version

**Dictionary.** Every prepared column is documented with its source field, its transformation, its data type, its role
and its sensitivity, as the brief requires [1]. The role says how a column may be used: identifier, target, predictor,
audit attribute, evaluation flag or descriptive measure. Validation fails if a column lacks an entry or if a predictor
list holds an audit, target or descriptive column (V14), so the documentation cannot drift from the data.

**Lineage.** The lineage table of the brief traces each prepared variable to its source file and field, with its
transformation, its window or filter, its purpose and its sensitivity [1]. Table 7.2 shows it for the variables that
carry the questions; the full table, with one row for each of the 88 prepared variables and the sensitive variables
marked in its purpose column, is Table A.12 in Appendix III.

**Table 7.2. Data lineage of the main prepared variables**

| Prepared variable | Source file / field | Transformation | Window / filter | Purpose / AQ | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| non_completion | studentInfo.final_result | Fail or Withdrawn | observed at the run end | AQ1–AQ3 target | none |
| enrolled_d14 | studentRegistration, registration days | enrolled at day 14 | day 14 | primary KPI denominator (C09) | none |
| clicks_0c | studentVle.sum_click, date | sum | days 0 to c | AQ2–AQ3 | none |
| tasks_missed_c | studentAssessment | due by c, no non-banked submission by c | submissions up to c | AQ2–AQ3; part of the rule | none |
| early_sign_rule | derived | missed task, late TMA or inactive | at c | AQ3 comparison rule; secondary KPI 1 (C10) | none |
| imd_band | studentInfo.imd_band | "10-20" → "10-20%"; missing → "Missing" | – | AQ4 fairness audit (C04) | sensitive |

**Version.** The version manifest names the prepared dataset OULAD-N04-prepared-1.0 and records the SHA-256 checksum
of every raw file, script and prepared file, the row counts of every view, the repository commit, the Python (3.12.7)
and polars (2.1.0) versions and the creation time in UTC. A reader can therefore tell which raw data and which code
produced a given prepared file, and the rerun check of Section 6.1 shows that the same inputs give the same outputs.

===== reports/milestone-3/report/07-03-residual-risks.md @ 19d35a4 =====
## 7.3. Residual Risks

Five issues remain in the prepared data on purpose, because resolving them needs information that OULAD does not
hold. The first three are flagged in the data with their size measured, so that Milestone 4 can report results with
and without them; the last two are limits of the KPI and of the capacity scenarios, stated with their effect.

(1) **Duplicate click rows.** The exact duplicate rows may be copies made by the logging system or repeated visits.
The de-duplicated twins of the click features bound their effect: they would remove 3.19% of all clicks.

(2) **Late CMAs and CMA marks.** The meaning of a late CMA in 2013–2014 is not documented, and the OU marking policy
on record dates from 2025 [3]. The early-sign rule therefore uses TMA lateness, and a variant that adds CMA lateness
is kept for comparison; with CMA lateness, the rule would flag 41.2% of enrolments at day 27 instead of 28.8%. CMA
marks known by the cut-off exist for only 1.4% of training rows at day 13 and 5.2% at day 27, below the 10% coverage
that we require before the CMA score enters the predictor set of Milestone 4, so the score is prepared but not
used.

(3) **Uncertain records.** 93 Withdrawn enrolments have no withdrawal day, and 1,962 test enrolments belong to students
seen in 2013. Both groups are flagged, so that test results can be reported with and without them.

(4) **The KPI is a proxy.** Completion of a module run stands for completion of a course, and leave or transfer cannot
be told apart from withdrawal in OULAD. The effect of the uncertain records on the KPI is small: without the 138
enrolments flagged for an unknown withdrawal day (93) or registration day (45), completion at day 14 is 54.9% instead
of 54.7%.

(5) **Assumed capacity.** The OU splits each module into tutor groups of a few tens of students [9], and the capacity
scenarios assume that one lecturer-advisor's caseload is one such group of 20 students. Each list then holds three or
five students per group, the weekly range that Milestone 1 sets for a lecturer-advisor, for the week after its review
point; for the support office, the scenarios use 30 or 40 students per run at each review point, the weekly range that Milestone 1 sets for
that office. The real caseload at the university may differ, so list sizes are scenarios,
not plans.

===== reports/milestone-3/report/08-00-readiness.md @ 19d35a4 =====
# 8. Analytics and Model Readiness

A project may need several analytic-ready views rather than one table, each with the structure that one level of
questions needs [1]. Section 8.1 maps the prepared views to the four analytics levels, and Section 8.2 rates each
question's readiness for Milestone 4 and names the questions that the data cannot yet answer.

The updated traceability that the brief asks for runs from the goal and the KPIs through each question, its analytics
type, its raw variables, its preparation and its prepared variables to the decision it supports [1]; it is Table A.13
in Appendix IV. Along that chain, the primary KPI and AQ1 rest on the enrolment and task views and serve D2 and D3;
AQ2 rests on the signs at day 27 and serves D2 and the reasons shown with each name in D1; AQ3 rests on both feature
views and the time split and serves D1; and AQ4 rests on the capacity table and the audit columns and serves D1, with
the choice of contact and the follow-up rate of secondary KPI 2 left to the pilot rather than filled with assumptions.

===== reports/milestone-3/report/08-01-views-by-level.md @ 19d35a4 =====
## 8.1. Prepared Views by Analytics Level

Each analytics level has its own prepared view, and each view adds to the one before it. The brief sets a check for
each level before Milestone 4: descriptive views must give summaries without double counting or join bias;
diagnostic views must compute associations from real data with comparison groups; predictive views must hold a
target, a prediction point, features from before that point, a split and enough cases of each class; and prescriptive
views need data on actions, constraints, costs and outcomes [1]. Appendix III (Table A.11) gives, for each level, the
prepared view, its population and grain, the check of the brief and its result; the paragraphs below state them.

The descriptive views, enrolment, assessment_due and student_week, give rates on the right denominator, because
every enrolment appears once and the populations of Section 4.1 are flags rather than filters; their keys are unique,
every join kept its rows and their clicks reconcile with the raw log. The diagnostic view, features_d27 with the
enrolment view, adds the signs at day 27 for the 27,535 enrolments enrolled then, so that their association with
non-completion can be compared within each of the seven modules. The predictive views, features_d13, features_d27
and the model-ready matrices, add a second cut-off at day 13, the time split into 9 training and 13 test runs and
transforms fitted on the training runs, with at least 92 enrolments in the smaller class of every run. The prescriptive table, capacity_by_run, supplies
only list sizes under assumed capacities, because the data hold no action, no cost and no outcome after a contact,
and the brief rules out turning a predictive result into a prescriptive one by advice [1].

===== reports/milestone-3/report/08-02-readiness-matrix.md @ 19d35a4 =====
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

===== reports/milestone-3/report/09-00-ethics-limitations.md @ 19d35a4 =====
# 9. Ethics, Bias and Limitations

**Sensitive attributes kept for audit.** The prepared data keep gender, age band, declared disability, deprivation
band and region in every view, outside both predictor sets, because a fairness audit needs them. Algorithmic
bias in education is a model that performs substantially better or worse for one group of students than for another;
it can arise through proxies even when no demographic attribute is an input, and a dataset without group membership
cannot be audited at all [14]. Removing the attributes would therefore hide bias rather than prevent it. The brief
likewise allows sensitive attributes to be kept for auditing while restricting their use as predictors [1]. Highest
education, the sixth attribute listed in Section 2.3, is a predictor, because prior qualifications describe a student's
preparation for the module; it stays in every view, so its groups can be audited as well. Whether the five audit
attributes should also be predictors is a policy choice, which Milestone 4 examines by comparing models with and
without them.

**What earlier work on OULAD shows.** A study of fairness on OULAD found students with a declared disability strongly
under-represented, a disparate impact of five to six percentage points in favour of male students, reproduced by
most models, little
gain in fairness from leaving the attributes out, and disabled students in some cases predicted to fail with a higher
probability [15]. The audit of this project is designed with these findings in mind. The audit groups have known
sizes, 3,164 enrolments with a declared disability and 216 aged 55 or over, so small groups are audited across runs
rather than run by run. The "Missing" deprivation group is reported on its own, because its students succeed more
often (Section 3.2), and merging it into a band would distort that band's rate.

**Privacy.** Privacy rules apply at two levels. OULAD was anonymised with k-anonymity, k = 5, meaning that every
combination of the attributes that could identify a student is shared by at least five students [2]. Under Vietnam's Personal Data
Protection Law No. 91/2025/QH15, de-identified data fall outside the definition of personal data, and re-identifying
them is prohibited [16], so OULAD is never linked to any other source. For the pilot on the university's own records,
the rules are stricter: health information, such as a declared disability, is an example of sensitive personal data
[17], processing must keep to a specific purpose [17], and the law names no general exemption from consent for
research [16], so the pilot needs its own legal basis before any student record is prepared.

**Limits of the claims.** Four limits follow from the data. Results describe UK distance-learning modules of 2013–2014
and must be checked on the university's records before they inform a decision. The associations of AQ2 are not
causes: a sign that goes with non-completion may be a symptom of the same difficulty rather than its source. No
effect of contacting a student can be drawn from OULAD, because it records no contact. And deprivation bands are not
pooled across the nations of the UK, since each nation uses its own index [6].

===== reports/milestone-3/report/10-00-genai-reflection.md @ 19d35a4 =====
# 10. Generative AI Usage and Reflection

**Roles.** Generative artificial intelligence (AI) supported this milestone in all seven roles that the brief allows,
and every finding about the data was confirmed by code, statistics, documentation or a direct check on the dataset, as
the brief requires [1]. AI was never treated as a source of data: no AI answer served as evidence that a dataset holds
a number of records, that students tend to behave in some way or that one variable causes another [1]. AI agents
worked on both sides of each review, as critic and as the drafter whose work was criticised, and members of our team
verified the decisions. The seven roles were data dictionary interpreter, exploratory data analysis (EDA) and quality checklist partner, code assistant, preparation
critic, feature engineering ideator, documentation assistant and synthetic-data assistant; Appendix V describes what AI
did in each role and how the result was verified. Table 10.1 gives the main entries of the AI Decision Log in the
brief's format: the suggestion, our decision, whether it was accepted, the evidence used to verify it and its
effect on the pipeline [1].

**Table 10.1. AI Decision Log, main entries**

| AI suggestion | Team decision | Accepted / Rejected | Evidence used to verify | Effect on pipeline |
| :---- | :---- | :---- | :---- | :---- |
| A CMA score appears within 7 days and a CMA cannot be submitted late (OU policy of 2025) | Use the 7-day lag for CMA scores; do not apply the no-late rule to 2013–2014 | Accepted in part | 32,991 of 69,956 CMA submissions are after the due day | CMA scores only from submissions made at least 7 days before the cut-off; lateness counted by task type |
| Test whether exact duplicate click rows are copies | Run a chance test on two-row groups | Accepted | 31.5% equal counts against 24.0% by chance | All rows kept; de-duplicated twin built |
| A precision limit of 50% sits near the base rate; measure lift and attainable recall | Re-express the AQ4 limit (C13) | Accepted | 45.3% and 44.2% non-completion at the cut-offs | Capacity view; list quality as lift and recall |
| CMA lateness of unclear meaning drives the rule | The rule uses TMA lateness; a CMA variant is kept | Accepted | 47.2% of CMA against 16.8% of TMA submissions late | early_sign_rule and early_sign_rule_cma (C10) |
| Report the outcome rate of test enrolments of students seen in 2013 before modelling | Report only their number now | Accepted in part | Looking at test outcomes while preparing breaks the independent test | 1,962 flagged; outcomes left to Milestone 4 |
| Tasks due before registration counted as missed; the leakage check could not fail | Correct the formula and the check | Accepted | 6 tasks at day 27; reading of the code | Missed only if due on or after registration; V13 can fail |

**Accepted and rejected suggestions.** The preparation critic raised 12 critiques, of which we accepted 9 and
3 in part, and the leakage auditor raised 8 findings, all accepted; the auditor found no use of data dated after a
cut-off. The reviews shaped four rules that the pipeline applies. The AQ4 list is judged by its gain over chance,
because a precision limit of 50% sits close to the base rate (C13). CMA lateness, seen in 47.2% of CMA submissions
against 16.8% of TMA submissions, stays out of the early-sign rule (C10). A task counts as missed only if it falls
due on or after the student's registration day, the auditor having pointed to six tasks at day 27 that fell due before
the student registered. And the leakage check is built so that it can fail, as the auditor required.

The fourth of the critic's twelve critiques was accepted only in part, because of a rule we keep. The critic asked for the outcome rate of the test enrolments of
students seen in 2013 to be reported before modelling. We report their number, 1,962, but not their outcomes, because looking
at test outcomes while preparing the data would make the test set part of the preparation, which the brief rules out
[1].

Appendix V gives the AI Decision Log with all thirteen entries, the prompts, every decision on the critiques and
findings, and a reflection on where the reviews helped most.

===== reports/milestone-3/report/11-references.md @ 19d35a4 =====
# References

The references are formatted in APA style (American Psychological Association, 7th edition) and numbered for in-text citation in the form [n], in order of first citation.

[1] MTH045 – The Science of Data Analytics. (2026). *Milestone P3: From understanding to preparation* [Course brief]. University of Science, VNU-HCM.

[2] Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, *4*, Article 170171. https://doi.org/10.1038/sdata.2017.171

[3] The Open University. (2025). *Tutor-Marked Assignment (TMA) and interactive Computer-Marked Assignment (iCMA) policy: Summary* [Policy summary, effective July 2025]. https://help.open.ac.uk/documents/policies/tma-icma-policy/files/402/TMA-and-iCMA-summary.pdf

[4] The Open University. (n.d.). *Get to know the OU*. Help Centre. Retrieved November 6, 2026, from https://help.open.ac.uk/get-to-know-the-ou

[5] Department for Communities and Local Government. (2015). *The English Indices of Deprivation 2015: Statistical release*. https://assets.publishing.service.gov.uk/media/5a7f42a940f0b6230268e6b3/English_Indices_of_Deprivation_2015_-_Statistical_Release.pdf

[6] Abel, G. A., Barclay, M. E., & Payne, R. A. (2016). Adjusted indices of multiple deprivation to enable comparisons within and between constituent countries of the UK including an illustration using mortality rates. *BMJ Open*, *6*(11), Article e012750. https://doi.org/10.1136/bmjopen-2016-012750

[7] OU Analyse. (n.d.). *Open University Learning Analytics dataset*. The Open University. Retrieved November 6, 2026, from https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/

[8] Howard, E. (2025). *ouladFormat R package: Preparing the Open University Learning Analytics Dataset for analysis* (arXiv:2501.08366v2) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2501.08366

[9] Hlosta, M., Herrmannova, D., Vachova, L., Kuzilek, J., Zdrahal, Z., & Wolff, A. (2018). *Modelling student online behaviour in a virtual learning environment* (arXiv:1811.06369). arXiv. https://doi.org/10.48550/arXiv.1811.06369

[10] Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM Transactions on Knowledge Discovery from Data*, *6*(4), Article 15. https://doi.org/10.1145/2382577.2382579

[11] scikit-learn developers. (n.d.). *Common pitfalls and recommended practices* (scikit-learn 1.9.1 documentation). Retrieved November 6, 2026, from https://scikit-learn.org/stable/common_pitfalls.html

[12] Knowledge Media Institute, The Open University. (n.d.). *OU Analyse: Project full details* [Project page]. Retrieved November 6, 2026, from https://kmi.open.ac.uk/projects/name/ou-analyse

[13] scikit-learn developers. (n.d.). *Cross-validation: Evaluating estimator performance* (scikit-learn 1.9.1 documentation). Retrieved November 6, 2026, from https://scikit-learn.org/stable/modules/cross_validation.html

[14] Baker, R. S., & Hawn, A. (2022). Algorithmic bias in education. *International Journal of Artificial Intelligence in Education*, *32*(4), 1052–1092. https://doi.org/10.1007/s40593-021-00285-9

[15] Riazy, S., Simbeck, K., & Schreck, V. (2020). Fairness in learning analytics: Student at-risk prediction in virtual learning environments. In *Proceedings of the 12th International Conference on Computer Supported Education (CSEDU 2020)* (Vol. 1, pp. 15–25). SCITEPRESS. https://doi.org/10.5220/0009324100150025

[16] Quốc hội. (2025). *Luật Bảo vệ dữ liệu cá nhân* (Luật số 91/2025/QH15) [Law on Personal Data Protection]. Công báo, số 971+972, 24/7/2025. https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf

[17] Tài liệu quán triệt nội dung cơ bản của Luật Bảo vệ dữ liệu cá nhân [Briefing document on Law No. 91/2025/QH15]. (n.d.). Trường Đại học Tiền Giang. https://www.tgu.edu.vn/upload/files/Tailieu-gioithieu-LuatBaovedulieucanhan.pdf

===== reports/milestone-3/report/12-00-appendices.md @ 19d35a4 =====
# Appendices

The appendices hold the evidence behind the main text: the full profiling and quality results (Appendix I), the pipeline and the Prepared Data Package (Appendix II), the data dictionary and lineage (Appendix III), the updated traceability and Controlled Change Log (Appendix IV), the AI Decision Log with its prompts (Appendix V) and the validation ledger (Appendix VI). Each table is generated from the file named with it, so it matches the package exactly.

===== reports/milestone-3/report/12-01-profiling-details.md @ 19d35a4 =====
## Appendix I – Data Understanding, Profiling and Quality Details

Figure A.1 shows the seven OULAD tables with their row counts and the keys that link them; each link was checked on the data (`understanding.json`).

![Figure A.1. Tables, row counts and keys of OULAD](assets/figures/fig-2-1-tables.png)

Figure A.2 shows weekly clicks per enrolled student by start month, with the two cut-offs at the end of weeks 2 and 4 (`fig_weekly_activity.csv`).

![Figure A.2. Weekly clicks per enrolled student by start month, with the two cut-offs](assets/figures/fig-3-2-weekly.png)

The inputs required by the brief, checked before preparation began, are listed in Table A.1 with their status.

**Table A.1. Inputs from Milestone 2 and their status**

| Input (brief) | Content in this project | Status |
| :---- | :---- | :---- |
| Milestone 1 baseline | Business Goal, SMART Goal, KPIs, AQ1–AQ4, analytics types and decisions, frozen with a SHA-256 checksum of each file; all 8 source files unchanged | Complete |
| Updated traceability matrix | KPI → AQ → data requirement → file → actual variables → coverage → decision | Complete |
| Raw data package | Seven CSV tables of OULAD, figshare version 1, DOI 10.6084/m9.figshare.5081998.v1, each matching its pinned SHA-256 | Complete, 7 of 7 match |
| Metadata and data dictionary | Column definitions from the data descriptor, license CC BY 4.0, citation | Complete |
| Collection evidence | Web address, DOI, access date 6 November 2026 (UTC+7), version, checksums, collection log | Complete |
| Controlled Change Log | C01–C08 with old and new content and data evidence | Complete |

Table A.2 sets out what each day field and measure of OULAD means and when it becomes known; the meanings come from the data descriptor and the OU's assessment policy, the counts from `understanding.json`.

**Table A.2. Meaning and timing of the key fields**

| Field | Meaning | Unit and scale | Known at |
| :---- | :---- | :---- | :---- |
| date_registration, date_unregistration | Days the student registered and unregistered; empty unregistration = did not withdraw | days from the start | the day itself |
| assessments.date | Cut-off (due) day of the assessment | days | from the start of the run |
| date_submitted | Day the student submitted; all 1,909 banked results carry −1, a placeholder | days | the day itself |
| is_banked | Result carried over from an earlier run | 0/1 | registration |
| score | Mark, 0–100; below 40 is a fail | points | TMA: tutor marking, usually within ten working days of the cut-off; CMA: automatic, within 7 days |
| weight | Share of the grade; exams 100, other assessments together 100 | % | from the start |
| sum_click | Number of interactions with one resource on one day | count | the day itself |
| studied_credits | Credits of all modules studied at the same time; 60 a year is part-time, 120 full-time | credits | registration |

Table A.3 lists the six sensitive attributes with their codes, smallest group and the number of module-run groups with fewer than 20 students.

**Table A.3. Sensitive attributes**

| Attribute | Codes | Smallest group | Run groups below 20 | Nature |
| :---- | :---- | :---- | :---- | :---- |
| gender | F, M | F: 14,718 | 0 | Personal |
| age_band | 0-35, 35-55, 55<= | 55<=: 216 | 18 | Personal |
| disability | Y, N (declared) | Y: 3,164 | 1 | Health-related |
| imd_band | ten deciles, blank | blank: 1,111 | 11 | Socio-economic, area-level |
| region | 13 regions | Ireland: 1,184 | 11 | Location |
| highest_education | five levels | Postgraduate: 313 | 29 | Socio-economic |

The Data Quality Issue Log in Table A.4 gives the full evidence of every issue of Table 3.1; P. refers to sections of `data/metadata/profile.json` and U. to `understanding.json`.

**Table A.4. Data Quality Issue Log with evidence**

| ID | Variable / table | Evidence | Impact on AQ | Severity | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle: exact duplicate rows | 787,170 rows (7.39%) repeat another row in every column; 3.82–11.73% per run; 69.8% of duplicated groups are single-click; collapsing them removes 3.19% of clicks (P.duplicates). In two-row student-site-day groups, 31.5% have equal counts against 24.0% expected by chance from each site's own counts (Table A.6) | Click measures of AQ2 and AQ3 | Medium | Cause not decidable from the data: keep every row in the primary click measures (the table's record grain) and build a de-duplicated variant of each click feature for sensitivity |
| DQ02 | studentVle: grain differs from the documentation | 1,614,505 student-site-day groups hold several rows (3,810,465 rows), 1,179,074 of them with different click counts; up to 10 rows in one group (P.shape) | Any join or count at row level would mistake records for days | Medium | Aggregate clicks to enrolment × day and enrolment × week before any join; count active days, not rows |
| DQ03 | studentVle, studentAssessment: activity after unregistration | 29,440 click rows (98,745 clicks) by 1,279 enrolments, up to 423 days after unregistering; 588 non-banked submissions by 411 enrolments (P.validity) | Engagement up to withdrawal (AQ1, AQ2); none at a cut-off for students still registered | Medium | Truncate engagement measures at the unregistration day; feature views contain only students still registered at the cut-off, so no post-withdrawal event enters them |
| DQ04 | final_result × date_unregistration | 93 Withdrawn enrolments without an unregistration day, 87 of them in October 2014 runs; 9 Fail enrolments with one, 8 of them on or before day 0 (U.outcome, P.validity) | Populations at day 14, 13 and 27; time to withdrawal | Low | Keep final_result as the outcome; keep the recorded day; flag both groups (`withdrawal_day_missing`, `unregistered_not_withdrawn`); the 93 stay in every population because no record shows them leaving before a cut-off, and an evaluation flag lets test metrics be reported with and without them |
| DQ05 | studentRegistration: registration after day 14 | 58 enrolments registered on days 16–167, after the two-week sign-up window of the descriptor; 16 of them later unregistered (P.validity) | KPI denominator and populations at cut-offs | Low | Define "enrolled at day d" as registered by day d (or registration day unknown) and not unregistered by day d; late registrants enter only the populations of later days |
| DQ06 | studentRegistration: departures before teaching | 3,097 enrolments unregistered on or before day 0; one unregistration on day 444 of a 268-day run (U.outcome) | KPI denominator | Low | Not an error: these students left before the run began and are outside the day-14 KPI population; the day-444 record is kept with a flag |
| DQ07 | studentAssessment: banked results | All 1,909 banked results carry date_submitted = −1, a placeholder for a result carried over from an earlier run (P.validity) | Timeliness and missed-task measures (AQ1–AQ3) | Medium | Exclude banked rows from submission timing, lateness and missed-task counts; keep a per-enrolment count of banked results, known at registration |
| DQ08 | assessments, studentAssessment: exams | 18 of 24 exams have no result rows (scores only for CCC 2 and DDD 4); 11 exams have no due day (P.missing, U.time) | "First missed assessed task" (AQ1); task signs (AQ2, AQ3) | High (exams) | Count missed and late tasks over TMA and CMA only; the outcome stays final_result; exam scores are not used |
| DQ09 | assessments: weights | Coursework weights sum to 0 in the three GGG runs and to 100 elsewhere; FFF CMAs weigh 0; CCC 2014 runs hold two exams (total 200) (P.validity, U.measurement) | Weighted score features | Medium | Build no weighted grade; count tasks unweighted (formative tasks are still due) and keep weight as a column |
| DQ10 | studentAssessment: late and post-run submissions | 49,318 of 169,138 non-banked submissions with a due day are late (29.2%; median 3, 99th percentile 29 days): 16,320 of 97,088 TMA and 32,991 of 69,956 CMA, although the OU's current (2025) policy accepts no CMA after its cut-off day; 85 fall after the run ended, up to day 608 (P.validity) | Late-task signs (AQ1, AQ2, early-sign rule) | Medium | Keep every submission; lateness = date_submitted − due day, counted separately for TMA and CMA because the meaning of a late CMA in 2013–2014 is not documented; post-run submissions fall after both cut-offs |
| DQ11 | studentAssessment.score | 173 missing scores, all TMA (P.missing); 45.8% of CMA scores are multiples of 10 against 17.4% of TMA (P.distribution) | Score features | Low | Keep the submission, leave the score missing; scores enter features only where the mark is known at the cut-off (decision matrix, row "Derived feature") |
| DQ12 | studentInfo.imd_band | 1,111 missing (3.41%), 40.1% of North Region and 22.5% of Ireland; success 65.7% when missing against 46.6% when present, so not missing at random; one label "10-20" lacks the % sign (P.missing, P.validity) | AQ4 fairness check by deprivation; background features | Medium | Normalise the label to "10-20%"; keep missing as its own category "Missing"; no imputation |
| DQ13 | studentRegistration.date_registration | 45 missing, 39 of them Withdrawn (P.missing) | Registration-lead feature | Low | Keep null with an indicator; any filling is fitted on the training runs only |
| DQ14 | vle.week_from, week_to | 82.4% missing; filled for 1,121 of 6,364 sites (P.missing, U.time) | None | Low | Not used |
| DQ15 | studentVle: days without any click | In all six February 2014 runs two consecutive days carry no click (days 218–219; days 211–212 in BBB) (P.temporal) | Daily activity series after week 30 | Low | Treat the two days as missing, not as zero activity, in daily series; both lie after the cut-offs |
| DQ16 | Outliers: clicks and credits | One row of 6,977 clicks; clicks per enrolment skewness 3.03, 2,503 enrolments beyond the upper interquartile-range fence; studied_credits up to 655 against a 99th percentile of 240 (P.distribution) | Scale-sensitive methods | Low | Keep every value (heavy users and students on several modules are real); log or rank transforms are applied in modelling, fitted on training runs |
| DQ17 | Enrolments without any activity or submission row | 3,365 enrolments without a click row (2,988 Withdrawn; 2,390 left by day 0); 6,750 without a submission (P.missing) | Counts would drop these students under an inner join | Medium | Absence of a row records no activity (descriptor: no submission, no result row): fill counts with 0 after left joins from the enrolment table |
| DQ18 | assessments: tasks due by the cut-offs | A non-exam task is due by day 13 in 1 of 22 runs and by day 27 in 16; two or more are due by day 27 in 1 run only (P.temporal) | AQ3 comparison rule and secondary KPI 1: the Milestone 1 rule ("two or more tasks missed or late by week 4") can fire in 1 run of 22, and its OULAD form of one task (C06) in 16 runs at day 27 and 1 at day 13 | High | Task 3 decision (AQ–Data fit): rule restated on the tasks actually due (Change Log C10) |
| DQ19 | Population and module mix | Seven UK distance-learning modules of 2013–2014, selected partly for many failing students; women 11.5% of EEE and 88.4% of BBB; completion in the day-14 population from 45.7% (CCC) to 73.8% (AAA) (P.representativeness) | Generalisation of every AQ; group comparisons | High (claims) | State the scope; compare groups within module; results describe OULAD and are re-checked on the university's data before decisions D1–D3 |

Thirteen figures of the profile were recounted by an independent exploration of the same files with separate code (`profile_crosscheck.csv`); Table A.5 shows the 13 measures compared, all equal.

**Table A.5. Cross-check with an independent recount**

| Measure | Independent recount | Milestone 3 profile | Equal |
| :---- | :---- | :---- | :---- |
| studentVle exact duplicate rows | 787,170 | 787,170 | yes |
| clicks raw | 39,605,099 | 39,605,099 | yes |
| clicks after collapsing duplicates | 38,343,063 | 38,343,063 | yes |
| repeated student-site-day groups | 1,614,505 | 1,614,505 | yes |
| rows in repeated groups | 3,810,465 | 3,810,465 | yes |
| enrolments without activity | 3,365 | 3,365 | yes |
| enrolments without submission | 6,750 | 6,750 | yes |
| late submissions | 49,318 | 49,318 | yes |
| submissions after run end | 85 | 85 | yes |
| click rows after unregistration | 29,440 | 29,440 | yes |
| enrolments with clicks after unregistration | 1,279 | 1,279 | yes |
| submissions after unregistration (incl. 13 banked rows dated day -1) | 601 | 601 | yes |
| click rows before day 0 | 688,988 | 688,988 | yes |

The chance test of duplicate click rows compares, in the 1,311,841 student-resource-day groups with exactly two rows, the share with equal click counts (31.5%) with the share expected by chance from each resource's own counts (24.0%) or from each activity type's counts (21.7%). Table A.6 gives the observed share for the six activity types with the most such groups.

**Table A.6. Equal counts in two-row groups by activity type**

| Activity type | Two-row groups | Equal counts observed |
| :---- | :---- | :---- |
| forumng | 895,551 | 32.8% |
| oucontent | 279,561 | 32.2% |
| quiz | 71,751 | 11.5% |
| ouwiki | 21,555 | 7.7% |
| questionnaire | 14,694 | 6.0% |
| oucollaborate | 11,921 | 59.6% |

**Profiling findings in full.** The paragraphs below give the full evidence and reasoning behind the summaries of
Sections 3.1 to 3.4, aspect by aspect, with the issue identifiers of the Data Quality Issue Log (Table 3.1).

**Evidence behind Section 3.1: shape, keys, duplicates and joins.**

**Shape and schema.** Every table holds the number of rows that its documentation states [2], and the six tables
with a key have no duplicate key. Two names differ from the documentation: the run length is stored as
module_presentation_length rather than length, and the withdrawn outcome as "Withdrawn" rather than "Withdrawal"
[2]. Neither changes a value, and the pipeline uses the names as stored.

**Grain of the click table.** The click table differs from its documentation in grain, the level of detail that one
row represents. It is documented as the interactions of a student with a resource on a day [7], which would give one
row per student, resource and day. Instead, 1,614,505 student-resource-days hold several rows, and 1,179,074 of them
hold different click counts in their rows, up to ten rows in one group. A row is therefore a record of the logging
system rather than a day, so clicks are summed by enrolment and day before any use, and activity is counted in active
days rather than rows (DQ02).

**Exact duplicates.** In addition, 787,170 click rows (7.39%) repeat another row in every column; collapsing them
would remove 3.19% of all clicks. Two explanations are possible: the duplicates are copies made by the logging system,
or they are separate visits that happen to carry the same count. If they were copies, two rows of the same student,
resource and day would carry equal click counts far more often than chance alone would produce. They do so in 31.5%
of two-row groups, against 24.0% expected by chance from each resource's own counts; the excess appears for forums
and content pages, while quizzes, wikis and questionnaires fall below chance (Table A.6). The evidence
points both ways, so the cause cannot be decided from the data. Every row is kept, which is the table's own grain, and
a de-duplicated twin of each click feature lets Milestone 4 test whether the choice matters (DQ01).

**Joins.** Joining the tables needs care for two reasons. First, a direct join of submissions with click rows on the
student would multiply rows: it returns 89,347,197 rows, because every submission is paired with every click record
of the same student. Second, an inner join with activity, which keeps only rows that appear in both tables, would drop
the 3,365 enrolments without any click row; most of these students left before the run began and so have no activity
rows [8], and dropping them would remove withdrawals from the descriptive rates. Tables are therefore summed to the
enrolment first and then joined to the enrolment table with left joins, which keep every enrolment and record no
activity as zero (DQ17).

**Evidence behind Section 3.2: missingness and validity.**

**Missing values.** Missing values are few, and their pattern shows where they come from. The deprivation band is
blank for 1,111 enrolments (3.41%), and the blanks concentrate in two regions: 40.1% of the enrolments of North Region
and 22.5% of those of Ireland lack a band. These students also succeed more often, in 65.7% of cases against 46.6% for
students with a band, so the blanks are related to the outcome rather than random, and filling them with a typical
value would hide a group that behaves differently (DQ12). The registration day is missing for 45 enrolments, 39 of
them Withdrawn (DQ13), and 173 TMA scores are missing although the submission exists (DQ11).

**Structural gaps.** Three further gaps are structural: they follow from how the data are recorded rather than from
lost values. An empty unregistration day marks a student who did not withdraw [2]; a missing submission row marks a
task that was not submitted [2]; and exam results are usually absent by design [2], so 18 of the 24 exams have no
result row at all (DQ08). These gaps are recorded absences, and they are read as "did not withdraw", "not submitted"
and "no exam result", never filled in.

**Validity.** The validity checks found scores within 0 to 100 and no submission dated before the student's
registration, but six inconsistencies:

(1) 93 Withdrawn enrolments have no unregistration day, 87 of them in the October 2014 runs, and 9 Fail enrolments have one (DQ04);
(2) 58 enrolments registered after the two-week sign-up window that the descriptor describes [2], up to day 167 (DQ05);
(3) all 1,909 banked results carry the placeholder submission day −1 (DQ07);
(4) 98,745 clicks by 1,279 enrolments and 588 submissions by 411 enrolments are dated after the student unregistered, up to 423 days later (DQ03);
(5) 32,991 of the 69,956 CMA submissions arrive after their due day, although the OU's current policy of 2025 accepts no CMA after its cut-off day [3]; the data describe 2013–2014 practice, whose rule is not documented (DQ10);
(6) one band label, "10-20", lacks its percent sign (DQ12).

None of these is corrected by changing a recorded value. Each receives a flag or a rule in the preparation plan of
Section 5, so that the prepared data keep what was recorded and show how it was used.

**Evidence behind Section 3.3: distributions, outliers and outcome balance.**

**Activity.** Activity is strongly skewed. Per enrolment, the median is 602 clicks over the whole run, a quarter of
enrolments have 142 clicks or fewer and a quarter 1,585 or more, and 3,365 enrolments have none. The upper fence of
the interquartile range, the usual statistical boundary for an outlier (the third quartile plus one and a half times
the distance between the first and third quartiles), lies at 3,750 clicks, and 2,503 enrolments lie beyond it; a
single record of one student on one resource on one day reaches 6,977 clicks. These students are heavy users of the
platform rather than errors in the data, since nothing in the records marks their activity as false, so no value is
removed or capped (DQ16). Because a few students carry a large share of all clicks, models that are sensitive to
scale receive the logarithm of the counts instead (Section 6.2).

**Scores and study load.** Scores lean the other way: the median is 80 and a quarter of scores reach 90 or more. In
addition, 45.8% of CMA scores fall on a multiple of ten, against 17.4% of TMA scores, a sign that computer marking
moves in coarse steps. Study load reaches 655 credits, against a 99th percentile of 240; such students are taking many
modules at once, which is unusual but possible, so the value is kept.

**Outcome balance.** The brief asks whether the outcome is badly imbalanced and whether the smaller class has enough
cases [1]. The KPI population is the enrolments registered by day 14 and not unregistered by it, 28,061 enrolments, of
whom 54.7% completed. Non-completion reaches 45.3% among the enrolments still enrolled at day 13 and 44.2% among those
enrolled at day 27, so the two classes are close in size and no resampling is needed. Between runs, non-completion
ranges from 24.9% to 58.3%, and the smaller class holds at least 92 enrolments in every run, enough to estimate a rate
for each run. Figure 3.1 shows the final results of every run: withdrawal is highest in the CCC runs (43–46%), while
GGG has the fewest withdrawals but the most failures.

**Evidence behind Section 3.4: temporal coverage and representativeness.**

**Temporal coverage.** The data cover the February and October runs of 2013 and 2014, and activity is recorded from
about four weeks before the start of a run to week 39. Weekly clicks per enrolled student rise before the start, peak
in week 3, just after the first cut-off, and then settle at a lower level (Figure A.2). In all six
February 2014 runs, two consecutive days near the end of the run carry no click at all, days 218 and 219 (days 211
and 212 in BBB). A gap shared by six modules on the same days points to a failure of the logging system rather than
to students' behaviour, so the two days are treated as missing rather than as zero activity (DQ15). Both days lie long after the cut-offs.

**Tasks due by the cut-offs.** The cut-offs sit early in the run, before most assessments fall due. A TMA or CMA
falls due by day 13 in only 1 of the 22 runs, and by day 27 in 16 runs; two or more fall due by day 27 in a single
run (DQ18). The first non-exam task falls due between day 12 and day 61, depending on the module. A rule that counts
missed or late tasks therefore has nothing to count at the first cut-off in 21 runs, and Section 4.1 explains how the
early-sign rule is restated as a result.

**History for prediction.** For prediction on a later run, 9 pairs of module and start month ran in both years, so a
model built on 2013 can be tested on the same module and start month in 2014. The CCC module in both start months and
the February runs of EEE and GGG ran only in 2014, so their test runs have no 2013 counterpart. Only withdrawals dated
on or before a cut-off can be known at that cut-off [8], so the outcome at the end of the run is never available as
a feature.

**Representativeness.** Representativeness limits every claim. OULAD is a subset of OU students of 2013–2014, reduced
by anonymisation, and its modules were chosen partly because many students failed them [2]. The students learn at a
distance; 70.4% are under 35, and 63.1% study 60 credits or fewer at once. The modules differ sharply: women form
11.5% of the enrolments in EEE and 88.4% in BBB, and completion in the KPI population ranges from 45.7% in CCC to
73.8% in AAA. The deprivation band follows each nation's own index and cannot be pooled across nations [6]. Results
therefore describe OULAD runs, groups are compared within module rather than across modules, and every result must be
checked on the university's own records before it informs decisions D1 to D3 (DQ19).

**Measures in full.**

Three of the key fields of Table A.2 need care before they become measures. First, a banked result is a result
carried over from an earlier run of the same module, and all 1,909 of them carry the placeholder submission day −1
rather than a real day, so they cannot be used to time a submission. Second, scores run from 0 to 100 with 40 as the
pass mark [2], but a TMA is returned by the tutor, usually within ten working days of its due day, and a CMA score is
expected within 7 days [3]; OULAD holds no day on which a mark was released, so a TMA mark cannot be shown to be known
at a cut-off. Third, weights depart from the documented rule [2] in two places: the three GGG runs weight all
coursework at zero, and the two CCC runs of 2014 hold two exams. Studied credits count every module the student takes
at the same time [2], with 60 credits a year being part-time and 120 full-time study [4], so they measure study load
rather than effort in one module.

===== reports/milestone-3/report/12-02-pipeline-package.md @ 19d35a4 =====
## Appendix II – Preparation Pipeline and Prepared Data Package

Figure A.3 shows the five phases of the pipeline, from the read-only raw files to the validated package.

![Figure A.3. From the raw files to the prepared views](assets/figures/fig-6-1-pipeline.png)

Table A.7 maps the ten preparation steps of the brief to the function of `src/prepare_data.py` or the script that carries each out, with the row counts it produced.

**Table A.7. Pipeline steps, code and results**

| Step (brief) | Code | Result |
| :---- | :---- | :---- |
| 1 Load raw files, validate schema | `step1_load_validate` | 7 tables, SHA-256 equal to the pins, columns as documented |
| 2 Select in-scope population | `step2_population` | 32,593 enrolments; 28,069 / 28,061 / 27,535 enrolled at days 13 / 14 / 27 |
| 3 Standardise types, labels, identifiers | `step3_standardise` | 3,516 "10-20" labels fixed; 182 tasks (TMA, CMA) |
| 4 Resolve keys and duplicates | `step4_keys` | 10,655,280 click rows → 1,808,119 enrolment-day records |
| 5 Handle missing values | `step5_missing` | 1,111 "Missing" bands; 45, 93, 9 and 1 flagged records |
| 6 Handle invalid values | `step6_truncate` | 98,745 clicks after withdrawal left out |
| 7 Integrate tables | `step7_integrate` | 286,898 enrolment-task rows; 168,953 submissions placed |
| 8 Construct features | `cutoff_features` | 28,069 and 27,535 feature rows |
| 9 Analysis-ready tables | `step9_views` | 6 views, among them 1,052,344 enrolment-week rows |
| 10 Persist with log and metadata | `step10_persist`, `fit_transforms.py`, `validate_prepared.py` | 8 Parquet files, dictionary, lineage, validation summary, version manifest |

The Prepared Data Package, submitted with this report, is laid out as the brief recommends: `data/raw/` (immutable inputs), `data/interim/`, `data/processed/`, `data/metadata/`, `notebooks/`, `src/`, `tests/` and `logs/`. One command, run from the package folder, rebuilds it from the raw files; when `data/raw/` is empty it first downloads the published archive and checks every table against its pinned SHA-256:

```
bash src/run_all.sh
```

Table A.8 lists the eight stages the command runs, each recording its command, time, output and exit status in `logs/`.

**Table A.8. Stages of run_all.sh**

| Stage | Script | Output |
| :---- | :---- | :---- |
| 00 | `link_raw.py` | raw files hard-linked, SHA-256 checked against the Milestone 2 pins |
| 01 | `01_understand.py` | Dataset Understanding Map (Section 2.1) |
| 02 | `02_profile.py` | profile and quality evidence (Section 3) |
| 03 | `unittest on tests/` | formula tests on synthetic fixtures |
| 04 | `prepare_data.py` | ten preparation steps, views and transformation log (Section 6) |
| 05 | `fit_transforms.py` | transforms fitted on 2013 runs, model-ready matrices (Section 6.3) |
| 06 | `validate_prepared.py` | 22 checks, dictionary, lineage, version manifest (Section 7) |
| 07 | `build_notebooks.py` | notebooks 02 and 03, executed |

The transformation log records every operation with its row counts, in the order the pipeline runs them; each raw table is loaded only after its SHA-256 matches the pin and its columns match the documentation. Table A.9 reproduces it.

**Table A.9. Transformation log**

| Step | Operation | Rows in | Rows out | Note |
| :---- | :---- | :---- | :---- | :---- |
| 1 load | courses.csv |  | 22 |  |
| 1 load | assessments.csv |  | 206 |  |
| 1 load | vle.csv |  | 6,364 |  |
| 1 load | studentInfo.csv |  | 32,593 |  |
| 1 load | studentRegistration.csv |  | 32,593 |  |
| 1 load | studentAssessment.csv |  | 173,912 |  |
| 1 load | studentVle.csv |  | 10,655,280 |  |
| 2 population | studentInfo + studentRegistration | 32,593 | 32,593 | left join, rows kept |
| 2 population | + courses (run length) | 32,593 | 32,593 | left join, rows kept |
| 2 population | flag enrolled_d13 | 32,593 | 28,069 | enrolled at the day (C09) |
| 2 population | flag enrolled_d14 | 32,593 | 28,061 | enrolled at the day (C09) |
| 2 population | flag enrolled_d27 | 32,593 | 27,535 | enrolled at the day (C09) |
| 3 standardise | imd_band label '10-20' → '10-20%' | 3,516 | 0 |  |
| 3 standardise | year, start_month, completed, non_completion, split derived | 32,593 | 32,593 |  |
| 3 standardise | tasks = TMA and CMA (exams excluded, DQ08) | 206 | 182 |  |
| 4 keys | studentVle rows → enrolment × day (records, clicks, clicks_dedup) | 10,655,280 | 1,808,119 | clicks 39,605,099, de-duplicated 38,343,063 |
| 4 keys | studentVle rows → distinct enrolment × site × day | 10,655,280 | 8,459,320 |  |
| 5 missing | imd_band missing → category 'Missing' (no imputation) | 1,111 | 1,111 |  |
| 5 missing | flag registration_missing | 32,593 | 45 |  |
| 5 missing | flag withdrawal_day_missing | 32,593 | 93 |  |
| 5 missing | flag unregistered_not_withdrawn | 32,593 | 9 |  |
| 5 missing | flag unregistered_after_run_end | 32,593 | 1 |  |
| 6 truncate | enrolment × day click records up to the unregistration day | 1,808,119 | 1,802,593 | clicks removed 98,745 |
| 6 truncate | enrolment × site × day records up to the unregistration day | 8,459,320 | 8,435,429 |  |
| 7 integrate | enrolment × task grid (TMA, CMA of the run) | 32,593 | 286,898 |  |
| 7 integrate | + submission (if any) | 286,898 | 286,898 | left join, rows kept |
| 7 integrate | TMA/CMA submissions placed in the grid | 168,953 | 168,953 |  |
| 9 views | + banked results | 32,593 | 32,593 | left join, rows kept |
| 9 views | + concurrent runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + student seen in training runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + paired run flag | 32,593 | 32,593 | left join, rows kept |
| 9 views | + first missed task week | 32,593 | 32,593 | left join, rows kept |
| 9 views | + tasks while enrolled | 32,593 | 32,593 | left join, rows kept |
| 9 views | + whole-run activity (truncated at withdrawal) | 32,593 | 32,593 | left join, rows kept |
| 9 views | student_week grid + weekly clicks | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + weekly distinct resources | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + logging-gap flag (DQ15) | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | student_week rows (weeks -3..run end, cut at withdrawal) |  | 1,052,344 | clicks before week -3 not in this view: 0 |
| 8 features d13 | + activity up to the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + distinct resources | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks due by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + CMA marks known by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks submitted before their due day (due after the cut-off) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + run median of clicks up to the cut-off (same run, no outcome) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | features built; max event day ≤ cut-off | 28,069 | 28,069 | early_sign_rule 5,673 |
| 8 features d27 | + activity up to the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + distinct resources | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks due by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + CMA marks known by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks submitted before their due day (due after the cut-off) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + run median of clicks up to the cut-off (same run, no outcome) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | features built; max event day ≤ cut-off | 27,535 | 27,535 | early_sign_rule 7,933 |
| 10 persist | processed/enrolment.parquet |  | 32,593 | 39 columns |
| 10 persist | processed/assessment_due.parquet |  | 286,898 | 14 columns |
| 10 persist | processed/student_week.parquet |  | 1,052,344 | 10 columns |
| 10 persist | processed/features_d13.parquet |  | 28,069 | 50 columns |
| 10 persist | processed/features_d27.parquet |  | 27,535 | 52 columns |
| 10 persist | processed/capacity_by_run.parquet |  | 44 | 9 columns |

The prepared files are identified by version OULAD-N04-prepared-1.0; Table A.10 gives their row counts and hashes from `version_manifest.json`, identical across two runs from the raw files.

**Table A.10. Prepared files**

| File | Rows | SHA-256 (first 16) |
| :---- | :---- | :---- |
| assessment_due.parquet | 286,898 | f67d7916dd95c2ab |
| capacity_by_run.parquet | 44 | 38f6868c2b74fcc7 |
| enrolment.parquet | 32,593 | 1d1e397ac67ce774 |
| features_d13.parquet | 28,069 | c58a44150e8c367c |
| features_d27.parquet | 27,535 | 4bf8a482b9ec7fa4 |
| model_ready_d13.parquet | 28,069 | 773d1e2fa0773564 |
| model_ready_d27.parquet | 27,535 | 3560a51594d4ad97 |
| student_week.parquet | 1,052,344 | 7526872e26e95da7 |

**Flagged records and placed submissions.** In step 5 of the pipeline, the four groups of flagged records are the 45
enrolments without a registration day, the 93 Withdrawn enrolments without a withdrawal day, the 9 Fail enrolments
with one, and the one unregistration on day 444 of a 268-day run. Step 7 places all 168,953 TMA and CMA submissions on
an enrolment-task row, the 1,909 banked results among them with the status "banked", so that they are counted but
never timed; the other 4,959 of the 173,912 submission rows are exam results, which are not tasks.

**Split controls in full.** The paragraphs below explain the controls summarised at the end of Section 6.3.

**Students seen in both years.** The 1,962 test enrolments of students who also enrolled in a 2013 run stay in the
main test set, because a later run of the same modules also contains repeating students, and a flag marks them so that
Milestone 4 can repeat the test on students never seen in training. When Milestone 4 tunes a model, it uses
leave-one-run-out folds inside 2013, holding out one run at a time, and removes from each fold's training data the
students who also appear in the held-out run, since the same student on both sides of a fold would inflate the
estimate [13].

**Fitted transforms.** Transforms that learn parameters from the data, such as filling a missing value with a median
or scaling a variable, are fitted on the training runs alone and then applied to the test runs [11]. As a check, the
parameters were fitted again after every test row had been changed, and they stayed the same, which shows that no
test row informs them. In addition, the 2014 outcomes are not looked at while the data are prepared: the validation
reports test outcome rates only as counts, so that the test set remains an independent check, as the brief requires
[1]. Test results will also be reported without the test enrolments that are Withdrawn without a withdrawal day, 89 at
day 13 and 90 at day 27, because such students may have left before the cut-off without a record of it.

**Package layout in full.**

The package follows the layout that the brief recommends [1]: `data/raw/` holds the immutable
raw tables; `data/interim/` the intermediate results that the pipeline can recreate; `data/processed/` the
analytic-ready views; `data/metadata/` the dictionary, lineage, quality logs and validation results; `notebooks/` the
notebooks for data understanding and preparation; and `src/` the scripts.

===== reports/milestone-3/report/12-03-dictionary-lineage.md @ 19d35a4 =====
## Appendix III – Prepared Data Dictionary and Lineage

Table A.11 links each analytics level to its prepared view, population and grain, with the check the brief sets before Milestone 4 and its result.

**Table A.11. Prepared views by analytics level**

| Level | Prepared view | Population | Grain | Check before Milestone 4 | Result |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Descriptive | enrolment, assessment_due, student_week | 32,593 enrolments; KPI on 28,061 | enrolment; enrolment × task; enrolment × week | No double counting, no join bias | Keys unique; joins kept rows; clicks reconcile |
| Diagnostic | features_d27 + enrolment | 27,535 enrolled at day 27 | enrolment | Associations from real data with comparison groups | Signs up to day 27; seven modules for within-module comparison |
| Predictive | features_d13, features_d27, model_ready | 28,069 and 27,535 | enrolment | Target, prediction point, pre-point features, split, enough of each class | Smaller class ≥ 92 per run; 9 training and 13 test runs; train-only transforms |
| Prescriptive | capacity_by_run | 44 run × cut-off rows | run × cut-off | Action, constraint, cost and outcome data | Assumed capacities only; no contact or outcome data |

The data dictionary (`data/metadata/data_dictionary.md`) lists every column of every view with its type, role, source, transformation and sensitivity. Table A.12 is the lineage table of brief section 13.1, one row per prepared variable other than the keys; the six sensitive variables are marked in the purpose column.

**Table A.12. Data lineage**

| Prepared variable | Source file / field | Transformation | Window / filter | Purpose / AQ |
| :---- | :---- | :---- | :---- | :---- |
| year | code_presentation | first four characters | – | time split |
| split | code_presentation | train if 2013, test if 2014 | run level | AQ3 time split (C07) |
| paired_run | courses | module and start month ran in both years | run level | AQ3 evaluation subsets |
| student_in_training_runs | studentInfo.id_student | test enrolment of a student with a 2013 enrolment | – | AQ3 strict unseen-student check |
| eval_withdrawal_day_unknown | final_result, date_unregistration | Withdrawn without a withdrawal day | – | AQ3: report test metrics with and without these rows (audit F1) |
| final_result | studentInfo.final_result | as recorded | observed at run end | AQ1 outcome |
| non_completion | studentInfo.final_result | Fail or Withdrawn | observed at run end | AQ1–AQ3 target |
| completed | studentInfo.final_result | Pass or Distinction | observed at run end | primary KPI |
| withdrawal_day_missing | final_result, date_unregistration | Withdrawn without a day | – | DQ04 flag |
| unregistered_not_withdrawn | final_result, date_unregistration | not Withdrawn but a day recorded | – | DQ04 flag |
| unregistered_after_run_end | date_unregistration, courses | day after run length | – | DQ06 flag |
| date_registration | studentRegistration.date_registration | as recorded | day offset | populations |
| date_unregistration | studentRegistration.date_unregistration | as recorded | day offset; after the cut-offs for feature rows | populations, withdrawal timing (AQ1) |
| enrolled_d13 | registration days | enrolled_at(13) | day 13 | AQ3 population (C09) |
| enrolled_d14 | registration days | enrolled_at(14) | day 14 | primary KPI denominator (C09) |
| enrolled_d27 | registration days | enrolled_at(27) | day 27 | AQ3 population (C09) |
| start_month | code_presentation | last character: B = February, J = October | – | AQ1 dimension; AQ3 predictor |
| run_length | courses.module_presentation_length | renamed | – | run end |
| gender | studentInfo.gender | as recorded | – | AQ3–AQ4 fairness audit (sensitive) |
| region | studentInfo.region | as recorded | – | fairness audit; explains imd_band Missing (sensitive) |
| age_band | studentInfo.age_band | as recorded (ordered 0-35, 35-55, 55<=) | – | fairness audit (sensitive) |
| disability | studentInfo.disability | as recorded (Y/N) | – | AQ4 fairness limit (C04) (sensitive) |
| imd_band | studentInfo.imd_band | '10-20' → '10-20%'; missing → 'Missing' | – | AQ4 fairness limit (C04) (sensitive) |
| highest_education | studentInfo.highest_education | ordered; ordinal code in model_ready | known at enrolment | AQ2–AQ3 (sensitive) |
| num_of_prev_attempts | studentInfo.num_of_prev_attempts | as recorded | known at enrolment | AQ3 |
| studied_credits | studentInfo.studied_credits | as recorded; outliers kept | known at enrolment | AQ3 (study load) |
| registration_lead | studentRegistration.date_registration | −date_registration | known at registration | AQ2–AQ3 |
| registration_missing | studentRegistration.date_registration | registration day missing | known at registration | AQ3 extended (39 of 45 are Withdrawn) |
| banked_results | studentAssessment.is_banked | count of banked results | known at registration | AQ3 |
| concurrent_runs | studentInfo | other enrolments of the student in the same presentation | – | AQ2 (2014 only, C12) |
| first_missed_week | assessment_due | week of earliest TMA/CMA not submitted and due while enrolled | whole run | AQ1 |
| tasks_due_while_enrolled | assessment_due | count, banked excluded | whole run | AQ1–AQ2 |
| tasks_missed_while_enrolled | assessment_due | count not submitted | whole run | AQ1–AQ2 |
| tasks_late_while_enrolled | assessment_due | count submitted after the due day | whole run | AQ2 |
| total_clicks | studentVle.sum_click | sum of all rows | whole run, up to the unregistration day | AQ1–AQ2 |
| total_clicks_dedup | studentVle.sum_click | sum with exact duplicate rows once | as total_clicks | DQ01 sensitivity |
| active_days | studentVle.date | distinct days with a click | whole run (student_week: within the week), up to the unregistration day | AQ1–AQ2 |
| assessment_type | assessments.assessment_type | TMA or CMA (exams excluded) | – | AQ1–AQ2 |
| due_day | assessments.date | renamed | day offset | AQ1–AQ2 |
| due_week | assessments.date | floor(due / 7) + 1 | – | AQ1 |
| weight | assessments.weight | as recorded; not used for grades | – | DQ09 |
| date_submitted | studentAssessment.date_submitted | as recorded; null if not submitted | whole run | AQ1–AQ2 |
| is_banked | studentAssessment.is_banked | as recorded | – | DQ07 |
| score | studentAssessment.score | as recorded; not a feature except via cma_score_mean_c | whole run | AQ2 |
| status | date_submitted, due day, is_banked | banked / not_submitted / on_time / late | whole run | AQ1–AQ2 |
| lateness_days | date_submitted, due day | submitted − due (non-banked) | whole run | AQ2 |
| due_while_enrolled | due day, registration days | registered by due day and unregistered after it | whole run | AQ1 (missed only if due while enrolled) |
| clicks | studentVle.sum_click | sum per week | week, up to the unregistration day | AQ1–AQ2 |
| clicks_dedup | studentVle.sum_click | weekly sum, exact duplicates once | week | DQ01 sensitivity |
| records | studentVle | number of log rows | week | DQ02 |
| sites | studentVle.id_site | distinct resources | week | AQ2 |
| logging_gap | studentVle.date | week holds a day with no click in the whole run | week | DQ15 |
| clicks_pre | studentVle.sum_click, date | sum | days before 0 | AQ2–AQ3 |
| clicks_pre14 | studentVle.sum_click, date | sum | days −14 to −1 | AQ3 |
| clicks_0c | studentVle.sum_click, date | sum (= sum of clicks_w*) | days 0 to c | AQ2–AQ3 |
| clicks_0c_dedup | studentVle | sum, exact duplicate rows once | days 0 to c | DQ01 sensitivity |
| active_days_0c | studentVle.date | distinct days with a click | days 0 to c | AQ2–AQ3 |
| sites_0c | studentVle.id_site | distinct resources | days 0 to c | AQ3 |
| inactive_last7 | studentVle | no click in days c−6 to c | last seven days | AQ2–AQ3; rule part |
| activity_ratio_run | studentVle | (clicks_0c + 1) ÷ (run median of clicks_0c + 1) | same run, days 0 to c, enrolled at c | AQ2 sign against the course average |
| tasks_due_c | assessments.date | TMA/CMA due by c and on or after the registration day | due ≤ c | AQ2–AQ3 |
| tasks_missed_c | studentAssessment | due ≤ c, no non-banked submission by c | submissions ≤ c | AQ2–AQ3; rule part |
| tasks_late_c | studentAssessment | due ≤ c, submitted after due and by c | submissions ≤ c | AQ2–AQ3 |
| tma_late_c | studentAssessment | late TMA by c | submissions ≤ c | AQ2–AQ3; rule part |
| cma_late_c | studentAssessment | late CMA by c | submissions ≤ c | AQ2–AQ3; rule variant |
| cma_marked_c | studentAssessment | CMA marks known by c | submitted ≤ c − 7 | AQ3 (coverage of the CMA score) |
| cma_score_mean_c | studentAssessment.score | mean of known CMA marks; null if none | submitted ≤ c − 7 | AQ3 |
| days_since_last_click | studentVle.date | c − last active day; c + 1 if no click in 0…c | days 0 to c | AQ3 |
| trend_last_week | studentVle | last week's clicks − previous week's | weeks up to c | AQ3 |
| tasks_submitted_early_c | studentAssessment | tasks due after c submitted by c | submissions ≤ c | AQ3 |
| clicks_oucontent_0c | studentVle, vle.activity_type | sum on content pages | days 0 to c | AQ2–AQ3 |
| clicks_forumng_0c | studentVle, vle.activity_type | sum on forums | days 0 to c | AQ2–AQ3 |
| clicks_quiz_0c | studentVle, vle.activity_type | sum on quizzes | days 0 to c | AQ2–AQ3 |
| clicks_homepage_0c | studentVle, vle.activity_type | sum on the homepage | days 0 to c | AQ2–AQ3 |
| early_sign_rule | derived | rule_missed or rule_tma_late or inactive_last7 | at c | AQ3 comparison rule; secondary KPI 1 (C10) |
| early_sign_rule_cma | derived | early_sign_rule or cma_late_c ≥ 1 | at c | sensitivity variant |
| rule_missed | derived | tasks_missed_c ≥ 1 | at c | rule part |
| rule_tma_late | derived | tma_late_c ≥ 1 | at c | rule part |
| enrolled | features views | count enrolled at the cut-off | run, cut-off | AQ4 |
| tutor_groups_est | enrolled | ceil(enrolled / 20) | run, cut-off | AQ4 (assumed group of 20) |
| list_tutor_3 | tutor_groups_est | 3 × groups (≤ enrolled) | run, cut-off | AQ4 assumed capacity |
| list_tutor_5 | tutor_groups_est | 5 × groups (≤ enrolled) | run, cut-off | AQ4 assumed capacity |
| list_office_30 | enrolled | min(30, enrolled) | run, cut-off | AQ4 assumed capacity |
| list_office_40 | enrolled | min(40, enrolled) | run, cut-off | AQ4 assumed capacity |
| clicks_w1 | studentVle | sum per week | week 1 (days 0–6) | AQ3 weekly trajectory |
| clicks_w2 | studentVle | sum per week | week 2 (days 7–13) | AQ3 weekly trajectory |
| clicks_w3 | studentVle | sum per week | week 3 (days 14–20) | AQ3 weekly trajectory |
| clicks_w4 | studentVle | sum per week | week 4 (days 21–27) | AQ3 weekly trajectory |

**Feature choices and predictor sets.**

Two of these definitions carry a choice. A task counts as missed only if it fell due on or after the student's
registration day, because a student who registers late cannot have missed a task that fell due before they joined.
The activity ratio compares a student with the median of the same run up to the same day, which stands for the "course
average" of the AQ2 sign; it adds one to both counts so that a run or a student with no clicks gives a defined value,
and it uses no outcome, so staff could compute it on the day of the cut-off.

**Predictor sets.** The feature views hold 20 primary predictors and 10 extended predictors, plus the weekly click
counts up to the cut-off, two at day 13 and four at day 27; every other column is an identifier, the target, a flag
for evaluation, the rule or an audit attribute. The primary set covers the module and start month, prior education,
previous attempts, study load, how early the student registered, banked results, activity before and after the start,
the activity ratio, inactivity, and the task counts and lateness. The extended set holds ten predictors for comparison in
Milestone 4: the registration-missing indicator, the de-duplicated clicks, the clicks in the 14 days before the start,
the days since the last click, the trend over the last week, the tasks submitted early, and the clicks on content
pages, forums, quizzes and the home page. The CMA score falls below the coverage that a predictor needs, as Section 7.3 explains.
Demographic attributes serve mainly the fairness audit, because earlier experiments at the OU found that adding them
to activity and assessment data did not significantly improve the prediction of students at risk [9]; Table A.12 gives
every prepared variable with its source and purpose.

===== reports/milestone-3/report/12-04-traceability-change-log.md @ 19d35a4 =====
## Appendix IV – Updated Traceability and Controlled Change Log

Table A.13 is the updated traceability of deliverable B: each row runs from the goal and KPI through the question and its analytics type to the raw variables, the preparation, the prepared variables and the decision supported.

**Table A.13. Updated traceability**

| Business Goal / SMART / KPI | AQ | Analytics type | Raw variables | Preparation | Prepared variables / view | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Primary KPI: completion rate of students enrolled after the add-drop period (day 14; SMART assumed 70% → 75%) | AQ1 | Descriptive | studentInfo.final_result; studentRegistration.date_registration, date_unregistration; assessments.date; studentAssessment.date_submitted, is_banked | Enrolled-at-day rule (C09); tasks = TMA and CMA; banked results separated; missed only if due while enrolled | `enrolment`: completed, non_completion, enrolled_d14, first_missed_week, code_module, code_presentation, start_month, year; `assessment_due`: status, due_week | D2 where advisors' time goes; D3 extend after the pilot |
| Primary KPI; secondary KPI 1, sign part (early-sign rule, C10) | AQ2 | Diagnostic | + studentVle.date, sum_click, id_site; vle.activity_type | Clicks aggregated by enrolment × day (DQ02), truncated at withdrawal (DQ03), all rows kept with a de-duplicated twin (DQ01); signs up to day 27 | `features_d27`: tasks_missed_c, tasks_late_c, tma_late_c, cma_late_c, inactive_last7, activity_ratio_run, clicks_*_0c; `enrolment`: concurrent_runs (2014) | D2; the reasons shown with D1 lists |
| Secondary KPI 1, sign part | AQ3 | Predictive | as AQ2 + num_of_prev_attempts, studied_credits, highest_education, date_registration, is_banked, score (CMA) | Populations at days 13 and 27; events ≤ cut-off only; CMA marks known at c − 7; time split; transforms fitted on 2013 runs | `features_d13`, `features_d27` (20 primary, 10 extended predictors, weekly clicks), `early_sign_rule`, `split`, `paired_run`, `student_in_training_runs`; `model_ready_d13/d27` | D1 who is listed in weeks 3 and 5 |
| Secondary KPI 2 (follow-up rate) and secondary KPI 1, contact part: pilot only (C08) | AQ4 | Prescriptive (ranking; AQ4 rewritten, C11) | AQ3 inputs; gender, age_band, disability, imd_band, region as audit columns | Capacity scenarios from tutor groups of about 20; list quality as lift and attainable recall (C13); fairness by imd_band ("Missing" apart) and disability | `capacity_by_run`: enrolled, list_tutor_3, list_tutor_5, list_office_30, list_office_40; audit columns in the feature views | D1 ordered list within capacity; contact choice deferred |

Table A.14 is the Controlled Change Log of deliverable E: C01–C08 from Milestone 2 and C09–C13 from the data understanding of Milestone 3 (column M), each with its evidence and effect.

**Table A.14. Controlled Change Log**

| ID | M | Old content | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C01 | 2 | The program's online and blended courses at a Vietnamese university | OULAD module runs (UK Open University, distance learning, 2013–2014) as an open stand-in for the analysis; the university's own records remain the target for the pilot | No open dataset of Vietnamese courses was found; OULAD is the only candidate passing the gates | All AQs answered on stand-in data; results describe OULAD and must be re-checked on the university's data before D1–D3 |
| C02 | 2 | Course and semester; weeks 1–5 of a semester (length not fixed in Milestone 1) | Module run (`code_presentation`), eight to nine months; days counted from day 0 of the run; week n = days 7(n−1) to 7n−1 | Dates in OULAD are days from the run start; runs last 234–269 days | Cut-offs become day 13 (week-3 list) and day 27 (week-5 list); the semester-length difference is a stated limit |
| C03 | 2 | Denominator: students enrolled after the add-drop period; withdrawal as in Circular 83/2026 | Enrolments still registered at day 14 (registration closes two weeks after the start); leave and transfer cannot be told apart | `date_registration`, `date_unregistration` exist; no status field for leave or transfer | Primary KPI computed as a proxy on 28,119 enrolments; deviation from the Circular 83 rule recorded |
| C04 | 2 | Comparisons by delivery mode and year of study; AQ4 limit on first-year against later-year recall | Comparisons by module and run; the fairness limit is checked across IMD band and disability | No delivery-mode or year-of-study field; all modules are distance learning | AQ1–AQ3 narrowed; AQ4 limit re-expressed on available groups |
| C05 | 2 | AQ2 sign: attendance at in-class sessions (blended courses) | Dropped | No in-class sessions or attendance in OULAD | AQ2 uses missed and late tasks, activity and concurrent runs |
| C06 | 2 | AQ3 week-3 list from assessment and activity signs | Week-3 list (day-13 cut-off) from activity only; assessment signs start with the week-5 list | A non-exam task is due by day 13 in 1 of 22 runs, by day 27 in 16 | Secondary KPI 1: two tasks fall due by day 27 in only 1 of 22 runs, so on OULAD its sign part counts one missed or late task in the 16 runs with a task due by day 27; the two-task rule stays for the university |
| C07 | 2 | AQ3 tested on a later semester of the same pilot courses | Train on 2013 runs, test on 2014 runs of the same module and start month (9 pairs); CCC, EEE-B and GGG-B only as later runs | B and J runs should be analysed separately; each module has at most two runs of one start month | Time-based validation feasible but with one earlier run per pair |
| C08 | 2 | AQ4 action and outcome; secondary KPI 2 and the contact part of secondary KPI 1 measured from a contact record | Kept as a future decision requirement; AQ4 limited to ranking under assumed capacity | No contact, capacity or intervention data in any candidate | No prescriptive or causal claim; secondary KPI 1 (contact part) and secondary KPI 2 measured only in the pilot |
| C09 | 3 | KPI denominator: enrolments still registered at day 14 (28,119; C03) | Enrolled at day d = registered by day d (or registration day unknown) and not unregistered by day d; day 14 for the KPI (28,061), days 13 and 27 for the lists (28,069; 27,535) | 58 enrolments registered after day 14, up to day 167 (DQ05) | Primary KPI recomputed on 28,061 enrolments; same rule for every population |
| C10 | 3 | AQ3 comparison rule and secondary KPI 1 early-sign rule: two or more assessed tasks missed or late by week 4 (Milestone 1); on OULAD one missed or late task, in the 16 runs with a task due by day 27 (C06) | Early-sign rule: at least one TMA or CMA due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off; CMA lateness only in a sensitivity variant | Two or more tasks are due by day 27 in 1 of 22 runs, one or more in 16, and by day 13 in 1 (DQ18), so a rule on tasks alone cannot fire in 6 runs at day 27 or in 21 at day 13; the meaning of a late CMA in 2013–2014 is undocumented (DQ10) | The rule can fire in every run; secondary KPI 1 (sign part) uses the same rule |
| C11 | 3 | AQ4: whom to list, in what order and with which contact, within capacity | AQ4 (rewritten): ranking under an assumed capacity with recall and precision overall and by deprivation band and disability; the choice of contact and its effect deferred to the pilot | No contact, capacity or outcome-after-contact data (C08; AQ4 RED) | No prescriptive claim; D1 receives an ordered list and its measured quality, not a contact plan |
| C12 | 3 | AQ2 sign "tasks missed in several modules at once", all runs | Described for 2014 runs only; not a predictor in AQ3 | Of 1,382 concurrent enrolments at day 14, 12 fall in 2013 runs (training runs) | AQ2 narrowed; AQ3 feature set excludes it |
| C13 | 3 | AQ4 list limit: precision of at least 50% | List quality measured as lift over the run's base rate and as recall against the most a list of the same size can reach, with a random list and the early-sign rule as baselines | Non-completion is 45.3% at day 13 and 44.2% at day 27, and 24.9–58.3% by run, so a random list already reaches about 45% precision; lists of 3 or 5 per 20 students cap recall | AQ4 limit re-expressed; D1 judges a list by its gain over chance |

**Reasoning behind each fit rating.** The paragraphs below explain, question by question, the ratings of the AQ–Data
Fit Decision Log (Table 4.1) and the changes C09 to C13 that follow from them.

**AQ1, descriptive.** OULAD records the final result of every enrolment and the due day of every task, so completion
rates by module, run, start month and year can be computed, and the week of the first missed task can be derived
from due days and submissions. The question is YELLOW rather than GREEN because two of its comparisons, by year of
study and by delivery mode, have no field in OULAD, and because exam results are missing in five modules, so the
first missed task is taken over TMA and CMA only. In addition, the population of the rates is restated: an enrolment
counts as enrolled on a given day when the student registered by that day, or the registration day is unknown, and
did not unregister by it. This rule (C09) adds the registration condition to the Milestone 2 definition, which counted
every enrolment still registered on day 14 (28,119); it removes the 58 students who registered after day 14 and leaves
28,061 enrolments in the KPI population, and the same rule gives the populations at both cut-offs.

**AQ2, diagnostic.** Each sign of AQ2 can be derived from the click and submission records with a stated formula and
window. Two parts of the question narrow. Task signs exist only in the 16 runs where a task falls due by day 27.
The sign "tasks missed in several modules at once" needs students enrolled in two runs at the same time, and of the
1,382 such enrolments at day 14, only 12 fall in the 2013 runs; the sign is therefore described for the 2014 runs
only and does not enter the predictive features, which are learned on 2013 (C12). AQ2 measures association, not
cause, and the attendance sign of Milestone 1 has no counterpart in distance learning.

**AQ3, predictive.** The target exists for every enrolment, the populations at both cut-offs are large, and nine
module and start-month pairs ran in both years, so a model built on 2013 can be tested on 2014. The comparison rule is
the weak part. In Milestone 1, the early-sign rule reads "two or more assessed tasks missed or late by the end of week
4"; two tasks fall due by day 27 in only one run, so Milestone 2 counted one missed or late task (C06), but even that
form cannot fire in the 6 runs without a task due by day 27 or in 21 runs at day 13. The meaning of a late CMA in
2013–2014 is also undocumented (DQ10). The rule is therefore restated (C10): a student shows early signs when a task
due by the cut-off has not been submitted, or a TMA has been submitted late, or the student has had no platform
activity in the seven days before the cut-off. The rule can now fire in every run, and the CMA-lateness version is kept
only as a sensitivity variant. Scores, in turn, enter only where the mark is known by the cut-off, which holds for CMA
marks submitted at least seven days earlier and never for TMA marks.

**AQ4, prescriptive.** AQ4 asks whom to list, in what order and with which contact, within capacity. OULAD records no
contact, no type of contact, no staff capacity and no outcome after a contact, and none of the seven candidate datasets
of Milestone 2 records them either, so the question is RED. Following the brief's order, it is rewritten to the part
the data support: under an assumed weekly capacity, which enrolments rank first at each cut-off, and what recall, the
share of later non-completers who appear on the list, and what precision, the share of listed students who later fail
or withdraw, the list reaches overall and by deprivation band and disability (C11). The choice of contact and its effect
are deferred to the pilot, where the contact record will exist. In addition, the Milestone 1 limit of at least 50%
precision says little when 44–45% of students do not
complete, since a random list already reaches about 45%. List quality is therefore measured as lift, the precision of
the list divided by the run's rate of non-completion, and as recall against the most that a list of the same length
can reach, with a random list and the early-sign rule as baselines (C13).

**Changes from Milestone 2 in full.** Milestone 2 selected OULAD as an open
stand-in for the university's own records, which cannot be used yet, and recorded eight changes, C01 to C08, in the
Controlled Change Log, the list of every change to the baseline with its reason in the data. The population became
the OULAD module runs of 2013–2014, the courses of a distance-learning university in the UK, in place of
the program's courses (C01). Time became a count of days from the start of each run, which places the two data
cut-offs at day 13 and day 27 (C02). The KPI denominator became the enrolments still registered on day 14 (C03).
Comparisons by delivery mode and year of study became comparisons by module and run, since OULAD records neither
(C04), and the attendance sign was dropped because distance learning has no classes to attend (C05). The week-3 list
rests on activity alone, because a task falls due by day 13 in only one run, and on OULAD the early-sign rule counts
one missed or late task rather than two (C06). The predictive question is trained on the 2013 runs and tested on the
2014 runs (C07), and the choice of contact and its outcome remain a requirement for the pilot, because OULAD records
no contact (C08).

**Synthetic-data policy in full.**

The brief allows synthetic data at five levels with different conditions: small test data for
code (level A) and simulation to illustrate a method (level B) are allowed; augmentation of training data (level C)
needs the lecturer's approval; and synthetic data that fill a missing concept, label or intervention (level D) or that
enter descriptive or diagnostic evidence (level E) are not allowed [1]. This project uses level A only: a few
hand-made test enrolments, labelled as synthetic in the `tests/` folder of the Prepared Data Package, check that each
feature formula gives the expected value. They never enter a prepared view, a statistic or a finding, and no
augmentation is planned.

===== reports/milestone-3/report/12-05-ai-decision-log.md @ 19d35a4 =====
## Appendix V – AI Decision Log and Prompts

Table A.15 is the AI Decision Log of deliverable F, one row per significant AI suggestion with our decision and the evidence used to verify it.

**Table A.15. AI Decision Log**

| # | Role (brief 14) | AI suggestion | Team decision | Accepted / Rejected | Evidence used to verify | Effect on pipeline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A1 | Data dictionary interpreter | A CMA score appears within 7 days and a CMA cannot be submitted late [3] | Use the 7-day lag for CMA scores; do not apply the no-late rule to 2013–2014 | Accepted in part | 32,991 of 69,956 CMA submissions are after the due day (profile.json) | `cma_score_mean_c` uses marks submitted ≤ c − 7; late counts split by TMA and CMA |
| A2 | Data dictionary interpreter | The English IMD covers England only; other UK nations use their own indices [5], [6] | Keep imd_band as recorded, "Missing" as its own group, no pooling claims across nations | Accepted | imd_band missing for 40.1% of North Region, 22.5% of Ireland (profile.json) | imd_band is an audit column; fairness rows keep "Missing" apart |
| A3 | EDA / quality checklist partner | Test whether exact duplicate click rows are copies or separate records | Run a chance test on two-row groups | Accepted | 31.5% equal against 24.0% expected; below chance for quizzes (profile.json) | All rows kept, de-duplicated twin built |
| A4 | Preparation critic | Precision ≥ 50% is near the base rate; measure lift and attainable recall | Re-express the AQ4 limit (C13) | Accepted | 45.3% and 44.2% non-completion at the cut-offs | Capacity view; Milestone 4 metric plan |
| A5 | Preparation critic | Target-derived flags could reach the predictors | Role `target_derived`, kept out of feature views | Accepted | Flags defined from final_result | V14 and V13 forbid them |
| A6 | Preparation critic | CMA lateness of unclear meaning drives the rule | Rule uses TMA lateness; CMA variant kept | Accepted | 47.2% of CMA vs 16.8% of TMA submissions late | `early_sign_rule`, `early_sign_rule_cma` (C10) |
| A7 | Feature engineering ideator | Recency, trend, pre-start window, clicks by resource type, early submissions; first-click day | Add all but first-click day as an extended set | Accepted in part | Pre-start clicks already carried by `clicks_pre`, `clicks_pre14` | 10 extended predictors |
| A8 | Preparation critic | Report the outcome rate of test enrolments of students seen in 2013 before modelling | Report only their count now | Accepted in part | Looking at test outcomes while preparing breaks the independent test (brief section 11) | 1,962 flagged, outcome left to Milestone 4 |
| A9 | Preparation critic (leakage audit) | 93 Withdrawn without a day sit in the test views as easy positives | Evaluation flag; metrics with and without | Accepted | 89 of 92 at day 13 are test rows; 41% have no early click | `eval_withdrawal_day_unknown` |
| A10 | Preparation critic (leakage audit) | Tasks due before registration counted as missed; V13 could not fail; a V14 line commented out | Fix the formula and both checks | Accepted | 6 tasks at day 27; code reading | Pipeline rerun: 22 of 22 checks PASS |
| A11 | Code assistant | Draft every script of the package (understanding, profile, preparation, transforms, validation, notebooks) | Keep after review, tests and independent recounts | Accepted | 13 of 13 numbers equal a separate recount by the exploration code; 9 fixture tests; 6 features recomputed from raw for every row, 0 mismatches; one row recounted by hand from the raw files | Package `src/`, `tests/` |
| A12 | Documentation assistant | Draft the dictionary, lineage, README and transformation log | Generated from code and checked | Accepted | V14: every prepared column documented with role and source | `data_dictionary.md`, `lineage.md` |
| A13 | Synthetic-data assistant | Small invented enrolments to test the formulas | Level A fixtures only, labelled, never in a view or a finding | Accepted | Brief section 8.3, level A | `tests/test_features.py` |

The preparation critic received the following instruction and read only the issue log, the matrix, the specifications, the fit log and the profile. In both instructions, files are named by their place in the Prepared Data Package.

> You are a critical reviewer of a data preparation plan for an education analytics project (course completion and
> early warning on the Open University Learning Analytics Dataset, OULAD). Read only these files:
> `data/metadata/quality_issue_log.md`,
> `data/metadata/decision_matrix.md`, `feature_spec.md`, `split_spec.md`,
> the AQ–Data Fit Decision Log (Section 4) and, for numbers, `data/metadata/profile.json`.
> Challenge the plan as a sceptical senior analyst would: (1) imputation, de-duplication, outlier and encoding
> choices; (2) any feature that could leak information from after its cut-off or from the test runs; (3) the split
> and the handling of students seen in both years; (4) the population rules and denominators; (5) whether any
> decision is cleaning by habit rather than tied to an analytical question; (6) features that are missing but
> computable from the real fields at the cut-off. Do not invent facts about the data: cite the file and key for
> every number you use, and say "not verifiable from these files" otherwise. Return at most 12 numbered critiques,
> each with: the issue, why it matters (which AQ), a concrete recommendation, and severity (high / medium / low).

Table A.16 records the decision on each of its 12 critiques.

**Table A.16. Decisions on the preparation critic's critiques**

| # | Critique (short) | Decision | Evidence used to verify | Effect on the pipeline |
| :---- | :---- | :---- | :---- | :---- |
| 1 | AQ4 precision ≥ 50% sits near the base rate (45.3% at day 13, 44.2% at day 27; 24.9–58.3% by run) | Accepted | P.outcome; capacity lists of 3 or 5 per group of 20 cap recall | AQ4 and AQ3 list quality measured as lift over the run's base rate and as recall against the most a list of that size can reach, with a random list and the early-sign rule as baselines (Change Log C13); `capacity_by_run` carries the list sizes |
| 2 | Target-derived flags and `registration_missing` could reach the predictors | Accepted | `withdrawal_day_missing` and `unregistered_not_withdrawn` are functions of final_result; 39 of 45 missing registration days are Withdrawn (P.missing) | The two flags exist only in `enrolment` with role `target_derived`; `registration_missing` moved to the extended set; V14 fails if a target-derived column appears in a feature view |
| 3 | The rule is an inactivity rule at day 13 | Accepted | A task is due by day 13 in 1 of 22 runs (P.temporal) | Rule components stored (`rule_missed`, `rule_tma_late`, `inactive_last7`); firing rate of each component per run and cut-off in the validation summary; the day-13 rule is named an activity rule |
| 4 | Repeat and concurrent students are dependent units | Accepted in part | `student_in_training_runs` and `concurrent_runs` exist in the views | Count of flagged test enrolments reported (no test outcome is inspected, so the requested outcome rate of this group is not computed now); Milestone 4 protocol: folds grouped by run and student inside 2013, bootstrap intervals clustered by student; lists are drawn per module run, so a student in two modules can appear on two tutors' lists |
| 5 | CCC unseen in training; 9 tuning groups | Accepted | `paired_run` = false for CCC-B, CCC-J, EEE-B, GGG-B | Reported as a new-module test; leave-one-run-out folds inside 2013 with fold variance (Milestone 4) |
| 6 | Duplicate share may shift between years | Accepted | Extra-row share 6.82% in 2013 runs, 7.87% in 2014 runs (P.duplicates) | Raw clicks are the declared primary measure; the `_dedup` twin is a sensitivity variant chosen, if at all, on 2013 folds before any 2014 evaluation; the run-relative ratio absorbs run-level differences |
| 7 | CMA score almost empty at day 13; filling unspecified | Accepted | Earliest task due on days 12–61 by run (P.temporal) | `cma_marked_c` (count of marks known) added; the score stays null without filling; its coverage per cut-off is reported; Milestone 4 uses it only if at least 10% of training rows carry it |
| 8 | Computable features missing | Accepted in part | Fields exist before the cut-off | Added as an extended set: recency (`days_since_last_click`), trend (`trend_last_week`), fixed pre-start window (`clicks_pre14`), clicks by the four busiest resource types, tasks submitted before their due day; the day of first click was not added, because `clicks_pre` and `clicks_pre14` already carry pre-start engagement |
| 9 | Linear copies among click features | Accepted | At both cut-offs the last seven days are the last calendar week | `clicks_last7` kept only as the source of `inactive_last7`, not as a predictor; the dictionary states that `clicks_0c` = sum of the weekly columns, so linear models use one or the other |
| 10 | CMA lateness has no documented meaning | Accepted | 32,991 of 69,956 CMA submissions after the due day against 16,320 of 97,088 TMA (P.validity) | Early-sign rule = a task missed, or a TMA late, or no activity in the last seven days; `early_sign_rule_cma` adds CMA lateness as a sensitivity variant; Change Log C10 restated |
| 11 | Small groups and imd "Missing" | Accepted in part | 93 + 45 enrolments flagged; imd "Missing" concentrated in two regions | KPI reported with and without the 138 flagged enrolments in the validation summary; "Missing" is its own row in the fairness audit; no exclusion |
| 12 | Habit transforms and zero median | Accepted | Ordered categories would be lost by one-hot encoding | Run-relative ratio is (clicks + 1) ÷ (run median + 1); model-ready matrices are for linear models only: ordered categories as ordinal codes with a missing indicator, nominal ones one-hot, counts log1p then standardised; tree models use the prepared views; the logging-gap flag stays in `student_week` only |

The leakage auditor received the following instruction and could query the prepared and raw files without changing them.

> You are an independent auditor of data leakage in a preparation pipeline for early prediction of course
> non-completion on OULAD (prediction points: end of day 13 and end of day 27 of each module run; training runs 2013,
> test runs 2014). Read `src/prepare_data.py`, `fit_transforms.py`, `validate_prepared.py`,
> `dictionary.py`, `common.py` and `data/metadata/feature_spec.md`, `split_spec.md`,
> `decision_matrix.md`. You may run read-only Python with Python (polars) on
> `data/processed/*.parquet` and `data/raw/*.csv`, writing
> nothing except your report. Look for: (1) any feature that uses information dated after its cut-off or derived from
> the outcome; (2) any population rule that uses future information (who is in a cut-off view); (3) any statistic
> computed across runs or with test rows that a model would learn from; (4) train–test contamination in
> fit_transforms.py; (5) identifiers or columns that could act as a proxy for the target; (6) bugs in the feature
> formulas (off-by-one days or weeks, banked results, exams, duplicates). For every finding give the file and line
> or the query and its result, the risk, and a fix, with severity (high / medium / low). Do not report a finding you
> could not support with code or a query result. At most 10 findings.

Table A.17 records the evidence and the effect of each of its 8 findings, all of which were accepted.

**Table A.17. Decisions on the leakage auditor's findings**

| # | Finding (severity) | Evidence used to verify | Effect on the pipeline |
| :---- | :---- | :---- | :---- |
| F1 | 93 Withdrawn enrolments without a withdrawal day stay in both cut-off views as positives, 89 of the 92 at day 13 in test runs (medium) | `eval_withdrawal_day_unknown` counts 92 (day 13) and 93 (day 27), 89 and 90 in test runs | Evaluation flag added to the feature views (role evaluation, never a predictor); Milestone 4 reports test metrics with and without these rows |
| F2 | Feature views hold id_student, final_result and non_completion, and tree models were told to use the views as they are (medium) | Columns listed in the view schema | `predictor_sets.json` names the only model inputs for every model family; `fit_transforms.py` docstring corrected |
| F3 | Missing indicator of registration_lead duplicates the extended flag registration_missing in the primary matrix (low) | 5 training rows, all non-completers | No indicator for registration_lead; the flag stays an extended predictor |
| F4 | Existence of a missing indicator was decided with test rows (low) | `fit()` read df instead of the training rows | Indicators decided on training rows; training medians computed for every numeric column |
| F5 | Tasks due before a late registrant's registration counted as missed at day 27 (low) | 6 such tasks at day 27 | A task counts only if due on or after the registration day; validator recount and fixture test changed accordingly |
| F6 | No-click students received the training median (1 day) for days_since_last_click (low) | Median 1.0 in `transform_params.json` | Value c + 1 for students with no click in days 0…c, set in the view |
| F7 | V13 could never fail, because the data were filtered before the check (low) | Code reading | V13 recounts clicks without any cut-off and requires the pipeline to differ exactly where later clicks exist (26,755 and 25,663 rows) |
| F8 | V14 check of extended predictors was commented out by a misplaced comment (low) | `validate_prepared.py` line 170 | Line split; V14 checks both predictor lists |

**Further decisions and reflection.**

The interpreter's suggestion on the OU policy of 2025 was also accepted in part: its reading of the 2025 policy gave a usable rule for
CMA marks, which appear within seven days, but its rule that a CMA cannot be submitted late does not hold in data
where 32,991 CMA submissions are late, so it was not applied.

**Reflection.** The reviews were most useful where the AI critic had to argue from the data rather than from general
advice: the duplicate test, the base-rate argument and the registration-day error each changed the pipeline, and each
was confirmed by a count before it was accepted.

**AI roles and verification.** The table below gives each of the seven roles, what AI did in it and how the result was
verified.

| Role (brief) | What AI did | How the result was verified |
| :---- | :---- | :---- |
| Data dictionary interpreter | Read the data descriptor, the OU's assessment policy and the IMD documentation | Each fact kept only with a verbatim quotation; the 2025 rule that a CMA cannot be late tested on the data and not applied |
| EDA and quality checklist partner | Proposed a test of whether duplicate click rows are copies | Test run on the data: 31.5% equal counts against 24.0% by chance |
| Code assistant | Drafted every script of the package | 13 figures equal to an independent recount; 9 unit tests; 6 features recomputed for every row without a difference; one row recounted by hand |
| Preparation critic | Reviewed the plan in isolation (12 critiques) and audited leakage (8 findings) | Each critique checked on the data or the code before a decision |
| Feature engineering ideator | Proposed recency, trend, a pre-start window, clicks by resource type and early submissions | Each feature computable from real fields before the cut-off; added as the extended set |
| Documentation assistant | Drafted the dictionary, lineage, package guide and transformation log | Generated from the code; V14 fails if a column lacks an entry |
| Synthetic-data assistant | Wrote small labelled test enrolments | Level A of the brief's policy only; never in a view or a finding |

===== reports/milestone-3/report/12-06-validation-ledger.md @ 19d35a4 =====
## Appendix VI – Validation Ledger

Table A.18 lists the 22 checks of `src/validate_prepared.py` with their expected and observed values, from `data/metadata/validation_summary.json`.

**Table A.18. Validation ledger**

| ID | Check | Expected | Observed | Status |
| :---- | :---- | :---- | :---- | :---- |
| V01a | enrolment rows and outcome mix equal raw studentInfo | 32,593; Distinction 3,024, Fail 7,052, Pass 12,361, Withdrawn 10,156 | as expected | PASS |
| V01b | students | 28,785 | as expected | PASS |
| V01c | population sizes equal the profile (C09) | d14: 28,061; d13: 28,069; d27: 27,535 | as expected | PASS |
| V01d | non-completion count per feature view equals the profile | d13: 12,708; d27: 12,156 | as expected | PASS |
| V02 | missing values after = before (no imputation in views) | imd_band Missing: 1,111; date_registration: 45; TMA/CMA score null (submitted): 173 | as expected | PASS |
| V03 | key unique in every view | 0 duplicates | 0 in all 6 | PASS |
| V04a | enrolment clicks + clicks after withdrawal = raw clicks | 39,605,099 | 39,506,354 + 98,745 = 39,605,099 | PASS |
| V04b | student_week clicks = enrolment clicks | 39,506,354 | as expected | PASS |
| V04c | de-duplicated total ≤ raw total | dedup ≤ raw | 38,247,422 ≤ 39,506,354 | PASS |
| V05 | every category in its expected set | no other label | none | PASS |
| V06 | banked results carry no lateness and no missed status | 0 | as expected | PASS |
| V07 | ranges after = before (no capping) | score 0–100; credits 30–655 | score: 0–100; studied_credits: 30–655 | PASS |
| V08 | no student_week row after the withdrawal week | 0 | as expected | PASS |
| V09 | every logged join kept its rows | 25 joins, rows in = rows out | 25 | PASS |
| V10 | enrolments without any click row kept with 0 clicks | ≥ 3,365 | 3,554 | PASS |
| V11-d13 | 6 features recomputed from raw for all 28,069 rows (independent code) | 0 mismatches | 0 in all 6 | PASS |
| V11-d27 | 6 features recomputed from raw for all 27,535 rows (independent code) | 0 mismatches | 0 in all 6 | PASS |
| V12 | transform parameters identical with and without test rows, equal to the stored ones | identical | d13: identical, d27: identical | PASS |
| V13-d13 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 26,755 rows with later clicks; no forbidden column | 26,755 rows differ; no forbidden column | PASS |
| V13-d27 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 25,663 rows with later clicks; no forbidden column | 25,663 rows differ; no forbidden column | PASS |
| V14 | every column documented; predictor lists hold no audit, target or descriptive column | none | as expected | PASS |
| V15 | no run in both partitions; 2013 = train; student flag recomputed | 9 train, 13 test runs; 0 flag mismatches | train runs: 9; test runs: 13; test enrolments of students seen in 2013: 1,962; flag mismatches: 0 | PASS |

The validation also reports, without using any test outcome, the figures that the Milestone 4 plan relies on: the early-sign rule flags 20.2% of enrolled students at day 13 and 28.8% at day 27 (41.2% with CMA lateness); CMA marks known by the cut-off cover 1.4% and 5.2% of training rows; and completion in the day-14 population is 54.7%, or 54.9% without the 138 enrolments flagged for an unknown withdrawal day (93) or registration day (45). Rule rates per run and cut-off are in `rule_rates.csv`.

**Before-and-after checks explained.** The paragraphs below explain two results of Table 7.1 and the checks beyond it.

Two results need a word of explanation. The number of enrolments without a click row rises from 3,365 in the raw data
to 3,554 in the prepared view, because clicks after withdrawal are left out, so 189 students whose only activity came
after they unregistered now show none. The leakage check is built so that it can fail: if a feature used any click
after its cut-off, the feature would equal an unfiltered recount for every student, and the check would find no
difference for the students who clicked later.

Beyond the recount of every feature row, nine unit tests on synthetic test enrolments confirm each formula, and one
row was recounted by hand from the raw files: a TMA due on day 19 and submitted on day 24, with 168 clicks over 10
active days by day 27, matches the prepared view.

Table A.19 gives the state of each of the six conditions that the brief sets for starting Milestone 4.

**Table A.19. Entry conditions for Milestone 4**

| Condition | State |
| :---- | :---- |
| Core AQs have a prepared view with clear traceability | AQ1–AQ3 views ready; AQ4 ranking view ready, with the action part deferred (Appendix IV) |
| Target, features and dimensions stable | Defined in the feature specification and the data dictionary; 9 of 9 formula tests pass |
| Leakage and split defined for predictive tasks | Split and leakage specification; V11–V13 and V15 pass |
| Important quality issues handled or kept on purpose | DQ01–DQ19 each with a decision; residual risks stated (Section 7.3) |
| No synthetic data as evidence | Only labelled level A test enrolments |
| Prepared data reproducible from raw | Two runs from the raw files; 8 of 8 data files identical |
