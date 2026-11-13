## Phụ lục VI – Sổ ghi kết quả kiểm tra

Bảng A.19 liệt kê 22 phép kiểm tra của `src/validate_prepared.py` cùng giá trị kỳ vọng và giá trị quan sát được, lấy từ `data/metadata/validation_summary.json`.

**Bảng A.19. Sổ ghi kết quả kiểm tra**

| Mã | Phép kiểm tra | Kỳ vọng | Quan sát được | Trạng thái |
| :---- | :---- | :---- | :---- | :---- |
| V01a | Số dòng và cơ cấu biến kết quả của enrolment bằng studentInfo gốc | 32.593; Distinction 3.024, Fail 7.052, Pass 12.361, Withdrawn 10.156 | đúng như kỳ vọng | PASS |
| V01b | Số sinh viên | 28.785 | đúng như kỳ vọng | PASS |
| V01c | Số lượt đăng ký học được xét bằng số liệu trong kết quả khảo sát dữ liệu (C09) | d14: 28.061; d13: 28.069; d27: 27.535 | đúng như kỳ vọng | PASS |
| V01d | Số trường hợp không hoàn thành trong mỗi bảng đặc trưng bằng số liệu trong kết quả khảo sát dữ liệu | d13: 12.708; d27: 12.156 | đúng như kỳ vọng | PASS |
| V02 | Giá trị thiếu sau xử lý = trước xử lý (không điền giá trị thiếu trong các bảng) | imd_band Missing: 1.111; date_registration: 45; điểm TMA/CMA rỗng (đã nộp): 173 | đúng như kỳ vọng | PASS |
| V03 | Khóa không trùng lặp trong mọi bảng | 0 dòng trùng | 0 ở cả 6 bảng | PASS |
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
| V12 | Tham số của phép biến đổi giống nhau khi có và khi không có dòng của tập kiểm thử, đồng thời bằng các tham số đã lưu | giống hệt | d13: giống hệt; d27: giống hệt | PASS |
| V13-d13 | Lượt nhấp của pipeline khác với lần đếm lại không lọc đúng ở những sinh viên có lượt nhấp về sau; bảng không có cột nào suy ra từ biến mục tiêu hoặc tính trên cả kỳ mở | 26.755 dòng có lượt nhấp về sau; không có cột bị cấm | 26.755 dòng khác biệt; không có cột bị cấm | PASS |
| V13-d27 | Lượt nhấp của pipeline khác với lần đếm lại không lọc đúng ở những sinh viên có lượt nhấp về sau; bảng không có cột nào suy ra từ biến mục tiêu hoặc tính trên cả kỳ mở | 25.663 dòng có lượt nhấp về sau; không có cột bị cấm | 25.663 dòng khác biệt; không có cột bị cấm | PASS |
| V14 | Mọi cột đều được mô tả; danh sách đặc trưng không chứa cột kiểm tra công bằng, cột mục tiêu hay cột mô tả | không có | đúng như kỳ vọng | PASS |
| V15 | Không kỳ mở nào nằm ở cả hai phần dữ liệu; 2013 = huấn luyện; cờ sinh viên được tính lại | 9 kỳ mở huấn luyện, 13 kỳ mở của tập kiểm thử; 0 cờ lệch | kỳ mở huấn luyện: 9; kỳ mở của tập kiểm thử: 13; lượt đăng ký học trong tập kiểm thử của sinh viên đã xuất hiện năm 2013: 1.962; cờ lệch: 0 | PASS |

Bước kiểm tra cũng báo cáo các con số mà kế hoạch Milestone 4 dựa vào; các con số này được tính mà không dùng bất kỳ kết quả nào của tập kiểm thử. Cụ thể, quy tắc dấu hiệu sớm đánh dấu 20,2% số sinh viên đang đăng ký học vào ngày 13 và 28,8% vào ngày 27 (41,2% nếu tính cả CMA nộp trễ); điểm CMA đã biết tại thời điểm chốt có ở 1,4% và 5,2% số dòng huấn luyện; tỷ lệ hoàn thành trong nhóm tính KPI là 54,7% và là 54,9% khi không tính 138 lượt đăng ký học được gắn cờ vì không rõ ngày rút (93 lượt) hoặc ngày đăng ký (45 lượt). Tỷ lệ sinh viên được quy tắc đánh dấu theo kỳ mở và thời điểm chốt có trong `rule_rates.csv`.

