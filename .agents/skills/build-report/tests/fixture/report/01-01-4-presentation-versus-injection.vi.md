### 1.1.4. Tấn công trình diện và tấn công chèn dữ liệu số

Hệ thuật ngữ và các cấp độ nêu trên có chung một ranh giới: ISO/IEC 30107-3 bao quát các cuộc tấn công "diễn ra tại thiết bị thu nhận sinh trắc học trong lúc trình diện" [3]. Xác minh danh tính từ xa, trong đó chính điện thoại hoặc máy tính của người dùng thu nhận khuôn mặt, mở ra con đường thứ hai hoàn toàn né tránh cảm biến [10]. Một bài báo năm 2024 của AI Labs thuộc Amazon Web Services (AWS), "Principles of Designing Robust Remote Face Anti-Spoofing Systems", hệ thống hóa sự phân biệt này và xác định tấn công trình diện vật lý và tấn công chèn dữ liệu số là hai nhóm mối đe dọa chính đối với một hệ thống chống giả mạo khuôn mặt [10].

Trong tấn công chèn dữ liệu số (DIA), kẻ tấn công vượt qua cảm biến và chèn nội dung số độc hại trực tiếp vào luồng dữ liệu [10]. Nội dung đó có thể là ảnh hoặc video được ghi sẵn, hoặc phương tiện được tạo bằng công nghệ deepfake [10]. Bài báo chia nhóm tấn công chèn dữ liệu thành ba nhóm con: tấn công deepfake, tấn công đối kháng số và tấn công phát lại số [10]. Tấn công đối kháng giả định rằng kẻ tấn công có thể gọi mô hình, với quyền truy cập hạn chế hoặc không hạn chế, và do đó có thể tạo các mẫu đối kháng, kể cả nhiễu đối kháng, để vượt qua hệ thống [10]. Một phần tài liệu về PAD cũng dùng thuật ngữ tấn công chèn dữ liệu cho nhiễu khó nhận biết được thêm vào ảnh số trước bước phân loại [13], vì vậy nhiễu đối kháng thuộc tự nhiên vào nhóm tấn công chèn dữ liệu.

Mô hình mối đe dọa của AWS còn mở rộng ra ngoài hai nhóm này với việc chiếm quyền bộ xử lý và sửa đổi kết quả, đồng thời tổ chức các biện pháp phòng vệ theo từng tầng của hệ thống: hiệu năng mô hình, độ bền vững của mô hình, độ bền vững của chuỗi xử lý học máy và độ bền vững của nền tảng [10]. Khuyến nghị chủ đạo của mô hình là một hệ thống chống giả mạo chủ động sử dụng cảm biến tích cực [10]. Hai nhóm tấn công cũng khác nhau về quy mô. Tấn công trình diện nhìn chung mang tính thủ công và quy mô nhỏ, trong khi tấn công chèn dữ liệu mở rộng quy mô dễ dàng hơn nhiều một khi kẻ tấn công có thể đẩy dữ liệu đã bị thao túng vào hệ thống [21].

Công tác tiêu chuẩn hóa cũng theo cùng ranh giới này. CEN/TS 18099, "Biometric data injection attack detection", một đặc tả kỹ thuật của Ủy ban Tiêu chuẩn hóa châu Âu (CEN), được công bố ngày 2/12/2024 và đang hiện hành [22]. Đặc tả này định nghĩa tấn công chèn dữ liệu sinh trắc học và công cụ tấn công chèn dữ liệu, mô tả các hệ thống phát hiện chúng cùng các kế hoạch kiểm thử, và để việc kiểm thử tấn công trình diện cho các tiêu chuẩn ISO/IEC 30107 [23]. Tính đến tháng 7 năm 2026, đây là đặc tả kỹ thuật chính thức duy nhất đang được áp dụng về khả năng chống chịu tấn công chèn dữ liệu, và tiêu chuẩn quốc tế ISO/IEC 25456 đang được xây dựng trên cơ sở của nó [21]. Bảng 1.4 so sánh hai con đường tấn công.

**Bảng 1.4. Tấn công trình diện và tấn công chèn dữ liệu**

| Khía cạnh | Tấn công trình diện | Tấn công chèn dữ liệu (DIA) |
| :---- | :---- | :---- |
| Điểm tấn công | Thiết bị thu nhận, trong lúc trình diện [3] | Luồng dữ liệu sau cảm biến [10] |
| Công cụ | PAI vật lý: ảnh in, màn hình phát lại, mặt nạ [10] | Nội dung số: deepfake, mẫu đối kháng, phát lại số [10] |
| Quy mô | Thủ công và quy mô nhỏ [21] | Lặp lại được và dễ mở rộng [21] |
| Tiêu chuẩn | ISO/IEC 30107 [23] | CEN/TS 18099; ISO/IEC 25456 đang xây dựng [22], [21] |

Do đó, PAD và phát hiện tấn công chèn dữ liệu tạo thành hai lớp phòng vệ liên quan nhưng khác biệt, và Mục 1.2 đặt cả hai vào kiến trúc của một hệ thống sinh trắc học.
