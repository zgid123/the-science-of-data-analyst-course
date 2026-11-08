# Milestone 2 revision: full draft, then move to appendix (2026-11-07)

User instruction (2026-11-07): repeat the Milestone 1 process on Milestone 2: write the complete report first, then
reduce the main text by moving blocks to appendices, never by condensing sentences. Also make the title-page field
"Project title / Chủ đề dự án" identical across Milestones 1–4.

## Before writing

- The Milestone 1 proposal was rewritten on 2026-11-07, so the baseline was frozen again from it
  (code/freeze_baseline.py, markers updated for the new KPI prose and question text; logs/R0_refreeze.log). The
  goal, SMART Goal, KPIs and AQ1–AQ4 are unchanged in meaning, so the Change Log C01–C08 still applies; Appendix V
  shows the new checksums. The earlier frozen copy is research/baseline/m1-baseline-before-m1-rewrite.md.
- Milestone 1 Section 6.1 was edited after that freeze ("32,593 student records", in the OULAD paragraph, outside the
  copied Table 6.1), so its checksum went out of date. The baseline was frozen again on 2026-11-07T17:48:28Z and
  Appendix V Table A.8 regenerated (logs/R9_refreeze_checksum.log); only the 06-01 checksum changed, the copied text
  is identical, and all eight checksums in Table A.8 (EN and VI) match the current files (logs/R9_checksum_check.log).
- Rule applied, as in Milestone 1: the main text keeps every element the brief's section 15.1 lists for a section,
  each result in full sentences, every definition the text needs and one reason per choice.

## Measurements (reports/milestone-1/code/estimate_parts.py)

| Stage | Main content (Parts 1–9) | Log |
| :---- | :---- | :---- |
| Condensed version | 11.2 pages, about 5,950 words | snapshot condensed-2026-11-07 (research/revisions/snapshots.md) |
| Full draft | 14.7 pages, 8,295 words | logs/R1_full_draft_pages.log, R1_full_draft_blocks.log |
| After moves | 14.1 pages | logs/R2_pages.log |

## Blocks moved

| Block | Moved to | Main text keeps | Reason |
| :---- | :---- | :---- | :---- |
| 1.2 Summary table of C01–C08 | Appendix V already holds the full Change Log (Table A.9) | The four revisions that matter most, in sentences, and pointers to Section 7.2 and Table A.9 | The full log is deliverable D; the main text needs the main effects |
| 4.1 Meaning of each of the ten criteria | Appendix II (via research/appendix/criteria.md, read by code/build_appendices.py) | The scale, the rule that a 2 needs a documented fact, and the gate rule | The criteria are the brief's own; the reader needs the scale and the decision rule |
| 5 Detailed reasoning on the three copies of OULAD | Appendix III (via research/appendix/copies.md) | Which copy was collected and why, in one paragraph | Provenance detail behind the acquisition plan |
| 7.2 AQ1/AQ2 paragraph | Removed as a repeat of Table 7.1 | One sentence with the codes | Repetition |

## Not moved, with reason

Tables 1.1, 2.1, 2.2, 2.3, 3.1, 4.1, 5.1, 6.1, 7.1 and 9.1 are the brief's own templates or required section content
(baseline, requirement matrix, levels, prediction point, ≥ 3 candidates, selection matrix, acquisition plan,
structure, traceability, AI roles). The explanations added in the full draft (gates with their reasons, OULAD's
organisation, coverage levels, checksums, k-anonymity, deprivation band) define terms the tables use, so they stay.

## Generator fixes

code/build_appendices.py no longer overwrites Appendix VI, whose prompts were rewritten by hand to name documents by
their place in the report; a regeneration had restored repository paths and task IDs. Appendices I–V regenerate as
before.

## Reader test and fixes

An independent reader of the built Word file returned 19 items. Fixed: the gate rule now states that a gate missed
outright rejects a candidate while a gate met for part of a dataset narrows the questions (OULAD's history gate);
unit of analysis per question; Section 1.1 restated in Milestone 1's words (D1, D3, SMART Goal, AQ4 limits, KPI 1
denominator); C02 no longer quotes a semester length Milestone 1 never set; denominator path 32,593 → 3,097 + 1,377 →
28,119 (code/count_early_tasks.py, logs/R3_early_tasks.log); documentation score explained; all ten criteria named and
shown in Table 4.1; OULAD column names explained; header check result stated; scores excluded for lack of release
dates; 32,593 enrolments of 28,785 students (and Milestone 1 now says "student records"); terms defined at first use;
"eight to nine months"; three documentation differences; 11 searches in 16 entries; appendix jargon (Task 6, IMD, GDPR,
LMS). Found while fixing: two tasks fall due by day 27 in only 1 of 22 runs, so the early-sign rule of secondary KPI 1
cannot be applied as defined on OULAD; C06 and Section 7.2 now state the one-task deviation. Not changed: the cover
row on the Milestone 1 version (all milestones are submitted on the same day).

Main content after fixes: EN 15.1 pages, VI 16.5 pages (logs/R5_pages.log).

## Review of Section 1.2 against the brief (2026-11-08)

User request: check whether Section 1.2 (Scope of Milestone 2 and Change Log Summary, 0.92 pages in the pessimistic
layout) is worth moving, judged against the brief's report structure (section 15.1) and the text as written.

| Part of 1.2 | Brief requirement | Elsewhere in the main text | Verdict |
| :---- | :---- | :---- | :---- |
| What this milestone does (the two questions, the steps, what is left to later milestones) | Section 15.1 row 1 "Milestone 1 Baseline & Scope"; section 2 "Đầu ra cốt lõi"; the "Không được làm ở Milestone 2" box | Nowhere | Required: stays |
| What the data changed (C01–C08, the four that matter most) | Rubric row 1 "Liên kết Milestone 1 và tính nhất quán của scope / Change Log"; section 3.1; deliverable D | C04–C08 in Section 7.2; C01, C02, C03 only here | Required: stays |
| Closing paragraph (no revision alters goals or decisions) | Rubric row 1 | Repeated in Section 7.2 "What does not change" | Repeated, 3 lines |

Page effect (logs/R21_page_budget.log): the last main-text page is 73% full in English and 20% full in Vietnamese, so
removing the 3 repeated lines (about 0.05 page) saves no page in either language. Decision: no change to Section 1.2;
no translation work follows.
