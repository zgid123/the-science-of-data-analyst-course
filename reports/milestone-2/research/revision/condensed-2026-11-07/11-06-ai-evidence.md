## Appendix VI – Generative AI Usage Evidence

An AI agent searched for candidate datasets for the team with the prompt below, in which documents are named by the report section that holds them and the agent's file-handling steps are left out; every query it ran is in Appendix I, and every fact it recorded was checked by team members against the saved official page.

Prompt of the search strategist and metadata interpreter:

```text
You are the research agent for the dataset search of the MTH045 Milestone 2 report ("From requirements to collection").

1. Record every search, fetch and interpretation before the next step, and anchor every fact in a verbatim quote from its source.
2. Read the team's data requirements and the must-have gates G1–G5 (Section 2) and the brief sections 7–8 and 13. Build search keywords from the requirements (e.g. student completion, dropout, withdrawal, LMS/VLE interaction, assessment submission, clickstream, higher education, learning analytics, MOOC dropout).
3. Find and document at least six candidate open education datasets from official sources (landing page, DOI, repository of the provider, or the original paper), reading the documentation/data dictionary and license page of each before judging it. Include at least: OULAD (official page https://research.stem.open.ac.uk/ouanalyse/dataset/ and the Scientific Data paper), UCI "Predict Students' Dropout and Academic Success" (id 697), UCI "Student Performance" (id 320), UCI "Higher Education Students Performance Evaluation" (id 856), and at least two more found by your own search (for example KDD Cup 2015 / XuetangX MOOC dropout data, MOOCCubeX, EdNet, HarvardX-MITx person-course data, xAPI-Edu-Data). When a dataset is found via Kaggle/blog/GitHub, trace it to the official source or record that provenance is unclear.
4. For each candidate record facts with quote anchors: provider/authors, official URL/DOI, license or terms, version/release date, population and context (level, country, years), unit of analysis, outcome/target available (does it separate pass, fail and withdrawal?), within-semester timing (dated activity or dated assessments? granularity), number of semesters/course runs, size (rows/records), file formats, documentation available, anonymisation, sensitive attributes, citation. Only facts found on the source pages; write "not stated" otherwise.
5. Write one section per candidate with those fields, each fact followed by its source, and a short note per gate G1–G5 (met / partly / not met / unclear, with the evidence). Also write the brief's Search Log table (| Date | Query / source | Candidate dataset | URL/DOI | Reason considered | Result |), one row per query/candidate examined, including rejected ones.
6. Do not download any dataset.

Return at most 6 lines: candidates documented, sources fetched/partial/blocked, facts recorded, gate result per candidate in one line, unresolved questions.

Follow-up message sent during the task: the must-have gates were revised (G1 also requires a dated withdrawal; G2 split into G2a dated assessed tasks and G2b dated activity; G3 at least three course runs ordered in time with a later run for testing; G5 adds a persistent pseudonymous identifier); write the gate notes against the revised gates and note early tasks and enrolment dates per candidate.
```

Two isolated AI agents critiqued the work at fixed points: a requirement critic before any dataset was scored, and a selection reviewer after the scoring. Each received only the brief and the team's documents named in its prompt. Their prompts are given in English, with documents named by the report section that holds them; Tables A.11 and A.12 give each critique in short form with the team's decision and the change made.

Prompt of the requirement critic:

```text
You act as the "Requirement critic" role that the MTH045 Milestone 2 brief allows for generative AI (brief section 12: "Chỉ ra AQ nào cần timestamp, target, intervention data hoặc có leakage risk"). Read only: the brief, the team's frozen Milestone 1 baseline (Section 1.1) and the team's data requirements (Section 2). Do not read any dataset file or exploration result, and do not search the web.

Critique the data requirements: for each AQ, is anything missing (timestamps, target definition, denominator, prediction point, intervention data), is any requirement written as a dataset's column rather than a concept, is there leakage risk not covered, are the must-have gates G1–G5 right (too strict, too loose, missing one), and are the requirements consistent with the baseline (KPIs, decisions)? Do not propose datasets and do not rewrite the document.

Write at most 12 numbered critiques, most important first, each with: the passage (quote a few words), the problem, why it matters.
```

Table A.11 lists the requirement critic's twelve critiques with the team's decisions.

**Table A.11. Requirement critic: AI critique, team decision and change**

