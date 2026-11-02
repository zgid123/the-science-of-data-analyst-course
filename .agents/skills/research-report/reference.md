# research-report reference

## 1. The task protocol

### 1.1. The loop

Every task runs the same seven steps, and the next task starts only when the ledger shows the previous one `done`:

| Step | What happens |
| :---- | :---- |
| 1. LOAD | Read the ledger (`progress.py next`) and only the files the card names: the outline slice (`outline.py --section`), synthesis entries, comprehension files, the last paragraph of the previous report file |
| 2. DO | Carry out the card with the tools it names |
| 3. WRITE | Save every output to the files the card names |
| 4. VERIFY | Tick each checklist item against a saved file or a command output |
| 5. DECIDE | All ticked → 6. Any unticked → STOP: status `blocked`, failing items and a question in the ledger, `AskUserQuestion` (continue / redo / skip / stop) |
| 6. CLOSE | `progress.py set Txx done --outputs … --verified … --note …` with a handoff note of at most 8 lines |
| 7. FREE | Drop the working context; the next task reads only the ledger and its card's files |

### 1.2. Rules

1. Verification is evidence-based: the ledger's "Verified by" column names the command or file that proved each item.
2. Fixes belong to steps 2–3. After a failed VERIFY the human decides how to continue, so every retry is a visible decision.
3. Every human answer is recorded under `Decisions` with the task ID, so a later session sees why.
4. Planned checkpoints (scope, end of each part, final) stop even on success.
5. Research tasks run in one foreground subagent (`Agent`, general-purpose, `run_in_background: false`) that writes its own trail files and returns at most 5 lines. Writing tasks read the comprehension notes and synthesis; `crawl.md` files serve verification.
6. Resume: `progress.py --base taskN next`; a task left `in-progress` is re-entered at VERIFY.
7. Tasks run one at a time by default. Independent tasks may run concurrently in background agents when four conditions hold (section 1.4): disjoint outputs, no input from each other, a shared vocabulary fixed in the plan, and whole-report checks left to the sequential finishing stage.
8. Source IDs: seeds S001–S0nn from the outline; Part N uses SN00–SN99. Claim IDs: CN-001, CN-002, … per part.

### 1.3. Human checkpoints

| When | Why |
| :---- | :---- |
| Stage 0, plan approval | The user owns the scope: part mapping, inclusions, file map |
| Any unticked checklist item | The user decides how to continue (continue / redo / skip / stop) |
| Any conflict between a source and the outline (R7) | The user decides which version the report states |
| Scope inputs (T02) | Title page (names copied character for character from the user's own title page into the report and into `people` in `tasks.toml`, which build-report's `check_names.py` checks), optional sections, language, ambiguities |
| End of each part | Part review; a natural point for `/compact` or `/clear` |
| Final review | Acceptance, or new tasks from feedback |

### 1.4. Concurrent tasks

A plan may group independent tasks into waves that run at the same time, each task in its own background agent. The plan states for each wave why its tasks cannot affect each other, and these safeguards apply:

| Shared resource | Safeguard |
| :---- | :---- |
| `search-log.md`, `sources.md`, claims files | Written only through `trail.py`, whose commands hold an exclusive lock on `research/.trail.lock` |
| Source IDs and folders | Disjoint ID blocks per task; seeds are fetched in their own wave before the part research, so each source is fetched once |
| Claims and synthesis | One research task per part |
| Figure registry | Written once in setup with stub builders; each figure task edits only its own module and renders with a name filter |
| Report files | Each file belongs to exactly one writing task |
| Abbreviations | An ownership table in the plan names the file that defines each abbreviation; part introductions, written last, use only abbreviations defined before them |
| Numbers and IDs | Section, figure, table and item numbers are fixed in the plan before writing starts |
| Ledger, `tasks.toml`, builds | Only the main agent writes them; whole-report gates and the build run in the sequential finishing stage |
| Temporary files | Each agent works in its own scratch subfolder named after its task (`scratchpad/T35/`), so files with fixed names stay apart |

The main agent launches a wave in one message, verifies each task as it returns, and closes it in the ledger. A failed check stops only that task, and the other tasks of the wave continue. A writing task starts as soon as the research of its own part is done.

## 2. Workspace and trail formats

