---
name: pdf2md
description: Convert a PDF into a faithful, as-is Markdown copy (every word, ruled tables including empty template rows and tables split across pages, headings, lists, callout boxes, code blocks, links, images) and prove the copy matches the PDF with a deterministic verifier plus a page-by-page visual check. Use this whenever the user wants a PDF turned into .md, a Markdown/plain-text version of a PDF (assignment briefs, milestone/requirement docs, reports, guidelines, forms), PDF content made readable for LLMs, git or diffs, or wants to check that an existing Markdown file matches its PDF — even if they only say "make an md of this pdf" or "extract this PDF".
compatibility: Needs `uv` (scripts declare their own Python deps inline - PyMuPDF, pymupdf4llm 1.x, diff-match-patch). Text-based PDFs only; scanned PDFs need OCR first.
---

# pdf2md — PDF → Markdown, as-is

The goal is a Markdown file a reader can trust *instead of* the PDF: same words,
same order, same structure, nothing added, nothing summarised. Scripts do
everything mechanical and measurable; your job is the part that needs eyes —
comparing rendered pages with the Markdown and fixing what the scripts cannot
judge.

The scripts are in the `scripts/` folder next to this file. Call them by
absolute path from any working directory, e.g.
`uv run <skill-dir>/scripts/convert.py doc.pdf`. The first run downloads the
dependencies; later runs are instant.

## Workflow

### 1. Convert

```bash
uv run <skill-dir>/scripts/convert.py path/to/doc.pdf           # -> path/to/doc.md (+ doc_assets/ if images)
uv run <skill-dir>/scripts/convert.py doc.pdf -o out/doc.md     # custom output; images go to out/doc_assets/
```

It prints what it found: pages, tables, boxes, code blocks, images, removed
and kept running lines, body font size, heading sizes. Exit code 2 means a
placeholder got lost — the verifier will show where.

If it says *no extractable text*, the PDF is scanned. Stop and tell the user it
needs OCR (e.g. `ocrmypdf in.pdf out.pdf`) before conversion; do not transcribe
pages by hand from images unless they explicitly ask for that.

### 2. Verify

```bash
uv run <skill-dir>/scripts/verify.py doc.pdf doc.md [--json report.json]
```

