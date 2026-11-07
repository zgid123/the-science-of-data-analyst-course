## 7.1. Updated Traceability Matrix

Table 7.1 links each question to the OULAD files and variables that serve it; every variable named exists in the
collected files, and coverage is Full, Partial or None as the brief defines [1].

**Table 7.1. Updated traceability from AQ to actual variables**

| AQ | Analytics type | Data requirement | Dataset / file | Actual variables | Coverage | Gap / action |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Outcome by module, module run and time; first missed task for students who passed and for those who did not | OULAD: studentInfo, studentRegistration, courses, assessments, studentAssessment | final_result, code_module, code_presentation, date_registration, date_unregistration, module_presentation_length, assessment_type, assessments.date, date_submitted | Partial | Only BBB, DDD and FFF have all four module runs; no delivery mode or year of study, so those comparisons are dropped (C04) |
| AQ2 | Diagnostic | Signs in weeks 1–4 against later outcome | AQ1 files + studentVle, vle | AQ1 variables + sum_click, studentVle.date, id_site, activity_type; concurrent module runs through id_student | Partial | Task signs only where a task is due by week 4 (16 of 22 module runs); no attendance (C05) |
| AQ3 | Predictive | Fail or withdrawal; features by the cut-off; later run for testing | As AQ2 | final_result; date_unregistration for who is still enrolled; sum_click by studentVle.date and date_submitted up to day 13 or 27; num_of_prev_attempts, studied_credits; imd_band, disability for group checks | Partial | Week-3 list from activity only (C06); testing on the 2014 runs of the 9 module and start-month pairs that have both a 2013 and a 2014 run (C07); groups by deprivation and disability (C04) |
| AQ4 | Prescriptive | Ranking within capacity; contacts and outcomes | AQ3 outputs | none for contacts or capacity | Partial (ranking) / None (action) | Ranking simulated under assumed capacity; no claim on the effect of contact; contact record kept as a pilot requirement (C08) |

The time frame of the questions maps onto OULAD as follows. Days are counted from the start of each module run, so
week n spans days 7(n−1) to 7n−1, and the cut-offs of the week-3 and week-5 lists fall on day 13 and day 27 (C02).
The add-drop period corresponds to the Open University's registration window, which closes two weeks after the start
[3]; the KPI denominator is therefore the 28,119 enrolments still registered on day 14 (C03). Appendix V extends the chain
to the Business Goal, measures and decisions, as the brief's deliverable B requires [1] (Table A.10).
