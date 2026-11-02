### 4.2.4. Từ một mạng xương sống đến ba bộ phát hiện

Sau tiền huấn luyện, FSFM chỉ giữ lại bộ mã hóa và gắn thêm một đầu ra nhỏ cho mỗi nhiệm vụ phát hiện [102]. Cùng một bộ mã hóa được tinh chỉnh ba lần, mỗi lần cho một nhiệm vụ và chỉ trên dữ liệu gán nhãn của nhiệm vụ đó [102]:

(1) **DfD.** Bộ phát hiện học từ các video bị chỉnh sửa của bộ sưu tập FaceForensics++ (FF++), rồi được kiểm thử trên bốn tập dữ liệu deepfake chưa từng gặp: CelebDF-v2, DFDC, DFDC preview và WildDeepfake [102].
(2) **FAS.** Bộ phát hiện học từ ba trong bốn tập dữ liệu chống giả mạo công khai, cùng bộ sưu tập CelebA-Spoof làm dữ liệu huấn luyện bổ sung, và được kiểm thử trên tập thứ tư [102].
(3) **Khuôn mặt do AI tạo ra.** Bộ phát hiện chỉ học từ phần DeepFake của FF++ và được kiểm thử trên các khuôn mặt do 13 mô hình khuếch tán khác nhau tạo ra, công nghệ đứng sau các công cụ tạo ảnh hiện nay [102].

Bản trình diễn trực tuyến đã phát hành còn tiến thêm một bước, gộp các nhiệm vụ thành một bộ phát hiện bốn lớp duy nhất, gán cho mỗi khuôn mặt nhãn thật, deepfake, ảnh sinh bằng mô hình khuếch tán hoặc tấn công trình diện [108].

Bản đồ nhiệt (heat map) cho thấy bộ phát hiện nhìn vào đâu khi ra quyết định. Hình 4.4, tái hiện từ bài báo, so sánh một bộ phát hiện xây dựng trên tiền huấn luyện bằng ảnh đời thường, một bộ xây dựng trên MAE đơn thuần, và FSFM. Theo lời nhóm tác giả, "FSFM làm nổi bật các dấu vết giả mạo và manh mối tấn công": trên ảnh deepfake, sự chú ý của nó tập trung vào các phần khuôn mặt bị chỉnh sửa, còn trên tấn công trình diện, vào các manh mối của tấn công [102].

![Hình 4.4. Bộ phát hiện nhìn vào đâu: bản đồ nhiệt trên (a) ảnh deepfake và (b) tấn công trình diện của các mạng xương sống ImageNet có giám sát, MAE và FSFM. Tái hiện từ Wang và cộng sự [102]](assets/figures/task2-4-4-paper-heat-maps.png){width=100%}

Như vậy, một mạng xương sống tiền huấn luyện trở thành ba bộ phát hiện chuyên biệt. Các bộ phát hiện này hoạt động tốt đến đâu, và điều đó được đo lường thế nào, là nội dung của Mục 4.3.
