### 1.3.5. Tổng hợp các cách phân loại

Các trục cấp hệ thống ở Mục 1.2 và các nhóm kỹ thuật ở Mục 1.3.1 đến 1.3.3 mô tả cùng các phương pháp từ hai hướng. Góc nhìn hệ thống hỏi bằng chứng đến từ đâu và người dùng làm gì; góc nhìn kỹ thuật hỏi bộ phát hiện khai thác tín hiệu nào [30]. Bảng 1.11 kết hợp hai góc nhìn và bổ sung đặc điểm tổng quát hóa từ Mục 1.3.4, còn Hình 1.2 thể hiện cùng cấu trúc đó dưới dạng cây.

**Bảng 1.11. Các nhóm kỹ thuật đặt trên các trục cấp hệ thống**

| Nhóm kỹ thuật | Nguồn bằng chứng | Vai trò người dùng | Đầu vào | Điểm mạnh điển hình | Giới hạn tổng quát hóa |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Kết cấu và tần số [30] | Phần mềm trên ảnh RGB [26] | Thụ động [10] | Một ảnh [30] | Khác biệt về vi kết cấu, màu sắc và vân moiré của ảnh in và màn hình [30] | Kết cấu màu đạt HTER 28,09–63,59% trên tập dữ liệu chưa từng gặp [42] |
| Chuyển động và sinh lý [30] | Phần mềm trên video [30] | Thụ động (chớp mắt, rPPG) hoặc chủ động (thử thách – phản hồi) [35], [26] | Video [35] | rPPG phát hiện ảnh và mặt nạ 3D chất lượng cao [30] | Bị video phát lại bắt chước; thời gian quan sát dài [35], [40] |
| Hình học 3D [30] | Cảm biến độ sâu phần cứng [26], hoặc phần mềm qua giám sát độ sâu giả [30] | Thụ động [27], [29] | Bản đồ độ sâu hoặc ảnh [26], [30] | Tách tấn công phẳng khỏi khuôn mặt có độ sâu [30] | Phần cứng chuyên dụng đắt tiền và không sẵn có rộng rãi [26] |
| Bộ phân loại sâu với giám sát nhị phân hoặc phụ trợ [35] | Phần mềm [35] | Thụ động [10] | Ảnh hoặc video [35] | ACER dưới 5% trong cùng một tập dữ liệu [35] | HTER trên 20% khi kiểm thử chéo tập dữ liệu với phần lớn mô hình sâu [35] |

![Hình 1.2. Phân loại PAD](assets/figures/task2-1-2-pad-taxonomy.png){width=100%}

Từ bảng có thể rút ra hai kết luận. Thứ nhất, mọi nhóm kỹ thuật, dù ở vị trí nào trên các trục hệ thống, đều bị giới hạn bởi khả năng chuyển giao sang dữ liệu, kiểu tấn công và thiết bị mới nhiều hơn là bởi những gì chúng phát hiện được trong một tập dữ liệu đã biết [35], [42]. Thứ hai, lịch sử của lĩnh vực trong Phần 2 có thể được đọc như một chuỗi lời giải cho vấn đề tổng quát hóa này, từ các tín hiệu thủ công qua giám sát phụ trợ đến tổng quát hóa miền và cuối cùng là mô hình nền tảng của Phần 4.
