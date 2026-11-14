# AGENTS.md

## Project overview

Coursework for MTH045 – The Science of Data Analytics (education analytics). Briefs and deliverables are mostly
Vietnamese; English technical terms stay as written. `CLAUDE.md` in each folder is a symlink to its `AGENTS.md`:
edit `AGENTS.md`, and re-read it after each change so the updated rules apply in the same session.

- `samples/` – standalone reference samples. `slidev/` is the reference Slidev deck (theme, layouts,
  section structure, Vue charts, speaker-note format): start new decks from its README.
- `milestones/` – the instructor briefs, one folder per milestone: `<nn>/milestone-<n>.pdf` as received and
  `milestone-<n>.md` its Markdown copy from `pdf2md`, with images in `milestone-<n>_assets/`; `README.md` gives each
  copy's verification result.
- `final-project/` – team N04 project; has its own `AGENTS.md`, which takes precedence inside that folder.
  `milestones/<nn>/` there holds the team's earlier deliverables (`N04_*`, the Milestone 2 data collection).
- `datasets/` – education datasets, fetched and verified by `scripts/fetch-datasets/`; raw files stay local
  (git-ignored) and each `<dataset>/exploration/` folder of analysis results is tracked. **Analysis
  focus: OULAD** (`datasets/oulad/`); the six other datasets are reference data from the milestone 2 screening.
  `final-project/datasets` links here for earlier code.
- `reports/` – report tasks built with the `research-report` and `build-report` skills: each task folder holds its
  outline (`reference.md`), plan (`EXECUTION_PLAN.md`, `plan.toml`), ledger (`PROGRESS.md`), research trail, section
  files (`report/*.md` in English, `*.vi.md` Vietnamese twins), `logs/` and `build/`. `tasks.toml` and `Makefile` at the
  root register the tasks. `reports/milestone-1/` is the team's fresh Milestone 1 proposal.
  A task with a talk keeps its speech scripts, storytelling drafts, plans and reviews in `presentation/` (index and
  naming table in its `README.md`), one subfolder per deck generation named `v<n>-<scope>/`; every file of a generation
  carries its scope: deck scripts in the project root, as the build-report slide kit requires
  (`build_slides_<task>_<scope>.py`, `slides_<task>_<scope>_vi.py`, slide packages `slides_<task>_<scope>/`), decks in
  the task's `build/` as `N04_<Task>_Slides-<Scope>_<LANG>.pptx`, briefs as `BRIEF.md` in the folder they govern.
  Working files beside the trail keep one layout (research-report `reference.md` section 2.1): review rounds as
  `research/reviews/NN-<kind>…` from `layout.py new-review`, revision records and `snapshots.md` (saved states as git
  commits) in `research/revisions/`, task notes declared in `plan.toml` `[layout]`; `layout.py check` runs in `make precheck`.
- `scripts/` – repository tooling: `fetch-datasets/` (dataset fetcher, sources in `datasets.toml`), `build-submission/`
  (builds `submission/N04_Project/` and its ZIP as the submission instructions ask: five reports, one deck, source code).
- `docs/` – project-wide guides: `data-analytics-skills-map.md` maps trusted agent skills (installed and suggested) to
  the ten stages of the analytics lifecycle, with alternatives, comparison pairs, gaps and install commands.
- `.agents/skills/` – all agent skills; GitHub provenance in `skills-lock.json` (update with `npx skills update`).
  Each skill has a relative symlink in `.claude/skills/` (`ln -s ../../.agents/skills/<name> .claude/skills/<name>`),
  so Claude Code and other agents read the same copy; `.claude/` is git-ignored, so recreate the links after a clone.
  - Project and tooling: `data-analyst` (lifecycle and methodology for the final project), `pdf2md`, `skill-creator`, `slidev`,
    `research-report` (evidence-backed report from an outline, with plan, ledger and research trail), `build-report`
    (checks, Vietnamese twin and Word build of a report).
  - Data work on OULAD, by step:
    - explore and check quality: `explore-data`, `exploratory-data-analysis` (scripted profile and leakage audit;
      pass absolute paths, `--max-rows 1000000` and `--max-bytes 536870912` for large files); the OULAD baseline
      profile (code, results, logs, `report.html`) is in `datasets/oulad/exploration/`;
    - wrangle: `polars` (full 10.6M-row `studentVle.csv`), `dask`, `vaex`;
    - statistics and models: `statistical-analysis`, `statsmodels`, `scikit-learn`, `scikit-survival` (time to
      withdrawal), `pymc`, `shap`, `statistical-power`, `experimental-design`;
    - visualise and report: `data-visualization`, `create-viz`, `seaborn`, `matplotlib`, `scientific-visualization`,
      `build-dashboard`, `analyze`; page design of HTML reports: `frontend-design` (aesthetic direction, typography,
      layout), `theme-factory` (10 colour and font themes);
    - check before sharing: `validate-data`; SQL and data dictionaries: `sql-queries`, `write-query`,
      `data-context-extractor`.

