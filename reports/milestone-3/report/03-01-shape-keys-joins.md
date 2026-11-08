## 3.1. Shape, Keys, Duplicates and Joins

Every table holds the number of rows that its documentation states [2], and the six tables with a key have no
duplicate key; two stored names differ from the documentation, module_presentation_length for the run length and
"Withdrawn" for "Withdrawal", without changing any value. The click table differs in grain, the level of detail that
one row represents: documented as one student's interactions with a resource on a day [7], it holds several rows for
1,614,505 student-resource-days, so clicks are summed by enrolment and day before any use (DQ02). In addition, 787,170
rows (7.39%) repeat another row exactly, 3.19% of all clicks. If these rows were only separate visits that
happen to carry the same count, two rows of the same student, resource and day would carry equal counts as often as
chance gives from each resource's own counts, 24.0% of such pairs; they do so in 31.5%, more often for forums and
content pages and less often for quizzes. Some rows may therefore be copies made by the logging system and others
real repeated visits, and the data cannot tell which, so every row is kept and a de-duplicated twin of each click feature allows a sensitivity check (DQ01).

Joins need care too: a
direct join of submissions with click rows would return 89,347,197 rows, and an inner join, which keeps only rows
found in both tables, would drop the 3,365 enrolments without any click; tables are therefore summed to the enrolment
and joined to the enrolment table with left joins, which keep every enrolment (DQ17). Appendix I gives the full
evidence of this section.
