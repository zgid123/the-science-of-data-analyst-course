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
