# AI selection reviewer output (T09)

Role: "Selection reviewer" (brief section 12). Inputs read: `final-project/milestones/02/milestone-2.md`,
`research/requirements/data-requirements.md`, `research/search/candidates.md`, `research/selection/selection.md`,
`research/part3-claims.md`. No web search; no dataset file opened. Totals in `selection.md` section 1 were re-added
and all seven match the row scores (17, 9, 7, 8, 9, 9, 4). Critiques, most important first.

1. **G3 is treated as passed, but the recorded facts make it doubtful per module.** Passage: "Gates failed: none
   (G5 linkage across runs to confirm in the data)" and "the only candidate that passes the outcome, timing, history
   and licence gates" (`selection.md`). Problem: G3 requires "at least three runs of the same courses" and AQ1 asks for
   "at least four consecutive semesters" (`data-requirements.md` sections 1 and 5). The only facts recorded are 22
   presentations over seven modules (C3-005) and the advice to analyse B and J presentations separately (C3-061);
   presentations per module are "not stated" (`candidates.md`, OULAD "Number of runs"). 22 / 7 ≈ 3.1 runs per module,
   so at least one module has three runs or fewer. If B and J runs must stay apart, a module with three runs may hold
   only one or two of the same type. Why it matters: the history gate decides AQ3's time-based train/test design and
   AQ1's four-semester window. "Met (per module to confirm)" is an open question, and the decision states it as passed.
   It should read "conditional on Task 6", and the decision should name the fallback if few modules qualify:
   narrow AQ3 to those modules, or relax the B/J separation with a stated reason.

2. **G5 is "Partly" in the candidate screening but drops out of the gate decision.** Passage: `candidates.md` gives
   OULAD "G5 Partly", saying "persistence of the identifier across runs is not stated explicitly". In `selection.md`,
   the "Gates failed" row says "none". Problem: G5 is a must-have, and a must-have that is only partly met is not a
   pass. Persistence is inferred from `num_of_prev_attempts` (C3-064). That field shows the provider knew of earlier
   attempts. It does not show that the released, randomised `id_student` (C3-012) stays the same across
   presentations. Why it matters: two requirements depend on it. One is the AQ2 sign "missed tasks in several courses
   in the same semester", which links one student across modules. The other is the "one list entry per student across
   courses" in AQ4. If the identifier is not stable, both fall to Partial. The decision should say the selection holds
   only if Task 6 confirms G5, and which AQ clauses become Partial if it does not.

3. **The G1 outcome classes in the matrix are not backed by a recorded claim.** Passage: "2 – pass, distinction,
   fail, withdrawn per enrolment, dated withdrawal" (`selection.md`, Outcome / target, OULAD). Problem: `candidates.md`
   states "The full list of result values is not stated in the pages read" and "Pass and fail values to be confirmed
   in the local data". The only recorded value is Withdrawal (C3-008). "Distinction" and "fail" appear in the matrix
   without a claim ID. Why it matters: G1 is the first must-have, and its pass/fail separation is the part not yet
   evidenced. The brief rejects recommendations without evidence (section 12). The cell should list only the values
   that C3-008 records, or it should cite a claim added from the data descriptor's variable definition.

4. **Feature availability and timing scores 2, but the requirements' leakage rules cannot yet be checked.** Passage:
   "2 – dated assessments, submissions, daily clicks" (`selection.md`). Problem: `data-requirements.md` section 3 allows
   "Scores only when the mark was known by the cut-off". The recorded facts give a cut-off day (C3-009) and a
   submission day (C3-010), but no date when a mark was released. In addition, "If the student does not submit the
   assessment, no result is recorded" (C3-016). A missed task therefore has to be built from the assessment list, not
   observed as a row. Whether any task falls due in weeks 1–4 is "Not stated (check in data)" (`candidates.md`
   summary). A presentation typically lasts nine months (C3-017), while the requirements assume semester weeks 1–4.
   Why it matters: the AQ2 and AQ3 early signs ("missed and late assessed tasks in weeks 1–4") rest on these four
   points. If no tasks fall due early, or marks cannot be timed, AQ3 at the week-2 cut-off relies on clicks alone.
   A score of 2 ("well met") hides three open conditions.

5. **The documented selection of modules with high failure is missing from population fit, ethics and the
   rationale.** Passage: "Its weak points are known in advance: population fit (UK distance learners, 2013–2014...)"
   (`selection.md` section 3). Problem: C3-015 records that modules were chosen partly because "The module has a
   significant number of failing students". `candidates.md` lists this under Population and context, but neither the
   Population fit cell nor the Ethics and representativeness cell nor the decision mentions it. Why it matters: AQ1's
   pass, fail and withdrawal shares and AQ4's precision ("share of listed students who later fail or withdraw") depend
   on the base rate. Seven modules picked for high failure will show higher non-completion rates than a typical
   program. This limit on generalisation belongs in brief section 8 ("Có hạn chế khi khái quát sang bối cảnh khác?")
   and in report section 8.

