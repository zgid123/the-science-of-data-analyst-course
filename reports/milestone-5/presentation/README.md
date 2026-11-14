# Milestone 5 presentation

Everything behind the Milestone 5 slide decks: the storytelling drafts, the speech scripts, the plans and the reviews.
The decks are built with the build-report slide kit (`.claude/skills/build-report/slides.md`) by deck scripts in the
project root, as the kit requires, and written to `reports/milestone-5/build/`.

## Naming

Each deck generation has a version and a scope, and every file that belongs to it carries the same scope:

| Generation | Folder here | Deck code (project root) | Built decks (`build/`) | Checks (`tasks.toml`) |
| :---- | :---- | :---- | :---- | :---- |
| v1, 30-slide limit | `v1-30/` | `build_slides_milestone5_30.py`, `slides_milestone5_30_vi.py` | `N04_Milestone5_Slides-30_EN.pptx`, `…-30_VI.pptx` | `slides_30_en`, `slides_30_vi` |
| v2, full, no limit, with its main / appendix split | `v2-full/` | `build_slides_milestone5_full.py`, `slides_milestone5_full/` (Vietnamese to come: `slides_milestone5_full_vi.py`) | `N04_Milestone5_Slides-Full_EN.pptx`, `N04_Milestone5_Slides-Split_EN.pptx` | `slides_full_en`, `slides_split_en` |
| v3, 15 main slides for a manager, the rest as appendix | `v3-15/` | `build_slides_milestone5_15.py`, `slides_milestone5_15/` (reuses `slides_milestone5_full/`) | `N04_Milestone5_Slides-15_EN.pptx`, `…-15_VI.pptx` (strings in `slides_milestone5_15_vi.py`) | `slides_15_en`, `slides_15_vi` |

Inside a generation: each brief sits in the folder of the work it governs and is named `BRIEF.md`; drafts are named
`<letter>-<method>.md` after the storytelling method that wrote them (the skill of the same name); the speech script is
`speech-script.md`. Code steps that serve the decks are `reports/milestone-5/code/deck_*.py`. Chart images are cached
as `m5-30-<chart>` and `m5-full-p<part>-<chart>`. Build logs keep their task number (`logs/T27_…` to `T33_…`).

## Status

| Deck | What it is | State |
| :---- | :---- | :---- |
| Slides-15 | The analytics lifecycle in 15 main slides for a manager (one new slide, "What Changed Along the Way"), the closing slide, a two-page appendix index and the other 79 slides of the full deck; speaker notes of the main slides in `v3-15/speech-script.md` carry the full delivery of each slide from end to end, one paragraph per step (about 43 minutes) | Built and checked in English and Vietnamese (translation, crossed native review and reader tests until every flag closed, for the slides and again for the end-to-end notes) |
| Slides-Full | Every slide of the ensembled story, 94 slides in story order | Built, checked, reviewed slide by slide |
| Slides-Split | The same slides: 51 main slides, the thank-you slide, an Appendix divider with an index, 43 appendix slides | Proposal; the main slide count is set by the team after review, then the Vietnamese deck is built |
| Slides-30 (EN, VI) | The first deck, written to a 30-slide limit | Earlier version; its Vietnamese deck is the presentation in the submission ZIP (`N04_Project.pptx`) until the team chooses another |

## Folders

```
presentation/
├── v3-15/                       the 15-slide deck for a manager
│   ├── speech-script.md         speaker notes of the 15 main slides and the closing slide, one paragraph per
│   │                            delivery step (blank lines become paragraph breaks), read by build_slides_milestone5_15.py
│   └── reading-pass-en.md       slide-only reading pass of the English deck and its fixes
├── v2-full/                     the full deck and its split (current)
│   ├── drafts/
│   │   ├── BRIEF.md             brief of the drafts: coverage of the brief's report parts, hard rules, no slide limit
│   │   ├── A-storytelling-with-data.md
│   │   ├── B-scqa-pyramid.md
│   │   └── C-data-storytelling-arc.md
│   ├── ensemble-plan.md         94 slides in story order: source draft slides, main / detail line, reused v1 slides
│   ├── script-parts/
│   │   ├── BRIEF.md             brief of the four range agents: script format, slide-code rules, build and review
│   │   └── part1.md … part4.md  the script by range of plan slides (1–21, 22–46, 47–69, 70–94)
│   ├── speech-script.md         assembled script; the full deck reads its speaker notes from here
│   └── appendix-split.md        the proposed split: main slides with time and pointers, appendix slides with reasons
└── v1-30/                       the first deck (30-slide limit)
    ├── drafts/
    │   ├── BRIEF.md             brief of its two drafts
    │   ├── A-storytelling-with-data.md
    │   └── B-scqa-pyramid.md
    ├── speech-script.md         slide text and speaker notes of build_slides_milestone5_30.py
    ├── outline.md, budget.json, timing-report.txt   25-minute word budget and timing (write-talk-script skill)
    └── reading-pass-en.md       slide-only reading pass of the English deck and its fixes
```

