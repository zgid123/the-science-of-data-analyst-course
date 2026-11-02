## 4.3. Cách đánh giá phương pháp

Một bộ phát hiện có thể sai theo hai cách: để lọt một tấn công, hoặc từ chối một người dùng hợp lệ. Mọi thước đo dùng cho FSFM đều kết hợp hai loại lỗi này, và mọi phép kiểm thử đều được thiết kế để bộ phát hiện gặp dữ liệu nó chưa từng thấy, vì đó là tình huống mà một hệ thống đã triển khai phải đối mặt.

Ba thước đo xuất hiện trong các đánh giá, đều đã được giới thiệu ở Phần 1:

(1) **AUC** tóm tắt mức độ bộ phát hiện xếp tấn công cao hơn khuôn mặt thật trên mọi ngưỡng quyết định có thể; 1,0 nghĩa là tách biệt hoàn hảo và 0,5 nghĩa là đoán mò, nên càng cao càng tốt [42]. Với deepfake, chỉ số này được báo cáo theo video và theo khung hình [102].
(2) **HTER** là trung bình của FAR và FRR, tức tỷ lệ tấn công bị chấp nhận và tỷ lệ người dùng hợp lệ bị từ chối tại một ngưỡng, nên càng thấp càng tốt [35].
(3) **ACER** là trung bình của APCER và BPCER, tức tỷ lệ tấn công bị chấp nhận và tỷ lệ trình diện hợp lệ bị từ chối, nên cũng càng thấp càng tốt [10].

Chính các phép kiểm thử quyết định ý nghĩa của những con số này. Bảng 4.1 liệt kê bốn giao thức dùng cho FSFM, và Hình 4.5 đối chiếu hai cách kiểm thử FAS.

**Bảng 4.1. Các giao thức đánh giá FSFM**

| Nhiệm vụ | Huấn luyện trên | Kiểm thử trên | Thước đo | Điều được làm rõ |
| :---- | :---- | :---- | :---- | :---- |
| DfD | FF++ ở mức nén c23 [102] | CelebDF-v2, DFDC, DFDC preview, WildDeepfake [102] | AUC theo video và theo khung hình [102] | Khả năng chuyển giao sang các bộ sưu tập deepfake chưa từng gặp khi huấn luyện |
| FAS, để-lại-một (leave-one-out) | Ba trong số OULU-NPU, CASIA-FASD, Idiap Replay-Attack, MSU-MFSD, cùng CelebA-Spoof [102] | Tập dữ liệu thứ tư; trung bình của bốn vòng qua 5 lần chạy [102] | HTER và AUC [102] | Khả năng chuyển giao sang điều kiện thu nhận mới, với dữ liệu huấn luyện đa dạng |
| Khuôn mặt do AI tạo ra | Phần DeepFake của FF++ [102] | Đánh giá chuẩn DiFF: khuôn mặt từ 13 mô hình khuếch tán [102] | AUC [102] | Khả năng chuyển giao sang một kỹ thuật tạo ảnh chưa từng gặp khi huấn luyện |
| FAS, kiểm thử độc lập | Một trong bốn tập dữ liệu [105] | Từng tập dữ liệu còn lại: 12 cặp; đồng thời trong từng tập dữ liệu [105] | ACER [105] | Khả năng chuyển giao từ một nguồn duy nhất, do một nhóm khác ngoài nhóm tác giả đo lường |

![Hình 4.5. Hai cách kiểm thử FAS trên dữ liệu chưa từng gặp: để-lại-một và kiểm thử chéo tập dữ liệu một nguồn](assets/figures/task2-4-5-evaluation-protocols.png){width=100%}

Từ đó rút ra ba nguyên tắc khi đọc bất kỳ kết quả nào được báo cáo. Thứ nhất, một kết quả chỉ có ý nghĩa khi đi cùng giao thức của nó: huấn luyện trên ba tập dữ liệu cộng CelebA-Spoof là điều kiện dễ hơn huấn luyện trên một tập, như Hình 4.5 cho thấy. Thứ hai, hai phương pháp chỉ so sánh được với nhau trong cùng điều kiện dữ liệu; chẳng hạn, FSFM và phương pháp thị giác – ngôn ngữ FLIP đều bổ sung CelebA-Spoof vào giao thức để-lại-một và đều lấy trung bình năm lần chạy, nên kết quả của hai phương pháp có thể đặt cạnh nhau [66], [102]. Thứ ba, một phép kiểm thử độc lập có trọng lượng hơn kết quả tự báo cáo, vì nó loại bỏ các lựa chọn về dữ liệu và thiết lập của nhóm tác giả khỏi kết quả [105].

Mục 4.4 áp dụng các nguyên tắc này vào chính kết quả của FSFM.
