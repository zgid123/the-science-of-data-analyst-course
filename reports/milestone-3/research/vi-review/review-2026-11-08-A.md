# Vietnamese native review – group A (Sections 1–3), 2026-11-08

Reviewer: native-review agent (fresh reader; not the translator). Protocol: `build-report/languages/vi/review.md`, three passes per file (reader, fidelity side by side with the English, checklist of section 3). Files: 01-00 to 01-02, 02-00 to 02-03, 03-00 to 03-05.

Glossary coverage before the passes (`glossary.py --lang vi --task milestone-3 coverage --report reports/milestone-3/report`): 21 drifting concepts reported. Those touching this group: enrolment (the OULAD unit is "lượt đăng ký học" by its own row, so the 9% figure for "lượt đăng ký học phần" is expected; the group uses "lượt đăng ký học" throughout); deprivation band (full form at first use per file, short form "mức khó khăn của khu vực" after it – consistent); baseline (two concepts: "mức cơ sở" for the KPI baseline, "phiên bản cơ sở" for the Milestone 1 baseline – consistent); stand-in ("bộ dữ liệu thay thế" in 01-01 – consistent); placeholder ("ngày nộp quy ước −1" → glossary "giữ chỗ", fixed in 02-02); registration lead (fixed in 03-05 DQ13); proxy (outcome variable → "biến đại diện", fixed in 02-02). Other drifting rows (flag, gap, due by day N, capacity, govern/map/…) do not occur, or occur in their glossary form, in this group. Section 3.4 checked: "hoạt động được ghi nhận từ khoảng bốn tuần trước ngày bắt đầu đến tuần 39" matches the English.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 01-00-baseline-dataset | 3 | 3.5 Head nouns present | các bảng mà phân tích ở Milestone 4 dùng được ngay | các bảng mà các phân tích ở Milestone 4 dùng được ngay |
| 2 | 01-00-baseline-dataset | 5 | 3.5 Structure stated | Mục 1.1 nhắc lại phiên bản cơ sở và các câu hỏi ở trạng thái hiện hành; Mục 1.2 … | Cấu trúc của Mục 1 như sau: Mục 1.1 nhắc lại phiên bản cơ sở và các câu hỏi phân tích hiện hành; Mục 1.2 … |
| 3 | 01-01-baseline-aqs | 3 | 3.1 Vietnamese order (ambiguous "đủ sớm") | nhận ra những sinh viên ngừng tham gia học tập đủ sớm để kịp hỗ trợ | sớm nhận ra những sinh viên ngừng tham gia học tập để kịp hỗ trợ |
| 4 | 01-01-baseline-aqs | 3 | 3.1 Voice with intent (actor named) | Mức cơ sở sẽ được đợt thí điểm đếm lại từ hồ sơ của trường và hiện được giả định là 70%. | Mức cơ sở hiện được giả định là 70%; đợt thí điểm sẽ đếm lại mức này từ hồ sơ của trường. |
| 5 | 01-01-baseline-aqs | 5 | 3.2 Every sentence linked (dangling "mà") | quy tắc dấu hiệu sớm, mà ở Milestone 1 có nội dung "…" | quy tắc dấu hiệu sớm; ở Milestone 1, quy tắc này là "…" |
| 6 | 01-01-baseline-aqs | 5 | 3.6 Meaning complete ("hiện trường" reads as "the scene") | hiện trường chưa có sổ này | trường hiện chưa có sổ này |
| 7 | 01-01-baseline-aqs | 7 | 3.5 Head nouns present; collocation | hết tuần 2 với danh sách tuần 3 …, vì việc xuất dữ liệu mất khoảng một tuần | hết tuần 2 cho danh sách tuần 3 …, vì khâu xuất dữ liệu mất khoảng một tuần |
| 8 | 01-01-baseline-aqs | 9 | 3.6 Meaning complete ("Milestone này" read as Milestone 3) | vốn chưa thể sử dụng. Milestone này cũng ghi tám thay đổi | vốn hiện chưa dùng được. Milestone 2 cũng ghi tám thay đổi |
| 9 | 01-01-baseline-aqs | 9 | 3.5 Punctuation (semicolons in enumeration) | … theo module và kỳ mở, bỏ dấu hiệu điểm danh, tính từ một bài … trong quy tắc dấu hiệu sớm khi áp dụng trên OULAD và để … | … theo module và kỳ mở; bỏ dấu hiệu điểm danh; tính từ một bài bỏ lỡ hoặc nộp trễ khi áp dụng quy tắc dấu hiệu sớm trên OULAD; và để … |
| 10 | 01-01-baseline-aqs | 19 | 3.1 One clear actor (data "estimates") | dữ liệu tính đến hết tuần 2 và hết tuần 4 ước lượng việc không hoàn thành tốt đến mức nào | việc không hoàn thành được ước lượng tốt đến mức nào từ dữ liệu tính đến hết tuần 2 và hết tuần 4 |
| 11 | 01-01-baseline-aqs | 20 | 3.1 Vietnamese order ("assumed capacity") | danh sách có độ dài theo số sinh viên cán bộ liên hệ được (giả định) | danh sách có độ dài bằng số sinh viên cán bộ liên hệ được theo giả định |
| 12 | 01-02-dataset-entry-gate | 5 | 3.3 Glossary forms (pinned value); 3.5 parentheses for side information | giá trị SHA-256 đã ghi sẵn …; tám tệp của bản đề xuất Milestone 1, nơi phiên bản cơ sở được sao chép ra, | giá trị SHA-256 tham chiếu ghi sẵn …; tám tệp của bản đề xuất Milestone 1 (nguồn sao chép phiên bản cơ sở) |
| 13 | 02-00-data-understanding | 3 | 3.5 Written connectives | (profiling) hay làm sạch | (profiling) hoặc làm sạch |
| 14 | 02-00-data-understanding | 3 | 3.5 Plain actions over images ("frame") | Một số thông tin về OU làm khung cho phần mô tả này. | Phần mô tả này dựa trên một số thông tin cơ bản về OU. |
| 15 | 02-00-data-understanding | 5 | 3.5 Structure stated | Trên cơ sở các thông tin này, Mục 2.1 …; Mục 2.3 … | Trên cơ sở các thông tin này, cấu trúc của Mục 2 như sau: Mục 2.1 …; và Mục 2.3 … |
| 16 | 02-00-data-understanding | 5 | 3.6 Meaning complete ("tính trực tiếp" reads as "directness") | dựa trên một phép kiểm tra tính trực tiếp trên dữ liệu | dựa trên kết quả của một phép kiểm tra chạy trên dữ liệu |
| 17 | 02-00-data-understanding | 5 | 3.2 Every sentence linked | ghi kết quả các phép kiểm tra đó vào | ghi các kết quả này vào |
| 18 | 02-01-population-unit-keys | 3 | 3.6 Meaning complete ("học lại" adds retake) | học lại cùng module ở một kỳ mở sau | đăng ký cùng module ở một kỳ mở sau |
| 19 | 02-01-population-unit-keys | 3 | 3.1 Complete (students compared with courses) | Sinh viên OU học từ xa, khác với các học phần trực tuyến … | Hình thức học từ xa của sinh viên OU khác với các học phần trực tuyến … |
| 20 | 02-01-population-unit-keys | 5 | 3.5 Head nouns present | trước khi nối (Mục 6.2) | trước khi nối bảng (Mục 6.2) |
| 21 | 02-02-outcome-time-measures | 3 | 3.1 One clear actor; 3.3 glossary (proxy variable) | Đây là kết quả thực chứ không phải chỉ số đại diện | Biến final_result là kết quả thực chứ không phải biến đại diện |
| 22 | 02-02-outcome-time-measures | 5 | 3.5 Parentheses for side information | ngày đến hạn của bài, OU gọi là cut-off date [2] | ngày đến hạn của bài (OU gọi là cut-off date) [2] |
| 23 | 02-02-outcome-time-measures | 7 | 3.5 Plain actions ("trở thành") | trước khi các trường trở thành thước đo | trước khi dùng các trường làm thước đo |
| 24 | 02-02-outcome-time-measures | 7 | 3.3 Glossary forms (placeholder) | ngày nộp quy ước −1 | ngày nộp giữ chỗ −1 |
| 25 | 02-02-outcome-time-measures | 7 | 3.1 Relational wording | , với 60 tín chỉ một năm là học bán thời gian và 120 tín chỉ là học toàn thời gian | , trong đó 60 tín chỉ một năm tương ứng với học bán thời gian và 120 tín chỉ với học toàn thời gian |
| 26 | 02-03-codes-sensitive | 3 | 3.5 No empty words | Trường mức khó khăn này, imd_band, ghi nhóm mà khu vực nơi sinh viên cư trú thuộc về theo … | Trường imd_band ghi nhóm của khu vực sinh viên cư trú theo … |
| 27 | 02-03-codes-sensitive | 5 | 3.3 Glossary forms (the team → nhóm tác giả) | Đề bài yêu cầu nhóm xác định | Đề bài yêu cầu nhóm tác giả xác định |
| 28 | 03-00-profiling-quality | 3 | 3.5 Head nouns present | script thứ hai của gói | script thứ hai của Gói dữ liệu đã chuẩn bị |
| 29 | 03-00-profiling-quality | 3 | 3.3 Formal register | cả mười ba số liệu đều trùng khớp | cả mười ba số liệu đều khớp nhau |
| 30 | 03-00-profiling-quality | 5 | 3.5 Structure stated; 3.1 collocation | Mục 3.1 đến Mục 3.4 …; mỗi phát hiện cần ra quyết định được gán … DQ19. Mục 3.5 … | Cấu trúc của Mục 3 như sau: Mục 3.1 đến Mục 3.4 …, trong đó mỗi phát hiện cần quyết định xử lý được gán … DQ19; Mục 3.5 … |
| 31 | 03-01-shape-keys-joins | 3 | 3.6 Meaning complete ("expected by chance") | so với 24,0% nếu chỉ do ngẫu nhiên | so với mức kỳ vọng 24,0% nếu chỉ do ngẫu nhiên |
| 32 | 03-02-missingness-validity | 5 | 3.3 One term per concept ("điểm" clashes with score) | sáu điểm không nhất quán | sáu loại không nhất quán |
| 33 | 03-02-missingness-validity | 5 | 3.6 Meaning complete (window ends two weeks after start) | sau thời hạn đăng ký (hai tuần đầu kỳ mở) | sau thời hạn đăng ký (hai tuần sau ngày bắt đầu kỳ mở) |
| 34 | 03-02-missingness-validity | 5 | 3.6 Meaning complete ("and" of the last item) | (DQ10); một nhãn khoảng | (DQ10); và một nhãn khoảng |
| 35 | 03-02-missingness-validity | 5 | 3.1 One clear actor; ambiguity with score | Không điểm nào được sửa bằng cách thay đổi giá trị đã ghi; mỗi điểm được gắn một cờ hoặc một quy tắc ở Mục 5. | Nhóm tác giả không sửa loại không nhất quán nào bằng cách thay đổi giá trị đã ghi; mỗi loại được gắn một cờ hoặc xử lý bằng một quy tắc ở Mục 5. |
| 36 | 03-03-distributions-outcome | 3 | 3.5 Head nouns present | Hoạt động có phân phối lệch mạnh. | Hoạt động trên nền tảng học tập có phân phối lệch mạnh. |
| 37 | 03-03-distributions-outcome | 3 | 3.5 Parentheses for side information | ngưỡng trên theo khoảng tứ phân vị, là ranh giới thống kê … ngoại lai; | ngưỡng trên theo khoảng tứ phân vị (ranh giới thống kê … ngoại lai); |
| 38 | 03-03-distributions-outcome | 3 | 3.1 Collocations | các mô hình nhạy với thang đo nhận logarit của số lượt nhấp | các mô hình nhạy với thang đo dùng logarit của số lượt nhấp làm đầu vào |
| 39 | 03-03-distributions-outcome | 3 | 3.1 One main idea; complete subject | Có 45,8% điểm CMA là bội số của mười, so với 17,4% điểm TMA, cho thấy bước chấm điểm khá thô; khối lượng học lên tới 655 tín chỉ, | Tỷ lệ điểm là bội số của mười đạt 45,8% ở CMA, so với 17,4% ở TMA; chênh lệch này cho thấy bước chấm điểm khá thô. Ngoài ra, số tín chỉ đang học lên tới 655, |
| 40 | 03-03-distributions-outcome | 5 | 3.5 No empty words ("lượt đăng ký học đã đăng ký") | 28.061 lượt đăng ký học đã đăng ký tính đến hết ngày 14 | 28.061 lượt đăng ký học có ngày đăng ký tính đến hết ngày 14 |
| 41 | 03-03-distributions-outcome | 5 | 3.2 Every sentence linked (reference word) | 54,7% hoàn thành. Đây là giá trị của OULAD | 54,7% hoàn thành. Tỷ lệ này là giá trị của OULAD |
| 42 | 03-04-temporal-representativeness | 3 | 3.2 Connectors accurate | Riêng hai ngày gần cuối cả sáu kỳ mở tháng 2 năm 2014 | Ngoài ra, hai ngày gần cuối của cả sáu kỳ mở tháng 2 năm 2014 |
| 43 | 03-04-temporal-representativeness | 3 | 3.6 Meaning complete (hypothetical "would") | một quy tắc đếm bài bỏ lỡ không có bài nào để đếm | một quy tắc đếm bài bỏ lỡ sẽ không có bài nào để đếm |
| 44 | 03-04-temporal-representativeness | 3 | 3.5 Head nouns / time phrase | chỉ được mở năm 2014 | chỉ được mở trong năm 2014 |
| 45 | 03-04-temporal-representativeness | 3 | 3.1 Complete (subjectless "chỉ biết được") | chỉ biết được những lượt rút khỏi module có ngày rút tính đến hết thời điểm đó [8] | chỉ những lượt rút khỏi module có ngày rút tính đến hết thời điểm đó mới được biết [8] |
| 46 | 03-04-temporal-representativeness | 5 | 3.1 One main idea | , bị thu hẹp do quá trình ẩn danh hóa, với các module được chọn một phần vì nhiều sinh viên không đạt | , bị thu hẹp do quá trình ẩn danh hóa; các module được chọn một phần vì có nhiều sinh viên không đạt |
| 47 | 03-05-quality-issue-log | 3 | 3.6 Meaning complete ("judged against the questions") | được đánh giá theo các câu hỏi | được đánh giá theo tác động đến các câu hỏi phân tích |
| 48 | 03-05-quality-issue-log | 3 | 3.1 Complete (bare labels as subjects) | Cao dành cho …; Trung bình dành cho …; Thấp dành cho … | Mức Cao dành cho …; mức Trung bình dành cho …; mức Thấp dành cho … |
| 49 | 03-05-quality-issue-log | 3 | 3.1 Relational wording | toàn bộ bằng chứng, với mục trong kết quả khảo sát dữ liệu làm căn cứ | toàn bộ bằng chứng, kèm mục tương ứng trong kết quả khảo sát dữ liệu làm căn cứ |
| 50 | 03-05-quality-issue-log | 13 | 3.4 Definitions (rule stated as a term) | Đang đăng ký học vào ngày d đòi hỏi đã đăng ký đến ngày d (C09) | Điều kiện "đang đăng ký học vào ngày d" đòi hỏi đã đăng ký tính đến hết ngày d (C09) |
| 51 | 03-05-quality-issue-log | 14 | 3.3 Formal register | Rời đi trước khi bắt đầu giảng dạy | Rút trước khi bắt đầu giảng dạy |
| 52 | 03-05-quality-issue-log | 15 | 3.6 Meaning complete ("never timed") | Không dùng để tính thời điểm; đếm là kết quả bảo lưu, biết được từ lúc đăng ký | Không dùng để xác định thời điểm nộp; đếm riêng là kết quả bảo lưu, đã biết từ lúc đăng ký |
| 53 | 03-05-quality-issue-log | 21 | 3.3 Glossary forms (registration lead) | Đặc trưng thời gian đăng ký trước ngày bắt đầu | Đặc trưng khoảng cách từ ngày đăng ký đến ngày bắt đầu |
| 54 | 03-05-quality-issue-log | 25 | 3.3 Glossary forms (inner join) | Phép nối trong sẽ loại các lượt này | Nối trong (inner join) sẽ loại các lượt này |
| 55 | 03-05-quality-issue-log | 29 | 3.1 Formal openers (calque "Với") | Với kết quả bài thi bị thiếu (DQ08), | Đối với kết quả bài thi bị thiếu (DQ08), |
| 56 | 03-05-quality-issue-log | 29 | 3.2 Connectors accurate (cause) | Với số ít bài đến hạn tính đến các thời điểm chốt dữ liệu (DQ18), | Do chỉ có ít bài đến hạn tính đến các thời điểm chốt dữ liệu (DQ18), |

