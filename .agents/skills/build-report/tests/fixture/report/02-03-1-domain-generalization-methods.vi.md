### 2.3.1. Các phương pháp tổng quát hóa miền

Phương pháp tổng quát hóa miền đầu tiên cho PAD khuôn mặt đã định nghĩa lại bài toán đằng sau những thất bại khi kiểm thử chéo ở Mục 2.1.3 và 2.2. Shao, Lan, Li và Yuen thuộc Đại học Báp-tít Hồng Kông nhận định tại CVPR 2019 rằng "các phương pháp chống giả mạo khuôn mặt hiện có nắm bắt những tín hiệu phân biệt mang tính thiên lệch theo tập dữ liệu" [44]. Phương pháp Multi-Adversarial Discriminative Deep Domain Generalization (MADDG) của họ học một không gian đặc trưng dùng chung cho nhiều tập dữ liệu nguồn thông qua học đối kháng "dưới ràng buộc khai thác bộ ba với lực kép", kèm giám sát phụ trợ bằng độ sâu [44]. Phương pháp này cũng giới thiệu cách đánh giá được mô tả ở Mục 1.3.4, trong đó một tập dữ liệu được giữ lại làm tập đích chưa từng gặp và "không thể được truy cập trong quá trình huấn luyện" [44]. MADDG báo cáo HTER 17,69%, 24,5%, 22,19% và 27,98% trên bốn bài kiểm thử [44]; mã PyTorch của phương pháp được công khai, và bài báo có 423 trích dẫn trên OpenAlex tính đến ngày 2/10/2026 [44].

SSDG, của Jia, Zhang, Shan và Chen thuộc Viện Công nghệ Tính toán, Viện Hàn lâm Khoa học Trung Quốc, tinh chỉnh ý tưởng này tại CVPR 2020 bằng cách xử lý khuôn mặt thật và giả một cách bất đối xứng [42]. Khuôn mặt thật từ mọi miền được làm cho không thể phân biệt và tập trung, sao cho "phân phối đặc trưng của khuôn mặt thật tập trung, còn của khuôn mặt giả thì phân tán giữa các miền nhưng tập trung trong từng miền" [42]. Biến thể SSDG-R đạt HTER từ 7,38% đến 15,61%, với mã nguồn công khai và 316 trích dẫn trên OpenAlex tính đến ngày 2/10/2026 [42].

Các transformer tiền huấn luyện mang đến bước tiếp theo. FLIP, của Srivatsan, Naseer và Nandakumar thuộc Đại học Trí tuệ nhân tạo Mohamed bin Zayed, được trình bày tại Hội nghị Quốc tế về Thị giác máy tính của IEEE (ICCV) năm 2023 [66]. Phương pháp khởi tạo một ViT bằng trọng số thị giác – ngôn ngữ của CLIP và căn chỉnh đặc trưng ảnh với mô tả bằng ngôn ngữ tự nhiên của các lớp, đồng thời bổ sung một mục tiêu học tương phản đa phương thức [66]. Trong kiểm thử zero-shot, biến thể FLIP-MCL đạt HTER từ 0,54% đến 4,95%, lấy trung bình qua năm lần chạy, với giá trị trung bình 3,01% [66]. Mã nguồn được công khai, và bài báo có 74 trích dẫn trên OpenAlex tính đến ngày 2/10/2026 [66]. Bảng 2.8 cho thấy sự tiến triển qua chuỗi phương pháp.

**Bảng 2.8. HTER (%) trên giao thức loại trừ từng tập O/C/I/M, theo năm**

| Phương pháp | Năm và nơi công bố | O&C&I→M | O&M&I→C | O&C&M→I | I&C&M→O | Trung bình |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| MADDG [44] | CVPR 2019 | 17,69 | 24,50 | 22,19 | 27,98 | 23,09 (tự tính) |
| SSDG-R [66], [42] | CVPR 2020 | 7,38 | 10,44 | 11,71 | 15,61 | 11,28 |
| SSAN-R [66] | CVPR 2022 | 6,67 | 10,00 | 8,88 | 13,72 | 9,80 |
| ViT [66] | ECCV 2022 | 1,58 | 5,70 | 9,25 | 7,47 | 6,00 |
| FLIP-MCL [66] | ICCV 2023 | 4,95 | 0,54 | 4,25 | 2,31 | 3,01 |

Giá trị trung bình của MADDG là trung bình của bốn giá trị được báo cáo; các giá trị trung bình khác là số liệu in trong bảng so sánh của FLIP [66].

Chỉ trong bốn năm, sai số trung bình trên các tập dữ liệu chưa từng gặp đã giảm từ khoảng 23% xuống khoảng 3%. Kết quả là bài toán mở của lĩnh vực dịch chuyển từ thiên lệch tập dữ liệu trong kết cấu sang những con đường tấn công mà không bộ phát hiện phía camera nào quan sát được, như Mục 2.3.2 mô tả.
