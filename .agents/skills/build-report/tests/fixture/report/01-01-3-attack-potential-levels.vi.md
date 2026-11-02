### 1.1.3. Tiềm năng tấn công

Các tỷ lệ lỗi ở Mục 1.1.2 cho biết tấn công thành công thường xuyên đến mức nào. Một đánh giá đầy đủ còn cho biết các cuộc tấn công đó đòi hỏi bao nhiêu công sức, và công sức này được biểu thị bằng tiềm năng tấn công (attack potential). Khái niệm này bắt nguồn từ việc đánh giá an ninh sản phẩm công nghệ thông tin. Bộ tiêu chuẩn ISO/IEC 19989 bổ sung cho tiêu chuẩn Common Criteria ISO/IEC 15408 và phương pháp đánh giá đi kèm ISO/IEC 18045 các yêu cầu chức năng an ninh mở rộng cùng các hoạt động bảo đảm tương ứng [17]. Phần 3 của bộ này, ISO/IEC 19989-3, đề cập đến PAD; phiên bản của Viện Tiêu chuẩn Anh (British Standards Institution) được công bố ngày 30/9/2020 và đang ở trạng thái hiện hành, được rà soát định kỳ [17]. Theo cách tiếp cận này, kẻ tấn công "tìm cách vô hiệu hóa chính sách an ninh của hệ thống bằng cách trình diện đặc điểm sinh trắc học tự nhiên của họ hoặc vật giả mang đặc điểm được sao chép hay làm giả" [17], qua đó đặt việc đánh giá PAD vào một phương pháp đánh giá an ninh đã được xác lập.

Common Criteria là một tập hợp các tiêu chuẩn kỹ thuật được quốc tế công nhận [18], và chúng đánh giá tiềm năng tấn công của từng cuộc tấn công bằng cách chấm điểm theo năm yếu tố: chuyên môn, hiểu biết về đối tượng được đánh giá, cơ hội tiếp cận, thiết bị và thời gian thực hiện [18]. Tổng điểm được quy về một thang xếp hạng có thứ tự, tăng dần từ Basic qua Moderate và High đến Beyond High [18]. Trên cơ sở cơ chế này, mức xếp hạng càng cao cho thấy hệ thống đã chống chịu được các cuộc tấn công đòi hỏi nhiều kỹ năng hơn, nhiều hiểu biết hơn, nhiều thời gian hơn và thiết bị tốt hơn.

Các phòng thử nghiệm cụ thể hóa khái niệm này thành các cấp độ kiểm thử, trong đó cấp độ càng cao càng dùng các công cụ tấn công "phản ánh công sức, kỹ năng và nguồn lực ngày càng lớn của kẻ tấn công" [19]. Các cấp độ của iBeta Quality Assurance, một phòng thử nghiệm được công nhận có các thư xác nhận được phân tích trong Phần 3 của báo cáo, cho thấy cách từng yếu tố trở thành một tham số kiểm thử. Bảng 1.3 liệt kê các cấp độ này theo dữ liệu truy xuất ngày 2/10/2026.

**Bảng 1.3. Các cấp độ kiểm thử PAD của iBeta (tính đến ngày 2/10/2026)**

| Tham số | Cấp độ 1 | Cấp độ 2 | Cấp độ 3 |
| :---- | :---- | :---- | :---- |
| Thời gian cho phép | 8 giờ cho mỗi đối tượng hoặc loại | 2–4 ngày cho mỗi đối tượng hoặc loại | 7 ngày cho mỗi loại, 4 ngày cho mỗi đối tượng |
| Chuyên môn của người tấn công | Không quy định | Trung bình: đã tham gia ít nhất một lần kiểm thử PAD khác với phương thức mục tiêu | Cao: ít nhất 16 giờ nghiên cứu về tấn công trình diện và ít nhất 10 lần kiểm thử PAD khác với phương thức này |
| Thiết bị | Sẵn có trong gia đình hoặc văn phòng thông thường | Đắt tiền hơn, như máy in 3D, mặt nạ nhựa resin hoặc mặt nạ latex | – |
| Chi phí tối đa mỗi vật giả | 30 USD | 300 USD | – |
| Số lần tấn công | 150 lần tấn công xen kẽ 50 lần trình diện hợp lệ | – | – |
| Tỷ lệ tấn công thành công cho phép | 0% | 1% | 5% |
| Giới hạn lỗi trên trình diện hợp lệ | 15% | 15% | 10% |

Nguồn: [20].

iBeta còn giới hạn các lỗi trên trình diện hợp lệ để một hệ thống đạt yêu cầu, gồm BPCER và tỷ lệ không khớp sai (FNMR), ở mức 15% cho Cấp độ 1 và 2 và 10% cho Cấp độ 3, đồng thời rà soát các giới hạn này sáu tháng một lần [20]. Nhờ đó, một hệ thống không thể đạt một cấp độ bằng cách từ chối người dùng thật. Cấu trúc cấp độ này hiện đang mở rộng ra ngoài tấn công trình diện: tiêu chuẩn ISO/IEC 25456 sắp ban hành về phát hiện tấn công chèn dữ liệu được kỳ vọng cũng sẽ đánh trọng số độ phức tạp của tấn công theo các cấp độ (tính đến tháng 7 năm 2026) [21].
