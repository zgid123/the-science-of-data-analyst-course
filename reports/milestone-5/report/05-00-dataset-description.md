# 5. Dataset Description and Requirement–Data Fit

OULAD covers 22 runs of seven distance-learning modules of the Open University in the United Kingdom (UK), coded AAA to GGG, in 2013 and 2014; a
run is named by its year and start month, B for February and J for October, and days count from day 0, the start of the
run. Its seven tables are keyed by module, run and student, with task and page identifiers for submissions and
clicks, and every link between them holds; they record 32,593 enrolments of 28,785 students, each with a final
result: Pass 12,361, Withdrawn 10,156, Fail 7,052 and Distinction 3,024, so completion means Pass or Distinction
(Table A.12, Appendix V).
The 9 runs of 2013 cover six modules and 13,529 enrolments and the 13 runs of 2014 all seven modules and 19,064
enrolments, and a task other than the exam falls due by day 27 in only 16 of the 22 runs. Table 5.1 is a short data
dictionary of the key variables; the full dictionary travels with the Final Project Package.

**Table 5.1. Key variables of OULAD**

| Variable | Meaning | Questions |
| :---- | :---- | :---- |
| final_result | Pass, Distinction, Fail or Withdrawn | Target of all four |
| code_module, code_presentation | Module (AAA–GGG) and run (year and start month) | All four |
| date_registration, date_unregistration | Registration and unregistration day relative to day 0 | Populations; withdrawal timing |
| assessment_type, date; date_submitted | Kind of task (TMA, CMA, exam), due day and submission day | AQ1–AQ3 |
| sum_click, date | Clicks on one page in one day | AQ2, AQ3 |
| num_of_prev_attempts, studied_credits | Earlier attempts; credits studied in the run | AQ2, AQ3 |
| imd_band, disability | Deprivation band of the home area; declared disability | Group checks only |
