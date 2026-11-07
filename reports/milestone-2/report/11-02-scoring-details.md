## Appendix II – Candidate Scoring Details

Table A.2 gives each candidate's score on the brief's ten criteria (0 = not met or not stated, 1 = partly met or uncertain, 2 = well met) with the fact behind it, and the must-have gates it fails. Every fact comes from the candidate's official page or descriptor.

The ten criteria ask whether the dataset can answer the questions (AQ coverage), whether its population resembles the project's (population fit), whether its unit and time grain match (unit and granularity), whether it holds the outcome (outcome availability), whether its predictors exist before the prediction point (feature availability and timing), whether it covers enough time (temporal coverage), whether it is documented and traceable (documentation and provenance), whether it may be used (license and access), whether it can be handled (quality feasibility) and whether it is anonymised and representative (ethics and representativeness). Each criterion takes 0 when it is not met or not stated, 1 when it is partly met or uncertain, and 2 when it is well met.

**Table A.2. Scores on the ten criteria and failed gates**

| Criterion | A OULAD | B UCI 697 | C UCI 320 | D UCI 856 | E XuetangX | F HarvardX | G xAPI-Edu |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ coverage | 1 – data for AQ1–AQ3 with partial clauses (no delivery mode, year of study, attendance); AQ4 ranking only | 0 – degree-level, no course timing | 0 – one grade per subject | 0 – questionnaire | 1 – activity and dropout, no assessments | 0 – aggregates | 0 – one grade band |
| Population fit | 1 – higher education, distance learning, UK; modules chosen partly for high failure | 1 – higher education, Portugal | 0 – secondary school | 1 – higher education, one 2019 collection | 1 – MOOC learners, China | 1 – MOOC learners | 0 – users of a school learning platform |
| Unit and granularity | 2 – student–module–run; daily activity | 0 – student | 0 – student–subject | 0 – student questionnaire | 1 – user–course, timestamped | 1 – user–course aggregates | 0 – student record |
| Outcome / target | 1 – Withdrawal recorded with a date; the other result values not stated in the documentation read | 1 – degree dropout / graduate | 1 – grade 0–20 | 1 – letter grade | 1 – binary dropout | 1 – certification only | 1 – grade band |
| Feature availability and timing | 1 – dated assessments, submissions and clicks; mark release dates not recorded, unsubmitted tasks leave no row, tasks in weeks 1–4 not stated | 0 – semester aggregates | 0 – period grades | 0 – none | 1 – dated actions, no assessments | 0 – first and last event only | 0 – none dated |
| Temporal coverage | 1 – 22 runs over 2013–2014, ordered by code; runs per module not stated | 1 – 11 entry cohorts, no cohort field documented | 0 – one year | 0 – one collection | 1 – two years; runs of a course not stated | 0 – one year | 0 – two undated semesters |
| Documentation and provenance | 1 – descriptor and DOI, but no version number and two distribution points | 2 – UCI page, descriptor, DOI | 1 – variable list | 1 – question list | 1 – column list, paper blocked | 2 – versioned deposit with checksum | 0 – Kaggle listing only |
| License and access | 2 – CC BY 4.0 | 2 – CC BY 4.0 | 2 – CC BY 4.0 | 2 – CC BY 4.0 | 0 – no license stated | 0 – community norms, no open license | 1 – CC BY-SA on a Kaggle listing |
| Quality feasibility | 1 – CSV, 10.7 million click rows; unsubmitted tasks leave no row, exam results mostly missing | 2 – one clean CSV | 2 – small CSV | 2 – small CSV | 1 – large logs | 2 – one table | 2 – small CSV |
| Ethics and representativeness | 1 – anonymised (k = 5); deprivation (IMD) band and disability present; high-failure module selection | 1 – anonymised under the EU General Data Protection Regulation | 0 – anonymisation not stated | 0 – not stated | 0 – not stated | 1 – de-identified | 0 – not stated |
| **Total (of 20)** | **12** | **10** | **6** | **7** | **8** | **8** | **4** |
| Gates failed (documented evidence) | none; G1 pass/fail values, G3 per module and G5 linkage across runs to confirm in the structural verification (Section 6) | G1, G2a, G2b | G1, G2a, G2b, G3 | G1, G2a, G2b, G3 | G1, G2a, G4 | G1, G2a, G2b, G3, G4 | G1, G2a, G2b, G3; G4 unclear |
