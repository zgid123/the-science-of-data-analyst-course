# build-report reference

## 1. Source conventions

The checks enforce these conventions; following them while writing keeps every check green.

### 1.1. Files and headings

| Element | Convention |
| :---- | :---- |
| Section file | `NN-SS-slug.md` (or `NN-SS-S-slug.md`); lexical order is document order. One heading per file is usual. |
| Language twin | Same name with the pack suffix, for example `.vi.md`; every language has the same files. |
| Front matter | `00-0-title-page`, `00-1-abbreviations`, `00-2-glossary` (or terms). Everything before the first H1 is the title page: institution lines, logo image, course, the title in capitals, a two-column table of names, place and date. |
| Parts | H1 `# N. Title`, numbered 1, 2, 3 … in order. Each part starts a new page. |
| Sections | H2 `## N.M. Title`, H3 `### N.M.K. Title`, H4 at depth 4; the number continues the parent and the previous sibling (1.2 → 1.3, 1.2 → 1.2.1). |
| Back matter | Unnumbered H1 after the parts: the reference list (`# References`) and `# Appendices`, whose H2s are `## Appendix I – Title`, `## Appendix II – …`, with H3s numbered `### 1.` again in each appendix. |

### 1.2. Figures, tables and cross-references

| Element | Convention |
| :---- | :---- |
| Figure | A paragraph of its own: `![Figure P.n. Caption](assets/figures/x.png){width=100%}` with blank lines around it, so pandoc makes it a captioned figure. |
| Table | A bold caption line `**Table P.n. Caption**`, a blank line, then a pipe table with a separator row `\| :---- \|`; every row has the header's cell count. |
| Numbering | P is the part number (appendices use `A`, numbered continuously across all appendices); n restarts at 1 in each part, separately for figures and tables. |
| Cross-reference | `Section 3.5.3`, `Figure 2.1`, `Table A.4`, `Part 2`, `Appendix I`, and lists such as `Sections 4.2.1 to 4.2.4`. Every figure and table is referred to in the text at least once, usually in the paragraph that introduces it. |
| Footnote | `[^label]` in the text and `[^label]: text` once, in the same report. |

### 1.3. Citations, abbreviations and house style

| Element | Convention |
| :---- | :---- |
| Citation | `[n]`, `[n], [m]` or `[n–m]`; numbers 1 … N, all listed in the reference file, each entry cited at least once. With `order = "first-citation"`, [1] is the first source cited, then [2], and so on. |
| Reference list | A file whose H1 is the pack's references heading; entries are paragraphs starting `[n] ` in APA 7. |
| Abbreviation | Listed in `00-1-abbreviations` (columns: abbreviation, full form, role). Defined at its first body use as "full form (ABBR)", then written as the abbreviation alone. Headings, quotations ("…" of 8 characters or more), code, front matter and the reference list are exempt. |
| House style | En dash "–" for ranges, pairs and asides; ordered lists `(1)`, `(2)`; display math in `$$…$$`, inline math in `$…$`. The build also enforces the dash and list rules through `report_format.lua`. |

## 2. `tasks.toml`

The project's task settings. `templates/tasks.toml` is the complete annotated version (every field marked required or optional, with its default), and `report.py init TASK --title "…"` installs it with a starter report. The summary:

