# Execution Plan: Final Integration and Project Report: Early Identification of Disengaging Students in Online Courses

Plan date: 2026-11-08. Input outline: [reference.md](reference.md) (the user's concise outline). Output: fine-grained report sections in `reports/milestone-5/report/`, compiled into one Word document by the build-report skill. The work runs as sequential tasks, each verified by its own checklist before the next one starts (Sections 4–7). The machine-readable half of this plan is `plan.toml` (file map, task list, seeds); keep both in step.

<!-- FILL: every "FILL" comment marks content this report needs; delete the comment once filled. -->

## 1. Goal and Scope

The report turns the outline into a formal, evidence-backed report. Every section is expanded with web research, and every factual claim is traced to a source in the reference list through a research trail saved on disk (Section 1.1).

<!-- FILL: map every outline section to a report part, or mark it "not included" with the reason. -->

| Outline section | Report part | Included |
| :---- | :---- | :---- |
| | | |

Rules carried over from the project:

- `CLAUDE.md` style: formal report sections, positive framing, cumulative sentences with additive and causal links, full paragraphs, and tables or numbered lists where they help the reader.
- Report text gives the reader information about the subject only, leaving commentary about the report, the outline or the writing process out.
- One topic per file, named `NN-SS-S-slug.md` so that sorting the names lexically gives document order. H1 marks a part, H2 an x.y section, and H3 an x.y.z section.
- APA 7 references, numbered for in-text citation as `[n]` in order of first citation. While drafting, citations use temporary source IDs (`[S101]`); the References task converts them to `[n]`.
- Abbreviations are spelled out at first use and listed in `00-1-abbreviations.md`.
- Scripts run with `./venv/bin/python`; every new dependency is installed in the venv.

### 1.1 Core Rule: Record Every Crawl on Disk

> **What is learned from the web counts once it is written to `reports/milestone-5/research/`.** Every search, every fetched page and every interpretation of that page is saved as a local file *at the moment it happens*, before the next tool call. The report is written only from these files.

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
| build-report skill (`make precheck/build/postcheck TASK=reports/milestone-5`) | Format, structure, abbreviation and citation checks; Word build; Word post-check |
| `AskUserQuestion` | Human verification on any failed checklist item, any conflict with the outline, and at the checkpoints (Section 8) |

## 3. Target File Map (`reports/milestone-5/report/`)

<!-- FILL: one row per file, in document order, matching plan.toml [[files]]. "Research focus" says what web research must add beyond the outline. -->

### 3.1 Front Matter

| File | Content |
| :---- | :---- |
| `00-0-title-page.md` | Institution, course, report title, group and lecturers (details from the user at the scope checkpoint) |
| `00-1-abbreviations.md` | Abbreviations as they appear (built from the text in the Front matter task) |
| `00-2-glossary.md` | Defined terms with section pointers |

### 3.2 Part 1: <!-- FILL -->

| File | Content | Research focus |
| :---- | :---- | :---- |
| | | |

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
6. **Resume rule.** A new session starts with `progress.py --base reports/milestone-5 next` and continues with the first task that is not `done`. A task left `in-progress` is re-entered at step 4 (verify what is already saved).
7. **One task at a time by default.** Independent tasks may run concurrently when the plan names the wave and shows why they cannot affect each other (skill reference.md section 1.4).
8. **Source IDs are reserved per part:** Part 1 S100–S199, Part 2 S200–S299, …; outline seeds are S001–S0nn.

## 5. Progress Ledger (`reports/milestone-5/PROGRESS.md`)

The ledger is the single record of where the work stands, updated at steps 5 and 6 of every task (`progress.py set`). Status values: `todo`, `in-progress`, `blocked`, `done`, and `skipped` (set only by a human decision).

## 6. Task Templates

The checklists of the three task kinds (R research, W writing, F figure), the finishing tasks and the human checkpoints are fixed in the research-report skill's `reference.md` (sections 3 and 4). Each card in Section 7 adds only its own inputs, outputs, research questions and extra checks.

## 7. Task Cards

<!-- FILL: one card per task in plan.toml [[tasks]]. Research cards list the research questions; writing cards list the files and any table, formula or figure they must contain. -->

### 7.1 Stage A: Setup

**T01: Scaffold the workspace and register the task.**
- **Do:** `scaffold.py build --base reports/milestone-5`, then `scaffold.py register --base reports/milestone-5`.
- **Checklist:**
  - [ ] `scaffold.py check --base reports/milestone-5` reports 0 errors.
  - [ ] `tasks.toml` has the `[<task>]` table; `make build TASK=<task>` builds the skeleton cleanly.

**T02: HC, scope inputs.**
- **Do:** ask the human for the title-page details, the inclusion of any outline section marked optional, the report language(s), and every ambiguity found in the outline.
- **Checklist:**
  - [ ] Every answer is recorded under `Decisions` in the ledger, and the plan is updated where an answer changes it.

### 7.2 Stage B: Part 1

| ID | Kind | Inputs | Outputs | Research questions or actions; extra checks |
| :---- | :---- | :---- | :---- | :---- |
| | | | | |

### 7.N Stage F: Finishing

The finishing cards follow the skill's reference.md section 4.4: front matter, references, full gates, fact spot-check, style read-through, build and post-check, final review.

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
| Plan and ledger | `reports/milestone-5/EXECUTION_PLAN.md`, `reports/milestone-5/plan.toml`, `reports/milestone-5/PROGRESS.md` |
| Section files | `reports/milestone-5/report/*.md` |
| Research trail | `reports/milestone-5/research/` (search log, register, claims, syntheses, sources with crawls and comprehension, spot-check, style review) |
| Word report | `build/<task>/Report_EN.docx` (build-report skill) |

## Task cards for Milestone 5 (2026-11-08)

**T05:** Offline research A (R; Parts 1–5; IDs S100–S199 for any new source). Read the brief (S001) and the team's
own reports as local sources: S101 (Milestone 1), S102 (Milestone 2), S107 (Milestone 2 package), plus S103 Sections
1, 4 and S104 Section 1 and Appendix VII for the final state. Add claims with verbatim anchors to part1–part5 claims
and a synthesis entry per planned file of Parts 1–5: the final Business Goal, SMART Goal, KPIs, decisions D1–D3,
stakeholders and needs, scope, the final AQ1–AQ4 with level and decision, the AQ quality check, the material of the
AQ Revision Log (Milestone 1 wording, finding from Milestones 2–3, final AQ, action, reason, effect on method, with
Change Log IDs), data requirements, candidates and selection rationale, provenance, version and licence, dataset
description and AQ–Data Fit with each AQ's status. Record every disagreement between milestones as a conflict.

**T06:** Offline research B (R; Parts 6–10, 11 (AQ3–AQ4 expected outputs), 12–13; IDs S600–S699 etc. per part for
any new source). Sources S103 (Milestone 3), S105 (prepared package metadata), S104 (Milestone 4), S106 (prototype
contract), and S101/S102 for the AI sections. Claims and synthesis per planned file: profiling and quality findings
that could change a conclusion, representativeness and sensitive fields, pipeline, features and leakage control,
prepared version and reproducibility; AQ → task → baseline → candidates → primary proposal → rationale; evaluation
metrics, validation, success criteria, fairness and interpretability checks; Level 2 status; AQ3 and AQ4 expected
outputs; limitations and future data needs; the AI use of every milestone (roles, suggestions, verification, accepted
and rejected, final human decision) as material for an AI Decision Log covering M1–M5.

**T07:** Online research (R; Parts 1, 9, 11, 12, 13). External published sources the integrated story needs: early
disengagement and non-completion in online and blended higher education, early-warning and learning-analytics
interventions, interpretation of association versus causation, reporting and reproducibility standards for data
projects, ethics of learning analytics, and guidance on generative AI in education. Reuse first: the trails of
Milestones 1–4 hold fetched sources; re-register a reused source here under a new ID in the part's block and copy its
crawl and comprehension (header id updated). Fetch new sources only where no earlier crawl covers the need.

**T08:** AQ1 and AQ2 analysis (S). Code `code/aq_analysis.py` on the Milestone 3 prepared views, following the
Milestone 4 plan (Sections 3.2, 4.1, 4.3, Appendices II–IV) on the 9 runs of 2013 only; the 2014 outcomes are never
read except the 2014 outcome shares already published by Milestone 3. Outputs in `results/`, run logs in `logs/`, a
methods note mapping each output to the plan, and every deviation from the plan with its reason.

### Writing brief for T11–T13 (full draft)

Every writer reads, in this order: `AGENTS.md` (writing conventions; "Submitted deliverables read on their own"),
`.claude/skills/research-report/reference.md` section 6, the brief `milestones/05/milestone-5.md` (the row of its
section 2 table for each section written: aim, content, required evidence, self-check question), the decisions in
`PROGRESS.md`, the planned files and headings in `plan.toml`, the part synthesis and claims files, the integration
documents in `research/design/` (tables are copied from there), the results in `results/` (README, aq_summary.md) and
the figure notes of T10.

- **Full draft.** Write each section completely, without regard to length: every element the brief's table asks for
  that section, the reasoning, the definitions and the evidence. The move to appendices happens later (T15).
- **One project story.** Each section is rewritten for the final report, never pasted from a milestone report; the
  earlier milestones are named in words where their work is the evidence ("Milestone 3 profiled…", "(Milestone 4,
  Section 4.1)"), and the final state is stated, with changes explained through the AQ Revision Log and Change Log.
- **Voice and tense.** First-person team voice ("we"). AQ3 and AQ4 modeling and evaluation are proposals: proposal
  tense ("is proposed", "would be evaluated"), no model metric. AQ1 and AQ2 report the real 2013 results with their
  population, denominator and 95% interval; associations are never written as causes.
- **Citations.** Published works only, as draft IDs `[Sxxx]` that occur in the claims; our own milestone reports and
  packages (S101–S107) are never cited as [S10x] – they are described in words. Numbers come from claims or result
  files only.
- **Deliverable rules.** No repository paths, file names, logs, task IDs, claim IDs or source IDs other than [Sxxx]
  draft citations; identifiers paired with their words ("the early-sign rule (C10)"); tables introduced in the sentence
  before them, captioned `**Table N.M. Caption**`; figures `![Figure N.M. Caption](assets/figures/<name>.png){width=100%}`.
- **Gate.** After each file: `check_drafts.py --base reports/milestone-5 --files <file>` (0 errors), and
  `.claude/skills/build-report/scripts/check_style.py` for the report (no voice errors).
