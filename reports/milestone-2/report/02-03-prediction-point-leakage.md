## 2.3. Prediction Point and Leakage Risk

**Prediction points.** A predictive question must name its prediction point, the moment at which a prediction is
made, and may use only information known before it [1]. The baseline assumes about one week of delay before data reach
staff, so the data cut-offs fall at the end of week 2 and the end of week 4, and the lists reach staff in weeks 3
and 5. Leakage is the use of information that is not yet known at the prediction point; it makes a method look more
accurate on past data than it can be in practice. Table 2.3 sets out, for each list, the target, the features it may
use and the fields that would leak information from after the cut-off.

**Table 2.3. Prediction points, allowed features and leakage risks**

| AQ predictive | Prediction point | Target | Features allowed before the point | Fields unavailable / leakage risk |
| :---- | :---- | :---- | :---- | :---- |
| AQ3, week-3 list | End of week 2 | Fail or withdrawal by the end of the semester | Activity to the end of week 2; submissions and their timeliness for tasks due by then; enrolment start date; background at enrolment | Final result; a withdrawal dated after the cut-off; scores and submissions of later tasks; later activity; exam results |
| AQ3, week-5 list | End of week 4 | Same | As above, to the end of week 4 | As above, after week 4; activity logged after a student's own withdrawal |
| Both lists | – | – | Course averages, scaling and encodings fitted on training semesters only, up to the cut-off; scores whose marks were known by the cut-off; study load and background as recorded at enrolment | Averages or scaling computed with test-semester students or with days after the cut-off; marks released after the cut-off; study load at the end of the semester; background fields updated later |

**Two further rules.** Two rules prevent counting a student's departure as a sign of it. In AQ1 and AQ2, a task counts
as missed only if it was due before the student's withdrawal date; otherwise every student who withdrew early would
appear to have missed every later task. In AQ3, students who had already left by a cut-off are not counted as found by
a list, because staff could no longer contact them.
