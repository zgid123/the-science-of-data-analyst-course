# AGENTS.md

## Project overview

Coursework for MTH045 – The Science of Data Analytics (education analytics). Briefs and deliverables are mostly
Vietnamese; English technical terms stay as written.

- `minitask/<nn>/` – individual tasks: brief PDF, data, analysis script/notebook, report `.docx`, Slidev deck in `slidev/`.
- `final-project/` – team N04 project; has its own `AGENTS.md`, which takes precedence inside that folder.
  `milestones/<nn>/milestone-<n>.pdf` is the instructor brief, `milestone-<n>.md` its verified Markdown copy,
  `N04_*` the team deliverables.
- `.agents/skills/` – agent skills: `pdf2md`, `skill-creator`, `slidev`. `skills/` is the source copy of `data-analyst`
  (installed copy: `final-project/.agents/skills/data-analyst/`).

## Setup

```bash
python3 -m venv venv                                  # shared environment, git-ignored
venv/bin/pip install -r <folder>/requirements.txt     # per-task dependencies
cd minitask/02/slidev && pnpm install --frozen-lockfile
```

Skill scripts with a `# /// script` header declare their own dependencies: run them with `uv run <script>`.

## Commands

```bash
cd minitask/02/slidev && pnpm dev | pnpm build | pnpm export | pnpm ppt         # slides
uv run .agents/skills/pdf2md/scripts/convert.py <file.pdf>                      # PDF -> Markdown
uv run .agents/skills/pdf2md/scripts/verify.py <file.pdf> <file.md>             # must print RESULT: PASS
cd final-project && python3 -m unittest discover -s .agents/skills/data-analyst/evals -v
```

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
  `skills-lock.json` together with installing or updating a skill from GitHub.

## Commits

Conventional Commits, as in the history: `feat:`, `fix:`, `docs:`, `chore:`, optional scope (`feat(skill): …`).
