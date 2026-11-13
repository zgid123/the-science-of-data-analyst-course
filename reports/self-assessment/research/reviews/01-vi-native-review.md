# Native Vietnamese review of the four twins


- Date (UTC): 2026-11-13T01:48Z
- Protocol: `.claude/skills/build-report/languages/vi/review.md` (three passes), `guide.md`, `lessons.md`, task glossary (`glossary.py --lang vi --task self-assessment show`)
- Voice: team decision S1c, "nhóm" ("Nhóm" at sentence start), never "nhóm chúng em" / "chúng em"; support office "Phòng Đào tạo"
- Pre-backup of the twins: session scratchpad `before/` (diff basis for the counts below)

## Before the passes

Command: `./venv/bin/python .claude/skills/build-report/scripts/glossary.py --lang vi --task self-assessment coverage --report reports/self-assessment/report`
Result: 6 drifting concepts.

| Concept | Verdict |
| :---- | :---- |
| brief (course brief) → đề bài, 26× in English, 0× | Real drift: the twins used "hướng dẫn". Fixed to "đề bài" everywhere (the milestone-1/4/5 twins use "đề bài"). |
| Answered / Partial / Deferred / Dropped | The English uses "answered" as an ordinary verb; "đã có câu trả lời", "được trả lời" are right. Resolved after edits (no longer listed). |
| gate (success criterion S1) → điều kiện đạt | False positive: the English "gate" here is "must-have gates" (→ điều kiện bắt buộc) and "entry gate" (→ điều kiện đầu vào), both glossary forms. |
| PASS / FAIL | False positive: "passed" is a verb ("checks passed" → "đều đạt"). |
| Before / After (Change Log columns) | False positive: ordinary "before/after"; the Milestone 1 "before-and-after refinements" now read "Before → After", as the glossary row for Milestone 1 asks. |
| Validation (traceability column) | False positive: "validation round", "validation checks" (→ vòng xác nhận, phép kiểm tra). |

## Criterion column check

Every "Tiêu chí" cell (44 rows over Tables 2.1–2.5, plus the M5 not-applicable row) was compared with the rubric tables of `milestones/0N/milestone-N.md` (M1 §10, M2 §17, M3 §18, M4 §14, M5 §8): all verbatim, no edit.

