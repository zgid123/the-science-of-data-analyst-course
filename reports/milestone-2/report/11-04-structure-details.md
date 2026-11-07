## Appendix IV – Structural Verification Details

Table A.6 gives, for each table, the headers found, the types inferred from the text values and the missing cells; Table A.7 lists the counts that settle the selection conditions.

**Table A.6. Headers, inferred types and missing values**

| Table | Headers and inferred types | Missing cells |
| :---- | :---- | :---- |
| courses | code_module (text), code_presentation (text), module_presentation_length (integer) | none |
| assessments | code_module (text), code_presentation (text), id_assessment (integer), assessment_type (text), date (integer), weight (decimal) | date 11 |
| vle | id_site (integer), code_module (text), code_presentation (text), activity_type (text), week_from (integer), week_to (integer) | week_from 5,243, week_to 5,243 |
| studentInfo | code_module (text), code_presentation (text), id_student (integer), gender (text), region (text), highest_education (text), imd_band (text), age_band (text), num_of_prev_attempts (integer), studied_credits (integer), disability (text), final_result (text) | imd_band 1,111 |
| studentRegistration | code_module (text), code_presentation (text), id_student (integer), date_registration (integer), date_unregistration (integer) | date_registration 45, date_unregistration 22,521 |
| studentAssessment | id_assessment (integer), id_student (integer), date_submitted (integer), is_banked (integer), score (integer) | score 173 |
| studentVle | code_module (text), code_presentation (text), id_student (integer), id_site (integer), date (integer), sum_click (integer) | none |

Table A.7 gives the counts that decide the selection conditions G1, G3 and G5, the timing of the first tasks and the KPI denominator.

**Table A.7. Counts behind the selection conditions and the denominator**

| Check | Result |
| :---- | :---- |
| Result values | Pass 12,361, Withdrawn 10,156, Fail 7,052, Distinction 3,024 |
| Withdrawn with / without an unregistration day; other results with one | 10,063 / 93 ; 9 |
| Students; students in more than one run | 28,785; 3,538 |
| Same-module repeats; repeats with a higher attempt count | 1,309; 1,309 |
| Runs per module | AAA: 2013J, 2014J; BBB: 2013B, 2013J, 2014B, 2014J; CCC: 2014B, 2014J; DDD: 2013B, 2013J, 2014B, 2014J; EEE: 2013J, 2014B, 2014J; FFF: 2013B, 2013J, 2014B, 2014J; GGG: 2013J, 2014B, 2014J |
| Runs with a non-exam task due by day 13 / day 27 (of 22) | 1 / 16 |
| First non-exam task due day per run | AAA-2013J 19, AAA-2014J 19, BBB-2013B 19, BBB-2013J 19, BBB-2014B 12, BBB-2014J 19, CCC-2014B 18, CCC-2014J 18, DDD-2013B 23, DDD-2013J 25, DDD-2014B 25, DDD-2014J 20, EEE-2013J 33, EEE-2014B 33, EEE-2014J 33, FFF-2013B 19, FFF-2013J 19, FFF-2014B 24, FFF-2014J 24, GGG-2013J 61, GGG-2014B 61, GGG-2014J 61 |
| Exams without a due day | 11 |
| Unregistered on or before day 0; registered after day 14; registration day missing | 3,097; 58; 45 |
| Still registered on day 14 | 28,119 |
| Rows without a parent (assessment, submission, click enrolment, click site) | 0, 0, 0, 0 |
