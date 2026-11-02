---
name: build-report
description: Pre-check, translate, build and post-check formal reports written as numbered markdown section files (taskN/report/*.md) into finished Word documents (.docx), in English and in every other language of the task (Vietnamese today), and build their presentation decks (.pptx) with the bundled slide kit. Use it whenever the user asks to build, rebuild, compile or check a report or its Word document; to translate a report or a deck, or create, update, sync or review its Vietnamese version (*.vi.md, slides_*_vi.py); to make, rework or translate a slide deck or speaker notes for a report; to check a report before delivery (format, structure, cross-references, abbreviations, citations, names, translation parity); to verify a built .docx or .pptx; to add a report task; or to support a new language, even when the request names only "the report", "the deck" or "the Vietnamese version".
---

# Build a report in every language

A report is a folder of numbered markdown section files (`NN-SS-slug.md`) written in English, the source language, plus a twin per target language (`NN-SS-slug.vi.md`). Each language compiles, in sort order, into its own Word document. This skill covers the whole path: **pre-checks** on the sources, **translation** of whatever a target language still lacks, the **build**, and **post-checks** on each Word file. Task settings live in `tasks.toml`; everything about a language lives in its pack under `languages/<code>/`, so the scripts stay general.

Read [reference.md](reference.md) before writing, translating or changing a report: source conventions (section 1), `tasks.toml` (section 2), language packs (section 3), the translation workflow (section 4) and every check with its fix (sections 5 and 6). Before translating into a language, also read that pack's `guide.md` and `lessons.md` (what human reviewers changed) and, for review, its `review.md` and print the task's glossary (`glossary.py --lang vi --task TASK show`): common technical-reporting terms plus the domain and topic layers the task selects.

## Requirements

- Python 3.11 or later with the packages in `requirements.txt` (`python3 -m venv venv && venv/bin/pip install -r .claude/skills/build-report/requirements.txt`); `pypandoc_binary` bundles pandoc. The Arial fonts are needed for exact text measuring (`slide_measure.FONT_DIRS` lists where they are looked up).
- A project root holding `tasks.toml` (reference.md section 2); `report.py init TASK --title "…"` creates it from `templates/tasks.toml`, which documents every field, together with the Makefile and a starter report. The scripts find it in `BUILD_REPORT_ROOT`, else in the current folder, else four levels above the scripts, where a project-level skill lives (`<project>/.claude/skills/build-report/`). They run hooks and helper scripts with the project's `venv/bin/python` when the project has one, and with the interpreter that runs them otherwise; the commands below write `python` for that interpreter.
- Outputs go where `tasks.toml` says; caches and self-test copies go to `build/.cache/` in the project.

## Commands

Run everything from the project root. `templates/Makefile`, copied to the project root, wraps the same commands (`make all`, `make translate TASK=taskN`, `make build TASK=taskN L=vi`, `make precheck`, `make postcheck`, `make test`); it uses the project's `venv/bin/python` when there is one.

```bash
R=".claude/skills/build-report/scripts/report.py"
python $R init      TASK [--title TEXT] [--author TEXT]   # new project or task: tasks.toml, Makefile, TASK/report/
python $R list                       # tasks, outputs, hooks and language packs
python $R translate TASK|all [--lang CODE]   # quick check: what each target language still needs
python $R precheck  TASK|all         # sources, translation status and parity
python $R build     TASK|all [--lang CODE] [--no-figures]
python $R postcheck TASK|all [--lang CODE]
python $R all       TASK|all         # precheck → build → postcheck, language by language
python $R test                       # self-tests with fault injection, then [project] tests
```

A reviewed single-file version of a report (for example a Google Docs export edited by a person) is split back into the report's file layout for side-by-side comparison with `scripts/split_export.py --export FILE --report DIR --lang CODE --out DIR`. It writes each section under the report's own file name in a separate folder, undoes the export's escapes outside formulas, maps figures to the report's image files, and lists every file with its similarity to the source in `_split-report.md`. `scripts/review_diff.py` then prints every changed paragraph with a word diff, the evidence for the pack's `lessons.md` (reference.md section 4.7). When citations move, are added or are removed after the references were numbered, `scripts/renumber_refs.py --report DIR --lang CODE [--write] [--drop-unused] [--map FILE]` numbers them again by first citation and rewrites the reference list to match. Reviewed corrections written as FIND/REPLACE blocks (a drift audit, a source check) are applied with `scripts/apply_fixes.py --report DIR --fixes FILE … [--skip IDs] [--write]`, each exactly once or not at all; `split_export.py --repair` restores list numbers, formulas and code fences that an export lost, in a split folder that was edited since.

Every step prints one line (`PASS`/`FAIL`, step, result) and its details when it fails.

## Workflow

1. **Quick check of the languages.** Run `translate` for the task. For each target language it lists the twins that are `missing` or `stale` in report order, the language guide, the domain glossary, and the language-only pages the pack offers. When the list is empty, go to step 3.
2. **Translate what is open** (reference.md section 4). A whole report runs in the stages of reference.md section 4.3: terms first, then front matter, translation in parallel groups, native review of every file by a reviewer other than its translator (the pack's `review.md`), a consistency pass and the build. For each file:
   - parallel translators and reviewers start from the prompt templates `templates/prompts/report-translate.md` and `report-review.md` (fill in `{python}`, `{skill}` – the interpreter and this skill's folder – and the files, task, report folder and scratch folder), so every agent reads the same guide, lessons and glossary;
   - read the language's `guide.md` and the task's merged glossary once (`glossary.py --lang CODE --task TASK show`), then for each file read the current source file in full (and the existing twin when it is stale, so reviewed wording carries over);
   - write the twin natively for that language's readers, with the structure, numbers, formulas, figures and citations identical to the source;
   - check the pair with `check_parity.py --report DIR --lang CODE FILE`, then record it with `translation_status.py --report DIR --lang CODE --mark FILE` (it re-runs the parity check and records only passing files);
   - at a language's first build, offer the user the pack's language-only pages (for Vietnamese: Lời cảm ơn, Lời cam đoan); add each chosen page with `report.py translate TASK --lang CODE --add-extra NAME` and fill in its placeholders with the user.
3. **Pre-check the sources.** Run `precheck`. It runs, for every language: `check_format.py` (house style and pandoc traps), `check_structure.py` (heading and caption numbering, cross-references in each language's words, images, footnotes), `check_style.py` (text addressed to the reader, and each language's spelling), `check_abbreviations.py`, `check_citations.py`, `check_names.py` (people's names spelled exactly as `people` in `tasks.toml` lists them), the task's `hooks.checks`; then for each target language its translation status and `check_parity.py` (structure plus the pack's conventions). Fix every `ERROR` (reference.md section 5); report each `WARN` that is a content decision to the user.
4. **Build.** Run `build`, or `all` for steps 3–5 together. Figures render once (`[taskN.figures]`), then one `.docx` per language with its pack's interface words and layout, then `hooks.extras` (for example a slide deck). The general checks gate every language; each target language is built once its own translation and parity checks pass, so the English document is ready while a translation is in progress.
5. **Post-check the Word documents.** Run `postcheck`. `check_docx.py` compares each document with its sources, checks layout, fields, numbering, headers and metadata, finds markdown leftovers and open placeholders, and applies the target language's conventions to the Word text. Translated slide decks are checked with `check_slides.py DECK --lang CODE`. Fix causes in the sources or the builder and rebuild, so the `.docx` always matches its sources.
6. **Report back** with the summary lines: languages built, files translated, checks passed, warnings for the user, and each document's figure and table counts.

## Figures

Report figures are code: a task's package in the project (for example `figures/taskN/`) lists `FIGURES = {output name: builder}` in its `__init__.py`, and each builder draws with this skill's visual kit, all in one validated colour set (`palette.py`): `c4kit.py` (a canvas for C4 and box-and-arrow diagrams, boxes with icons), `diagrams.py` (sequence, timelines, state machine, process, cycle, branches, loop, decision ladder, tree, matrices, layers, Gantt lanes, token strip, unit rows, cards, comparison, annotated screenshot), `charts.py` (bars, dots, stacked bars, lines, slope, scatter, heatmap, Venn, histogram, with numbers in each language's style), `icons.py` (46 pictograms), `scene.py` (one drawing rendered as an image or as native, editable PowerPoint shapes, so every diagram type goes into a report or onto a slide natively) and `native_charts.py` (editable PowerPoint charts). Word reports take figures as pictures, optionally as SVG with a PNG fallback (`vector_figures`). Read [figures.md](figures.md) before planning figures: which visual fits which job, the modules, the design rules and the layout check. `python scripts/gallery.py OUT_DIR` draws every visual of the kit with example content into one contact sheet to choose from. `render_figures.py TASK [filter]` writes the PNGs into `<report>/assets/figures/`, shared by every language (a builder with a `lang` argument also writes `<name>.<code>.png`), and checks each one for overlapping, cut-off or crossed labels, text past its box, text printing below 6 pt and empty margins; the build's figure step counts the findings, and `render_figures.py TASK` lists them.

## Slide decks

A report's presentation is a deck script in the project root built with this skill's kit, `scripts/slidekit.py` (theme and type scale, layout blocks, native diagrams, 400-dpi charts, Vietnamese strings keyed by English, `build_deck`). Read [slides.md](slides.md) before planning or changing a deck: the workflow from plan to reviewed Vietnamese, the content and visual rules, the kit's catalogue and a gallery of proven slide patterns. The kit's command line carries the deterministic steps: `strings` lists what the translator still has to write, `prompt translate|review` writes the translator's or reviewer's prompt with the deck's files, `text` gives the reviewer the deck as text, `sync` renames Vietnamese keys after English edits, and `diff` proves that a refactor changed nothing; `preview_slides.py` and `check_slides.py` check the result.

## Adding a task or a language

- **New report task:** run `report.py init taskN --title "…" --author "…"`. It adds the `[taskN]` tables to `tasks.toml` from `templates/tasks.toml` (every field with its meaning; optional ones commented out) and copies a starter report into `taskN/report/` that passes every check, so `report.py all taskN` builds a Word document at once; then replace the starter sections with the report. By hand, add a `[taskN]` table to `tasks.toml` with `report`, `build`, `author` and one `[taskN.<lang>]` table per language (`out`, `title`, `short_title`, `subject`, and for a target language its `glossaries` list of domain and topic files), and `people`, the lecturers' and authors' names copied character for character from the user's title page; optional `figures`, `hooks`, `citations`, `abbreviations` and `structure` tables are in reference.md section 2. Then run `report.py all taskN`.
- **New language:** create `languages/<code>/` with `pack.toml` (interface words, conventions as data, `[translation]`), `guide.md` (how to write natively for that language's readers), `glossaries/` (common, domains, topics) and, if the language's reports carry extra pages, `templates/` (reference.md section 3). The scripts pick it up from there; add the language's checks to the self-test.

## Principles

- Report text addresses the reader with information only: facts, findings and signposts such as "Table 3.8 summarises…". A conclusion states what is now known about the subject and what follows from it; sections appear in it as pointers. Benchmark material states what is measured and how, as a specification. `check_style.py` holds each language's phrase list for this.
- Figures change through their source code in `figures/taskN/` and are re-rendered, so every PNG is reproducible.
- Tooling runs on the requirements above; a new capability uses what they and the system already provide, so the skill keeps working wherever it is installed.

- Keep scripts general: titles, authors, glossaries, citation rules and hooks belong in `tasks.toml`; interface words, conventions and writing guidance belong in the language pack.
- Translate for the reader: each twin reads as if written natively in its language, while its structure stays identical to the source, so numbering, cross-references and citations hold in every language. The six translation principles at the head of reference.md section 4 (complete phrases for a reader without the source, one term per concept across deliverables, a named actor in every sentence, meaning before fit, briefed fresh reviewers, every correction turned into a rule) apply to every language and deliverable; `glossary.py coverage` measures term drift.
- Deliver only documents whose checks pass; `--force` is for inspecting drafts.
- After changing any script, pack or guide rule, run `report.py test` (fault injection, 100 % expected) and `report.py all` (every task passes with unchanged figure and table counts).