## Findings

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 01, 02, 03 | many (26×) | 3.3 One term per concept (glossary "brief") | hướng dẫn (Milestone N) | đề bài |
| 2 | 01 | 3 | 3.1 Who speaks / actor | kết quả đã nộp | kết quả nhóm đã nộp |
| 3 | 01 | 3 | 3.5 Established words | Hướng dẫn chỉ cho tổng điểm 100 của mỗi milestone | Đề bài chỉ quy định tổng 100 điểm cho mỗi milestone |
| 4 | 01 | 10 | 3.1 Actor named ("that we state") | còn một hạn chế, được ghi rõ trên cùng dòng | còn một hạn chế; nhóm ghi rõ hạn chế đó trên cùng dòng |
| 5 | 01 | 11 | 3.1 Complete sentence (subjectless "Thiếu") | Thiếu một nội dung mà tiêu chí nêu hoặc nội dung đó dựa trên… | Một nội dung mà tiêu chí nêu bị thiếu hoặc chỉ dựa trên… |
| 6 | 01 | 12 | 3.6 Meaning ("makes the criterion optional") | Hướng dẫn cho phép chọn làm hoặc không làm nội dung này và nhóm không chọn làm | Đề bài để tiêu chí này ở dạng tùy chọn và nhóm không thực hiện phần tùy chọn đó |
| 7 | 01 | 14 | 3.5 Parentheses for side information | …của milestone đó, nơi người đọc tìm thấy phần việc tương ứng; Số trang là số trang phần chính, không tính phụ lục, được đo… | …mục, bảng hoặc phụ lục chứa phần việc tương ứng…; Số trang là số trang của phần chính (không tính phụ lục), được đo… |
| 8 | 01 | 23 | 3.6 Meaning ("not reported") | đã được đặc tả nhưng không được trình bày kết quả | đã được đặc tả nhưng chưa được báo cáo kết quả |
| 9 | 01 | 24 | 3.5 Plain wording | cùng 1 tiêu chí không áp dụng | ngoài ra 1 tiêu chí không áp dụng |
| 10 | 01, 02, 03 | 01:24; 02:89; 03:13 | 3.3 Glossary (test set / test → kiểm thử) | chờ một lần kiểm tra sau | chờ một lần kiểm thử sau |
| 11 | 01 | 26 | 3.6 Meaning ("rated partly met") | không có tiêu chí nào chỉ đạt một phần | không có tiêu chí nào ở mức đạt một phần |
| 12 | 02, 03 | 02:16, 32, 36, 89; 03:13 (×2) | 3.3 Glossary (prescriptive → chỉ định; "đề xuất" reads as "proposed") | đề xuất hành động | chỉ định |
| 13 | 02 | 13 | 3.6 Meaning lost ("two more than") | nhiều hơn mức tối thiểu ba của hướng dẫn | nhiều hơn hai bên so với mức tối thiểu ba bên của đề bài |
| 14 | 02 | 14 | 3.5 No repeated word; clear actor | một vòng xác nhận với mọi bên liên quan để xác nhận, sửa và bổ sung yêu cầu | một vòng xác nhận với cả năm bên liên quan, qua đó các bên xác nhận, chỉnh sửa và bổ sung yêu cầu |
| 15 | 02 | 16 | 3.3 Glossary (Milestone 1 Before → After stays English) | hai ví dụ chỉnh sửa trước và sau | hai ví dụ chỉnh sửa Before → After |
| 16 | 02 | 17 | 3.5 Head noun; 3.1 actor | người dùng của từng câu hỏi; không nêu thuật toán… | người sử dụng kết quả của từng câu hỏi; báo cáo không nêu thuật toán… |
| 17 | 02 | 18 | 3.6 Meaning lost ("that apply") | các quy định của Việt Nam về bảo vệ dữ liệu cá nhân | các quy định có liên quan của Việt Nam về bảo vệ dữ liệu cá nhân |
| 18 | 02 | 20 | 3.5 Established word | ma trận truy vết nối mục tiêu… | ma trận truy vết liên kết mục tiêu… |
| 19 | 02 | 24, 42, 77 | 3.1 One idea per sentence; ambiguous "và" joining two predicates | …có kiểm chứng và yêu cầu nộp kèm gói…; …(AI Decision Log) và yêu cầu một quy trình…; …tài liệu tham khảo và khuyến nghị phần chính… | split into two sentences each ("Ngoài báo cáo, đề bài còn yêu cầu…", "Đề bài còn yêu cầu…", "Đề bài khuyến nghị…") |
| 20 | 02 | 30 | 3.3 Glossary (baseline of a milestone) | Phiên bản Milestone 1 được nhắc lại | Phiên bản cơ sở của Milestone 1 được nhắc lại |
| 21 | 02 | 34, 35 | 3.5 Plain wording / head noun | được chọn với ba điều kiện; cách dựng lại bằng hai lệnh | được chọn kèm ba điều kiện; quy trình dựng lại bằng hai lệnh |
| 22 | 02 | 36 | 3.6 Meaning (prescriptive action not covered) | ba điểm khác nhau…; hành động đề xuất được ghi là không đáp ứng | ba điểm khác biệt…; hành động của câu hỏi chỉ định được ghi là chưa có dữ liệu |
| 23 | 02 | 37 | 3.1 Who speaks (bare "nhóm" here meant a group of students, read as the team) | tính trên nhóm có ít nhất năm người | tính trên ít nhất năm sinh viên |
| 24 | 02 | 38 | 3.1 Clarity; 3.6 meaning (which round had the partly accepted ones) | mười trên mười hai góp ý và toàn bộ mười góp ý được chấp nhận, số còn lại được chấp nhận một phần | nhóm chấp nhận mười trên mười hai góp ý ở vòng thứ nhất (hai góp ý còn lại được chấp nhận một phần) và cả mười góp ý ở vòng thứ hai |
| 25 | 02 | 50 | 3.2 Linking | mười chín vấn đề…, ba vấn đề ở mức nghiêm trọng cao | …, trong đó ba vấn đề ở mức nghiêm trọng cao |
| 26 | 02 | 51 | 3.3 Glossary (GREEN/YELLOW/RED explained once) | mức YELLOW … mức RED | mức YELLOW (hỗ trợ một phần) … mức RED (không được hỗ trợ) |
| 27 | 02 | 52 | 3.5 Head noun ("the check that proves it") | phép kiểm tra chứng minh | phép kiểm tra chứng minh quyết định đó |
| 28 | 02 | 53 | 3.5 Parentheses (two adjacent brackets) | kèm truy vết nguồn gốc dữ liệu (lineage) (Mục… | có truy vết nguồn gốc dữ liệu (lineage) cho từng biến (Mục… |
| 29 | 02 | 54, 70, 87 | 3.3 Glossary (leave-one-run-out, test set) | kiểm tra trên mười ba kỳ mở…; mỗi fold tách riêng một kỳ mở | kiểm thử trên…; các fold … theo cách loại trừ từng kỳ mở (leave-one-run-out); later "các fold loại trừ từng kỳ mở" |
| 30 | 02 | 56 | 3.6 Meaning ("kept for audit only") | chỉ dùng để kiểm tra | chỉ được giữ lại để kiểm tra tính công bằng |
| 31 | 02 | 61 | 3.5 Parentheses over repeated "tức"; 3.1 split | chấm Level 1, tức phần đề xuất…; Level 2, tức nguyên mẫu…, không bắt buộc và không cần để đạt đủ 100 điểm; …không quy định số trang và phần chính dài… | Level 1 (đề xuất phương pháp và cách đánh giá); Level 2 (nguyên mẫu có kết quả) … không phải điều kiện để đạt đủ 100 điểm; "Đề bài không quy định số trang; phần chính dài…" |
| 32 | 02 | 67 | 3.3 Glossary (AQ Modeling Brief) | một bản mô tả mô hình hóa cho mỗi câu hỏi | một AQ Modeling Brief (bản mô tả yêu cầu mô hình hóa) cho mỗi câu hỏi |
| 33 | 02 | 68 | 3.1 Actor; head verb | mỗi câu hỏi cần mô hình…, không dùng học máy | mỗi câu hỏi cần mô hình hóa…, báo cáo không dùng học máy |
| 34 | 02 | 70 | 3.1 Voice | các ngưỡng thành công cố định trước mọi lần kiểm tra | các ngưỡng thành công được cố định trước mọi lần kiểm thử |
| 35 | 02 | 71 | 3.5 Head noun | ba nhóm thuộc diện kiểm định khẳng định | ba nhóm sinh viên thuộc diện kiểm định khẳng định |
| 36 | 02 | 73 | 3.3 Glossary (prototype protocol); 3.5 punctuation | …bản đề xuất và nguyên mẫu … ở dạng giao thức chạy | …bản đề xuất; nguyên mẫu … dưới dạng giao thức chạy nguyên mẫu |
| 37 | 02 | 83 | 3.3 Glossary (AQ Revision Log); 3.5 head noun | Bối cảnh, …; nhật ký điều chỉnh | Bối cảnh nghiệp vụ, …; Nhật ký điều chỉnh AQ |
| 38 | 02 | 88 | 3.1 Voice, complete clause | Báo cáo ghi Level 2 đã đặc tả, chưa chạy …, nên theo hướng dẫn điểm của tiêu chí này chuyển vào | Báo cáo ghi rõ Level 2 đã được đặc tả nhưng chưa chạy …, nên theo đề bài, điểm của tiêu chí này được chuyển vào |
| 39 | 02 | 89 | 3.3 Glossary (sign effect is an association, never causal; accuracy → chất lượng dự báo) | năm dấu hiệu sớm giữ nguyên ở cả hai năm, trong đó bỏ lỡ một bài làm tăng tỷ lệ không hoàn thành…; danh sách liên hệ chưa có độ chính xác đo được | năm dấu hiệu sớm được xác nhận ở cả hai năm, trong đó sinh viên bỏ lỡ một bài có tỷ lệ không hoàn thành cao hơn khoảng 40 điểm phần trăm; chất lượng dự báo của danh sách liên hệ chưa được đo |
| 40 | 02 | 91 | 3.1 Ambiguous "và"; 3.6 meaning ("written anew") | …có đánh dấu khoảng trống và báo cáo được viết lại thành một mạch… thay vì ghép các báo cáo trước | …có đánh dấu các khoảng trống; phần trình bày được viết mới thành một mạch… thay vì ghép từ các báo cáo trước |
| 41 | 02 | 92 | 3.3 Glossary (Reflection → Bài học rút ra) | phần nhìn lại | phần bài học rút ra |
| 42 | 02 | 93 | 3.1 Word order | dài hơn mức khuyến nghị 25 trang khoảng sáu trang | vượt mức khuyến nghị tối đa 25 trang khoảng sáu trang |
| 43 | 03 | 3 | 3.6 Hedge added | không diễn ra hoàn toàn như kế hoạch | không diễn ra đúng như kế hoạch |
| 44 | 03 | 9 | 3.1 Actor; ambiguous "và"; "chạy" a person | Mỗi bên liên quan được chạy…, xây dựng trên… và từng câu…; Một vòng xác nhận được thực hiện lại…; …đúng như hướng dẫn cho phép và cần được cán bộ thật xác nhận | được mô phỏng…, dựa trên…; từng câu…; "Nhóm tiến hành thêm một vòng xác nhận…"; "…đúng như đề bài cho phép; trước khi thí điểm, các yêu cầu này cần được cán bộ thật của trường xác nhận" |
| 45 | 03 | 10 | 3.5 Comma splice; 3.3 glossary (sign effect → mức liên hệ, not "ảnh hưởng") | không dùng được ngay; Lượt nhấp được cộng theo ngày, mỗi đặc trưng…; …bị loại và việc bỏ lỡ bài chỉ tính…; bỏ dòng trùng chỉ làm ảnh hưởng của mức tham gia sớm thay đổi tối đa 0,004 | không dùng nguyên trạng được; …theo ngày và mỗi đặc trưng… có thêm một phiên bản…; …bị loại bỏ; số bài bị bỏ lỡ chỉ tính…; khi bỏ dòng trùng, mức liên hệ giữa mức tham gia sớm và kết quả học phần thay đổi tối đa 0,004 |
| 46 | 03 | 11 | 3.1 Ambiguous double "và"; 3.3 term (sensitivity analysis) | gọi một giá trị… khác với tên trong tệp và trang web… ; cho rằng; Việc nộp trễ được tính riêng…; giữ làm phép kiểm tra độ nhạy | …bằng tên khác với tên trong tệp; ngoài ra, trang web…; ghi rằng; Số bài nộp trễ được tính riêng cho từng loại bài tập; giữ làm phân tích độ nhạy |
| 47 | 03 | 12 | 3.5 Plain wording | trong khoảng đó | trước mốc đó |
| 48 | 03 | 13 | 3.6 Meaning (read as "one third of the questions"); 3.3 glossary precision | Dữ liệu chỉ hỗ trợ một phần ba câu hỏi; Mục tiêu độ chính xác 50% | Dữ liệu chỉ hỗ trợ một phần cho ba câu hỏi; Mục tiêu độ chính xác của danh sách (precision) đạt 50% |
| 49 | 03 | 14 | 3.5 "hoặc" not "hay" in statements; "và" ambiguity | cố vấn học tập hay biện pháp hỗ trợ; được để lại cho; …2013–2014 và các học phần của trường cần… | hoặc; được dành cho; …2013–2014; các học phần của trường cần… |
| 50 | 03 | 15 | 3.6 Meaning ("checks had passed" = missed); clarity of example | đã bỏ qua; các bài đến hạn trước khi sinh viên đăng ký muộn bị tính là bỏ lỡ và một phép kiểm tra… | đã bỏ sót; với sinh viên đăng ký muộn, các bài đến hạn trước ngày đăng ký bị tính là bỏ lỡ; một phép kiểm tra khác… |
| 51 | 03 | 16 | 3.3 Glossary (test set → tập kiểm thử; Change Log → Nhật ký thay đổi) | tập kiểm tra; nhật ký thay đổi | tập kiểm thử; Nhật ký thay đổi |
| 52 | 03 | 17 | 3.1 Order (object after long insertion) | chuyển nguyên văn sang phụ lục, từng khối một, những chi tiết vượt quá… | chuyển từng khối chi tiết vượt quá yêu cầu của đề bài sang phụ lục, giữ nguyên văn |
| 53 | 03 | 18 | 3.1 Actor and one idea per sentence | Người dịch và người rà soát riêng biệt viết lại toàn bộ bản tiếng Việt và các phép kiểm tra tự động nay giữ mỗi khái niệm một thuật ngữ; Đã giải quyết với các báo cáo; chờ quyết định số slide | Bản tiếng Việt được viết lại toàn bộ, do người dịch và người rà soát độc lập với nhau thực hiện. Các phép kiểm tra tự động nay bảo đảm mỗi khái niệm chỉ dùng một thuật ngữ; Đã giải quyết đối với các báo cáo; đang chờ chốt số slide |
| 54 | 03 | 20 | 3.5 Plain action over image; "và" ambiguity; "hoặc" | …câu trả lời của AI và phần lớn…; một câu hỏi hay một mục tiêu; kéo giãn bằng chứng; …bỏ sót và mỗi gợi ý… | …câu trả lời của AI; phần lớn…; hoặc; suy diễn vượt quá bằng chứng; …bỏ sót; mỗi gợi ý… |

Notes:

- Finding 39 keeps the English number and population; "raising the non-completion rate" is rendered as a rate difference ("có tỷ lệ … cao hơn"), which is the arithmetic meaning and follows the glossary rule that a sign effect is an association. The English sentence stays as written; the team may want to align it ("with a missed task associated with a non-completion rate about 40 percentage points higher").
- `check_style.py` first flagged "Nhóm thực hiện" (finding 44) as the third-person label "the performing group"; reworded to "Nhóm tiến hành". Rerun: 0 errors, 0 warnings.
- The title page (00-0) needed no change: names, titles, course, university block and date match the Milestone 5 twin.

## Checks after the edits

| Command | Result |
| :---- | :---- |
| `./venv/bin/python .claude/skills/build-report/scripts/check_parity.py --report reports/self-assessment/report --lang vi` | 4 pairs, 0 errors, 1 warning: line 33 of 02 "datasets" (English loanword) sits inside the brief's criterion "Search strategy + ≥3 candidate datasets + Search Log", copied verbatim by design – justified |
| `./venv/bin/python .claude/skills/build-report/scripts/check_style.py --report reports/self-assessment/report --lang vi` | 3 body files, 0 errors, 0 warnings |
| `./venv/bin/python .claude/skills/build-report/scripts/glossary.py --lang vi --task self-assessment coverage --report reports/self-assessment/report` | 4 drifting, all false positives explained above |
| `translation_status.py --report reports/self-assessment/report --lang vi --mark FILE.md` for 01, 02, 03 | recorded; status: 4 sections, 0 need translation, 0 orphaned |
| Scan `grep -nE ', (và|hoặc) |chúng em|hướng dẫn|đề xuất hành động'` over the twins | no hits |

## Per file

- 00-0-title-page.vi.md: reviewed, 0 findings, parity pass.
- 01-00-basis-overview.vi.md: reviewed, 11 findings fixed (8 lines changed), parity pass.
- 02-00-assessment-by-milestone.vi.md: reviewed, 31 findings fixed (37 lines changed), parity pass (1 justified warning).
- 03-00-team-comments.vi.md: reviewed, 13 findings fixed (12 lines changed), parity pass.

## Addendum: coordinator term decisions (stage 1, topic glossary course-completion-report-conventions.md)

Glossary re-printed after the decisions. Status of each decision in the twins:

| # | Decision | Status | Edits |
| :---- | :---- | :---- | :---- |
| 1 | brief → "đề bài" | Already applied in finding 1; `grep -c "hướng dẫn"` = 0 in all four twins | none |
| 2 | main text → "phần nội dung chính" at first use in a file, "phần chính" after | Applied: 01 line 14 "số trang của phần nội dung chính", 02 line 7 "phần nội dung chính của báo cáo", 03 line 17 "phần nội dung chính còn lại" | 3 |
| 3 | Rating scale Đạt / Đạt phần lớn / Đạt một phần / Không áp dụng; column "Mức đánh giá" | Already in place (Table 1.1 and every table of Section 2) | none |
| 4 | grading criterion → "tiêu chí chấm điểm"; self-assessment → "tự đánh giá" | Already in place (Sections 1–2, table captions) | none |

Checks after the addendum: `check_parity.py` 4 pairs, 0 errors, 1 justified warning (unchanged); `check_style.py` 0 errors, 0 warnings; `translation_status.py --mark` re-run for 01, 02, 03. `glossary.py coverage`: 5 drifting. The new row "main text" shows 3 of 21 because the other 18 uses take the permitted short form "phần chính". The other four are the false positives above.
