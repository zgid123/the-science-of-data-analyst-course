# Dataset scoring and selection (T08, Task 4; revised after the AI selection reviewer, T09)

Inputs: gates and requirements (`requirements/data-requirements.md` section 5), candidate facts with claim IDs
(`search/candidates.md`, `part3-claims.md`). Scale (brief section 8): 0 = not met or not stated, 1 = partly met or
uncertain, 2 = well met on recorded evidence. A fact the documentation does not state scores as uncertain or not met,
for every candidate alike. Scores support the discussion; the gates decide first.

## 1. Full scoring on the brief's ten criteria

| Criterion | A OULAD | B UCI 697 | C UCI 320 | D UCI 856 | E XuetangX | F HarvardX | G xAPI-Edu |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ coverage | 1 – data for AQ1–AQ3 with partial clauses (no delivery mode, year of study, attendance); AQ4 ranking only (C3-008–C3-011) | 0 – degree-level, no course timing (C3-021, C3-030) | 0 – one grade per subject (C3-034) | 0 – questionnaire (C3-040) | 1 – activity and dropout, no assessments (C3-046, C3-047) | 0 – aggregates (C3-053) | 0 – one grade band (C3-069) |
| Population fit | 1 – higher education, distance learning, UK; modules chosen partly for high failure (C3-006, C3-015) | 1 – higher education, Portugal (C3-019) | 0 – secondary school (C3-032) | 1 – higher education, one 2019 collection (C3-039) | 1 – MOOC learners, China (C3-051) | 1 – MOOC learners (C3-052) | 0 – users of a school learning platform (C3-066) |
| Unit and granularity | 2 – student–module–run; daily activity (C3-007, C3-011) | 0 – student (C3-022) | 0 – student–subject (C3-033) | 0 – student questionnaire (C3-040) | 1 – user–course, timestamped (C3-046) | 1 – user–course aggregates (C3-053) | 0 – student record (C3-067) |
| Outcome / target | 1 – Withdrawal recorded with a date; the other result values not stated in the documentation read (C3-008, C3-063) | 1 – degree dropout / graduate (C3-021) | 1 – grade 0–20 (C3-034) | 1 – letter grade (C3-041) | 1 – binary dropout (C3-047) | 1 – certification only (S307) | 1 – grade band (C3-069) |
| Feature availability and timing | 1 – dated assessments, submissions and clicks; mark release dates not recorded, unsubmitted tasks leave no row, tasks in weeks 1–4 not stated (C3-009–C3-011, C3-016) | 0 – semester aggregates (C3-030) | 0 – period grades (C3-035) | 0 – none (C3-040) | 1 – dated actions, no assessments (C3-046) | 0 – first and last event only (C3-056) | 0 – none dated |
| Temporal coverage | 1 – 22 runs over 2013–2014, ordered by code; runs per module not stated (C3-005, C3-061) | 1 – 11 entry cohorts, no cohort field documented (C3-026) | 0 – one year | 0 – one collection (C3-039) | 1 – two years; runs of a course not stated (C3-045) | 0 – one year (C3-052) | 0 – two undated semesters (C3-068) |
| Documentation and provenance | 1 – descriptor and DOI, but no version number and two distribution points (C3-004, C3-018) | 2 – UCI page, descriptor, DOI (C3-024) | 1 – variable list (C3-037) | 1 – question list (C3-043) | 1 – column list, paper blocked (C3-044) | 2 – versioned deposit with checksum (C3-054, C3-057) | 0 – Kaggle listing only (C3-070) |
| License and access | 2 – CC BY 4.0 (C3-002, C3-018) | 2 – CC BY 4.0 (C3-024) | 2 – CC BY 4.0 (C3-037) | 2 – CC BY 4.0 (C3-043) | 0 – no license stated (S305) | 0 – community norms, no open license (C3-055) | 1 – CC BY-SA on a Kaggle listing (C3-070) |
| Quality feasibility | 1 – CSV, 10.7 million click rows; unsubmitted tasks leave no row, exam results mostly missing (C3-003, C3-005, C3-016) | 2 – one clean CSV (C3-025, C3-027) | 2 – small CSV (C3-038) | 2 – small CSV (C3-043) | 1 – large logs (S305) | 2 – one table (S307) | 2 – small CSV (C3-067) |
| Ethics and representativeness | 1 – anonymised (k = 5); deprivation (IMD) band and disability present; high-failure module selection (C3-013–C3-015) | 1 – anonymised under the EU General Data Protection Regulation (C3-031) | 0 – anonymisation not stated | 0 – not stated | 0 – not stated | 1 – de-identified (C3-057) | 0 – not stated |
| **Total (of 20)** | **12** | **10** | **6** | **7** | **8** | **8** | **4** |
| Gates failed (documented evidence) | none; G1 pass/fail values, G3 per module and G5 linkage across runs to confirm in the structural verification (Section 6) | G1, G2a, G2b | G1, G2a, G2b, G3 | G1, G2a, G2b, G3 | G1, G2a, G4 | G1, G2a, G2b, G3, G4 | G1, G2a, G2b, G3; G4 unclear |

