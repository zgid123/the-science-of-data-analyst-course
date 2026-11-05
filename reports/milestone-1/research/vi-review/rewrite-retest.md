# Rewrite after the reader re-test – Vietnamese twins (reference.md §4.3, stage 5 → stage 3)

Date: 2026-11-05. Input: `reader-retest.md` (second reader test), guide.md, lessons.md (T1–T6), the merged glossary
(`glossary.py --lang vi --task milestone-1 show`). Each passage was compared with its English source (same name
without `.vi`); meaning, numbers and evidence codes are unchanged. Backups of the twins before this round: scratchpad
`retest-backup/`. Line numbers are those of the edited twin. Business Goal, SMART Goal, persona, prompt and
Before → After stay in English as the brief writes them.

## Ten hardest passages and three also worth fixing

| # | Finding | File:line | Before | After |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 34 – new office not introduced | 04-01:11 | chuyển tiếp đến phòng công tác sinh viên để được hỗ trợ về tài chính hoặc vấn đề cá nhân | chuyển tiếp đến phòng công tác sinh viên, một đơn vị khác với phòng hỗ trợ sinh viên, để được hỗ trợ về tài chính hoặc vấn đề cá nhân |
| 2 | 29 – "câu hỏi chỉ định", "giới hạn" opaque | 03-03:13 | Thay vào đó, chênh lệch này là giới hạn về tính công bằng của câu hỏi chỉ định (AQ4, Mục 4.1). | Thay vào đó, câu hỏi chỉ định (prescriptive, chọn hành động) AQ4 đặt ra một điều kiện về tính công bằng: danh sách liên hệ không được bỏ sót sinh viên năm nhất nhiều hơn hẳn sinh viên các năm trên (Mục 4.1). |
| 3 | 23 – "one in six" arithmetic implicit | 03-02:16 | Tăng năm điểm phần trăm nghĩa là cứ sáu sinh viên không hoàn thành học phần thì có thêm một sinh viên hoàn thành. | Với mức cơ sở giả định, cứ 100 sinh viên thì có 30 sinh viên không hoàn thành học phần. Tăng năm điểm phần trăm nghĩa là thêm năm sinh viên trong số 30 sinh viên này hoàn thành học phần, tức là một trong sáu sinh viên. |
| 4 | 24 – "vừa với" + capacity phrase | 03-02:16 | Quy mô đợt thí điểm vừa với số sinh viên cán bộ liên hệ được mỗi tuần | Đợt thí điểm có quy mô phù hợp với số sinh viên mà cán bộ liên hệ được mỗi tuần |
| 5 | 25 – counterfactual not marked | 03-02:20 | có thể vẫn đạt học phần ngay cả khi không ai liên hệ | có lẽ vẫn đạt học phần ngay cả khi không được liên hệ |
| 6 | 40 – "because" does not follow | 05-00:14 | kết quả của AQ3 được so với một quy tắc đơn giản, vì theo một nghiên cứu … mạnh nhất [8]. | kết quả của AQ3 được so với một quy tắc đơn giản dựa trên số bài được chấm điểm bị bỏ lỡ. Quy tắc này đã là một mốc so sánh khó vượt qua, vì theo một nghiên cứu … mạnh nhất [8]. |
| 7 | 41 – "một điểm rủi ro" read as risk point | 05-00:14 | cho biết sẽ bỏ qua một điểm rủi ro không kèm lý do | cho biết một điểm rủi ro (risk score) không kèm lý do sẽ bị bỏ qua |
| 8 | 37 – week-2/4 data vs week-3/5 lists left implicit | 04-02:14 | Danh sách chỉ được lập từ dữ liệu ghi nhận đến hết tuần 2 và đến hết tuần 4, vì bộ phận dữ liệu dự kiến dữ liệu chậm khoảng một tuần (DO4). | Bộ phận dữ liệu dự kiến dữ liệu về chậm khoảng một tuần (DO4). Vì vậy, danh sách gửi vào tuần 3 chỉ dùng dữ liệu ghi nhận đến hết tuần 2, còn danh sách gửi vào tuần 5 chỉ dùng dữ liệu ghi nhận đến hết tuần 4. |
| 9 | 46 – four authors, three schemes in two sentences | 07-00:3–5 | Bảng 7.1 phân loại từng quyết định theo ba cách. Gorry và Scott Morton [24] đã kết hợp hai cách phân loại có từ trước, của Anthony và của Simon, trong một khung chung. Theo các cấp quyết định của Anthony, … | Bảng 7.1 phân loại từng quyết định theo ba cách: cấp quyết định theo Anthony, loại quyết định theo Simon và khả năng đảo ngược theo Bezos. Hai cách đầu có từ trước; Gorry và Scott Morton [24] đã kết hợp hai cách này trong một khung chung. Anthony chia quyết định thành ba cấp. Hoạch định chiến lược … |
| 10 | 47 – circular Simon definition | 07-00:8–10 | Theo Simon, một quyết định càng lặp lại, càng thường lệ và càng có sẵn quy trình xử lý thì càng gần với quyết định theo quy trình có sẵn (programmed decision). | Simon xếp một quyết định vào loại theo quy trình có sẵn (programmed decision) khi quyết định đó lặp lại, mang tính thường lệ và đã có cách xử lý được xây dựng từ trước, nên không phải cân nhắc lại từ đầu mỗi lần; quyết định càng có những đặc điểm này thì càng gần loại đó. |
| 11 | 4 – codes before they are explained | 01-02:3 | vào khoảng tuần 5 hoặc tuần 6 (CL5). | vào khoảng tuần 5 hoặc tuần 6 (CL5; các mã như CL5 chỉ các phát biểu trong Phụ lục II). |
| 12 | 52 – long subject, main verb lost | 08-00:28–30 | Bên cạnh đó, ý kiến cho rằng sinh viên không phản đối việc trường liên hệ dựa trên hoạt động học tập hiện chỉ có cơ sở từ một sinh viên mô phỏng và các nghiên cứu ở nước ngoài [12]. Ý kiến này cần được sinh viên thật ở Việt Nam xác nhận. | Bên cạnh đó, có ý kiến cho rằng sinh viên chấp nhận việc trường liên hệ dựa trên hoạt động học tập. Ý kiến này hiện chỉ dựa trên một sinh viên mô phỏng và các nghiên cứu ở nước ngoài [12], nên cần được sinh viên thật ở Việt Nam xác nhận. |
| 13 | 39 – unclear AQ2 technique list | 05-00:10 | So sánh giữa các nhóm, chỉ số và kiểm định về mức độ liên quan, hồi quy giải thích, so sánh giữa các khóa | So sánh giữa các nhóm sinh viên; chỉ số đo mức độ liên quan và kiểm định thống kê tương ứng; hồi quy dùng để giải thích (explanatory regression); so sánh giữa các khóa sinh viên |
| 14 | 42 – "phần lớn trường" ambiguous | 06-00:3 | Hướng tiếp cận ở Mục 5 cần những dữ liệu mà phần lớn trường đã có | Phần lớn dữ liệu mà hướng tiếp cận ở Mục 5 cần đã có sẵn ở nhà trường |
| 15 | 53 – "theo" suggests ordering by capacity | 09-00:13 | xếp thứ tự ưu tiên theo số sinh viên cán bộ liên hệ được mỗi tuần | xếp thứ tự ưu tiên trong giới hạn số sinh viên mà cán bộ liên hệ được mỗi tuần |