6. **The same evidence status gets different scores and gate readings across candidates.**
   - Ethics "not stated" scores 1 for C, D and E but 0 for G.
   - Temporal coverage "unclear" scores 0 for B, although eleven cohorts are recorded (C3-026) and G3 is "Unclear".
     It scores 1 for E, whose "runs unclear".
   - In the "Gates failed" row, E fails G4 for having no licence. F has no named open licence either ("Dataverse
     Community Norms", C3-055), and its G4 status is "Partly" in `candidates.md`, yet G4 is not listed among F's
     failed gates. G's G4 is "Unclear", and its listed failures leave G4 out with no stated reason.
   - The matrix cites no claim IDs, and two size facts it relies on carry none in `candidates.md`: "1.6 GB logs"
     (S305) and HarvardX's 338,223 records ("not a stated sentence").
   - The brief-format matrix (section 2) has no column for Temporal coverage or Unit and granularity. As a result, the
     history criterion behind G3 cannot be seen there.

   Why it matters: none of these changes the outcome, since every rejected candidate fails G1. They do weaken the
   claim that "each candidate was evaluated by the same set of criteria" (brief section 8). A grader can find each one
   by reading the matrix against `candidates.md`. One rule for "not stated" and claim IDs in the cells would close it.

7. **AQ coverage scores 2 ("well met") while several required clauses for AQ1–AQ2 are not shown in OULAD.** Passage:
   "2 – AQ1–AQ3 data present; AQ4 ranking only". Problem: the requirements make several items AQ dimensions or
   signs: delivery mode, year of study, attendance, concurrent courses, and the leave or transfer distinction
   (`data-requirements.md` sections 1 and 6). Section 3 of the selection itself lists delivery mode, year of study and
   attendance as missing. AQ4 is described as "ranking only", which corresponds to Partial in brief section 11.1.
   Why it matters: 2 means coverage is enough "cho mức analytics đã cam kết" (brief section 8). With AQ4 Partial and
   several AQ1–AQ2 comparisons Partial, the score overstates coverage and predicts the traceability table (Task 7)
   too optimistically. Either score 1 with the reason, or define 2 as "core clauses met" and list the Partial clauses.

8. **Version and provenance are scored 2 with no version and two distribution points.** Passage: "2 – provider page,
   peer-reviewed descriptor, DOI" (Documentation) and "Met" for G4. Problem: the provider offers "the latest version"
   with no version number (C3-004). UCI holds a copy donated on 20 December 2015 under its own DOI (C3-018). Nothing
   recorded says the two copies are identical, or which one the team will download. Why it matters: Task 5 requires
   Version / release and integrity evidence, and brief section 13 asks the team to "ghi provenance về nguồn gốc"
   when a dataset appears on several sites. The selection should name the source copy it relies on. If the two copies
   cannot be compared, the open point goes into the acquisition plan, not under a settled "2".

9. **The denominator of the primary measure is not tested against OULAD.** Passage: AQ1 population "Students
   enrolled after the add-drop period" and the optional "student status (approved leave, transfer)"
   (`data-requirements.md`). In `selection.md`, OULAD's G1 is "dated withdrawal". Problem: the recorded facts are a
   registration day and an unregistration day relative to the presentation start (C3-063). No recorded fact says
   whether unregistration can come before the start, or whether OULAD has an add-drop period, leave or transfer.
   Why it matters: the AQ1 shares and the primary KPI depend on who is in the denominator. If early unregistrations
   count as Withdrawal (C3-008), withdrawal rates rise compared with the team's add-drop rule. The selection should
   record this as a Task 6 check: unregistration days ≤ 0 and how they are counted. It should also add leave and
   transfer to the gap list (see 10).

10. **The supplementary-dataset decision rests on an incomplete gap list and a reason that does not apply.** Passage:
    "The only data the proposal still lacks after OULAD are a contact record, staff capacity, delivery mode, year of
    study and attendance; ... none shares keys or context with OULAD". Problem: the list leaves out leave and transfer
    (`data-requirements.md` section 6) and depends on G5 for concurrent courses. It also does not cover the largest
    weakness the team itself names, population fit. A supplementary dataset for that weakness would not need shared
    keys: it would serve as a second population to check whether the AQ2 activity signs hold outside one UK distance
    provider. On the recorded evidence the only candidate with dated activity is XuetangX, which meets G2b (C3-046)
    and fails G4 (no licence stated, S305). The correct reason to rule it out is therefore the licence, not keys. Why
    it matters: brief section 11.1 allows a supplementary dataset when "compatibility, keys/context hợp lý và license
    phù hợp" are met. Stating the actual blocker, together with the full gap list, shows the option was considered
    and records the external-validity gap as an open limitation rather than settled.