## From brief to deck (v2)

1. `v2-full/drafts/BRIEF.md` → three independent drafts, each complete with no slide limit.
2. The drafts → `v2-full/ensemble-plan.md`: the union of their topics in story order, one idea per slide.
3. `v2-full/script-parts/BRIEF.md` → four range agents write `script-parts/part1–4.md` and the slide code
   `slides_milestone5_full/part1–4.py`.
4. `reports/milestone-5/code/deck_full_script.py` → `v2-full/speech-script.md`.
5. `build_slides_milestone5_full.py` → `Slides-Full` and `Slides-Split`.
6. `reports/milestone-5/code/deck_appendix_split.py` → `v2-full/appendix-split.md`.

## Code (project root)

| File | Role |
| :---- | :---- |
| `build_slides_milestone5_30.py` | v1 deck, English and Vietnamese; also the theme, helpers and charts the v2 deck reuses |
| `slides_milestone5_30_vi.py` | Vietnamese strings of the v1 deck, keyed by the English text |
| `build_slides_milestone5_full.py` | v2 deck in two layouts (`--layout full|split|both`); `SPLIT` lists the appendix slides |
| `slides_milestone5_full/` | `common.py` (plan, notes, layout-aware references, appendix labels) and `part1–4.py` (one function per plan slide, named `s<plan number>`) |
| `build_slides_milestone5_15.py` | v3 deck, English and Vietnamese (`--lang en|vi|all`): `MAIN` lists the 15 main slides by plan number, `CLOSING` the closing slide; every other plan slide becomes an appendix slide behind a two-page index; notes of the main slides from `v3-15/speech-script.md` |
| `slides_milestone5_15/` | `path.py`: the one new slide, "What Changed Along the Way" (plan number 95) |
| `slides_milestone5_15_vi.py` | Vietnamese strings of the v3 deck (slides, appendix and notes, one key per note paragraph), keyed by the English text |

## Commands

```bash
venv/bin/python reports/milestone-5/code/deck_full_script.py      # script parts → v2-full/speech-script.md
venv/bin/python build_slides_milestone5_full.py                    # Slides-Full and Slides-Split (English)
venv/bin/python reports/milestone-5/code/deck_appendix_split.py    # → v2-full/appendix-split.md
venv/bin/python build_slides_milestone5_30.py                      # Slides-30, English and Vietnamese
venv/bin/python build_slides_milestone5_15.py                      # Slides-15, English and Vietnamese
make all TASK=milestone-5                                          # report, both deck scripts and every check
```

`make all` builds the three deck scripts (`tasks.toml` hooks) and checks every deck with `check_slides.py`. Check renders
with `.claude/skills/build-report/scripts/preview_slides.py DECK --out DIR`; it does not catch one text box covering
another, so read the slide images.

## Records

The work is logged in `../PROGRESS.md` (v1 and v2: T27–T33 and T37; v3: T38–T47) with build logs in `../logs/`; the
build logs keep the file names of their time. Vietnamese reviews in `../research/reviews/`: the v1 deck in
`08-slides-review-deck-vi.md` and `09-slides-review-deck-vi-fluency.md`; the v3 deck in `10-slides-review.md`, reader
tests and rewrites `11`–`18`, and its end-to-end notes in `19`–`22` (`…-notes15.md`).

Every deck rebuilds byte for byte: two builds of each script, compared with `slidekit.py diff`, differ in no part.
