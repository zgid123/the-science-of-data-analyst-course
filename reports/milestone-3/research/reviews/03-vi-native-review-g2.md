# Vietnamese native review – group G2 (Sections 3 and 4)

Reviewer: native Vietnamese reviewer agent (not the translator), 2026-11-06. Protocol: `build-report/languages/vi/review.md`
(three passes per file), with `guide.md`, `lessons.md` and the merged glossary (`glossary.py --lang vi --task milestone-3 show`).

Glossary coverage before the passes (`glossary.py --lang vi --task milestone-3 coverage --report reports/milestone-3/report`):
10 drifting concepts. Those touching G2: enrolment (the twins use the settled "lượt đăng ký học", so the drift against the
glossary form "lượt đăng ký học phần" is expected), grain ("mức chi tiết (grain)" in 03-01, "Mức chi tiết của studentVle" in
03-05 – short form of "mức chi tiết của bảng (grain)", kept), deprivation band (full form at first use in 03-02, short form
"mức khó khăn của khu vực" in 03-04 – both glossary forms), non-completion (bare "không hoàn thành", as settled).

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 03-00-profiling-quality | 1 | 3.3 Glossary forms (settled: profiling) | Lập hồ sơ và đánh giá chất lượng dữ liệu | Khảo sát dữ liệu và chất lượng dữ liệu |
| 2 | 03-00-profiling-quality | 3 | 3.3 Glossary forms; English at first use | Hồ sơ dữ liệu (data profile) bao quát … | Kết quả khảo sát dữ liệu (profiling) bao quát … |
| 3 | 03-00-profiling-quality | 3 | 3.3 One term per concept | Quá trình lập hồ sơ chạy …; mười ba số liệu trong hồ sơ | Bước khảo sát chạy …; mười ba số liệu khảo sát |
| 4 | 03-00-profiling-quality | 3 | 3.1 Voice with intent (actor) | đếm lại độc lập … bằng một đoạn mã riêng | đếm lại độc lập … do một đoạn mã riêng thực hiện |
| 5 | 03-01-shape-keys-joins | 3 | 3.5 Head nouns present | sáu bảng có khóa đều không có khóa trùng lặp | sáu bảng có khóa chính đều không có giá trị khóa trùng lặp |
| 6 | 03-01-shape-keys-joins | 3 | 3.5 Head nouns; plain wording | lượt nhấp được cộng theo … trước khi sử dụng | số lượt nhấp được cộng dồn theo … trước khi đưa vào phân tích |
| 7 | 03-01-shape-keys-joins | 3 | 3.1 Complete (one clear actor) | 787.170 dòng (7,39%) trùng lặp …, chiếm 3,19% | …; các dòng này chiếm 3,19% |
| 8 | 03-01-shape-keys-joins | 3 | 3.6 Meaning complete ("expected") | so với mức 24,0% nếu chỉ do ngẫu nhiên | so với mức 24,0% kỳ vọng nếu chỉ do ngẫu nhiên |
| 9 | 03-01-shape-keys-joins | 3 | 3.5 Head nouns present | vì sinh viên rời đi trước ngày bắt đầu | vì những sinh viên rời đi trước ngày bắt đầu |
| 10 | 03-01-shape-keys-joins | 3 | 3.2 Connector accurate; 3.6 meaning ("joined from") | Trên cơ sở đó, … nối vào bảng lượt đăng ký học | Vì thế, … nối vào bảng lượt đăng ký học, lấy bảng này làm gốc |
| 11 | 03-02-missingness-validity | 3 | 3.2 Every sentence linked | Dữ liệu có ít giá trị thiếu. Cách các giá trị thiếu phân bố cho thấy nguồn gốc phát sinh. | Dữ liệu có ít giá trị thiếu; cách phân bố của các giá trị thiếu cho thấy nguồn gốc phát sinh của từng loại. |
| 12 | 03-02-missingness-validity | 3 | 3.3 One term per concept (completion) | đạt module ở 65,7% | hoàn thành module ở 65,7% |
| 13 | 03-02-missingness-validity | 3 | 3.6 Meaning ("not submitted", not "not yet") | bài chưa được nộp | sinh viên không nộp bài đó |
| 14 | 03-02-missingness-validity | 3 | 3.1 Vietnamese order | kết quả bài thi thường không có theo thiết kế của bộ dữ liệu | theo thiết kế, bộ dữ liệu thường không chứa kết quả bài thi |
| 15 | 03-02-missingness-validity | 5 | 3.1 Relational pair (cho thấy … nhưng cũng) | nhưng phát hiện sáu điểm | nhưng cũng phát hiện sáu điểm |
| 16 | 03-02-missingness-validity | 5 | 3.3 One term per concept (enrolment) | 58 lượt đăng ký sau thời hạn | 58 lượt đăng ký học diễn ra sau thời hạn |
| 17 | 03-03-distributions-outcome | 3 | 3.5 Head nouns present | 2.503 lượt vượt ngưỡng trên | 2.503 lượt đăng ký học vượt ngưỡng trên |
| 18 | 03-03-distributions-outcome | 5 | 3.5 Economy (redundant "đăng ký … đã đăng ký") | 28.061 lượt đăng ký học đã đăng ký đến ngày 14 và chưa hủy đăng ký đến ngày đó | 28.061 lượt đăng ký học được ghi nhận đến ngày 14 và chưa bị hủy tính đến ngày đó |
| 19 | 03-03-distributions-outcome | 5 | 3.3 English only where kept | nhiều kết quả Fail nhất | nhiều lượt không đạt (Fail) nhất |
| 20 | 03-04-temporal-representativeness | 3 | 3.1 Vietnamese order | còn với ngày 27 thì có 16 lượt mở | trong khi với ngày 27 con số này là 16 lượt mở |
| 21 | 03-04-temporal-representativeness | 3 | 3.6 Meaning ("dated by a cut-off" = on or before) | có ngày ghi nhận trước thời điểm đó | có ngày rút không muộn hơn thời điểm đó |
| 22 | 03-04-temporal-representativeness | 5 | 3.1 Parallel structure | 11,5% sinh viên của EEE nhưng 88,4% của BBB | 11,5% sinh viên ở EEE nhưng 88,4% ở BBB |
| 23 | 03-05-quality-issue-log | 3 | 3.1 One idea per breath; "chỉ" read as "only" | Mức Cao chỉ vấn đề …; mức Trung bình chỉ vấn đề …; mức Thấp chỉ vấn đề … | Mức độ nghiêm trọng được xếp như sau: Cao dành cho vấn đề …; Trung bình dành cho …; Thấp dành cho vấn đề chỉ liên quan … |
| 24 | 03-05-quality-issue-log | 9 | 3.6 Meaning (truncate = drop what follows) | Cắt tại ngày hủy đăng ký | Cắt bỏ hoạt động sau ngày hủy đăng ký |
| 25 | 03-05-quality-issue-log | 13 | 3.3 Collocation | Dấu hiệu về bài được chấm điểm | Dấu hiệu từ bài được chấm điểm |
| 26 | 03-05-quality-issue-log | 14 | 3.6 Meaning complete (unweighted) | các bài được đếm không theo trọng số | các bài được đếm như nhau, không theo trọng số |
| 27 | 03-05-quality-issue-log | 16 | 3.1 Collocation | giữ "Missing" thành một nhóm riêng | giữ "Missing" là một nhóm riêng |
| 28 | 03-05-quality-issue-log | 18 | 3.6 Meaning ("by cut-offs" = on or before) | Bài đến hạn trước thời điểm chốt | Bài đến hạn chậm nhất vào thời điểm chốt |
| 29 | 04-00-aq-data-fit | 3 | 3.4 Formal register | các trường có thật | các trường dữ liệu thực |
| 30 | 04-01-fit-ratings | 3 | 3.3 Glossary forms (claim → nhận định); 3.6 meaning | theo kết luận mà câu hỏi đó cần chứng minh | theo nhận định mà câu hỏi đó phải trả lời |
| 31 | 04-01-fit-ratings | 10 | 3.6 Meaning ("by day 27"); one form across files | bài đến hạn trước ngày 27 | bài đến hạn chậm nhất vào ngày 27 |
| 32 | 04-01-fit-ratings | 11 | 3.3 One term per concept (as Section 3.4) | 9 cặp lượt mở có ở cả hai năm | 9 cặp module – tháng bắt đầu có ở cả hai năm |
| 33 | 04-01-fit-ratings | 12 | 3.5 Economy | số lượt đăng ký học đang học | số sinh viên đang đăng ký học |
| 34 | 04-01-fit-ratings | 12 | 3.5 Head nouns (step 3 = add an open dataset) | Không có bộ dữ liệu (3) | Không có bộ dữ liệu bổ sung (3) |
| 35 | 04-01-fit-ratings | 14 | 3.5 Established words ("đo", not "đo lường") | cách đo lường các câu hỏi | cách đo các câu hỏi |
| 36 | 04-01-fit-ratings | 14 | 3.6 Meaning ("due by the cut-off not submitted") | có một bài đến hạn trước thời điểm chốt dữ liệu mà chưa nộp | có một bài đến hạn chậm nhất vào thời điểm chốt dữ liệu nhưng không được nộp |
| 37 | 04-01-fit-ratings | 14 | 3.6 Meaning (lift is over the run's base rate); 3.1 one idea per clause | mức vượt tỷ lệ nền (lift) của từng lượt mở module và bằng tỷ lệ phát hiện (recall) so với … | hai chỉ số: mức vượt tỷ lệ nền (lift), tính theo tỷ lệ nền của từng lượt mở module; tỷ lệ phát hiện (recall), so với … |
| 38 | 04-02-gap-decisions | 3 | 3.5 Written connectives ("hoặc"); 3.1 complete | điền giá trị thiếu hay sinh dữ liệu … như thể dữ liệu thật | điền giá trị thiếu hoặc sinh dữ liệu … như thể đó là dữ liệu thật |
| 39 | 04-02-gap-decisions | 11 | 3.6 Meaning (not imputed, not simulated) | Không điền giá trị hoặc mô phỏng | Không điền giá trị thiếu, không mô phỏng |
| 40 | 04-02-gap-decisions | 14 | 3.5 Economy; written connective | vì không bộ dữ liệu nào trong bảy bộ dữ liệu … hay năm theo học | vì không bộ nào trong bảy bộ dữ liệu … hoặc năm theo học |

Term for the glossary to settle: "due by day N / by the cut-off" – the twins now use "đến hạn chậm nhất vào ngày N /
vào thời điểm chốt" in Sections 3.4, 3.5 and 4.1; other groups should use the same form (not "trước ngày N", which
excludes day N).

- 03-00-profiling-quality: reviewed, 4 findings fixed, parity 0 errors 0 warnings, marked.
- 03-01-shape-keys-joins: reviewed, 6 findings fixed, parity 0 errors 0 warnings, marked.
- 03-02-missingness-validity: reviewed, 6 findings fixed, parity 0 errors 0 warnings, marked.
- 03-03-distributions-outcome: reviewed, 3 findings fixed, parity 0 errors 0 warnings, marked.
- 03-04-temporal-representativeness: reviewed, 3 findings fixed, parity 0 errors 0 warnings, marked.
- 03-05-quality-issue-log: reviewed, 6 findings fixed, parity 0 errors 0 warnings, marked.
- 04-00-aq-data-fit: reviewed, 1 finding fixed, parity 0 errors 0 warnings, marked.
- 04-01-fit-ratings: reviewed, 8 findings fixed, parity 0 errors 0 warnings, marked.
- 04-02-gap-decisions: reviewed, 3 findings fixed, parity 0 errors 0 warnings, marked.
