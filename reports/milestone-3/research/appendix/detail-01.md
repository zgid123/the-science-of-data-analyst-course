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