```
taskN/
├── reference.md            the user's outline (input, kept as the user wrote it)
├── plan.toml               machine-readable plan: [plan], [checks], [references], [[files]], [[tasks]], [[seeds]]
├── EXECUTION_PLAN.md       human-readable plan: scope mapping, file map, protocol, task cards, checkpoints
├── PROGRESS.md             ledger: ID | Task | Status | Outputs | Verified by | Handoff note; Decisions; Blocked
├── report/                 00-0-title-page, 00-1-abbreviations, 00-2-glossary, NN-SS-S-slug.md …, NN-references.md
│   └── assets/             university-logo.png, figures/
└── research/
    ├── AGENT_BRIEF.md      rules every research subagent reads first
    ├── README.md           how to read the trail
    ├── search-log.md       | # | Task | Date | Query | Kept (→ ID) | Dropped (reason) |   append-only
    ├── sources.md          | ID | Folder slug | Source | URL | Outline item | Primary/secondary | Status | APA 7 entry |
    ├── partN-claims.md     | Claim ID | Claim | Exact value or quote anchor | Source ID | Primary or secondary | Report file(s) |
    ├── partN-synthesis.md  ## <file>: Claims, Outline, Conflicts with the outline, Gaps
    ├── spot-check.md, style-review.md
    ├── templates/          crawl.md, comprehension.md
    └── sources/Sxxx-slug/  crawl.md (header + text), raw.* (original), attempts.md (fetch log), comprehension.md
```

| File | Rule checked by `check_trail.py` |
| :---- | :---- |
| `crawl.md` | Front matter with `id`, `url`, `fetched`, `tool`, `status`, `task` (also `part`, `raw`, `fetch_prompt`); the id equals the folder; the text below stays exactly as converted; extra fetches are appended as `<!-- fetch N: … -->` blocks |
| `comprehension.md` | Six non-empty headings: Summary in my own words, Key facts, Used in, Against <outline>, Reliability, Open questions; every "…" quote in Key facts occurs verbatim in `crawl.md` |
| claims | 6 columns; at least one "…" anchor of 8+ characters per claim, verbatim in the source's `crawl.md`; the source is `fetched` or `partial`; the report file is filled once written |
| register | Status `fetched`, `partial`, `blocked`, `error` (folder required), `to-fetch`, `duplicate`; it agrees with the crawl header (ok ↔ fetched) |
| reference map | After finishing: `| n | Source ID |` rows, each pointing to a usable source |

Verbatim matching collapses whitespace and straightens typographic quotes; `\|` inside a cell is a literal pipe.

**Works a source cites.** A survey or review often reports other works as "Liu et al. [93]". Its Key facts name each such work by first author with initials, year and venue, and give the work's own source ID when `sources.md` holds it: `- Liu Y., Jourabloo & Liu X. (CVPR 2018; S206) fuse estimated depth and rPPG – "…"`. The citation marker in the source and its reference-list entry give these details; a work that the register holds is then read in its own `crawl.md` for the facts the report states about it, so the primary source carries them.

## 3. Task kinds and checklists

### 3.1. Research task (R), one foreground subagent

**Load:** the card's research questions, the previous handoff, `sources.md` (each source registered once), `AGENT_BRIEF.md`. **Prompt:** `progress.py --base taskN prompt Txx` prints `templates/RESEARCH_TASK_PROMPT.md` filled with the card, handoff, outline lines, ID block and files. **Write:** the trail entries with `trail.py` (log-search, register, comprehension, claim, apa).

- [ ] R1. `search-log.md` has a row for every query of the task, with kept and dropped results.
- [ ] R2. Every source used has `crawl.md` (header and status) and `comprehension.md` (six headings).
- [ ] R3. `check_trail.py --base taskN --task Txx` reports 0 errors.
- [ ] R4. Every research question is answered by a claim, or listed as a gap under Open questions.
- [ ] R5. Every fact-carrying claim comes from a primary source, or is labelled secondary with a reason.
- [ ] R6. `partN-synthesis.md` has an entry for each report file of the card, with its claim IDs.
- [ ] R7. Every conflict with the outline is resolved; **each conflict is a stop for the user**.
- [ ] R8. Every work known through another source is identified by first author with initials, year and venue, and linked to its source ID when the register holds it (section 2, "Works a source cites").

