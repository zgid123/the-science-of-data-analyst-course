### 4.2.2. Cách che giúp học cấu trúc khuôn mặt

Điều mạng học được phụ thuộc vào phần bị che, vì mạng học cách suy ra phần bị che từ phần còn nhìn thấy. Do đó, FSFM thiết kế cách che dựa trên cấu trúc của khuôn mặt. Trước tiên, một bộ phân vùng khuôn mặt chia mỗi khuôn mặt thành các vùng: lông mày, mắt, miệng, mũi, tóc, da, nền và đường biên khuôn mặt [102]. Hình 4.2 so sánh ba cách che 75% khuôn mặt.

![Hình 4.2. Ba chiến lược che trên một khuôn mặt dạng sơ đồ (vẽ lại theo mô tả trong [102])](assets/figures/task2-4-2-masking-strategies.png){width=100%}

Che ngẫu nhiên đơn thuần không xét đến khuôn mặt, nên thường che kín những vùng nhỏ nhưng giàu thông tin như đôi mắt [102]. Che cùng một tỷ lệ trong mọi vùng, gọi là che theo tỷ lệ, giữ cho vùng nào cũng còn một phần nhìn thấy; tuy nhiên, cách này tạo ra một lối tắt, vì một vùng có thể được điền lại từ chính các mảnh còn sót của nó mà không cần hiểu phần còn lại của khuôn mặt [102].

Chiến lược của FSFM, che kín một vùng khuôn mặt ngẫu nhiên rồi che theo tỷ lệ (CRFR-P), kết hợp ưu điểm của cả hai [102]. Chiến lược này che kín một vùng được chọn ngẫu nhiên, chẳng hạn mũi hoặc miệng, rồi che một tỷ lệ bằng nhau ở mỗi vùng còn lại cho đến khi 75% khuôn mặt bị che [102]. Vùng bị che kín chỉ có thể được dựng lại từ phần khuôn mặt xung quanh, nhờ đó mạng học được mối liên hệ giữa các vùng; phần còn lại bị che đều tay vẫn đòi hỏi chi tiết tinh trong từng vùng [102]. Nhóm tác giả mô tả đây là "một nhiệm vụ MIM không tầm thường và có ý nghĩa", trong đó mô hình hóa ảnh bị che (MIM) là tên gọi của bài tập che rồi dựng lại này [102].

Nhờ vậy, mạng học được vị trí đôi mắt phải nằm khi biết vị trí mũi, kết cấu da tiếp diễn thế nào bên kia một đường biên, và các bộ phận của một khuôn mặt gắn kết với nhau ra sao, tức chính những hiểu biết mà các ảnh giả mạo và tấn công trình diện thường vi phạm.
