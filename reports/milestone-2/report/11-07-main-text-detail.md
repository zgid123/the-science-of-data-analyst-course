## Appendix VII – Supporting Detail for the Main Text

This appendix gives the detail behind several sections of the main text, item by item in the order of the parts: the
reasons and steps that the main text states in short, each next to the section it supports.

### 1. Baseline Freeze, Scope and Controlled Revisions

This item gives the detail behind Sections 1.1 and 1.2: why and how the Milestone 1 baseline was frozen, how the work
of this milestone follows the brief's steps, and what each of the eight controlled revisions changes.

**Why the baseline is frozen.** The brief requires us to start this milestone from our proposal, not from a
dataset: the questions decide what data are needed, and the data may not quietly change the questions [1]. Before any
dataset was examined, we therefore froze the Milestone 1 baseline. Its goal, measures, questions, data needs and
decisions were copied word for word into a baseline record, and a checksum (a fingerprint of a file's exact content)
was recorded for every source file, so that any later difference between the proposal and this report is visible and
must be explained (Appendix V). Every change that the data made necessary is recorded in a Controlled Change Log, the
brief's term for a list of changes with their reasons [1].

**What this milestone does.** Building on the frozen baseline, this milestone answers the two questions that the brief
sets: which data the four questions need, and whether the open dataset that we collect actually provides them
[1]. Its work follows the brief's steps. Section 2 turns each question into a data requirement. Section 3 describes
the search for candidate open datasets, and Section 4 scores the candidates and selects one. Section 5 records how the
selected dataset was collected so that anyone can collect it again, and Section 6 checks that the collected files can
be read and match their documentation. Section 7 then maps every question to the real files and variables and states
how far each question can be answered. Sections 8 and 9 cover the risks and the use of generative
AI. Cleaning the data, filling in missing values, building features and training models are left to
later milestones, as the brief requires [1].

**What the data changed.** The selected dataset, OULAD, describes
distance-learning modules of a university in the UK, not the courses of a Vietnamese program, so the
questions cannot be answered on it exactly as the proposal framed them. We recorded eight controlled revisions,
C01 to C08, each with the old and the new content, the data evidence behind it and its effect on the questions, KPIs
and decisions. Four of them matter most. OULAD stands in for the university's courses in the analysis, while the
university's own records remain the target for the pilot (C01). A semester becomes a module run, one offering of a
module lasting eight to nine months, with time counted in days from the run's start (C02). Comparisons by delivery mode and year of study are dropped,
because OULAD holds neither (C04). The action part of AQ4, the record of contacts and their outcomes, stays a
requirement for the pilot, because no open dataset records it (C08). The other four adjust the KPI denominator to
OULAD's registration window (C03), drop the attendance sign (C05), build the week-3 list from activity alone and adapt the early-sign rule to OULAD's calendar (C06) and
test AQ3 on the 2014 runs of each module (C07). Section 7.2 explains every revision, and Appendix V (Table A.9) gives
the full Change Log.

### 2. Data Requirements by Analytics Level

This item gives the detail behind Section 2.2, where the four questions climb the analytics levels and each level needs
a different kind of evidence [1]. Table A.13 sets out the minimum data for each level and what that data can,
and cannot, show.

**Table A.13. Data requirements by analytics level**

| Level | AQ | Minimum data | What the data can show |
| :---- | :---- | :---- | :---- |
| Descriptive | AQ1 | Outcome; course and semester dimensions; dated tasks; the denominator of students enrolled after add-drop | Rates and the timing of first missed tasks |
| Diagnostic | AQ2 | AQ1 data, plus dated signs and comparison groups, with background attributes to check consistency across groups | Associations, not causes |
| Predictive | AQ3 | A labelled outcome; predictors timestamped before the prediction point; enough semesters to test on a later one | Accuracy on a later semester, for a list of fixed length |
| Prescriptive | AQ4 | Actions (contacts), constraints (capacity) and outcomes after the action | A ranking under constraints; without action and outcome data, no claim that a contact helps |

### 3. Rules for Every Hit and First Comparison of the Candidates

This item gives the detail behind Section 3: the rules applied to every dataset found, and what the summary of the seven
candidates in Table 3.1 already shows before the scoring of Section 4.

**Three rules for every hit.** Three rules applied to every dataset found, as the brief asks [1]. First, we read
the documentation and the license before judging the data. Second, a dataset found on Kaggle, a blog or another
copy was traced back to the provider that published it. Third, re-uploads without a known origin were rejected.

Table 3.1 already shows the main difference between the candidates. Only OULAD and the XuetangX data record when
students did things within a course, which AQ2 and AQ3 need, and only OULAD combines that timing with an outcome that
includes withdrawal and with dated assessments. Section 4 tests this impression against the gates and the brief's
criteria.

### 4. Reasons for Rejecting Each Candidate

This item gives the detail behind Section 4.2: why each candidate other than OULAD was rejected, with the facts from its
official page or descriptor behind the gates it fails in Table 4.1.

**Why not the others.** Every other candidate fails at least the outcome gate (G1) and the dated-task gate (G2a). UCI
697 labels students by their degree after three or four years, not by course, and holds only semester totals, so it
cannot show when within a course a student stopped [4], [5]. UCI 320 and UCI 856 describe secondary-school pupils or a
single questionnaire, with grades but no withdrawal and no dated tasks or activity [6], [7]. The XuetangX data record dated activity,
but their outcome is a yes-or-no dropout label without pass or fail, and they state no license [8]. HarvardX records
only the first and last activity of each learner and is not openly licensed [10], and xAPI-Edu-Data has no dated
records and is known only from a Kaggle listing [11].

### 5. Tables, Column Names and Linkage Evidence of OULAD

This item gives the detail behind Section 6: what each of the seven OULAD tables holds, what the column names used in
Table 6.1 and Section 7 mean, and the counts that show that a student's identifier persists across module runs.

The seven tables of OULAD divide the data as follows: courses lists the module runs; assessments lists their assessed tasks with due days; vle lists the pages of the VLE; studentInfo holds one row per enrolment of a student in a module run, with background attributes and the final result; studentRegistration holds the days on which each enrolment was registered and, where it happened, unregistered; studentAssessment holds each submitted task with its day and score; and studentVle holds each student's daily number of clicks on each page.

Several column names appear in Table 6.1 and in Section 7. In studentInfo, final_result is the outcome, in which Distinction is a pass with honours, so completion means Pass or Distinction; imd_band is the deprivation band of the student's home area; num_of_prev_attempts counts earlier attempts at the same module; and studied_credits is the credits the student was taking in that run. In studentVle, sum_click is the number of clicks on one page in one day, and id_site and activity_type identify the page and its kind. code_module and code_presentation name the module and the run, and assessment_type separates tutor-marked, computer-marked and exam tasks.

The student identifier persists across runs, so the linkage gate G5 holds. OULAD holds 32,593 enrolments of 28,785 students; 3,538 students appear in more than one module run, and in all 1,309 cases in which a student repeats the same module, the recorded count of previous attempts rises. That count can only rise if the same identifier marks the same student in each run.

### 6. Limits of AQ3 and the First Secondary KPI on OULAD

This item gives the detail behind Section 7.2: the three limits under which AQ3 is kept, and how the early-sign rule of
the first secondary KPI is measured on OULAD.

**AQ3.** The predictive question keeps its target, its two cut-offs and its test on a later module run, with three
limits. First, before the end of week 2 almost no module run has a task due, so the week-3 list rests on activity alone
(C06). Second, each module and start month has at most one earlier run to learn from, so the method trains on the 2013
runs and is tested on the 2014 runs of the 9 module and start-month pairs that have both (C07). Module CCC and the
February runs of EEE and GGG have no earlier run of the same start month, so they can test a method trained on other
runs but cannot train one of their own. Third, the comparison between first-year and later-year students cannot be
made, so it is replaced by a check across deprivation band and disability, which OULAD records (C04). In addition, OULAD records no date on which marks were released, so task scores are not
used as features for either list; only whether and when tasks were submitted is used, as Table 2.2 requires.

**The first secondary KPI.** The early-sign rule needs two or more missed or late tasks by the end of week 4, but two
tasks fall due by then in only 1 of the 22 module runs. On OULAD, the sign part of this KPI is therefore measured with
one missed or late task in the 16 runs that have a task due by the end of week 4, a stated deviation recorded with C06;
the rule as defined stays the measure for the university's courses, whose assessment calendars the pilot will check.
