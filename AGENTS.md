# AGENTS.md

## Project overview

Coursework for MTH045 – The Science of Data Analytics (education analytics). Briefs and deliverables are mostly
Vietnamese; English technical terms stay as written. `CLAUDE.md` in each folder is a symlink to its `AGENTS.md`:
edit `AGENTS.md`, and re-read it after each change so the updated rules apply in the same session.

- `samples/` – standalone reference samples. `slidev/` is the reference Slidev deck (theme, layouts,
  section structure, Vue charts, speaker-note format): start new decks from its README.
- `final-project/` – team N04 project; has its own `AGENTS.md`, which takes precedence inside that folder.
  `milestones/<nn>/milestone-<n>.pdf` is the instructor brief, `milestone-<n>.md` its verified Markdown copy,
  `N04_*` the team deliverables.
- `datasets/` – education datasets, fetched and verified by `scripts/fetch-datasets/`; raw files stay local
  (git-ignored) and each `<dataset>/exploration/` folder of analysis results is tracked. **Analysis
  focus: OULAD** (`datasets/oulad/`); the six other datasets are reference data from the milestone 2 screening.
  `final-project/datasets` links here for earlier code.
- `scripts/` – repository tooling: `fetch-datasets/` (dataset fetcher, sources in `datasets.toml`).
- `.agents/skills/` – all agent skills; GitHub provenance in `skills-lock.json` (update with `npx skills update`).
  Each skill has a relative symlink in `.claude/skills/` (`ln -s ../../.agents/skills/<name> .claude/skills/<name>`),
  so Claude Code and other agents read the same copy; `.claude/` is git-ignored, so recreate the links after a clone.
  - Project and tooling: `data-analyst` (lifecycle and methodology for the final project), `pdf2md`, `skill-creator`, `slidev`.
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
python3 -m unittest discover -s .agents/skills/data-analyst/evals -v           # data-analyst evaluator tests
```

## Working out loud

Write down every step, so that anyone can retrace the work from the files alone, in the same order you did it.

- Save each command that produces a result as code in the task folder: scripts for analysis steps, and a runner
  (for example `code/run_all.sh`) that chains them. One-off queries count too: when a quick query yields a number
  worth keeping, move it into the task's script and rerun the script before quoting the number.
- Keep intermediate results next to the final ones: script output in `results/`, independent audits in
  `evidence/`, and each run's console output in `logs/<step>.log` with its UTC timestamp, command and exit status.
- Record checks the same way as results: validations, renders and tests go into `logs/` with their command and outcome.
- Trace every number in a report to a file in `results/`, `evidence/` or `logs/`, and name that file next to the number.
- Give each analysis report a methods checklist: `- [x]` for each method applied, with its output file, and
  `- [ ]` for each method still to run.
- In conversation, state each command, its result and what it means as you go, then summarise the final state.

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
- Build cumulatively: each sentence adds evidence toward the section's point, linked by additive or causal
  connectors ("in addition", "as a result", "building on this"); let facts carry the argument.
- Every section reads on its own:
  - Restate, then point: "the primary KPI is completion rate at day 60 (Section 3.2)". The sentence carries the
    meaning; the reference invites the reader to go deeper.
  - Keep the definition, number or rule a sentence depends on in the same paragraph.
  - Pair each identifier with its words: "the late-submission question (AQ2)".
  - Define a concept where it is first needed, before anything that relies on it.
  - Introduce each table or figure in the sentence before it and state what it shows.

## Source material

- Keep instructor briefs, raw datasets and submitted deliverables in their original state; write derived files
  alongside them under new names.
- Write Vietnamese content in Vietnamese; translate when the user asks for it.
- Commit code and documents; keep datasets, `venv/` and secrets local (they are git-ignored). Change
  `skills-lock.json` together with installing or updating a skill from GitHub, and add its `.claude/skills/` link.

## Commits

Conventional Commits, as in the history: `feat:`, `fix:`, `docs:`, `chore:`, optional scope (`feat(skill): …`).
