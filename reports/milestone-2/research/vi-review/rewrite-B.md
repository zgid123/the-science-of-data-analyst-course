# Rewrite B – Vietnamese twins of Sections 5–9 and the appendices after the reader test

Date: 2026-11-06. Inputs: `reader-test.md` (62 passages), topic glossary `course-completion-early-contact` as updated
after the test, `templates/prompts/report-translate.md` (rewrite rule after a reader test). Files rewritten from the
English: 05-00, 06-00, 07-00, 07-01, 07-02, 08-00, 09-00 (stale ones brought in line with the English: 06-00, 07-01,
07-02, 08-00, 09-00). Appendices 11-00 to 11-06: term pass and the flagged wording. Line numbers are those of the new
twin.

## Reader-test findings fixed

| # | File:line (new) | Before | After |
| :-- | :-- | :-- | :-- |
| 41 | 05-00:15 | "được đối chiếu với giá trị tham chiếu ghi sẵn" | "đối chiếu … với giá trị tham chiếu ghi sẵn trong script thu thập" (also 11-03:28, 11-03:32) |
| 42 | 05-00:17 | "được ghi trong manifest" | "được ghi trong manifest (tệp kê khai tên, kích thước và mã kiểm tra của từng tệp)"; 11-03:32 "Bảng A.4 là manifest của gói, tức tệp kê khai …" |
| 43 | 05-00:20 | "thấy bảy bảng của hai bản có các dòng dữ liệu giống nhau. Khác biệt duy nhất nằm ở năm bảng" | "cả bảy bảng có các dòng dữ liệu như nhau. Hai bản chỉ khác nhau ở cách ghi giá trị thiếu trong năm bảng: UCI ghi dấu "?", còn figshare để trống ô" |
| 44 | 06-00:3 | "Mỗi bảng được đọc ở dạng văn bản để không giá trị nào bị chuyển đổi" | "Nhóm đọc mọi cột của từng bảng dưới dạng chuỗi ký tự, nhờ đó không giá trị nào bị tự động đổi kiểu" |
| 45 | 06-00:3 | negative days unexplained | added: "các trường thời gian là số ngày tính từ ngày bắt đầu của lượt mở module, nên giá trị âm là những ngày trước ngày bắt đầu" |
| 46 | 06-00:17 | "thiếu dòng tương ứng ở bảng cha" | "đều có dòng tương ứng ở bảng gốc mà bản ghi đó tham chiếu đến" (11-04:33 likewise) |
| 47 | 06-00:19 | "Các giá trị kết quả phân biệt được đạt và đạt loại giỏi với trượt và rút học phần." | "biến kết quả tách được hai nhóm: nhóm hoàn thành (Pass và Distinction) và nhóm không hoàn thành (Fail và Withdrawn)" |
| 48 | 06-00:19 | "số lần học trước đó đều tăng lên, nên mã sinh viên được giữ nguyên" | "Số này chỉ tăng được khi cùng một mã sinh viên chỉ cùng một người ở mọi lượt mở, nên mã sinh viên được giữ ổn định" (follows the updated English) |
| 49 | 06-00:19 | "mỗi module có tối đa một đợt trước và một đợt sau có cùng tháng bắt đầu" | "Khi xét riêng các lượt bắt đầu vào tháng 2 và các lượt bắt đầu vào tháng 10, mỗi module có nhiều nhất một lượt mở năm trước và một lượt mở năm sau cùng tháng bắt đầu" |
| 50 | 06-00:19 | "28.119 lượt vẫn duy trì đăng ký đến ngày 14" (no purpose) | "… vẫn còn đăng ký vào ngày 14. Con số 28.119 là mẫu số của KPI (Mục 7.1)" |
| 51 | 07-01:1 | "Ma trận truy vết cập nhật" | "Ma trận truy vết đã cập nhật" (also Bảng 7.1 caption) |
| 14 | 07-01:9 | "bài được chấm điểm bị bỏ lỡ đầu tiên ở cả hai nhóm sinh viên" | "bài được chấm điểm đầu tiên bị bỏ lỡ, tính riêng cho sinh viên đạt và sinh viên không đạt" (follows the updated English) |
| 52 | 07-01:11 | "trên các đợt mở năm 2014 của 9 cặp module và tháng bắt đầu" | "trên các lượt mở năm 2014 của 9 cặp module – tháng bắt đầu có cả lượt năm 2013 và năm 2014" |
| 53 | 07-01:14 | "theo yêu cầu của sản phẩm bàn giao B trong đề bài [1] (Bảng A.10)" | "đúng yêu cầu của sản phẩm B trong đề bài (ma trận truy vết đã cập nhật) [1]; toàn bộ chuỗi nằm ở Bảng A.10 của phụ lục này" |
| 54 | 07-02:3 | "một câu hỏi chỉ định chưa có bằng chứng về hành động được giữ làm yêu cầu …; nhận định … ở mức thận trọng hơn" | "Đề bài đặt ra hai quy tắc. Theo quy tắc thứ nhất, … Theo quy tắc thứ hai, nếu dữ liệu không ghi nhận hành động đã thực hiện và kết quả của hành động đó, câu hỏi chỉ định được giữ làm yêu cầu dữ liệu cho một quyết định trong tương lai; khi đó, báo cáo chỉ đưa ra nhận định ở mức hẹp hơn so với khi có dữ liệu đó" |
| 55 | 07-02:5 | "mỗi cặp module và tháng bắt đầu có nhiều nhất một đợt mở trước đó để huấn luyện; CCC và các đợt mở tháng 2 của EEE và GGG không có đợt nào" | "với mỗi module và tháng bắt đầu, dữ liệu có nhiều nhất một lượt mở năm trước để huấn luyện mô hình. Module CCC và các lượt mở tháng 2 của EEE và GGG không có lượt mở năm trước cùng tháng bắt đầu, nên các lượt này chỉ dùng để đánh giá, không dùng để huấn luyện" (follows the updated English) |
| 56 | 08-00:3 | "Do đó, nhóm … chỉ sử dụng dữ liệu trong phạm vi các điều kiện …; bản thân dữ liệu cũng giới hạn …" | "Mục này trình bày hai loại ràng buộc: các điều kiện về quyền riêng tư và đạo đức khi sử dụng dữ liệu; và những giới hạn mà chính dữ liệu đặt ra cho các kết luận." |
| 57 | 08-00:5 | "Dữ liệu chỉ được lưu trên máy của các thành viên nhóm theo giấy phép CC BY 4.0" | "Về lưu trữ, dữ liệu chỉ nằm trên máy của các thành viên nhóm. Nhóm sử dụng dữ liệu theo giấy phép CC BY 4.0 [2] và trích dẫn bài mô tả dữ liệu." |
| 58 | 08-00:9 | "thay vì được sửa âm thầm" | "thay vì tự ý sửa mà không ghi nhận" |
| 59 | 09-00:3 | "hỗ trợ Milestone này ở bốn trong số các vai trò mà đề bài cho phép" | "Trong Milestone này, nhóm dùng AI tạo sinh cho bốn vai trò, đều nằm trong danh sách vai trò mà đề bài cho phép" |
| 60 | 09-00:9 | "Một tác tử AI làm việc cho nhóm" | "Một AI agent (trợ lý AI tự thực hiện nhiều bước) làm việc cho nhóm"; then "agent" (also 11-06:3, 5, 23) |
| 61 | 09-00:14 | "vẫn có thể vượt qua các điều kiện bắt buộc đầu tiên" | rewritten from the updated English: "các điều kiện bắt buộc phải đòi hỏi bộ dữ liệu có ngày rút và có ngày đến hạn của các bài được chấm điểm, vì AQ3 và KPI phụ 1 cần cả hai thông tin này. Các điều kiện bắt buộc hiện có đòi hỏi đủ hai thông tin đó và đã được chốt trước khi nhóm chấm điểm …" |
| 62 | 09-00:14 | "nhóm chỉ còn dữ liệu tổng hợp (synthetic)" | "nhóm chỉ còn cách dùng dữ liệu giả lập" (also 11-06:44) |

