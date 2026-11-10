# AQ1 and AQ2 completed on both years (T26): from "Partial, 2013 only" to "Answered"

The submitted-to-be report (built at T24) answered AQ1 and AQ2 on the 9 runs of 2013 only and kept the 2014 runs
closed for the single AQ3 test (decision T02, Change Log C14 and the draft C15). On 2026-11-10 the user asked that
AQ1 and AQ2 be solved as completely as possible for Milestone 5, with every limitation acknowledged, and that AQ3 and
AQ4 stay Deferred in the report (their local experiment is not mentioned in it). This record gives the reasoning, the
changes and the checks.

## Why opening 2014 for AQ1 and AQ2 keeps the AQ3 test valid

C14 kept 2014 outcomes away from the choice of AQ3 predictors. That choice (19 predictors, candidate configurations
B1–B3 and M1–M4, selection rule, gate S1) was fixed in Milestone 4 on 2013 alone, so describing 2014 now informs no AQ3
choice. The report states the condition (Section 12, Appendix XV, Table A.8 C15): the AQ3 test on 2014 stays
independent only while the Milestone 4 design is kept; a later change needs a test population not yet seen.
C15 is a Milestone 5 entry not yet submitted, so it was rewritten to state the final decision instead of adding a C18
that reverses it (rule: the report describes the final state only).

## Code (Final Project Package)

- `package/src/analysis/aq_analysis.py --scope 2013|2014|all`; the 2013 output stays byte-identical (21/21 checksums
  before and after the refactor). A module where a sign never occurs gets no sign × module term (CCC, late TMA, 2014).
- `aq2_sensitivity_continuous.py --scope`, `aq_year_compare.py` (results/compare/, AQ2 values refitted to 4 decimals),
  `aq_checks_years.py` (52 PASS), `tests/test_scope.py` (fault injection: removing the module filter fails the test).
- `run_all.sh` steps 12–18; `results/checksums.csv` 62 files; determinism: two runs byte-identical (40 files).
- Task runner `code/run_T26.sh` (logs/T26_*.log); cross-check against the local experiment's replication
  `code/t26_crosscheck_replication.py` (35/35 to 0.01 pp; task trail only).

## Exact rounding

The result CSVs store rounded values (4 decimals for rates, 2 for points), so ties such as 20.25 or 0.4495 rounded the
wrong way. `code/t26_exact_rows.py` recomputes Tables A.29–A.34 from unrounded values (55/56 rows match; the remaining
one keeps the more precise −0.04 of the report) and `code/t26_exact_text.py` checks every rate in the AQ1 text. The
recount also corrected 0.1-point errors inherited from the 2013 tables of T08/T13 (e.g. Fail 26.8% → 26.7%, BBB 45.9% →
45.8%, EEE CI 38.0 → 37.9, GGG fail 31.8% → 31.7%, Table A.34 2013: AAA 67.6 → 67.5, DDD late 15.7 → 15.6, and five CI
bounds; Table A.33 OR 1.40 → 1.39).

## Report changes (English; Vietnamese twins follow)

Sections 1.2, 3 (Tables 3.1, 3.2), 5.1, 6 (Table 6.1), 8, 9, 10, 11.0–11.3, 11.5, 12, 12.1, 13, 14, the abstract and
glossary; Appendices III (C15, statuses), V, IX, X, XI, XII and XIII (rewritten, Tables A.29–A.36 with 2014), XIV, XV
(Table A.42 down to 5 steps), XVI. Figures 11.1 (module × year) and 11.2 (2013 vs 2014, mutually adjusted) redrawn;
Figure 1.1 label. English main text stays at 25.0 pages pessimistic (last page 86% full).

## Findings added (honest limits)

- AQ1: the year difference reverses with the denominator (+2.3 over all enrolments; −0.7 at day 14; −3.5 in the six
  shared modules), because 16.2% of 2014 vs 10.7% of 2013 enrolments were not registered at day 14.
- AQ2: all five signs consistent in both years, differences ≤ 2 points; late TMA in AAA 2014 −1.2 (−14.4 to 12.1);
  with a continuous click adjustment the below-median sign falls to 5.9 (3.7–8.1) in 2014, 4 of 7 modules, weak or
  inconsistent; several-modules sign 28 of 15,724 (27 non-completers), too rare for a list.

## Write full, then move (T26, 2026-11-11, user decision "Full draft, then move")

Sections 11.2 and 11.3 had first been written compact. On the user's question they were rewritten in full (saved
in `research/revisions/03-section-11-full-draft.md`), measured, and moved block by block against the brief
(brief 4.1: Sections 11–12 "2–4 trang", 13–14 "1–2 trang"; ours 6.4 and 2.7 pessimistic). The condensing trims made
before that (Sections 10, 11.2, 12, 14) were reverted. Measurements (`page_budget.py`, English, pessimistic):
full draft 27.0 → after the moves below 25.0 (last page 95% full). Table 11.3 is a landscape section, so only blocks
after it move the last page; blocks before it were moved only as far as the segment needed, and two moved 11.3 blocks
that saved nothing were put back (25.0 unchanged). Restoring the several-modules sentence gives 26.0, so it stays
moved.

| Block | From | To (already there) | Brief element kept in main text |
| :---- | :---- | :---- | :---- |
| All-enrolment shares by year and why they rise | 11.2 | Appendix XII, Table A.29 text | headline rate per year with interval |
| Module order, Feb/Oct numbers, how students leave | 11.2 | Appendix XII, Table A.30 text | module range, Feb > Oct, pointer |
| Runs outside the interval (7/9, 10/13) | 11.2 | Appendix XII, denominator paragraph | "up to 13.6 points" |
| Median first missed week; EEE/GGG composition | 11.2 | Appendix XII, Table A.31 text | shares by week 4 per year |
| Subgroups (disability, deprivation) | 11.2 | Appendix XII; pointer kept | pointer |
| Pooled 22-run AQ2 estimates; overlap of click signs | 11.3 | Appendix XIII, two-year comparison and associations | five signs per year |
| Module intervals mostly in AAA; subgroups | 11.3 | Appendix XIII | exception named |
| Several-modules sign (28 of 15,724) | 11.3 | Appendix XIII; Tables 12.1, A.39 | – |
| D1 list quality (B2), gate, pilot choice | 11.5 | Appendix XIV (D1 paragraph); pointer kept | Table 11.3 implication column |
| Legal duties (Law on AI, high-risk use) [17][18]; adoption [19] | 12.1 | Appendix XV; pointer kept | risk classification named |
| Milestone 5 AI use figures (369 statements, 66 critiques) | 13.1 | Appendix XVI, Table A.43 | AI log pointer, rule |

References renumbered by first citation after the moves (`renumber_refs.py`, both languages).
