# Reader re-test after the rewrite

Overall judgement (Vietnamese reader, lecturer of the course, first reading of the `.vi.md` files only). The form reads as natural Vietnamese and I can follow it without the English version: the rating scale (Bảng 1.1), the summary table (Bảng 1.2) and the closing lessons read smoothly, and the settled terms "kỳ mở module" (02:54, 03:12), "fold" (02:54) and "câu hỏi chỉ định" (02:16, 03:13) are defined in plain words at first use. Nothing stopped me completely. The places I had to reread cluster in two areas: (1) the description of the contact-list metric, which is a long, back-to-front clause and is called a count in Section 2 but a rate in Section 3; and (2) a few compressed evidence cells where a noun ("ba điểm", "rò rỉ thông tin", "fold loại trừ") is used without saying what it refers to. "rò rỉ thông tin" is never defined in these four files; in a row that sits next to privacy criteria a reader can take it as a personal-data leak rather than data leakage into the model. The remaining items only sound translated.

| # | File:line | Quote | What stopped me | Clarity (1–3) |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 02-00-assessment-by-milestone.vi.md:16 | "kèm hai ví dụ chỉnh sửa câu hỏi trước và sau" | "trước và sau" attaches to "chỉnh sửa câu hỏi", so it first reads as "edit the question before and after". I had to reread to see it means two before/after examples of a revised question ("hai ví dụ câu hỏi trước và sau khi chỉnh sửa"). | 2 |
| 2 | 02-00-assessment-by-milestone.vi.md:32 | "Với mỗi danh sách sinh viên cần liên hệ dự kiến lập (vào ngày 13 và ngày 27 của học phần)" | The subject of "dự kiến lập" is missing, so "cần liên hệ dự kiến lập" runs together; the contact list also appears here for the first time in Section 2 without saying who makes it or what it is for. Understood only after rereading as "mỗi danh sách ... mà nhóm dự kiến lập". | 2 |
| 3 | 02-00-assessment-by-milestone.vi.md:32 | "cách kiểm tra rò rỉ thông tin" | The term is not defined anywhere in the form. In Vietnamese "rò rỉ thông tin" first suggests a personal-data/privacy leak; I only understood it as data leakage (information from after the prediction date entering the model) from the analytics context. A short gloss at first use is needed. | 2 |
| 4 | 02-00-assessment-by-milestone.vi.md:34 | "được chọn với điều kiện các tệp dữ liệu xác nhận ba điểm và bước kiểm tra cấu trúc sau đó đã kiểm chứng ba điểm này" | "ba điểm" is never named, so I cannot tell what had to be confirmed; I understood the logic (conditional selection, later confirmed) only on rereading, and still do not know the content. | 2 |
| 5 | 02-00-assessment-by-milestone.vi.md:70 | "Chỉ số chính đếm số sinh viên về sau không hoàn thành học phần mà danh sách tìm ra, khi danh sách chỉ dài bằng số sinh viên Phòng Đào tạo liên hệ được" | Long relative clause stacked on another ("số sinh viên ... mà danh sách tìm ra, khi danh sách chỉ dài bằng ..."); I had to reread to get "among the top-N students the list flags, where N is the office's contact capacity, how many later fail to complete". | 2 |
| 6 | 02-00-assessment-by-milestone.vi.md:70 (also :87) | "các fold loại trừ từng kỳ mở" | "loại trừ" reads as "excluding each offering", which sounds like offerings are dropped. Only by recalling line 54 ("mỗi fold ... để riêng một kỳ mở làm dữ liệu đánh giá") did I see it means leave-one-offering-out. | 2 |
| 7 | 03-00-team-comments.vi.md:13 | "Thước đo mới của danh sách liên hệ là tỷ lệ sinh viên về sau không hoàn thành học phần mà danh sách tìm ra, khi danh sách chỉ dài bằng số sinh viên Phòng Đào tạo liên hệ được" | Same heavy clause as item 5, and here it is a "tỷ lệ" (rate) while 02:70 says the metric "đếm số" (counts). I had to reread both to decide whether it is a count or a proportion, and of what denominator. | 2 |
| 8 | 03-00-team-comments.vi.md:15 | "Việc tạo biến chỉ báo giá trị thiếu nào nay chỉ được quyết định trên dữ liệu huấn luyện" | "tạo biến chỉ báo giá trị thiếu nào" is an English "which" structure; I had to reread to get "the choice of which missing-value indicator variables to create is made on the training data only". | 2 |
| 9 | 03-00-team-comments.vi.md:16 | "tập kiểm thử của câu hỏi dự báo đã mở rộng từ 9 kỳ mở năm 2014 có kỳ mở cùng module năm 2013 sang cả 13 kỳ mở năm 2014" | Three "kỳ mở" in one noun phrase; "9 kỳ mở năm 2014 có kỳ mở cùng module năm 2013" needed two readings to parse as "the 9 offerings in 2014 whose module also ran in 2013". | 2 |
| 10 | 01-00-basis-overview.vi.md:3 | "giữ nguyên thứ tự và cách gọi" | Clear in context, but "cách gọi" (of the criteria) sounds translated; "giữ nguyên thứ tự và tên gọi của các tiêu chí" is more natural. | 3 |
| 11 | 01-00-basis-overview.vi.md:26 | "báo cáo Milestone 4 cũng dài so với một bản đề xuất" | Understood (Milestone 4 has no page limit), but "dài so với một bản đề xuất" is vague and sounds translated; it does not say against what yardstick. | 3 |
| 12 | 02-00-assessment-by-milestone.vi.md:13 | "đúng với bối cảnh bên liên quan mô phỏng mà đề bài cho phép" | Meaning clear; "bối cảnh bên liên quan mô phỏng" is a calque ("simulated-stakeholder setting"). | 3 |
| 13 | 02-00-assessment-by-milestone.vi.md:19 | "quyết định đó có thể thay đổi lại được hay không" | Understood as reversible, but "thay đổi lại" sounds translated; "có thể đảo ngược hay không" is the usual phrasing. | 3 |
| 14 | 02-00-assessment-by-milestone.vi.md:48 (also :67) | "Sáu điều kiện đầu vào kế thừa từ Milestone 1–2 đều đạt" | Understood after a moment as carried-over entry conditions; "điều kiện đầu vào" is an unusual phrase for this. | 3 |
| 15 | 02-00-assessment-by-milestone.vi.md:53 | "lần chạy lại cho kết quả trùng khớp từng byte, cùng từ điển 88 biến" | "cùng" glues a new item onto the clause about the rerun; reads like a translated list. | 3 |
| 16 | 02-00-assessment-by-milestone.vi.md:89 | "lượt đăng ký học chưa rút vào ngày thứ 14 kể từ khi học phần bắt đầu" | Understood as "still enrolled on day 14", but "chưa rút vào ngày thứ 14" can momentarily read as "did not withdraw on day 14". | 3 |
| 17 | 03-00-team-comments.vi.md:10 | "hệ số ảnh hưởng của lượt nhấp sớm (Cliff's delta, thang từ −1 đến 1)" | Understood thanks to the parenthesis; "hệ số ảnh hưởng" is not the usual Vietnamese term for effect size ("độ lớn hiệu ứng / mức độ khác biệt"). | 3 |
| 18 | 03-00-team-comments.vi.md:14 | "các học phần của trường cần được tính lại trên dữ liệu riêng" | "của trường" — which university is not said in this row; understood as the adopting university, but sounds translated. | 3 |
| 19 | 03-00-team-comments.vi.md:18 | "bản tiếng Việt của bộ slide đầy đủ đang chờ chốt số slide cuối cùng" | "bộ slide đầy đủ" (as opposed to which other deck?) is unclear but the overall status is understandable. | 3 |

