## 3.3. Đánh giá chuẩn của cơ quan nhà nước: NIST FATE PAD

Các thư xác nhận của phòng thí nghiệm như ở Mục 3.2 kiểm thử từng sản phẩm một theo yêu cầu của nhà cung cấp. Một đánh giá chuẩn (benchmark) của cơ quan nhà nước bổ sung một loại bằng chứng khác: một lần kiểm thử nhiều thuật toán trên cùng một bộ dữ liệu được lưu giữ biệt lập, do một cơ quan không có sản phẩm nào để bán thực hiện. Báo cáo NIST IR 8491, FATE Phần 10, của Mei Ngan, Patrick Grother và Austin Hom thuộc Phòng thí nghiệm Công nghệ Thông tin của NIST, cung cấp bằng chứng này cho PAD [31]. Báo cáo được phê duyệt ngày 19/9/2023, dài 152 trang [31] và được công bố ngày 20/9/2023 [90].

Đánh giá chuẩn này phát triển từ chương trình nghiên cứu khuôn mặt lâu năm của NIST. Từ năm 1999 đến tháng 7/2023, các phép kiểm thử nhận dạng và phân tích khuôn mặt của NIST "được gọi chung là FRVT" [31], tức Face Recognition Vendor Test, chương trình vốn đã bao quát PAD dưới tên FRVT PAD trong kế hoạch đánh giá năm 2022 [9]. Ngày 18/8/2023, NIST tách chương trình thành Face Recognition Technology Evaluation (FRTE) và FATE [90], và IR 8491 nằm trong hai ấn phẩm đầu tiên sau lần tách này, nhằm cung cấp thông tin cho nhà phát triển, người dùng cuối, các quy trình tiêu chuẩn hóa và nhà hoạch định chính sách [91].

Thiết kế kiểm thử tuân theo phương pháp luận của Mục 3.1. NIST đánh giá 82 thuật toán nguyên mẫu từ 45 nhà phát triển; cả 82 thuật toán đều thực hiện phát hiện mạo danh (impersonation), và 27 thuật toán còn thực hiện phát hiện lẩn tránh (evasion) [31]. Việc tham gia mở rộng trên toàn thế giới và miễn phí từ ngày 3/1 đến 28/2/2023, mỗi nhà phát triển nộp tối đa hai thuật toán, mỗi thuật toán ở dạng thư viện đã biên dịch theo giao diện C++ do NIST công bố và được chạy như một hộp đen [31], [90]. Hai trường hợp sử dụng khác nhau ở mục tiêu của kẻ tấn công: mạo danh là cố trông giống một người cụ thể khác, còn lẩn tránh là cố không bị nhận ra là chính mình [91]. Phù hợp với Mục 1.2.1 và 1.2.2, phép kiểm thử bao quát PAD thụ động, dựa trên phần mềm, trên hình ảnh thu sẵn và chỉ với các tấn công vật lý [31]. Mỗi thuật toán trả về một quyết định nhị phân và một điểm tin cậy, NIST tính APCER và BPCER theo từng loại tấn công như định nghĩa trong ISO/IEC 30107-3, và mọi lần không xử lý được đều được tính là một tấn công đã bị phát hiện [31]. Bảng 3.4 tóm tắt thiết kế này.

**Bảng 3.4. Thiết kế kiểm thử của NIST FATE Phần 10 (IR 8491)**

| Thành phần | Giá trị |
| :---- | :---- |
| Thuật toán | 82 thuật toán nguyên mẫu từ 45 nhà phát triển; 27 thuật toán được kiểm thử thêm về lẩn tránh [31] |
| Dữ liệu | Khoảng 20.000 lượt tấn công thuộc 9 loại tấn công và khoảng 21.000 lượt trình diện hợp lệ, cùng 747 video; lưu giữ biệt lập tại NIST [31] |
| Các loại tấn công được nêu tên | Ảnh in hoặc phát lại, ảnh in hoặc phát lại được phóng to, khẩu trang bảo hộ, mặt nạ silicon mềm; năm loại còn lại chỉ được báo cáo theo số thứ tự [31] |
| Hình ảnh | Camera màu cố định; ảnh tĩnh từ 640 × 480 đến 5.184 × 3.456 điểm ảnh; video nén [31] |
| Chỉ số | APCER và BPCER theo từng loại tấn công (ISO/IEC 30107-3); APCER tại BPCER = 0,01 (thuận tiện) và BPCER tại APCER = 0,01 (an ninh) [31] |
| Phạm vi | Thụ động, dựa trên phần mềm, tấn công vật lý; ngoại tuyến [31] |

Mục 3.3.1 trình bày những gì đánh giá chuẩn này phát hiện được.
