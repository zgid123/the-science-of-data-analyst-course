### 1.2.1. PAD dựa trên phần cứng và dựa trên phần mềm

PAD dựa trên phần cứng bổ sung các cảm biến đo những đặc tính mà ảnh in, màn hình hay mặt nạ khó tái tạo. Các tiếp cận phần cứng chuyên dụng sử dụng camera cận hồng ngoại (NIR), cảm biến nhiệt, camera trường ánh sáng, cảm biến đa phổ và camera 3D [26]. Các cảm biến này đọc trực tiếp bằng chứng vật lý, chẳng hạn nhiệt độ từ camera nhiệt và thể tích 3D của vật giả từ cảm biến thu nhận 3D [26]. Bên cạnh đó, da người có đặc tính phản xạ riêng ở các bước sóng hồng ngoại sóng ngắn (SWIR) đa phổ, không phụ thuộc vào tuổi, giới tính hay loại da của đối tượng [6], nhờ đó cảm biến phổ có được một dấu hiệu vật lý của làn da sống.

Hai hệ thống tiêu dùng được triển khai rộng rãi cho thấy PAD phần cứng trong thực tế. Face ID của Apple chiếu và phân tích hàng nghìn điểm vô hình để dựng bản đồ độ sâu của khuôn mặt, đồng thời thu thêm một ảnh hồng ngoại [27]. Để chống giả mạo số và vật lý, camera TrueDepth ngẫu nhiên hóa trình tự chụp ảnh 2D và ảnh độ sâu, đồng thời chiếu một mẫu ngẫu nhiên riêng cho từng thiết bị [28]. Xác thực khuôn mặt Windows Hello của Microsoft dùng camera được cấu hình để chụp ảnh NIR [29], và Microsoft cho biết ảnh hồng ngoại ngăn được các cuộc tấn công dễ thực hiện nhất vì ánh sáng hồng ngoại không hiển thị trên ảnh chụp hay màn hình tinh thể lỏng [29]. Các tiếp cận phần cứng thường đạt tỷ lệ phát hiện cao, song vẫn ít phổ biến hơn vì phần cứng cần thiết đắt tiền và không sẵn có rộng rãi [26].

PAD dựa trên phần mềm làm việc trên dữ liệu mà một camera thông thường đã tạo ra. Cách tiếp cận này nâng cấp biện pháp đối phó của hệ thống hiện có mà không cần phần cứng mới, xác thực theo thời gian thực mà không cần người dùng thao tác thêm [26], và quyết định giữa trình diện hợp lệ và tấn công bằng thuật toán, không phụ thuộc vào thiết bị thu nhận [25]. Một hướng nghiên cứu riêng tập trung vào PAD khuôn mặt chỉ cần camera đỏ, lục, lam (RGB) của các thiết bị tiêu dùng phổ thông, được phát triển trong hai thập kỷ [30]. Các phương pháp phần mềm chia thành phân tích tĩnh trên từng khung hình và phân tích động trên thông tin theo thời gian [26]. Đây cũng chính là nhóm mà hoạt động đánh giá chuẩn của cơ quan nhà nước hướng tới: Face Analysis Technology Evaluation (FATE) Phần 10 của NIST đánh giá các thuật toán PAD khuôn mặt thụ động, thuần phần mềm, hoạt động trên ảnh 2D thông thường [31]. Hạn chế chính của PAD phần mềm là khả năng tổng quát hóa, vì hiệu năng thường giảm đáng kể khi mô hình được kiểm thử trên các cơ sở dữ liệu khác [26].

Trục này mô tả nguồn bằng chứng chứ không chia các sản phẩm thành hai nhóm loại trừ nhau. Face ID kết hợp cảm biến chuyên dụng với các mạng nơ-ron chống giả mạo trước mặt nạ và các hình thức giả mạo khác [27], vì vậy một hệ thống được triển khai thường tận dụng cả hai đầu của trục. Bảng 1.5 so sánh hai nguồn bằng chứng.

**Bảng 1.5. PAD dựa trên phần cứng và dựa trên phần mềm**

| Khía cạnh | PAD dựa trên phần cứng | PAD dựa trên phần mềm |
| :---- | :---- | :---- |
| Bằng chứng | Đo lường vật lý: độ sâu, nhiệt độ, phản hồi NIR và phổ [26], [6] | Nội dung ảnh và video từ camera hiện có [26], [30] |
| Chi phí triển khai | Đắt; cảm biến chuyên dụng không sẵn có rộng rãi [26] | Không cần phần cứng mới; nâng cấp hệ thống hiện có [26] |
| Tương tác người dùng | Không có ngoài bản thân việc thu nhận [27], [29] | Không có; theo thời gian thực [26] |
| Hạn chế chính | Mức độ sẵn có và chi phí [26] | Khả năng tổng quát hóa giữa các cơ sở dữ liệu [26] |
| Ví dụ triển khai hoặc đánh giá | Face ID, Windows Hello [27], [29] | NIST FATE Phần 10 [31] |
