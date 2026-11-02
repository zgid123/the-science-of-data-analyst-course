# 4. Phương pháp tiêu biểu: FSFM

Phần 2 và Phần 3 cùng dẫn đến một yêu cầu chung: một bộ phát hiện vẫn hoạt động tốt trên dữ liệu và kiểu tấn công chưa từng gặp, đồng thời bảo vệ khuôn mặt trước cả tấn công trình diện vật lý lẫn giả mạo số. FSFM, viết tắt của Face Security Foundation Model (mô hình nền tảng cho an ninh khuôn mặt), là một phương pháp được công bố mở, được xây dựng cho đúng yêu cầu đó và được trình bày tại CVPR 2025 [102].

Ý tưởng cốt lõi của phương pháp có thể nói gọn trong một câu. Thay vì học từ các ví dụ tấn công đã gán nhãn, FSFM trước hết học xem một khuôn mặt thật trông như thế nào từ hàng triệu khuôn mặt thật không gán nhãn, rồi mới chuyển hóa hiểu biết đó thành các bộ phát hiện deepfake, tấn công trình diện và khuôn mặt do AI tạo ra [102].

Mục 4.1 giải thích lý do chọn phương pháp này và bài toán mà nó giải quyết. Mục 4.2 trình bày cách phương pháp hoạt động theo từng bước, kèm hình minh họa. Mục 4.3 giải thích cách đánh giá phương pháp, tức là những phép kiểm thử và thước đo nào quyết định phương pháp có hiệu quả hay không. Mục 4.4 khép lại với các giới hạn của phương pháp và những câu hỏi còn mở trước khi có thể đưa nó vào vận hành thực tế.
