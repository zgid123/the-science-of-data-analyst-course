# Part 2 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 02-00-data-understanding.md

**Claims:** C2-001, C2-010, C2-013, C2-022 (task T05; overview claims only, details in 02-01 to 02-03)

**Outline:**
- OULAD as OU module-presentations: assessment types TMA, CMA and Exam (C2-001), presentations named by start month (C2-010).
- All times are relative days from the presentation start (C2-013).
- Seven tables joined by student, module-presentation, assessment and site keys (C2-022); lead into the Dataset Understanding Map.

**Conflicts with the outline:** None.

**Gaps:** None from T05.

## 02-01-population-unit-keys.md

**Claims:** C2-010, C2-011, C2-012, C2-022

**Outline:**
- code_presentation = year + start month letter; B = February, J = October (C2-010, C2-011).
- B and J presentations should be analysed separately, which affects pooling across presentations (C2-012).
- Join keys between the seven tables (C2-022); the unit of analysis is student × module-presentation.

**Conflicts with the outline:** None. Side note for the descriptor S002: its dataset URL (analyse.kmi.open.ac.uk/open_dataset) now redirects to the OU Analyse home page; the description lives at research.stem.open.ac.uk/ouanalyse/open-dataset-more/ (S206; S205 documents the redirect).

**Gaps:** None.

## 02-02-outcome-time-measures.md

**Claims:** C2-013, C2-014, C2-015, C2-016, C2-007, C2-008, C2-001, C2-002, C2-003, C2-004, C2-005, C2-006, C2-009, C2-019, C2-018, C2-017, C2-020, C2-021

**Outline:**
- Time axis: day 0 = official module start; length runs from module start to end; registration up to two weeks after start and VLE content before start, so negative days are valid (C2-013, C2-014, C2-015, C2-016).
- Assessment date = cut-off (deadline) day in days since start (C2-007, C2-008).
- When a score is known: TMA marked by the tutor, usually returned within ten working days after the cut-off; TMA extensions possible; CMA/iCMA marked automatically, no submissions after the cut-off, score expected within 7 days; deadline midday + grace to 23:59 (C2-001 to C2-005). Rule for features: a score is usable at cut-off day t only if its assessment cut-off day plus the marking lag is ≤ t (about +14 calendar days for a TMA, about 0–7 days for a CMA); date_submitted alone is not the day the score was known.
- Exam results usually missing; weights: exam 100%, other assessments sum to 100% (C2-006, C2-009); score 0–100, < 40 = fail (C2-019).
- is_banked = result carried over from a previous presentation, not earned in the current one (C2-018); date_unregistration empty for completers, withdrawal recorded in final_result (C2-017).
- VLE: sum_click per student × material × day; activity_type = role of the material; week_from/week_to = planned weeks (C2-020, C2-021).

**Conflicts with the outline:** None. With the descriptor: S002 calls the assessment `date` "the cut-off day", S206 "the final submission date" – same meaning, wording differs.

**Gaps:** The marking timeline is from the OU policy effective July 2025 (S201); the 2013–2014 rule is not documented (C3-016). The marking lag is a working-day target, not a recorded date: OULAD has no "score released" date.

## 02-03-codes-sensitive.md

**Claims:** C2-023, C2-024, C2-025, C2-026, C2-027, C2-028, C2-029, C2-030, C2-031, C2-032

**Outline:**
- imd_band = IMD band of the student's home area; descriptor cites the English Indices of Deprivation 2015 Technical Report (C2-023).
- English IMD: England-only ranking of 32,844 LSOAs in ten deciles from 37 indicators in seven domains, mostly 2012/13 data; area measure, not a person measure (C2-024 to C2-027).
- Scotland, Wales and Northern Ireland use their own indices on their own areas; bands are not comparable across nations, and the Republic of Ireland has no UK IMD – so imd_band for the Wales, Scotland and Ireland regions is either from another national index or missing (C2-028, C2-029).
- Anonymisation generalised age and IMD band (quasi-identifiers, k = 5) (C2-030).
- studied_credits = all credits currently studied; 60 = part-time year (16–18 h/week), 120 = full-time year (32–36 h/week) (C2-031, C2-032).

**Conflicts with the outline:** None.

**Gaps:** No source states which IMD edition (2010 or 2015) or which national index the OU used for students outside England, or how the OULAD "Ireland" region is defined (Northern Ireland only or also the Republic). To be checked in the data: missing imd_band by region.
