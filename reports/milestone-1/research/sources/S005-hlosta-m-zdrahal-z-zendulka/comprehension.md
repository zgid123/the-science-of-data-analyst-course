# S005 – Ouroboros: early identification of at-risk students without models based on legacy data (Hlosta, Zdrahal & Zendulka, LAK 2017)

## Summary in my own words

Only the bibliographic record and abstract could be read; the ACM, Open Research Online and CORE copies all returned 403 to scripts and to WebFetch. The abstract states the problem of identifying students at risk of failing when no data from earlier presentations of the course exist, as happens in new courses. The authors propose a "self-learner" that trains machine-learning models on data produced during the current presentation, using information about assessments already submitted. This creates imbalanced training and testing data, which the paper addresses. Authors are from the Open University and Brno University of Technology, the same group that built OU Analyse and released OULAD (S002).

## Key facts

- Problem – "This paper focuses on the problem of identifying students, who are at risk of failing their course."
- No legacy data – "The presented method proposes a solution in the absence of data from previous courses, which are usually used for training machine learning models. This situation typically occurs in new courses."
- Self-learner – "that builds the machine learning models from the data generated during the current course"
- Data used and difficulty – "The approach utilises information about already submitted assessments, which introduces the problem of imbalanced data for training and testing the classification models."
- Institutions – "institutions: Brno University of Technology; The Open University"
- Venue and pages – "pages: 6–15"
- Citation traction – "cited_by_count (OpenAlex): 113" (as of 2026-11-02)

## Used in

05-01-types-techniques-outputs.md, 05-02-evaluation-design.md

## Against reference.md

Confirms the outline's reference [5] as prior work (section 5) and extends it: it shows a second design option for the predictive question (train within the current presentation instead of on the previous one), which matters when a course has no earlier run. The abstract gives no evaluation figures, so the outline's use should stay at the level of the design idea.

## Reliability

Primary (method paper by the OU Analyse team); ACM LAK '17 full paper, pages 6–15; 113 citations in OpenAlex as of 2026-11-02. Metadata and abstract only: status partial.

## Open questions

Prediction target (next-assessment submission), timing, evaluation metrics and the comparison with legacy-data models could not be read from the full text; a readable copy (for example, Open Research Online item 49731 opened in a browser) is needed before stating any result.