```toml
[project]
tests = ["test_x.py"]                    # run by `report.py test` after the skill self-test

[taskN]
name = "Readable name"
report = "taskN/report"                  # section folder
build = "build/taskN"                    # output folder
author = "Group 4"                       # default author for every language
google_docs = true                       # optional: also build an all-portrait <out>_GoogleDocs.docx
people = ["Phạm Thị Bạch Huệ"]           # optional: names that must appear exactly (lecturers, authors), without titles;
people_files = ["slides_taskN_vi.py"]    #   check_names.py also reads the report, hooks.extras and these files

[taskN.en]                               # one table per language pack code (en, vi, …)
out = "Report_EN.docx"
title = "Full Title"                     # core property
short_title = "Short Title"              # running header
subject = "Course or field"              # core property
author = "…"                             # optional override
glossaries = ["domain", "topic"]         # target languages: + common/*, from languages/<code>/glossaries/
figure_lang = "en"                       # optional: figures from <name>.<code>.png; "en" (the source) keeps the original figures; default: the build language

[taskN.layout]
compact = true                           # optional: a short document (a proposal): no page breaks before parts,
                                         # no contents or lists of figures and tables, arabic numbering from the
                                         # page after the title page; front pages (00-*) flow into the body
body_size = 11                           # optional: body font size in pt and line spacing of running text,
line_spacing = 1.15                      # overriding the language pack's [docx] values (a page budget)

[taskN.figures]
package = "figures.taskN"                # FIGURES in figures/taskN/__init__.py; rendered before the documents
                                         # (skipped with --no-figures)

[taskN.hooks]
extras = ["build_slides_taskN.py"]       # after the documents (a slide deck, slides.md)
checks = { name = "script.py --args" }   # extra prechecks, {report} and {task} are filled in
extra_checks = { name = "script.py …" }  # extra postchecks

[taskN.citations]
order = "first-citation"                 # or "any" (default)
unused = "error"                         # or "warn": listed but uncited references
draft_ids = "S\\d{3}"                    # optional: draft source IDs such as [S101], all finalized to [n] before delivery

[taskN.abbreviations]
names = ["FSFM", "OULU-NPU"]             # method, dataset and product names kept out of --candidates

[taskN.abbreviations.aliases.en]         # full forms for grouped rows such as "Q1, Q2, Q3"
Q1 = ["Question 1"]

[taskN.abbreviations.titles]             # official titles that contain a full form by name (not a repeat)
vi = ["Luật Phòng, chống rửa tiền"]

[taskN.structure]
ignore_refs = ["Part 10"]                # cross-references that name another document
```

Hook commands ending in `.py` run from the project root with the project's Python (SKILL.md, Requirements).

## 3. Language packs

Each language is a folder `languages/<code>/`. English is the source language; every other pack is a target language and carries a `[translation]` table. Another skill may also contribute a pack as `report-language-<code>.toml`.

| File | Content |
| :---- | :---- |
| `pack.toml` | Interface words, conventions as data, translation settings and Word layout (tables below) |
| `review.md` | Target languages: the native reviewer's protocol and checklist, used after translation (section 4.4) |
| `lessons.md` | Target languages: what human reviewers changed in earlier translations, with before/after examples and the rule each produced (section 4.7) |
| `guide.md` | How to write natively for this language's readers: voice, natural forms for English sentence patterns, slides and presenter notes, orthography, structure, numbers and dates, quotations, references, language-only pages, the self-review before marking a file translated (target languages) |
| `glossaries/` | Fixed terms in three layers: `common/` (every report), `domains/` and `topics/` (selected per task with `[taskN.<code>] glossaries = [...]`); rows `English \| Vietnamese \| Usage \| Replaces`; `glossary.py` shows, looks up and lints them (`glossaries/README.md`) |
| `templates/` | Pages only this language's reports carry (for Vietnamese: `00-0a-loi-cam-on.vi.md`, `00-0b-loi-cam-doan.vi.md`) |

| `pack.toml` key | Purpose | English | Vietnamese |
| :---- | :---- | :---- | :---- |
| `code`, `name`, `locale`, `suffix` | Pack code, display name, Word language tag, file suffix | en, English, en-GB, `.md` | vi, Tiếng Việt, vi-VN, `.vi.md` |
| `contents`, `lof`, `lot`, `hint` | Front-matter headings and the hint shown before Word fills the fields | Contents, List of Figures, List of Tables | Mục lục, Danh mục hình, Danh mục bảng |
| `figure`, `table`, `section`, `part`, `appendix` | Caption and cross-reference words, singular first | Figure/Figures, … | Hình, Bảng, Mục, Phần, Phụ lục |
| `connectors` | Words between numbers in reference lists | `, and `, ` and `, ` to `, ` or ` | ` và `, ` đến `, ` tới `, ` hoặc ` |
| `references`, `abbreviation_header` | H1 of the reference list; first header cell of the abbreviation table | References; Abbreviation | Tài liệu tham khảo; Từ viết tắt |
| `function_words` | Source language only: words whose density marks untranslated text | the, and, of, … | – |
| `[style.conclusion]` | `headings` (H1 words of a conclusion part), `phrases` (narration about the report: errors), `subject` (regex for a part or section leading a sentence: warnings) | Conclusion; "the report", "each part", … | Kết luận; "báo cáo này", "mỗi phần", … |
| `[style]` | `meta_phrases` (talk about the report, reader, outline or writing process, and planned runs or pending results: errors in `check_style.py`), `[[warn]]` patterns (warnings) | "this report will", "the reader", "planned run", …; en-GB spelling of ordinary words | "báo cáo này sẽ", "chúng tôi sẽ", … |
| `[translation]` | `source`, `guide`, `review`, `lessons`, `terms_page` (glob of the terms page, whose rows must open with the source term), `glossaries`, `extra_files` (globs of language-only pages), `extras` (their templates) | – | from en; `00-0a-*`, `00-0b-*` |
| `[conventions]` | `decimal` ("comma"), `reference_words` and `version_words` (numbers after them keep their dots), `check_untranslated`, `source_references` ("warn"/"error"), `glossary` (variant regex = preferred form), `[[warn]]` (pattern, message) | – | decimal comma, glossary variants, modern tone placement, grammar warnings (plural markers, 'của' chains, nominalisers, stacked passives, calques, spoken openers, sentence length) |
| `[docx]` | Word layout for this language: `body_size`, `line_spacing` | – | available; Vietnamese academic layout (13 pt, 1.3–1.5) on the user's request |

