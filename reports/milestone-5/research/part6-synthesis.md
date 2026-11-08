# Part 6 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 06-00-data-understanding.md

**Milestone evidence (T06):**
- Claims: C6-001, C6-002, C6-003, C6-005, C6-004, C6-006, C6-015, C6-016, C6-014.
- Brief requirement (section 2, Part 6): distribution, missingness, duplicates, invalids, outliers, imbalance, temporal coverage, representativeness, sensitive fields; evidence = profiling tables/charts + quality findings; self-check "which data problem could change a conclusion?".
- Outline: (1) what the data are in education terms: 22 runs, 7 modules, 32,593 enrolments of 28,785 students, enrolment as unit, keys checked (C6-001–C6-003); (2) outcome and time semantics: final_result counts, non-completion = Fail or Withdrawn, days from day 0, cut-offs day 13 and day 27 (C6-004, C6-005); (3) profile on all rows with independent recount (C6-006); (4) outcome balance: 54.7% completion in the KPI population of 28,061, 45.3%/44.2% non-completion at the cut-offs, 24.9–58.3% by run, no resampling (C6-015, C6-016); (5) score distributions and study load (C6-014).
- Conflicts with the outline: None.
- Gaps: no profiling figure is planned for Part 6 in the Milestone 5 figure task (T10 covers the logic chain and AQ1/AQ2 only); the Milestone 3 figure of final results by run (Figure 3.1) would need to be redrawn or re-used, or the profile stated as a table.

## 06-01-quality-findings.md

**Milestone evidence (T06):**
- Claims: C6-025, C6-008, C6-009, C6-007, C6-010, C6-011, C6-012, C6-027, C6-028, C6-013, C6-026, C6-033.
- Brief requirement: quality findings with evidence; which issues could change a conclusion.
- Outline: (1) the Data Quality Issue Log DQ01–DQ19 and its severity rule (C6-025); (2) duplicates and grain: 787,170 exact duplicate click rows kept with a de-duplicated twin, sum to enrolment-day, left joins (C6-008, C6-009, C6-007); (3) missingness: imd_band 1,111 kept as "Missing" (65.7% vs 46.6% success), 45 registration days, 173 TMA scores, exams absent by design (C6-010, C6-011); (4) six validity inconsistencies flagged, never overwritten, incl. CMA lateness and post-unregistration activity (C6-012, C6-027, C6-028); (5) outliers kept, logs in matrices (C6-013); (6) the three High issues that could change a conclusion: DQ08, DQ18, DQ19 (C6-026), and none of the resulting changes C09–C13 touches the Business Goal or D1–D3 (C6-033).
- Conflicts with the outline: None.
- Gaps: the Milestone 5 analysis runs on the 9 runs of 2013 only, so the quality findings that matter most for AQ1/AQ2 should be restated for 2013 where they differ (duplicate share 6.82% in 2013 against 7.87% in 2014, C7-027; how many of the 9 runs of 2013 have a task due by day 27 is not stated in Milestones 3–4: T08 should count it).

## 06-02-representativeness-sensitive.md

**Milestone evidence (T06):**
- Claims: C6-017, C6-018, C6-019, C6-020, C6-021, C6-022, C6-023, C6-024, C6-029, C6-030, C6-032, C6-031.
- Brief requirement: temporal coverage, representativeness, sensitive fields.
- Outline: (1) temporal coverage: four weeks before the start to week 39, peak in week 3, logging gap DQ15 (C6-017); few tasks due by the cut-offs, DQ18 (C6-018); 9 module–start-month pairs in both years, CCC and February EEE/GGG in 2014 only (C6-019); (2) representativeness: anonymised subset of UK distance students of 2013–2014, modules chosen partly for failure, completion 45.7% (CCC) to 73.8% (AAA), age, credit load and gender mix (C6-020, C6-021); (3) sensitive attributes: six held, 20-student reporting limit, smallest groups (C6-022, C6-023), IMD describes the area not the student and is not comparable across UK nations (C6-024); (4) why they are kept for audit and not as predictors, known audit group sizes, published OULAD fairness finding (C6-029, C6-030, C6-032); (5) privacy: k = 5 anonymity, no linkage, the pilot needs its own legal basis under Law 91/2025/QH15 (C6-031).
- Conflicts with the outline: None.
- Gaps: None.