### 3.2. Writing task (W), main agent

**Load:** the ledger, the card's synthesis entries, the `comprehension.md` of each listed source, the outline slice, the last paragraph of the previous file. Citations are `[Sxxx]` while drafting.

- [ ] W1. Every file of the card is filled with the right heading level and number, and `scaffold.py check` passes.
- [ ] W2. Every factual sentence carries an `[Sxxx]` used by a claim: `check_drafts.py --base taskN --files …` 0 errors.
- [ ] W3. Every fact comes from the trail; a missing fact sends the work back to research (stop and ask).
- [ ] W4. The first sentence of each file links to the previous section; paragraphs build cumulatively.
- [ ] W5. Reader-focused text only (`check_drafts.py` meta phrases; reader-focused text, section 6.2).
- [ ] W6. Abbreviations defined at first use: build-report `check_abbreviations.py --report taskN/report --lang en` 0 violations (add rows to `00-1-abbreviations.md` as you go).
- [ ] W7. The "Report file(s)" column of every used claim is filled.
- [ ] W8. Words per file within the plan's range (`check_drafts.py` warns); section intros exempt from the minimum.
- [ ] W9. Each cited work has a distinct name: works of different research groups whose first authors share a surname carry initials ("Liu S.-Q. et al. (2016)", "Liu Y. et al. (2018)"); `check_drafts.py` warns when one "Surname et al." names works of different years in a file.
- [ ] W10. `check_drafts.py` reports no priority claim stated as the report's own and no citation of the authors' own material (section 6.2).

### 3.3. Figure task (F), main agent

Figures are code: add a builder to `figures/taskN/` (registered in its `FIGURES`), declare `[taskN.figures] package = "figures.taskN"` in `tasks.toml`, render with build-report's `render_figures.py taskN`. Plan figures generously, at Stage 0 and again in each part: every key comparison, ranking that flips, structure, mechanism or worked example that a paragraph of numbers carries is a candidate. A figure adds what a table cannot (a pattern, a sequence, a mechanism), so a table already in the text stays a table. Builders take `lang`, so each language gets its own labels; a source's own figure is reproduced with credit when its licence allows and redrawing is not possible.

- [ ] F1. The PNG exists at 300 DPI under `report/assets/figures/`.
- [ ] F2. The PNG has been viewed with `Read`: labels are readable, separated and fully inside the frame.
- [ ] F3. Every label matches a term used in the text.
- [ ] F4. Every element is backed by claims.
- [ ] F5. The file has the image line with its caption, and the text refers to the figure by number.

### 3.4. Part checkpoint (HC)

Write the part introduction (names every section and figure of the part), then: `check_trail.py --part N` and `check_drafts.py --part N` 0 errors; build-report `check_structure.py` (headings, captions, cross-references) clean for the part; **stop for the user's review**.

## 4. Planning and finishing

### 4.1. Planning from the outline (Stage 0)

| Outline element | Becomes |
| :---- | :---- |
| Scope, objectives, selection criteria | Guidance for the whole report: the criteria apply to every new source and to any "flagship" choice |
| Each numbered top-level topic section | A part `# N. Title` (ask the user about hands-on or optional sections) |
| Each subsection | A section `## N.M. Title` with an intro file `NN-MM-0-…`, split into `### N.M.K.` files of one topic each |
| Anchor papers, standards, URLs in a section | Seeds and the research focus of that section's R card |
| The reference list | Seeds S001–S0nn (`outline.py --seeds`; merge duplicates, split items that hold several sources) |
| Claims, numbers and dates in the outline | Facts to verify; each difference found goes to the user as a conflict to decide |

### 4.2. The standard task list

T01 scaffold and register → T02 scope checkpoint → per part: (R, W) per section group, F per figure, HC part review → Front matter → References → Full gates → Fact spot-check → Style read-through → Build and post-check → Final review.

### 4.3. Finishing cards

