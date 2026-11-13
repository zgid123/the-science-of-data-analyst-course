# Vietnamese native review

A translated file is finished when a native Vietnamese reader other than its translator has read it as a reader and as an editor and found it natural, complete and faithful. This file is that reviewer's protocol and checklist. The translator works from `guide.md`; the reviewer works from this file, with `guide.md` and the task's glossary as references.

## 1. The reviewer's role

- The reviewer is a different person (or agent) from the translator, so the text meets fresh eyes.
- The reviewer reads as a Vietnamese academic reader first and as an editor second. The question at every sentence is "would a Vietnamese author have written it this way?", not "does it match the English word for word?".
- The reviewer edits the `.vi.md` file directly and logs each finding (section 5). The English file, the structure, the citations, the numbers and the identifiers stay untouched.
- A finding that changes meaning, rather than wording, goes back to the source: the reviewer checks the English sentence and corrects the Vietnamese to match its meaning.

## 2. Three reading passes per file

| Pass | How | What it catches |
| :---- | :---- | :---- |
| 1. Reader pass (Vietnamese only) | Read the whole file once with the English closed, at reading speed, as the intended reader would | Sentences that need the English to be understood, broken flow between sentences, unnatural rhythm, terms that feel foreign, a paragraph whose point is unclear |
| 2. Fidelity pass (side by side) | Read each Vietnamese paragraph against its English paragraph | Lost or added meaning, a qualification or condition dropped, a number, citation or identifier moved, a definition placed later than in the English |
| 3. Editor pass (checklist) | Walk through the checklist of section 3, sentence by sentence | The specific faults below, each fixed in place |

Pass 1 comes first on purpose: a reader who has seen the English already understands every sentence and no longer notices what a Vietnamese-only reader would stumble over.

## 3. Checklist

Each item names what a natural, complete Vietnamese text does. A sentence that does otherwise is rewritten.

### 3.1. Sentences (ngữ pháp câu)

- [ ] **Complete.** Every sentence has a visible subject and predicate; every subordinate clause ("Khi …", "Nhằm …", "Với …") joins a main clause.
- [ ] **One main idea, one breath.** Sentences run about 25–45 syllables; any sentence past about 70 syllables is split at its main connective.
- [ ] **Vietnamese order.** Head noun before its modifiers; topic and claim before conditions and sources; English pre-modifier chains reordered the Vietnamese way.
- [ ] **Relational pairs complete.** "nếu … thì", "vì … nên", "tuy … nhưng", "không chỉ … mà còn" appear as pairs, and "thì", "là", "mà" are used only where Vietnamese needs them.
- [ ] **Light function words.** At most one "việc" or "sự" (as a nominaliser) per clause; no chain of three "của"; no "các những"; "một" only where the count matters.
- [ ] **Who speaks.** The writers name themselves as the task's voice sets (a group report: "nhóm" throughout, written "Nhóm" at the start of a sentence, lessons S1c; a solo report: "em"), matching "we" or "I" in the English; "nhóm tác giả" and "các tác giả" are reserved for the authors of a cited work.
- [ ] **Voice with intent.** Active clauses with a named actor wherever the actor is known; "được" for neutral or welcome outcomes, "bị" for adverse ones; at most two stacked passives per sentence.
- [ ] **Collocations.** Established verb–noun pairs ("đóng vai trò", "đáp ứng yêu cầu", "gây ra sự cố", "tiến hành kiểm thử") in place of word-for-word calques ("đóng một vai trò", "thực hiện việc …").
- [ ] **Formal openers.** No sentence in report prose opens with "Và", "Nhưng", "Mà", "Còn".

### 3.2. Coherence (mạch lạc và liên kết)

- [ ] **Topic sentence first.** Each paragraph opens with its point; evidence, mechanism and consequence follow in order.
- [ ] **Every sentence linked.** Each sentence after the first is tied to the one before by repetition of the key noun, a reference word ("cơ chế này", "bước đó") or a connective.
- [ ] **Connectors varied and accurate.** Adjacent sentences use different connectors; each connector states the real relation (addition "ngoài ra", cause "do đó", contrast "tuy nhiên", result "nhờ đó").
- [ ] **Given before new.** Sentences start from known information and end with the new point.
- [ ] **File bridges.** The first sentence links to the previous section and the last leads into the next, as in the English.

### 3.3. Terms and register (thuật ngữ và văn phong)

