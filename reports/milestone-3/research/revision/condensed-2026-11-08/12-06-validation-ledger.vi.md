## Phụ lục VI – Sổ ghi kết quả kiểm tra

Bảng A.18 liệt kê 22 phép kiểm tra của `src/validate_prepared.py` cùng giá trị kỳ vọng và giá trị quan sát được, lấy từ `data/metadata/validation_summary.json`.

**Bảng A.18. Sổ ghi kết quả kiểm tra**

| Mã | Phép kiểm tra | Kỳ vọng | Quan sát được | Trạng thái |
| :---- | :---- | :---- | :---- | :---- |
| V01a | Số dòng và cơ cấu biến kết quả của enrolment bằng studentInfo gốc | 32.593; Distinction 3.024, Fail 7.052, Pass 12.361, Withdrawn 10.156 | đúng như kỳ vọng | PASS |
| V01b | Số sinh viên | 28.785 | đúng như kỳ vọng | PASS |
| V01c | Quy mô các tổng thể bằng số liệu trong kết quả khảo sát dữ liệu (C09) | d14: 28.061; d13: 28.069; d27: 27.535 | đúng như kỳ vọng | PASS |
| V01d | Số trường hợp không hoàn thành trong mỗi bảng đặc trưng bằng số liệu trong kết quả khảo sát dữ liệu | d13: 12.708; d27: 12.156 | đúng như kỳ vọng | PASS |
| V02 | Giá trị thiếu sau xử lý = trước xử lý (không điền giá trị thiếu trong các bảng) | imd_band Missing: 1.111; date_registration: 45; điểm TMA/CMA rỗng (đã nộp): 173 | đúng như kỳ vọng | PASS |
| V03 | Khóa là duy nhất trong mọi bảng | 0 dòng trùng | 0 ở cả 6 bảng | PASS |
| V04a | Lượt nhấp trong enrolment + lượt nhấp sau khi rút = lượt nhấp gốc | 39.605.099 | 39.506.354 + 98.745 = 39.605.099 | PASS |
| V04b | Lượt nhấp trong student_week = lượt nhấp trong enrolment | 39.506.354 | đúng như kỳ vọng | PASS |
| V04c | Tổng sau khi loại trùng ≤ tổng gốc | sau loại trùng ≤ gốc | 38.247.422 ≤ 39.506.354 | PASS |
| V05 | Mọi giá trị phân loại đều nằm trong tập giá trị kỳ vọng | không có nhãn nào khác | không có | PASS |
| V06 | Kết quả bảo lưu không mang số ngày trễ và không có trạng thái bỏ lỡ | 0 | đúng như kỳ vọng | PASS |
| V07 | Khoảng giá trị sau xử lý = trước xử lý (không cắt ngưỡng) | score 0–100; credits 30–655 | score: 0–100; studied_credits: 30–655 | PASS |
| V08 | Không có dòng student_week nào sau tuần rút | 0 | đúng như kỳ vọng | PASS |
| V09 | Mọi phép nối bảng được ghi nhật ký đều giữ nguyên số dòng | 25 phép nối, dòng vào = dòng ra | 25 | PASS |
| V10 | Lượt đăng ký học không có dòng lượt nhấp nào được giữ lại với 0 lượt nhấp | ≥ 3.365 | 3.554 | PASS |
| V11-d13 | 6 đặc trưng được tính lại từ dữ liệu gốc cho cả 28.069 dòng (mã độc lập) | 0 chỗ lệch | 0 ở cả 6 đặc trưng | PASS |
| V11-d27 | 6 đặc trưng được tính lại từ dữ liệu gốc cho cả 27.535 dòng (mã độc lập) | 0 chỗ lệch | 0 ở cả 6 đặc trưng | PASS |
| V12 | Tham số của phép biến đổi giống nhau khi có và khi không có dòng kiểm thử, đồng thời bằng các tham số đã lưu | giống hệt | d13: giống hệt; d27: giống hệt | PASS |
| V13-d13 | Lượt nhấp của pipeline khác với lần đếm lại không lọc đúng ở những sinh viên có lượt nhấp về sau; bảng không có cột nào suy ra từ biến mục tiêu hoặc tính trên cả kỳ mở | 26.755 dòng có lượt nhấp về sau; không có cột bị cấm | 26.755 dòng khác biệt; không có cột bị cấm | PASS |
| V13-d27 | Lượt nhấp của pipeline khác với lần đếm lại không lọc đúng ở những sinh viên có lượt nhấp về sau; bảng không có cột nào suy ra từ biến mục tiêu hoặc tính trên cả kỳ mở | 25.663 dòng có lượt nhấp về sau; không có cột bị cấm | 25.663 dòng khác biệt; không có cột bị cấm | PASS |
| V14 | Mọi cột đều được mô tả; danh sách biến dự báo không chứa cột kiểm tra công bằng, cột mục tiêu hay cột mô tả | không có | đúng như kỳ vọng | PASS |
| V15 | Không kỳ mở nào nằm ở cả hai phần dữ liệu; 2013 = huấn luyện; cờ sinh viên được tính lại | 9 kỳ mở huấn luyện, 13 kỳ mở kiểm thử; 0 cờ lệch | kỳ mở huấn luyện: 9; kỳ mở kiểm thử: 13; lượt đăng ký học kiểm thử của sinh viên đã xuất hiện năm 2013: 1.962; cờ lệch: 0 | PASS |

Bước kiểm tra cũng báo cáo các con số mà kế hoạch Milestone 4 dựa vào; các con số này không dùng bất kỳ kết quả nào của tập kiểm thử. Cụ thể, quy tắc dấu hiệu sớm gắn cờ 20,2% số sinh viên đang đăng ký học tại ngày 13 và 28,8% tại ngày 27 (41,2% nếu tính cả việc nộp trễ CMA); điểm CMA đã biết tại thời điểm chốt có ở 1,4% và 5,2% số dòng huấn luyện; tỷ lệ hoàn thành trong tổng thể ngày 14 là 54,7% (54,9% khi không tính 138 lượt đăng ký học được gắn cờ vì không rõ ngày rút (93) hoặc ngày đăng ký (45)). Tỷ lệ kích hoạt quy tắc theo kỳ mở và thời điểm chốt có trong `rule_rates.csv`.
