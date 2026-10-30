# Troubleshooting layouts the scripts don't fully handle

Read the section matching what verify.py or the visual review showed.

## Contents
- Re-extracting exact lines from the PDF
- Nested lists
- Borderless tables
- Multi-column pages ("moved" hunks)
- Images inside table cells
- Vector charts / diagrams (WARN vector drawings)
- Wrong heading levels
- Footnotes, superscripts, links
- Forms and checkboxes
- Scanned or partly scanned PDFs
- Text that differs only in Unicode form

## Re-extracting exact lines from the PDF
When you need exact text, font and position (to rebuild a table, a list, a
code block or a whole page), use the helper instead of retyping:
```bash
uv run <skill-dir>/scripts/dump_page.py doc.pdf --pages 4 [--clip x0,y0,x1,y1]   # line table
uv run <skill-dir>/scripts/dump_page.py doc.pdf --pages 4 --draft                  # Markdown draft
```
Line table columns: y, x, size, style (B bold, I italic, M monospace), region
(body / table#N rRcC / box / code / running), text. Equal x = same indent
level; links and images are listed after the lines.

## Nested lists
Lists come out flat because the converter's indentation is unreliable. Where
the page shows nesting (a sub-bullet further right, often a different glyph
such as ◦ or ▪), indent the child items by 3 spaces per level under their
parent. Use `dump_page.py` to read the x positions. Text and order stay
unchanged.

## Borderless tables
Tables aligned with whitespace (no ruling lines) are not detected; their cells
come out as consecutive lines or one run-on paragraph. `verify.py` still passes
because the words are all there, so this is caught only in visual review.
Rebuild the table in Markdown from the rendered page, keeping cell text exactly
as extracted. Re-run verify: cell order must still match the PDF's reading
order (row by row, left to right) or you will see "moved" hunks.

## Multi-column pages
The converter reads columns one after the other, which is right, but headings
that sit side by side on the same line (one per column) are merged into one
heading ("## Method Observations"). Split them and put each heading above its
own column's text. verify.py notes this as "same text in a different order";
that is expected. If the Markdown interleaves the columns line by line instead,
verify reports "moved" hunks; reorder to the visual reading order (left column
fully, then right). Sidebars go where the page's reading flow puts them,
usually after the main column of that page, as a blockquote.

## Images inside table cells
Images inside a table/box are not extracted (verify shows fewer md images than
PDF images, with the page number). Render the cell region and add the image:
```bash
uv run --with pymupdf python -c "import pymupdf;d=pymupdf.open('doc.pdf');p=d[PAGE-1];p.get_pixmap(clip=pymupdf.Rect(x0,y0,x1,y1),dpi=200).save('doc_assets/doc-pPAGE-cell.png')"
```
then put `![](doc_assets/doc-pPAGE-cell.png)` in the cell.

## Vector charts / diagrams
`WARN vector drawings` lists regions (page, bbox in points) drawn with paths.
Look at the render: decoration (background panels, rules) needs nothing. A real
chart/diagram has lost everything but its text labels — render the bbox as
above (pad by ~5pt), insert the image where the chart sits, and move the chart's
label text out of the body (it is part of the figure). Verify will then report
those labels as missing; that is expected — state it in your report.

## Wrong heading levels
Heading levels come from bold font sizes (convert.py prints `heading_sizes`).
If the document uses the same size for different levels, or colour/numbering
instead of size, fix levels by hand from the visual hierarchy. Keep heading
text exact; only the number of `#` changes.

## Footnotes, superscripts, links
Footnote markers may come out as plain digits glued to words (`word1`). Use
`word[^1]` and put `[^1]: text` where the footnote text appears. Hyperlinks are
kept as `[text](url)`; underline used only to style a link is dropped.

## Forms and checkboxes
Checkbox glyphs at the start of a line become Markdown task items (`- [ ]`, `- [x]`); a ✓ inside running text stays as text. Fillable form fields' *values*
are not page text; if the user needs them, read them with PyMuPDF
`page.widgets()` and add them explicitly, telling the user they came from form
fields.

## Scanned or partly scanned PDFs
`convert.py` refuses PDFs with no text at all. A page that is only an image
inside an otherwise digital PDF shows up as an image link with little or no
text around it; tell the user the page needs OCR rather than retyping it.

## Text that differs only in Unicode form
Both sides are NFC-normalised and Word's private-use bullet glyphs are mapped
to •. If verify still shows a hunk that looks identical, it is a different code
point (e.g. `-` vs `–`, `'` vs `’`): the Markdown must use the PDF's character.
