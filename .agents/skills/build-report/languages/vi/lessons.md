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
| S2. One term per concept from the reviewed report; concepts explained at first use (solo deck, 2026-10-28) | "bộ đánh giá" 53×, "bộ chọn" 4×, "tác tử lựa chọn" 2× for one component → "tác tử lựa chọn (bộ chọn)", then "bộ chọn" | reference 4, principle 2; `glossary.py coverage` (also in the deck reviewer's prompt); review 3.3; guide 3.2; slides.md 2; topic glossary row "judge" |
| S3. Every slide reads on its own, in both languages (solo deck, 2026-10-28) | slide 4 showed "pool", "oracle" and "self-consistency" whose meaning lived only in the note → each defined on the slide, the chart's measure and one square's meaning stated | slides.md 2 "Every slide reads on its own"; slide-only reading pass (slides.md 1, step 3); deck-review pass 4; guide 3.2 |

In S2 the English used three words for one component ("selection agent", "selector", "judge"), which an English reader takes as one thing; the Vietnamese turned them into unrelated terms, and the domain glossary itself had mapped "judge" and "selector" to different terms.
