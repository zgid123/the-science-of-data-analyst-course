## Phụ lục IV – Chi tiết kiểm tra cấu trúc ban đầu

Bảng A.6 cho biết tên các cột đọc được ở từng bảng, kiểu dữ liệu suy ra từ giá trị dạng văn bản và số ô thiếu giá trị. Bảng A.7 liệt kê các số đếm dùng để kết luận về các điều kiện đi kèm quyết định chọn OULAD.

**Bảng A.6. Tên cột, kiểu dữ liệu suy ra và giá trị thiếu**

| Bảng | Tên cột và kiểu dữ liệu suy ra | Số ô thiếu |
| :---- | :---- | :---- |
| courses | code_module (văn bản), code_presentation (văn bản), module_presentation_length (số nguyên) | không có |
| assessments | code_module (văn bản), code_presentation (văn bản), id_assessment (số nguyên), assessment_type (văn bản), date (số nguyên), weight (số thập phân) | date 11 |
| vle | id_site (số nguyên), code_module (văn bản), code_presentation (văn bản), activity_type (văn bản), week_from (số nguyên), week_to (số nguyên) | week_from 5.243, week_to 5.243 |
| studentInfo | code_module (văn bản), code_presentation (văn bản), id_student (số nguyên), gender (văn bản), region (văn bản), highest_education (văn bản), imd_band (văn bản), age_band (văn bản), num_of_prev_attempts (số nguyên), studied_credits (số nguyên), disability (văn bản), final_result (văn bản) | imd_band 1.111 |
| studentRegistration | code_module (văn bản), code_presentation (văn bản), id_student (số nguyên), date_registration (số nguyên), date_unregistration (số nguyên) | date_registration 45, date_unregistration 22.521 |
| studentAssessment | id_assessment (số nguyên), id_student (số nguyên), date_submitted (số nguyên), is_banked (số nguyên), score (số nguyên) | score 173 |
| studentVle | code_module (văn bản), code_presentation (văn bản), id_student (số nguyên), id_site (số nguyên), date (số nguyên), sum_click (số nguyên) | không có |

Bảng A.7 nêu các số đếm dùng để kết luận về ba điều kiện G1, G3 và G5, để xác định ngày đến hạn của các bài đầu tiên và để tính mẫu số của KPI.

**Bảng A.7. Số đếm làm căn cứ cho các điều kiện đi kèm quyết định chọn OULAD và mẫu số của KPI**

| Nội dung kiểm tra | Kết quả |
| :---- | :---- |
| Các giá trị kết quả | Pass 12.361, Withdrawn 10.156, Fail 7.052, Distinction 3.024 |
| Kết quả Withdrawn có / không có ngày hủy đăng ký; các kết quả khác có ngày này | 10.063 / 93 ; 9 |
| Số sinh viên; số sinh viên học từ hai kỳ mở module trở lên | 28.785; 3.538 |
| Số trường hợp học lại cùng module; trong đó, số trường hợp ghi số lần học trước cao hơn | 1.309; 1.309 |
| Các kỳ mở của từng module | AAA: 2013J, 2014J; BBB: 2013B, 2013J, 2014B, 2014J; CCC: 2014B, 2014J; DDD: 2013B, 2013J, 2014B, 2014J; EEE: 2013J, 2014B, 2014J; FFF: 2013B, 2013J, 2014B, 2014J; GGG: 2013J, 2014B, 2014J |
| Số kỳ mở có bài không phải bài thi đến hạn tính đến hết ngày 13 / ngày 27 (trong 22 kỳ mở) | 1 / 16 |
| Ngày đến hạn của bài đầu tiên không phải bài thi, theo từng kỳ mở | AAA-2013J 19, AAA-2014J 19, BBB-2013B 19, BBB-2013J 19, BBB-2014B 12, BBB-2014J 19, CCC-2014B 18, CCC-2014J 18, DDD-2013B 23, DDD-2013J 25, DDD-2014B 25, DDD-2014J 20, EEE-2013J 33, EEE-2014B 33, EEE-2014J 33, FFF-2013B 19, FFF-2013J 19, FFF-2014B 24, FFF-2014J 24, GGG-2013J 61, GGG-2014B 61, GGG-2014J 61 |
| Số bài thi không có ngày đến hạn | 11 |
| Số lượt đăng ký học: hủy vào hoặc trước ngày 0; đăng ký sau ngày 14; thiếu ngày đăng ký | 3.097; 58; 45 |
| Số lượt đăng ký học còn hiệu lực tại ngày 14 | 28.119 |
| Số dòng không có dòng tương ứng ở bảng cha (bài được chấm điểm, bài nộp, lượt nhấp đối chiếu với lượt đăng ký học, lượt nhấp đối chiếu với tài nguyên học tập) | 0, 0, 0, 0 |
