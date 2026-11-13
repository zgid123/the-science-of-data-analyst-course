# Initial structural verification (Task 6)

Generated 2026-11-05T18:33:01Z by `src/verify_structure.py` from `data/raw/` (files read as text, nothing changed).

| File | Rows | Columns | Key(s) | Duplicate keys | Exact duplicate rows | Time fields (min–max day) | Headers not in the dictionary | Dictionary columns not in file |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses.csv | 22 | 3 | code_module, code_presentation | 0 | 0 | module_presentation_length 234–269 | module_presentation_length | length |
| assessments.csv | 206 | 6 | id_assessment | 0 | 0 | date 12–261 | – | – |
| vle.csv | 6,364 | 6 | id_site | 0 | 0 | week_from 0–29; week_to 0–29 | – | – |
| studentInfo.csv | 32,593 | 12 | code_module, code_presentation, id_student | 0 | 0 | – | – | – |
| studentRegistration.csv | 32,593 | 5 | code_module, code_presentation, id_student | 0 | 0 | date_registration -322–167; date_unregistration -365–444 | – | – |
| studentAssessment.csv | 173,912 | 5 | id_assessment, id_student | 0 | 0 | date_submitted -11–608 | – | – |
| studentVle.csv | 10,655,280 | 6 | none documented | – | 787,170 | date -25–269 | – | – |

## Missing values (empty cells, by column)

| File | Column | Missing |
| :---- | :---- | :---- |
| assessments.csv | date | 11 |
| vle.csv | week_from | 5,243 |
| vle.csv | week_to | 5,243 |
| studentInfo.csv | imd_band | 1,111 |
| studentRegistration.csv | date_registration | 45 |
| studentRegistration.csv | date_unregistration | 22,521 |
| studentAssessment.csv | score | 173 |

## Inferred types

- courses.csv: code_module (text), code_presentation (text), module_presentation_length (integer)
- assessments.csv: code_module (text), code_presentation (text), id_assessment (integer), assessment_type (text), date (integer), weight (decimal)
- vle.csv: id_site (integer), code_module (text), code_presentation (text), activity_type (text), week_from (integer), week_to (integer)
- studentInfo.csv: code_module (text), code_presentation (text), id_student (integer), gender (text), region (text), highest_education (text), imd_band (text), age_band (text), num_of_prev_attempts (integer), studied_credits (integer), disability (text), final_result (text)
- studentRegistration.csv: code_module (text), code_presentation (text), id_student (integer), date_registration (integer), date_unregistration (integer)
- studentAssessment.csv: id_assessment (integer), id_student (integer), date_submitted (integer), is_banked (integer), score (integer)
- studentVle.csv: code_module (text), code_presentation (text), id_student (integer), id_site (integer), date (integer), sum_click (integer)

## Selection conditions and denominators

```json
{
 "final_result_values": {
  "Pass": 12361,
  "Withdrawn": 10156,
  "Fail": 7052,
  "Distinction": 3024
 },
 "withdrawn_with_date": 10063,
 "withdrawn_without_date": 93,
 "date_but_not_withdrawn": 9,
 "studentInfo_registration_match": true,
 "runs_per_module": {
  "AAA-J": [
   "2013J",
   "2014J"
  ],
  "BBB-B": [
   "2013B",
   "2014B"
  ],
  "BBB-J": [
   "2013J",
   "2014J"
  ],
  "CCC-B": [
   "2014B"
  ],
  "CCC-J": [
   "2014J"
  ],
  "DDD-B": [
   "2013B",
   "2014B"
  ],
  "DDD-J": [
   "2013J",
   "2014J"
  ],
  "EEE-B": [
   "2014B"
  ],
  "EEE-J": [
   "2013J",
   "2014J"
  ],
  "FFF-B": [
   "2013B",
   "2014B"
  ],
  "FFF-J": [
   "2013J",
   "2014J"
  ],
  "GGG-B": [
   "2014B"
  ],
  "GGG-J": [
   "2013J",
   "2014J"
  ]
 },
 "runs_per_module_all": {
  "AAA": [
   "2013J",
   "2014J"
  ],
  "BBB": [
   "2013B",
   "2013J",
   "2014B",
   "2014J"
  ],
  "CCC": [
   "2014B",
   "2014J"
  ],
  "DDD": [
   "2013B",
   "2013J",
   "2014B",
   "2014J"
  ],
  "EEE": [
   "2013J",
   "2014B",
   "2014J"
  ],
  "FFF": [
   "2013B",
   "2013J",
   "2014B",
   "2014J"
  ],
  "GGG": [
   "2013J",
   "2014B",
   "2014J"
  ]
 },
 "students_total": 28785,
 "students_in_more_than_one_run": 3538,
 "same_module_repeats": 1309,
 "repeats_with_higher_attempt_counter": 1309,
 "first_task_due_day": {
  "AAA-2013J": 19,
  "AAA-2014J": 19,
  "BBB-2013B": 19,
  "BBB-2013J": 19,
  "BBB-2014B": 12,
  "BBB-2014J": 19,
  "CCC-2014B": 18,
  "CCC-2014J": 18,
  "DDD-2013B": 23,
  "DDD-2013J": 25,
  "DDD-2014B": 25,
  "DDD-2014J": 20,
  "EEE-2013J": 33,
  "EEE-2014B": 33,
  "EEE-2014J": 33,
  "FFF-2013B": 19,
  "FFF-2013J": 19,
  "FFF-2014B": 24,
  "FFF-2014J": 24,
  "GGG-2013J": 61,
  "GGG-2014B": 61,
  "GGG-2014J": 61
 },
 "runs_with_task_due_by_day_13": 1,
 "runs_with_task_due_by_day_27": 16,
 "exams_without_cutoff_day": 11,
 "unregistered_on_or_before_day_0": 3097,
 "registered_after_day_14": 58,
 "registration_day_missing": 45,
 "still_registered_at_day_14": 28119,
 "assessment_rows_without_parent": 0,
 "submissions_without_enrolment": 0,
 "click_rows_without_enrolment": 0,
 "click_rows_without_site": 0
}
```
