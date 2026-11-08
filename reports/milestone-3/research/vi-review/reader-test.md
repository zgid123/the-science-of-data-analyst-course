# Reader test – Milestone 3, Vietnamese version (stage 5)

Reader: a Vietnamese lecturer in data analytics who has not seen the source-language version. I read
`reports/milestone-3/report/01-00 … 10-00 *.vi.md` in file-name order, with the abbreviation page (00-1) and the
terms page (00-2). I ignored evidence codes and citations in square brackets. No English `.md` file and no research
file was opened.

Overall judgement: yes, a reader of the field could explain the document afterwards: what OULAD is, what was
profiled, which quality issues were found and how each was handled, how the data was split to avoid leakage, and which
questions are ready for Milestone 4. Sections 2.1, 3.2, 4.2, 6.3 (first half), 9 and 10 read well. Comprehension
breaks in three places. (a) Dense numeric sentences in 3.1, 7.1 and 8.2: several statistics are chained without
saying what each proves (the duplicate-click argument, the leakage row of Table 7.1, the "thu hẹp khoảng chênh lệch"
sentence). (b) Identifiers that are used before or without a definition in the main text: D1–D3 inside Table 1.1
before line 16, "quy tắc dấu hiệu sớm" in Table 1.1 (defined only in 4.1), "KPI phụ 1" and "KPI phụ 2" (never defined),
the numbered "bước (2)…(5)" in Table 4.1 that point to an unnumbered list in Section 4. (c) A layer of calqued terms
that are understandable once learned but never sound like a Vietnamese colleague: "lượt mở (module)", "chậm nhất vào
ngày c", "khớp" for *fit*, "vắng mặt có ghi nhận", "dòng dõi dữ liệu", "số sinh viên cán bộ liên hệ được mỗi tuần". The
collision between "cut-off date" (OU's term for the assessment due date, 2.2) and "thời điểm chốt dữ liệu" (glossary:
Cut-off) is a real trap. Counts: clarity 1 = 7, clarity 2 = 47, clarity 3 = 23 (77 passages).

## Passages

