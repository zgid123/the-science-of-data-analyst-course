---
name: research-report
description: Turn a concise outline markdown (taskN/reference.md style – headings, bullets, anchor papers, a reference list) into a formal, evidence-backed report through web research and local sources, a fine-grained execution plan with a progress ledger, a research trail saved on disk (search log, readable crawls, comprehension notes, claims with verbatim quote anchors), and sequential part-by-part writing of fine-grained markdown sections including front matter, ending in a Word document via the build-report skill. Use it whenever the user gives an outline or a topic and asks for a researched report, a critical review of a paper, a technical report on a code base or a research proposal; asks to plan, continue or resume such a report (PROGRESS.md, EXECUTION_PLAN.md); asks to fetch or convert a source that is unreadable; or asks to verify a report's facts, numbers or citations against its sources.
---

# Research report from an outline

The input is the user's **concise outline markdown** (for example `task3/reference.md`): headings per topic, a few bullets and anchor papers each, often a scope section with selection criteria, and a reference list. The output is a report folder `taskN/report/` of numbered section files (front matter, parts, references) whose every fact is traceable to a saved source, plus the Word document built by the build-report skill.

Read [reference.md](reference.md) before planning: it fixes the task protocol (section 1), the trail formats (section 2), the task kinds and their checklists (sections 3–4), the fetch and fallback ladder (section 5) and the writing rules (section 6). The task folder then carries its own copies: `EXECUTION_PLAN.md`, `PROGRESS.md` and `research/AGENT_BRIEF.md`.

`R=.claude/skills/research-report/scripts` below; run every script with `./venv/bin/python` from the project root.

## Working principles

1. **Speak loudly on disk.** Every search, fetch and interpretation is written to `taskN/research/` the moment it happens; the report is written only from those files. Working files beside the trail follow the layout of reference.md section 2.1: reviews in numbered rounds (`layout.py new-review`), revisions with saved states as commits in `revisions/snapshots.md`, task notes declared in `plan.toml`; `layout.py check` fails on anything else.
2. **Verified tasks, run one at a time unless independent.** Independent tasks may run as concurrent waves (reference.md section 1.4). LOAD → DO → WRITE → VERIFY → DECIDE → CLOSE → FREE. A failed checklist item stops the work and goes to the user (continue / redo / skip / stop); fixes happen before verification, so every retry is a visible decision.
3. **Pick up only what is needed.** Each task loads the ledger and the files its card names (the outline slice via `outline.py --section`, the synthesis entry, the comprehension files). Research runs in one foreground subagent per task, so its context is discarded. The handoff note is the only memory between tasks.
4. **Ask the user** at planning, at the scope checkpoint, on every conflict between a source and the outline, on any failed check, at the end of each part and at the final review. Record each answer under `Decisions` in the ledger.
5. **Steady pace.** Parts are written sequentially, file by file, each file checked before the next.
6. **Every cited work keeps its identity.** A work known through another source is named by its first author with initials, year and venue, and linked to its own source ID when the register holds it (reference.md sections 2, 5 and 6.2).
7. **Reader first.** Report text gives the reader information: facts with their sources, findings, signposts. Benchmark material reads as a specification of what is measured.
8. **Project tools only.** Scripts run on `./venv`; fetching uses `curl` and macOS PDFKit, which the system already has.
9. **Grounded and modest.** The reference list holds published works, while the authors' own code, draft and documents stay in the trail as evidence; priority claims are attributed or backed by a search; plans and schedules rest on checked dates and figures (reference.md section 6.2).

## Workflow

### Stage 0 – Plan (with the user)

