# AQ Revision Log (design file, T09)

Working design file for report Section 3.2 (brief section 3.1). Columns as in the brief, with the Change Log IDs that
carry each change. The Milestone 1 wording is verbatim from Milestone 1 Section 4.1; the final wording is verbatim
from Milestone 4 Section 1.1 (Table 1.1). Milestone 5 changes no AQ wording: its one new measurement change, C15,
narrows the data on which AQ1 is computed, not what AQ1 asks. The Action column uses the brief's scale; no milestone
recorded an action per AQ, so the actions below are our reading of the Change Log (conflict R4, R6).

## Table 1. AQ Revision Log

| AQ-ID | AQ at Milestone 1 (verbatim) | Finding from M2/M3 | Final AQ (verbatim) | Action | Reason | Effect on method |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | In the program's online and blended courses over the four semesters of 2024–2025 and 2025–2026, what share of students enrolled after the add-drop period passed, failed or withdrew, by course, delivery mode and year of study, and how does the week of the first missed assessed task compare between students who passed and students who did not? | No open dataset of Vietnamese courses exists, so OULAD stands in (C01); a semester becomes a module run counted in days (C02); OULAD has a final result for all 32,593 enrolments and due days for 182 TMA and CMA tasks, but no delivery mode or year of study (C04), and exam results recorded in only 2 of 7 modules (CCC, DDD); 58 enrolments registered after day 14 (C03 → C09). Rated YELLOW. | What share of enrolments end in pass, fail or withdrawal, by module, run, start month and year, and in which week non-completers first miss an assessed task? | Modify (C01, C02, C04, C09); the 2014 detail is computed after the AQ3 test (C15) | Fields the question names do not exist in any open dataset, and the population must count only students enrolled at day 14; computing 2014 by outcome before the AQ3 test would open the test outcomes. | Rates by module, run, start month and year replace rates by course, delivery mode and year of study; the first missed task counts TMA and CMA only; the KPI population is the day-14 rule (28,061 enrolments over 22 runs); in Milestone 5 the rates are computed on the 9 runs of 2013 and the year comparison uses the 2014 outcome counts published in Milestone 3. |
| AQ2 | Which signs observable in weeks 1–4 (missed or late quizzes and assignments, LMS activity compared with the course's own average, missed tasks in several courses at once, and, in blended courses only, attendance at in-class sessions) show the largest difference in later non-completion rates between students who have the sign and students who do not, and are these differences similar across courses, delivery modes and years of study? | OULAD has no in-class sessions, so attendance has no counterpart (C05); no delivery mode or year of study (C04); tasks fall due by day 27 in only 16 of 22 runs; only 12 of the 1,382 enrolments taken at the same time as another fall in 2013, so the several-modules sign exists in 2014 only (C12). Rated YELLOW; ready for association only. | Which signs recorded by the end of week 4 (missed and late tasks, inactivity, activity against the run's median) go with later non-completion, compared within each module? | Modify (C01, C02, C04, C05, C12) + Defer (2014 replication and several-modules sign, C14) | Attendance, delivery mode and year of study are absent from OULAD; estimating AQ2 on 2014 before the AQ3 model is frozen would leak test information into AQ3 (C14). | Within-module association by logistic regression with run fixed effects on the 9 runs of 2013; task signs only in runs with a task due by day 27; comparison across modules replaces comparison across delivery modes and years of study; replication on the 13 runs of 2014 (with CCC and the several-modules sign) after the AQ3 test; association, never cause. |
| AQ3 | For each student enrolled in a pilot course, how well can failing or withdrawing by the end of the semester be estimated from the data recorded by the end of week 2 and by the end of week 4, compared with a simple rule such as "two or more assessed tasks missed"? Accuracy is measured on a list as long as staff can follow up each week, as recall and precision, and is compared between first-year and later-year students and across courses. | A non-exam task falls due by day 13 in 1 of 22 runs and by day 27 in 16, so the week-3 list rests on activity (C06) and a task-only rule cannot fire in 6 runs at day 27 or 21 at day 13 (C10); each module has at most one earlier run of the same start month, 9 pairs ran in both years (C07); no year of study (C04). Rated YELLOW. | How well can non-completion be estimated from the data up to the end of week 2 and of week 4, compared with the early-sign rule, when a model built on the 2013 runs is applied to the 2014 runs? | Modify (C01, C02, C04, C06, C07, C10, C16) | Assessed tasks rarely fall due by the cut-offs, so the comparison rule needs an activity part to flag anyone; testing on a later year mirrors use on a later semester; year of study does not exist. | Train on the 9 runs of 2013, test once on all 13 runs of 2014 (9 paired and 4 unpaired runs reported apart, C16); the comparison rule is the C10 early-sign rule; group checks by deprivation band and disability replace first-year against later-year; recall and precision at capacity become normalised recall at capacity (C13). |
| AQ4 | At each review point (weeks 3 and 5), which students should be listed, in what order, and with which contact (a message from the lecturer or lecturer-advisor, a call from the support office, or a referral to the student affairs office, which handles financial and personal matters, separate from the support office), so that the list reaches as many as possible of the students most likely not to complete? The list must fit weekly capacity (three to five contacts per lecturer-advisor, about 30–40 for the support office), reach a precision of at least 50%, and keep first-year recall within ten points of later-year recall. | No candidate dataset records contacts, contact types, staff capacity or outcomes after a contact (C08), so AQ4 is RED; non-completion is 44–45% at the cut-offs, so a random list already reaches about 45% precision (C13); year of study is absent, so the fairness limit moves to deprivation band and disability (C04). | Which enrolments should rank first on a list of an assumed capacity, with what gain over a random list and what recall, overall and by deprivation band and disability? | Modify (ranking part; C04, C08, C11, C13) + Defer (contact choice and its effect, to the pilot; C11) | The contact part has no data in OULAD or any screened dataset, and the 50% precision limit says nothing when the base rate is about 45%. | Top-k list per run from the AQ3 scores under an assumed capacity of 3 or 5 per 20, judged by lift and normalised recall against random and rule-ranked lists; the ten-point fairness gap returns as rule FR1 on declared disability, band 0–10% and the missing band, where a flag leads to human review; no prescriptive or causal claim; the contact choice waits for a randomised pilot. |