**Lý do cần xếp hạng.** Quy tắc dấu hiệu sớm đánh dấu 20,2% số sinh viên đang đăng ký học vào ngày 13 và 28,8% vào ngày
27, trong khi danh sách 3 hoặc 5 sinh viên trên mỗi nhóm 20 sinh viên chỉ chứa được 15% hoặc 25% số sinh viên của nhóm. Với
danh sách 5 sinh viên trên mỗi nhóm 20, quy tắc đánh dấu nhiều sinh viên hơn độ dài danh sách ở 7 trong 22 kỳ mở tại ngày 13 và ở 10 kỳ mở tại
ngày 27; với danh sách 3 sinh viên trên mỗi nhóm 20, con số này là 15 kỳ mở tại ngày 13 và cả 22 kỳ mở tại ngày 27. Vì vậy, cán bộ cần
một thứ tự ưu tiên để biết nên liên hệ ai trước. AQ3 và AQ4 cung cấp thứ tự đó, còn riêng quy tắc dấu hiệu sớm thì không xếp được thứ tự này.

**Giải thích các phép kiểm tra trước và sau chuẩn bị.** Các đoạn dưới đây giải thích hai kết quả trong Bảng 7.1 và các phép kiểm tra bổ sung ngoài bảng đó.

Hai kết quả cần được giải thích thêm. Thứ nhất, số lượt đăng ký học không có dòng lượt nhấp nào tăng từ 3.365 trong dữ liệu gốc lên 3.554 trong bảng dữ liệu đã chuẩn bị. Nguyên nhân là các lượt nhấp sau khi rút được loại khỏi dữ liệu, nên 189 sinh viên chỉ có hoạt động sau ngày hủy đăng ký nay không còn lượt nhấp nào. Thứ hai, phép kiểm tra rò rỉ thông tin được thiết kế sao cho có thể báo lỗi (FAIL): nếu một đặc trưng dùng bất kỳ lượt nhấp nào sau thời điểm chốt, đặc trưng đó sẽ bằng kết quả đếm lại không lọc ở mọi sinh viên; khi đó, phép kiểm tra sẽ không tìm thấy khác biệt nào ở những sinh viên có lượt nhấp về sau.

Ngoài việc tính lại mọi dòng đặc trưng, chín kiểm thử đơn vị trên các bản ghi giả lập xác nhận từng công thức. Bên cạnh đó, một dòng được đếm lại thủ công từ các tệp gốc và trùng khớp với bảng dữ liệu đã chuẩn bị: dòng này có một TMA đến hạn vào ngày 19 và được nộp vào ngày 24, cùng 168 lượt nhấp trong 10 ngày có hoạt động tính đến hết ngày 27.

Bảng A.20 trình bày tình trạng của sáu điều kiện mà đề bài đặt ra để bắt đầu Milestone 4.

**Bảng A.20. Điều kiện đầu vào của Milestone 4**

| Điều kiện | Tình trạng |
| :---- | :---- |
| Các AQ cốt lõi có bảng dữ liệu đã chuẩn bị, truy vết được rõ ràng | Các bảng cho AQ1–AQ3 đã sẵn sàng; bảng xếp hạng cho AQ4 đã sẵn sàng, việc chọn hình thức liên hệ được hoãn (Phụ lục IV) |
| Biến mục tiêu, đặc trưng và các chiều phân tích đã ổn định | Được định nghĩa trong bản đặc tả đặc trưng và từ điển dữ liệu; 9/9 kiểm thử đơn vị cho công thức đều PASS |
| Rò rỉ thông tin và cách chia dữ liệu đã được xác định cho các bài toán dự báo | Có bản đặc tả cách chia dữ liệu và kiểm soát rò rỉ thông tin; V11–V13 và V15 đạt |
| Các vấn đề chất lượng quan trọng đã được xử lý hoặc được giữ lại có chủ đích | DQ01–DQ19 đều có quyết định; các rủi ro còn lại đã được nêu (Mục 7.3) |
| Không dùng dữ liệu giả lập làm bằng chứng | Chỉ có các bản ghi giả lập có gắn nhãn thuộc mức A (dữ liệu kiểm thử nhỏ cho mã) |
| Dữ liệu đã chuẩn bị tạo lại được từ dữ liệu gốc | Hai lần chạy từ các tệp gốc; 8/8 tệp dữ liệu giống hệt nhau |

