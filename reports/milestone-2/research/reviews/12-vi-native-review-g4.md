# Native review G4 of the rewritten twins (11-01 to 11-06, appendices)

Reviewer: native-review agent, 2026-11-07 (UTC). Three passes per file (review.md section 2), against rewrite2-brief.md.
Coverage before the passes (`glossary.py --lang vi --task milestone-2 coverage --report reports/milestone-2/report`): 8 drifting
concepts. In this group only "enrolment (OULAD unit)" needed changes: "lượt đăng ký" became "lượt đăng ký học" in Table A.7, C03.
"due by day N" (the row's literal N never matches), "capacity (Milestone 4)", "reviewer / sparring partner" (11-06 uses the row
"selection reviewer"), "gate (S1)" (11-02 uses "must-have gate"), "gap" (11-02 uses "khoảng trống dữ liệu") and "baseline / target"
(already in Table A.10) needed none. Edits were applied by a script requiring each Before to occur exactly once. Code fences
were diffed against the English (identical); URLs, DOIs, hashes and identifiers were compared by script (identical).

Rulings on the additions the brief lists for this group:

| Addition | File | Ruling | Reason |
| :---- | :---- | :---- | :---- |
| "để đánh giá" in C07 | 11-05 | Kept, wording aligned to "kỳ mở sau" | 07-02 says these runs "can test a model" but cannot train one |
| "trợ lý AI tự thực hiện nhiều bước" | 11-06 | Removed | Not in the English or elsewhere in the report |
| "theo giả định, từ mức cơ sở 70% lên mức mục tiêu 75%" | 11-05 | Kept, verb "tăng" added, "vào cuối" → "đến cuối" | 01-01 states the same baseline and target; "by end" is a deadline |
| "Mục 6" for "Task 6" | 11-02 | Kept | The structural check is Section 6 (05-00, 07-00); "Task 6" stays in the code fence of 11-03 |

