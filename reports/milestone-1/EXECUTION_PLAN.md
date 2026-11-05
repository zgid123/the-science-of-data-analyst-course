# Execution Plan: Improving Course Completion in Online and Blended Courses: Requirement Analysis and Analytics Project Proposal

Plan date: 2026-11-05. Input outline: [reference.md](reference.md) (the user's concise outline). Output: fine-grained report sections in `reports/milestone-1/report/`, compiled into one Word document by the build-report skill. The work runs as sequential tasks, each verified by its own checklist before the next one starts (Sections 4–7). The machine-readable half of this plan is `plan.toml` (file map, task list, seeds); keep both in step.

## 1. Goal and Scope

The report turns the outline into a formal, evidence-backed report. Every section is expanded with web research, and every factual claim is traced to a source in the reference list through a research trail saved on disk (Section 1.1).

The report is the team's Milestone 1 proposal and follows the brief [S001] task by task. The problem is the brief's "Course completion / dropout" direction (low course completion; students stop taking part mid-semester), set in the brief's starting scenario: a university expanding online and blended learning. Milestone 1 analyses no dataset: data requirements stay conceptual, baselines and targets are labelled assumptions, and open datasets appear only as possible sources. Web research serves two purposes: real-world background for Part 1, and real accounts that ground the simulated stakeholder personas (Part 2, appendices). Research about personas never becomes a fact about the scenario university.

| Outline section | Report part | Included | Brief tasks |
| :---- | :---- | :---- | :---- |
| 1. Project Context and Problem Statement | Part 1 (01-*) | yes | section 3, section 6 row 1 |
| 2. Stakeholder Analysis and Requirement Findings | Part 2 (02-*) | yes | Tasks 1–4 |
| 3. Business Goal, SMART Goal and KPIs | Part 3 (03-*) | yes | Tasks 5–6 |
| 4. Analytical Question Ladder | Part 4 (04-*) | yes | Task 7 |
| 5. Proposed Analytic Approach | Part 5 (05-*) | yes | Task 8 |
| 6. Preliminary Data Requirements and Feasibility | Part 6 (06-*) | yes | Task 9 |
| 7. Decision Supported and Expected Value | Part 7 (07-*) | yes | Task 10 |
| 8. Generative AI Usage and Team Reflection | Part 8 (08-*) | yes | section 6 row 8, section 9 |
| 9. Traceability Matrix | Part 9 (09-*) | yes | section 7 |
| Appendices | 11-* | yes | section 9 |

Page budget: 6–10 pages of main text (Parts 1–9), appendices excluded; main-text files stay near 200–450 words, tables carry the required templates of the brief.

Rules carried over from the project:

- `CLAUDE.md` style: formal report sections, positive framing, cumulative sentences with additive and causal links, full paragraphs, and tables or numbered lists where they help the reader.
- Report text gives the reader information about the subject only, leaving commentary about the report, the outline or the writing process out.
- One topic per file, named `NN-SS-S-slug.md` so that sorting the names lexically gives document order. H1 marks a part, H2 an x.y section, and H3 an x.y.z section.
- APA 7 references, numbered for in-text citation as `[n]` in order of first citation. While drafting, citations use temporary source IDs (`[S101]`); the References task converts them to `[n]`.
- Abbreviations are spelled out at first use and listed in `00-1-abbreviations.md`.
- Scripts run with `./venv/bin/python`; every new dependency is installed in the venv.

### 1.1 Core Rule: Record Every Crawl on Disk

> **What is learned from the web counts once it is written to `reports/milestone-1/research/`.** Every search, every fetched page and every interpretation of that page is saved as a local file *at the moment it happens*, before the next tool call. The report is written only from these files.

| Layer | What is saved | File | Written when |
| :---- | :---- | :---- | :---- |
| 1. Search trail | Every `WebSearch` query, the results kept and dropped, with a one-line reason | `research/search-log.md` (append-only, `trail.py log-search`) | Right after each search |
| 2. Crawl output | The full source converted to readable text by `fetch.py` (or the verbatim `WebFetch` output as a fallback) under a metadata header, the original file as `raw.*`, and every fetch attempt | `research/sources/Sxxx-slug/crawl.md`, `raw.*`, `attempts.md` | Right after each fetch |
| 3. Comprehension | My reading of that crawl: summary, key facts with quote anchors, use in the report, agreement or conflict with the outline, reliability, open questions | `research/sources/Sxxx-slug/comprehension.md` | Right after the crawl is saved |

`research/partN-claims.md` lists one claim per row with its source ID and a verbatim quote anchor; `research/partN-synthesis.md` places the claim IDs under each planned report file. Every report sentence can therefore be followed back along the chain:

```
report sentence [n] → reference entry n → sources.md Sxxx → partN-claims.md claim → comprehension.md → crawl.md quote (→ raw.*)
```

Failed fetches are recorded too: `fetch.py` walks its fallback ladder (retries, other copies of the same work, the Wayback Machine, a metadata record) and logs every attempt in `attempts.md`; a source that stays unusable keeps its folder, and a replacement source is searched for and logged (reference.md of the research-report skill, section 5).

## 2. Tools Used

| Tool | Purpose in this task |
| :---- | :---- |
| `ToolSearch` | Load the deferred `WebSearch` and `WebFetch` schemas once, in the first research task |
| `WebSearch` | Find primary sources, current editions, adoption figures and newer surveys. **Each call is followed by an append to `search-log.md`** |
| `fetch.py get` (research-report skill) | Download a source and convert it to readable text with retries and fallbacks; writes `crawl.md`, `raw.*`, `attempts.md` |
| `fetch.py meta` / `find` | Bibliographic record (Crossref, OpenAlex) for APA entries and citation counts; title search for other copies |
| `WebFetch` | Fallback for pages `fetch.py` cannot read; ask for verbatim passages and save the output as a fetch block in `crawl.md` |
| `Read` | Read a PDF that no converter can read (page ranges), the trail files and drafts |
| `Agent` (general-purpose, foreground) | One subagent per research task; it writes its own trail files and returns at most 5 status lines |
| `Write` / `Edit` / `Bash` | Trail files, report sections, gate commands |
| `trail.py` (log-search, register, comprehension, claim, apa) | Exact trail entries: row numbers, dates, claim IDs, verified anchors, APA drafts |
| `check_trail.py`, `check_drafts.py`, `finalize_refs.py`, `spot_check.py`, `progress.py` (status, next, set, prompt) | Research-report gates and tools |
| build-report skill (`make precheck/build/postcheck TASK=reports/milestone-1`) | Format, structure, abbreviation and citation checks; Word build; Word post-check |
| `AskUserQuestion` | Human verification on any failed checklist item, any conflict with the outline, and at the checkpoints (Section 8) |

## 3. Target File Map (`reports/milestone-1/report/`)

### 3.1 Front Matter

| File | Content |
| :---- | :---- |
| `00-0-title-page.md` | Institution, course, report title, group and lecturers (details from the user at the scope checkpoint) |
| `00-1-abbreviations.md` | Abbreviations as they appear (built from the text in the Front matter task) |
| `00-2-glossary.md` | Defined terms with section pointers |

### 3.2 Main Text and Appendices

| File | Content | Evidence |
| :---- | :---- | :---- |
| `01-00`, `01-01`, `01-02` | Scenario; real-world background on non-completion and mid-semester disengagement; problem statement, scope, need for analytics | T04 (S100–S199), S001 |
| `02-00` … `02-04` | Stakeholder map (Task 1); interview approach and personas (Tasks 2–3); synthesis table and themes (Task 4); conflicts, constraints and validation table | T05–T11 interview records, S200–S299 |
| `03-00` … `03-03` | Business Goal (Task 5); SMART Goal with assumed baseline; 1 primary and 2 secondary KPIs (Task 6) | interviews, synthesis |
| `04-00` … `04-02` | AQ ladder at four levels; five-criteria table; Before → After (Task 7) | interviews, AI review |
| `05-00` | Analytics type, candidate technique family and expected output per AQ (Task 8) | S001 table, S004–S006 |
| `06-00` … `06-02` | Preliminary data requirements per AQ (Task 9); access, quality risks, privacy and ethics | S002, S003, S007, S008 |
| `07-00` | Decision supported, users, decision level, expected value (Task 10) | S010–S013, interviews |
| `08-00` | AI roles, accepted and rejected suggestions, what needs real evidence | T16 review log |
| `09-00` | Traceability matrix (brief section 7) | Parts 3–7 |
| `11-01` … `11-04` | Question lists; interview excerpts; validation round; AI critique → team decision → reason table and reviewer prompt (brief section 9) | interview and review records |

Interview records live in `research/interviews/`: `personas/<role>.md` (persona card with its sources), `questions/<role>.md` (team question list), `<role>.md` (transcript with statement labels), `validation-<role>.md`, `synthesis.md`. Each persona is played by its own isolated subagent that sees only the brief's role prompt (section 4.2), the scenario and its persona card; the main agent, acting as the team, asks one question at a time and follows up.

### 3.N Back Matter

| File | Content |
| :---- | :---- |
| `NN-references.md` | APA 7, numbered `[n]` in order of first citation; seeds from the outline verified, plus new sources |

## 4. Sequential Task Protocol

Every task, whatever its kind, runs the same seven-step loop:

```
1. LOAD    Read the ledger and the input files named in the task card, and only those.
2. DO      Carry out the card's actions with the tools it names.
3. WRITE   Save every output to the files the card names.
4. VERIFY  Tick each checklist item against the saved files or a command output.
5. DECIDE  All items ticked     → go to step 6.
           Any item unticked    → STOP. Set status "blocked", write the failing items and a question
                                  in the ledger, ask the human (AskUserQuestion) and wait for:
                                  continue / redo / skip / stop.
6. CLOSE   Mark the task "done" in the ledger, with the date and a handoff note of at most 8 lines:
           the output files, key facts or numbers, decisions, and anything the next task must know.
7. FREE    Drop the working context. The next task picks up only the ledger and the files its card names.
```

Rules of the loop:

1. **Verification is evidence-based.** An item counts as ticked only when a saved file or a command output shows it.
2. **Fixes happen before verification.** Once step 4 shows a failing item, the task stops and the human decides how to continue, so every retry is a visible decision.
3. **Human decisions are recorded** in the ledger under `Decisions`, so a later session can see why a task continued, was redone or was skipped.
4. **Planned checkpoints stop even on success** (Section 8).
5. **Freeing space is built in:** research tasks run inside one foreground subagent whose context is discarded; writing tasks read only the synthesis entry, the `comprehension.md` files and the outline lines of their card (`outline.py --section`); the handoff note is the only memory passed between tasks; at each checkpoint the user may run `/compact` or `/clear`.
6. **Resume rule.** A new session starts with `progress.py --base reports/milestone-1 next` and continues with the first task that is not `done`. A task left `in-progress` is re-entered at step 4 (verify what is already saved).
7. **One task at a time by default.** Independent tasks may run concurrently when the plan names the wave and shows why they cannot affect each other (skill reference.md section 1.4).
8. **Source IDs are reserved per part:** Part 1 S100–S199, Part 2 S200–S299, …; outline seeds are S001–S0nn.

## 5. Progress Ledger (`reports/milestone-1/PROGRESS.md`)

The ledger is the single record of where the work stands, updated at steps 5 and 6 of every task (`progress.py set`). Status values: `todo`, `in-progress`, `blocked`, `done`, and `skipped` (set only by a human decision).

## 6. Task Templates

The checklists of the three task kinds (R research, W writing, F figure), the finishing tasks and the human checkpoints are fixed in the research-report skill's `reference.md` (sections 3 and 4). Each card in Section 7 adds only its own inputs, outputs, research questions and extra checks.

## 7. Task Cards

### 7.1 Stage A: Setup

**T01: Scaffold the workspace and register the task.**
- **Do:** `scaffold.py build --base reports/milestone-1`, then `scaffold.py register --base reports/milestone-1`.
- **Checklist:**
  - [ ] `scaffold.py check --base reports/milestone-1` reports 0 errors.
  - [ ] `tasks.toml` has the `[<task>]` table; `make build TASK=<task>` builds the skeleton cleanly.

**T02: HC, scope inputs.**
- **Do:** ask the human for the title-page details, the inclusion of any outline section marked optional, the report language(s), and every ambiguity found in the outline.
- **Checklist:**
  - [ ] Every answer is recorded under `Decisions` in the ledger, and the plan is updated where an answer changes it.

**T03: Seeds.** Carry the reusable sources of the archived trail (`.cache/milestone-1-old/research/sources/`) into this trail as seeds S001–S013 with their crawls and comprehension notes; `check_trail.py --all` 0 errors.

### 7.2 Stage B: Research (wave T04–T06, concurrent)

The three research tasks run as one wave: disjoint ID blocks (S100–S199, S200–S249, S250–S299), disjoint claims files (part1, part2 rows written only through `trail.py`), and no input from each other.

| ID | Outputs | Research questions |
| :---- | :---- | :---- |
| T04 | part1-claims, part1-synthesis (01-01, 01-02) | Q1 How large is course non-completion and withdrawal in online and blended higher education, internationally and in Vietnam, as of the latest data? Q2 When in a course or semester do students typically disengage, and what early signs do institutions observe? Q3 What reasons do studies and student surveys give for not completing a course? Q4 Which data do universities typically hold for this (LMS, academic records, assessments, surveys)? |
| T05 | part2-claims (S200–S249), persona notes for Student and Lecturer | Q1 In their own words (surveys, interviews, published accounts, forums), why do students stop taking part in online or blended courses mid-semester, and what support did they want or reject? Q2 How do lecturers notice disengagement, what do they do about it, what limits them (class size, time, tools), and how do they view predictive dashboards? |
| T06 | part2-claims (S250–S299), persona notes for Advisor, Program Manager, Learning technology and data staff | Q1 How do academic advisors and student support staff run early-alert work: caseloads, outreach, response rates, false alarms, student reactions? Q2 What do program managers track (completion, retention, KPIs), what decisions they own and what pressures they face? Q3 What do LMS administrators and institutional research staff say about data access, data quality and privacy for learning analytics? |

### 7.3 Stage C: Interviews (sequential)

| ID | Actions | Checks |
| :---- | :---- | :---- |
| T07 | One persona card per role in `research/interviews/personas/`: role, setting, experience, priorities, constraints, typical worries, each trait citing a source ID; traits without a source marked "scenario assumption" | Every trait sourced or marked; no numbers about the scenario university stated as facts |
| T08 | Stakeholder map hypotheses (Task 1 table); 5–8 open, non-leading questions per role covering the five information groups (Task 2) | Each list covers all five groups; no leading question (self-check logged) |
| T09 | One isolated subagent per persona with the brief's prompt (section 4.2); questions asked one at a time; follow-ups when vague or contradictory; transcript saved verbatim with labels (opinion, assumption, scenario information) | ≥ 1 follow-up per interview; every key statement labelled |
| T10 | Organize (Task 4 table) → themes → prioritize → refine into a problem statement | Themes trace to labelled statements |
| T11 | Return to each persona conversation with the team's understanding; record confirmed, adjusted and rejected points (validation table) | Every persona validated |

### 7.4 Stage D: Writing

| ID | Files | Must contain |
| :---- | :---- | :---- |
| T12 | 01-* | Scenario, real-world background with sources, problem statement, scope, need for analytics |
| T13 | 02-* | Task 1 table, interview approach, Task 4 synthesis table, themes and priorities, conflicts, validation table |
| T14 | 03-*, 04-* | Business Goal with origin and decision; SMART table with assumed baseline; KPI table; AQ ladder; five-criteria table; Before → After |
| T15 | 05-00, 06-*, 07-00 | Task 8 table; Task 9 table; feasibility, quality risks, privacy; decision levels and expected value |
| T16 | research/review/ | Reviewer prompt run by an isolated subagent on Parts 1–7; each critique → team decision → reason; fixes applied |
| T17 | 08-00, 09-00, 11-* | AI usage and reflection; traceability matrix; appendices of brief section 9 |

### 7.N Stage F: Finishing

The finishing cards follow the skill's reference.md section 4.3: front matter (T18), references (T19), full gates (T20), fact spot-check (T21), style read-through (T22), build and post-check of the English document (T23), English review (T24). The Vietnamese twin follows build-report reference.md section 4.3 (T25: terms, front matter, translators, native review by a different agent, consistency pass, reader test), then every language is built and post-checked (T26) before the final review (T27).

## 8. Human Checkpoints

| When | Why it stops |
| :---- | :---- |
| Any unticked checklist item (any task) | The user decides how to continue |
| Any conflict with the outline (R7) | The human owns the content of the outline |
| Scope inputs (T02) | Details needed before writing |
| End of each part | Part review; a natural point for `/compact` or `/clear` |
| Final review | Acceptance |

## 9. Deliverables

| Deliverable | Location |
| :---- | :---- |
| Plan and ledger | `reports/milestone-1/EXECUTION_PLAN.md`, `reports/milestone-1/plan.toml`, `reports/milestone-1/PROGRESS.md` |
| Section files | `reports/milestone-1/report/*.md` |
| Research trail | `reports/milestone-1/research/` (search log, register, claims, syntheses, sources with crawls and comprehension, spot-check, style review) |
| Word report | `reports/milestone-1/build/N04_Milestone1_EN.docx`, `N04_Milestone1_VI.docx` and their `_GoogleDocs` copies |
