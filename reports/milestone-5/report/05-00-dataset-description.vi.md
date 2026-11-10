# 5. Mô tả bộ dữ liệu và mức phù hợp giữa yêu cầu với dữ liệu

OULAD bao gồm 22 kỳ mở của 7 module đào tạo từ xa do Đại học Mở Anh tổ chức tại Vương quốc Anh (UK) trong năm 2013 và
năm 2014, với mã module từ AAA đến GGG. Mỗi kỳ mở được đặt tên theo năm và tháng bắt đầu, với B là tháng 2 và J là
tháng 10; ngày được đếm từ ngày 0, tức ngày bắt đầu kỳ mở. Bảy bảng của bộ dữ liệu nối với nhau bằng ba khóa chung là
mã module, mã kỳ mở và mã sinh viên. Ngoài ra, bảng bài nộp dùng thêm mã bài được chấm điểm, còn bảng lượt nhấp dùng
thêm mã trang. Mọi liên kết giữa các bảng đều khớp. Các bảng này ghi nhận 32.593 lượt đăng ký học của 28.785 sinh viên, mỗi lượt có một kết quả cuối cùng: Đạt (Pass)
12.361, Rút khỏi module (Withdrawn) 10.156, Không đạt (Fail) 7.052 và Xuất sắc (Distinction) 3.024. Vì vậy, hoàn thành
nghĩa là Đạt hoặc Xuất sắc (Bảng A.12, Phụ lục V).
Xét theo năm, 9 kỳ mở năm 2013 gồm 6 module với 13.529 lượt đăng ký học, còn 13 kỳ mở năm 2014 gồm cả 7 module với 19.064 lượt
đăng ký học. Nếu không tính bài thi, chỉ 16 trong 22 kỳ mở có bài được chấm điểm đến hạn tính đến hết ngày 27. Bảng 5.1 là từ
điển dữ liệu rút gọn của các biến chính; từ điển dữ liệu đầy đủ nằm trong Gói nộp cuối kỳ (Final Project Package).

**Bảng 5.1. Các biến chính của OULAD**

| Biến | Ý nghĩa | Câu hỏi sử dụng |
| :---- | :---- | :---- |
| final_result | Pass, Distinction, Fail hoặc Withdrawn | Biến kết quả của cả bốn câu hỏi |
| code_module, code_presentation | Module (AAA–GGG) và kỳ mở (năm và tháng bắt đầu) | Cả bốn câu hỏi |
| date_registration, date_unregistration | Ngày đăng ký và ngày hủy đăng ký, tính so với ngày 0 | Xác định phạm vi dữ liệu; thời điểm rút khỏi module |
| assessment_type, date; date_submitted | Loại bài (TMA, CMA, bài thi), ngày đến hạn và ngày nộp | AQ1–AQ3 |
| sum_click, date | Số lượt nhấp trên một trang trong một ngày | AQ2, AQ3 |
| num_of_prev_attempts, studied_credits | Số lần học trước; số tín chỉ đang học trong kỳ mở | AQ2, AQ3 |
| imd_band, disability | Mức khó khăn kinh tế – xã hội của khu vực cư trú; tình trạng khuyết tật do sinh viên tự khai | Chỉ dùng để kiểm tra theo nhóm |
