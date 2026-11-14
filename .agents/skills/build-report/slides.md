# Slide decks

A deck presents a report to an audience in a talk of about 25 minutes, in every language of the task. It is a Python
script in the project root (`build_slides_taskN.py`) that draws each slide with the skill's kit,
`scripts/slidekit.py`, and builds `build/taskN/Slides_EN.pptx` and `Slides_VI.pptx`. English text is written in the
script; the Vietnamese lives in `slides_taskN_vi.py`, a dict `VI` keyed by the English text. A new deck starts from
`templates/deck/example_deck.py`, a runnable deck with one slide per proven layout (section 6).

## 1. Workflow

1. **Plan from the report.** Read the whole report, then list the slides (about 30 for 25 minutes, 45–60 seconds
   each). Decide what the audience must understand and give it room; fold bibliographic and procedural detail
   (identifiers, versions, review procedures, data provenance, long inventories) into the speaker notes or leave it to
   the report. For each slide, name the visual it needs and why (section 3).
2. **Write the English deck.** One function per slide (`s_name(prs)`), a `SLIDES` list, `DECK_TITLE` (one line
   that names the deck in agent prompts) and `build(lang)` calling `kit.build_deck(...)`; start from a copy of the
   example deck (section 6) and keep the layouts the content needs.
3. **Build, look, check.** Build with `SLIDES_OUT_DIR=<draft folder> python build_slides_taskN.py --lang en` (the project's Python).
   Every `! en … needs … has …` line is content that overflows its room at the fixed type scale: re-lay out or split the
   slide, keeping the type scale. Preview with `scripts/preview_slides.py DECK --out DIR` and read `contact.png`, then
   every dense slide at full size. Run `scripts/check_slides.py DECK --lang en --task taskN` to 0 errors and 0 warnings.
   Then run the **slide-only reading pass**: a separate agent that has not seen the notes, the script or the report
   reads the previews and `slidekit.py text DECK --slides-only`, plays the audience named for the deck, and lists per
   slide the undefined terms, unreadable visual elements (a mark, colour or axis without a key) and points it cannot
   see. Fix every item that blocks or slows understanding on the slide itself (section 2, "Every slide reads on its
   own"), then run the pass again on the changed slides.
4. **Translate.** `slidekit.py prompt translate build_slides_taskN.py --task taskN --voice group|solo --scratch DIR`
   writes the strings still to translate into the scratch folder and prints the translator's prompt
   (`templates/prompts/deck-translate.md`, filled from the deck, the task and the language pack); hand it to a
   translator agent, which writes `slides_taskN_vi.py` following section 5.
5. **Review natively.** `slidekit.py prompt review … --log FILE [--focus TEXT]` builds the Vietnamese deck, writes its
   plain text for the first reading pass and prints the reviewer's prompt; a separate agent, other than the translator,
   runs the three passes of `languages/vi/review.md` plus a slide-only read and logs its edits.
6. **Final read and checks.** Read every Vietnamese title and lead aloud yourself, run `check_slides.py --lang vi` to
   0 warnings, preview again, and build into `build/taskN/`. Register the deck in `tasks.toml`
   (`hooks.extras`, `hooks.extra_checks`, and the Vietnamese module in `people_files`) so `report.py all taskN`
   builds and checks it, and record it in the task's progress ledger when it keeps one.
7. **Later English edits.** After changing English strings, `slidekit.py sync build_slides_taskN.py` lists the keys
   that went missing or unused and pairs each changed string with the key it replaces; `--write` renames those keys,
   keeping their values for a review against the new English. A change to the deck script that should leave the
   slides as they are is proven with `slidekit.py diff OLD.pptx NEW.pptx` (0 parts differ).

## 2. Content rules

- **Titles** are short topic headings in plain words ("Finding Stored Values", "Generator 1: Divide and Conquer",
  "Selector Versus Majority Vote"; Vietnamese in sentence case) under a small section label (`Part 2 · Method`).
  Short and plain together: a newcomer grasps the topic from the title alone, so a title is never a bare term the
  slide only explains in its body ("Ablation Study", "Round-Robin Tournament"), never vague ("Headline Results",
  "Strengths"), one component keeps one name in every title, and slides of one series are numbered. The message goes
  in the lead line under the title, one sentence that states what the slide shows, and in the body; the title itself
  stays a topic heading, not a claim.
- **Middle level.** Explain how things work and why the evidence says what it says, with numbers, at the
  level of mechanism above pseudocode and implementation detail. Every concept appears on a slide before a later slide uses it.
- **Every slide reads on its own.** A reader who has the deck but not the presenter understands each slide from
  what is on it; the notes add delivery, context and depth, never a definition or a key the slide needs. In practice:
  - **Define on the slide where a term first appears**: a short gloss beside it ("execution accuracy (EX): the share
    of questions whose query returns exactly the gold rows"), a "Key terms" strip, or a card. Later slides use the
    term's one name (the report's term) without defining it again; symbols in a formula are named under it.
  - **Give every visual its key on the slide**: what is measured and in what unit (an axis title or a chart title such
    as "Questions answered correctly (%)"), what one mark stands for ("one square = one candidate query"), what each
    colour means (a legend or coloured words), and what a reference line or bracket marks.
  - **State the point in plain words**: the lead line says what the slide shows and why it matters, and the body ends
    with what follows from it, so no slide is a set of numbers to decode.
  - **Spell out names once**: a dataset, model or system is introduced with what it is ("BIRD, a benchmark of 12,751
    questions over 95 real databases"), an abbreviation with its full form.
  The slide-only reading pass (workflow step 3) tests this rule.
- **Cumulative flow.** Order slides problem → mechanism → evidence → assessment → use → conclusions. Each slide's
  notes open from the previous slide and hand over to the next.
- **On-slide text** is short complete clauses or sentences a presenter can read aloud, in both languages, rather
  than keyword fragments joined with "·". Cards have a 2–5 word head and a one- or two-sentence body.
- **Speaker notes** start with the spoken time, `(~50 seconds)` / `(~50 giây)`, and carry what the presenter adds:
  the walk through the visual, the reasoning between the points, examples and the hand-over. Presenter
  names appear only on the title slide, as authors; the kicker line, the outline and the notes stay free of them, and
  hand-overs point to the next part ("The next part weighs the evidence") rather than to a person. The Vietnamese notes of a solo deck speak as "em"; a group deck speaks as "nhóm", written "Nhóm" at the start of a sentence (lessons S1c); the authors of the reviewed
  work are always "nhóm tác giả" (guide section 3.2), so every sentence makes clear who acts.
- **Honesty.** An illustration built by the authors of the deck is labelled as such on the slide (a footnote), and
  every number on a chart or card has its source in a footnote (`foot()`).
- **Closing.** A conclusions slide ordered from the firmest to the most qualified finding, an open-problems or
  take-home slide, then a thank-you slide.

## 3. Visuals

Add a visual where the idea is a **sequence** (a pipeline, a loop, a procedure), a **structure** (what feeds what,
which reference each score uses), a **comparison or trend** (results, ablations, rankings that flip) or a **worked
example** (one item followed through the method). A figure adds what a table cannot show, so a table already shown stays a
table, and list-like content stays a list rather than a grid-shaped figure. Before calling a deck finished, check that
every slide that needs a visual of these four kinds has one.

- **Diagrams are native shapes** (`node`, `flow_row`, `arrow`, `path`, `chip`, `label`), drawn in each language, so
  their text is real slide text that the checks and the translators see. A ready-made diagram type from `diagrams.py`
  (sequence, tree, branches, loop flow, decision ladder, timelines, Gantt lanes, token strip, pair matrix, unit rows,
  risk matrix, stripe cards and more; figures.md section 1) goes on a slide natively with
  `dg.<type>(…, medium="slide", width=W).to_slide(s, x, y, name=…)`: one group of editable shapes, checked like a
  figure. Charts can be native too (`native_charts.py`, figures.md section 6). Node styles carry meaning consistently:
  `agent` for an LLM step, `system` for a tool or engine, `input`, `out` for a result, `bad` for an error, `ref`
  for a reference.
- **Charts are matplotlib PNGs at 400 dpi at their exact size on the slide** (`chart()`), rather than PowerPoint
  charts (blurry in some viewers) or report PNGs scaled up. Inside `chart()`, draw with the chart forms of
  `charts.py` (`ax = charts.axes(fig)`, then `charts.bars`, `dots`, `stacked`, `lines`, `slope`, `scatter`,
  `heatmap`, `venn`, `hist`; figures.md section 1 says which form fits which job): they apply the slide type sizes,
  the language's number style, direct labels, recessive axes and the palette's series order (`C_BLUE` the baseline,
  `C_WARM` the method, `C_GREYBAR` others), and the plot area is fitted to its labels. Labels go through `T()`.
- **Icons** (`icon(s, name, x, y, size, color, bg)`, 46 names in `icons.py`) mark a node, a card or a tile so the
  slide is quick to scan; each sits beside its word, in the element's colour (white on a solid fill, with the fill as
  `bg`).
- **Formulas** are rendered once with mathtext (`formula()`), one per line.
- A label inside a chart has fixed room in both languages: when a translation overflows, change the chart (put
  the label beside the bar, widen the margin) and keep the wording.

## 4. The kit

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / ".claude" / "skills" / "build-report" / "scripts"))
import slidekit as kit
from slidekit import (CW, END, EMU, MX, PT, D, T, I, lead, note, foot, node, flow_row, cards_at, side_cards, split,
                      chart, clean_axes, table_at, panels)

