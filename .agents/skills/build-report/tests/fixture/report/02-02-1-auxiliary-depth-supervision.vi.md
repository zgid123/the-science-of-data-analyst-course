### 2.2.1. Giám sát phụ trợ bằng độ sâu và rPPG

Liu, Jourabloo và Liu bắt đầu từ việc chẩn đoán cách huấn luyện nhị phân. Một CNN được huấn luyện với hàm mất mát softmax "có thể tìm ra những tín hiệu tùy ý có khả năng tách hai lớp, chẳng hạn viền màn hình" [45], và nó "chỉ đưa ra một quyết định nhị phân mà không có lời giải thích hay lý do cho quyết định đó" [45]. Lời giải của họ là giám sát mạng bằng hai tín hiệu vật lý mà khuôn mặt sống tạo ra còn vật giả mạo thì không.

Mô hình kết hợp một CNN với một mạng nơ-ron hồi quy. CNN ước lượng bản đồ độ sâu của khuôn mặt dưới giám sát theo từng điểm ảnh, phần hồi quy ước lượng tín hiệu rPPG dưới giám sát theo chuỗi, và một lớp đăng ký không cứng dùng hình dạng 3D dày đặc đã ước lượng để căn chỉnh các bản đồ đặc trưng của CNN cho phần hồi quy [45]. Nhãn độ sâu tuân theo ý tưởng đã mô tả ở Mục 1.3.3: với khuôn mặt sống, các đỉnh khuôn mặt 3D được khớp và chuẩn hóa sao cho "đỉnh gần camera nhất (ví dụ mũi) có độ sâu bằng một" [45], còn video giả mạo nhận một bề mặt phẳng có độ sâu bằng không [45]. Độ sâu và rPPG ước lượng được sau đó được hợp nhất thành một điểm số sống hay giả, với một trọng số không đổi kết hợp hai đầu ra [45]. Giới hạn bộ nhớ khiến đầu vào chỉ ở kích thước 128 × 128 điểm ảnh trong mọi thí nghiệm [45].

Cùng bài báo này giới thiệu tập dữ liệu Spoof in the Wild (SiW). Tập dữ liệu cung cấp video 30 khung hình mỗi giây của 165 đối tượng, mỗi đối tượng có 8 video sống và 20 video giả mạo, tổng cộng 4.620 video, với video sống ở độ phân giải 1.920 × 1.080 điểm ảnh [45]. Bốn phiên ghi hình thay đổi khoảng cách tới camera, tư thế đầu trong khoảng góc xoay từ –90° đến 90° kèm biểu cảm khuôn mặt, và ánh sáng từ một nguồn điểm được di chuyển quanh khuôn mặt [45]. Mỗi đối tượng có hai kiểu tấn công bằng ảnh in và bốn kiểu tấn công phát lại, với video phát lại trên màn hình Samsung Galaxy S8, iPhone 7, iPad Pro và máy tính [45].

Kết quả được báo cáo tổng hợp trong Bảng 2.5. Trên OULU-NPU, mô hình đạt ACER từ 1,6% đến 9,5% qua bốn giao thức, và trên SiW từ 0,57% đến 8,31% [45]. Khi kiểm thử chéo giữa CASIA-FASD và Replay-Attack, mô hình đạt HTER 27,6% và 28,4%, so với 48,5% và 45,5% của một CNN nhị phân và 30,3% và 37,7% của phương pháp kết cấu màu ở Mục 2.1.1 [45].

**Bảng 2.5. Kết quả được báo cáo của giám sát phụ trợ bằng độ sâu và rPPG (Liu và cộng sự, 2018)**

| Bộ đánh giá chuẩn | Giao thức | ACER hoặc HTER |
| :---- | :---- | :---- |
| OULU-NPU | Giao thức 1 / 2 / 3 / 4 | ACER 1,6% / 2,7% / 2,9% / 9,5% [45] |
| SiW | Giao thức 1 / 2 / 3 | ACER 3,58% / 0,57% / 8,31% [45] |
| CASIA-FASD và Replay-Attack | Kiểm thử chéo, cả hai chiều | HTER 27,6% và 28,4%; CNN nhị phân 48,5% và 45,5% [45] |

Bài báo đã biến giám sát phụ trợ thành thiết kế chuẩn của giai đoạn, và có 593 trích dẫn trên Crossref tính đến ngày 2/10/2026 [45]. Giới hạn của nó xuất hiện một năm sau với các kiểu tấn công chưa từng gặp, khi cùng mô hình này đạt ACER trung bình 23,6% trên SiW-M [56].
