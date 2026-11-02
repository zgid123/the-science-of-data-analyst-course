## 5.1. Các kết luận chính

Từ các bằng chứng về PAD, quá trình phát triển, hướng chính sách và những phương pháp mới nhất của nó, có thể rút ra năm kết luận.

(1) **Tấn công đã biết được phát hiện tốt; điều kiện chưa từng gặp thì chưa.** Trong đánh giá của NIST, nhiều nhà phát triển giữ được cả APCER và BPCER ở mức không quá 0,01 đối với tấn công in và phát lại, khẩu trang bảo hộ và mặt nạ silicon, trong khi một số loại tấn công vẫn có sai số cao với mọi thuật toán và không thuật toán nào bắt được tất cả [31], [91]. Các mô hình học sâu đạt ACER dưới 5% trong cùng một tập dữ liệu nhưng HTER trên 20% khi chuyển sang tập dữ liệu khác [35], và một phép kiểm thử độc lập trên một mô hình nền tảng năm 2025 đo được ACER 4,2% trong cùng tập dữ liệu so với 37,3% chéo tập dữ liệu [105]. Vì vậy, độ chính xác trên một tập dữ liệu đã biết chỉ là bằng chứng yếu về độ bền vững khi triển khai thực tế.

(2) **Tiến bộ được báo cáo phụ thuộc vào điều kiện kiểm thử.** HTER trung bình trên các tập dữ liệu chưa từng gặp của giao thức O/C/I/M đã giảm từ 23,09% năm 2019 xuống 3,01% năm 2023 [44], [66]. Những con số này dựa trên dữ liệu huấn luyện cụ thể: cả FLIP và FSFM đều bổ sung CelebA-Spoof vào giao thức [66], [102], và HTER trung bình của FSFM tăng từ 4,81% lên 8,88% khi không có tập dữ liệu này [102]. Kết quả chỉ so sánh được với nhau khi dữ liệu huấn luyện và giao thức đồng nhất.

(3) **Mối đe dọa đã vượt ra ngoài cảm biến.** Tấn công trình diện nhìn chung được thực hiện thủ công và ở quy mô nhỏ, trong khi tấn công chèn dữ liệu dễ nhân rộng hơn nhiều [21]; ENISA cho biết "theo các bên tham gia thị trường, chèn video là phương thức tấn công triển vọng nhất" [67], và hai loại tấn công này nay là hai nhóm mối đe dọa chính đối với xác minh khuôn mặt từ xa [10]. Do đó, cổng PAD bảo vệ camera, còn một bộ phát hiện tấn công chèn dữ liệu riêng bảo vệ luồng dữ liệu.

(4) **Niềm tin được xác lập bằng kiểm thử độc lập.** Bằng chứng bảo đảm của lĩnh vực đến từ các tổ chức hơn là từ các bài báo về phương pháp: 273 thư xác nhận của một phòng thí nghiệm được công nhận [20], một đánh giá chuẩn của cơ quan nhà nước trên 82 thuật toán từ 45 nhà phát triển [31], và một quy định ngân hàng yêu cầu PAD được chứng nhận đạt ISO 30107 Cấp độ 2 hoặc cấp độ tương đương [98]. Ở quy mô quốc gia, hơn 173 triệu hồ sơ khách hàng cá nhân tại Việt Nam đã được đối chiếu sinh trắc học tính đến ngày 11/9/2026 [101], và ngân hàng trung ương gắn chương trình này với mức giảm hơn 59% số vụ lừa đảo [100].

(5) **Tính mở biến tuyên bố thành bằng chứng kiểm chứng được.** FSFM công bố mã nguồn và trọng số vào tháng 12/2024 [106], và các nhà nghiên cứu độc lập đã đánh giá mô hình theo giao thức riêng của họ vào năm 2026 [105], [110]. Ngược lại, kho mã của CDCN không có checkpoint tiền huấn luyện nào [62], nên kết quả của nó chỉ tái lập được bằng cách huấn luyện lại. Trọng số được công bố rút ngắn con đường từ một kết quả công bố đến một phép đo độc lập. Bảng 5.1 đặt năm kết luận cạnh bằng chứng và hệ quả của chúng.

**Bảng 5.1. Các kết luận chính, bằng chứng và hệ quả**

| Kết luận | Bằng chứng | Hệ quả |
| :---- | :---- | :---- |
| Tấn công đã biết được phát hiện tốt; điều kiện chưa từng gặp thì chưa | APCER và BPCER ≤ 0,01 với tấn công in, phát lại và mặt nạ ở nhiều nhà phát triển, không thuật toán nào bắt được mọi loại tấn công [31], [91]; ACER 4,2% so với 37,3% trong cùng tập và chéo tập dữ liệu [105] | Yêu cầu kết quả chéo tập dữ liệu và với tấn công chưa từng gặp, thay vì độ chính xác trong cùng tập dữ liệu |
| Tiến bộ được báo cáo phụ thuộc vào điều kiện kiểm thử | HTER trung bình O/C/I/M từ 23,09% xuống 3,01%, giai đoạn 2019–2023 [44], [66]; HTER từ 4,81% lên 8,88% khi không có CelebA-Spoof [102] | Chỉ so sánh các phương pháp khi dữ liệu huấn luyện và giao thức đồng nhất |
| Mối đe dọa đã vượt ra ngoài cảm biến | Tấn công chèn dữ liệu dễ nhân rộng hơn nhiều so với tấn công trình diện [21]; chèn video được xem là phương thức triển vọng nhất [67] | Kết hợp PAD với phát hiện tấn công chèn dữ liệu trong xác minh từ xa |
| Niềm tin được xác lập bằng kiểm thử độc lập | 273 thư xác nhận [20]; 82 thuật toán được đánh giá [31]; PAD được chứng nhận Cấp độ 2 trong pháp luật [98] | Lấy cấp độ chứng nhận và kết quả đánh giá chuẩn làm căn cứ mua sắm |
| Tính mở biến tuyên bố thành bằng chứng kiểm chứng được | Trọng số FSFM được công bố và đánh giá độc lập [106], [105]; CDCN không có checkpoint [62] | Ưu tiên các phương pháp công bố trọng số để đánh giá và so sánh |
