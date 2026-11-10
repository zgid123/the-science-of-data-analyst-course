# 9. Thiết kế đánh giá

Thiết kế đánh giá được chốt ở Milestone 4 trước khi chạy bất kỳ đoạn mã nào; thiết kế này cho biết cách nhóm chúng em
xác định một câu trả lời đã đủ tốt hay chưa. Đối với AQ1 và AQ2, thiết kế này đã được áp dụng cho dữ liệu năm 2013 và năm 2014; đối
với AQ3 và AQ4, đây là quy trình đánh giá mà hai câu hỏi sẽ phải trải qua.
Thiết kế áp dụng Hướng dẫn báo cáo minh bạch mô hình dự báo đa biến cho tiên lượng hoặc chẩn đoán cá nhân, phiên bản cập nhật cho AI (TRIPOD+AI). Hướng dẫn này xem
việc đánh giá gồm ba khía cạnh: khả năng phân biệt, hiệu chuẩn và giá trị hỗ trợ ra quyết định [11]. Độ dài của một
danh sách do hạn mức liên hệ k quyết định: 3 hoặc 5 lần liên hệ trên 20 sinh viên, với thiết lập chính là 5 trên 20 tại
ngày 27. Tỷ lệ phát hiện trong giới hạn danh sách là tỷ lệ sinh viên không hoàn thành của một kỳ mở có tên trong danh
sách. Mức cao nhất mà một danh sách dài k có thể đạt dao động từ 46% đến 100% giữa các kỳ mở huấn luyện, nên tỷ lệ phát
hiện chuẩn hóa lấy tỷ lệ phát hiện chia cho mức cao nhất đó. Bên cạnh đó, lift là tỷ lệ sinh viên không hoàn thành trong
danh sách chia cho tỷ lệ nền, tức tỷ lệ không hoàn thành của cả kỳ mở; lift bằng 1 nghĩa là danh sách không hơn chọn
ngẫu nhiên. Bảng 9.1 là Kế hoạch đánh giá (Evaluation Plan).

**Bảng 9.1. Kế hoạch đánh giá**

| AQ | Chỉ số chính | Phương pháp cơ sở | Cách đánh giá | Tiêu chí thành công |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Tỷ lệ không hoàn thành và tỷ lệ từng loại kết quả kèm khoảng tin cậy 95%, theo module, kỳ mở, tháng bắt đầu và năm | Tỷ lệ gộp; tỷ lệ trên mọi lượt đăng ký học; tỷ lệ khi loại các lượt đăng ký học mang cờ chất lượng dữ liệu | Kiểm tra mẫu số; hai cách tổng hợp độc lập (từ bảng dữ liệu đã chuẩn bị và từ các bảng gốc) | Hai cách cho kết quả khớp đến từng lượt đăng ký học; mọi tỷ lệ đều ghi kèm mẫu số và khoảng tin cậy; không so sánh tỷ lệ giữa các kỳ mở khi thiếu khoảng tin cậy |
| AQ2 | Chênh lệch nguy cơ trung bình của từng dấu hiệu trong cùng kỳ mở module, tính bằng điểm phần trăm, kèm khoảng tin cậy 95% và tỉ số odds (odds ratio) | Chênh lệch tỷ lệ chưa hiệu chỉnh cho từng dấu hiệu | Ước lượng trên 9 kỳ mở năm 2013; các phép kiểm tra độ nhạy; phân tích lặp lại trên 13 kỳ mở năm 2014 | Chênh lệch nguy cơ đã hiệu chỉnh ít nhất 5 điểm phần trăm, với khoảng tin cậy không chứa 0 và cùng chiều ở ít nhất hai phần ba số module tính được dấu hiệu đó |
| AQ3 | Tỷ lệ phát hiện chuẩn hóa trong giới hạn danh sách, gộp qua các kỳ mở (ngày 27, 5 trên 20) | Danh sách xếp theo quy tắc dấu hiệu sớm; mô hình chỉ dùng đặc điểm cá nhân; danh sách ngẫu nhiên | Fold loại trừ từng kỳ mở (leave-one-run-out) trong năm 2013; một lần kiểm tra có ghi nhật ký trên cả 13 kỳ mở năm 2014 | Điều kiện đạt duy nhất S1, quyết định mô hình có được dùng hay không: tỷ lệ phát hiện chuẩn hóa gộp của mô hình sẽ phải cao hơn của danh sách theo quy tắc; khoảng tin cậy của chênh lệch giữa mô hình và quy tắc, tính bằng bootstrap hai tầng (lấy mẫu lại kỳ mở, rồi lượt đăng ký học trong từng kỳ mở, với mô hình và quy tắc được so trên cùng một mẫu lấy lại), phải nằm trên 0; giá trị p của kiểm định hoán vị đổi dấu (sign-flip test) phải nhỏ hơn 0,05 |
| AQ4 | Tỷ lệ phát hiện chuẩn hóa trong giới hạn danh sách | Danh sách ngẫu nhiên; danh sách xếp theo quy tắc dấu hiệu sớm | Như AQ3; danh sách được lập riêng cho từng kỳ mở của tập kiểm thử | Danh sách sẽ phải thỏa mãn điều kiện đạt S1, đồng thời phép kiểm tra công bằng phải đạt hoặc các nhóm bị phép kiểm tra này đánh dấu phải được con người xem xét; nêu rõ rằng giả định thứ tự nguy cơ trùng với thứ tự nhu cầu hỗ trợ chưa được kiểm chứng; không khẳng định gì về tác động của việc liên hệ |
