## 7.2. Truy vết nguồn gốc dữ liệu, từ điển dữ liệu và phiên bản

**Từ điển dữ liệu.** Mỗi cột của dữ liệu đã chuẩn bị đều được mô tả kèm trường nguồn, phép biến đổi, kiểu dữ liệu, vai trò và mức độ nhạy cảm, đúng như đề bài yêu cầu [1]. Vai trò cho biết một cột được dùng theo cách nào: mã định danh, biến mục tiêu, đặc trưng, thuộc tính dùng để kiểm tra công bằng, cờ phục vụ đánh giá hoặc chỉ số mô tả (cột chỉ dùng để mô tả dữ liệu, không dùng làm đặc trưng). Phép kiểm tra V14 báo lỗi nếu một cột thiếu mô tả hoặc nếu một danh sách đặc trưng chứa cột có vai trò khác, cụ thể là thuộc tính dùng để kiểm tra công bằng, biến mục tiêu hoặc chỉ số mô tả; nhờ đó, tài liệu mô tả không thể lệch khỏi dữ liệu.

**Truy vết nguồn gốc dữ liệu.** Bảng truy vết nguồn gốc dữ liệu (lineage) theo mẫu của đề bài nối mỗi biến đã chuẩn bị với tệp và trường nguồn, kèm phép biến đổi, khoảng thời gian hoặc điều kiện lọc, mục đích sử dụng và mức độ nhạy cảm [1]. Bảng 7.2 trích bảng này cho các biến chính dùng để trả lời các AQ; bảng đầy đủ là Bảng A.12 trong Phụ lục III, gồm một dòng cho mỗi biến trong 88 biến đã chuẩn bị, với các biến nhạy cảm được đánh dấu ở cột mục đích.

**Bảng 7.2. Truy vết nguồn gốc dữ liệu của các biến chính trong dữ liệu đã chuẩn bị**

| Biến đã chuẩn bị | Tệp / trường nguồn | Phép biến đổi | Khoảng thời gian / điều kiện lọc | Mục đích / AQ | Mức độ nhạy cảm |
| :---- | :---- | :---- | :---- | :---- | :---- |
| non_completion | studentInfo.final_result | Fail hoặc Withdrawn | quan sát vào cuối kỳ mở | biến mục tiêu của AQ1–AQ3 | không |
| enrolled_d14 | studentRegistration, các ngày đăng ký | đang đăng ký học vào ngày 14 | ngày 14 | mẫu số của KPI chính (C09) | không |
| clicks_0c | studentVle.sum_click, date | tổng | từ ngày 0 đến ngày c | AQ2–AQ3 | không |
| tasks_missed_c | studentAssessment | đến hạn tính đến hết ngày c, không có bài nộp nào (ngoài kết quả bảo lưu) tính đến hết ngày c | bài nộp tính đến hết ngày c | AQ2–AQ3; một phần của quy tắc dấu hiệu sớm | không |
| early_sign_rule | dẫn xuất | bỏ lỡ bài, nộp trễ TMA hoặc không hoạt động | tại c | quy tắc dùng làm mốc so sánh cho mô hình ở AQ3; KPI phụ 1 (C10) | không |
| imd_band | studentInfo.imd_band | "10-20" → "10-20%"; giá trị thiếu → "Missing" | – | kiểm tra công bằng của AQ4 (C04) | nhạy cảm |

**Phiên bản.** Bản kê phiên bản (version manifest) đặt tên bộ dữ liệu đã chuẩn bị là OULAD-N04-prepared-1.0 và ghi lại mã kiểm tra SHA-256 của mọi tệp gốc, script và tệp đã chuẩn bị, số dòng của mọi bảng, commit của kho mã, phiên bản Python (3.12.7) và polars (2.1.0) cùng thời điểm tạo theo UTC. Nhờ đó, người đọc biết được dữ liệu gốc nào và mã nguồn nào đã tạo ra một tệp dữ liệu đã chuẩn bị; ngoài ra, phép kiểm tra chạy lại ở Mục 6.1 cho thấy cùng đầu vào cho ra cùng đầu ra.
