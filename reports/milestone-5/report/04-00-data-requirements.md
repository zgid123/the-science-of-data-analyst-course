# 4. Data Requirements and Dataset Selection

We stated the requirements in the terms of the university's records before searching for data, so that the data fit
the questions rather than the other way round. Every question uses one student's enrolment in one course and semester,
the population enrolled after add-drop, and the final result with a dated withdrawal; each list may use only data
recorded up to its cut-off, one week before the list, so every event needs a timestamp. Table 4.1 is the AQ–Data
Requirement Matrix (Table A.9, Appendix IV, adds the source systems). Six must-have gates followed from it: a dated
outcome (G1), dated tasks (G2a) and activity (G2b), at least three time-ordered runs (G3), an open licence with
provenance (G4) and a persistent anonymised identifier (G5); the contact record was declared a gap before the search.

**Table 4.1. AQ–Data Requirement Matrix**

| AQ | Outcome or measure | Required variables | Time and grain | Decision point |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Pass, fail or withdrawal; first missed week | Identifiers; enrolment dates; final result; dated withdrawal; task dates | Four semesters; week | D2, semester end |
| AQ2 | Difference in non-completion with and without each sign | AQ1 variables; dated activity; missed and late tasks | Weeks 1–4; day | D2; reasons in D1 |
| AQ3 | Non-completion by the end of the semester | Timestamped activity and submissions; background at enrolment | Weeks 2 and 4; runs in time order | D1, weeks 3 and 5 |
| AQ4 | Recall within capacity; outcome after contact | AQ3 output; capacity (assumed); contact record (to create) | Each review point | D1 |
