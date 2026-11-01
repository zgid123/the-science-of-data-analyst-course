# Design notes for report.html

Working record of the page design, following the `frontend-design` skill (plan, review against the brief,
build, critique). Chart colours are outside this plan: they follow the dataviz palette validated in
`logs/08_palette_check.log`.

## Brief

- **Subject:** a descriptive exploration of OULAD, the Open University's distance-learning dataset (7 modules,
  22 presentations, click logs, assessments, outcomes).
- **Audience:** team N04 during the deep dive (chosen 1 November 2026), as a working document rather than a
  submission.
- **Primary job:** find a finding, an issue or a method quickly, see its size, and reach the evidence file in one
  click.

## Diagnosis of the first version

The first page was a Markdown render with default chrome, and it shows four of the skill's generic tells:

1. Every chart sits in an identical rounded card (radius 10, same faint border), the "SaaS card kit".
2. Near-black `#0b0b0b` stands in for a chosen ink colour.
3. The header is a meta string joined with middle dots (`A · B · C`).
4. No navigation on a 170 KB page: a teammate looking for issue 7 or Section 5.6 has to scroll.

## Plan

**Colour** (UI only):

| Token | Hex | Role |
|---|---|---|
| paper | `#ffffff` | reading surface, chart background |
| rail | `#f3f5f8` | navigation rail, table headers |
| ink | `#1d2433` | text, high-severity badge |
| ink-2 | `#5b6475` | secondary text, captions |
| rule | `#dfe3ea` | hairlines, grid |
| marker | `#1d6b47` | links, current section, ticked methods |

**Type:** Charter (fallbacks: Bitstream Charter, Sitka Text, Cambria) for headings and figure titles, giving the
page the tone of an academic working paper; Avenir Next (fallbacks: Segoe UI, Helvetica Neue) for body text and
tables, with tabular figures. System fonts only, so the file stays offline and small.

**Layout:**

```text
+--------------+--------------------------------------------+
| rail         | title, dataset facts as a key/value list   |
|  contents    | status and summary                         |
|   1 ... 9    | Findings at a glance (table, linked)       |
|   5.1 ...    | 1. Dataset map ... (prose <= 72 characters,|
|  data issues |    tables and figures up to 980 px)        |
|   1 high ... | Figure 1 ... Figure 12                     |
|  files       | appendices                                 |
+--------------+--------------------------------------------+
```

Left-aligned throughout. On narrow screens the rail moves above the content and its contents list folds.

**Principles:**

1. Navigation is the feature: a sticky rail with every section, the nine data issues with their severity, and the
   evidence folders; the current section is marked as you scroll.
2. Evidence is one click away: every `results/`, `code/`, `evidence/` and `logs/` path becomes a link to the file,
   and every "Section 5.2" becomes a link to that section.
3. Severity is shown by shape as well as words: High is a solid ink badge, Medium an outlined badge, Low plain
   text; no hue carries status alone, and red stays reserved for the Withdrawn outcome in the charts.
4. Figures are numbered (Figure 1–12) because the team refers to them in discussion; no cards, only a hairline
   above each figure.

## Review against the brief and the skill's defaults

- A violet or indigo accent was the first idea for links; it is the default SaaS accent, so the accent became a
  marker green, the colour of a reviewer's annotation, which also stays clear of the outcome reds and blues.
- Serif headings over a sans body is common, but the skill's tell is the cream background with a high-contrast
  serif and a terracotta accent; Charter is a low-contrast book face on white, which suits a working paper.
- A documentation-style rail is a familiar layout; it stays because the primary job is navigation, and the boldness
  is spent on the data-issue list inside it, which is specific to this report.
- Removed: the middle-dot meta line (now a key/value list in `REPORT.md`), card chrome, near-black `#0b0b0b`.
- Motion: only in answer to an action (smooth scroll after a navigation click, the current-section marker), and
  none when the reader prefers reduced motion.

## Critique log

Renders and fixes after building are recorded in `logs/09_render_check.log`.

First build, four slices rendered (top, Section 3, Section 5.1, Section 8):

1. The rail's issue list showed two numbers ("1. 1"): the list style targeted `.issues ol` while the class sits on
   the `<ol>`; fixed with `ol.issues`.
2. "Section 2" links wrapped onto two lines in the findings table; in-page links now stay on one line.
3. Issue names in the Section 3 table wrapped word by word; the issue and severity columns have minimum widths.
4. Disabled checkboxes rendered too faint to tell done from open; replaced by a marker-green tick and a grey
   open circle, each with an accessible label.
5. Confidence intervals broke at the en dash; "35.2% (33.6–36.8)" now stays on one line.
6. Regression from fix 2: rail links stopped wrapping and were clipped; the rail is exempted.

Change requested by the team (1 November 2026): prose now fills the content column (about 960 px, 110–120
characters per line) instead of stopping at 72 characters, so paragraphs share one right edge with tables and
figures. This trades the skill's line-length guidance for an even page on wide screens.

Not checked: the narrow-screen layout (the renderer has a fixed width) and hover in a live browser.
