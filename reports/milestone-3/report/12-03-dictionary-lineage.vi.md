## Phụ lục III – Từ điển dữ liệu đã chuẩn bị và bảng truy vết nguồn gốc dữ liệu

Bảng A.11 gắn mỗi mức phân tích với bảng dữ liệu đã chuẩn bị, các lượt đăng ký học được xét và đơn vị của mỗi dòng (grain), kèm phép kiểm tra mà đề bài đặt ra trước Milestone 4 và kết quả của phép kiểm tra đó.

**Bảng A.11. Các bảng dữ liệu đã chuẩn bị theo mức phân tích**

| Mức phân tích | Bảng dữ liệu đã chuẩn bị | Lượt đăng ký học được xét | Đơn vị mỗi dòng | Kiểm tra trước Milestone 4 | Kết quả |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Mô tả | enrolment, assessment_due, student_week | 32.593 lượt đăng ký học; KPI tính trên 28.061 lượt | lượt đăng ký học; lượt đăng ký học × bài; lượt đăng ký học × tuần | Không đếm trùng, không thiên lệch do phép nối bảng | Khóa không trùng lặp; các phép nối giữ nguyên số dòng; tổng lượt nhấp khớp với dữ liệu gốc |
| Chẩn đoán | features_d27 + enrolment | 27.535 lượt đăng ký học còn hiệu lực tại ngày 27 | lượt đăng ký học | Mối liên hệ từ dữ liệu thực, có nhóm so sánh | Dấu hiệu đến ngày 27; bảy module để so sánh trong cùng module |
| Dự báo | features_d13, features_d27, model_ready | 28.069 và 27.535 | lượt đăng ký học | Biến mục tiêu, thời điểm dự báo, đặc trưng có trước thời điểm dự báo, cách chia dữ liệu, đủ mẫu cho mỗi lớp | Lớp thiểu số có ≥ 92 mẫu mỗi kỳ mở; 9 kỳ mở huấn luyện và 13 kỳ mở của tập kiểm thử; phép biến đổi chỉ được ước lượng trên tập huấn luyện |
| Chỉ định | capacity_by_run | 44 dòng kỳ mở × thời điểm chốt | kỳ mở × thời điểm chốt | Dữ liệu về hành động, ràng buộc, chi phí và kết quả | Chỉ có số sinh viên cán bộ liên hệ được theo giả định; không có dữ liệu liên hệ hay kết quả sau liên hệ |

Từ điển dữ liệu (`data/metadata/data_dictionary.md`) liệt kê mọi cột của mọi bảng cùng kiểu dữ liệu, vai trò, nguồn, phép biến đổi và mức độ nhạy cảm. Bảng A.12 là bảng truy vết nguồn gốc dữ liệu (lineage) theo mục 13.1 của đề bài, mỗi dòng ứng với một biến đã chuẩn bị, trừ các khóa; sáu biến nhạy cảm được đánh dấu ở cột mục đích.

**Bảng A.12. Bảng truy vết nguồn gốc dữ liệu**

