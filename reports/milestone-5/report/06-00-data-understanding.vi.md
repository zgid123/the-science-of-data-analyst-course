# 6. Hiểu dữ liệu và chất lượng dữ liệu

Trước khi trả lời bất kỳ câu hỏi nào, nhóm chúng em cần hiểu dữ liệu đủ rõ để biết đặc điểm nào của dữ liệu có thể làm thay đổi một
kết luận. Ở Milestone 3, chúng em đã khảo sát dữ liệu (profiling) trên toàn bộ 10,9 triệu dòng của bảy bảng gốc;
mười ba con số trong kết quả khảo sát dữ liệu được một đoạn mã khác tính lại độc lập và cả mười ba đều khớp (Phụ lục VI). Biến không hoàn thành gộp hai kết quả Không đạt (Fail) và Rút khỏi module (Withdrawn), giống cách tính của KPI chính, còn AQ1 báo cáo riêng hai
kết quả này. Trên cả 22 kỳ mở, có 28.061 lượt đăng ký học chưa rút tại ngày 14 (tính từ
ngày bắt đầu kỳ mở); 54,7% số lượt này hoàn thành. Cũng trên 22 kỳ mở, tỷ lệ không hoàn thành là 45,3% trong số lượt
đăng ký học chưa rút tại ngày 13 và 44,2% tại ngày 27; giữa các kỳ mở, tỷ lệ này dao động từ 24,9% đến 58,3%. Vì vậy, hai lớp nhãn có kích thước gần
nhau và không cần lấy mẫu lại. Cơ cấu kết quả khác nhau giữa các module: tỷ lệ rút khỏi module cao nhất ở các kỳ mở của
CCC, từ 43% đến 46%, còn GGG có ít trường hợp rút khỏi module nhất nhưng nhiều trường hợp không đạt nhất. Hoạt động trên
nền tảng có phân phối lệch mạnh, với trung vị 602 lượt nhấp và 3.365 lượt đăng ký học không có lượt nhấp nào; do đó,
các số đếm được đưa vào mô hình dưới dạng logarit và không giá trị nào bị loại bỏ. Bước phát triển mô hình dùng 9 kỳ mở năm 2013 và để riêng 13 kỳ mở năm 2014 cho lần kiểm tra duy nhất, còn AQ1 và AQ2 mô tả cả hai năm (C15); Bảng 6.1 trình bày
phạm vi dữ liệu mà mọi con số ở các phần sau đều dựa vào.

**Bảng 6.1. Phạm vi dữ liệu của các kỳ mở phát triển năm 2013 và các kỳ mở của tập kiểm thử năm 2014**

| Phạm vi dữ liệu | Lượt đăng ký học | Sinh viên không hoàn thành | Được dùng cho |
| :---- | :---- | :---- | :---- |
| Toàn bộ lượt đăng ký học năm 2013 (9 kỳ mở) | 13.529 | 6.959 (51,4%) | AQ1, mẫu số thứ hai |
| Năm 2013, chưa rút tại ngày 14 | 12.076 | 5.515 (45,7%) | AQ1, mẫu số chính |
| Năm 2013, chưa rút tại ngày 13 | 12.080 | 5.519 | Phát triển mô hình AQ3, ngày 13 |
| Năm 2013, chưa rút tại ngày 27 | 11.811 | 5.245 (44,4%) | AQ2; phát triển mô hình AQ3, ngày 27 |
| Năm 2013, ngày 27, 7 kỳ mở có bài đến hạn | 9.960 | – | Các dấu hiệu dựa trên bài được chấm điểm của AQ2 |
| Năm 2014, chưa rút tại ngày 14 | 15.985 | 7.185 (44,9%) | AQ1, mẫu số chính |
| Tập kiểm thử năm 2014 (13 kỳ mở), ngày 13 và ngày 27 | 15.989 và 15.724 | Ngày 27: 6.911 (44,0%) | Phân tích lặp lại AQ2; kiểm tra AQ3 và AQ4 |