Terms for the glossary to settle: (1) "inconsistency" as a counted finding – "điểm không nhất quán" collides with "điểm" (score) in a section about scores; this group uses "loại không nhất quán"/"trường hợp không nhất quán"; a row would fix it report-wide. (2) "registration window / sign-up window" – no row; rendered "thời hạn đăng ký (hai tuần sau ngày bắt đầu kỳ mở)". (3) "study load" (studied credits) – rendered "số tín chỉ đang học"; a row would stop "khối lượng học" returning.

- 01-00-baseline-dataset: reviewed, 2 findings fixed, parity 0 errors, 0 warnings.
- 01-01-baseline-aqs: reviewed, 9 findings fixed, parity 0 errors, 0 warnings.
- 01-02-dataset-entry-gate: reviewed, 1 finding fixed, parity 0 errors, 0 warnings.
- 02-00-data-understanding: reviewed, 5 findings fixed, parity 0 errors, 0 warnings.
- 02-01-population-unit-keys: reviewed, 3 findings fixed, parity 0 errors, 0 warnings.
- 02-02-outcome-time-measures: reviewed, 5 findings fixed, parity 0 errors, 0 warnings.
- 02-03-codes-sensitive: reviewed, 2 findings fixed, parity 0 errors, 0 warnings.
- 03-00-profiling-quality: reviewed, 3 findings fixed, parity 0 errors, 0 warnings.
- 03-01-shape-keys-joins: reviewed, 1 finding fixed, parity 0 errors, 0 warnings.
- 03-02-missingness-validity: reviewed, 4 findings fixed, parity 0 errors, 0 warnings.
- 03-03-distributions-outcome: reviewed, 6 findings fixed, parity 0 errors, 0 warnings.
- 03-04-temporal-representativeness: reviewed, 5 findings fixed, parity 0 errors, 0 warnings.
- 03-05-quality-issue-log: reviewed, 10 findings fixed, parity 0 errors, 0 warnings.

All 13 twins marked translated with `translation_status.py --mark` (recorded in `reports/milestone-3/report/.vi-sync.json`; status: 41 sections, 0 need translation).
