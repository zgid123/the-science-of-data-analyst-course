## 3.1. Shape, Keys, Duplicates and Joins

Every table holds the number of rows its documentation states [2], and the six keyed tables have no duplicate key;
the run length is stored as module_presentation_length, not length, and withdrawal as "Withdrawn", not "Withdrawal"
[2]. The click table differs in grain: documented as interactions with a resource on a day [7], it holds several
rows for 1,614,505 student-resource-days, 1,179,074 of them with different counts, so clicks are summed by enrolment
and day before use (DQ02). In addition, 787,170 rows (7.39%) repeat another row exactly, 3.19% of all clicks. If they
were copies, pairs of rows for the same student, resource and day would share their click count far more often than
chance; they do so in 31.5% of cases against 24.0% expected by chance, more often for forums and content pages and
less often for quizzes, so the evidence points both ways and the cause cannot be decided; every row is kept and a de-duplicated twin of each click
feature supports a sensitivity check (DQ01). Joins need care as well: submissions joined to click rows would multiply
to 89,347,197 rows, and an inner join with activity would drop the 3,365 enrolments without clicks, students who left
before the start having no activity rows [8]; tables are therefore aggregated first and joined from the enrolment
table (DQ17).
