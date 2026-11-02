## 4.4. Giới hạn và các câu hỏi mở

Khi áp dụng vào FSFM, các nguyên tắc của Mục 4.3 cho thấy một phương pháp đầy hứa hẹn trên nhiều nhiệm vụ nhưng vẫn chưa được chứng minh ở những nơi mà quyết định an ninh cần bằng chứng. Sáu giới hạn nổi bật như sau.

(1) **Phép kiểm thử độc lập cho thấy một khoảng cách tổng quát hóa lớn.** Một đánh giá chuẩn của Viện Nghiên cứu Idiap, được chấp nhận tại Hội nghị Liên hợp Quốc tế về Sinh trắc học năm 2026, đã kiểm thử mô hình chống giả mạo của FSFM theo giao thức một nguồn ở Hình 4.5: mô hình đạt ACER trung bình 4,2% khi dữ liệu huấn luyện và kiểm thử cùng một tập dữ liệu, nhưng 37,3% trên mười hai cặp chéo tập dữ liệu [105]. Một nghiên cứu thứ hai của Idiap báo cáo cùng các số liệu này [110], và nhóm tác giả kết luận rằng mô hình của FSFM không cung cấp đặc trưng PAD tốt hơn so với tiền huấn luyện tổng quát quy mô lớn [105].
(2) **Kết quả tốt nhất của chính phương pháp phụ thuộc vào dữ liệu huấn luyện bổ sung.** Theo giao thức để-lại-một, FSFM báo cáo HTER trung bình 4,81% khi bổ sung CelebA-Spoof vào dữ liệu huấn luyện và 8,88% khi không có tập này [102]. Trong cùng điều kiện, phương pháp thị giác – ngôn ngữ FLIP báo cáo 3,01% [66], nên nếu chỉ xét riêng FAS, một phương pháp chuyên biệt làm tốt hơn; thế mạnh của FSFM nằm ở độ bao phủ trên ba nhiệm vụ chứ không phải điểm số tốt nhất trên một nhiệm vụ [102].
(3) **Phương pháp nhìn thấy hình ảnh, không nhìn thấy con đường hình ảnh đi vào hệ thống.** FSFM chỉ học từ hình ảnh, không dùng các tín hiệu như âm thanh hay tín hiệu sinh lý, như chính nhóm tác giả lưu ý [102], và phương pháp xem tấn công là nội dung hình ảnh mà không xử lý các tấn công chèn dữ liệu vượt qua camera [102], trong khi chứng nhận FIDO yêu cầu có tài liệu về cơ chế bảo vệ chống chèn dữ liệu [79].
(4) **Dữ liệu huấn luyện có thể mang thiên lệch.** Nhóm tác giả lưu ý rằng VGGFace2 có thể chứa thiên lệch về chủng tộc, sắc tộc và độ tuổi [102], và tính đến ngày 3/10/2026 chưa có đánh giá nào trên các nhóm nhân khẩu học được công bố, trong khi chương trình FIDO kiểm thử theo màu da, độ tuổi và giới tính [78].
(5) **Đây là một bản phát hành nghiên cứu, chưa phải sản phẩm được chứng nhận.** Mã nguồn, trọng số và bản trình diễn được phát hành theo giấy phép CC BY-NC 4.0 cho mục đích nghiên cứu phi thương mại, và tính đến ngày 3/10/2026 chưa có sản phẩm nào dựa trên FSFM có thư xác nhận của iBeta, chứng nhận FIDO hay kết quả NIST FATE PAD [107], trong khi quy định ngân hàng Việt Nam yêu cầu PAD được chứng nhận đạt ISO 30107 Cấp độ 2 hoặc cấp độ tương đương [98].
(6) **Việc tái lập và huấn luyện có chi phí thực tế.** Kho mã cố định Python 3.9.21, PyTorch 1.13.1 với CUDA phiên bản 11.7 và timm 0.4.5 [106], nên một môi trường hiện hành phải tái tạo đúng các phiên bản này, và tiền huấn luyện cần 400 lượt qua 3,3 triệu ảnh trên bốn card đồ họa cao cấp [102]. Một đánh giá chuẩn năm 2026 trên 15 mô hình nền tảng thị giác cho chống giả mạo chưa đưa FSFM vào [111].

Bảng 4.2 đặt các giới hạn này cạnh những thế mạnh của phương pháp.

**Bảng 4.2. Thế mạnh và giới hạn của FSFM**

| Khía cạnh | Thế mạnh | Giới hạn |
| :---- | :---- | :---- |
| Cách học | Chỉ học từ khuôn mặt thật không gán nhãn [102] | Dữ liệu huấn luyện có thể mang thiên lệch nhân khẩu học [102] |
| Phạm vi | Một mạng xương sống cho deepfake, tấn công trình diện và khuôn mặt do AI tạo ra [102] | Chỉ xử lý hình ảnh; không bảo vệ con đường chèn dữ liệu [102] |
| Độ chính xác | Kết quả tốt theo các giao thức của nhóm tác giả [102] | Khoảng cách chéo tập dữ liệu lớn trong một phép kiểm thử độc lập [105]; FLIP chuyên biệt làm tốt hơn ở chống giả mạo [66] |
| Tính mở | Mã nguồn, trọng số và một bản trình diễn đang hoạt động đều công khai [106], [107], [108] | Giấy phép phi thương mại; chưa có chứng nhận [107] |
| Tính thực tiễn | Một lần tiền huấn luyện phục vụ mọi nhiệm vụ [102] | Tiền huấn luyện tốn kém; bộ phần mềm bị cố định phiên bản [102], [106] |

Những giới hạn này xác định các câu hỏi mà một lần triển khai thực tế phải trả lời. Câu hỏi thứ nhất là hiểu biết về khuôn mặt thật của FSFM có giữ vững được trong các phép kiểm thử chéo tập dữ liệu độc lập khi dữ liệu huấn luyện được đồng nhất hay không. Câu hỏi thứ hai là một sản phẩm xây dựng trên phương pháp này có thể đạt một cấp độ PAD được chứng nhận như ISO 30107 Cấp độ 2, mức mà pháp luật Việt Nam hiện chấp nhận, hay không [98]. Câu hỏi thứ ba là nên kết hợp phương pháp với phát hiện tấn công chèn dữ liệu như thế nào. Cho đến khi các câu hỏi này được trả lời, FSFM phát huy giá trị tốt nhất như một ví dụ mở, được ghi chép đầy đủ, về hướng đi của nghiên cứu an ninh khuôn mặt, và như một điểm khởi đầu vững chắc cho các phép kiểm thử độc lập tiếp theo.