Addition found outside the brief: "tháng 2 (B) và tháng 10 (J)" in C07 (English "B and J runs"). Kept, as 06-00 states the months.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| R4-1 | 11-01-search-log.vi.md | 9 | Head noun; list of parallel nouns | Bậc đại học; có kết quả ở cấp module, trong đó có rút khỏi module; có bài được chấm điểm kèm ngày và số lượt nhấp | Bậc đại học; kết quả theo từng module, gồm cả rút khỏi module; bài được chấm điểm có ngày và số lượt nhấp |
| R4-2 | 11-01-search-log.vi.md | 9 | Clear actor | theo tài liệu, ứng viên đạt G2a, G2b và G4 | tài liệu cho thấy ứng viên đạt G2a, G2b và G4 |
| R4-3 | 11-01-search-log.vi.md | 13 | Head noun present | Tìm theo tên bài "Predicting | Tìm theo tên bài báo "Predicting |
| R4-4 | 11-01-search-log.vi.md | 19 | Head noun present | Tìm theo tên bài "Understanding | Tìm theo tên bài báo "Understanding |
| R4-5 | 11-01-search-log.vi.md | 14 | Plain wording; stacked noun | bản trên Zenodo là bản sao của chính nhóm tác giả, cùng dữ liệu (nhóm phân tích dữ liệu dùng trang UCI) | bản trên Zenodo do chính các tác giả đăng và có cùng dữ liệu (nhóm dùng trang UCI) |
| R4-6 | 11-01-search-log.vi.md | 18 | Translated pattern ('đối với') | Bản sao của bên thứ ba đối với dữ liệu KDD Cup 2015 | Bản sao dữ liệu KDD Cup 2015 do bên thứ ba đăng |
| R4-7 | 11-01-search-log.vi.md | 18 | Plain wording; hedge kept | trang chính thức của KDD Cup được cho là không còn truy cập được | có nguồn cho biết trang chính thức của KDD Cup đã ngừng hoạt động |
| R4-8 | 11-01-search-log.vi.md | 19 | Collocation ('source paper' of a dataset) | Bài báo gốc của XuetangX | Bài báo gốc về dữ liệu XuetangX |
| R4-9 | 11-01-search-log.vi.md | 21 | Head noun present | Tin công bố, blog, script | Tin công bố dữ liệu, blog, script |
| R4-10 | 11-01-search-log.vi.md | 23 | Vietnamese order | Thay thế cho trang bị chặn của Đại học Jordan | Thay cho trang của Đại học Jordan bị chặn |
| R4-11 | 11-02-scoring-details.vi.md | 9 | One term per concept (phần câu hỏi, as 02-01); list | nhưng một số phần của câu hỏi chỉ đạt mức Một phần (không có hình thức học, năm theo học, chuyên cần) | nhưng một số phần câu hỏi chỉ đạt mức Một phần (không có hình thức học, năm theo học và chuyên cần) |
| R4-12 | 11-02-scoring-details.vi.md | 9 | Fragment made a clause | 0 – một khoảng điểm | 0 – chỉ có một khoảng điểm |
| R4-13 | 11-02-scoring-details.vi.md | 10 | English kept only where needed (Vương quốc Anh, as 01-02) | đào tạo từ xa, UK; | đào tạo từ xa, Vương quốc Anh; |
| R4-14 | 11-02-scoring-details.vi.md | 10 | Brief 15 (học sinh); plain wording | 0 – người dùng hệ thống quản lý học tập ở bậc phổ thông | 0 – học sinh phổ thông dùng hệ thống quản lý học tập |
| R4-15 | 11-02-scoring-details.vi.md | 12 | Collocation | 1 – có ghi rút khỏi module kèm ngày | 1 – có ghi nhận rút khỏi module kèm ngày |
| R4-16 | 11-02-scoring-details.vi.md | 14 | Head noun present ('ordered by code') | xếp được theo mã | xếp được thứ tự theo mã |
| R4-17 | 11-02-scoring-details.vi.md | 17 | Stacked nouns | 10,7 triệu dòng lượt nhấp | 10,7 triệu dòng dữ liệu lượt nhấp |
| R4-18 | 11-03-acquisition-package.vi.md | 3 | Exhibit introduced right before the block; colon | Cấu trúc của gói được trình bày dưới đây. Các tệp gốc do script thu thập tạo ra và được giữ nguyên, không chỉnh sửa. | Các tệp gốc do script thu thập tạo ra và được giữ nguyên, không chỉnh sửa. Cấu trúc của gói như sau: |
| R4-19 | 11-03-acquisition-package.vi.md | 24 | Time word | trả về lỗi HTTP 404 ngày 05/11/2026 | trả về lỗi HTTP 404 vào ngày 05/11/2026 |
| R4-20 | 11-03-acquisition-package.vi.md | 26 | Head noun present | ghi "phiên bản mới nhất" nhưng không có số | ghi "phiên bản mới nhất" nhưng không nêu số phiên bản |
| R4-21 | 11-03-acquisition-package.vi.md | 30 | 'Mục' reserved for sections; plain wording | (mục đầy đủ trong citation.bib) | (thông tin đầy đủ trong citation.bib) |
| R4-22 | 11-03-acquisition-package.vi.md | 32 | Reference clear ('bảng' clashed with Bảng A.4) | Từng bảng đều khớp với giá trị | Mỗi bảng dữ liệu đều khớp với giá trị |
| R4-23 | 11-04-structure-details.vi.md | 17 | Verbs over stacked nouns; verb fits each object | Bảng A.7 cho biết các số đếm dùng để kết luận về ba điều kiện G1, G3 và G5, về ngày đến hạn của các bài đầu tiên và về mẫu số của KPI. | Bảng A.7 nêu các số đếm dùng để kết luận về ba điều kiện G1, G3 và G5, để xác định ngày đến hạn của các bài đầu tiên và để tính mẫu số của KPI. |
| R4-24 | 11-04-structure-details.vi.md | 19 | Economy (caption) | **Bảng A.7. Các số đếm làm căn cứ cho các điều kiện đi kèm quyết định chọn OULAD và cho mẫu số của KPI** | **Bảng A.7. Số đếm làm căn cứ cho các điều kiện đi kèm quyết định chọn OULAD và mẫu số của KPI** |
| R4-25 | 11-04-structure-details.vi.md | 24 | Head noun present | Withdrawn có / không có ngày hủy đăng ký; các kết quả khác có ngày hủy đăng ký | Kết quả Withdrawn có / không có ngày hủy đăng ký; các kết quả khác có ngày này |
| R4-26 | 11-04-structure-details.vi.md | 26 | Plain wording; subset stated | Số trường hợp học lại cùng một module; số trường hợp có số lần học trước tăng lên | Số trường hợp học lại cùng module; trong đó, số trường hợp ghi số lần học trước cao hơn |
| R4-27 | 11-04-structure-details.vi.md | 31 | Glossary: enrolment (OULAD) = lượt đăng ký học; stacked nouns | Số lượt đăng ký đã hủy vào hoặc trước ngày 0; số lượt đăng ký sau ngày 14; số lượt thiếu ngày đăng ký | Số lượt đăng ký học: hủy vào hoặc trước ngày 0; đăng ký sau ngày 14; thiếu ngày đăng ký |
| R4-28 | 11-04-structure-details.vi.md | 32 | Glossary: lượt đăng ký học | Số lượt đăng ký còn hiệu lực vào ngày 14 | Số lượt đăng ký học còn hiệu lực vào ngày 14 |
| R4-29 | 11-04-structure-details.vi.md | 33 | Stacked 'của'; meaning of the two click checks | (bài được chấm điểm, bài nộp, lượt đăng ký của lượt nhấp, tài nguyên học tập của lượt nhấp) | (bài được chấm điểm, bài nộp, lượt nhấp đối chiếu với lượt đăng ký học, lượt nhấp đối chiếu với tài nguyên học tập) |
| R4-30 | 11-05-change-log.vi.md | 3 | Clear subject; given before new | nhờ đó có thể phát hiện mọi chỉnh sửa về sau trên các tệp này | nhờ đó mọi chỉnh sửa về sau trên các tệp này đều có thể bị phát hiện |
| R4-31 | 11-05-change-log.vi.md | 18 | Collocation (tác động đến, as 01-02) | bằng chứng dữ liệu và tác động lên các AQ, KPI và quyết định | bằng chứng dữ liệu và tác động đến các AQ, KPI và quyết định |
| R4-32 | 11-05-change-log.vi.md | 22 | Collocation (tác động đến) | Tác động lên AQ / KPI / quyết định | Tác động đến AQ / KPI / quyết định |
| R4-33 | 11-05-change-log.vi.md | 24 | English kept only where needed; plain action | (Open University, UK, đào tạo từ xa, 2013–2014) là bộ dữ liệu mở thay thế để phân tích; đợt thí điểm vẫn nhắm đến dữ liệu của chính trường | (Open University, Vương quốc Anh, đào tạo từ xa, 2013–2014) là bộ dữ liệu mở thay thế để phân tích; đợt thí điểm vẫn dùng dữ liệu của chính trường |
| R4-34 | 11-05-change-log.vi.md | 25 | No 'một' where the count does not matter | được nêu rõ là một giới hạn | được nêu rõ là giới hạn |
| R4-35 | 11-05-change-log.vi.md | 26 | Glossary: lượt đăng ký học | Các lượt đăng ký còn hiệu lực vào ngày 14 | Các lượt đăng ký học còn hiệu lực vào ngày 14 |
| R4-36 | 11-05-change-log.vi.md | 26 | Plain wording | không có cột tình trạng học tập nào ghi tạm ngừng học hoặc chuyển chương trình đào tạo | không có cột nào ghi tình trạng tạm ngừng học hoặc chuyển chương trình đào tạo |
| R4-37 | 11-05-change-log.vi.md | 26 | Glossary: lượt đăng ký học; one wording (phần sai khác, as Q3) | tính trên 28.119 lượt đăng ký; phần khác với quy định của Thông tư 83 được ghi nhận | tính trên 28.119 lượt đăng ký học; phần sai khác so với quy định của Thông tư 83 được ghi nhận |
| R4-38 | 11-05-change-log.vi.md | 27 | Plain wording | mọi module đều đào tạo từ xa | mọi module đều theo hình thức đào tạo từ xa |
| R4-39 | 11-05-change-log.vi.md | 29 | Plain wording | bắt đầu có từ danh sách tuần 5 | bắt đầu được dùng từ danh sách tuần 5 |
| R4-40 | 11-05-change-log.vi.md | 30 | One term (kỳ mở sau, as 07-01); brief addition kept, supported by 07-02 | chỉ dùng làm kỳ mở muộn hơn để đánh giá | chỉ dùng làm kỳ mở sau để đánh giá |
| R4-41 | 11-05-change-log.vi.md | 30 | Unit: OULAD runs, as 07-02 | Đánh giá trên học kỳ sau (huấn luyện trên các học kỳ trước) là khả thi, nhưng mỗi cặp chỉ có một kỳ mở sớm hơn | Đánh giá trên kỳ mở sau (huấn luyện trên các kỳ mở trước) là khả thi, nhưng mỗi cặp chỉ có một kỳ mở trước đó |
| R4-42 | 11-05-change-log.vi.md | 31 | Collocation | không đưa ra nhận định chỉ định hoặc nhân quả | không đưa ra nhận định mang tính chỉ định hoặc nhân quả |
| R4-43 | 11-05-change-log.vi.md | 39 | Verb added to the brief's kept addition; 'by' = đến | Tỷ lệ hoàn thành học phần ở các học phần thí điểm, theo giả định từ mức cơ sở 70% lên mức mục tiêu 75% vào cuối năm học 2027–2028 (KPI chính) | Tỷ lệ hoàn thành học phần ở các học phần thí điểm, theo giả định tăng từ mức cơ sở 70% lên mức mục tiêu 75% đến cuối năm học 2027–2028 (KPI chính) |
| R4-44 | 11-05-change-log.vi.md | 41 | One term (kỳ mở sau, as 07-01) | một kỳ mở muộn hơn để đánh giá | kỳ mở sau để đánh giá |
| R4-45 | 11-05-change-log.vi.md | 42 | Meaning complete ('within capacity') | Xếp hạng theo số sinh viên cán bộ liên hệ được mỗi tuần; | Xếp hạng trong giới hạn số sinh viên cán bộ liên hệ được mỗi tuần; |
| R4-46 | 11-06-ai-evidence.vi.md | 3 | Addition removed (gloss not in the English); translated 'tức' apposition; active voice; one actor | Một tác tử AI (AI agent), tức trợ lý AI tự thực hiện nhiều bước, tìm các bộ dữ liệu ứng viên cho nhóm phân tích dữ liệu theo prompt dưới đây. Trong prompt, mỗi tài liệu được gọi theo mục của báo cáo chứa tài liệu đó và các bước xử lý tệp của tác tử được lược bỏ. | Một tác tử AI (AI agent) tìm các bộ dữ liệu ứng viên cho nhóm phân tích dữ liệu theo prompt dưới đây. Prompt này gọi tên tài liệu theo mục tương ứng của báo cáo và lược bỏ các bước xử lý tệp của tác tử. |
| R4-47 | 11-06-ai-evidence.vi.md | 22 | Clear actor; verb fits ('làm việc' twice) | AI phản biện yêu cầu làm việc trước khi có bộ dữ liệu nào được chấm điểm, còn AI phản biện lựa chọn làm việc sau khi chấm điểm xong. | AI phản biện yêu cầu nhận xét trước khi nhóm chấm điểm bộ dữ liệu nào, còn AI phản biện lựa chọn nhận xét sau khi nhóm chấm điểm xong. |
| R4-48 | 11-06-ai-evidence.vi.md | 22 | Stacked relative clause; same wording as paragraph 1 | Các prompt được giữ nguyên bằng tiếng Anh, trong đó mỗi tài liệu được gọi theo mục của báo cáo chứa tài liệu đó. | Các prompt giữ nguyên tiếng Anh và gọi tên tài liệu theo mục tương ứng của báo cáo. |
| R4-49 | 11-06-ai-evidence.vi.md | 22 | Economy | tóm tắt từng nhận xét phản biện, kèm quyết định | tóm tắt từng nhận xét, kèm quyết định |
| R4-50 | 11-06-ai-evidence.vi.md | 43 | One term (phần câu hỏi, as 02-01) | Những phần của câu hỏi chỉ đạt mức Một phần khi thiếu hai biến này | Những phần câu hỏi chỉ đạt mức Một phần khi thiếu hai biến này |
| R4-51 | 11-06-ai-evidence.vi.md | 44 | One term (kỳ mở sau); plain wording | ba kỳ mở học phần xếp được theo thời gian, trong đó có một kỳ mở muộn hơn để đánh giá | ba kỳ mở học phần xếp được thứ tự thời gian, trong đó có kỳ mở sau để đánh giá |
| R4-52 | 11-06-ai-evidence.vi.md | 48 | Plain wording (identifier fixed across tables) | mã định danh sinh viên dạng bí danh, không đổi giữa các bảng | mã định danh sinh viên dạng bí danh, cố định giữa các bảng |
| R4-53 | 11-06-ai-evidence.vi.md | 49 | Established word (volume of data) | Không có yêu cầu về số lượng dữ liệu hoặc phân bố kết quả | Không có yêu cầu về khối lượng dữ liệu hoặc phân bố kết quả |
| R4-54 | 11-06-ai-evidence.vi.md | 50 | Stacked passive; named actor | Số sinh viên cán bộ liên hệ được mỗi tuần được ghi là giả định của phiên bản cơ sở. | Phiên bản cơ sở ghi số sinh viên cán bộ liên hệ được mỗi tuần là giả định. |
| R4-55 | 11-06-ai-evidence.vi.md | 51 | One term (field = cột) | Cách diễn đạt nêu tên trường dữ liệu hoặc tên hệ thống | Cách diễn đạt nêu tên cột dữ liệu hoặc tên hệ thống |
| R4-56 | 11-06-ai-evidence.vi.md | 69 | Brief 16; head noun | Chấp nhận \| Quyết định chọn phụ thuộc vào bước kiểm tra cấu trúc ban đầu; nêu rõ phương án dự phòng | Chấp nhận \| Quyết định chọn OULAD phụ thuộc vào kết quả kiểm tra cấu trúc ban đầu; nêu rõ phương án dự phòng |
| R4-57 | 11-06-ai-evidence.vi.md | 70 | Brief 16; head noun | Chấp nhận \| Quyết định chọn phụ thuộc vào bước kiểm tra cấu trúc ban đầu; nêu rõ các phần chỉ đạt mức Một phần | Chấp nhận \| Quyết định chọn OULAD phụ thuộc vào kết quả kiểm tra cấu trúc ban đầu; nêu rõ các phần câu hỏi chỉ đạt mức Một phần |
| R4-58 | 11-03-acquisition-package.vi.md | 38–45 | English kept only where needed (value label) | MATCH (8 rows) | Khớp (8 rows) |
| R4-59 | 11-03-acquisition-package.vi.md | 53–59 | Numbers (dot for thousands); value labels in Vietnamese | True / False; 5690310; 173912; (22560 dòng) (7 rows) | Có / Không; 5.690.310; 173.912; (22.560 dòng) (7 rows) |

- 11-01-search-log.vi.md: reviewed, 10 findings fixed, parity 0 errors, 2 warnings (the word 'dataset' inside verbatim search queries and a URL: justified).
- 11-02-scoring-details.vi.md: reviewed, 7 findings fixed, parity 0 errors, 0 warnings.
- 11-03-acquisition-package.vi.md: reviewed, 7 findings fixed, parity 0 errors, 1 warning (the word 'dataset' inside a URL: justified).
- 11-04-structure-details.vi.md: reviewed, 7 findings fixed, parity 0 errors, 0 warnings.
- 11-05-change-log.vi.md: reviewed, 16 findings fixed, parity 0 errors, 0 warnings.
- 11-06-ai-evidence.vi.md: reviewed, 12 findings fixed, parity 0 errors, 0 warnings.
