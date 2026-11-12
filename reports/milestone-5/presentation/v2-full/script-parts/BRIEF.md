# Brief: ensembled script and slides for one range of the full deck

You own one range of plan slides (given in your task). For each slide in it you write (1) its section of the
ensembled speech script and (2) its slide function, then build, render and inspect your slides until each one reads
well on its own at full size. Work only in your own files; four ranges are built in parallel.

## Read first

1. `reports/milestone-5/presentation/v2-full/ensemble-plan.md` — the 94 slides in story order, the ensembling rules, and per
   slide the source draft slides (A12 = draft A slide 12) and the matching slide of the deck already built (`Deck`).
2. `reports/milestone-5/presentation/v2-full/drafts/BRIEF.md` — audience, coverage and the hard rules (numbers only from
   the Milestone 5 report with their source; AQ3/AQ4 are designs with no results; AQ2 is association only; simulated
   interviews are never evidence; no repository paths or internal IDs; team voice "we"; every identifier defined on
   the slide where it appears).
3. The source drafts for your slides: `reports/milestone-5/presentation/v2-full/drafts/A-storytelling-with-data.md`,
   `B-scqa-pyramid.md`, `C-data-storytelling-arc.md` (read the slides your rows name, and their neighbours).
4. The kit and the house patterns: `.claude/skills/build-report/slides.md` (content and visual rules, catalogue,
   pattern gallery) and `build_slides_milestone5_30.py` — every helper you need is there (`lead`, `rich`, `card`,
   `card_h`, `cols`, `key`, `bottom_key`, `fit_pt`, `table`, `table_h`, `stretch_table`, `node`, `chip`, `bignum`,
   `chart`, `closing_box`, `src`, colours, `PT`, `BODY`, `HEAD`, `END`, `X0`, `CWI`, `XR`). For a slide whose `Deck`
   column names a slide of the built deck, start from that slide function's code (copy it into your module and adapt
   it); its on-slide wording was already reviewed.
5. `slides_milestone5_full/common.py` — `notes(n)`, `ref(n)`, `kicker(n)`, `PLAN`.

## (1) Script section

Write `reports/milestone-5/presentation/v2-full/script-parts/<range>.md` (the file name is in your task), one section per
plan slide, in exactly this format (the build reads `## Slide N` and the `**Speaker notes:**` paragraph):

```
## Slide N – <Title from the plan>   [part label]   [Line: main | detail]
**Lead:** <one sentence>
**On the slide:** <what appears on the slide>
**Visual:** <the visual and why, or "none">
**Speaker notes:** <spoken register, 90–140 words, one paragraph; opens from plan slide N−1 and hands over to N+1>
**Sources:** <report sections behind every number, e.g. [M5 §11.2], [M5 App XII Table A.32]>
```

Ensemble from the source drafts as the plan's rules say: take the clearest lead and content, keep exact report
numbers, write notes that run in this plan's order. Check every number you keep against the Milestone 5 report text
(`reports/milestone-5/report/*.md`, English files only).

## (2) Slide functions

Write `slides_milestone5_full/<module>.py` (name in your task):

```python
from slides_milestone5_full.common import *   # noqa: F401,F403

def s07(prs):
    s = kit.base(prs, kicker(7), T("Withdrawal Is a Regulated Measure"), notes(7))
    y = lead(s, T("…"))
    …
    src(s, "Source: Milestone 5 report, Section 1.1.")

SLIDES = {7: s07, …}
```

Rules, all learned on the built deck (each was a real defect):
- **Title** = the plan title; **lead** = one sentence; then the content. Text sizes come only from the kit:
  `PT["lead"]` 18, `PT["body"]` 16, `BODY` 14 (dense), `PT["small"]` 12 for keys. Use `fit_pt(paras, w, room)` to
  take the largest size that fits; never shrink below 12.
- **Fill the slide.** Content runs to `END` (7.2 in). In each column fix the gaps (0.2–0.3 in) and give the free
  height to one element (cards via `h=`, table rows via `stretch_table`, a chart's height, a timeline, a number box);
  anchor keys and closing lines to the bottom edge (`bottom_key`, `END - height`). Columns end level at the bottom.
  No slide may stop at two-thirds height; no card may be half empty because it was stretched (use a larger text size
  or give the space to another element instead).
- **Keys stay with what they explain**: a key sits directly under its chart or diagram; a heading directly above its
  content.
- **Every slide reads on its own**: define every identifier and abbreviation on the slide (in the content or a
  `Key:` line); never write a bare slide number — cite another slide only with `ref(n)` (e.g. `T("the add-drop rule,
  ") + ref(39)`), because slides move between the main deck and the appendix.
- **Source line**: `src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Table A.32.")` — in words, no
  repository paths; it goes to the speaker notes, not onto the slide.
- **Charts**: chart cache names must be unique to your range: prefix them `m5-full-p<n>-` (for example
  `chart(s, "m5-full-p3-aq1-modules", …)`).
- Use `kit.room(name, need, have)` where a block could overflow; the build prints `! … needs X in, has Y in` when it
  does — fix every such line.

## (3) Build, render, inspect

Build only into your own scratch folder so ranges do not collide:

```bash
SLIDES_OUT_DIR=<your scratch folder> venv/bin/python build_slides_milestone5_full.py --layout full
venv/bin/python .claude/skills/build-report/scripts/check_slides.py <scratch>/N04_Milestone5_Slides-Full_EN.pptx --lang en --task milestone-5
venv/bin/python .claude/skills/build-report/scripts/preview_slides.py <scratch>/N04_Milestone5_Slides-Full_EN.pptx --out <scratch>/pv --slides <your numbers, comma-separated>
```

In the full layout the deck position equals the plan number. `check_slides` reports on all 94 slides (the others are
placeholders or other ranges): fix every error and warning on your slides. Then **read every one of your slide
images at full size** (not the contact sheet) and fix overlaps, cut-off text, empty bottoms, detached keys, crowded
or tiny text. `check_slides` does not detect one text box covering another: only the images show that.

## Report back

Your script file and module, the slide count, the `check_slides` lines for your slides, which slides you inspected
at full size, and anything you could not resolve (a number you could not confirm, a slide that does not fit its
content). Do not edit any file outside your two files.
