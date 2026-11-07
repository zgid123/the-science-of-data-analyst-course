# S301 – Predict Students' Dropout and Academic Success [Dataset], UCI Machine Learning Repository (2021)

## Summary in my own words

The UCI record (DOI 10.24432/C5MC89, donated 12 December 2021) holds one table of 4,424 students from undergraduate degrees of a Portuguese higher education institution (creators at Instituto Politécnico de Portalegre). Each row is a student, with information known at enrolment (academic path, demographics, socio-economic factors) and academic performance aggregated at the end of the first and second semesters. The target has three classes: dropout, enrolled and graduate, measured at the end of the normal duration of the course, so it does not separate fail from withdrawal at course level and has no within-semester dates. The licence is CC BY 4.0 and the file is a single 520.7 KB CSV without missing values after preprocessing.

## Key facts

- Context – "A dataset created from a higher education institution (acquired from several disjoint databases) related to students enrolled in different undergraduate degrees"
- Content – "The dataset includes information known at the time of student enrollment (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first and second semesters."
- Target – "The problem is formulated as a three category classification task (dropout, enrolled, and graduate) at the end of the normal duration of the course."
- Unit – "Each instance is a student"
- Size – "Instances 4424"
- Imbalance – "there is a strong imbalance towards one of the classes"
- Funding – "This dataset is supported by program SATDAP - Capacitação da Administração Pública under grant POCI-05-5762-FSE-000191, Portugal."
- Preprocessing – "We performed a rigorous data preprocessing to handle data from anomalies, unexplainable outliers, and missing values."
- File – "| data.csv | 520.7 KB"
- Licence – "Creative Commons Attribution 4.0 International"
- Citation – "Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021). Predict Students' Dropout and Academic Success [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89."
- Introductory paper: Martins M. V. et al. (Trends and Applications in Information Systems and Technologies 2021) – "Early prediction of student's performance in higher education: a case study"
- Sensitive attributes in the variable table, e.g. nationality and marital status – "| Marital Status | Feature | Integer | Marital Status |"

## Used in

03-00-search-strategy.md, 04-02-selection-matrix.md, 11-01-search-log.md

## Against reference.md

Confirms brief section 13 (higher education, dropout/success classification, CC BY 4.0). Extends it: the target is degree-level (dropout, enrolled, graduate), not course-level pass/fail/withdrawal, and there are no dated tasks or activity.

## Reliability

Primary; UCI Machine Learning Repository record with DOI, creators at Instituto Politécnico de Portalegre; the page shows "1 citations" and 336,731 views as of 2026-11-06 (UCI's own counter).

## Open questions

The page lists only 10 of 37 variables and states no years of collection; the data descriptor (Realinho et al., Data 2022) is needed for the period and the anonymisation statement.
