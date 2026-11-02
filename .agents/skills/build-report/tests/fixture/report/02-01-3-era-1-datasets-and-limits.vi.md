### 2.1.3. Các tập dữ liệu ban đầu và giới hạn của chúng

Các phương pháp ở Mục 2.1.1 và 2.1.2 được phát triển trên một số ít tập dữ liệu công khai, được liệt kê trong Bảng 2.3. NUAA, do Tan, Li, Liu và Jiang giới thiệu tại Hội nghị Thị giác máy tính châu Âu (ECCV) năm 2010 [52], gồm 5.105 ảnh sống và 7.509 ảnh giả mạo của 15 đối tượng với tấn công bằng ảnh in phẳng và ảnh in uốn cong [35]. Print-Attack (2011) gồm 200 video tấn công bằng ảnh in và 200 video truy cập thật của 50 người dùng [47]. CASIA-FASD, do Zhang và cộng sự thuộc Viện Hàn lâm Khoa học Trung Quốc công bố tại Hội nghị Quốc tế về Sinh trắc học năm 2012 [53], gồm 150 video sống và 450 video giả mạo của 50 đối tượng trong 7 kịch bản và 3 mức chất lượng ảnh, với ảnh in phẳng, uốn cong, khoét lỗ và phát lại trên máy tính bảng [35]. Replay-Attack (2012) được trang cơ sở dữ liệu mô tả là gồm 1.300 đoạn video về các lần tấn công bằng ảnh và video nhắm vào 50 người dùng trong các điều kiện ánh sáng khác nhau, còn bảng trong công trình tổng quan ghi nhận 200 video sống và 1.000 video giả mạo [54], [35]; dữ liệu được quay bằng webcam máy tính xách tay ở độ phân giải 320 × 240 điểm ảnh và bị tấn công bằng iPhone 3GS, iPad thế hệ đầu và ảnh in [54]. MSU-MFSD, được công trình tổng quan về học sâu nêu ở Mục 1.3 ghi năm 2014 [35] và được mô tả trên IEEE Transactions on Information Forensics and Security năm 2015 [55], gồm 70 video sống và 210 video giả mạo của 35 đối tượng, quay bằng máy tính xách tay và điện thoại Android [35], [55].

**Bảng 2.3. Các tập dữ liệu PAD khuôn mặt công khai của Giai đoạn 1**

| Tập dữ liệu | Năm | Số đối tượng | Quy mô (sống / giả mạo) | Kiểu tấn công | Thu nhận |
| :---- | :---- | :---- | :---- | :---- | :---- |
| NUAA [52], [35] | 2010 | 15 | 5.105 / 7.509 ảnh | Ảnh in: phẳng, uốn cong | – |
| Print-Attack [47] | 2011 | 50 | 200 / 200 video | Ảnh in: cố định hoặc cầm tay | – |
| CASIA-FASD [53], [35] | 2012 | 50 | 150 / 450 video | Ảnh in: phẳng, uốn cong, khoét lỗ; phát lại trên máy tính bảng | 7 kịch bản, 3 mức chất lượng ảnh |
| Replay-Attack [54], [35] | 2012 | 50 | 200 / 1.000 video | Ảnh in; phát lại trên điện thoại và máy tính bảng | Webcam máy tính xách tay, 320 × 240 điểm ảnh |
| MSU-MFSD [35], [55] | 2014 (bài báo 2015) | 35 | 70 / 210 video | Ảnh in; phát lại trên điện thoại và máy tính bảng | Máy tính xách tay và điện thoại Android |

Các tập dữ liệu này có ba đặc điểm chung: từ 15 đến 50 đối tượng, một hoặc hai thiết bị thu nhận, và chỉ có tấn công bằng ảnh in và phát lại. Do đó, một phương pháp có thể khớp rất sát với một tập dữ liệu, và các bài kiểm thử chéo tập dữ liệu đã bộc lộ điều này. Khi huấn luyện trên một trong hai tập CASIA-FASD và Replay-Attack rồi kiểm thử trên tập còn lại, mốc cơ sở dựa trên chuyển động đạt HTER 50,2% và 47,9%, LBP đạt 55,9% và 57,6%, và LBP-TOP đạt 49,7% và 60,6%, tất cả đều gần 50% [45]. Phương pháp kết cấu màu cho kết quả tốt nhất trong số này, ở mức 30,3% và 37,7% [45], nhưng ngay trong bài báo của chính nó, HTER tăng từ 2,9% trên Replay-Attack lên tới 47,5% khi huấn luyện trên Replay-Attack và kiểm thử trên CASIA-FASD [50]. Chính các tác giả ở Oulu cũng nhận xét rằng "khả năng tổng quát hóa của các phương pháp này vẫn còn đáng nghi ngờ" [50].

**Bảng 2.4. HTER khi kiểm thử chéo của các mốc cơ sở Giai đoạn 1 (CASIA-FASD và Replay-Attack)**

| Phương pháp | Huấn luyện CASIA-FASD, kiểm thử Replay-Attack | Huấn luyện Replay-Attack, kiểm thử CASIA-FASD |
| :---- | :---- | :---- |
| Chuyển động | 50,2% | 47,9% |
| LBP | 55,9% | 57,6% |
| LBP-TOP | 49,7% | 60,6% |
| Kết cấu màu | 30,3% | 37,7% |

Nguồn: [45].

Đánh giá về giai đoạn này rút ra trực tiếp từ các con số trên. Các phương pháp thủ công trở nên kém tin cậy do năng lực biểu diễn hạn chế, và khi các tập dữ liệu quy mô lớn xuất hiện, học sâu đã chiếm ưu thế trong lĩnh vực [35]. Phương pháp học sâu đầu-cuối đầu tiên đã lập luận rằng LBP và LBP-TOP "vẫn chưa nắm bắt được những tín hiệu phân biệt rõ nhất giữa khuôn mặt thật và giả" [49], và Mục 2.2 theo dõi các bộ phân loại sâu đã thay thế chúng.
