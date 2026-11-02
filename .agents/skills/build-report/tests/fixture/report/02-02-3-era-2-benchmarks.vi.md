### 2.2.3. Bộ đánh giá chuẩn và các cuộc thi

Các phương pháp ở Mục 2.2.1 và 2.2.2 được đo trên một thế hệ tập dữ liệu mới, lớn hơn về số đối tượng và rộng hơn về kiểu tấn công lẫn cảm biến. Bảng 2.7 tổng hợp các tập dữ liệu này cùng điều kiện truy cập, những điều kiện biến chúng thành tài nguyên nghiên cứu thay vì dữ liệu tải xuống tự do.

**Bảng 2.7. Các bộ đánh giá chuẩn PAD khuôn mặt của Giai đoạn 2**

| Tập dữ liệu | Năm và nhóm | Đối tượng và video | Phương thức và kiểu tấn công | Điều kiện truy cập |
| :---- | :---- | :---- | :---- | :---- |
| OULU-NPU | 2017, Đại học Oulu (Mục 1.3.4) | 55 đối tượng, 4.950 video [43] | RGB; ảnh in và phát lại [43] | EULA do một nhân viên biên chế ký; không chấp nhận địa chỉ thư điện tử công cộng [63] |
| SiW | 2018, Đại học Bang Michigan [45] | 165 đối tượng, 4.620 video [45] | RGB; ảnh in và phát lại [45] | Thỏa thuận cung cấp dữ liệu do người hướng dẫn ký; chỉ dùng cho nghiên cứu nội bộ [64] |
| SiW-M | 2019, Đại học Bang Michigan [56] | 493 đối tượng sống; 660 video sống và 968 video giả mạo [56] | RGB; 13 kiểu tấn công, kể cả mặt nạ 3D [56] | – |
| CASIA-SURF | 2019, Viện Hàn lâm Khoa học Trung Quốc [58] | 1.000 đối tượng, 21.000 video [58] | RGB, độ sâu và hồng ngoại (IR); sáu kiểu tấn công bằng ảnh in khoét lỗ [58] | Thỏa thuận có chữ ký và thể lệ cuộc thi [65] |
| CASIA-SURF CeFA | 2020, Viện Hàn lâm Khoa học Trung Quốc [59] | 1.607 đối tượng, 23.538 video; ba sắc tộc [59] | RGB, độ sâu và IR; tấn công 2D và 3D [59] | Thỏa thuận cấp phép có chữ ký; giấy phép thương mại riêng [65] |

Mỗi tập dữ liệu bổ sung một chiều khó mới. CASIA-SURF, được ghi bằng camera Intel RealSense SR300, là tập dữ liệu lớn nhất về số đối tượng và video tại thời điểm công bố [58]. SiW-M giới thiệu một giao thức loại trừ từng kiểu, trong đó mô hình huấn luyện trên 12 kiểu tấn công và được kiểm thử trên kiểu bị giữ lại [56], nhờ đó đo trực tiếp hiệu năng trên các kiểu tấn công chưa từng gặp. CeFA là tập dữ liệu PAD khuôn mặt đầu tiên có nhãn sắc tộc rõ ràng, gồm các đối tượng người châu Phi, Đông Á và Trung Á với 500 đối tượng cho mỗi sắc tộc trong tập con 2D, còn các tập con mặt nạ 3D bổ sung thêm 99 và 8 đối tượng [59].

Hai cuộc thi ChaLearn đã biến các tập dữ liệu này thành những cuộc tranh tài công khai. Cuộc thi năm 2019 sử dụng CASIA-SURF; hơn 300 tổ chức học thuật và công nghiệp tham gia, 13 đội vào vòng chung kết [61], và VisionLabs giành chiến thắng với tỷ lệ dương tính thật 99,8739% tại tỷ lệ dương tính giả $10^{-4}$ [61]. Cuộc thi năm 2020 sử dụng CeFA nhằm giải quyết thiên lệch sắc tộc, với một hạng mục đơn phương thức (RGB) và một hạng mục đa phương thức (RGB, độ sâu và IR) [60]. Giao thức 4 của cuộc thi huấn luyện trên một sắc tộc với tấn công phát lại và kiểm thử trên hai sắc tộc còn lại với tấn công bằng ảnh in [60]. Tổng cộng 340 đội tham gia giai đoạn phát triển, lần lượt 11 và 8 đội nộp mã ở hạng mục đơn phương thức và đa phương thức, và ban tổ chức chạy lại toàn bộ kết quả [60]. Các bài dự thi tốt nhất giảm ACER từ 36,62% xuống 2,72% ở hạng mục đơn phương thức và từ 32,02% xuống 1,02% ở hạng mục đa phương thức [60].

Các bộ đánh giá chuẩn này giúp đo lường được bài toán của Giai đoạn 3. Những giao thức kiểm thử chéo kiểu tấn công, sắc tộc và cảm biến trở thành phép thử chuẩn cho khả năng tổng quát hóa [60], [61].
