### 1.3.1. Tín hiệu kết cấu và tần số

Các phương pháp kết cấu xuất phát từ nhận xét rằng ảnh in hay màn hình là một bề mặt khác với da. Chúng phân tích vi kết cấu của bề mặt được đưa ra trước camera, sử dụng tín hiệu kết cấu tĩnh hoặc động [30]. Määttä, Hadid và Pietikäinen thuộc Đại học Oulu khởi đầu hướng này tại Hội nghị Liên hợp Quốc tế về Sinh trắc học năm 2011, áp dụng ba toán tử mẫu nhị phân cục bộ (LBP) đồng nhất lên ảnh khuôn mặt đã chuẩn hóa kích thước 64 × 64 điểm ảnh để phát hiện giả mạo từ một ảnh duy nhất [30], [36]. Bài báo có 385 trích dẫn trên Crossref tính đến ngày 2/10/2026 [36].

Màu sắc bổ sung một chiều thông tin mang tính quyết định. Các bộ mô tả thủ công được trích xuất từ nhiều không gian màu, cụ thể là RGB, HSV và YCbCr, để nắm bắt các mẫu giả mạo [35]. Boulkenafet, Komulainen và Hadid cho thấy một phương pháp dựa trên LBP đạt hiệu năng hàng đầu chỉ nhờ thay đổi không gian màu được sử dụng [30]. Bài báo về kết cấu màu của họ được đăng trên IEEE Transactions on Information Forensics and Security vào tháng 8 năm 2016 và có 486 trích dẫn trên Crossref tính đến ngày 2/10/2026 [37].

Chất lượng ảnh tạo thành một nhánh liên quan, vì khuôn mặt bị chụp lại mang những biến dạng mà khuôn mặt sống không có. Phương pháp phân tích biến dạng ảnh của Wen, Han và Jain kết hợp đặc trưng phản xạ gương, đặc trưng độ mờ, đặc trưng mô men màu và đặc trưng đa dạng màu, tổng cộng 121 chiều, và phân loại chúng bằng máy vectơ hỗ trợ [30]. Bài báo được đăng trên IEEE Transactions on Information Forensics and Security vào tháng 4 năm 2015 và có 764 trích dẫn trên Crossref tính đến ngày 2/10/2026 [38]. Các phương pháp miền tần số hoàn thiện nhóm này: chúng phân tích phổ Fourier của phần dư nhiễu để nắm bắt nhiễu mà một cuộc tấn công giả mạo đưa vào, chẳng hạn vân moiré của một màn hình bị chụp lại [30]. Bảng 1.7 tổng hợp các phương pháp kết cấu và tần số tiêu biểu.

**Bảng 1.7. Các phương pháp kết cấu và tần số tiêu biểu**

| Phương pháp | Hội nghị hoặc tạp chí và năm | Tín hiệu khai thác | Số trích dẫn trên Crossref (2/10/2026) |
| :---- | :---- | :---- | :---- |
| Määttä và cộng sự, vi kết cấu LBP | Hội nghị Liên hợp Quốc tế về Sinh trắc học, 2011 [36] | Vi kết cấu của một ảnh khuôn mặt [30] | 385 [36] |
| Wen và cộng sự, phân tích biến dạng ảnh | IEEE Transactions on Information Forensics and Security, 2015 [38] | Phản xạ gương, độ mờ, mô men màu, đa dạng màu [30] | 764 [38] |
| Boulkenafet và cộng sự, kết cấu màu | IEEE Transactions on Information Forensics and Security, 2016 [37] | Kết cấu LBP trong RGB, HSV và YCbCr [30], [35] | 486 [37] |
| Phân tích miền tần số | Nhóm phương pháp trong công trình tổng quan [30] | Phổ Fourier của phần dư nhiễu, vân moiré [30] | – |

Các phương pháp này chỉ cần một ảnh và không cần người dùng thao tác, nhờ đó thuộc về góc thụ động, dựa trên phần mềm của cách phân loại hệ thống ở Mục 1.2.
