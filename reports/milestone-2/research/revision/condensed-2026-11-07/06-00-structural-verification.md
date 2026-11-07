# 6. Initial Structural Verification

With the files collected, a structural check confirmed that they can be read and match their documentation, without
cleaning or exploring them [1]. Every table was read as text, so no value was converted, and its rows, columns,
keys, types, missing values and time fields were compared with the data dictionary copied from the descriptor. Table 6.1 summarises the result; Appendix IV gives the full output.

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

All links between tables hold: no submission, assessment, click or site record lacks its parent row. Three
differences between the documentation and the files were found. The run-length column is named
module_presentation_length, not length as documented [3]; the outcome value for withdrawn students is "Withdrawn"
in the file, while the descriptor calls it Withdrawal [3]; and the click table has no key, so 787,170 identical rows
cannot be told apart from repeated visits. In addition, the descriptor's rule that only withdrawn students carry an
unregistration day [3] has exceptions: 93 Withdrawn enrolments lack the day, and 9 others carry one.

The check also settled the conditions of the selection. The result values separate pass and distinction from fail and
withdrawal, and 10,063 of 10,156 withdrawals are dated, so G1 holds. Of 28,785 students, 3,538 appear in more than
one module run. In all 1,309 repeats of the same module, the count of previous attempts rises. That count
can only rise if the same identifier marks the same student in each run, so the identifier persists and G5 holds. G3 holds only in part. BBB, DDD and FFF have four module runs, EEE and GGG three, and AAA and
CCC two. With February and October runs kept apart, each module has at most one earlier and one later run of the same
start month. A task other than the exam falls due by the end of week 2 in 1 of 22 module runs, and by the end of
week 4 in 16. Finally, 3,097 enrolments ended on or before day 0, and 28,119 were still registered on day 14; these form the KPI
denominator (Section 7.1). Negative days fall before the start of a module run.
