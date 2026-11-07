## 2.3. Prediction Point and Leakage Risk

AQ3 must name its prediction points and use only what is known before them [1]. The baseline assumes about one
week of delay before data reach staff, so the data cut-offs fall at the end of week 2 and week 4, and the lists reach
staff in weeks 3 and 5. Table 2.3 sets out what each list may use and which fields would leak information from after
the cut-off.

**Table 2.3. Prediction points, allowed features and leakage risks**

| AQ predictive | Prediction point | Target | Features allowed before the point | Fields unavailable / leakage risk |
| :---- | :---- | :---- | :---- | :---- |
| AQ3, week-3 list | End of week 2 | Fail or withdrawal by the end of the semester | Activity to the end of week 2; submissions and their timeliness for tasks due by then; enrolment start date; background at enrolment | Final result; a withdrawal dated after the cut-off; scores and submissions of later tasks; later activity; exam results |
| AQ3, week-5 list | End of week 4 | Same | As above, to the end of week 4 | As above, after week 4; activity logged after a student's own withdrawal |
| Both lists | – | – | Course averages, scaling and encodings fitted on training semesters only, up to the cut-off; scores whose marks were known by the cut-off; study load and background as recorded at enrolment | Averages or scaling computed with test-semester students or with days after the cut-off; marks released after the cut-off; study load at semester end; background fields updated later |

Two further rules prevent counting a student's departure as a sign of it. In AQ1 and AQ2, a task counts as missed
only if it was due before the student's withdrawal date. In AQ3, students who had already left by a cut-off are not
counted as found by a list.
