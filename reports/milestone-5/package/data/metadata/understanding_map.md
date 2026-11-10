# Dataset Understanding Map (Task 1)

Generated 2026-11-10T17:57:31Z by `src/01_understand.py` from `data/raw/`. Every key and relationship below is a computed check; full results in `understanding.json`.

| File/Table | Rows | Unit of Analysis | Primary Key | Foreign Key | Main Variables | Time Field | Role in AQ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses.csv | 22 | module run (module × presentation) | code_module, code_presentation (unique) | – | module_presentation_length | module_presentation_length (days) | Run length; run end for exam due days (AQ1–AQ3) |
| assessments.csv | 206 | assessment of a module run | id_assessment (unique) | code_module, code_presentation → courses | assessment_type, weight | date (due day) | Due days of tasks: missed and late tasks (AQ1, AQ2), task-based features and baseline rule (AQ3) |
| vle.csv | 6,364 | learning-platform resource (site) of a module run | id_site (unique) | code_module, code_presentation → courses | activity_type | week_from, week_to (planned weeks) | Resource type of clicks (AQ2 activity mix); planned weeks rarely filled |
| studentInfo.csv | 32,593 | enrolment (student × module run) | code_module, code_presentation, id_student (unique) | code_module, code_presentation → courses | final_result, gender, region, highest_education, imd_band, age_band, num_of_prev_attempts, studied_credits, disability | – (final_result observed at run end) | Outcome and target (AQ1–AQ3); background and audit attributes (AQ2, AQ3, AQ4 fairness) |
| studentRegistration.csv | 32,593 | enrolment (student × module run) | code_module, code_presentation, id_student (unique) | code_module, code_presentation, id_student → studentInfo (1–1) | date_registration, date_unregistration | date_registration, date_unregistration (days) | KPI denominator (registered on day 14), withdrawal day, population at each cut-off |
| studentAssessment.csv | 173,912 | submission (student × assessment) | id_assessment, id_student (unique) | id_assessment → assessments; id_student (+ run of the assessment) → studentInfo | score, is_banked | date_submitted (day) | Submission and lateness (AQ1, AQ2, AQ3) |
| studentVle.csv | 10,655,280 | logged interaction record (student × resource × day; several rows per day possible) | none documented (no key) | id_site → vle; code_module, code_presentation, id_student → studentInfo | sum_click | date (day of interaction) | Platform activity by day and week (AQ2, AQ3) |

## Relationships

| Relationship | Result |
| :---- | :---- |
| courses→assessments | orphan_rows=0, parents_without_children=0, children_per_parent_min=5, children_per_parent_max=14 |
| courses→vle | orphan_rows=0, parents_without_children=0, children_per_parent_min=106, children_per_parent_max=529 |
| courses→studentInfo | orphan_rows=0, parents_without_children=0, children_per_parent_min=365, children_per_parent_max=2498 |
| studentInfo↔studentRegistration | info_without_registration=0, registration_without_info=0 |
| assessments→studentAssessment | orphan_rows=0, parents_without_children=18, children_per_parent_min=278, children_per_parent_max=1917 |
| studentInfo→studentAssessment (enrolment) | orphan_rows=0, enrolments_with_submissions=25843 |
| vle→studentVle | orphan_sites=0, sites_never_used=96 |
| studentInfo→studentVle (enrolment) | orphan_enrolments=0, enrolments_with_activity=29228, enrolments_without_activity=3365 |
