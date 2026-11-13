# OULAD data dictionary (as documented)

Column definitions copied from the data descriptor: Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University
Learning Analytics dataset. Scientific Data, 4, 170171, section "Data Records". Every day value is counted from the
start of the module presentation (day 0). `src/verify_structure.py` compares this list with the headers of the files
in `data/raw/` and reports every difference in `data/metadata/structure_report.md`.

| Table | Column (documented) | Definition (descriptor) |
| :---- | :---- | :---- |
| courses | code_module | code name of the module, which serves as the identifier |
| courses | code_presentation | code name of the presentation |
| courses | length | the length of the module-presentation in days from module start date to module end date |
| assessments | code_module | module identification code, to which the assessment belongs |
| assessments | code_presentation | presentation identification code, to which the assessment belongs |
| assessments | id_assessment | assessment identification number |
| assessments | assessment_type | type of assessment: Tutor Marked Assessment (TMA), Computer Marked Assessment (CMA), Final Exam (Exam) |
| assessments | date | information about the cut-off day of the assessment |
| assessments | weight | weight of the assessment; exams 100%, the sum of all other assessments also 100% |
| vle | id_site | identification number of the material |
| vle | code_module | identification code for the module |
| vle | code_presentation | identification code of the presentation |
| vle | activity_type | role associated with the module material |
| vle | week_from | week from which the material is planned to be used |
| vle | week_to | week until which the material is planned to be used |
| studentInfo | code_module | module identification code on which the student is registered |
| studentInfo | code_presentation | presentation identification code during which the student is registered on the module |
| studentInfo | id_student | unique student identification number |
| studentInfo | gender | student's gender |
| studentInfo | region | geographic region where the student lived while taking the module-presentation |
| studentInfo | highest_education | highest student education level on entry to the module presentation |
| studentInfo | imd_band | IMD band of the place where the student lived during the module-presentation |
| studentInfo | age_band | band of student's age |
| studentInfo | num_of_prev_attempts | number of times the student has attempted this module |
| studentInfo | studied_credits | total number of credits for the modules the student is currently studying |
| studentInfo | disability | whether the student has declared a disability |
| studentInfo | final_result | student's final result in the module-presentation |
| studentRegistration | code_module | module identification code |
| studentRegistration | code_presentation | presentation identification code |
| studentRegistration | id_student | unique student identification number |
| studentRegistration | date_registration | day of the student's registration for the module presentation |
| studentRegistration | date_unregistration | day of unregistration; empty for students who completed; Withdrawal as final_result for those who unregistered |
| studentAssessment | id_assessment | assessment identification number |
| studentAssessment | id_student | unique student identification number |
| studentAssessment | date_submitted | day of assessment submission |
| studentAssessment | is_banked | flag: the result was transferred from a previous presentation |
| studentAssessment | score | score from 0 to 100; below 40 is interpreted as Fail |
| studentVle | code_module | module identification code |
| studentVle | code_presentation | presentation identification code |
| studentVle | id_student | unique student identification number |
| studentVle | id_site | VLE material identification number |
| studentVle | date | day of the student's interaction with the material |
| studentVle | sum_click | number of times the student interacted with the material |