| # | File:line | Quote | What stopped me | Clarity (1–3) |
| :-- | :---- | :---- | :---- | :-- |
| 1 | 01-00:3 | "Điểm xuất phát là các câu hỏi ở trạng thái hiện tại" | "ở trạng thái hiện tại" is a calque of *current state*; a Vietnamese writer would say "các câu hỏi hiện hành" or "phiên bản mới nhất của các câu hỏi" | 3 |
| 2 | 01-01:3 | "nâng tỷ lệ hoàn thành học phần … trong các học phần trực tuyến … Milestone 2 đã chọn … OULAD … các lượt mở module" | "học phần" and "module" appear side by side with no statement that an OU module stands for a học phần; this is only explained in 7.3 (4). I wondered whether these were two different units | 2 |
| 3 | 01-01:3 | "tổng thể là các lượt mở module của OULAD trong năm 2013–2014" | "lượt mở module" is an invented term (I guessed: one offering/presentation of a module); the glossary helps, but on first reading it sounds like "number of times a module was opened" | 2 |
| 4 | 01-01:5 | "ở trạng thái hiện tại, sau các thay đổi trên và các quyết định về khoảng trống dữ liệu ở Mục 4" | sentence forward-references decisions the reader has not seen; translated word order | 3 |
| 5 | 01-01:11 | "tuần sinh viên lần đầu bỏ lỡ một bài được chấm điểm" | missing head word: "tuần [mà] sinh viên…"; reads as a noun list, not a question | 3 |
| 6 | 01-01:12 | "D2, lý do cụ thể cho D1" | D1, D2, D3 are used in the table before they are defined (line 16); I had to read ahead | 2 |
| 7 | 01-01:13 | "so với quy tắc dấu hiệu sớm, khi đánh giá trên một lượt mở về sau" | "quy tắc dấu hiệu sớm" is not defined until Section 4.1; "một lượt mở về sau" (a later run) is awkward | 2 |
| 8 | 01-01:14 | "Những lượt đăng ký học nào được xếp đầu danh sách với số lượt liên hệ tối đa mỗi tuần theo giả định, đạt mức vượt tỷ lệ nền (lift) và tỷ lệ phát hiện (recall) bao nhiêu, trên toàn bộ và theo mức khó khăn kinh tế – xã hội của khu vực cư trú và tình trạng khuyết tật" | four ideas in one cell (ranking, weekly capacity, two metrics, two subgroups); "mức vượt tỷ lệ nền" is invented; ranking "lượt đăng ký học" rather than sinh viên is odd | 2 |
| 9 | 01-01:14 | "D1; phần liên hệ được hoãn" | "phần liên hệ" (the contact part) of a question is not explained here; I guessed it means the intervention/outreach evaluation | 2 |
| 10 | 01-01:16 | "Các thay đổi C09–C13 thu hẹp cách đo các câu hỏi trên OULAD" | "thu hẹp cách đo" (narrow the way of measuring) is unnatural; "điều chỉnh/thu hẹp phạm vi đo" | 3 |
| 11 | 01-02:3 | "tám tệp của bản đề xuất Milestone 1 (nguồn của phiên bản cơ sở) cũng giữ nguyên" | "phiên bản cơ sở" sounds like a software base version; the concept (*baseline* of the project) is never explained in plain words | 2 |
| 12 | 01-02:3 | "các bảng gốc là liên kết cứng (hard link) tới chính các tệp đó và ở chế độ chỉ đọc (read-only)" | technical file-system detail; understandable but sounds translated | 3 |
| 13 | 01-02:3 | "hỗ trợ phần xếp hạng của AQ4, chứ không chỉ một phần nhỏ của bản đề xuất" | the clause "chứ không chỉ một phần nhỏ của bản đề xuất" has no clear subject; I guessed the brief's entry rule says the dataset must cover more than a small part of the proposal, but that rule is not stated | 2 |
| 14 | 01-02:3 | "bước chuẩn bị dữ liệu là có cơ sở" | "là có cơ sở" calque of *is justified*; "việc chuyển sang bước chuẩn bị dữ liệu là hợp lý" | 3 |
| 15 | 02-00:3 | "trước mọi bước khảo sát dữ liệu (profiling)" | "khảo sát" normally means a survey (questionnaire); for profiling a colleague says "lập hồ sơ dữ liệu" or "thống kê mô tả sơ bộ" | 3 |
| 16 | 02-00:3 | "đều dựa trên một phép kiểm tra tính trực tiếp trên dữ liệu" | parses as "kiểm tra tính [chất]…"; I had to reread to see "phép kiểm tra [được] tính trực tiếp trên dữ liệu" | 2 |
| 17 | 02-01:5 | "Bảng 2.1 là Bản đồ hiểu bộ dữ liệu … với từng bảng dữ liệu, bảng này cho biết" | "bảng" means both a report table and a data table in the same sentence; "Bản đồ hiểu bộ dữ liệu" is a literal name | 3 |
| 18 | 02-01:11 | "courses … độ dài lượt mở \| độ dài lượt mở \| ngày kết thúc lượt mở, tháng bắt đầu" | the same value in "Biến chính" and "Trường thời gian"; the "Vai trò trong AQ" cell names variables, not a role | 2 |
| 19 | 02-01:15 | "studentRegistration … \| các tổng thể, KPI" | plural "các tổng thể" (several populations) is unusual; I guessed "xác định tập sinh viên đang học tại mỗi mốc" | 2 |
| 20 | 02-02:3 | "bài mô tả dữ liệu gọi giá trị rút khỏi module là 'Withdrawal'" | why this matters is not said until 3.1; looks like a stray remark | 3 |
| 21 | 02-02:5 | "Ngày của bài đánh giá là ngày đến hạn của bài, mà OU gọi là cut-off date" | collides with "thời điểm chốt dữ liệu" (glossary: Cut-off) in the previous sentence; I first thought the assessment date was the data cut-off | 2 |
| 22 | 02-02:5 | "Tuy nhiên, giảng viên hướng dẫn thường chấm và trả TMA trong vòng mười ngày làm việc" | "Tuy nhiên" contrasts with nothing (previous sentence: pass mark 40); the point (scores are not known at the due date) is left to the reader | 2 |
| 23 | 02-02:5 | "trọng số bài đánh giá lệch khỏi quy tắc được mô tả trong tài liệu" | the rule itself is not stated, so the deviation cannot be judged | 2 |
| 24 | 02-03:3 | "có 18 nhóm tuổi và 29 nhóm trình độ học vấn chỉ gồm dưới 20 sinh viên" | there are only a few age groups; I had to infer this counts group × lượt mở cells | 2 |
| 25 | 03-00:3 | "từ kích thước bảng và schema đến tính đại diện" | untranslated "schema" (cấu trúc bảng/lược đồ) | 3 |
| 26 | 03-01:3 | "trong trường module_presentation_length chứ không phải length, còn kết quả … ghi là 'Withdrawn' chứ không phải 'Withdrawal'" | the subject (the documentation names differ from the files) is missing; the reader must guess why this is reported | 2 |
| 27 | 03-01:3 | "bảng chứa nhiều dòng cho 1.614.505 tổ hợp sinh viên – tài nguyên – ngày, trong đó 1.179.074 tổ hợp có số lượt nhấp khác nhau giữa các dòng" | two large numbers and a grain concept in one clause; understood after rereading | 2 |
| 28 | 03-01:3 | "số lượt nhấp bằng nhau ở 31,5% trường hợp, so với mức 24,0% kỳ vọng nếu chỉ do ngẫu nhiên; tỷ lệ này cao hơn ở diễn đàn … nhưng thấp hơn ở bài kiểm tra ngắn, nên không thể xác định nguyên nhân" | I could not reconstruct the argument: where 24,0% comes from, which hypothesis each figure supports, and why the pattern leads to "không thể xác định nguyên nhân" | 1 |
| 29 | 03-01:3 | "mỗi đặc trưng lượt nhấp có thêm một bản đối chiếu đã loại trùng để kiểm tra độ nhạy" | "bản đối chiếu" (comparison copy) for a deduplicated variant feature; plain: "phiên bản đã loại dòng trùng" | 3 |
| 30 | 03-01:3 | "các bảng được gộp trước rồi mới nối vào bảng lượt đăng ký học" | "gộp" can mean merge or aggregate; next to "nối" I first read it as merging tables; "tổng hợp (aggregate)" would be clear | 2 |
| 31 | 03-02:3 | "theo thiết kế, bộ dữ liệu thường không chứa kết quả bài thi" | "theo thiết kế … thường" – by design yet only "usually"; sounds translated | 3 |
| 32 | 03-02:5 | "58 lượt đăng ký học diễn ra sau thời hạn đăng ký hai tuần" | ambiguous: two weeks after the deadline, or after the two-week deadline after the start? | 2 |
| 33 | 03-02:5 | "dù quy định năm 2025 của OU không chấp nhận CMA nộp trễ" | a 2025 rule applied to 2013–2014 data is surprising; its relevance is clear only in 7.3 | 3 |
| 34 | 03-03:5 | "28.061 lượt đăng ký học được ghi nhận đến ngày 14 và chưa bị hủy tính đến ngày đó" | why day 14 here when the cut-offs are 13 and 27? "được ghi nhận đến ngày 14" is ambiguous (registered by day 14?) | 2 |
| 35 | 03-03:5 | "lớp nhãn ít mẫu hơn có ít nhất 92 lượt đăng ký học" | calque of *minority class*; "lớp thiểu số" is the usual term | 3 |
| 36 | 03-04:3 | "chỉ 1 trong 22 lượt mở có một TMA hoặc CMA đến hạn chậm nhất vào ngày 13" | "đến hạn chậm nhất vào ngày 13" (due on or before day 13) is a calque; "có hạn nộp trong 13 ngày đầu" or "đến hạn trước hoặc vào ngày 13" | 2 |
| 37 | 03-04:3 | "Đối với dự báo trên một lượt mở về sau, 9 cặp module và tháng bắt đầu được mở trong cả hai năm" | link between "forecast on a later run" and "9 pairs" is implicit (pairs available for train-2013/test-2014) | 2 |
| 38 | 03-05:3 | "Trung bình dành cho vấn đề làm thay đổi một thước đo theo một lượng đã biết" | "theo một lượng đã biết" – I guessed "by a quantified, bounded amount"; unclear why that makes it less severe | 2 |
| 39 | 03-05:3 | "các tuần theo kế hoạch không được sử dụng (DQ14)" | could not tell what these weeks are (planned-use weeks of resources in `vle`?) or what the issue is | 1 |
| 40 | 03-05:10 | "DQ10 … Giữ thông tin nộp trễ theo loại bài; quy tắc dùng thông tin nộp trễ TMA (C10)" | telegraphic; why only TMA is not said here | 2 |
| 41 | 03-05:18 | "Quy tắc của AQ3; KPI phụ 1" | "KPI phụ 1" is never defined in the main text; I do not know what this secondary KPI measures | 1 |
| 42 | 04-00:3 | "GREEN (hỗ trợ đầy đủ) … YELLOW … RED" | English colour labels in a Vietnamese text; "Xanh / Vàng / Đỏ" would read naturally | 3 |
| 43 | 04-01:3 | "Mỗi câu hỏi được đánh giá theo nhận định mà câu hỏi đó phải trả lời" | "nhận định mà câu hỏi phải trả lời" (the claim the question must answer) is odd; translated | 3 |
| 44 | 04-01:9 | "Suy ra bài đầu tiên bị bỏ lỡ (2); thu hẹp câu hỏi (4)" | the step numbers (2), (3), (4), (5) refer to the order in Section 4, which is written as a prose list without numbers; I had to count | 2 |
| 45 | 04-01:10 | "các lượt mở diễn ra đồng thời năm 2014" | why concurrent runs support AQ2 is not explained | 2 |
| 46 | 04-01:11 | "Phát biểu lại quy tắc (2); chỉ dùng điểm CMA (4)" | why only CMA scores (because TMA marks come back late) is not stated in this paragraph | 2 |
| 47 | 04-01:14 | "chỉ 1 trong 22 lượt mở có từ hai bài trở lên đến hạn chậm nhất vào ngày 27; vì vậy, quy tắc … được phát biểu lại thành 'có một bài đến hạn … hoặc có một TMA nộp trễ, hoặc không có hoạt động …'" | long quoted rule inside a long sentence; old and new rule must be compared in the head | 2 |
| 48 | 04-01:14 | "tỷ lệ phát hiện (recall), so với mức tối đa mà một danh sách cùng độ dài có thể đạt" | the normalisation (recall relative to the best possible list) is compressed into one clause | 2 |
| 49 | 04-02:10 | "Vắng mặt có ghi nhận \| Không có dòng lượt nhấp hoặc dòng bài nộp" | "vắng mặt" evokes class attendance, and "có ghi nhận" contradicts "no row"; I guessed "không phát sinh, tính là 0" | 2 |
| 50 | 05-00:15 | "không điền giá trị thiếu trong các bảng dữ liệu đã chuẩn bị \| … \| Chỉ điền bằng trung vị của tập huấn luyện" | "không điền" and "chỉ điền" in the same row read as a contradiction until I separated views from model matrices | 2 |
| 51 | 05-00:23 | "ma trận cho mô hình tuyến tính được khớp trên các lượt mở năm 2013" | "khớp" for *fit* (ước lượng tham số / huấn luyện); "khớp" usually means *match* elsewhere in the text | 2 |
| 52 | 05-00:24 | "Giữ làm cột kiểm tra công bằng \| Phục vụ bước kiểm tra công bằng" | the reason restates the decision (circular) | 3 |
| 53 | 06-01:3 | "Mười bước mà đề bài khuyến nghị, từ nạp và kiểm tra các tệp gốc đến lưu … [1], là các hàm trong …" | subject of three lines before the verb "là"; English sentence order | 2 |
| 54 | 06-01:9 | "chạy cả tám giai đoạn" (with "mười bước" line 3 and "năm giai đoạn" 06-00:7) | ten steps, eight stages, five stages: I could not tell how they relate | 2 |
| 55 | 06-02:7 | "các bản ghi được cập nhật về sau mà không có dấu thời gian là con đường phổ biến dẫn đến rò rỉ thông tin" | general statement; its link to OULAD (which records?) is not made | 3 |
| 56 | 06-02:19 | "Bài đến hạn chậm nhất vào ngày c, được nộp trễ nhưng vẫn chậm nhất vào ngày c" | two "chậm nhất vào" in one cell; I had to work out "due ≤ c, submitted after due date but ≤ c" | 2 |
| 57 | 06-03:12 | "Trung vị, thang đo, nhóm giá trị được khớp trên mọi lượt mở" | "nhóm giá trị được khớp" (category levels fitted) is opaque; "khớp" again | 2 |
| 58 | 06-03:19 | "Các phép biến đổi được khớp trên dữ liệu chỉ học tham số từ các lượt mở huấn luyện [11]; khi khớp lại sau khi thay đổi toàn bộ dòng kiểm thử, các tham số vẫn giữ nguyên" | I could not parse the first clause on first reading, and "thay đổi toàn bộ dòng kiểm thử" (perturbing all test rows as a check) is not recognisable as a test | 1 |
| 59 | 06-03:21 | "dùng các fold loại trừ từng lượt mở (leave-one-run-out) trong năm 2013, mỗi sinh viên chỉ nằm trong một fold" | leaving out one run per fold and keeping each student in one fold sound contradictory for students in two runs; not reconciled | 2 |
| 60 | 07-01:11 | "28.061 tại ngày 14; 28.069 tại ngày 13; 27.535 tại ngày 27" | more students at day 13 than day 14 is surprising and unexplained | 2 |
| 61 | 07-01:16 | "số lượt nhấp khác với lần đếm lại không lọc ở đúng 26.755 và 25.663 lượt đăng ký học có lượt nhấp về sau" | I could not work out what was compared, what "đúng" proves, or which number belongs to which cut-off | 1 |
| 62 | 07-02:5 | "Bảng dòng dõi dữ liệu (lineage)" | "dòng dõi" is genealogy (family line); a colleague says "nguồn gốc dữ liệu" or "truy vết dữ liệu" | 3 |
| 63 | 07-02:6 | "Bản kê phiên bản đặt tên bộ dữ liệu đã chuẩn bị là…" | "bản kê phiên bản" (version manifest) is unusual; "tệp mô tả phiên bản" | 3 |
| 64 | 07-03:6 | "còn chính sách chấm điểm của OU hiện có trong tài liệu lại ban hành năm 2025" | "hiện có trong tài liệu" is ambiguous (in the report? publicly available?) | 2 |
| 65 | 07-03:8 | "điểm CMA đã biết tại thời điểm chốt dữ liệu chỉ có ở 1,4% và 5,2% số dòng huấn luyện" | the two numbers are not tied to day 13 and day 27; I had to assume | 2 |
| 66 | 07-03:14 | "Các kịch bản về số sinh viên cán bộ liên hệ được mỗi tuần giả định mỗi cố vấn phụ trách … khoảng 20 sinh viên" | why this assumption is a residual risk is not said; the long invented phrase for *capacity* | 2 |
| 67 | 08-01:6 | "Các bảng dự báo bổ sung thời điểm chốt dữ liệu thứ hai tại ngày 13" | day 13 is the earlier cut-off, yet called "thứ hai"; I first thought it was a typo | 2 |
| 68 | 08-01:9 | "đề bài không cho phép nâng một kết quả dự báo thành kết quả chỉ định chỉ bằng lời khuyên" | "nâng … chỉ bằng lời khuyên" – I guessed: a prediction cannot be presented as prescriptive just by adding recommendations | 2 |
| 69 | 08-02:13 | "Danh sách 3 hoặc 5 trên 20" | "3 or 5 out of 20" is only explained in 7.3 (5); in the matrix it is cryptic | 2 |
| 70 | 08-02:15 | "Tại ngày 13, quy tắc này đánh dấu nhiều hơn danh sách 5 trên 20 ở 7 trong 22 lượt mở, còn tại ngày 27 là 10 lượt mở; AQ3 và AQ4 phải thu hẹp khoảng chênh lệch này" | I could not tell what "thu hẹp khoảng chênh lệch" means: shrink the rule? choose among flagged students? | 1 |
| 71 | 08-02:17 | "Cách liên hệ được chọn và hiệu quả của việc liên hệ, các phép so sánh theo năm theo học, hình thức học và mức chuyên cần, cùng tỷ lệ liên hệ kịp thời của KPI phụ 2 đều cần sổ theo dõi riêng của đợt thí điểm" | very long subject; "KPI phụ 2" undefined | 1 |
| 72 | 08-02:19 | "cách chia dữ liệu đã được xác định, biện pháp kiểm soát rò rỉ thông tin, các vấn đề chất lượng được ghi nhận" | list items missing a verb ("biện pháp kiểm soát … [đã có]") | 3 |
| 73 | 09-00:9 | "phần lớn mô hình tái tạo mức chênh lệch 5–6 điểm nghiêng về sinh viên nam" | "5–6 điểm" of what (accuracy points? percentage points of pass rate?) | 2 |
| 74 | 09-00:18 | "thông tin sức khỏe là một ví dụ về dữ liệu cá nhân nhạy cảm" | the link to the disability attribute is left implicit | 3 |
| 75 | 10-00:5 | "Các tác tử AI đảm nhận cả hai phía của mỗi lượt rà soát" | "cả hai phía" – I guessed reviewer and author are both AI; not obvious | 2 |
| 76 | 10-00:9 | "Quy định năm 2025 rằng CMA không được nộp trễ đã được kiểm tra trên dữ liệu và không được áp dụng" | "không được áp dụng" – not applied by OU in 2013–2014, or not applied by the team? | 2 |
| 77 | 10-00:21 | "bước kiểm tra rò rỉ thông tin được thiết kế để có thể báo không đạt" | the point (the test is not vacuous) is unstated; sounds translated | 3 |

