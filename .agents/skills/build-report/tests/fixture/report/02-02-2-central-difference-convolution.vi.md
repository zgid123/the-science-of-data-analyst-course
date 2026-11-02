### 2.2.2. Tích chập sai phân trung tâm

Hai năm sau giám sát phụ trợ, Yu, Zhao và cộng sự thuộc Đại học Oulu, Viện Khoa học Mininglamp, Aibee và Đại học Bách khoa Tây Bắc đã thay đổi chính khối xây dựng của mạng. CDCN của họ được công bố ngày 9/3/2020 và được chấp nhận tại CVPR 2020 [57]. Phương pháp giải quyết hai điểm hạn chế: các lớp tích chập thông thường xếp chồng "yếu trong việc mô tả thông tin chi tiết tinh vi và dễ mất hiệu quả khi môi trường thay đổi (ví dụ ánh sáng khác nhau)", và các chuỗi đầu vào dài khó triển khai ở những nơi cần phản hồi nhanh [57]. Vì vậy, CDC làm việc trên từng khung hình và tổng hợp cả thông tin cường độ lẫn gradient [57].

Toán tử này bổ sung một thành phần gradient vào phép tích chập thông thường. Với vị trí đầu ra $p_0$, vùng lân cận $\mathcal{R}$, trọng số $w$ và đầu vào $x$ [57]:

$$y(p_0) = \theta \sum_{p_n \in \mathcal{R}} w(p_n)\,\big(x(p_0 + p_n) - x(p_0)\big) + (1 - \theta) \sum_{p_n \in \mathcal{R}} w(p_n)\,x(p_0 + p_n)$$

Siêu tham số $\theta \in [0, 1]$ cân bằng giữa thông tin ở mức gradient và mức cường độ, và với $\theta = 0$ toán tử trở về phép tích chập thông thường [57]. Trong thí nghiệm loại bỏ thành phần trên Giao thức 1 của OULU-NPU, $\theta = 0.7$ cho ACER tốt nhất là 1,0%, so với 3,8% của tích chập thông thường [57]. CDCN giữ lại giám sát độ sâu của Mục 2.2.1, dự đoán bản đồ độ sâu khuôn mặt kích thước 32 × 32 với hàm mất mát sai số bình phương trung bình và hàm mất mát độ sâu tương phản [57]. CDCN++ tiến thêm một bước: tìm kiếm kiến trúc mạng nơ-ron (NAS) trên một không gian tìm kiếm riêng cho CDC, cách tiếp cận NAS đầu tiên cho chống giả mạo khuôn mặt, tìm ra mạng nền, sau đó được kết hợp với một mô-đun hợp nhất chú ý đa tỉ lệ [57].

Kết quả trong Bảng 2.6 cho thấy mức cải thiện. CDCN++ đạt ACER 0,2%, 1,3%, 1,8% và 5,0% trên bốn giao thức của OULU-NPU và từ 1,90% trở xuống trên SiW [57]. Khi kiểm thử chéo, phương pháp giảm HTER từ CASIA-FASD sang Replay-Attack xuống 6,5%, so với 27,6% của giám sát phụ trợ, trong khi chiều ngược lại vẫn ở mức 29,8% [57]. Trên các kiểu tấn công chưa từng gặp của SiW-M, phương pháp đạt ACER trung bình 12,7%, cải thiện 24% so với kết quả tốt nhất trước đó [57].

**Bảng 2.6. Kết quả được báo cáo của CDCN++ (Yu và cộng sự, 2020)**

| Bộ đánh giá chuẩn | Giao thức | Kết quả |
| :---- | :---- | :---- |
| OULU-NPU | Giao thức 1 / 2 / 3 / 4 | ACER 0,2% / 1,3% / 1,8% / 5,0% [57] |
| SiW | Giao thức 1 / 2 / 3 | ACER 0,12% / 0,04% / 1,90% [57] |
| CASIA-FASD và Replay-Attack | Kiểm thử chéo, cả hai chiều | HTER 6,5% và 29,8% [57] |
| SiW-M | Loại trừ từng kiểu tấn công | ACER trung bình 12,7%, EER 11,9% [57] |

Phương pháp cũng chứng minh năng lực trong thi đấu mở. Tại cuộc thi ChaLearn Face Anti-spoofing Attack Detection Challenge ở CVPR 2020, do ChaLearn tổ chức cùng CASIA, đội BOBO của Oulu do Zitong Yu dẫn dắt giành hạng nhất ở hạng mục đa phương thức với ACER 1,02% và hạng nhì ở hạng mục đơn phương thức (RGB) với 4,84%, sau VisionLabs [60], [62]. Bài báo có 592 trích dẫn trên Crossref tính đến ngày 2/10/2026 [57]. Kho mã chính thức công bố mã huấn luyện, bộ nạp dữ liệu và định nghĩa mô hình theo một giấy phép MIT sửa đổi dành cho nghiên cứu, và không chứa tệp trọng số đã huấn luyện nào (kiểm tra ngày 2/10/2026) [62]. Bản thân OULU-NPU, tập dữ liệu mà bộ nạp dữ liệu của kho mã hướng tới, chỉ được cung cấp theo một thỏa thuận cấp phép người dùng cuối (EULA) có chữ ký [63].
