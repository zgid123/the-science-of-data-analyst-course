## 8.3. Updated Traceability

The brief asks for an updated traceability that runs from the Business Goal, the SMART Goal and the KPIs through each
question, its analytics type, the raw variables, the preparation and the prepared variables or views, to the decision
supported [1]. Every row serves the same Business Goal, to improve successful course completion by identifying
students who stop taking part early enough to support them within the semester. Table 8.4 gives the chain for each
question, with the raw variables named as OULAD columns and the prepared variables as columns of the prepared views.

**Table 8.4. Updated traceability**

| Goal / KPI | AQ | Analytics type | Raw variables | Preparation | Prepared variables / view | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Primary KPI: completion rate of students enrolled after the add-drop period (day 14) | AQ1 | Descriptive | final_result; registration and unregistration days; due days; submission days; banked flag | Enrolled-at-day rule (C09); tasks are TMA and CMA; banked results separated; missed only if due while enrolled | enrolment: completed, non_completion, enrolled_d14, first_missed_week, module, run, start month, year; assessment_due: status | D2: where support time goes; D3: whether to extend |
| Primary KPI; secondary KPI 1, sign part (C10) | AQ2 | Diagnostic | AQ1 variables plus click day, clicks, resource and resource type | Clicks summed by enrolment and day; truncated at withdrawal; duplicate rows kept with a twin; signs up to day 27 | features_d27: tasks_missed_c, tma_late_c, cma_late_c, inactive_last7, activity_ratio_run, clicks; enrolment: concurrent runs (2014) | D2; the reasons shown with each name in D1 |
| Secondary KPI 1, sign part | AQ3 | Predictive | AQ2 variables plus previous attempts, credits, highest education, registration day, CMA scores | Populations at days 13 and 27; events up to the cut-off only; CMA marks known seven days before; time split; transforms fitted on 2013 | features_d13, features_d27, early_sign_rule, split, paired_run, student_in_training_runs; model_ready | D1: who is listed in weeks 3 and 5 |
| Secondary KPI 2 and the contact part of KPI 1: pilot only (C08) | AQ4 (C11) | Prescriptive (ranking) | AQ3 inputs; gender, age band, disability, imd_band, region as audit columns | Capacity scenarios from tutor groups of about 20; list quality as lift and attainable recall (C13); fairness by imd_band, with "Missing" apart, and disability | capacity_by_run: enrolled and list sizes; audit columns in the feature views | D1: an ordered list within capacity; contact choice deferred |

Read along a row, the table shows that each decision rests on prepared variables that come from named raw fields
through stated preparation rules, and that the two decisions without data in OULAD, the choice of contact and the
follow-up rate, are marked as belonging to the pilot rather than filled with assumptions. Appendix IV gives the same
traceability with every prepared column and the full Controlled Change Log.