OUT = {"en": ROOT / "build" / "taskN" / "Slides_EN.pptx", "vi": ...}
kit.use_strings("slides_taskN_vi")

def s_loop(prs):
    s = kit.base(prs, K["p2"], T("The Cleaning Loop"), T("(~60 seconds) ..."))
    y = lead(s, T("Three agents plan one operation at a time; a tool executes it"))
    flow_row(s, y, 1.6, [(T("Input"), None, "input"), (T("Agent"), T("plans a step"), "agent"),
                         (T("Tool"), T("executes it"), "system"), (T("Result"), None, "out")])

def build(lang):
    kit.build_deck(lang, SLIDES, OUT[lang], FOOTER_EN, cache=ROOT / "build/.cache/slides/taskN", before=kickers)
```

A deck without a footer line passes `FOOTER_EN = ""`: `base` then places the slide number at the right end of the kicker line, and the deck can extend its content area by setting `kit.END = END = 7.3` (0.2 in above the bottom edge) right after importing the kit.

| Layer | Names | Notes |
| :---- | :---- | :---- |
| Theme | `NAVY INK GREY LINE SOFT WHITE PLUS MINUS BLUE WARM VIOLET`, fills, `W H MX TOP BOTTOM CW END`, `PT` | 13.333 × 7.5 in; `PT`: cover 36, title 26, lead 18, head 18, body 16, small 12, number 48 |
| Primitives | `text rect base table points link number_fields arial_theme` | EMU arguments, as python-pptx |
| Measuring | `lh line_h list_height list_h node_h num_h room` | inches; `room()` prints content that does not fit |
| Blocks | `lead note foot table_at cards cards_at panel_list panels side_cards split bignum` | inches; return the y below; `cards_at(..., icons=[…])` puts an icons.py icon in each card's colour before its heading (or at the right of the number row) |
| Diagrams | `node chip flow_row arrow path label brace_label picture formula` | `NODE_STYLES` holds the node styles |
| Charts | `chart clean_axes HEX C_*` | `chart(s, name, x, y, w, h, draw)` with `draw(fig)` |
| Strings | `use_strings T D MISSING` | `T()` returns English or the VI form and collects missing keys |
| Deck | `build_deck` | builds, tightens text boxes (`slide_measure.tighten`), numbers pages, sets Arial theme fonts |

Common slide layouts: lead + `flow_row` + `cards_at` (a mechanism and its facts); chart on the left of a `split`
+ `side_cards` on the right (a result and its reading); `panels` (two contrasting lists); `table_at` + `bignum` tiles
(evidence and its headline numbers); a navy take-home box (`rect` + `text`) under a table.

## 5. Vietnamese

The translator reads `languages/vi/guide.md` in full (section 3 is about slides), `lessons.md` and the task's glossary
(`glossary.py --lang vi --task taskN show`), reuses the wording of the reviewed `.vi.md` report and of any earlier
reviewed deck, and writes the module with a script so that every key is byte-identical (`strings --all` gives the full
list). Placeholders and prefixes keep their spacing (`"{n} steps"`, `"Presenter: "`). One English key used in places
with different room gets one Vietnamese value; when it overflows somewhere, change the layout in the deck script
and keep the meaning. A separate reviewer, other than the translator, runs the three passes of `review.md` on the plain-text
deck, may rewrite freely within the fixed room, rebuilds, runs `check_slides.py --lang vi` to 0 warnings and appends
its log (Location | Original | Revised | Reason) to the round's file `research/reviews/NN-slides-review.md` (`layout.py new-review --kind slides-review`). Both prompts come from
`slidekit.py prompt`, which also puts the pack's line on who speaks into them (`[slides] voice_group`,
`voice_solo` in `pack.toml`).

`preview_slides.py` may mark a wrapped card head in magenta; judge by the real PNG and the text.

## 6. Example deck and proven patterns

`templates/deck/example_deck.py` builds a ten-slide deck on neutral content, one slide per proven layout, and
`example_deck_vi.py` beside it shows the form of a Vietnamese module. Build it to see the layouts at full size:
`python templates/deck/example_deck.py [--lang vi] [--out DIR]`. The self-test builds it and checks it with
`check_slides.py`, so the example always runs on the current kit.

| Slide function | Pattern | Use it for |
| :---- | :---- | :---- |
| `s_title`, `s_thanks` | Title slide with the context line; navy closing slide | opening and closing |
| `s_outline` | Outline as a grid of cards (part label, one sentence) | the plan of the talk |
| `s_pipeline` | Lead line, `flow_row` of styled nodes with icons, fact cards | a mechanism and its facts |
| `s_loop` | Row of nodes with a feedback `path` above and an exit below | a loop that repeats until a test passes |
| `s_results` | `charts.bars` with a dashed reference line in a `split`, `side_cards` beside | a result and its reading |
| `s_evidence` | `table_at`, then `bignum` tiles | evidence and its headline numbers |
| `s_matrix` | Matrix of `chip`s with a score column | pairwise comparison, a worked example |
| `s_conclusions` | Two `panels` | firm against open findings |
| `s_takehome` | Table of open problems, then a navy take-home box | the closing message |

Further patterns are built from the same kit functions:

- **Retry loop with yes/no branches:** a `flow_row`, a decision `node`, and two `path`s with `label`s ("yes", "no").
- **One item followed through several passes:** one `node` per pass in a column, with the changed value in its body
  and `arrow`s between passes.
- **Worked flaw of a metric:** `formula()` on top, then a small `table_at` with the counter-example and a
  `side_cards` reading.
- **Conclusions tagged firm / qualified / open:** `side_cards` with the tag as each head, coloured `PLUS`, `WARM` and
  `MINUS`.
- **Charts beyond bars:** a dot plot against a reference tick (`ax.plot` markers with `ax.axvline`), a 100 % stacked
  bar of shares (`ax.barh` with `left=`), a line chart of a trend (`ax.plot` with direct end labels) and a Venn
  diagram of three sets (`matplotlib.patches.Circle` with counts placed by hand), each drawn in a `chart()` callback
  with `clean_axes` and the fixed colours `C_BLUE`, `C_WARM`, `C_GREYBAR`.
- **Token strips and brackets:** a row of `chip`s, one per token, with `brace_label` under a span.
- **Content-sized diagrams** (a taxonomy, a timeline): measure each box with `node_h` or `lh` first, then place the
  boxes from the measured heights, so the diagram fits its text in every language.