| Biến đã chuẩn bị | Tệp / trường nguồn | Phép biến đổi | Khoảng thời gian / điều kiện lọc | Mục đích / AQ |
| :---- | :---- | :---- | :---- | :---- |
| year | code_presentation | bốn ký tự đầu | – | chia dữ liệu theo thời gian |
| split | code_presentation | `train` nếu năm 2013, `test` nếu năm 2014 | mức kỳ mở | chia dữ liệu theo thời gian cho AQ3 (C07) |
| paired_run | courses | module và tháng bắt đầu có kỳ mở ở cả hai năm | mức kỳ mở | các tập con đánh giá của AQ3 |
| student_in_training_runs | studentInfo.id_student | lượt đăng ký học thuộc tập kiểm thử của sinh viên có lượt đăng ký học năm 2013 | – | AQ3: kiểm tra chặt trên sinh viên chưa từng xuất hiện trong dữ liệu huấn luyện |
| eval_withdrawal_day_unknown | final_result, date_unregistration | Withdrawn nhưng không có ngày rút | – | AQ3: báo cáo chỉ số trên tập kiểm thử khi có và khi không có các dòng này (phát hiện F1) |
| final_result | studentInfo.final_result | giữ nguyên như ghi nhận | quan sát khi kỳ mở kết thúc | biến kết quả của AQ1 |
| non_completion | studentInfo.final_result | Fail hoặc Withdrawn | quan sát khi kỳ mở kết thúc | biến mục tiêu của AQ1–AQ3 |
| completed | studentInfo.final_result | Pass hoặc Distinction | quan sát khi kỳ mở kết thúc | KPI chính |
| withdrawal_day_missing | final_result, date_unregistration | Withdrawn nhưng không có ngày | – | cờ của DQ04 |
| unregistered_not_withdrawn | final_result, date_unregistration | không phải Withdrawn nhưng có ghi ngày | – | cờ của DQ04 |
| unregistered_after_run_end | date_unregistration, courses | ngày sau độ dài kỳ mở | – | cờ của DQ06 |
| date_registration | studentRegistration.date_registration | giữ nguyên như ghi nhận | số ngày lệch | xác định lượt đăng ký học được xét |
| date_unregistration | studentRegistration.date_unregistration | giữ nguyên như ghi nhận | số ngày lệch; sau các thời điểm chốt đối với dòng đặc trưng | xác định lượt đăng ký học được xét, thời điểm rút (AQ1) |
| enrolled_d13 | các ngày đăng ký | enrolled_at(13) | ngày 13 | lượt đăng ký học được xét ở AQ3 (C09) |
| enrolled_d14 | các ngày đăng ký | enrolled_at(14) | ngày 14 | mẫu số của KPI chính (C09) |
| enrolled_d27 | các ngày đăng ký | enrolled_at(27) | ngày 27 | lượt đăng ký học được xét ở AQ3 (C09) |
| start_month | code_presentation | ký tự cuối: B = tháng 2, J = tháng 10 | – | chiều phân tích của AQ1; đặc trưng của AQ3 |
| run_length | courses.module_presentation_length | đổi tên | – | ngày kết thúc kỳ mở |
| gender | studentInfo.gender | giữ nguyên như ghi nhận | – | kiểm tra công bằng của AQ3–AQ4 (nhạy cảm) |
| region | studentInfo.region | giữ nguyên như ghi nhận | – | kiểm tra công bằng; giải thích nhóm Missing của imd_band (nhạy cảm) |
| age_band | studentInfo.age_band | giữ nguyên như ghi nhận (thứ tự 0-35, 35-55, 55<=) | – | kiểm tra công bằng (nhạy cảm) |
| disability | studentInfo.disability | giữ nguyên như ghi nhận (Y/N) | – | giới hạn về công bằng của AQ4 (C04) (nhạy cảm) |
| imd_band | studentInfo.imd_band | '10-20' → '10-20%'; giá trị thiếu → 'Missing' | – | giới hạn về công bằng của AQ4 (C04) (nhạy cảm) |
| highest_education | studentInfo.highest_education | có thứ tự; mã thứ bậc trong model_ready | biết khi đăng ký học | AQ2–AQ3 (nhạy cảm) |
| num_of_prev_attempts | studentInfo.num_of_prev_attempts | giữ nguyên như ghi nhận | biết khi đăng ký học | AQ3 |
| studied_credits | studentInfo.studied_credits | giữ nguyên như ghi nhận; giữ giá trị ngoại lai | biết khi đăng ký học | AQ3 (số tín chỉ đang học) |
| registration_lead | studentRegistration.date_registration | −date_registration | biết khi đăng ký | AQ2–AQ3 |
| registration_missing | studentRegistration.date_registration | thiếu ngày đăng ký | biết khi đăng ký | nhóm mở rộng của AQ3 (39 trên 45 là Withdrawn) |
| banked_results | studentAssessment.is_banked | số kết quả bảo lưu | biết khi đăng ký | AQ3 |
| concurrent_runs | studentInfo | số lượt đăng ký học khác của sinh viên trong cùng kỳ mở | – | AQ2 (chỉ năm 2014, C12) |
| first_missed_week | assessment_due | tuần của TMA/CMA sớm nhất chưa nộp và đến hạn trong thời gian đăng ký học | cả kỳ mở | AQ1 |
| tasks_due_while_enrolled | assessment_due | số bài, không tính bài bảo lưu | cả kỳ mở | AQ1–AQ2 |
| tasks_missed_while_enrolled | assessment_due | số bài chưa nộp | cả kỳ mở | AQ1–AQ2 |
| tasks_late_while_enrolled | assessment_due | số bài nộp sau ngày đến hạn | cả kỳ mở | AQ2 |
| total_clicks | studentVle.sum_click | tổng trên mọi dòng | cả kỳ mở, đến ngày hủy đăng ký | AQ1–AQ2 |
| total_clicks_dedup | studentVle.sum_click | tổng, mỗi dòng trùng lặp hoàn toàn tính một lần | như total_clicks | phân tích độ nhạy của DQ01 |
| active_days | studentVle.date | số ngày khác nhau có lượt nhấp | cả kỳ mở (student_week: trong tuần), đến ngày hủy đăng ký | AQ1–AQ2 |
| assessment_type | assessments.assessment_type | TMA hoặc CMA (loại bài thi) | – | AQ1–AQ2 |
| due_day | assessments.date | đổi tên | số ngày lệch | AQ1–AQ2 |
| due_week | assessments.date | floor(due / 7) + 1 | – | AQ1 |
| weight | assessments.weight | giữ nguyên như ghi nhận; không dùng để tính điểm tổng kết | – | DQ09 |
| date_submitted | studentAssessment.date_submitted | giữ nguyên như ghi nhận; rỗng nếu chưa nộp | cả kỳ mở | AQ1–AQ2 |
| is_banked | studentAssessment.is_banked | giữ nguyên như ghi nhận | – | DQ07 |
| score | studentAssessment.score | giữ nguyên như ghi nhận; không phải đặc trưng, trừ khi qua cma_score_mean_c | cả kỳ mở | AQ2 |
| status | date_submitted, ngày đến hạn, is_banked | banked / not_submitted / on_time / late | cả kỳ mở | AQ1–AQ2 |
| lateness_days | date_submitted, ngày đến hạn | ngày nộp − ngày đến hạn (không bảo lưu) | cả kỳ mở | AQ2 |
| due_while_enrolled | ngày đến hạn, các ngày đăng ký | đã đăng ký tính đến hết ngày đến hạn và hủy đăng ký sau ngày đó | cả kỳ mở | AQ1 (chỉ tính bỏ lỡ khi đến hạn trong thời gian đăng ký học) |
| clicks | studentVle.sum_click | tổng theo tuần | tuần, đến ngày hủy đăng ký | AQ1–AQ2 |
| clicks_dedup | studentVle.sum_click | tổng theo tuần, mỗi dòng trùng lặp hoàn toàn tính một lần | tuần | phân tích độ nhạy của DQ01 |
| records | studentVle | số dòng nhật ký | tuần | DQ02 |
| sites | studentVle.id_site | số tài nguyên khác nhau | tuần | AQ2 |
| logging_gap | studentVle.date | tuần có một ngày không có lượt nhấp nào trong cả kỳ mở | tuần | DQ15 |
| clicks_pre | studentVle.sum_click, date | tổng | các ngày trước ngày 0 | AQ2–AQ3 |
| clicks_pre14 | studentVle.sum_click, date | tổng | ngày −14 đến −1 | AQ3 |
| clicks_0c | studentVle.sum_click, date | tổng (= tổng các cột clicks_w*) | ngày 0 đến c | AQ2–AQ3 |
| clicks_0c_dedup | studentVle | tổng, mỗi dòng trùng lặp hoàn toàn tính một lần | ngày 0 đến c | phân tích độ nhạy của DQ01 |
| active_days_0c | studentVle.date | số ngày khác nhau có lượt nhấp | ngày 0 đến c | AQ2–AQ3 |
| sites_0c | studentVle.id_site | số tài nguyên khác nhau | ngày 0 đến c | AQ3 |
| inactive_last7 | studentVle | không có lượt nhấp từ ngày c−6 đến ngày c | bảy ngày gần nhất | AQ2–AQ3; thành phần của quy tắc |
| activity_ratio_run | studentVle | (clicks_0c + 1) ÷ (trung vị clicks_0c của kỳ mở + 1) | cùng kỳ mở, ngày 0 đến c, còn hiệu lực tại c | dấu hiệu AQ2 so với mức trung bình của kỳ mở |
| tasks_due_c | assessments.date | TMA/CMA đến hạn tính đến hết ngày c và vào hoặc sau ngày đăng ký | ngày đến hạn ≤ c | AQ2–AQ3 |
| tasks_missed_c | studentAssessment | đến hạn ≤ c, không có bài nộp không bảo lưu đến c | bài nộp ≤ c | AQ2–AQ3; thành phần của quy tắc |
| tasks_late_c | studentAssessment | đến hạn ≤ c, nộp sau ngày đến hạn nhưng tính đến hết ngày c | bài nộp ≤ c | AQ2–AQ3 |
| tma_late_c | studentAssessment | TMA nộp trễ tính đến c | bài nộp ≤ c | AQ2–AQ3; thành phần của quy tắc |
| cma_late_c | studentAssessment | CMA nộp trễ tính đến c | bài nộp ≤ c | AQ2–AQ3; biến thể của quy tắc |
| cma_marked_c | studentAssessment | số điểm CMA đã biết tại c | nộp ≤ c − 7 | AQ3 (tỷ lệ dòng có điểm CMA) |
| cma_score_mean_c | studentAssessment.score | trung bình các điểm CMA đã biết; rỗng nếu không có | nộp ≤ c − 7 | AQ3 |
| days_since_last_click | studentVle.date | c − ngày hoạt động gần nhất; c + 1 nếu không có lượt nhấp trong 0…c | ngày 0 đến c | AQ3 |
| trend_last_week | studentVle | lượt nhấp tuần gần nhất − lượt nhấp tuần trước đó | các tuần đến c | AQ3 |
| tasks_submitted_early_c | studentAssessment | các bài đến hạn sau c đã nộp tính đến hết ngày c | bài nộp ≤ c | AQ3 |
| clicks_oucontent_0c | studentVle, vle.activity_type | tổng trên trang nội dung | ngày 0 đến c | AQ2–AQ3 |
| clicks_forumng_0c | studentVle, vle.activity_type | tổng trên diễn đàn | ngày 0 đến c | AQ2–AQ3 |
| clicks_quiz_0c | studentVle, vle.activity_type | tổng trên bài kiểm tra ngắn | ngày 0 đến c | AQ2–AQ3 |
| clicks_homepage_0c | studentVle, vle.activity_type | tổng trên trang chủ | ngày 0 đến c | AQ2–AQ3 |
| early_sign_rule | suy ra | rule_missed or rule_tma_late or inactive_last7 | tại c | quy tắc so sánh của AQ3; KPI phụ 1 (C10) |
| early_sign_rule_cma | suy ra | early_sign_rule or cma_late_c ≥ 1 | tại c | biến thể dùng để phân tích độ nhạy |
| rule_missed | suy ra | tasks_missed_c ≥ 1 | tại c | thành phần của quy tắc |
| rule_tma_late | suy ra | tma_late_c ≥ 1 | tại c | thành phần của quy tắc |
| enrolled | các bảng đặc trưng | số lượt đăng ký học còn hiệu lực tại thời điểm chốt | kỳ mở, thời điểm chốt | AQ4 |
| tutor_groups_est | enrolled | ceil(enrolled / 20) | kỳ mở, thời điểm chốt | AQ4 (giả định nhóm 20 sinh viên) |
| list_tutor_3 | tutor_groups_est | 3 × số nhóm (≤ enrolled) | kỳ mở, thời điểm chốt | số sinh viên liên hệ được theo giả định của AQ4 |
| list_tutor_5 | tutor_groups_est | 5 × số nhóm (≤ enrolled) | kỳ mở, thời điểm chốt | số sinh viên liên hệ được theo giả định của AQ4 |
| list_office_30 | enrolled | min(30, enrolled) | kỳ mở, thời điểm chốt | số sinh viên liên hệ được theo giả định của AQ4 |
| list_office_40 | enrolled | min(40, enrolled) | kỳ mở, thời điểm chốt | số sinh viên liên hệ được theo giả định của AQ4 |
| clicks_w1 | studentVle | tổng theo tuần | tuần 1 (ngày 0–6) | quỹ đạo theo tuần của AQ3 |
| clicks_w2 | studentVle | tổng theo tuần | tuần 2 (ngày 7–13) | quỹ đạo theo tuần của AQ3 |
| clicks_w3 | studentVle | tổng theo tuần | tuần 3 (ngày 14–20) | quỹ đạo theo tuần của AQ3 |
| clicks_w4 | studentVle | tổng theo tuần | tuần 4 (ngày 21–27) | quỹ đạo theo tuần của AQ3 |