Counts (77 rows): clarity 1 = 7 (rows 28, 39, 41, 58, 61, 70, 71); clarity 2 = 47; clarity 3 = 23.

## Recurring terms that feel invented or unnatural

Counts are occurrences in sections 01-00 to 10-00 (`.vi.md`), tables included.

| Term in the text | Count | What I took it to mean | Plainer word a colleague would use |
| :---- | :-- | :---- | :---- |
| lượt mở (module) | 70 | one presentation/offering of a module | "đợt mở lớp", "khóa (của module)", "kỳ học của module" |
| lượt đăng ký học | 42 | student × presentation record (enrolment) | "lượt ghi danh", "bản ghi đăng ký"; in prose often simply "sinh viên" |
| thời điểm chốt dữ liệu | 19 | prediction cut-off day (13 or 27) | acceptable, but clashes with OU's "cut-off date" (due date); "mốc dự báo" or "mốc cắt dữ liệu" |
| bảng dữ liệu đã chuẩn bị | 15 | prepared analytic view | "bảng phân tích", "bảng dữ liệu đầu ra" |
| chậm nhất vào (ngày c) | 10 | on or before day c | "trước hoặc vào ngày c", "tính đến ngày c" |
| mức khó khăn (kinh tế – xã hội của khu vực cư trú) | 9 | IMD band | "nhóm IMD", "mức nghèo/khó khăn theo khu vực" (shorter after first use) |
| gộp | 7 | aggregate (sometimes) | "tổng hợp" for aggregate; keep "gộp" only for merge |
| khớp (fit sense) | ~6 of 10 | fit a transformer/model | "ước lượng tham số", "huấn luyện", or keep "fit" |
| khảo sát (dữ liệu) | 6 | data profiling | "lập hồ sơ dữ liệu", "thống kê mô tả sơ bộ" |
| phần liên hệ (của AQ4) | 5 | outreach/intervention part of AQ4 | "phần đánh giá can thiệp (liên hệ sinh viên)" |
| tác tử | 5 | AI agent | acceptable in AI literature; "tác tử AI (agent)" at first use |
| số sinh viên cán bộ liên hệ được mỗi tuần | 4 | weekly outreach capacity | "năng lực liên hệ mỗi tuần", "hạn mức liên hệ/tuần" |
| phiên bản cơ sở | 4 | project baseline | "mốc cơ sở (baseline)", "phương án gốc" |
| mức vượt tỷ lệ nền / mức vượt | 4 | lift | "hệ số nâng (lift)" or simply "lift" |
| bản đối chiếu (đã loại trùng) | 4 | deduplicated sensitivity variant | "phiên bản đã loại dòng trùng" |
| dòng dõi dữ liệu | 3 | data lineage | "nguồn gốc dữ liệu", "truy vết dữ liệu" |
| trạng thái hiện tại (của câu hỏi) | 3 | current wording | "hiện hành", "phiên bản mới nhất" |
| vắng mặt có ghi nhận | 2 | absence of row = zero activity | "không phát sinh (ghi 0)", "không có hoạt động" |
| lớp nhãn ít mẫu hơn | 2 | minority class | "lớp thiểu số" |
| KPI phụ 1 / KPI phụ 2 | 2 | secondary KPIs (undefined) | define them once in 1.1, or name them in words |
