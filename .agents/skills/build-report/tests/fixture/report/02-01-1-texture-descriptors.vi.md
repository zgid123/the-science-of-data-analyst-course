### 2.1.1. Các bộ mô tả kết cấu

Phân tích kết cấu trở thành hướng chính của Giai đoạn 1 qua một chuỗi bốn bước. Năm 2011, Määttä và cộng sự thuộc Đại học Oulu lần đầu đề xuất áp dụng LBP đa tỉ lệ cho PAD khuôn mặt [30], tại Hội nghị Liên hợp Quốc tế về Sinh trắc học [36]. Năm 2012 và 2014, de Freitas Pereira và cộng sự mở rộng ý tưởng từ ảnh đơn sang video bằng cách áp dụng kết cấu động dựa trên LBP, và giới thiệu đặc trưng LBP trên ba mặt phẳng trực giao (LBP-TOP) [30].

Bước thứ ba chuyển từ kết cấu sang chất lượng ảnh. Phương pháp phân tích biến dạng ảnh của Wen, Han và Jain được đăng trên IEEE Transactions on Information Forensics and Security vào tháng 4 năm 2015 [38], và Mục 1.3.1 mô tả các đặc trưng phản xạ gương, độ mờ và màu sắc của phương pháp này.

Bước thứ tư bổ sung màu sắc. Ngày 19/11/2015, Boulkenafet, Komulainen và Hadid công bố phương pháp kết cấu màu, với nhận xét rằng các nghiên cứu trước đó "chủ yếu tập trung phân tích độ chói của ảnh khuôn mặt" [50]. Việc trích xuất LBP từ không gian màu YCbCr cải thiện kết quả của LBP trên ảnh xám "trên các cơ sở dữ liệu CASIA-FA và Replay-Attack lần lượt 64,5% và 81,4%" [50], và bộ mô tả kết hợp YCbCr với HSV đạt tỷ lệ lỗi cân bằng (EER) 0,4% và HTER 2,9% trên Replay-Attack [50]. Phiên bản tạp chí được đăng trên IEEE Transactions on Information Forensics and Security vào tháng 8 năm 2016 [37], đánh dấu đỉnh cao của phân tích kết cấu thủ công. Bảng 2.1 tổng hợp chuỗi bước này.

**Bảng 2.1. Trình tự thời gian các phương pháp kết cấu và chất lượng ảnh của Giai đoạn 1**

| Năm | Phương pháp | Nhóm tác giả | Nơi công bố | Đóng góp |
| :---- | :---- | :---- | :---- | :---- |
| 2011 | LBP đa tỉ lệ [30] | Đại học Oulu [30] | Hội nghị Liên hợp Quốc tế về Sinh trắc học [36] | Ứng dụng LBP đầu tiên cho PAD khuôn mặt [30] |
| 2012, 2014 | Kết cấu động LBP-TOP [30] | de Freitas Pereira và cộng sự [30] | – | Mở rộng kết cấu sang video [30] |
| 2015 | Phân tích biến dạng ảnh [38] | Wen, Han và Jain [38] | IEEE Transactions on Information Forensics and Security [38] | Tín hiệu chất lượng: phản xạ, độ mờ, màu sắc [30] |
| 2015, 2016 | Kết cấu màu [50], [37] | Boulkenafet, Komulainen và Hadid [50] | arXiv 2015; IEEE Transactions on Information Forensics and Security 2016 [50], [37] | EER 0,4% và HTER 2,9% trên Replay-Attack [50] |

Mỗi bước đều cải thiện kết quả trên bộ đánh giá chuẩn mà nó hướng tới, và nhờ đó phương pháp kết cấu màu trở thành mốc so sánh thủ công mà các phương pháp sâu sau này dùng để đối chiếu [45].
