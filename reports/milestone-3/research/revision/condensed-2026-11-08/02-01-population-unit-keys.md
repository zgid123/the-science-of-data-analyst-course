## 2.1. Population, Unit of Analysis and Keys

The population is the students enrolled in 22 runs of seven OU modules, four in science, technology, engineering and
mathematics and three in social sciences, taught by distance learning in the United Kingdom (UK) in 2013 and 2014
[2]: 32,593 enrolments of 28,785 students, of whom 3,538 enrolled in more than one run. A run code ends in B for a
February start and J for an October start, and the authors advise analysing B and J runs separately [2].

The unit of analysis is the enrolment, one student in one module run. Table 2.1, the Dataset Understanding Map,
gives each table's unit, keys, main variables, time field and role in the questions, each key checked on the data.

**Table 2.1. Dataset Understanding Map**

| File / table | Unit of analysis | Primary key | Foreign key | Main variables | Time field | Role in AQ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses (22) | module run | module + run | – | run length | run length | run end, start month |
| assessments (206) | assessment | id_assessment | → courses | type, weight | due day | tasks due (AQ1–AQ3) |
| vle (6,364) | resource | id_site | → courses | activity type | planned weeks | resource type (AQ2) |
| studentInfo (32,593) | enrolment | run + student | → courses | final_result, background | – | target; audit (AQ1–AQ4) |
| studentRegistration (32,593) | enrolment | run + student | → studentInfo (1–1) | registration and withdrawal days | days | populations, KPI |
| studentAssessment (173,912) | submission | assessment + student | → assessments, studentInfo | submission day, score | submission day | missed and late tasks |
| studentVle (10,655,280) | click record | none | → vle, studentInfo | clicks | interaction day | activity (AQ2, AQ3) |

The six keyed tables have unique keys, no child row lacks its parent (Appendix I, Figure A.1), and the click
table, which has no key, is examined in Section 3.1.