**Sources (Table 1)**

- Milestone 1 wording: baseline file "Milestone 1: Questions at four levels (Section 4.1)"; C3-001, C3-002, C3-003,
  C3-004.
- Findings: AQ1 C1-016 (C01), C3-016 (C02), C3-014, C3-015 (C04), C7-002 and C2-009 (C09, 58 late registrants: C03
  vs C09 in the baseline file, Milestone 3 Section 4.1); rating C3-013. AQ2 C3-017 (C05), C3-015, C5-016 (16 of
  22 runs), C3-018 (C12); readiness C8-001. AQ3 C3-020 (C06), C3-022 (C10), C3-021 and C6-019 (C07); C3-015. AQ4
  C3-023 (C08), C5-017 (RED), C3-025 (C13), C3-015 (C04).
- Final wording: C3-008, C3-009, C3-010, C3-011.
- Actions: synthesis of the Change Log (Part 3 synthesis, 03-02 "Gaps"); AQ4 Modify + Defer C3-024, C3-027; no
  question dropped C3-027. AQ1 C15 and AQ3 C16: `change-log-m5.md`.
- Reasons: C3-015, C3-017, C3-019 (C14), C3-022, C3-024, C3-025, C15 reason (`change-log-m5.md`).
- Effects: AQ1 C8-021, C7-002, C6-026 (TMA and CMA only), `results/README.md` (2013-only rule). AQ2 C8-022, C3-019,
  C9-007, C9-008 (association only). AQ3 C7-035, C9-010, C9-018 (paired/unpaired), C7-011 (C10 rule), C9-026
  (groups), C9-014 (normalised recall). AQ4 C8-028, C9-013, C9-023 (FR1, 10 points), C9-026, C9-027 (flag → review),
  C12-009, C12-019.

## Table 2. Change Log IDs per AQ

| AQ | Change Log entries | Milestone |
| :---- | :---- | :---- |
| AQ1 | C01, C02, C03, C04, C09, C15 | 2, 2, 2, 2, 3, 5 |
| AQ2 | C01, C02, C04, C05, C12, C14 | 2, 2, 2, 2, 3, 4 |
| AQ3 | C01, C02, C04, C06, C07, C10, C13, C16 | 2, 2, 2, 2, 2, 3, 3, 3–4 (recorded in 5) |
| AQ4 | C01, C04, C08, C11, C13 | 2, 2, 2, 3, 3 |
| Secondary KPI 1 (rule) | C06, C10, C17 | 2, 3, 5 |

Sources: Change Log rows C01–C13 (S103 crawl lines 1466–1478), C14 (S104 crawl line 1338), C15–C17
(`change-log-m5.md`).

## Table 3. Mapping the milestones' status scales to the brief's scales

Each milestone rated the questions on its own brief's scale. Table 3 maps each scale onto the two scales of the
Milestone 5 brief: the revision action (Keep / Modify / Defer / Drop, brief 3.1 and section 2 row 5) and the final
status (Answered / Partial / Deferred / Dropped, brief section 3). Milestone 1 rated no status; its questions are the
starting point.

| Milestone | Scale and meaning | AQ1 | AQ2 | AQ3 | AQ4 | Maps to revision action |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2 – Coverage | Full: answers the question as stated; Partial: answers its core, kept or narrowed with limits; None: cannot answer, revise or keep as a future requirement | Partial | Partial | Partial | Partial (ranking) / None (action) | Full → Keep; Partial → Modify; None → Defer (kept as a future data requirement) or Drop |
| 3 – AQ–Data Fit | GREEN: data enough at the claimed level; YELLOW: narrow the question, change its claim or add data; RED: key concept, variable, target or intervention missing, revise, drop or defer | YELLOW | YELLOW | YELLOW | RED | GREEN → Keep; YELLOW → Modify; RED → Modify (part the data support) + Defer, or Drop |
| 3 – Model Readiness | Ready: view, target and rules fixed and validated; Revise: part of the question still lacks data | Ready | Ready, for association only | Ready | Revise (ranking ready, contact deferred) | Ready → no further action; Revise → Defer for the missing part |
| 4 – Entry status | Ready, with qualifiers | Ready | Ready, for association only | Ready | Ready as a ranking; contact deferred (C11) | Same content as Milestone 3 readiness (R12) |
| 5 – Revision action (brief 3.1) | Keep / Modify / Defer / Drop | Modify (2014 detail after the AQ3 test) | Modify + Defer (2014 replication) | Modify | Modify + Defer (contact choice) | – |
| 5 – Final status (brief 3) | Answered / Partial / Deferred / Dropped | Partial | Partial | Deferred | Deferred | – |

**Sources (Table 3):** M2 scale and ratings C5-011 and S102 crawl lines 489–504; M3 fit scale C5-014 and S103 crawl
lines 400–405, ratings C3-013; M3 readiness C8-001 and baseline file "Milestone 3: Readiness matrix"; M4 entry
status C5-020, C3-008–C3-011; final status `traceability-matrix.md` (status justification). The mapping rules
restate each scale's own definition (S102 line 489–492; S103 line 402–405); brief scales from
`milestones/05/milestone-5.md` sections 2, 3, 3.1.