`lang_rules.py` applies `[conventions]`, together with the Replaces variants of the task's glossary layers, to the target-language sources (`check_parity.py`, errors), to the Word text (`check_docx.py`, warnings) and to slide decks (`check_slides.py`, errors). Quotations, inline code, math and snake_case identifiers are exempt everywhere.

## 4. Translation workflow

Every target language, every deliverable (report, deck, answers to questions) and every translator follows the same principles. Each one comes from what reviewers and the user corrected in earlier translations (the packs' `lessons.md`), so it carries its reason with it.

1. **Write for a reader who never sees the source.** That reader cannot recover a missing head noun, a dropped subject or a source-language image from the original, so every phrase names what it is about, every sentence has its subject and verb, and a figure of speech becomes the plain action it describes. Human reviewers' edits converge on this: fewer words, every phrase complete.
2. **One concept, one term, across files and deliverables.** A reader takes two names for two things. When the source varies its words for one thing (a "selector" that is also the "judge"), the translation keeps one term; a deck, a summary or a set of answers takes its terms from the reviewed report twins; the glossary records the decision, with the source's synonyms in one row. `glossary.py --task TASK coverage --report DIR` (or `--deck MODULE.py`) measures drift over a whole deliverable and lists each concept that travels under other names.
3. **Every sentence names who acts.** The writers or presenters, the authors of the work under review, the work itself, the method and the audience stay distinct; the pack fixes how each is named (for Vietnamese, guide section 3.2).
4. **Meaning first, then fit.** When fixed space (a slide box, a chart label, a table cell) cannot hold the faithful wording, the layout changes and the meaning stays.
5. **Fresh eyes, briefed with evidence.** A reviewer other than the translator reads every file; a review that answers a complaint starts from measured evidence (counts, a drift report, examples) rather than an impression, so its edits address the cause.
6. **Every correction becomes a rule where it acts.** A human review (section 4.7) or a user's remark on any deliverable is recorded in `lessons.md` with before and after examples, then turned into a guide rule, a checklist item, a glossary row, a check or a prompt template, and verified: a new check fires on the old text and stays quiet on the corrected one.

### 4.1. Status and sync

`translation_status.py --report DIR --lang CODE` lists every source file whose twin is `missing` or `stale`. A twin is in sync when the source's content hash recorded in `<report>/.<code>-sync.json` matches the current source, so only a real text change marks it stale. `--mark FILE …` records files after their parity check passes; `--mark-all` records every existing pair (for example after adopting a finished translation). Language-only pages are listed separately and stay out of sync and parity.

### 4.2. Translating a file

1. Read the source file in full; when the twin exists and is stale, read it too and change only what the source changed, so reviewed wording carries over.
2. Write the twin in the language's own voice (guide sections 1, 2 and 5: write as a native author, replace English sentence patterns with natural ones, then orthography), with the terms of the task's glossary layers (guide section 4; `glossary.py --lang CODE --task TASK show`). For a translated slide deck, also follow the guide's section on slides and presenter notes (section 3).
3. Keep the structure one-to-one: headings with the same numbers, tables with the same rows and columns, lists with the same items, figures with the same paths (caption translated), footnote labels, code, formulas, and `[n]` citations in the same order.
4. Front matter: the abbreviation list and the terms page keep one row per source row in the same order, in the pack's forms (Vietnamese: guide section 6, "English term – Vietnamese name" on the terms page, which `check_parity.py` checks through `terms_page`); the reference list translates only its heading and introduction.
5. Run `check_parity.py --report DIR --lang CODE FILE` until it reports 0 errors, review its warnings, then `translation_status.py … --mark FILE` (which records the file once its parity check passes).
6. Add any new recurring term to the right glossary layer (common, domain or topic; glossaries README), then run `glossary.py --lang CODE lint`.

### 4.3. Translating a whole report

A full translation runs in stages, so that terms are fixed before anyone translates and every file meets a reviewer other than its translator.

| Stage | Work | Runs |
| :---- | :---- | :---- |
| 1. Terms | Print the task's merged glossary; list the report's recurring terms that the layers leave open (`glossary.py --lang CODE --task TASK show` against the English text); settle each in the right layer, taking regulated concepts from the Vietnamese original of the legal text (guide section 4, rule 7); write the task's topic glossary for its own names (categories, components, zones); `glossary.py --lang CODE lint` | Once, before any file is translated |
| 2. Front matter | Translate the title page, the abbreviation list (one row per source row, Vietnamese full forms, official Vietnamese abbreviations where they exist) and the glossary page, so every translator copies the same full forms | Once |
| 3. Translation | Translate the body files in groups of whole sections (guide sections 1, 2, 4–8), each agent starting from `templates/prompts/report-translate.md`; each translator runs `check_parity.py` on its files and marks them with `translation_status.py --mark` | In parallel when the groups are disjoint, since stage 1 fixed the shared vocabulary |
| 4. Native review | A reviewer other than the group's translator reads every file in the three passes of `review.md` (prompt: `templates/prompts/report-review.md`), edits in place and logs the findings | In parallel, one reviewer per group, each group reviewed by a different agent from its translator |
| 5. Consistency | One reader goes through the whole Vietnamese report in order: term consistency across files, abbreviation first use in document order, file-to-file bridges, `glossary.py lint` | Once, after all reviews |
| 6. Build | `report.py all TASK`; compare the target document's figure and table counts with the source's | Once |

Groups follow the report's own sections, and each file belongs to exactly one translator and one reviewer, so parallel agents always edit separate files. Each agent keeps its temporary files in its own scratch subfolder named after its task, so helper scripts and notes stay apart too. A group that changes the glossary in stage 3 or 4 tells the main agent, which updates the glossary once and notes it for the remaining groups.

### 4.4. Native review

`languages/<code>/review.md` holds the reviewer's protocol: a reader pass on the target text alone, a fidelity pass side by side, and an editor pass through a checklist of sentences, coherence, terms, self-contained sections, fidelity and form. Edits go into the twin; findings go into the task's review log with the checklist item they answer. A file counts as translated once its review is logged and its parity check passes again.

### 4.5. A language's first build

Offer the user the pack's language-only pages (`report.py translate` lists them), add each chosen one with `report.py translate TASK --lang CODE --add-extra NAME`, and fill in its placeholders together; `check_docx.py` lists any placeholder still open. Ask whether the language's own layout (`[docx]`) is wanted. Then run `report.py all TASK` and compare the target document's figure and table counts with the source document's.

### 4.6. Slides and other deliverables

A translated slide deck follows the same guide and glossary; `check_slides.py DECK --lang CODE` applies the pack's conventions to slide text, tables and speaker notes (wire it as a `hooks.extra_checks` entry). Decks are built with `scripts/slidekit.py`; [slides.md](slides.md) holds their workflow, design rules and the translation and review steps for their strings.

### 4.7. Learning from a human review

A user's remark on any deliverable ("the Vietnamese notes are hard to follow") is evidence of the same kind: measure it (counts of terms, `glossary.py coverage`, examples), record it in `lessons.md`, and turn it into a rule as below. When a person reviews a translation, the edits are the best guide to natural writing in that language. `split_export.py` splits the reviewed single-file version (for example a Google Docs export) into the report's file layout in a separate folder, with a similarity index per file; `review_diff.py` prints every changed paragraph with a word diff. Run it on the body and on the front matter (`--files "00-*"`), whose pages have forms of their own. Read the pairs, set aside changes of content and typing slips, group the rest by kind, and record each kind with examples in the pack's `lessons.md`. Then turn each kind into a rule where it acts: the guide (writing), `review.md` (reviewing), a glossary row (terms) or a `[[conventions.warn]]` pattern (checks), keeping only patterns that fire on the translated text and stay quiet on the reviewed text.

A reviewer edits meaning as well as wording, so the review is also checked for truth before it is adopted:

1. **Drift.** Every changed paragraph that restates one of the report's claims is compared with the source sentence and with the evidence behind the claim: the cited source itself, or the project's evidence trail when the report keeps one. A changed number, hedge, scope, attribution, definition or causal relation is restored in the reviewer's own wording.
2. **New content.** Each statement the reviewer added is checked against the source it cites. A new source is read in full first and, when the report keeps an evidence trail, entered in it with the passage that supports the statement. A statement is then reworded to what the source supports, given a source, or removed.
3. **References.** New entries get full APA 7 form. `check_citations.py` reports entries that are no longer cited and citations out of first-citation order. `renumber_refs.py --write` (with `--drop-unused` when entries fell out and `--map` for the trail's record) numbers everything again, after which the checks run once more.

Corrections from these checks are written as `### Fix ID – file` blocks with `FIND:` and `REPLACE:` lines and applied with `apply_fixes.py`, which applies the changes only when every block matches exactly once; the blocks stay as the record of what changed and why.

To adopt the reviewed version as the report: keep the reviewed folder separate from the original (the original stays as the "before" side), copy the source-language files into it with their citations renumbered, bring them in line with the reviewed target language (removals, restructuring and verified additions; a meaning change in parts not yet audited is checked against the trail first), reach 0 parity errors, record the sync with `translation_status.py --mark-all`, and point the task's `report` in `tasks.toml` to the reviewed folder.

## 5. Pre-checks: what each reports and how to fix it

| Check | Message | Fix |
| :---- | :---- | :---- |
| format | em dash '—' | Replace with "–". |
| format | numbered list item '1.' | Write `(1)`, `(2)`. |
| format | heading / list / table without a blank line before it | Insert the blank line; without it pandoc merges the block into the paragraph above. |
| format | image not alone between blank lines | Put the image line in its own paragraph, so pandoc makes it a captioned figure. |
| format | table header without a separator row; row has n cells | Add `\| :---- \|` per column; escape a literal pipe as `\|`. |
| format | unclosed code fence / display formula | Close the ``` or `$$`. |
| structure | part heading should be numbered N; heading breaks the sequence; depth differs from level | Renumber the heading and its file name; check that the H-level matches the number depth. |
| structure | Figure/Table P.n is not in Part P; breaks the sequence | Renumber the caption and every reference to it. |
| structure | caption is not directly followed by a table | Keep caption, blank line, table together. |
| structure | 'Section x.y' refers to nothing | Correct the number; if it names another document's part, rephrase ("Part 10 of NIST IR 8491") or add it to `structure.ignore_refs`. |
| structure | image file does not exist; footnote has no definition / never referenced / defined twice | Fix the path or the footnote label. |
| structure | WARN figure or table never referred to | Refer to it in the introducing paragraph, or confirm with the user. |
| style | meta commentary '…' | State the information itself: the finding, the figure, the specification |
| style | conclusion narrates the report '…'; WARN conclusion sentence led by 'Part 1' | Rewrite as a conclusion about the subject (the field, its methods, its threats) with its evidence; cite sections as pointers "(Section 3.3)" |
| style | WARN US spelling | Write the en-GB form (-ise, -isation); names and quotations keep their own spelling |
| abbreviations | DEFINE: first use has no full form beside it | Write "full form (ABBR)" at the first body use. |
| abbreviations | REPEAT: full form again after the definition | Use the abbreviation, or quote the source verbatim. |
| citations | citation has no entry; entries not numbered 1 … N; listed twice | Correct the number or the reference list. |
| citations | reference is never cited | Cite it where it supports a claim, or remove it and renumber with `renumber_refs.py --drop-unused` (a content decision: ask the user). |
| citations | [n] is cited before [m] | With first-citation order, renumber with `renumber_refs.py --write` (or move the citation). |
| citations | draft citation [S101] left in the text | Finalize the draft source IDs into numbered references. |
| names | 'X' looks like 'Y' | Copy the name from `people` in `tasks.toml`, which holds it as the user's title page spells it. |
| translation | missing / stale twin; orphan | Translate or refresh the twin (section 4.2); rename or delete an orphan |
| parity | heading levels or numbers, table shapes, image paths, footnote labels, code, list items differ | Make the twin's structure match the source line for line |
| parity | math differs; citation sequence differs | Copy formulas exactly; keep every `[n]` where the source has it, in the same order |
| parity | decimal point; glossary variant | Use the language's decimal style; use the glossary's form (pack `[conventions]`) |
| parity | WARN source-language reference; looks untranslated; style warning (tone placement, bare "nhóm" as speaker) | Translate the reference word or the sentence; keep originals inside quotation marks only |

## 6. Post-checks of the Word document

| Group | Message | Usual cause |
| :---- | :---- | :---- |
| Parity | numbered headings differ; captions / images / tables count differs | A heading or caption pandoc did not recognise (see the format traps), or a filter dropped content. |
| Parity | caption not directly above its table / below its image; caption without SEQ field | Caption separated from its object; the caption is missing from the list of figures or tables. |
| Layout | image or table wider than the text area; table without repeating header row | Adjust the builder's sizing rules and rebuild, so the `.docx` stays reproducible. |
| Fields | contents / figure / table list field missing; updateFields not set | Builder regression (a compact task has no contents or lists, and these field checks and the roman-numbering check are skipped for it). |
| Numbering | title page has a header; no restart at 1; front matter not roman; header lacks short title or author; footer without PAGE | Builder regression or wrong `short_title`/`author` in `tasks.toml`. |
| Delivery | markdown leftover (`**`, `![`, `](`, `{width`, `$$`, `[^`, `\| :--`, ```); em dash; list not `(1)` | Malformed markdown in the sources. |
| Delivery | citation beyond the references; core property differs | Wrong citation number; metadata in `tasks.toml` differs from the document. |
| Delivery | WARN placeholder to fill; empty paragraphs in a row | Title-page placeholders such as `[Course name]` still to complete before delivery. |
| Language | WARN `<code>` convention: … | A convention slip in the target-language text, usually introduced in a caption or table; fix the twin |

Word computes page numbers only when it opens the file, so these checks work on the document structure; page-level layout (widows, blank pages) is handled by the builder's keep-with-next and landscape rules.

## 7. Builder behaviour

`build_docx.py` styles a reference document (A4, Times New Roman 12 pt or the pack's `[docx] body_size`, line spacing 1.3 or `line_spacing`, justified body, navy headings, captions, table styles), converts the language's section files with pandoc and `report_format.lua`, then lays out the Word file: a vertically justified title page; contents, list of figures and list of tables as Word fields (filled on opening); the report's own front pages (abbreviations, terms) after the contents; roman page numbers in the front matter and arabic from Part 1; running header (short title, author) and centred page number; tables with fixed column widths sized to their content (each column at least its longest word, a header within about three lines and short cells such as numbers, years and names on one line; a table whose content fits takes its natural width and is centred, a wider one gives the remaining width to the columns whose text still wraps), repeating header rows and banded rows; landscape pages for tables whose readable minimum is wider than a portrait page or whose cells hold long text, and for figures that print at least 8 % larger in landscape; every caption registered with a hidden SEQ field so Word's lists find it. With `[taskN.layout] compact = true` (`--compact`), the build makes a short document such as a proposal: parts and front pages follow one another without page breaks, no contents page or lists of figures and tables are inserted, the page after the title page is numbered 1 in arabic numerals, and every page stays portrait (wide tables take the portrait width in a smaller font, as with `--portrait`), so no page breaks surround rotated pages; title page, captions, tables and headers stay the same. `body_size` and `line_spacing` in the same table override the language pack's values. With `google_docs = true` in the task, the build also writes `<out>_GoogleDocs.docx` with `--portrait`: no landscape sections (wide tables take the portrait width at 8.5 pt, wide figures scale to it), so the document has only the title, front-matter and body sections. Use that copy for editing in Google Docs, where copying content across an orientation change between documents has been observed to stop the document from saving; the postcheck covers it too. Interface texts (contents headings, caption words) and the document language come from the language's pack, and language-only pages (for example a Vietnamese Lời cảm ơn) take their place among the front pages after the contents.