| # | Critique (short) | Decision | Change |
| :---- | :---- | :---- | :---- |
| Q1 | Withdrawal date only nice-to-have, though AQ3 needs it | Accepted | G1 now requires a dated withdrawal |
| Q2 | G2 accepts dated activity alone; AQ3 rule and secondary KPI 1 need dated tasks | Accepted | G2 split: G2a dated assessed tasks and submissions, G2b dated learning-platform activity; tasks due in weeks 1–4 is a nice-to-have, reported per module run |
| Q3 | KPI denominator (add-drop, leave, transfer) not required | Accepted | Enrolment start and end dates relative to the course start are minimum variables; leave/transfer distinction stays optional and its absence is recorded as a KPI deviation |
| Q4 | Year of study and delivery mode optional though AQs name them | Partly accepted | They stay optional, because a gate no open dataset can meet would leave only synthetic data, which the brief forbids; the clauses that become Partial without them are declared now |
| Q5 | G3 three runs against AQ1 four semesters; no time order | Accepted | G3: at least three course runs ordered in time, a later run available for testing; AQ1 is Partial with fewer than four semesters |
| Q6 | Missing leakage paths (course average, mark release, study load, updated background, normalisation) | Accepted | Leakage table extended with five rows |
| Q7 | Missed tasks counted after withdrawal | Accepted | Rule: a task counts as missed only if due before the student's withdrawal date |
| Q8 | Week numbering and data delay unspecified | Accepted | Course start date is a minimum variable; the cut-offs (ends of weeks 2 and 4) already leave one week for the data delay before the lists in weeks 3 and 5 |
| Q9 | No gate for identifiers that link across tables and courses | Accepted | G5 requires a persistent pseudonymous student identifier across tables, courses and semesters |
| Q10 | No volume or outcome-distribution requirement | Partly accepted | Nice-to-have: at least 100 later non-completers per compared group in the test run (an assumption to confirm in Milestone 3) |
| Q11 | AQ4 mixes data and assumptions; advisor assignment missing; contact record known not to exist | Accepted | Capacity labelled as a baseline assumption; advisor assignment added as optional; one list entry per student across courses; contact record declared a gap now; referral data marked sensitive |
| Q12 | Wording names fields or systems; grade mapping unclear | Accepted | Concept wording ("withdrawal indicator and date", "enrolment start and end dates", "dated learning-platform activity"); any passing grade, including higher grades, counts as completion |

Prompt of the selection reviewer:

```text
You act as the "Selection reviewer" role that the MTH045 Milestone 2 brief allows for generative AI (brief section 12: "Phản biện Dataset Selection Matrix và phát hiện criteria bị bỏ sót"; "Không chấp nhận recommendation nếu không có evidence"). Read only: the brief, the requirements and gates (Section 2), the candidate facts with their sources and verbatim quotes, and the team's scoring and decision (Section 4). Check that each score rests on a recorded fact. Do not search the web and do not open any dataset file.

Challenge the selection: scores not backed by a recorded fact, criteria applied inconsistently across candidates, gates that were misread, a candidate rejected or kept for a weak reason, a criterion the brief lists that is missing, a supplementary dataset that should have been considered, and anything about the selected dataset that the team treats as settled without evidence. Do not rescore the matrix yourself and do not propose new datasets unless you name the evidence gap they would close.

Write at most 10 numbered critiques, most important first, each with the passage, the problem and why it matters.
```

Table A.12 lists the selection reviewer's ten critiques with the team's decisions.

**Table A.12. Selection reviewer: AI critique, team decision and change**

| # | Critique (short) | Decision | Change |
| :---- | :---- | :---- | :---- |
| S1 | G3 treated as passed, uncertain per module | Accepted | Selection conditional on the structural check; fallback named |
| S2 | G5 "Partly" missing from the gate decision | Accepted | Conditional on the structural check; Partial clauses named |
| S3 | Outcome classes claimed without a recorded fact | Accepted | Outcome scored 1; pass/fail values checked in the structural check |
| S4 | Feature timing scored 2 with open conditions | Accepted | Scored 1; mark release, unsubmitted tasks and early tasks noted |
| S5 | High-failure module selection ignored | Accepted | Added to population fit, ethics and rationale |
| S6 | Inconsistent scoring of "not stated" and gate lists | Accepted | "Not stated" scores 0 everywhere; HarvardX fails G4; xAPI G4 unclear; the recorded fact named for every score; unsupported figures removed |
| S7 | AQ coverage 2 despite Partial clauses | Accepted | Scored 1 |
| S8 | No version number, two distribution points | Accepted | Documentation scored 1; the acquisition records which copy and its checksums |
| S9 | Denominator not tested | Accepted | The structural check counts unregistration on or before day 0 |
| S10 | Supplementary dataset reasoning | Accepted | Real blocker for XuetangX (license, outcome) named; external-validity check recorded as an open limitation |