## Recurring terms applied (reader-test table and updated glossary)

| Term before | Term after | Where |
| :-- | :-- | :-- |
| đợt mở học phần, đợt (OULAD presentation) | lượt mở module, lượt mở | 06-00, 07-01, 07-02, 08-00, 09-00, 11-02, 11-04, 11-05 (C01, C02, C04–C07, Bảng A.10), 11-06 (Q2) |
| kết quả ở cấp học phần, có rút học phần (OULAD) | kết quả theo từng module, có ghi nhận rút khỏi module | 11-01:9; 11-02:12; 06-00:17 |
| số sinh viên cán bộ liên hệ được mỗi tuần | số lượt liên hệ tối đa mỗi tuần | 07-01:12, 07-02:5, 11-05 (C08, Bảng A.10), 11-06 (Q11) |
| độ chính xác (accuracy, general) | chất lượng dự báo (của danh sách) | 08-00:5, 08-00:7 |
| dữ liệu tổng hợp (synthetic) | dữ liệu giả lập | 09-00:14, 11-06:44 (Q4) |
| thông tin nền | đặc điểm cá nhân | 11-06 (Q6) |
| tác tử | AI agent / agent | 09-00, 11-06 |
| vế câu hỏi | phần câu hỏi | 11-02:9, 11-06 (Q4, S2, S7) |
| nhóm phân tích dữ liệu (repeated) | nhóm | 05-00, 06-00, 07-02, 08-00, 09-00, 11-01, 11-03, 11-05, 11-06 |
| bản tải lại | bản đăng lại | 11-01 (two rows) |
| Mục 13 của đề bài | mục 13 của đề bài | 11-01 (four rows) |
| cặp module và tháng bắt đầu | cặp module – tháng bắt đầu, defined where used | 07-01:11, 11-05 (C07) |
| UK (first use in 08-00) | Vương quốc Anh (UK) | 08-00:7 |
| code block "(Mục 6)" | "(Task 6)", as in the English code block | 11-03:11 |

## Checks

`check_parity.py --report reports/milestone-2/report --lang vi` on each of the 14 files: 0 errors, 0 warnings, except
the "English loanword" warning on URLs and quoted search queries (`/dataset/`, `/datasets/`) in 11-01 and 11-03, which
stay verbatim. Each file was then marked with `translation_status.py --mark` (one call per file).

## Left open for the main session

- "mức thiếu thốn của khu vực cư trú" (IMD band, reader test #25) is still the glossary form; kept here. The reader
  proposed "mức độ khó khăn kinh tế – xã hội của khu vực".
- "bài được chấm điểm" (reader-test table, 14 uses) is still the glossary form; kept.
- "Khả năng xử lý chất lượng dữ liệu" (criterion name, #35) is kept in 11-02 as the glossary gives it.
