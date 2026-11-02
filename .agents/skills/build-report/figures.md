# Figures, charts and icons

A report figure or a slide visual is code in the project, drawn with this skill's visual kit, so it can be redrawn in
every language and stays consistent with every other figure. Most diagram types are described once and come out two
ways: as an image (a report figure, or a picture on a slide) or as native PowerPoint shapes that stay editable
(section 6). This file explains how to choose a visual, which
module draws it, the design rules every visual follows, and how each figure is checked. `python scripts/gallery.py
[OUT_DIR] [--lang vi]` draws every visual of the kit with example content into one contact sheet, `gallery.png`;
open it before planning figures, and copy a call from `gallery.py` to start a new one.

## 1. Choose the visual by the job it does

Plan figures with the text: each one shows something the prose alone carries poorly, is introduced in the sentence
before it, and is named in that sentence by its number. The job decides the form:

| The reader should see… | Visual | Module |
| :---- | :---- | :---- |
| how parts of a system connect | C4 context, container or component diagram | `c4kit.Canvas` |
| layers of an architecture and what each holds | layers | `diagrams.layers` |
| who calls whom, in what order | sequence diagram | `diagrams.sequence` |
| the steps of a method or procedure | process | `diagrams.process` |
| a flow with entry points above it and outcomes below it | branches | `diagrams.branches` |
| a loop with a back edge and an exit | loop flow | `diagrams.loop_flow` |
| a chain of yes/no questions | decision ladder | `diagrams.decision_ladder` |
| a classification (root, groups, members) | tree | `diagrams.tree` |
| a loop that repeats until a test passes | cycle | `diagrams.cycle` |
| the states of an object and what moves it between them | state machine | `diagrams.state_machine` |
| what happened when | timeline (evenly spaced cards), era timeline (a true time scale with eras), lane timeline (one lane per actor) | `diagrams.timeline`, `era_timeline`, `lane_timeline` |
| spans over time per lane (waiting, holding, outcome) | Gantt lanes | `diagrams.gantt` |
| tokens, ids or values in a row, with spans and windows | token strip | `diagrams.token_strip` |
| every item against every other | pair matrix with totals | `diagrams.pair_matrix` |
| small counts at a glance | unit rows (one square per unit) | `diagrams.unit_rows` |
| items by two ordered scales (likelihood × impact) | risk matrix | `diagrams.risk_matrix` |
| verdicts or findings with their strength | stripe cards | `diagrams.stripe_cards` |
| which methods have which properties | matrix with check, cross and warning marks | `diagrams.matrix` |
| the change a proposal makes | two contrasting panels | `diagrams.compare` |
| where things are on a screen or a photo | screenshot with numbered markers | `diagrams.screenshot` |
| magnitudes across categories | bars (vertical; horizontal for long names), dots for many categories or small gaps | `charts.bars`, `charts.dots` |
| parts of a whole | 100 % stacked bars | `charts.stacked` |
| change over an ordered x | lines with end labels; slope for before and after | `charts.lines`, `charts.slope` |
| the relation of two measures | scatter (up to three groups) | `charts.scatter` |
| a matrix of numbers | heatmap | `charts.heatmap` |
| overlap of two or three sets | Venn diagram | `charts.venn` |
| a distribution | histogram | `charts.hist` |
| one headline number | no chart: a sentence, or a stat tile on a slide (`slidekit.bignum`) | |

A table stays a table when the reader looks up values; a figure earns its place when the shape of the data, an
order or a structure is the point. A source figure from a cited paper may be reused with credit in its caption.

## 2. The modules

