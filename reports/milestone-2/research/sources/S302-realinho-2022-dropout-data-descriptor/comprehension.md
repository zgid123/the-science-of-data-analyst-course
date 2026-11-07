# S302 – Predicting Student Dropout and Academic Success (Realinho et al., Data 2022)

## Summary in my own words

This MDPI Data descriptor documents the dataset held at UCI as id 697 (S301) and at Zenodo (10.5281/zenodo.5777339). It covers students enrolled between 2008/2009 and 2018/2019 in 17 undergraduate degrees of the Polytechnic Institute of Portalegre, Portugal, merged from the academic management system and other sources into one CSV of 4,424 records and 35 attributes. Each student is labelled dropout, enrolled or graduate at the end of the normal duration of the degree (3 years, 4 for Nursing); 1,421 records are dropouts. Academic features are aggregated counts and grades of curricular units at the end of the first and second semesters, with no dated tasks. The data are anonymised and GDPR compliance was validated by the institution's Data Protection Officer.

## Key facts

- Period and degrees – "The data refer to records of students enrolled between the academic years 2008/2009 (after the application of the Bologna Process to higher education in Europe) to 2018/2019."
- Format and size – "The final dataset is available as a comma-separated values (CSV) file encoded as UTF8 and consists of 4424 records with 35 attributes and contains no missing values."
- Target definition – "each student is classified as a dropout, enrolled, or graduate depending on their situation at the end of the normal duration of the course (3 years, except Nursing which has 4 years)."
- Class shares – "Dropout represents 32% of total records (1421 of 4424)"
- Semester aggregates – "| Curricular units 1st sem (evaluations) | Numeric/discrete"
- Anonymisation – "All data are anonymized, and compliance with the Privacy and Personal Data Processing Policy of the institution is ensured according to the General Data Protection Regulation (GDPR)."
- DPO validation – "Privacy issues related to the use and publication of the dataset were validated by the Data Protection Officer (DPO) of the Polytechnic Institute of Portalegre"
- Dataset licence – "Dataset License: CC BY 4.0"
- Dataset DOI – "Dataset:https://doi.org/10.5281/zenodo.5777339."

## Used in

03-00-search-strategy.md, 04-02-selection-matrix.md

## Against reference.md

Extends brief section 13: the dataset is degree-level (one row per student, outcome after 3–4 years) and does not separate course-level fail from withdrawal. The descriptor says 35 attributes while UCI lists 36 features (the target is likely counted on UCI); no conflict with the brief.

## Reliability

Primary; authors at the Polytechnic Institute of Portalegre; peer-reviewed data descriptor in Data (MDPI) 2022; 175 citations per OpenAlex as of 2026-11-06 (fetch.py find). Read from a Wayback copy because MDPI returned HTTP 403.

## Open questions

No per-record enrolment year is described in the read text, so an ordering of cohorts for time-based testing is not documented.