**Các lựa chọn khi xây dựng đặc trưng và các bộ đặc trưng.**

Hai định nghĩa trong bảng trên phản ánh lựa chọn của nhóm chúng em. Thứ nhất, một bài chỉ được tính là bỏ lỡ nếu bài đó đến hạn vào hoặc sau ngày đăng ký của sinh viên, vì sinh viên đăng ký muộn không thể bỏ lỡ một bài đã đến hạn trước khi sinh viên đó bắt đầu theo học. Thứ hai, tỷ lệ hoạt động so sánh một sinh viên với trung vị của chính kỳ mở đó tính đến cùng ngày; trung vị này đại diện cho "mức trung bình của kỳ mở" nêu trong dấu hiệu của AQ2. Công thức cộng thêm 1 vào cả tử số và mẫu số để tỷ lệ vẫn có giá trị xác định khi kỳ mở hoặc sinh viên không có lượt nhấp nào; đồng thời, tỷ lệ này không dùng biến kết quả, nên cán bộ có thể tính ngay vào ngày chốt dữ liệu.

**Các bộ đặc trưng.** Các bảng đặc trưng gồm 20 đặc trưng chính và 10 đặc trưng mở rộng, cùng số lượt nhấp theo tuần tính đến thời điểm chốt (hai tuần tại ngày 13 và bốn tuần tại ngày 27); mỗi cột còn lại là định danh, biến mục tiêu, cờ phục vụ đánh giá, quy tắc dấu hiệu sớm hoặc thuộc tính dùng để kiểm tra công bằng. Bộ đặc trưng chính bao gồm module và tháng bắt đầu, trình độ học vấn trước đó, số lần học trước, số tín chỉ đang học, thời điểm đăng ký sớm hay muộn, kết quả bảo lưu, hoạt động trước và sau ngày bắt đầu, tỷ lệ hoạt động, thời gian không hoạt động, cùng số bài và mức nộp trễ. Bộ đặc trưng mở rộng gồm mười đặc trưng dùng để so sánh ở Milestone 4: biến chỉ báo thiếu ngày đăng ký, số lượt nhấp đã loại trùng, số lượt nhấp trong 14 ngày trước ngày bắt đầu, số ngày kể từ lượt nhấp gần nhất, xu hướng trong tuần gần nhất, số bài nộp sớm, cùng số lượt nhấp vào trang nội dung, diễn đàn, bài kiểm tra ngắn và trang chủ. Tỷ lệ dòng có điểm CMA thấp hơn mức mà một đặc trưng cần có, như Mục 7.3 giải thích. Các thuộc tính nhân khẩu học chủ yếu phục vụ bước kiểm tra công bằng, vì các thử nghiệm trước đây tại OU cho thấy khi bổ sung các thuộc tính này vào dữ liệu hoạt động và dữ liệu bài được chấm điểm, khả năng dự báo sinh viên có nguy cơ không được cải thiện đáng kể [9]. Bảng A.12 liệt kê mọi biến đã chuẩn bị cùng nguồn và mục đích của từng biến.