- [ ] **Glossary forms.** Every recurring term matches the task's glossary (`glossary.py --lang vi --task TASK lookup "<term>"`); regulated concepts use the wording of the Vietnamese legal text.
- [ ] **One term per concept.** Each concept keeps the same term within a file, across files and across deliverables: a deck uses the report's terms, and several English words for one thing (selector, judge, selection agent) share one Vietnamese term. `glossary.py --lang vi --task TASK coverage --report DIR` (or `--deck MODULE.py`) lists concepts that drift.
- [ ] **English kept only where Vietnamese engineers keep it.** Terms listed as "Keep English" stay English; every other English word is translated; an English term in parentheses appears only at its first use in the file.
- [ ] **Formal, calm register.** Precise Sino-Vietnamese terms where the field uses them, everyday Vietnamese words where they are clearer; no slang, no spoken fillers in report prose.
- [ ] **Positive framing.** Statements say what is, what works and what is recommended, as in the English.

### 3.4. Self-contained sections (mỗi mục tự đứng được)

- [ ] **Identifiers carry their Vietnamese words.** "(C3.A1.1)", "(P04)" come with their Vietnamese words wherever the English gives words.
- [ ] **Restatement before pointers.** "(Mục 2.3.1)" follows a clause that restates the point.
- [ ] **Definitions at first need.** Each term is explained where the English explains it, not later.
- [ ] **Exhibits introduced.** The sentence before each table and figure states in Vietnamese what it shows.

### 3.5. Economy and plain wording (gọn, đủ và cụ thể) – what human reviewers change most

- [ ] **No empty words.** No "một" before an ordinal or known item, no "đã/đang/sẽ/còn" where the context fixes the time, no "của nó/của chúng/của mình/của họ" – repeat the noun ("chỉ số này", "Phần 3").
- [ ] **Head nouns present.** Each phrase names its head noun ("khái niệm đối lập với…", "bài toán PAD", "tần suất tấn công", "cơ chế phát hiện"); "việc + verb" for a process becomes the noun of what performs it.
- [ ] **Plain actions over images.** English figures of speech ("mở ra con đường", "nhìn xa hơn", "đổi … lấy …", "hai đầu của trục", "trở thành một …") are rewritten as the plain action.
- [ ] **Established words.** trình bày, cơ sở, áp dụng, phân biệt A với B, quy định về, chứng minh rằng, ưu điểm và hạn chế, giải pháp, ghi nhận, xử lý, bỏ qua, mô phỏng (guide 2.7).
- [ ] **Parentheses for side information.** Pointers "(Hình 1.1)", affiliations "(Đại học Oulu)", years "(2018)", short glosses – instead of "như Hình … thể hiện", "thuộc …", "một phương pháp năm …".
- [ ] **Written connectives.** nhưng (not ", song"), do, ví dụ, Ngoài ra, Trên cơ sở, Trong khi … thì, Như vậy, Tóm lại, hoặc (not "hay" in statements), là (not "tức" in a definition).
- [ ] **Punctuation.** No comma before "và"/"hoặc"; semicolons between the clauses of an enumeration; a colon before an explanation.
- [ ] **Abbreviations in use.** After its definition an abbreviation replaces the Vietnamese words.
- [ ] **Structure stated.** Section introductions announce subsections with "Cấu trúc của Mục … như sau:" and semicolons; summing-up paragraphs open with "Tóm lại,".

### 3.6. Fidelity and form (trung thành và hình thức)

- [ ] **Meaning complete.** Facts, conditions, numbers and hedges match the English one for one; quantities, dates and limits match too.
- [ ] **Citations and identifiers in place.** `[n]` numbers, difficulty, component and case IDs, codes and document numbers sit with the clause they support.
- [ ] **Orthography.** Modern tone placement (hóa, thủy); sentence case in headings and captions; captions start with "Hình" or "Bảng" and a capitalised noun.
- [ ] **Numbers.** Decimal comma, dot for thousands, dates "02/10/2026" (two-digit day and month) or "tháng 10 năm 2026", "Mục", "Hình", "Bảng", "Phần".
- [ ] **Front matter.** Terms page rows open with the English term, then "–" and the Vietnamese name, also for terms kept in English; abbreviation rows give the Vietnamese full form, then "–" and the English expansion (guide 6).
- [ ] **Abbreviations.** Vietnamese full form with the abbreviation in parentheses at first use, in the file the English uses; official Vietnamese abbreviations where they exist (NHNN, ĐVCNT if the glossary chooses it).

## 4. After the edits

1. Run `check_parity.py --report DIR --lang vi FILE` for every edited file: 0 errors, and each warning resolved or justified in the log.
2. Re-read every rewritten sentence once more in pass 1 style, with the English closed.
3. Add a glossary row for any term the review settled, and add the replaced form to Replaces, so later files and reports follow it.
4. When a human review arrives, learn from it with the method of reference.md section 4.7, record it in `lessons.md`, and add each new kind of change to the guide, this checklist, the glossaries or the pack's warnings.

## 5. Review log

Each reviewer writes its log to the round's file in `taskN/research/reviews/`, created with research-report's `layout.py new-review --kind vi-native-review --scope g1` (`--same` for the parallel groups of one round, so they share its number):

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |

The log closes with one line per file: reviewed, findings fixed, parity result.
