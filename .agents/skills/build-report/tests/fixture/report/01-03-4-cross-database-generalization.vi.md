### 1.3.4. Khả năng tổng quát hóa chéo cơ sở dữ liệu

Mọi nhóm kỹ thuật trong Mục 1.3.1 đến 1.3.3 đều được đánh giá trên các tập dữ liệu, và cách kiểm thử quyết định ý nghĩa của các con số. Trong kiểm thử trong cùng tập dữ liệu, dữ liệu huấn luyện và kiểm thử được lấy từ cùng một tập và có phân phối miền tương tự; trong kiểm thử chéo tập dữ liệu, mô hình được huấn luyện trên một hoặc vài tập nguồn và được kiểm thử trên các tập đích chưa từng gặp với miền đã dịch chuyển [35]. Kết quả kiểm thử chéo thường được báo cáo bằng một nửa tổng tỷ lệ lỗi (HTER), tức trung bình của tỷ lệ chấp nhận sai (FAR) và tỷ lệ từ chối sai (FRR) [35].

Khả năng tổng quát hóa là vấn đề mở trung tâm của lĩnh vực, vì kết quả trong hai thiết lập này chênh lệch rất lớn. Những phương pháp hoạt động tốt trong một cơ sở dữ liệu không thể tổng quát hóa tốt khi dữ liệu huấn luyện và kiểm thử đến từ các miền khác nhau, vì chúng học các đặc trưng thiên lệch theo cơ sở dữ liệu [42]. Phần lớn các phương pháp quá khớp với tập huấn luyện và thất bại trước các kiểu tấn công và môi trường chưa từng gặp [41]. Bổ sung thêm cơ sở dữ liệu huấn luyện cũng không thu hẹp được khoảng cách này, vì ngay cả khi kết hợp nhiều cơ sở dữ liệu cũng không xử lý được các kiểu tấn công vắng mặt trong dữ liệu huấn luyện [30].

Hai thiết kế đánh giá chuẩn giúp đo lường được vấn đề này. Tập dữ liệu OULU-NPU, công bố năm 2017, gồm 4.950 video truy cập thật và tấn công của 55 đối tượng, được quay bằng camera trước của sáu điện thoại thông minh trong ba phiên với ánh sáng và phông nền khác nhau [43]. Mỗi giao thức trong bốn giao thức của tập dữ liệu giữ lại một yếu tố ngoài quá trình huấn luyện, như Bảng 1.10 thể hiện [43].

**Bảng 1.10. Các giao thức đánh giá của OULU-NPU**

| Giao thức | Yếu tố chưa từng gặp khi kiểm thử |
| :---- | :---- |
| Giao thức I | Điều kiện môi trường: ánh sáng và phông nền [43] |
| Giao thức II | Công cụ tấn công: máy in hoặc màn hình [43] |
| Giao thức III | Cảm biến đầu vào: loại trừ một camera [43] |
| Giao thức IV | Kết hợp môi trường, công cụ tấn công và cảm biến [43] |

Thiết kế thứ hai kiểm thử chéo giữa các tập dữ liệu hoàn chỉnh. Giao thức loại trừ từng tập O/C/I/M sử dụng OULU-NPU, CASIA-FASD, Idiap Replay-Attack và MSU-MFSD, trong đó CASIA-FASD còn được gọi là CASIA-MFSD trong một số bài báo [42]: một tập được chọn làm tập đích chưa từng gặp và ba tập còn lại làm nguồn huấn luyện, tạo thành bốn bài kiểm thử được chấm bằng HTER và diện tích dưới đường cong ROC (AUC) [42].

Các con số cho thấy độ lớn của khoảng cách này. Trong cùng một tập dữ liệu, nhiều phương pháp sâu đạt ACER dưới 5%, nhưng khi huấn luyện trên Replay-Attack và kiểm thử trên CASIA-FASD, phần lớn mô hình sâu có HTER vượt 20% do khác biệt về ánh sáng và độ phân giải camera [35]. Trên bốn bài kiểm thử O/C/I/M, phương pháp kết cấu màu ở Mục 1.3.1 đạt HTER từ 28,09% đến 63,59% và một CNN nhị phân đạt từ 29,25% đến 34,88%, trong khi các phương pháp tổng quát hóa miền giảm được sai số, MADDG xuống còn từ 17,69% đến 27,98% [44] và SSDG-R xuống còn từ 7,38% đến 15,61% [42]. Các phương pháp tổng quát hóa miền này là điểm khởi đầu của giai đoạn thứ ba trong Mục 2.3.