## Setup

```bash
python3 -m venv venv                                  # shared environment, git-ignored
venv/bin/pip install -r <folder>/requirements.txt     # per-task dependencies
cd samples/slidev && pnpm install --frozen-lockfile
```

Skill scripts with a `# /// script` header declare their own dependencies: run them with `uv run <script>`.

## Commands

```bash
cd samples/slidev && pnpm dev | pnpm build | pnpm export | pnpm ppt # reference deck
venv/bin/python scripts/fetch-datasets/fetch_datasets.py [--all | names]        # OULAD by default -> datasets/
uv run .agents/skills/pdf2md/scripts/convert.py <file.pdf>                      # PDF -> Markdown
uv run .agents/skills/pdf2md/scripts/verify.py <file.pdf> <file.md>             # must print RESULT: PASS
venv/bin/python .agents/skills/data-analyst/scripts/stats_helpers.py --selftest  # data-analyst helper self-test
venv/bin/python .claude/skills/research-report/scripts/progress.py --base reports/milestone-1 next  # report task: next card
venv/bin/python .claude/skills/research-report/scripts/layout.py new-review --base reports/milestone-4 --kind vi-native-review --scope g1  # next review file
make precheck TASK=milestone-1 | make build TASK=milestone-1 | make all TASK=milestone-1          # report checks and Word build
make pages TASK=milestone-1 BUDGET=10                                       # page budget: optimistic and pessimistic layout per part
venv/bin/python scripts/build-submission/build_submission.py               # submission/N04_Project/ and N04_Project.zip
```

## Working out loud

Write down every step, so that anyone can retrace the work from the files alone, in the same order you did it.

- Save each command that produces a result as code in the task folder: scripts for analysis steps, and a runner
  (for example `code/run_all.sh`) that chains them. One-off queries count too: when a quick query yields a number
  worth keeping, move it into the task's script and rerun the script before quoting the number.
- Keep intermediate results next to the final ones: script output in `results/`, independent audits in
  `evidence/`, and each run's console output in `logs/<step>.log` with its UTC timestamp, command and exit status.
- Record checks the same way as results: validations, renders and tests go into `logs/` with their command and outcome.
- Trace every number to a file in `results/`, `evidence/` or `logs/`. In working documents (analysis notes, exploration
  reports, ledgers) name that file next to the number; for a submitted deliverable keep the trace in the task's ledger
  and research trail, and let the deliverable name only what is submitted (see "Submitted deliverables read on their own").
- Give each working analysis report a methods checklist: `- [x]` for each method applied, with its output file, and
  `- [ ]` for each method still to run.
- In conversation, state each command, its result and what it means as you go, then summarise the final state.

## Keep, commit, submit

Working out loud keeps every step on disk; three tiers then decide where each file goes, so the repository stays lean
and the submission stays self-contained. `.gitignore` carries the first decision: whatever it matches stays local.

| Tier | What belongs | Where it lives |
| :---- | :---- | :---- |
| Keep on disk | Everything the work produces: raw data, downloads, intermediate tables, scratch output, every log | The task folder, or the session scratchpad for throwaway trials |
| Commit | The text record that lets anyone retrace and rebuild the work: code and runners, `results/` and `evidence/`, `logs/`, research notes (`crawl.md`, comprehension notes, claims, register), ledgers, plans, report sections, built deliverables | Git |
| Submit | The deliverables the instructor reads: the built Word reports, slide decks and data packages | The submission, built from committed files |

- Commit a file when it records a decision, a result or a check, or when it is needed to rebuild a result; small text
  files (scripts, Markdown, CSV results, logs) are the default commit.