## Decisions on the re-test flags

| # | Decision |
| :-- | :-- |
| 1 | Fixed: "hai ví dụ so sánh câu hỏi trước và sau khi chỉnh sửa". |
| 2 | Fixed: subject named ("Nhóm dự kiến lập danh sách sinh viên cần liên hệ…"), the list introduced with its purpose. |
| 3 | Fixed: "rò rỉ thông tin" (glossary term kept) glossed at first use in 02 and 03: "dữ liệu phát sinh sau thời điểm dự báo lọt vào mô hình". |
| 4 | Fixed in the English source and the twin: the three facts named. |
| 5 | Fixed in source and twin: the metric is a share (recall within the list length), stated in two clauses. |
| 6 | Fixed: "mỗi fold để riêng một kỳ mở làm dữ liệu đánh giá" in 02:70 and 02:87. |
| 7 | Fixed: split into two sentences; count/share conflict removed (both say "tỷ lệ phát hiện (recall)"). |
| 8 | Fixed: "Nhóm nay chỉ dùng dữ liệu huấn luyện để quyết định cần tạo những biến chỉ báo giá trị thiếu nào". |
| 9 | Fixed: "ban đầu gồm 9 kỳ mở năm 2014 mà module của chúng cũng được mở năm 2013, nhưng sau đó đã mở rộng…". |
| 10 | Fixed: "tên gọi của các tiêu chí". |
| 11 | Fixed in source and twin: "dù đề bài không quy định độ dài, vẫn dài khoảng 22 trang". |
| 12 | Fixed: "đúng như đề bài cho phép dùng bên liên quan mô phỏng". |
| 13 | Fixed: "có thể đảo ngược hay không". |
| 14 | Kept: "điều kiện đầu vào" is the glossary term for the entry gate (topic conventions glossary) and is explained in place ("kế thừa từ Milestone 1–2"). |
| 15 | Fixed: semicolon instead of "cùng". |
| 16 | Fixed: "vẫn còn theo học tính đến ngày thứ 14". |
| 17 | Fixed: glossary term "độ lớn hiệu ứng" (effect size). |
| 18 | Fixed in source and twin: "trường đại học nào áp dụng cách làm này". |
| 19 | Fixed in source and twin: "bộ slide dài hơn (gồm cả các slide phụ lục)". |

Consistency pass (logs/vi_consistency.log): coverage drift checked; "mức cơ sở" restored for the KPI baseline in 02 (Milestone 1 SMART row); the other drift warnings match ordinary English words ("fact", "passed", "before/after", "validation") or the allowed short form "phần chính". Glossary lint: 0 errors. Stage 5 closes: every flag of both rounds is fixed or kept with a reason, and no clarity-1 passage remained in the re-test.
