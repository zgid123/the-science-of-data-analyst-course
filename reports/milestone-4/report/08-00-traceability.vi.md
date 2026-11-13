# 8. Ma trận truy vết đã cập nhật

**Ma trận theo đề bài.** Từ Phần 1 đến Phần 7, báo cáo xây dựng cho mỗi câu hỏi một chuỗi lập luận đi từ Business Goal đến quyết định mà câu hỏi đó hỗ trợ. Bảng 8.1 trình bày chuỗi này theo các cột mà đề bài quy định cho thời điểm kết thúc Milestone 4 [1]: loại phân tích, bài toán kỹ thuật, phương pháp cơ sở, phương pháp chính, chỉ số chính, cách đánh giá và quyết định được hỗ trợ. Mỗi dòng dựa trên các bảng dữ liệu đã chuẩn bị của Milestone 3: bảng theo lượt đăng ký học và bảng theo bài được chấm điểm cho AQ1; bảng đặc trưng ngày 27 cho AQ2; cả hai bảng đặc trưng cho AQ3 và AQ4, cùng các ma trận sẵn sàng cho mô hình được lập từ hai bảng này.

**Bảng 8.1. Ma trận truy vết đã cập nhật**

| AQ | Loại phân tích | Bài toán kỹ thuật | Phương pháp cơ sở | Phương pháp chính | Chỉ số chính | Cách đánh giá | Quyết định được hỗ trợ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Mô tả | Tổng hợp | Tỷ lệ gộp chung; tính lại theo mẫu số thứ hai | Tỷ lệ theo nhóm kèm khoảng tin cậy 95% | Tỷ lệ kèm khoảng tin cậy và mẫu số | Tính theo hai cách tổng hợp độc lập; đối chiếu với các tổng số đã biết | D2, D3 |
| AQ2 | Chẩn đoán | Mối liên hệ trong từng kỳ mở module | Chênh lệch tỷ lệ chưa hiệu chỉnh theo từng dấu hiệu | Hồi quy logistic có hiệu ứng cố định theo kỳ mở và các số hạng dấu hiệu × module | Chênh lệch nguy cơ kèm khoảng tin cậy | Ước lượng trên các kỳ mở năm 2013; lặp lại trên các kỳ mở năm 2014 sau lần kiểm tra AQ3 trên tập kiểm thử | D2; các dấu hiệu làm lý do cho D1 |
| AQ3 | Dự báo | Phân loại nhị phân tại ngày 13 và ngày 27 | Danh sách xếp theo quy tắc dấu hiệu sớm; mô hình chỉ dùng đặc điểm cá nhân; danh sách ngẫu nhiên | Hồi quy logistic có hiệu chỉnh phạt trên các biến dự báo chính, trừ khi cây tăng cường độ dốc hoặc bộ biến dự báo mở rộng vượt trội ít nhất bằng mức chênh lệch đã ấn định | Tỷ lệ phát hiện chuẩn hóa của danh sách dài k theo hạn mức liên hệ | Kiểm định chéo loại trừ từng kỳ mở trên các kỳ mở năm 2013; kiểm tra một lần duy nhất trên các kỳ mở năm 2014 | D1 |
| AQ4 | Chỉ định (xếp hạng) | Xếp hạng theo hạn mức liên hệ | Danh sách ngẫu nhiên và danh sách xếp theo quy tắc dấu hiệu sớm | k sinh viên đứng đầu mỗi kỳ mở, kèm lý do | Tỷ lệ phát hiện chuẩn hóa của danh sách dài k | Như AQ3; thêm kiểm định khẳng định về tính công bằng | D1; việc chọn hình thức liên hệ được hoãn |

**Chuỗi truy vết đầy đủ.** Mỗi dòng của bảng phục vụ Business Goal là cải thiện tỷ lệ hoàn thành học phần bằng cách nhận ra đủ sớm những sinh viên ngừng tham gia học tập để kịp hỗ trợ các sinh viên này ngay trong học kỳ; mục tiêu này được đo bằng KPI chính là tỷ lệ hoàn thành học phần của sinh viên còn theo học sau thời gian điều chỉnh đăng ký học phần. Phụ lục VII trình bày chuỗi truy vết đầy đủ từ mục tiêu này và các KPI đến quyết định được hỗ trợ (Bảng A.22), cùng thay đổi C14 trong Nhật ký thay đổi (Bảng A.23).

Mỗi câu hỏi vẫn giữ liên kết với Business Goal và với các bảng dữ liệu đã chuẩn bị của Milestone 3. Thay đổi C14 là điều chỉnh duy nhất về cách đo một câu hỏi và nhằm bảo vệ tính độc lập của lần kiểm tra AQ3 trên tập kiểm thử.
