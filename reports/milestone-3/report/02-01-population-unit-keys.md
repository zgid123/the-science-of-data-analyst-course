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
