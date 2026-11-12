# 4. Yêu cầu dữ liệu và lựa chọn bộ dữ liệu

Trước khi tìm dữ liệu, nhóm viết các yêu cầu theo đúng những loại hồ sơ mà trường đang lưu. Nhờ vậy, dữ liệu
được chọn theo câu hỏi chứ không phải câu hỏi bị sửa theo dữ liệu sẵn có. Mọi câu hỏi đều dùng chung đơn vị phân tích là lượt đăng ký học phần của một sinh viên trong một học phần và một học kỳ, chung nhóm sinh viên được xét (còn theo học sau thời gian điều chỉnh đăng ký học phần) và chung biến kết quả (kết quả cuối cùng kèm ngày rút học phần). Mỗi danh sách chỉ được dùng dữ liệu ghi nhận tính đến hết thời điểm chốt dữ liệu, tức
một tuần trước khi lập danh sách, nên mọi sự kiện đều cần mốc thời gian. Bảng 4.1 là Ma trận AQ – yêu cầu dữ liệu
(AQ–Data Requirement Matrix); Bảng A.9 (Phụ lục IV) bổ sung các hệ thống nguồn. Từ ma trận này, nhóm rút ra sáu
điều kiện bắt buộc mà bộ dữ liệu nào cũng phải đạt, ký hiệu G1–G5: kết quả học tập có mốc thời gian, gồm cả ngày rút học
phần (G1); bài được chấm điểm có mốc thời gian (G2a); hoạt động học tập có mốc thời gian (G2b); ít nhất ba kỳ mở học
phần nối tiếp nhau theo thời gian (G3); giấy phép mở kèm nguồn gốc dữ liệu rõ ràng (G4); và mã định danh ẩn danh không
đổi qua các kỳ mở (G5). Sổ theo dõi liên hệ được xác định là một khoảng trống dữ liệu ngay từ trước khi tìm kiếm.

**Bảng 4.1. Ma trận AQ – yêu cầu dữ liệu**

| AQ | Biến kết quả hoặc đại lượng đo | Các biến cần có | Thời gian và mức chi tiết | Thời điểm ra quyết định |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Đạt, không đạt hoặc rút học phần; tuần đầu tiên bỏ lỡ bài | Mã định danh; ngày đăng ký học phần; kết quả cuối cùng; ngày rút học phần; ngày của các bài được chấm điểm | Bốn học kỳ, chi tiết theo tuần | D2, cuối học kỳ |
| AQ2 | Chênh lệch tỷ lệ không hoàn thành giữa sinh viên có và không có từng dấu hiệu | Các biến của AQ1; hoạt động có mốc thời gian; bài bị bỏ lỡ và bài nộp trễ | Tuần 1–4, chi tiết theo ngày | D2; lý do cụ thể trong D1 |
| AQ3 | Không hoàn thành học phần tính đến cuối học kỳ | Hoạt động và bài nộp có mốc thời gian; đặc điểm cá nhân tại thời điểm đăng ký | Tuần 2 và tuần 4; các kỳ mở theo thứ tự thời gian | D1, tuần 3 và tuần 5 |
| AQ4 | Tỷ lệ phát hiện trong giới hạn danh sách; kết quả sau khi liên hệ | Kết quả của AQ3; hạn mức liên hệ (giả định); sổ theo dõi liên hệ (cần tạo mới) | Mỗi đợt lập danh sách | D1 |
