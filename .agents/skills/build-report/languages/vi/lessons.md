# Lessons from reviews of Vietnamese translations

This is the ledger of what native Vietnamese reviewers, and the user reacting to a deliverable, changed in our translations. Each lesson keeps one typical edit, which calibrates a translator's ear faster than a rule does, and points to the place where its rule now acts: the guide (writing), `review.md` (reviewing), a glossary (terms), `pack.toml` (checks) or reference.md section 4 (the process for every language). The full evidence stays in the task folders. Reference.md section 4.7 describes how a lesson is learned and turned into a rule.

## 1. Human review of a translated report (2026-10-10)

A native reviewer edited a whole translated report: 80 of 159 body paragraphs and 25 of 86 front-matter paragraphs changed. The edits share one direction: fewer words, every phrase complete.

| Lesson | Before → after | Rule lives in |
| :---- | :---- | :---- |
| L1. Drop words that carry no meaning | Phạm vi của **nó** bao gồm… → Phạm vi của **Phần 3** là… | guide 2.7; review 3.5; pack warnings ("của nó", "Một … thứ ba") |
| L2. Complete the phrase with its head noun | PAD quy về một quyết định nhị phân → **Bài toán** PAD là quyết định nhị phân | guide 2.7; review 3.5; reference 4, principle 1 |
| L3. Plain actions instead of English images | Chỉ số thứ ba **nhìn xa hơn** phân hệ PAD → Chỉ số thứ ba **đánh giá** toàn bộ hệ thống | guide 2.7; review 3.5; reference 4, principle 1 |
| L4. Plainer, established words | Phần này **xác lập** các khái niệm → Phần này **trình bày** các khái niệm | glossary `common/report-writing.md`; review 3.5 |
| L5. Parentheses for pointers, affiliations, years, glosses | …, **như Hình 1.1 thể hiện** → … **(Hình 1.1)** | guide 2.7; review 3.5; pack warnings |
| L6. No comma before "và"/"hoặc"; semicolons in enumerations | bổ sung cho nhau**,** và… → bổ sung cho nhau và… | guide 5; review 3.5; pack warning |
| L7. Connectives in their written form | …, **song** vẫn ít phổ biến hơn → … **nhưng** ít phổ biến hơn | guide 2.7; review 3.5; pack warning |
| L8. The abbreviation once it is defined | Các **công cụ** chi phí thấp → Các **PAI** chi phí thấp | guide 5; review 3.5 |
| L9. Two-digit day and month | ngày 2/10/2026 → ngày **02/10/2026** | guide 7; pack warning |
| L10. Announce the structure | Mục 1.1.1 định nghĩa…, Mục 1.1.2… → **Cấu trúc của Mục 1.1 như sau:** Mục 1.1.1…; Mục 1.1.2… | guide 2.7; review 3.5 |
| L11. Curly quotation marks in running text | "…" → “…” (the builder converts straight quotes) | guide 5 |
| F1. Title page: lecturers first, each group under its label | one table, members left → "Giảng viên giảng dạy và hướng dẫn:" first, "Thực hiện: Nhóm 7" after | guide 6 |
| F2. Terms page: the English term leads | Tiềm năng tấn công (attack potential) → **Attack potential –** Tiềm năng tấn công | guide 6; review 3.6; `terms_page` check |

Decisions where the reviewer's habit and the house rules differed (2026-10-11): "dataset", "test" and "laptop" become "tập dữ liệu", "kiểm thử", "máy tính xách tay" (pack warning "English loanword"); every list is numbered "(1)", "(2)" (`check_format.py`); the reviewer's title-page layout (F1) is adopted.

## 2. Deck notes, the user's feedback