| Check | What it proves |
|---|---|
| `text` | Every letter/digit/symbol of the PDF appears in the same order, nothing extra (whitespace and Markdown punctuation ignored). Hunks show page and context, the difference in `⟦…⟧`; "moved" = same text, different order. |
| `tables` | Each ruled table has a Markdown table with the same header and shape, and **every cell** holds the PDF words inside that cell (catches shifted or merged cells). |
| `code` | Monospace blocks appear line by line with their indentation inside ``` fences. |
| `headings` | Every bold line at a heading font size is a Markdown heading. |
| `links` | Every PDF hyperlink URL is linked in the Markdown at least as often as in the PDF. |
| `images` | Raster image count matches and every linked file exists. |
| `structure` | Fences balanced, no heading inside a fence, nothing that renders as an accidental indented code block, checklists as task items. |
| `rendered` | The text a reader actually sees (Markdown parsed by a CommonMark renderer) equals the PDF text — catches literal characters Markdown silently turns into syntax, e.g. "1)" inside a bullet becoming a numbered list. |
| `formatting` | Bold and italic in the rendered Markdown equal the PDF's bold and italic text, in both directions (headings count as bold). |
| `rules` | Free-standing horizontal lines in the PDF appear as `---`. |
| `artefacts` | No leftover placeholders, `<mark>`, `~~`, `<u>`, U+FFFD. |
| `WARN vector drawings` | (warning) sizeable drawings outside tables — maybe a chart that only kept its labels. |

It also prints real examples of the removed running lines and the constant
ones that were kept once — confirm nothing meaningful was dropped.

### 3. Visual review — always, even when verify passes

**A verify PASS does not mean the structure is right.** The verifier proves
words, table cells, code, links and headings. It cannot see
whether paragraphs are split where the page splits them, whether a list is
nested, or whether a whitespace-aligned table was flattened. Render the pages:

```bash
uv run <skill-dir>/scripts/render_pages.py doc.pdf --out <scratch-dir>/pages
```

For each page it prints what is on it (tables, boxes, code, images, links) and
the first/last words outside tables; search the Markdown for those words and
read the PNG and that Markdown section side by side. **Review every page** for
documents up to ~30 pages. For longer ones, review every page with a verify
finding, a table, code, an image or a WARN, plus the first and last page and a
spread of the rest — and say which pages you reviewed.

Look for:
- **Paragraph boundaries** — two paragraphs joined, or one wrapped line split into two (common for centred lines, which Word stores as separate blocks).
- **Lists** — the scripts flatten lists (see conventions); restore nesting the page shows. Ordered vs bulleted, numbering continuity, checkboxes as `- [ ]` task items.
- **Tables without ruling lines** — come out as plain lines; rebuild them as tables.
- **Headings** — level matches the visual hierarchy.
- **Figures** — image placed where it is on the page, caption right after; WARN regions that are real charts need an image (see reference).
- **Inline emphasis** — bold/italic where the page shows it.

Known conventions (listed below) are not errors; do not "fix" them.

### 4. Fix in the Markdown, then re-verify

Edit the `.md` directly — do not change the scripts for one document. To keep
the copy *as-is*:
- Copy text exactly from the PDF; never paraphrase, translate, summarise, fix typos or "improve" wording. If the source has an error, the copy has it too.
- Restructure only to match the PDF's structure (join a split paragraph, nest a list, rebuild a flattened table); never drop text.
- Re-run `verify.py` after every round of edits. Finish only when it passes, or when each remaining difference is explained and justified.

`references/troubleshooting.md` covers the rarer layouts (borderless tables,
multi-column pages, images in cells, vector charts, footnotes, forms,
re-extracting exact lines from the PDF).

### When the scripts can't handle it — you take over

The scripts are the default, not the limit. When they fail or produce
something wrong, do the work yourself — but with the same rules: the PDF is
the only source of text, and `verify.py` plus your visual review stay the
acceptance gate. Escalate only as far as needed:

| Situation | What you do |
|---|---|
| A few spots wrong (verify finding or review) | Edit those lines in the `.md` (step 4). |
| A region has the wrong structure — a borderless table flattened to lines, side-by-side column headings merged into one, a nested list flattened, a sidebar, a form | Rebuild that region from the line table: `uv run <skill-dir>/scripts/dump_page.py doc.pdf --pages N [--clip x0,y0,x1,y1]` prints every line with x/y, size, style and region; equal x = same column or indent level. Assemble the region from those lines and replace it in the `.md`. Several regions may be fixed in one edit; keep the converter's text everywhere else. Re-verify. |
| `convert.py` crashes, exits 2, or the output is broadly unusable | Read the error first. Environment problems (uv, network, dependency resolution) — fix the environment, never the PDF. Otherwise build the document from `dump_page.py --draft` (all pages): a Markdown draft built without pymupdf4llm. It shares the converter's layout analysis, so it has the same blind spots (only ruled tables, flat lists, same-line headings) — fix those as in the row above. Merge tables that continue across pages, place images (see troubleshooting), then run the normal review + verify loop. |
| `verify.py` reports something the page shows is right (a false positive) | Confirm with the render and `dump_page.py`. Do **not** bend the Markdown to satisfy a wrong check. Leave it, and report the check name, the page and your evidence as a justified exception. |
| `verify.py` itself crashes | Report it; meanwhile compare with `dump_page.py` output page by page and say the automated gate did not run. Never call such a file verified. |
| The PDF is scanned or the text layer is garbage (U+FFFD, wrong glyphs) | Stop and ask; OCR is a separate decision. Do not transcribe from images unless the user asks. |

What verify does with hand-built structure:
- A Markdown table with no *ruled* table in the PDF (a rebuilt borderless table) passes `tables` with a note; its words are still checked by `text` and `rendered`, so they must be the PDF's words in reading order (row by row).
- Text that is correct but in a different order than the verifier's top-to-bottom reading (e.g. a column heading placed above its own column) is reported as a "same text in a different order" note, not a failure.

Rules while hand-building:
- Take text from `dump_page.py`, copy-pasted — never retype from an image or from memory, and never "tidy" it.
- Keep the conventions below (task lists, blockquote boxes, `---`, escaping) so the output looks the same as script output and the verifier reads it the same way.
- Mark nothing as done until verify passes or every remaining FAIL is a reported, evidenced exception.

**One document vs. the skill.** Fix a one-off in the Markdown. If the same
failure would hit other PDFs (a layout class the scripts get wrong, a verifier
false positive), say so in the report and propose the script change; change
the scripts only when the user agrees, add the case to `evals/`, and re-run
the evals, so the next conversion needs less manual work.

### 5. Report

Per file: output path, the verify summary lines, pages reviewed, every manual
fix (page, what, why), any takeover (which region or document, which tool you
used), justified verify exceptions with evidence, and anything left unresolved.

## Conventions the scripts apply (what "as-is" means here)

These are deliberate; mention them when the user might expect otherwise.
- **Running headers/footers**: lines repeated in the top/bottom margin on at least half the pages are removed from the flow. Those whose text never changes (course code, document title) are **kept once** — headers at the top of the file, footers at the end; varying ones (page numbers) are dropped.
- **Tables split across a page break become one table**; the repeated header row is dropped. **Empty rows are kept** — fill-in templates are content.
- **Single-cell bordered boxes become blockquotes** (`> **Title**` / `>` / `> body`).
- **Monospace blocks become ``` fences** with indentation rebuilt from the page.
- **Lists are tight and flat** (`- item`); checkbox lines (☐ □ ▢ / ☑ ☒) become native Markdown task items `- [ ] item` / `- [x] item` (the verifier maps them back to the glyph for the text check and fails on leftover glyph lists). The white squares □ ▢ count as empty checkboxes only at the start of a line, where pymupdf4llm reads them as bullets; inside a table cell they stay literal, and the verifier compares □ ▢ ☐ as one glyph.
- **Soft line wraps are joined** using the PDF's own paragraph starts; words broken mid-line in narrow cells are rejoined; real compound hyphens (`event-level`) are kept.
- **Horizontal rules** (free-standing lines at least half the page wide, not table borders or underlines) become `---`, placed after the text line above them.
- **Literal markers are escaped**: text that starts with something Markdown would parse as syntax (`1)`, `2.`, `-`, `#`, `>` at the start of a list item) is written as `1\)` etc., so it renders exactly as printed.
- **Not represented** (no native Markdown): text colour, font size, background shading of boxes, cell shading, centred alignment of paragraphs. Table column alignment is not emitted either; check centred/right-aligned columns in review and add `:---:` / `---:` if needed.
- **Links** keep their URL and only the text that is linked in the PDF; underline used as link styling is dropped.
- **Images are saved byte-for-byte** to `<name>_assets/` with an empty alt text (the PDF has none).
- **Heading levels come from font size**: largest bold size `#`, then `##`, `###`…; a heading wrapped over two lines is one heading. Bold sizes used only on the cover page (a kicker such as "MILESTONE P1" above the title) stay bold text.

## How the scripts work (for debugging)

- `pdf_layout.py` — shared analysis: running lines, ruled-grid detection from vector cell borders (shaded cells, missing outer borders, empty rows), span-level cell text with bold/italic and links, page-break continuations, monospace blocks, paragraph starts, heading levels.
- `convert.py` — replaces running lines, grids, code blocks and images with tokens in an in-memory copy of the PDF, runs pymupdf4llm (classic rule-based path) for the text flow, swaps tokens for Markdown, then normalises.
- `verify.py` — compares raw PDF text, raw words per table cell, links, code lines and heading lines with the Markdown.
- `render_pages.py` — page PNGs and per-page review hints.
- `dump_page.py` — exact lines with region labels, or a pymupdf4llm-free Markdown draft (`--draft`), for takeover work.