| Task | Do | Checklist |
| :---- | :---- | :---- |
| Front matter | Title page from T02; `00-1-abbreviations.md` from the acronyms actually used (build-report `check_abbreviations.py --report … --candidates` lists them, with table rows never used); `00-2-glossary.md` from defined terms | Every abbreviation used has a row and every row is used; build-report abbreviations 0 violations |
| References | `finalize_refs.py --base taskN` | Every `[Sxxx]` replaced; build-report `check_citations.py` 0 errors (first-citation order); `check_trail.py --all` 0 errors (reference map) |
| Full gates | `check_trail.py --all`, `make precheck TASK=taskN` | All 0 errors; outputs pasted into the ledger |
| Fact spot-check | `spot_check.py --base taskN --write`, then judge each row against the quoted evidence | 10 of 10 match; any mismatch is a stop |
| Style read-through | Read every file in order against CLAUDE.md, section 6 and consistent terms; log in `style-review.md` (a subagent may list findings; the main agent applies and verifies them) | Every finding fixed or justified; gates still clean |
| Build and post-check | `make all TASK=taskN` | Precheck, build and Word post-check pass; caption counts as planned |
| Final review | Report deliverables, gate results, spot-check and open questions to the user | Accepted, or new tasks added from feedback |

## 5. Fetching: readable text, retries and replacements

### 5.1. The ladder

| Level | What `fetch.py get` tries | Typical rescue |
| :---- | :---- | :---- |
| L1 | The requested URL; retry with backoff on 429/5xx/network errors, a second browser user agent on 403 | Rate limits, flaky servers |
| L2 | Other copies of the same work: arXiv HTML → PDF → abstract; for a DOI, the publisher page plus every open-access location from OpenAlex and Semantic Scholar | Paywalled publisher page with an author or repository copy |
| L3 | The Wayback Machine snapshot (`web.archive.org/web/2id_/URL`) of each L1 URL | 403/Cloudflare pages, moved or deleted pages |
| L4 | A metadata record from Crossref and OpenAlex (authors, venue, year, pages, DOI, citations, abstract, open-access locations) | Bibliographic facts and citation traction when no full text is reachable |
| L5 (agent) | `WebFetch` with a verbatim prompt, appended as a fetch block with `fetch.py webfetch`; `Read` on a PDF's page ranges; a replacement source via `fetch.py find "<title>"` or `WebSearch`, logged as "replacement for Sxxx" | JavaScript-only pages, scanned PDFs, sources that are simply unavailable |

