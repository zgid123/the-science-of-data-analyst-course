### 1.3.3. Bộ phân loại sâu và giám sát phụ trợ

Các tín hiệu kết cấu và sự sống ở Mục 1.3.1 và 1.3.2 đều được thiết kế thủ công. Học sâu thay việc thiết kế đặc trưng bằng việc học từ dữ liệu, và cách tiếp cận sâu đơn giản nhất xem PAD là một bài toán phân loại nhị phân, gán nhãn 0 cho khuôn mặt sống và 1 cho khuôn mặt giả mạo, rồi huấn luyện một mạng nơ-ron tích chập (CNN) với hàm mất mát entropy chéo nhị phân [35]. Tín hiệu nhị phân này cho mạng biết một mẫu có phải là tấn công hay không, nhưng không cho biết vì sao.

Giám sát phụ trợ bổ sung lời giải thích đó. Nhãn độ sâu giả, bản đồ phản xạ, nhãn mặt nạ nhị phân và bản đồ đám mây điểm 3D là các tín hiệu giám sát phụ trợ theo từng điểm ảnh điển hình [35]. Mỗi tín hiệu yêu cầu mạng dự đoán một bản đồ theo từng điểm ảnh, không chỉ một nhãn lớp. Với độ sâu giả, nhãn chuẩn của khuôn mặt thật được ước lượng bằng một thuật toán khớp mô hình khuôn mặt 3D, còn với tấn công trình diện phẳng thì được đặt bằng không [30]. Theo cách này, tín hiệu hình học 3D trở thành một mục tiêu huấn luyện, và mạng học được rằng khuôn mặt sống có độ sâu còn ảnh in hay màn hình thì phẳng. Mục 2.2 theo dõi ý tưởng này qua các công trình mang tính bước ngoặt.

Hai nhóm khác mở rộng thêm bộ công cụ học sâu. Các phương pháp sinh mô hình hóa mẫu giả mạo nội tại thông qua các ràng buộc tái tạo theo từng điểm ảnh được nới lỏng [35]. Transformer mang đến một kiến trúc khác: một hướng nghiên cứu đưa các bản đồ rPPG theo không gian – thời gian vào một Vision Transformer (ViT) để nắm bắt đặc trưng nhịp tim tuần hoàn [35], nhờ đó tín hiệu sinh lý cũng đi vào các mô hình sâu. Ngoài ra, George và Marcel thuộc Viện Nghiên cứu Idiap đã dùng học chuyển giao từ một ViT tiền huấn luyện cho bài toán chống giả mạo zero-shot tại Hội nghị Liên hợp Quốc tế về Sinh trắc học năm 2021, và vượt các phương pháp trước đó trên các giao thức HQ-WMCA và SiW-M với kiểu tấn công chưa từng gặp [41]. Bảng 1.9 liệt kê các tín hiệu giám sát.

**Bảng 1.9. Các tín hiệu giám sát của bộ phân loại PAD sâu**

| Giám sát | Mục tiêu mạng dự đoán |
| :---- | :---- |
| Nhị phân [35] | Nhãn sống hoặc giả |
| Độ sâu giả [35], [30] | Bản đồ độ sâu từ việc khớp khuôn mặt 3D; bằng không với tấn công phẳng |
| Bản đồ phản xạ [35] | Độ phản xạ theo từng điểm ảnh |
| Mặt nạ nhị phân [35] | Nhãn sống hoặc giả theo từng điểm ảnh |
| Đám mây điểm 3D [35] | Đám mây điểm của khuôn mặt |
| Tái tạo (phương pháp sinh) [35] | Mẫu giả mạo qua tái tạo được nới lỏng |
| Bản đồ rPPG với ViT [35] | Đặc trưng nhịp tim tuần hoàn |
