You translate one group of report sections into {lang_name} (reference.md section 4.3, stage 3). Work in {root} with {python}. Your files: {files}. Scratch folder: {scratch}; keep helper scripts and notes there.

**Read first, in full:** {skill}/languages/{lang}/guide.md, lessons.md, and the task's glossary (`{python} {skill}/scripts/glossary.py --lang {lang} --task {task} show`). The front matter twins ({report}/00-*{suffix}) fix the full forms of every abbreviation; copy them.

**Who speaks:** {voice_line} (the line `report.py translate TASK` prints as "voice"; guide section 1, "Register").

**For each file, in report order:**
1. Read the English file in full; when its twin exists and is stale, read the twin too and change only what the English changed, so reviewed wording carries over. Exception: when the user or a reader test (reference.md section 4.3, stage 5) reports the twin as hard to read, rewrite every sentence from the English as a native author would; keeping an old sentence then needs a reason.
2. Write the twin as a native author would: the language's own sentence patterns, the glossary's terms, the same headings and numbers, table shapes, list items, figure paths (caption translated), footnote labels, code, formulas and `[n]` citations in the same order.
3. Run `{python} {skill}/scripts/check_parity.py --report {report} --lang {lang} {report}/FILE.md` to 0 errors and read its warnings; then record the file with `translation_status.py --report {report} --lang {lang} --mark {report}/FILE.md`.

Edit only your own twins. A recurring term that the glossary layers leave open goes into your report back, so the main session settles it once for every group. Report the files translated, the parity results, new terms, and any English sentence that looks wrong.