1. Read the outline in full, then map it: `$R/outline.py taskN/reference.md` (sections, line ranges, anchors) and `--seeds` (reference list → seed rows).
2. Propose the plan: `$R/scaffold.py init --base taskN --outline taskN/reference.md --title "…"`. It writes `plan.toml` (file map from the outline, the standard task list, seeds) and `EXECUTION_PLAN.md` from the template.
3. Refine both: split sections into fine-grained files (one topic each, 150–700 words; reference.md 6.1), write the research focus per file, the research questions per R card, tables, formulas and figures per W/F card, and the checkpoints. Keep `plan.toml` [[files]] and [[tasks]] in step with the plan (`scaffold.py tasks` regenerates the task list from the file map).
4. Ask the user to approve the part mapping (which outline sections become parts, which are left out) and the plan, with `AskUserQuestion`; record the decisions.

### Stage A – Setup (T01–T02)

- T01: `scaffold.py build --base taskN` (report skeleton with front-matter pages, research trail, `AGENT_BRIEF.md`, `PROGRESS.md`), `scaffold.py register --base taskN` (adds the task to `tasks.toml` for build-report), `scaffold.py check` → 0 errors.
- T02 (checkpoint): title-page details, optional sections, report language(s), every ambiguity in the outline.

### Stages B… – One stage per part

For each section group: an **R** task (research subagent launched with the prompt from `progress.py --base taskN prompt Txx`, which fills in the card, the handoff, the outline lines, the ID block and the files), a **W** task (write the files from the synthesis and comprehension notes, citing `[Sxxx]`), **F** tasks for figures (build-report's figure toolkit), and an **HC** task that writes the part introduction and stops for the user's review. Gates: `check_trail.py --task/--part`, `check_drafts.py --files/--part`, build-report `check_structure.py` and `check_abbreviations.py`.

### Final stage – Finishing

Front matter (abbreviations and glossary from the text) → `finalize_refs.py` ([Sxxx] → [n], APA list, reference map) → full gates (`check_trail.py --all`, `make precheck TASK=taskN`) → `spot_check.py --write` (10 sentences traced to verbatim evidence) → style read-through (`style-review.md`) → `make all TASK=taskN` (build and Word post-check) → final review with the user.

### Resuming

`$R/progress.py --base taskN status` and `next` print where the work stands, the next card and the last handoff. A task left `in-progress` is re-entered at VERIFY.

## Bookkeeping by script

Every trail entry whose form is fixed is written by a script, so numbering, dates, columns and quote anchors are exact: `trail.py log-search` (search-log row), `trail.py register` (register row; `fetch.py` keeps its status current), `trail.py comprehension` (the six-heading skeleton), `trail.py claim` (next claim ID; written once the anchor is verified in `crawl.md`), `trail.py apa` (APA 7 draft from the metadata record), `progress.py set` (ledger), `progress.py prompt` (research prompt), `finalize_refs.py` and `spot_check.py` (finishing). The agent's own work is the judgement: what to search, what a source says, how the report reads.

## Unreadable sources: fetch, convert, retry, replace

`$R/fetch.py get --base taskN --id S101 --slug name --task T05 --part 1 <URL | DOI | arXiv:ID>` downloads with retries, converts PDF/HTML/JSON to readable text, scores readability and walks the ladder **L1** the URL → **L2** other copies of the same work (arXiv HTML/PDF, OpenAlex and Semantic Scholar open-access copies) → **L3** Wayback Machine → **L4** a Crossref/OpenAlex metadata record. It writes `crawl.md`, `raw.*` and `attempts.md`, and exits 0 (readable), 3 (partial) or 4 (nothing usable). On 4, **L5**: `WebFetch` with a verbatim prompt, `Read` on PDF page ranges, or a replacement source found with `fetch.py find` / `WebSearch` and logged as "replacement for Sxxx". Details: reference.md section 5.

## Hand-over to other skills

- **build-report** builds and checks the Word document (`make all TASK=taskN`, through the Makefile that build-report ships in `templates/Makefile`); `scaffold.py register` wires the trail check and the draft-ID citation rule into its precheck.
- **build-report** also translates: once the English report is accepted, `make translate TASK=taskN` lists what a target language needs (for Vietnamese, with its guide and glossaries); give the new task a domain or topic glossary in `tasks.toml` when its field is new, and `make all` builds every language.
