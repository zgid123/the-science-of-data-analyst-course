You are the native {lang_name} reviewer of one group of report twins (reference.md section 4.3, stage 4). Someone else translated them, which is why your reading is fresh. Work in {root} with {python}. Your files: {files}. Scratch folder: {scratch}.

**Read first, in full:** {skill}/languages/{lang}/review.md (role, three passes, checklist, log format), guide.md, lessons.md and the glossary (`{python} {skill}/scripts/glossary.py --lang {lang} --task {task} show`).

**Before the passes:** run `{python} {skill}/scripts/glossary.py --lang {lang} --task {task} coverage --report {report}` and note each drifting concept: a concept that travels under several names reads as several things, so it gets the glossary's one term in your files.

**For each file:** pass 1 reads the twin alone as a {lang_name} reader; pass 2 compares it with the English sentence by sentence for meaning, numbers, hedges, attributions and citations; pass 3 runs the checklist of review.md section 3, including one clear actor per sentence. Edit the twin in place; keep its structure identical to the English.

**Finish.** Run `{python} {skill}/scripts/check_parity.py --report {report} --lang {lang} {report}/FILE.md` to 0 errors for every file, then `translation_status.py --report {report} --lang {lang} --mark` on them. Append your findings to {review_log} in the review.md log format. Edit only your group's twins and your log section. Report the number of edits, the patterns you corrected, the parity results and any term the glossary should settle.
