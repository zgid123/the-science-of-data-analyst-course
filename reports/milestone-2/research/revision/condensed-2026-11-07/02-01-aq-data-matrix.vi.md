## 2.1. Ma trận AQ – yêu cầu dữ liệu

Cả bốn câu hỏi dùng chung một đơn vị phân tích là lượt đăng ký học phần: một sinh viên học một học phần trong một học kỳ. Tổng thể là sinh viên còn theo học sau thời gian điều chỉnh đăng ký học phần. Nhóm sinh viên này cũng là mẫu số của KPI chính. Biến kết quả ghi kết quả cuối cùng của học phần, gồm ba giá trị: đạt, trượt và rút học phần. Đạt ở bất kỳ mức điểm nào đều được tính là hoàn thành học phần; trượt hoặc rút học phần thì không.
Với từng câu hỏi, Bảng 2.1 nêu những gì cần đo, các biến không thể thiếu, độ chi tiết về thời gian và quyết định mà câu hỏi phục vụ.

**Bảng 2.1. Ma trận AQ – yêu cầu dữ liệu**

| AQ | Loại phân tích | Đơn vị phân tích | Kết quả / chỉ số đo | Biến bắt buộc | Thời gian / độ chi tiết | Thời điểm ra quyết định |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Mô tả | Sinh viên – học phần – học kỳ | Đạt, trượt hoặc rút học phần; tuần mà sinh viên lần đầu bỏ lỡ bài được chấm điểm, tính riêng cho sinh viên đạt và sinh viên không đạt | Mã định danh cố định của sinh viên, học phần và học kỳ; ngày bắt đầu học phần; ngày bắt đầu và ngày kết thúc đăng ký; kết quả cuối cùng; ngày rút học phần; ngày đến hạn và ngày nộp bài | Bốn học kỳ; theo tuần | D2, cuối học kỳ |
| AQ2 | Chẩn đoán | Sinh viên – học phần – học kỳ, kèm dấu hiệu theo tuần | Với từng dấu hiệu, chênh lệch giữa nhóm có dấu hiệu và nhóm không có dấu hiệu về tỷ lệ sinh viên về sau không hoàn thành học phần | Các biến của AQ1, thêm hoạt động trên nền tảng học tập có ghi ngày; bài bị bỏ lỡ và bài nộp trễ (chỉ tính bài đến hạn trước ngày sinh viên rút học phần); các học phần sinh viên học trong cùng học kỳ | Tuần 1–4; theo ngày hoặc theo tuần | D2; lý do cụ thể trong D1 |
| AQ3 | Dự báo | Sinh viên – học phần – học kỳ tại mỗi thời điểm dự báo | Không hoàn thành học phần tính đến cuối học kỳ | Hoạt động và bài nộp có dấu thời gian; ngày rút học phần; ngày bắt đầu đăng ký; đặc điểm cá nhân đã biết khi đăng ký | Thời điểm dự báo là hết tuần 2 và hết tuần 4; ít nhất ba học kỳ xếp theo thứ tự thời gian | D1, tuần 3 và tuần 5 |
| AQ4 | Chỉ định | Sinh viên tại mỗi đợt lập danh sách | Tỷ lệ phát hiện (recall) và độ chính xác của danh sách (precision) khi danh sách không vượt quá số sinh viên cán bộ liên hệ được mỗi tuần; kết quả học phần của sinh viên sau khi được liên hệ | Kết quả của AQ3, mỗi sinh viên chỉ có một dòng trong danh sách; số sinh viên cán bộ liên hệ được mỗi tuần (giả định); sổ theo dõi liên hệ | Theo đợt lập danh sách và theo tuần | D1, liên hệ ai |

Các biến tùy chọn gồm hình thức học; năm theo học; chuyên cần; thông tin phân biệt tạm ngừng học, chuyển chương trình đào tạo và thôi học; và phân công cố vấn học tập cho sinh viên. Các biến này giúp trả lời AQ1–AQ4 đầy đủ hơn, nhưng không quyết định một bộ dữ liệu có dùng được hay không. Khi thiếu các biến này, bộ dữ liệu không bị loại mà những phần câu hỏi cần đến các biến đó chỉ đạt mức đáp ứng Một phần (Phụ lục V). Từ các yêu cầu trên, nhóm phân tích dữ liệu rút ra sáu điều kiện bắt buộc cho mọi bộ dữ liệu ứng viên, mang mã từ G1 đến G5, riêng G2 gồm hai phần:

(1) G1 Kết quả: mỗi lượt đăng ký học phần có kết quả cuối cùng phân biệt đạt, trượt và rút học phần, kèm ngày rút.
(2) G2a Bài được chấm điểm có ngày: có ngày đến hạn và ngày nộp bài, tính từ ngày bắt đầu học phần.
(3) G2b Hoạt động có ngày: có hoạt động trên nền tảng học tập của từng sinh viên, theo ngày hoặc theo tuần.
(4) G3 Lịch sử: cùng một học phần có ít nhất ba kỳ mở học phần xếp theo thứ tự thời gian, trong đó có một kỳ mở muộn hơn dùng để đánh giá mô hình.
(5) G4 Quyền truy cập: có giấy phép mở cho mục đích học thuật, tài liệu mô tả chính thức và nguồn gốc dữ liệu kiểm chứng được.
(6) G5 Quyền riêng tư và liên kết: dữ liệu đã được ẩn danh, đồng thời có mã định danh sinh viên cố định để liên kết bản ghi giữa các bảng và giữa các kỳ mở học phần.
