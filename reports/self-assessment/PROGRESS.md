# Self-assessment – ledger

## Decisions

- 2026-11-13, user: deliver a lean Word document with the self-assessment table(s) against the briefs' grading criteria
  and a "group comment" on problems met and how they were solved; built with build-report, English source and
  Vietnamese twin.
- Scale instead of points: the briefs give 100 points per milestone but no points per criterion (M1–M4 rubric cells
  "NA", M5 empty), so each criterion is rated Met / Mostly met / Partly met / Not applicable.
- One table per milestone plus a summary table and one problems table.
- 2026-11-13, user: the team comments are the only main content; the rating scale, summary and per-milestone
  assessment move to the appendices word for word (memory rule: write full, then move). Layout: Section 1 Team comments
  (new opening paragraph restating the totals and pointing to the appendices; 1.1 problems, Table 1.1; 1.2 lessons),
  Appendices intro, Appendix I basis and overview (Tables A.1–A.2), Appendix II by milestone (Tables A.3–A.7).
  Edits beyond renumbering: the first and last sentences of Appendix I ("This appendix…", "Appendix II… Section 1")
  and "from the problems in Table 1.1" at the start of 1.2.
- Level 2: rated as the submitted reports state it (M4 Section 7 and M5 Section 10: specified, not run). Open for the
  user: the M4 package holds a run of the 2014 test (`reports/milestone-4/package/logs/06_test.log`,
  `results/s1_gate.csv`, commit d389717) that the reports do not mention; if the reports change, Tables A.2, A.6 and
  A.7 change with them.
- Open for the user: the last row of Table 1.1 says the full Milestone 5 deck with appendix slides exists in English
  only; it changes once the slide count is settled and the Vietnamese deck is built.
- 2026-11-13, rating correction from the reader re-test: Milestone 2 and 3 generative-AI criteria were downgraded for
  page length, which those criteria do not grade (no presentation criterion in either rubric); both are Met. Totals
  37 met / 7 mostly met / 0 partly met of 44 rated, 1 not applicable (M1 6/2/0, M2 8/1/0, M3 10/0/0, M4 6/1/0,
  M5 7/3/0 + 1 N/A); recounted from Tables A.3–A.7 by script in both languages. Milestone 4 "Presentation and
  consistency" keeps length as its limitation; the optional Level 2 no longer downgrades it.