| Module | What it gives |
| :---- | :---- |
| `palette.py` | every colour: `SERIES` (six hues in a fixed, validated order), `OTHER`, `STATUS` (good, warning, critical), text and structure (`INK`, `MUTED`, `GRID`, `LINE`, `SOFT`, `NAVY`, `CONNECTOR`), diagram `ROLES` and `LIGHT` tones, `sequential(n)`, `diverging(n)`, `tint`, `shade`, `blend`, `text_on(fill)` |
| `c4kit.py` | `Canvas(w, h)` in inches from the top-left: `box` (with `icon=`), `person`, `database`, `boundary`, `lane`, `band`, `uml_class`, `note`, `arrow`, `legend`, `icon`, `trim()`, `save()` |
| `scene.py` | one drawing, two outputs: rectangles, ellipses, polygons, lines and curves with arrowheads, measured text, badges, icons and images, rendered by `save()` as an image or by `to_slide()` as one group of native PowerPoint shapes |
| `diagrams.py` | the ready-made diagram types of section 1, each sized from its measured text and returned as a Scene; `medium="slide"` switches to slide type sizes |
| `native_charts.py` | editable PowerPoint charts (bars, stacked, lines, scatter, doughnut) in the kit's style, labels in the build language |
| `charts.py` | `figure(w, h, lang=)` and `axes(fig)`, the chart forms of section 1, `legend`, `callout`, `ticks`, `num` (numbers in the language's style), `fit`, `save` |
| `icons.py` | 46 pictograms drawn in code (`ICONS`): `draw_icon(fig, name, left, top, size, color, bg)`, `icon_png(...)`; `python icons.py OUT.png` draws them all |
| `figqa.py` | the layout check (section 5) |
| `gallery.py` | every visual with example content, checked |

A figure package in the project (`figures/taskN/__init__.py` with `FIGURES = {output name: builder}`) holds one
builder per figure; a builder takes the output path and, when it draws text, `lang`, so `render_figures.py` writes
`<name>.png` and `<name>.<code>.png` for each target language:

```python
import charts as ch
import diagrams as dg

T = {"vi": {"No cleaning": "Không làm sạch", "Method": "Phương pháp"}}

def results(out, lang="en"):
    t = lambda s: T.get(lang, {}).get(s, s)
    fig, ax = ch.figure(6.3, 2.8, lang=lang)
    ch.bars(ax, ["Model A", "Model B"], {t("Baseline"): [0.28, 0.30], t("Method"): [0.52, 0.63]},
            ref=0.22, ref_label=t("No cleaning"))
    ch.save(fig, out)

def flow(out, lang="en"):
    dg.process([("Profile", "Inspect the input", "search"), ("Plan", "Choose one step", "agent")]).save(out)
```

## 3. Design rules

- **Size for the page.** Draw a report figure at the width it prints: 6.3 in on a portrait page; a figure that is
  much wider than tall goes on a landscape page (up to 9.7 in) when that prints it at least 8 % larger. Text sizes
  are then printed sizes: names 9.5 pt bold, text 8 pt, small labels 7.5 pt, never below 6 pt. A canvas twice the
  page width halves every label, which the layout check reports.
- **Colour does one job.** Series take `SERIES` in order (slot 1 the baseline or the system, slot 2 the method under
  study), never cycled; a seventh series folds into "Other". Magnitude takes one hue from light to dark
  (`sequential`), a signed value two hues around grey (`diverging`). State colours mean state only and always come
  with an icon whose shape carries the meaning (check, warning, cross) and a word. Text stays in `INK` or `MUTED`,
  never in a series colour.
- **Label directly.** Values sit on or beside their marks, lines are named at their ends, so the reader needs no
  legend lookup or gridline; a legend appears for two or more series in bars, dots and stacks, and none for one.
- **One value axis.** Two measures of different scale make two charts, never a second y-axis.
- **Recessive structure.** No frames, light baselines and grids, no tick marks; marks are thin with rounded data
  ends and a white gap between neighbours; labels that sit on a line get a white plate.
- **Icons beside words.** An icon makes an element quick to find and the page inviting; the word next to it carries
  the meaning. Use one icon per element, from the same set, in the element's colour (white on a solid fill).
- **Words in the build language.** Every label goes through the builder's language table; numbers go through
  `charts.num` (0.75 and 1,250 in English; 0,75 and 1.250 in Vietnamese).
- **Honest scales.** Bars start at zero; a dot plot or line may zoom, and says so through its axis.

## 4. On slides

`slidekit.chart(s, name, x, y, w, h, draw)` renders `draw(fig)` at the slide's type sizes and language; inside it,
`ax = charts.axes(fig)` and the same chart calls as in a report, and the plot area is fitted to its labels.
`slidekit.icon(s, name, x, y, size, color, bg)` places an icon; `slidekit` colours (`BLUE`, `WARM`, `TEAL`, `PLUS`,
`MINUS`, …) come from the same palette, so a slide and its report figure match. A diagram drawn with `diagrams` can
go on a slide as a picture, but native slide shapes (`node`, `flow_row`, `path`) stay preferable for text a
translator must see (slides.md section 3).

## 5. The layout check

`figqa.check(fig)` runs on every figure that `c4kit.Canvas.save`, `charts.save` or `render_figures.py` writes, and
prints one `WARN` line per finding; the build's figure step counts them. It reports labels that overlap, labels cut
off at the edge, labels without a plate lying across a line, text running past the box it sits in, text printing
below 6 pt (taking into account how much the figure shrinks to fit the page) and empty margins wider than 18 % of the
figure. Fix each finding in the builder: widen the box, move or wrap the label, enlarge the text or narrow the
canvas, or `Canvas.trim()` the empty space; then render again. The layout check sees geometry, not meaning, so
after it passes, look at every figure at full size before the build.

## 6. Image or native: two outputs of one drawing

Every diagram type returns a Scene, which renders two ways:

```python
sc = dg.loop_flow(steps, back=(2, 0, T("retry")), medium="slide", width=8.0)
sc.to_slide(slide, x=0.3, y=1.5, name="retry loop")    # native shapes, one group
sc = dg.loop_flow(steps, back=(2, 0, "retry"))         # report sizes
sc.save(out)                                           # PNG (or .svg by the file name), checked
```

On a slide, prefer native shapes: the text is real slide text, so `check_slides.py` and the translators see it, the
presenter can edit a label in PowerPoint, and the diagram moves and scales as one group (ungroup to edit a part).
`to_slide()` runs the layout check on the diagram's image twin, so a native diagram is checked like a figure. Choose
an image on a slide when the visual is a chart form PowerPoint lacks (heatmap, Venn, slope, dot plot) or must look the
same in every viewer.

Charts on a slide come two ways as well. `slidekit.chart()` with `charts.py` gives an image at 400 dpi that looks the
same everywhere; `native_charts.py` gives an editable PowerPoint chart whose data the presenter can change
(right-click, Edit Data), styled the same way, with value labels written by the kit in the build language. Native
charts render with PowerPoint's engine, which some quick-look viewers draw softer; use them for figures a presenter
may update, images where the exact look matters most.

## 7. In the Word report

Word documents receive figures as pictures: pandoc places each PNG with its caption, and the builder sizes it to the
page. Word's own drawing objects (shapes, text boxes, Word charts with an embedded workbook) have no support in the
libraries the build uses; writing their XML by hand would be fragile to lay out, and Google Docs converts them
poorly. The kit therefore keeps the figure as one drawing and offers a vector option instead:

- `[taskN.layout] vector_figures = true` makes `render_figures.py` write an SVG twin of each figure (text kept as
  text) and the Word build attach it the way Word itself stores an SVG picture, with the PNG as fallback. Word 2016
  and later draw the vector version, sharp at any zoom, with selectable text; Word 365 can turn it into editable
  shapes (right-click, Convert to Shape); readers without SVG support show the PNG. The Google Docs copy always
  keeps PNG only.
- For an editable chart inside Word, the practical route is the same data in a native PowerPoint chart
  (`native_charts.py`) pasted into Word by the author; the report itself keeps the reproducible image.
