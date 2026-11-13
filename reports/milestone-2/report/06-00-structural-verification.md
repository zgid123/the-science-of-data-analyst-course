# 6. Initial Structural Verification

**What the check does.** With the files collected, a structural check confirmed that they can be read and that they
match their documentation, without cleaning or exploring them, as the brief limits this step [1]. Every table was read
as text, so that no value was converted on reading, and its rows, columns, keys, types, missing values and time fields
were compared with the data dictionary copied from the descriptor. Every header matches the dictionary except the one
column name noted below; Appendix IV gives the headers, the types inferred from the values and the missing cells of
every table (Table A.6).

**How OULAD is organised.** OULAD describes seven modules, the Open University's equivalent of courses, coded AAA to
GGG. Each module is offered in several runs, which the dataset calls presentations. A run is named by its year and its
starting month: B for February and J for October, so that 2013J is the run that started in October 2013 [3]. Time is
counted in days from the start of each run, day 0, so a negative day falls before the run begins. Table 6.1 summarises the structure found in the seven
files, and Appendix VII (item 5) states what each table holds.

**Table 6.1. Structure of the collected OULAD files**

| File / table | Rows | Columns | Key(s) | Target / outcome | Time field | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses | 22 | 3 | module, module run; unique | – | run length 234–269 days | Column named module_presentation_length, documented as length |
| assessments | 206 | 6 | id_assessment; unique | – | due day (date) 12–261 | 11 exams without a due day |
| vle | 6,364 | 6 | id_site; unique | – | planned weeks 0–29 | Planned weeks missing for 5,243 sites |
| studentInfo | 32,593 | 12 | module, module run, student; unique | final_result: Pass 12,361; Withdrawn 10,156; Fail 7,052; Distinction 3,024 | – | imd_band missing for 1,111 |
| studentRegistration | 32,593 | 5 | module, module run, student; unique, 1:1 with studentInfo | – | registration day −322 to 167; unregistration day −365 to 444 | Unregistration empty for 22,521; registration missing for 45 |
| studentAssessment | 173,912 | 5 | assessment, student; unique | score 0–100 | submission day −11 to 608 | score missing for 173 |
| studentVle | 10,655,280 | 6 | none documented | – | interaction day −25 to 269 | 787,170 rows are exact duplicates |

**Outcome column.** In studentInfo, final_result is the outcome, in which Distinction is a pass with honours, so
completion means Pass or Distinction; Appendix VII (item 5) explains the other column names that appear in Table 6.1
and Section 7.

**Links between tables.** All links between tables hold: every submission, assessment, click record and page has its
parent row, so the tables can be joined for the same student, module run and task without losing records.

**Differences from the documentation.** The brief asks for every difference between the documentation and the files
to be recorded [1]; the check found three. The run-length column is named module_presentation_length, not length as
documented [3]. The outcome value for withdrawn students is "Withdrawn" in the file, while the descriptor calls it
Withdrawal [3]. The descriptor's rule that only withdrawn students carry an unregistration day [3] has exceptions: 93
Withdrawn enrolments lack the day, and 9 enrolments with another result carry one. One further issue is not a
difference, because the documentation gives the click table no key: its 787,170 identical rows cannot be told apart
from repeated visits on the same day.

**The three conditions of the selection.** The check settled the conditions on which OULAD was selected (Section
4.2). First, the result values separate pass and distinction from fail and withdrawal, and 10,063 of the 10,156
withdrawals are dated, so the outcome gate G1 holds. Second, the student identifier persists across runs, so the
linkage gate G5 holds (Appendix VII,
item 5). Third, the history gate G3 holds only in part. Modules BBB, DDD and FFF
have four runs, EEE and GGG three, and AAA and CCC two. With February and October runs kept apart, as the authors
advise, each module has at most one earlier and one later run of the same start month.

**Timing and the denominator.** Two further counts shape the questions. A task other than the final exam falls due by
the end of week 2 in only 1 of the 22 module runs, and by the end of week 4 in 16, so task-based signs are available
for the week-5 list but hardly for the week-3 list. Two such tasks fall due by the end of week 4 in only 1 run, which
matters for the early-sign rule of the first secondary KPI (Section 7.2). Of the 32,593 enrolments, 3,097 ended on or
before day 0, before the run began, and 1,377 ended between days 1 and 14; the remaining 28,119 enrolments, still
registered on day 14, form the KPI denominator (Section 7.1).