**Chi tiết về các rủi ro còn lại.** Các đoạn dưới đây giải thích năm rủi ro còn lại mà Mục 7.3 liệt kê.

(1) **Dòng lượt nhấp trùng lặp.** Các dòng trùng lặp hoàn toàn có thể là bản sao do hệ thống ghi nhật ký tạo ra hoặc là những lượt truy cập lặp lại. Phiên bản đã bỏ dòng trùng của các đặc trưng lượt nhấp cho biết ảnh hưởng tối đa của các dòng này: bỏ dòng trùng sẽ làm mất 3,19% tổng số lượt nhấp.

(2) **CMA nộp trễ và điểm CMA.** Ý nghĩa của một CMA nộp trễ trong giai đoạn 2013–2014 không được mô tả trong tài liệu, còn chính sách chấm điểm của OU tìm được là bản năm 2025 [3]. Vì vậy, quy tắc dấu hiệu sớm chỉ xét TMA nộp trễ, còn một phương án xét thêm CMA nộp trễ được giữ lại để so sánh; khi tính cả CMA nộp trễ, quy tắc sẽ đánh dấu 41,2% số lượt đăng ký học tại ngày 27 thay vì 28,8%. Bên cạnh đó, điểm CMA đã biết tại thời điểm chốt dữ liệu chỉ có ở 1,4% số dòng huấn luyện tại ngày 13 và 5,2% tại ngày 27, thấp hơn mức bao phủ 10% mà nhóm yêu cầu trước khi đưa điểm CMA vào nhóm đặc trưng của Milestone 4. Do đó, điểm CMA được chuẩn bị nhưng không được sử dụng.

(3) **Bản ghi chưa chắc chắn.** Trong dữ liệu, 93 lượt đăng ký học có kết quả Withdrawn nhưng không có ngày rút; ngoài ra, 1.962 lượt đăng ký học trong tập kiểm thử thuộc về những sinh viên đã xuất hiện năm 2013. Cả hai nhóm đều được gắn cờ để kết quả trên tập kiểm thử có thể được báo cáo khi có và khi không có các nhóm này.

(4) **KPI chỉ là chỉ số đại diện.** Tỷ lệ hoàn thành một kỳ mở module của OULAD được dùng thay cho tỷ lệ hoàn thành học phần của trường; bên cạnh đó, OULAD không phân biệt được tạm ngừng học hoặc chuyển chương trình đào tạo với rút khỏi module. Ảnh hưởng của các bản ghi chưa chắc chắn lên KPI là nhỏ: khi bỏ 138 lượt đăng ký học được gắn cờ do không rõ ngày rút (93) hoặc ngày đăng ký (45), tỷ lệ hoàn thành tại ngày 14 là 54,9% thay vì 54,7%.

(5) **Giả định về năng lực liên hệ mỗi tuần.** OU chia mỗi module thành các nhóm hướng dẫn, mỗi nhóm vài chục sinh viên [9]. Các kịch bản giả định rằng mỗi giảng viên kiêm cố vấn học tập phụ trách một nhóm như vậy, gồm 20 sinh viên. Milestone 1 đặt năng lực liên hệ mỗi tuần của một giảng viên kiêm cố vấn học tập là từ ba đến năm sinh viên; vì vậy, trong tuần sau mỗi đợt lập danh sách, danh sách của mỗi nhóm gồm ba hoặc năm sinh viên. Với Phòng Đào tạo, các kịch bản dùng danh sách 30 hoặc 40 sinh viên cho mỗi kỳ mở tại mỗi đợt lập danh sách, theo khoảng năng lực liên hệ mỗi tuần mà Milestone 1 đặt ra cho phòng này. Số sinh viên phụ trách thực tế ở trường có thể khác, nên độ dài danh sách chỉ là kịch bản, chưa phải kế hoạch.
