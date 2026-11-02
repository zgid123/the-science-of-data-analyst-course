### 1.2.2. PAD thụ động và chủ động

Trục thứ hai liên quan đến việc người dùng được yêu cầu làm gì. PAD thụ động phân tích chính mẫu đã thu: các mô hình thụ động dùng một ảnh tìm kiếm vết giả hoặc điểm bất thường trong dữ liệu đầu vào [10]. Mô hình thụ động mang lại trải nghiệm người dùng rất tốt với mức phiền hà tối thiểu [10], và đánh giá chuẩn NIST FATE Phần 10 đánh giá chính xác nhóm thụ động này [31]. Việc chỉ dựa vào một ảnh thu được cũng xác định giới hạn của chúng, vì các mô hình dùng một ảnh nhìn chung không hiệu quả trước tấn công phát lại số [10].

PAD chủ động, còn gọi là thử thách – phản hồi, đưa ra một thử thách cho người dùng, chẳng hạn hoàn thành một nhiệm vụ định trước, hoặc đặt người dùng trước một kích thích để ghi nhận phản hồi có chủ ý hoặc không chủ ý [26]. Các phản hồi điển hình gồm chuyển động mắt và đọc các từ định trước [26]. Các phương pháp thử thách – phản hồi hiệu quả trước nhiều kiểu tấn công trình diện, song thường đòi hỏi nhiều thời gian và sự hợp tác hơn từ người dùng, điều không phải lúc nào cũng khả thi hay mong muốn [26]. Do đó, trục này đánh đổi sự thuận tiện lấy độ mạnh của bằng chứng về sự sống.

Một nhóm thứ ba để thiết bị tự đưa ra thử thách mà không yêu cầu người dùng thao tác. Mô hình mối đe dọa của AWS đề xuất một cách tiếp cận chủ động, khai thác khả năng của cảm biến để cảm nhận và tạo ảnh tích cực [10]. Face Flashing, một phương pháp năm 2018, chiếu ngẫu nhiên các hình ảnh được thiết kế sẵn lên màn hình và phân tích ánh sáng phản xạ từ khuôn mặt [32]. Phương pháp này khai thác tốc độ phản xạ ánh sáng, kết cấu khuôn mặt và hình dạng 3D không phẳng của khuôn mặt thật, và báo cáo độ chính xác tổng thể 98,8% [32]. Những thử thách ánh sáng như vậy kết hợp trải nghiệm thụ động với một kích thích chủ động, và Bảng 1.6 đặt chúng vào giữa hai đầu của trục.

**Bảng 1.6. PAD thụ động, chủ động và lai**

| Nhóm | Thao tác của người dùng | Bằng chứng | Điểm mạnh | Điểm hạn chế |
| :---- | :---- | :---- | :---- | :---- |
| Thụ động | Không có | Vết giả trong một ảnh hoặc đoạn video ngắn [10] | Phiền hà tối thiểu [10] | Yếu trước tấn công phát lại số [10] |
| Chủ động (thử thách – phản hồi) | Hoàn thành một nhiệm vụ, ví dụ chuyển động mắt hoặc đọc từ [26] | Phản hồi có chủ ý hoặc không chủ ý [26] | Hiệu quả trước nhiều kiểu tấn công trình diện [26] | Tốn thêm thời gian và sự hợp tác [26] |
| Lai (thử thách từ thiết bị) | Không có; màn hình phát kích thích [32] | Ánh sáng phản xạ, kết cấu, hình dạng 3D [32] | Bằng chứng chủ động với trải nghiệm thụ động; độ chính xác 98,8% do nhóm tác giả báo cáo [32] | – |
