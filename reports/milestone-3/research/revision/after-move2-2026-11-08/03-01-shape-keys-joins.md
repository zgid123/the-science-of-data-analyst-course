## 3.1. Shape, Keys, Duplicates and Joins

**Shape and schema.** Every table holds the number of rows that its documentation states [2], and the six tables
with a key have no duplicate key. Two names differ from the documentation: the run length is stored as
module_presentation_length rather than length, and the withdrawn outcome as "Withdrawn" rather than "Withdrawal"
[2]. Neither changes a value, and the pipeline uses the names as stored.

**Grain of the click table.** The click table differs from its documentation in grain, the level of detail that one
row represents. It is documented as the interactions of a student with a resource on a day [7], which would give one
row per student, resource and day. Instead, 1,614,505 student-resource-days hold several rows, and 1,179,074 of them
hold different click counts in their rows, up to ten rows in one group. A row is therefore a record of the logging
system rather than a day, so clicks are summed by enrolment and day before any use, and activity is counted in active
days rather than rows (DQ02).

**Exact duplicates.** In addition, 787,170 click rows (7.39%) repeat another row in every column; collapsing them
would remove 3.19% of all clicks. Two explanations are possible: the duplicates are copies made by the logging system,
or they are separate visits that happen to carry the same count. If they were copies, two rows of the same student,
resource and day would carry equal click counts far more often than chance alone would produce. They do so in 31.5%
of two-row groups, against 24.0% expected by chance from each resource's own counts; the excess appears for forums
and content pages, while quizzes, wikis and questionnaires fall below chance (Appendix I, Table A.6). The evidence
points both ways, so the cause cannot be decided from the data. Every row is kept, which is the table's own grain, and
a de-duplicated twin of each click feature lets Milestone 4 test whether the choice matters (DQ01).

**Joins.** Joining the tables needs care for two reasons. First, a direct join of submissions with click rows on the
student would multiply rows: it returns 89,347,197 rows, because every submission is paired with every click record
of the same student. Second, an inner join with activity, which keeps only rows that appear in both tables, would drop
the 3,365 enrolments without any click row; most of these students left before the run began and so have no activity
rows [8], and dropping them would remove withdrawals from the descriptive rates. Tables are therefore summed to the
enrolment first and then joined to the enrolment table with left joins, which keep every enrolment and record no
activity as zero (DQ17).