**Local sources.** When the subject is a software artefact (a repository, the group's own documents), `fetch.py local --repo DIR --rev COMMIT --url-prefix URL PATH …` copies the files at that revision verbatim into one source's `crawl.md` (each under a `===== PATH @ REV =====` line), so code fragments serve as claim anchors like any quotation; `--worktree` reads uncommitted files from disk and `--strip-images` drops embedded `data:image` URIs. Group files by module, one source per group, and pin the revision so every claim stays reproducible.

Give a DOI or arXiv ID whenever one exists; it unlocks L2 and L4. A `WebFetch` request for a passage that reports other works also asks for their citation markers and the matching reference-list entries ("keep every citation marker such as [93] and return the reference entries they point to"), so each cited work keeps its identity in the crawl. `fetch.py meta` writes only the L4 record (for APA entries and citation counts); `--append` adds another page of the same source to its `crawl.md`.

### 5.2. Conversion and readability

| Input | Converters, in order |
| :---- | :---- |
| PDF | macOS PDFKit text layer (`pdf/pdfkit_text.js` via `osascript`), then pypdf when the venv has it, then a standard-library extractor (Flate streams, Tj/TJ text); page markers `<!-- page n -->`; ligatures (ﬁ, ﬂ) restored and line-end hyphens re-joined |
| HTML | Structure-preserving text: headings as `#`, list items as `-`, table cells separated by `|`; scripts, styles, navigation and forms removed; `title` and `citation_*`/`dc.*` metadata on top |
| JSON | Crossref, OpenAlex or Semantic Scholar record as labelled fields |
| Text | As is |

| Verdict | Rule | crawl status → register |
| :---- | :---- | :---- |
| readable | ≥ 300 words, mostly letters or digits, normal word length and function-word share, no broken glyphs | ok → fetched |
| partial | 40–299 words, or words that lost a ligature (quotes may not match) | partial → partial |
| metadata | A bibliographic record (L4) | partial → partial |
| blocked | A short page with a blocking signature (captcha, "Just a moment", "enable JavaScript", access denied) | blocked → blocked |
| unreadable | Symbol soup, replacement or CID glyphs, exploded one-character lines, almost no text | error → error |

Each run downloads into its own folder `build/.cache/fetch/run-<pid>/`, so each parallel agent keeps its own files. Every attempt (tier, URL, HTTP code, type, size, converter, words, verdict, reasons) is appended to `attempts.md`, so gaps stay visible.

### 5.3. Rules for partial and failed sources

- Quote only text present in `crawl.md`, copied from the file.
- A metadata-only source supports bibliographic facts: authors, venue, pages, date and citation counts as of the fetch date.
- A source with status `blocked` or `error` keeps its folder and files as a record of the gap; claims cite `fetched` and `partial` sources.

## 6. Writing rules

### 6.1. Structure

- One topic per file, 150–700 words; section intro files (`-0-`, `-00-`) may be shorter.
- Headings `# N.`, `## N.M.`, `### N.M.K.`; figures `![Figure P.n. Caption](assets/figures/x.png){width=100%}`; tables after a bold `**Table P.n. Caption**` line; formulas as LaTeX (`$…$`, `$$…$$`). The build-report skill's reference.md section 1 lists every convention its checks enforce.
- Each file opens with a sentence that links to the previous section and closes towards the next.

### 6.2. Style

- CLAUDE.md: formal, positive framing, cumulative sentences with additive and causal links, full paragraphs, tables or numbered lists where they help.
- Every section reads on its own (CLAUDE.md, "Every Section Reads On Its Own"): restate the key point in a clause, then point to the section that develops it; keep the definition, number or rule a sentence needs in the same paragraph; give every identifier its words ("guaranteed reversal (P04)"); define a concept where it is first needed; introduce each table and figure in the sentence before it. Structured items (components, cases) read as connected prose rather than labelled fields.
- Reader-focused: the text gives information about the subject only, leaving out commentary about the report, the outline, the sources' retrieval or the writing rules ("this report presents…", "as the outline says", "was found during research"). Signposting ("Table 3.8 summarises…") is fine.
- The conclusion states what is now known about the subject once all the evidence is weighed: conclusions about the field, each with its evidence and its implication, then the open problems and the consequences for practice. It speaks about the subject (the field, the methods, the threats), and sections serve as pointers, for example "(Section 3.3)". `check_style.py` reports narration about the report itself in a Conclusion part. Selecting the prominent references that the conclusions rest on is part of writing it: the selection goes into the part's synthesis as its evidence base, and the conclusions cite those works; the reference list stays the one place that lists references.
- Benchmark and evaluation material is written as a specification: what is measured, under which conditions, with which metric and why. Results enter the text once they are measured and saved in the trail.
- Each cited work has a name of its own: the first author's surname, with initials when another cited work shares that surname ("Liu S.-Q. et al. (2016)" and "Liu Y. et al. (2018)"), or all authors' surnames for two or three authors ("Liu, Jourabloo and Liu"). One research group across several years reads as one name with its years.
- Facts carry their source in the same sentence; point-in-time numbers carry an "as of" date; secondary and industry figures are labelled as such; author-reported results are labelled as author-reported.
- Conflicts that the user resolved are written as decided: both versions attributed, or the decided version.
- **Own material.** When the report's subject is the authors' own work (their system, code, draft or documents), that material is evidence in the trail (`fetch.py local`, claims anchored in it) and the subject of the text, while the reference list holds published works only. A conventions sentence states once that facts about the system refer to the repository at a named commit; files, tests and commits are named inline where they help. `check_drafts.py` warns when a draft cites a locally fetched source.
- **Paper and artefact.** Where a paper and its released code or data disagree, the text states what the paper says, then what the artefact does, in one attributed clause ("the released code applies a different rule [n]"); where a planned structure and the code disagree, the code is the record and each case goes into a conflict register the user approves.
- **Grounded claims.** A priority claim ("the first", "novel", "for the first time") is attributed to the work that makes it ("the authors present it as the first"), or backed by the search that establishes it; contributions of a proposal are stated conditionally on its hypotheses, and an elementary result is called elementary. A plan, schedule or effort figure rests on checked facts: real deadlines, published compute or effort figures, stated assumptions (people, hardware, a slower case) and a buffer, naming the venue or date the schedule actually fits. `check_drafts.py` warns on priority claims stated as the report's own.