| Lesson | Before → after | Rule lives in |
| :---- | :---- | :---- |
| S1. Name the presenters and the authors apart (group deck, 2026-10-26) | Theo **nhóm**, đây là yếu tố đe dọa quan trọng nhất → Theo **nhóm chúng em**, … | guide 3.2 "Who speaks, who wrote"; pack warning on a bare "nhóm"; `[slides]` voice lines; reference 4, principle 3 |
| S1b. The same voice rule in reports (group report, 2026-11-08) | **Nhóm tác giả** ước lượng lại các phép biến đổi trong từng fold → **Chúng em** ước lượng lại …; "The team accepted nine" → "We accepted nine" | guide 1 "Register"; task `voice` in tasks.toml; pack `[style.voice]` checked by check_style.py; voice line in report-translate and report-review prompts; review 3 "Who speaks" |
| S2. One term per concept from the reviewed report; concepts explained at first use (solo deck, 2026-10-28) | "bộ đánh giá" 53×, "bộ chọn" 4×, "tác tử lựa chọn" 2× for one component → "tác tử lựa chọn (bộ chọn)", then "bộ chọn" | reference 4, principle 2; `glossary.py coverage` (also in the deck reviewer's prompt); review 3.3; guide 3.2; slides.md 2; topic glossary row "judge" |
| S3. Every slide reads on its own, in both languages (solo deck, 2026-10-28) | slide 4 showed "pool", "oracle" and "self-consistency" whose meaning lived only in the note → each defined on the slide, the chart's measure and one square's meaning stated | slides.md 2 "Every slide reads on its own"; slide-only reading pass (slides.md 1, step 3); deck-review pass 4; guide 3.2 |

In S2 the English used three words for one component ("selection agent", "selector", "judge"), which an English reader takes as one thing; the Vietnamese turned them into unrelated terms, and the domain glossary itself had mapped "judge" and "selector" to different terms.

## 3. A translated proposal the user could not read (milestone-1, 2026-11-04)

The user, a native reader, found the Vietnamese proposal very hard to understand although every check passed. A reader
test (an agent reading only the twins, `templates/prompts/report-reader-test.md`) flagged 82 of about 140 main-text
passages: 49 understood only after rereading, 33 sounding translated. Sentence length was mostly within the guide
(median 35 syllables); the causes were terms built to mirror English, a different denominator in each sentence, several
conditions in one sentence, and delta translation, which kept the stiff wording of earlier rounds.

| Lesson | Before → after | Rule lives in |
| :---- | :---- | :---- |
| T1. The everyday word of the field, not a mirror of the English | **lượt đăng ký học phần về sau không đạt hoặc rút học phần** → **sinh viên về sau không hoàn thành học phần**; **khả năng xem xét** → **năng lực xử lý của cán bộ**; **đợt học** → **lớp học phần**; **mốc xem xét** → **ngày lập danh sách** | guide 4, rule 8; topic glossary Replaces |
| T2. Say which group a share is out of | tại ngày 28, 71,9% số lượt rút học phần **vẫn chưa diễn ra** → **trong số sinh viên còn theo học vào ngày 0 và về sau rút học phần**, 71,9% rút **sau ngày 28** | guide 2.3; review 3 |
| T3. Name the scenario and what "at most" means | các danh sách theo kịch bản khả năng xem xét gồm 1.384 tên, nên … chỉ đạt độ bao phủ tối đa 36,9% → kịch bản chính giả định cán bộ xem xét kỹ được 15% số sinh viên …; các danh sách gồm 1.384 tên, ít hơn nhiều so với 3.755 sinh viên về sau không hoàn thành, nên ngay cả một danh sách hoàn hảo **cũng chỉ phát hiện được tối đa 36,9%** | guide 2.4; review 3 |
| T4. One condition per sentence in a goal or a question | the SMART Goal box as one sentence with six conditions → a framing sentence, then "Điều kiện thứ nhất / thứ hai / thứ ba" | guide 2.1 |
| T5. Rewrite, not patch, after a readability complaint | stale twins updated only where the English changed → every sentence rewritten from the English, then reviewed, a whole-report read and a second reader test | reference 4.2 step 1 and 4.3 stage 5; `report-translate.md` |
| T6. Test the replacement term too | **lớp học phần** for the course → **học phần**; **năng lực xử lý của cán bộ** → **số sinh viên cán bộ liên hệ được mỗi tuần** (short form "khả năng liên hệ của cán bộ"); **ngày lập danh sách** → **đợt lập danh sách** (milestone-1, 2026-11-05: the native reader found the T1 replacements still unnatural) | guide 4, rule 8; topic glossary course-completion-early-contact |

## 4. A finished translation still clunky (milestone-2, 2026-11-07)

The user, a native reader, found the Vietnamese clunky although all six stages had run and every check passed. Two causes
were measured. The last reader test ended with flags still open (milestone-2: 47 flagged, 19 fixed; milestone-1: 53
flagged, 13 fixed), and the glossary itself required phrases the reader had flagged, so translators had to use them.

| Lesson | Before → after | Rule lives in |
| :---- | :---- | :---- |
| T7. A reader test closes only when every flag is resolved | "ten hardest fixed, the rest not re-tested" recorded as done → each flag fixed or rejected with a reason, and the fixes tested again | reference 4.3 stage 5; `report-reader-test.md` |
| T8. A flagged term is a glossary question, and the native user decides it | **lượt mở module**, **lượt tổ chức** → **kỳ mở module**; **bài được chấm điểm** kept by the user's decision | reference 4.3 stages 1 and 5; topic glossary |
