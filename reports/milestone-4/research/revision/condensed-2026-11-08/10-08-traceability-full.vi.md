## Phụ lục VIII – Truy vết đầy đủ và nhật ký thay đổi

Bảng A.21 mở rộng ma trận truy vết của Milestone 3 sang các lựa chọn về mô hình hóa và đánh giá. Mỗi dòng bắt đầu từ Business Goal (mục tiêu của tổ chức) và KPI của mục tiêu này, đi qua câu hỏi cùng loại phân tích và bài toán kỹ thuật của câu hỏi, rồi đến dữ liệu đã chuẩn bị, phương pháp cơ sở (baseline), phương pháp chính, chỉ số chính, cách kiểm định và quyết định được hỗ trợ. Business Goal là nâng tỷ lệ hoàn thành học phần bằng cách sớm nhận ra những sinh viên ngừng tham gia học tập, để kịp hỗ trợ ngay trong học kỳ. KPI chính là tỷ lệ hoàn thành học phần của sinh viên còn theo học sau thời gian điều chỉnh đăng ký học phần.

**Bảng A.21. Truy vết đầy đủ từ mục tiêu đến quyết định**

| AQ | KPI | Loại phân tích | Bài toán kỹ thuật | Dữ liệu đã chuẩn bị | Phương pháp cơ sở | Phương pháp chính | Chỉ số chính | Kiểm định | Quyết định |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | KPI chính | Mô tả | Tổng hợp và so sánh tỷ lệ | enrolment (bảng lượt đăng ký học), assessment_due (bảng bài đến hạn); tổng thể các lượt đăng ký học còn hiệu lực vào ngày 14 | Tỷ lệ gộp; tỷ lệ theo mẫu số thứ hai, tức toàn bộ 32.593 lượt đăng ký học thay vì 28.061 lượt còn hiệu lực tại ngày 14 | Tỷ lệ theo nhóm kèm khoảng tin cậy 95%; tuần có bài bị bỏ lỡ đầu tiên theo kết quả | Tỷ lệ không hoàn thành kèm khoảng tin cậy | Hai cách tổng hợp cho kết quả trùng nhau; khớp với các tổng số đã biết | D2, D3 |
| AQ2 | KPI chính; KPI phụ 1 | Chẩn đoán | Mối liên hệ trong cùng kỳ mở module | features_d27 (bảng biến dự báo tại ngày 27), enrolment; các kỳ mở năm 2013, sau đó năm 2014 | Chênh lệch tỷ lệ chưa hiệu chỉnh của từng dấu hiệu | Hồi quy logistic với hiệu ứng cố định theo kỳ mở và biến tương tác dấu hiệu × module | Chênh lệch nguy cơ kèm khoảng tin cậy (tỉ số odds đặt bên cạnh) | Các phân tích độ nhạy; lặp lại trên năm 2014 sau khi kiểm thử AQ3 | D2; cung cấp lý do cho từng tên trong danh sách D1 |
| AQ3 | KPI phụ 1 | Dự báo | Phân loại nhị phân tại ngày 13 và ngày 27 | features_d13, features_d27 (bảng biến dự báo tại ngày 13 và ngày 27), model_ready (bảng dữ liệu sẵn sàng cho mô hình); 19 biến dự báo chính | Danh sách xếp theo quy tắc dấu hiệu sớm; mô hình chỉ dùng đặc điểm cá nhân; danh sách ngẫu nhiên | Hồi quy logistic có hiệu chỉnh phạt; cây tăng cường độ dốc chỉ được chọn khi vượt ngưỡng chênh lệch đặt trước | Tỷ lệ phát hiện chuẩn hóa của danh sách dài k (ngày 27, 5 trên 20) | Loại trừ từng kỳ mở trong năm 2013; kiểm thử một lần duy nhất trên năm 2014 | D1 |
| AQ4 | KPI phụ 1 và 2 | Chỉ định (xếp hạng) | Xếp hạng theo hạn mức liên hệ (số sinh viên giảng viên hướng dẫn liên hệ được: 3 hoặc 5 trên mỗi nhóm khoảng 20) | Điểm rủi ro của AQ3; capacity_by_run (độ dài danh sách theo hạn mức liên hệ của từng kỳ mở) | Danh sách ngẫu nhiên; danh sách xếp theo quy tắc dấu hiệu sớm | Chọn k sinh viên đầu tiên của mỗi kỳ mở theo điểm rủi ro của AQ3, kèm lý do | Tỷ lệ phát hiện chuẩn hóa của danh sách dài k | Như AQ3; kiểm tra công bằng theo mức khó khăn của khu vực và tình trạng khuyết tật do sinh viên tự khai | D1; quyết định về việc liên hệ được để lại sau |

Bảng A.22 ghi lại thay đổi duy nhất về cách đo một câu hỏi do thiết kế đánh giá đưa ra; thay đổi này tiếp nối Nhật ký thay
đổi có kiểm soát C01–C13 của Milestone 2 và 3.

**Bảng A.22. Thay đổi C14 trong Nhật ký thay đổi có kiểm soát**

| Mã | Milestone | Nội dung cũ | Nội dung mới | Lý do | Tác động |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C14 | 4 | Các mối liên hệ của AQ2 được ước lượng trên cả 22 kỳ mở | AQ2 được ước lượng trên 9 kỳ mở năm 2013; chỉ lặp lại trên 13 kỳ mở năm 2014 sau khi mô hình AQ3 đã được chốt và chấm điểm | Nếu nhóm xem kết quả năm 2014 trong lúc chọn biến dự báo cho AQ3 thì thông tin của tập kiểm thử sẽ rò rỉ vào mô hình [39] | Kết quả AQ2 trên năm 2014 là một phép lặp lại; phép kiểm thử của AQ3 vẫn độc lập |