## Recurring phrases

| Change | File:line | Before | After |
| :-- | :-- | :-- | :-- |
| Capacity phrase, second use in the row shortened | 09-00:13 | Kết quả của AQ3, số sinh viên cán bộ liên hệ được mỗi tuần | Kết quả của AQ3, số sinh viên liên hệ được mỗi tuần |
| Capacity phrase with two "bằng" (finding 33) | 04-01:9 | được đo trên một danh sách dài đúng bằng số sinh viên cán bộ liên hệ được mỗi tuần, bằng hai chỉ số | được đo bằng hai chỉ số, trên một danh sách có số tên bằng số sinh viên mà cán bộ liên hệ được mỗi tuần |
| Capacity phrase, "mà" restored | 04-01:13 | số sinh viên cán bộ liên hệ được mỗi tuần | số sinh viên mà cán bộ liên hệ được mỗi tuần |
| Capacity restated once in the paragraph | 01-02:3 | sinh viên giảm tham gia từ sớm và số sinh viên liên hệ được mỗi tuần | sinh viên giảm dần mức tham gia từ sớm và cán bộ mỗi tuần chỉ liên hệ được vài chục sinh viên |
| "giảm tham gia" as a noun phrase; repeated "được nhận ra" (finding 3) | 01-02:3 | sinh viên giảm tham gia học tập thường được nhận ra muộn và chỉ một phần trong số đó được nhận ra | sinh viên giảm dần mức tham gia học tập thường được nhận ra muộn; hơn nữa, không phải sinh viên nào trong nhóm này cũng được nhận ra |
| "giảm tham gia" | 03-01:3, 09-00:10 | những sinh viên giảm tham gia học tập | những sinh viên đang giảm dần mức tham gia học tập |
| "giảm tham gia" | 03-03:10 | sinh viên đang giảm tham gia học tập | sinh viên đang giảm dần mức tham gia học tập |
| "giảm tham gia" | 08-00:28 | sinh viên giảm tham gia học tập từ sớm | sinh viên giảm dần mức tham gia học tập từ sớm |
| AQ4 level glossed at first use in the file | 04-01:11; 05-00:12; 09-00:13 (03-03:13 above) | AQ4 – Chỉ định / Chỉ định | AQ4 – Chỉ định (prescriptive, chọn hành động) / Chỉ định (prescriptive, chọn hành động) |
| "dễ không hoàn thành" (finding 35) | 04-01:11 | những sinh viên dễ không hoàn thành học phần nhất | những sinh viên có khả năng cao nhất không hoàn thành học phần |
| "dữ liệu đến từng sinh viên" (finding 49) | 07-00:31–32 | Trường có được dữ liệu đến từng sinh viên mà Thông tư 83/2026 yêu cầu [4]. | Trường có được hồ sơ tình trạng học tập của từng sinh viên, như Thông tư 83/2026 yêu cầu [4]. |

## Checks

| Command | Result |
| :-- | :-- |
| `check_parity.py --report reports/milestone-1/report --lang vi <FILE>.md` for 01-02, 03-01, 03-02, 03-03, 04-01, 04-02, 05-00, 06-00, 07-00, 08-00, 09-00 | 0 errors, 0 warnings each (01-02 first gave one warning, comma before "và", fixed with "; hơn nữa,") |
| `translation_status.py --report reports/milestone-1/report --lang vi --mark <FILE>.md`, one call per file | recorded, 11 files |
| `check_abbreviations.py --report reports/milestone-1/report --lang vi` | 5 abbreviations, 0 violations |

Still open: the other findings of `reader-retest.md` (for example 1, 12, 15–18, 21, 26–27, 31, 44, 51) were not in this
round's scope; a further reader test of the edited files has not been run.