- 2026-11-13, user: Milestone 5 now runs Level 2 (Phong, `reports/milestone-5/CHANGELOG.md`); restructure the form per milestone
  after the user's reference (`self_assessment_reference.md`, not a source of truth), with clear team comments and
  landscape tables. Layout: Section 1 self-assessment by milestone (Table 1.1 per milestone: task, results, contribution
  to the project story, completion and limitations; Table 1.2 coherence on the reference's four aspects), Section 2 team
  comments (Table 2.1 problems, 2.2 lessons, 2.3 overall judgement and next steps), Appendix I basis (Table A.1; the old
  summary Table A.2 dropped as it duplicates Table 1.1), Appendix II per criterion (Tables A.2–A.6). Ratings after
  Level 2: M5 Experimental evidence Mostly met (tuning measure chosen after both results, C18), Findings Met; totals
  38 met / 7 mostly met of 45, none N/A. M5 pages 25.0 EN / 32.0 VI (reports/milestone-5/logs/T36_pages_final.log).
- Skill change: build-report `landscape_tables` layout option (compact documents may rotate text-heavy tables);
  report.py, build_docx.py, templates/tasks.toml, reference.md; `report.py test` run after the change.
- 2026-11-13, user (correction): the main content is the team comments with a milestone column, inspired by the
  reference form, not a criterion-style assessment; detail goes to the appendices. Layout: Section 1 Team comments by
  milestone (opening with the project story from Milestone 1 to 5 and the overall result; Table 1.1 problems with a
  Milestone column, ordered by the milestone where each arose, the two cross-cutting problems last; 1.2 lessons; 1.3
  overall judgement), Appendix I results by milestone (Tables A.1–A.3: per-milestone results and contribution, answers
  to AQ1–AQ4, coherence), Appendix II basis and scale (A.4), Appendix III per criterion (A.5–A.9). Blocks moved word for
  word; only linking sentences and numbers changed. The AQ answers left Table A.1's Milestone 5 cell for Table A.2 because
  the Vietnamese cell wrapped to 24 lines (check_docx limit 20).
- Ratings after the reader tests: M3 Change Log criterion Mostly met (C16: test set kept 13 runs instead of the 9
  paired runs of C07, recorded only in Milestone 5); totals 37 met / 8 mostly met of 45.
- Cross-references in the evidence columns point into the milestone reports; they are listed in
  `[self-assessment.structure] ignore_refs` in tasks.toml.

## Sources of the numbers

| Number in the document | Source |
| :---- | :---- |
| Criteria and their wording | `milestones/01/milestone-1.md` §10, `02` §17, `03` §18, `04` §14, `05` §8 |
| Page lengths (EN/VI): M1 19/21, M2 19/21, M3 27/33, M4 22/28, M5 24/31 | `make pages` logs of the 2026-11-13 reduction round: M1 T36, M2 T53, M3 A10, M4 A10, M5 T35.7 rows of each `PROGRESS.md` |
| Recommended lengths 6–10, 6–10, 8–12, none, 15–25 | the briefs (M1 line 241, M2 §15, M3 §16, M4 none, M5 §7) |
| Milestone 1 evidence (5 stakeholders, 12 critiques 9/2/1, SMART 70%→75%) | `reports/milestone-1/report/02-*`, `03-02-smart-goal.md`, `08-00-genai-reflection.md`; `research/reviews/01-ai-reviewer-decisions.md`; 51 quotes: `PROGRESS.md` T07–T11 |
| Milestone 2 evidence (8 changes, 11 searches / 16 entries / 7 candidates, 10 criteria, critic rounds 12 and 10) | `reports/milestone-2/report/01-*`–`09-*`, Appendix I |
| Milestone 3 evidence (10.9M rows, 19 issues, 22 checks, 55,604 rows, 88 variables, 8 audit findings) | `reports/milestone-3/report/03-*`, `07-*`; `research/reviews/02-ai-leakage-auditor-decisions.md` |
| Milestone 4 evidence (24 critiques, 16 risks) | `reports/milestone-4/report/06-00-genai-usage.md`, Appendix V–VI |
| Milestone 5 findings (45.3% of 28,061; 44.7–45.8; missed task +40.8 / +39.3 points) | `reports/milestone-5/report/11-02-aq1-findings.md` line 8, `11-03-aq2-findings.md` line 8 |
| 7.39% duplicate clicks, 18 of 24 exams, 93 withdrawals without date | `datasets/oulad/exploration/REPORT.md`; `reports/milestone-5/report/06-01-quality-findings.md` |
| 47% late CMA submissions (32,991 of 69,956) | `reports/milestone-3/PROGRESS.md`, Decisions T10 |
| Early-sign rule fires in 1 of 22 runs | `reports/milestone-3/package/data/metadata/change_log.md` C06/C10; `reports/milestone-2/PROGRESS.md` T40 |
| Base rate ≈45% (45.3% day 13, 44.2% day 27) | `reports/milestone-5/report/03-02-aq-revision-log.md` |
| Duplicates move the early-engagement effect by ≤ 0.004 | `reports/milestone-3/PROGRESS.md` T07–T12 |
| Test set 9 paired → 13 runs (C16) | `reports/milestone-5/PROGRESS.md` T05–T09 |

## Tasks

| ID | Task | Status | Evidence |
| :---- | :---- | :---- | :---- |
| S01 | Map rubric criteria to report evidence; harvest problems and resolutions (two read-only agents) | done | agent reports summarised in this ledger |
| S02 | Write English sections and Vietnamese twins; register task | done | `report/`, `tasks.toml` |
| S03 | `make all TASK=self-assessment` | done, exit 0 | `logs/make_all.log` |
| S05 | Stage 1 terms: "brief" = "đề bài" (glossary, 169 uses in M1–M5); four rows added to topics/course-completion-report-conventions.md (grading criterion, main text, self-assessment, rating scale); `glossary.py lint` 0 errors | done | glossary file |
| S06 | Stage 4 native review by a separate reviewer: 54 findings, 57 lines changed; criteria cells verified verbatim against the briefs | done | `research/reviews/01-vi-native-review.md` |
| S07 | Stage 5 reader test: 59 flags (2 / 32 / 25 by clarity 1 / 2 / 3); 37 English source fixes for the flags that were source faults (Milestone 4 length contradiction, missing comparison groups, undefined contact list, "Resolved" status for a half-open problem, 0.004 scale); every flag decided | done | `research/reviews/02-vi-reader-test.md`, `03-vi-rewrite.md` |
| S08 | Reader re-test by a fresh reader: 19 flags (0 / 9 / 10), all fixed or kept with reason; consistency pass (coverage, lint) | done | `research/reviews/04-vi-reader-test.md`, `logs/vi_consistency.log` |
| S09 | Pair-by-pair check of all four EN–VI pairs (structure, rows, numbers per row); fault-tested; 0 pairs with differences, five reviewed differences recorded with reasons | done | `code/check_pairs.py`, `logs/check_pairs.log` |
| S10 | Final `make all` exit 0 (parity 0 errors, 1 justified warning: "datasets" inside a verbatim brief criterion); 8 tables in each language; pages EN 11.7, VI 12.9 pessimistic | done | `logs/make_all.log`, `logs/pages.log` |
| S11 | Skill fix: vi `review.md` "Who speaks" item said "nhóm chúng em / chúng em"; now "nhóm" per lessons S1c | done | `.agents/skills/build-report/languages/vi/review.md` |
| S12 | Restructure: team comments main (Section 1), assessment to Appendices I–II; English edits; stage 1 terms looked up (phụ lục, tiêu chí chấm điểm, phần nội dung chính, đề bài); twins written; parity 0 errors; `check_pairs.py` keys renamed, 0 pairs with differences | done | `report/`, `code/check_pairs.py` |
| S13 | Stage 4 native review of the restructured twins: 34 edits; English fault found ("three-level scale") and fixed | done | `research/reviews/05-vi-native-review.md` |
| S14 | Stage 5 reader test: 46 flags (0/21/25); 37 fixed (about half in the English source: 45-criteria total, page counts per language, OULAD named in Section 1, Change Log, base rate), 9 kept with reasons | done | `research/reviews/06-vi-reader-test.md`, `07-vi-rewrite.md` |
| S15 | Reader re-test: 40 flags (0/20/20); rating correction (M2, M3 GenAI → Met; totals 37/7); every flag fixed or kept with reason | done | `research/reviews/08-vi-reader-test.md`, `09-vi-rewrite.md` |
| S16 | Reader re-test rounds 3 and 4 (13 flags 1/11/1; 11 flags 0/7/4) and a final check of the rewritten passages; every flag fixed (round-4 decisions in `13-vi-rewrite.md`); deck status checked against `reports/milestone-5/build/` (30-slide deck EN+VI; full deck EN only) | done | `research/reviews/10`–`14` |
| S17 | Consistency pass: coverage 9 drifts, "analytics level" fixed, 8 kept with reasons; lint 0 errors. Build: ignore_refs extended with the evidence-column labels that the old numbering had resolved locally (Section 2.1–2.4, Table 1.2/2.1/3.1, VI forms); one voice wording fixed | done | `logs/vi_consistency.log`, `tasks.toml` |
| S18 | Final: `make all` 12/12 + skill tests 2/2, exit 0; 8 tables each language; `check_pairs.py` 0 differences; pages main text EN 4.3, VI 4.6 pessimistic, appendices about 9.5 (EN) | done | `logs/make_all.log`, `logs/check_pairs.log`, `logs/pages.log` |
| S19 | Per-milestone restructure and Milestone 5 Level 2 update: English rewritten (Sections 1–2, Appendices I–II), twins translated, parity 0 errors, `check_pairs.py` 0 differences; landscape tables enabled | done | `report/`, `tasks.toml` |
| S20 | Native review (43 edits) and reader tests of the per-milestone version (26 flags, then 14, then a final check); M3 rating correction; AQ defined | done | `research/reviews/15`–`20` |
| S21 | Team-comments-first layout per the user's correction; English and Vietnamese restructured, parity 0 errors, `check_pairs.py` 0 differences; `make all` 12/12 + tests | done | `report/`, `logs/make_all.log` |
| S22 | Vietnamese flow on the team-comments-first layout: native review 16 edits (one English comma splice fixed), reader test 15 flags (0/11/4) all decided, final check 5 small flags fixed; EN fixes: late-quiz rule, when the test-set gap was found, S1 defined, five signs named, log loss named; `make all` 12/12 + tests exit 0, `check_pairs.py` 0 differences, pages main EN 6.6 / VI 6.7 pessimistic | done | `research/reviews/21`–`24`, `logs/` |
