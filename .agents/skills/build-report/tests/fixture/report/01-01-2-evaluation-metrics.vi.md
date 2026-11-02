### 1.1.2. Các chỉ số đánh giá

Vì mọi lần trình diện đều hoặc là hợp lệ, hoặc là tấn công, hiệu năng PAD được đo bằng hai tỷ lệ lỗi bổ sung cho nhau. Tỷ lệ lỗi phân loại trình diện tấn công (APCER) là "tỷ lệ các lần trình diện tấn công dùng cùng một loại PAI bị phân loại sai thành trình diện hợp lệ trong một kịch bản cụ thể (proportion of attack presentations using the same PAI species incorrectly classified as bona fide presentations in a specific scenario)" [6]. Tỷ lệ lỗi phân loại trình diện hợp lệ (BPCER) là "tỷ lệ các lần trình diện hợp lệ bị phân loại sai thành tấn công trình diện trong một kịch bản cụ thể (proportion of bona fide presentations incorrectly classified as presentation attacks in a specific scenario)" [6]. APCER phản ánh khía cạnh an ninh của một phân hệ PAD, còn BPCER phản ánh khía cạnh thuận tiện của nó.

APCER được tính riêng cho từng loại PAI $S$, và hệ thống được đánh giá theo khâu kém nhất của nó. APCER tổng thể là giá trị APCER lớn nhất trên tất cả các kiểu tấn công được đánh giá, đo tại một ngưỡng quyết định $\tau$ cho trước [13]:

$$\mathrm{APCER}_S(\tau) = \frac{\text{attack presentations of species } S \text{ classified as bona fide}}{\text{attack presentations of species } S}, \qquad \mathrm{APCER}(\tau) = \max_S \mathrm{APCER}_S(\tau)$$

$$\mathrm{BPCER}(\tau) = \frac{\text{bona fide presentations classified as attacks}}{\text{bona fide presentations}}$$

Hạ thấp ngưỡng sẽ đổi loại lỗi này lấy loại lỗi kia, vì vậy các nghiên cứu tuân theo ISO/IEC 30107-3 còn báo cáo tỷ lệ lỗi cân bằng phát hiện (D-EER), tức tỷ lệ lỗi tại điểm vận hành nơi APCER bằng BPCER [11]. Các nghiên cứu PAD có bình duyệt năm 2025 đánh giá mô hình bằng APCER và BPCER theo cách này [14].

Chỉ số thứ ba nhìn xa hơn phân hệ PAD, tới toàn bộ hệ thống sinh trắc học. Tỷ lệ khớp trình diện tấn công mạo danh (IAPMR) là "tỷ lệ các lần trình diện tấn công mạo danh thành công, tức là khi mẫu tham chiếu sinh trắc học của danh tính bị nhắm tới được so khớp (proportion of impostor attack presentations that are successful; that is, in which the biometric reference for the targeted identity is matched)" [2]. Các nghiên cứu gần đây theo chuẩn ISO dùng tên mới là tỷ lệ chấp nhận trình diện tấn công mạo danh (IAPAR) cho đại lượng này [8], và Liên minh FIDO dùng nó để đo khả năng chống giả mạo và deepfake [4]. Chỉ số này cho thấy một phân hệ PAD yếu có thể nghiêm trọng đến mức nào: một nghiên cứu về khuôn mặt in trên áo phông ghi nhận IAPAR khoảng 99% tại các điểm vận hành được chọn [8].

Các cuộc thi và bài báo đánh giá chuẩn thường bổ sung tỷ lệ lỗi phân loại trung bình (ACER), tức trung bình của APCER và BPCER [10]. Việc lấy trung bình hai tỷ lệ này đã không còn được khuyến nghị trong ISO/IEC 30107-3, và ACER chủ yếu được báo cáo để so sánh với các cuộc thi có sử dụng nó [6]. Cuộc thi chống giả mạo khuôn mặt ChaLearn tại Hội nghị Thị giác máy tính và Nhận dạng mẫu (CVPR) năm 2019 viện dẫn các chỉ số của ISO/IEC 30107-3 và định nghĩa ACER của mình là trung bình của APCER và một tỷ lệ lỗi trên trình diện hợp lệ [15]. Các bài báo về PAD khuôn mặt năm 2026 vẫn báo cáo APCER, BPCER và ACER trên bộ đánh giá chuẩn OULU-NPU [16]. Bảng 1.2 tổng hợp bốn chỉ số này.

**Bảng 1.2. Các chỉ số đánh giá PAD**

| Chỉ số | Đo lường | Phạm vi tính | Vị trí trong ISO/IEC 30107-3 | Nguồn |
| :---- | :---- | :---- | :---- | :---- |
| APCER | Tấn công được chấp nhận là hợp lệ | Từng loại PAI; báo cáo giá trị lớn nhất | Chuẩn tắc | [6], [13] |
| BPCER | Trình diện hợp lệ bị từ chối như tấn công | Toàn bộ trình diện hợp lệ | Chuẩn tắc | [6] |
| IAPMR (IAPAR) | Tấn công mạo danh đạt kết quả khớp | Toàn bộ hệ thống sinh trắc học | Chuẩn tắc; tên mới là IAPAR | [2], [8] |
| ACER | Trung bình của APCER và BPCER | Cả hai tỷ lệ lỗi | Không còn khuyến nghị | [10], [6] |

Do đó, một đánh giá theo chuẩn ISO báo cáo APCER, lấy giá trị lớn nhất trên các loại được đánh giá, và BPCER tại một ngưỡng được nêu rõ, bổ sung thêm D-EER [11].