- Keep a file local when a committed script or a pinned download re-creates it: raw datasets, package `raw/`,
  `interim/` and `processed/` data, source downloads (`research/sources/*/raw.*`, whose readable `crawl.md` is
  committed), page renders of built documents (`results/table-audit/`, whose measurements are in `logs/`), caches
  and environments. Add its pattern to `.gitignore` with a one-line comment naming the command that
  re-creates it.
- When a new kind of file appears, place it in a tier before the next commit: a `.gitignore` rule for local files, or
  a commit for the record. `git status` then lists only work still to be placed.
- Submit only what the instructor needs (see "Submitted deliverables read on their own"); the committed record
  behind it stays in the repository for the team.

## Testing and verification

- Run every script you add or change, and check its output against the source it derives from.
- PDF-derived Markdown is complete when `verify.py` prints `RESULT: PASS` and every page has been compared with its render.
- Skill changes: test each check on deliberately broken input, then re-run the skill's `evals/`.
- Report each verified item with its command and result, and list separately the checks still to run.

## Code conventions

- Save a script in the folder of the task it serves; reusable tooling lives in its skill's `scripts/`.
- Use the shared `./venv` interpreter; record new dependencies in that folder's `requirements.txt`.
- Use paths relative to the script or passed as arguments, so scripts run on any machine.
- Deterministic work (parsing, converting, checking) goes in scripts; skills' `SKILL.md` keeps the judgment steps.
- Add the run command of any new script to its folder's `README.md`.

## Writing conventions (reports and Markdown documents)

Report Markdown files are sections of one formal report compiled to Word.

- Give each file one topic. Nest headings one level at a time (`#` → `##` → `###`), write full paragraphs, and
  use tables or numbered lists where they aid reading.
- State what is, what works and what is recommended. Include every limitation, phrased as a condition or
  scope: "reliable for courses with ≥ 200 students; smaller courses need a separate check".
- Describe the final state only. Earlier drafts, interview rounds and revisions may be reused or reworked, but the
  report never mentions them ("earlier round", "replaced", "no longer", "revision R3", "adapted from"): readers have
  only the final document. Process history stays in the task's ledger, plan, research trail and logs.
- Build cumulatively: each sentence adds evidence toward the section's point, linked by additive or causal
  connectors ("in addition", "as a result", "building on this"); let facts carry the argument.
- Every section reads on its own:
  - Restate, then point: "the primary KPI is completion rate at day 60 (Section 3.2)". The sentence carries the
    meaning; the reference invites the reader to go deeper.
  - Keep the definition, number or rule a sentence depends on in the same paragraph.
  - Pair each identifier with its words: "the late-submission question (AQ2)".
  - Define a concept where it is first needed, before anything that relies on it.
  - Introduce each table or figure in the sentence before it and state what it shows.

### Submitted deliverables read on their own

The instructor reads only what is submitted: the Word reports, their slide decks and the data packages. Every
deliverable is complete with those files alone.

- Refer only to material that travels with the submission: sections, tables, figures and appendices of the same report;
  files inside a submitted package, named by their path within that package; earlier milestone reports by milestone
  and section; and published works in the reference list.
- Keep repository material in the repository: task folders, `logs/`, `research/`, `code/`, skill scripts, source and
  claim IDs (S201, C5-012), machine paths and `venv` stay in the ledger and trail, where they support the team's
  traceability.
- State evidence in words inside the deliverable: "computed from the 2013 training runs (Appendix III)", with the
  number and its population in the sentence.
- Make each data package run from a clean copy outside the repository: its own requirements, its inputs inside the
  package or fetched from a pinned public download.
- Before each build, scan the report sections and the built documents for repository paths and internal IDs, and
  test each package from a clean copy.

## Source material

- Keep instructor briefs, raw datasets and submitted deliverables in their original state; write derived files
  alongside them under new names.
- Write Vietnamese content in Vietnamese; translate when the user asks for it.
- Commit by the tiers of "Keep, commit, submit"; secrets always stay local. Change `skills-lock.json` together with
  installing or updating a skill from GitHub, and add its `.claude/skills/` link.

## Commits

Conventional Commits, as in the history: `feat:`, `fix:`, `docs:`, `chore:`, optional scope (`feat(skill): …`).
