# Part 3 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 03-01-shape-keys-joins.md

**Claims:** C3-009, C3-006, C3-007

**Outline:**
- Descriptor row counts per table as the reference for the shape check (studentInfo 32,593; assessments 206; studentAssessment 173,912; studentVle 10,655,280; vle 6,364; courses 22) (C3-009).
- Student counts differ by table: students who unregistered before the start have no assessment rows, so inner joins drop them (C3-006).
- Repeat students across presentations need a keep-or-remove rule (C3-007); the key is student × module × presentation, not id_student alone.

**Conflicts with the outline:** None.

**Gaps:** No primary source documents duplicate rows in studentVle; whether repeated (student, site, date) rows are errors or split daily summaries must be decided from the data profile.

## 03-02-missingness-validity.md

**Claims:** C3-001, C3-002, C3-003, C3-004, C3-005, C3-010, C3-014

**Outline:**
- Missing submissions are absent rows, not empty cells (C3-001); exam results are usually missing by design (C3-002); a missing assessment date marks a final exam in the last week (C3-003).
- Empty date_unregistration is a structural blank for non-withdrawers (C3-004); positive date_registration values are valid up to about two weeks after start (C3-010).
- Label check: descriptor says "Withdrawal", a third-party package codes "Withdrawn" (C3-004, C3-005) – the data value decides.
- imd_band validity across nations: pooling national bands is misleading (C3-014).

**Conflicts with the outline:** None. With the descriptor S002: the withdrawal label ("Withdrawal" in S002, "Withdrawn" in S207) – confirm by counting final_result values.

**Gaps:** Withdrawn students without an un-registration date and the count of missing imd_band are not documented in any source; they must be counted (Part 3 profile).

## 03-04-temporal-representativeness.md

**Claims:** C3-012, C3-011, C3-015, C3-013, C3-008, C3-016

**Outline:**
- OULAD is a 2013–2014 subset of seven modules reduced by anonymisation (C3-012).
- IMD drifts with home postcode, the largest 2013/14-vs-2015 difference in the descriptor's check (C3-011); IMD 2015 indicators date from 2012/13 (C3-015); national indices use different data years (C3-013).
- Withdrawal must be read relative to the analysis cut-off week: only withdrawals up to the cut-off are known then (C3-008).
- The OU marking timeline on disk is from 2025, an assumption for 2013–2014 (C3-016).

**Conflicts with the outline:** None.

**Gaps:** No source for OU marking rules in 2013–2014.