## 2. Dataset Selection Matrix (brief section 8.1)

| Candidate | AQ coverage | Population fit | Target / timing | Docs / license | Quality feasibility | Ethics / representativeness | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A OULAD | 1 | 1 | 1 / 1 | 1 / 2 | 1 | 1 | Selected, conditional on Task 6 (G1, G3, G5) |
| B UCI 697 | 0 | 1 | 1 / 0 | 2 / 2 | 2 | 1 | Rejected: fails G1, G2a, G2b |
| C UCI 320 | 0 | 0 | 1 / 0 | 1 / 2 | 2 | 0 | Rejected: fails G1–G3 |
| D UCI 856 | 0 | 1 | 1 / 0 | 1 / 2 | 2 | 0 | Rejected: fails G1–G3 |
| E XuetangX | 1 | 1 | 1 / 1 | 1 / 0 | 1 | 0 | Rejected: fails G1, G2a, G4 |
| F HarvardX | 0 | 1 | 1 / 0 | 2 / 0 | 2 | 1 | Rejected: fails G1–G4 |
| G xAPI-Edu-Data | 0 | 0 | 1 / 0 | 0 / 1 | 2 | 0 | Rejected: fails G1–G3; provenance unclear |

## 3. Decision and rationale

OULAD is selected as the primary dataset, conditional on Task 6. It is the only candidate whose documentation meets
the outcome (dated withdrawal), timing and license gates; every other candidate fails at least G1 and G2a. Its score
(12 of 20) is modest because the documentation leaves facts open, and the score is not the reason for the choice.

Task 6 must confirm, in the downloaded files:
- G1: the result values separate pass (including distinction) from fail and withdrawal;
- G3: each module used for AQ3 has at least three runs ordered in time, counting B and J runs separately as the
  authors advise; fallback: narrow AQ3 to the modules that qualify;
- G5: a student keeps the same identifier across runs; fallback: concurrent-course signs (AQ2) and one list entry
  per student (AQ4) become Partial;
- tasks due in weeks 1–4 per run, and unregistration on or before day 0, which sets the KPI denominator.

Known limits enter the coverage and ethics sections: UK distance learners in 2013–2014, modules chosen partly for
their high failure rates (C3-015), so base rates are higher than in a typical program; no delivery mode, year of
study, attendance, leave or transfer.

No supplementary dataset is selected. No candidate holds the missing contact record, staff capacity, delivery mode,
year of study, attendance or leave and transfer status. A second population could test whether the activity signs of
AQ2 hold elsewhere; the only candidate with dated activity, XuetangX, has no stated license (fails G4) and no pass/fail
outcome, so that external check remains an open limitation.
