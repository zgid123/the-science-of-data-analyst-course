## Phụ lục I – Chi tiết về hiểu dữ liệu, khảo sát dữ liệu (profiling) và chất lượng dữ liệu

Hình A.1 trình bày bảy bảng của OULAD cùng số dòng và các khóa liên kết giữa chúng; từng liên kết đều đã được kiểm tra trên dữ liệu (`understanding.json`).

![Hình A.1. Các bảng, số dòng và khóa của OULAD](assets/figures/fig-2-1-tables.png)

Hình A.2 cho thấy số lượt nhấp mỗi tuần trên một sinh viên đang đăng ký học, theo tháng bắt đầu, kèm hai thời điểm chốt dữ liệu vào cuối tuần 2 và cuối tuần 4 (`fig_weekly_activity.csv`).

![Hình A.2. Số lượt nhấp mỗi tuần trên một sinh viên đang đăng ký học theo tháng bắt đầu, kèm hai thời điểm chốt dữ liệu](assets/figures/fig-3-2-weekly.png)

Bảng A.1 liệt kê các đầu vào mà đề bài yêu cầu, được kiểm tra trước khi bắt đầu chuẩn bị dữ liệu, cùng trạng thái của từng đầu vào.

**Bảng A.1. Các đầu vào từ Milestone 2 và trạng thái**

| Đầu vào (đề bài) | Nội dung trong dự án | Trạng thái |
| :---- | :---- | :---- |
| Phiên bản cơ sở của Milestone 1 | Business Goal, SMART Goal, các KPI, AQ1–AQ4, loại phân tích và các quyết định, được chốt bằng mã kiểm tra SHA-256 của từng tệp; cả 8 tệp nguồn không thay đổi | Đầy đủ |
| Ma trận truy vết đã cập nhật | KPI → AQ → yêu cầu dữ liệu → tệp → biến thực tế → mức đáp ứng → quyết định | Đầy đủ |
| Gói dữ liệu gốc | Bảy bảng CSV của OULAD, phiên bản 1 trên figshare, DOI 10.6084/m9.figshare.5081998.v1, mỗi bảng khớp với giá trị SHA-256 tham chiếu ghi sẵn | Đầy đủ, khớp 7/7 |
| Metadata và từ điển dữ liệu | Định nghĩa các cột theo bài mô tả dữ liệu, giấy phép CC BY 4.0, thông tin trích dẫn | Đầy đủ |
| Bằng chứng thu thập | Địa chỉ web, DOI, ngày truy cập 06/11/2026 (UTC+7), phiên bản, mã kiểm tra, nhật ký thu thập | Đầy đủ |
| Nhật ký thay đổi có kiểm soát | C01–C08, kèm nội dung cũ, nội dung mới và bằng chứng dữ liệu | Đầy đủ |

Bảng A.2 giải thích ý nghĩa của từng trường ngày và từng đại lượng đo trong OULAD, cùng thời điểm giá trị được biết; ý nghĩa lấy từ bài mô tả dữ liệu và chính sách đánh giá của OU, còn các số đếm lấy từ `understanding.json`.

**Bảng A.2. Ý nghĩa và thời điểm có giá trị của các trường chính**

| Trường | Ý nghĩa | Đơn vị và thang đo | Thời điểm được biết |
| :---- | :---- | :---- | :---- |
| date_registration, date_unregistration | Ngày sinh viên đăng ký và hủy đăng ký; ngày hủy đăng ký để trống nghĩa là sinh viên không rút | ngày (từ ngày 0) | chính ngày đó |
| assessments.date | Ngày đến hạn (cut-off) của bài đánh giá | ngày | từ khi kỳ mở bắt đầu |
| date_submitted | Ngày sinh viên nộp bài; cả 1.909 kết quả bảo lưu đều mang giá trị −1, là giá trị giữ chỗ | ngày | chính ngày đó |
| is_banked | Kết quả được chuyển từ một kỳ mở trước | 0/1 | khi đăng ký |
| score | Điểm, 0–100; dưới 40 là không đạt | điểm | TMA: giảng viên hướng dẫn chấm, thường trong vòng mười ngày làm việc sau ngày đến hạn; CMA: chấm tự động, trong vòng 7 ngày |
| weight | Tỷ trọng trong điểm tổng kết; bài thi chiếm 100, các bài đánh giá còn lại cộng lại chiếm 100 | % | từ khi bắt đầu |
| sum_click | Số lượt tương tác với một tài nguyên học tập trong một ngày | số đếm | chính ngày đó |
| studied_credits | Tổng tín chỉ của mọi module học cùng lúc; 60 tín chỉ một năm là học bán thời gian, 120 là toàn thời gian | tín chỉ | khi đăng ký |

Bảng A.3 liệt kê sáu thuộc tính nhạy cảm cùng mã giá trị, nhóm nhỏ nhất và số nhóm theo kỳ mở module có dưới 20 sinh viên.

**Bảng A.3. Các thuộc tính nhạy cảm**

| Thuộc tính | Mã giá trị | Nhóm nhỏ nhất | Số nhóm theo kỳ mở dưới 20 | Bản chất |
| :---- | :---- | :---- | :---- | :---- |
| gender | F, M | F: 14.718 | 0 | Cá nhân |
| age_band | 0-35, 35-55, 55<= | 55<=: 216 | 18 | Cá nhân |
| disability | Y, N (tự khai) | Y: 3.164 | 1 | Liên quan đến sức khỏe |
| imd_band | mười nhóm thập phân vị, để trống | để trống: 1.111 | 11 | Kinh tế – xã hội, theo khu vực |
| region | 13 vùng | Ireland: 1.184 | 11 | Vị trí |
| highest_education | năm cấp | Postgraduate: 313 | 29 | Kinh tế – xã hội |

Nhật ký vấn đề chất lượng dữ liệu (Data Quality Issue Log) trong Bảng A.4 trình bày đầy đủ bằng chứng cho từng vấn đề của Bảng 3.1; tiền tố P. chỉ các phần của `data/metadata/profile.json`, còn U. chỉ các khóa của `understanding.json`.

**Bảng A.4. Nhật ký vấn đề chất lượng dữ liệu kèm bằng chứng**

| Mã | Biến / bảng | Bằng chứng | Ảnh hưởng đến AQ | Mức độ | Quyết định |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle: dòng trùng lặp hoàn toàn | 787.170 dòng (7,39%) lặp lại một dòng khác ở mọi cột; 3,82–11,73% theo kỳ mở; 69,8% số nhóm trùng lặp chỉ có một lượt nhấp; gộp các dòng này làm mất 3,19% số lượt nhấp (P.duplicates). Trong các nhóm sinh viên – tài nguyên – ngày có hai dòng, 31,5% có số lượt nhấp bằng nhau, so với 24,0% kỳ vọng do ngẫu nhiên tính từ chính số lượt nhấp của từng tài nguyên (Bảng A.6) | Các đại lượng lượt nhấp của AQ2 và AQ3 | Trung bình | Dữ liệu không đủ để xác định nguyên nhân: giữ mọi dòng trong các đại lượng lượt nhấp chính (theo mức chi tiết bản ghi của bảng) và dựng phiên bản đã loại dòng trùng cho từng đặc trưng lượt nhấp để phân tích độ nhạy |
| DQ02 | studentVle: mức chi tiết khác với tài liệu | 1.614.505 nhóm sinh viên – tài nguyên – ngày có nhiều dòng (3.810.465 dòng), trong đó 1.179.074 nhóm có số lượt nhấp khác nhau; một nhóm có tối đa 10 dòng (P.shape) | Mọi phép nối bảng hoặc phép đếm ở mức dòng sẽ nhầm bản ghi với ngày | Trung bình | Gộp lượt nhấp theo lượt đăng ký học × ngày và lượt đăng ký học × tuần trước mọi phép nối bảng; đếm số ngày hoạt động, không đếm số dòng |
| DQ03 | studentVle, studentAssessment: hoạt động sau khi hủy đăng ký | 29.440 dòng lượt nhấp (98.745 lượt nhấp) của 1.279 lượt đăng ký học, muộn nhất 423 ngày sau khi hủy đăng ký; 588 bài nộp không bảo lưu của 411 lượt đăng ký học (P.validity) | Mức tham gia đến lúc rút (AQ1, AQ2); không ảnh hưởng tại thời điểm chốt đối với sinh viên còn đăng ký | Trung bình | Cắt các đại lượng mức tham gia tại ngày hủy đăng ký; các bảng đặc trưng chỉ chứa sinh viên còn đăng ký tại thời điểm chốt, nên không sự kiện nào sau khi rút đi vào các bảng này |
| DQ04 | final_result × date_unregistration | 93 lượt đăng ký học Withdrawn không có ngày hủy đăng ký, 87 lượt trong số đó thuộc các kỳ mở tháng 10 năm 2014; 9 lượt đăng ký học Fail có ngày hủy đăng ký, 8 lượt trong số đó vào ngày 0 hoặc sớm hơn (U.outcome, P.validity) | Tổng thể tại ngày 14, 13 và 27; thời gian đến khi rút | Thấp | Giữ final_result làm biến kết quả; giữ ngày đã ghi nhận; gắn cờ cho cả hai nhóm (`withdrawal_day_missing`, `unregistered_not_withdrawn`); 93 lượt này vẫn nằm trong mọi tổng thể vì không bản ghi nào cho thấy sinh viên rời đi trước thời điểm chốt; một cờ đánh giá cho phép báo cáo các chỉ số trên tập kiểm thử khi có và khi không có các lượt này |
| DQ05 | studentRegistration: đăng ký sau ngày 14 | 58 lượt đăng ký học có ngày đăng ký từ ngày 16 đến ngày 167, sau thời hạn đăng ký hai tuần theo bài mô tả dữ liệu; 16 lượt trong số đó về sau hủy đăng ký (P.validity, nhật ký kiểm tra T08) | Mẫu số của KPI và tổng thể tại các thời điểm chốt | Thấp | Định nghĩa "đang đăng ký học vào ngày d" là đã đăng ký đến ngày d (hoặc không rõ ngày đăng ký) và chưa hủy đăng ký đến ngày d; sinh viên đăng ký muộn chỉ vào tổng thể của các ngày về sau |
| DQ06 | studentRegistration: rời đi trước khi giảng dạy | 3.097 lượt đăng ký học hủy đăng ký vào ngày 0 hoặc sớm hơn; một lượt hủy đăng ký vào ngày 444 của một kỳ mở dài 268 ngày (U.outcome) | Mẫu số của KPI | Thấp | Không phải lỗi: các sinh viên này rời đi trước khi kỳ mở bắt đầu và nằm ngoài tổng thể KPI tại ngày 14; bản ghi ngày 444 được giữ lại kèm cờ |
| DQ07 | studentAssessment: kết quả bảo lưu | Cả 1.909 kết quả bảo lưu đều có date_submitted = −1, là giá trị giữ chỗ cho kết quả chuyển từ một kỳ mở trước (P.validity) | Các đại lượng về nộp đúng hạn và bài bỏ lỡ (AQ1–AQ3) | Trung bình | Loại các dòng bảo lưu khỏi phép tính thời điểm nộp, nộp trễ và số bài bỏ lỡ; giữ số kết quả bảo lưu của mỗi lượt đăng ký học, giá trị này biết được ngay khi đăng ký |
| DQ08 | assessments, studentAssessment: bài thi | 18 trên 24 bài thi không có dòng kết quả (chỉ có điểm cho CCC 2 và DDD 4); 11 bài thi không có ngày đến hạn (P.missing, U.time) | "Bài được chấm điểm đầu tiên bị bỏ lỡ" (AQ1); dấu hiệu về bài (AQ2, AQ3) | Cao (bài thi) | Chỉ đếm bài bỏ lỡ và bài nộp trễ trên TMA và CMA; biến kết quả vẫn là final_result; không dùng điểm thi |
| DQ09 | assessments: tỷ trọng | Tổng tỷ trọng bài tập trong kỳ bằng 0 ở ba kỳ mở GGG và bằng 100 ở các kỳ mở khác; các CMA của FFF có tỷ trọng 0; các kỳ mở CCC năm 2014 có hai bài thi (tổng 200) (P.validity, U.measurement) | Các đặc trưng điểm có trọng số | Trung bình | Không dựng điểm tổng kết có trọng số; đếm bài không theo trọng số (bài đánh giá không tính điểm vẫn có ngày đến hạn) và giữ weight thành một cột |
| DQ10 | studentAssessment: bài nộp trễ và nộp sau khi kỳ mở kết thúc | 49.318 trên 169.138 bài nộp không bảo lưu có ngày đến hạn bị trễ (29,2%; trung vị 3 ngày, phân vị thứ 99 là 29 ngày): 16.320 trên 97.088 TMA và 32.991 trên 69.956 CMA, dù chính sách hiện hành (2025) của OU không nhận CMA nào sau ngày đến hạn; 85 bài nộp sau khi kỳ mở kết thúc, muộn nhất vào ngày 608 (P.validity) | Dấu hiệu nộp trễ (AQ1, AQ2, quy tắc dấu hiệu sớm) | Trung bình | Giữ mọi bài nộp; số ngày trễ = date_submitted − ngày đến hạn, đếm riêng cho TMA và CMA vì ý nghĩa của một CMA nộp trễ trong giai đoạn 2013–2014 không được ghi trong tài liệu; các bài nộp sau khi kỳ mở kết thúc đều nằm sau cả hai thời điểm chốt |
| DQ11 | studentAssessment.score | 173 điểm bị thiếu, đều là TMA (P.missing); 45,8% điểm CMA là bội số của 10, so với 17,4% ở TMA (P.distribution) | Các đặc trưng về điểm | Thấp | Giữ bài nộp, để trống điểm; điểm chỉ đi vào đặc trưng khi đã biết tại thời điểm chốt (ma trận quyết định, dòng "Derived feature") |
| DQ12 | studentInfo.imd_band | 1.111 giá trị thiếu (3,41%), chiếm 40,1% ở North Region và 22,5% ở Ireland; tỷ lệ đạt là 65,7% khi thiếu so với 46,6% khi có, nên giá trị không thiếu ngẫu nhiên; một nhãn "10-20" thiếu dấu % (P.missing, P.validity) | Kiểm tra công bằng của AQ4 theo mức khó khăn của khu vực; các đặc trưng về đặc điểm cá nhân | Trung bình | Chuẩn hóa nhãn thành "10-20%"; giữ giá trị thiếu thành một nhóm riêng "Missing"; không điền giá trị thiếu |
| DQ13 | studentRegistration.date_registration | 45 giá trị thiếu, 39 trong số đó là Withdrawn (P.missing) | Đặc trưng số ngày đăng ký trước khi bắt đầu | Thấp | Giữ giá trị rỗng kèm biến chỉ báo; mọi phép điền giá trị thiếu chỉ được ước lượng trên các kỳ mở huấn luyện |
| DQ14 | vle.week_from, week_to | 82,4% giá trị thiếu; chỉ có giá trị cho 1.121 trên 6.364 tài nguyên (P.missing, U.time) | Không | Thấp | Không sử dụng |
| DQ15 | studentVle: các ngày không có lượt nhấp nào | Ở cả sáu kỳ mở tháng 2 năm 2014, hai ngày liên tiếp không có lượt nhấp nào (ngày 218–219; ngày 211–212 ở BBB) (P.temporal) | Chuỗi hoạt động theo ngày sau tuần 30 | Thấp | Coi hai ngày này là dữ liệu thiếu, không phải không hoạt động, trong chuỗi theo ngày; cả hai ngày đều nằm sau các thời điểm chốt |
| DQ16 | Giá trị ngoại lai: lượt nhấp và tín chỉ | Một dòng có 6.977 lượt nhấp; độ lệch của số lượt nhấp trên mỗi lượt đăng ký học là 3,03, với 2.503 lượt đăng ký học vượt ngưỡng trên theo khoảng tứ phân vị; studied_credits lên tới 655, so với phân vị thứ 99 là 240 (P.distribution) | Các phương pháp nhạy với thang đo | Thấp | Giữ mọi giá trị (người dùng hoạt động nhiều và sinh viên học nhiều module là có thật); phép biến đổi log hoặc xếp hạng được áp dụng khi lập mô hình, với tham số ước lượng trên các kỳ mở huấn luyện |
| DQ17 | Lượt đăng ký học không có dòng hoạt động hoặc bài nộp nào | 3.365 lượt đăng ký học không có dòng lượt nhấp (2.988 Withdrawn; 2.390 rời đi trước hoặc vào ngày 0); 6.750 lượt không có bài nộp (P.missing) | Phép nối trong (inner join) sẽ làm mất các sinh viên này khỏi phép đếm | Trung bình | Không có dòng nghĩa là không có hoạt động (theo bài mô tả dữ liệu: không nộp bài thì không có dòng kết quả): điền 0 vào các số đếm sau phép nối trái từ bảng lượt đăng ký học |
| DQ18 | assessments: các bài đến hạn tính đến hết thời điểm chốt | Bài không phải bài thi có ngày đến hạn tính đến hết ngày 13 ở 1 trên 22 kỳ mở và tính đến hết ngày 27 ở 16 lượt; có từ hai bài trở lên đến hạn tính đến hết ngày 27 ở 1 kỳ mở duy nhất (P.temporal) | Quy tắc so sánh của AQ3 và KPI phụ 1 ("bỏ lỡ hoặc nộp trễ từ hai bài trở lên tính đến hết tuần 4") chỉ có thể kích hoạt ở 1 trên 22 kỳ mở | Cao | Quyết định ở Nhiệm vụ 3 (mức phù hợp giữa AQ và dữ liệu): phát biểu lại quy tắc trên các bài thực sự đến hạn (nhật ký thay đổi, C10) |
| DQ19 | Tổng thể và cơ cấu module | Bảy module đào tạo từ xa của UK giai đoạn 2013–2014, được chọn một phần vì có nhiều sinh viên không đạt; nữ chiếm 11,5% ở EEE và 88,4% ở BBB; tỷ lệ hoàn thành trong tổng thể ngày 14 từ 45,7% (CCC) đến 73,8% (AAA) (P.representativeness) | Khả năng tổng quát hóa của mọi AQ; so sánh giữa các nhóm | Cao (nhận định) | Nêu rõ phạm vi; so sánh các nhóm trong cùng module; kết quả mô tả OULAD và phải được kiểm tra lại trên dữ liệu của trường trước các quyết định D1–D3 |

Mười ba con số trong kết quả khảo sát dữ liệu đã được đếm lại bằng một lần khám phá độc lập trên cùng các tệp với mã riêng (`profile_crosscheck.csv`); Bảng A.5 trình bày 13 đại lượng được so sánh, tất cả đều bằng nhau.

**Bảng A.5. Đối chiếu với một lần đếm lại độc lập**

| Đại lượng | Lần đếm lại độc lập | Kết quả khảo sát Milestone 3 | Bằng nhau |
| :---- | :---- | :---- | :---- |
| Dòng trùng lặp hoàn toàn trong studentVle | 787.170 | 787.170 | có |
| Lượt nhấp gốc | 39.605.099 | 39.605.099 | có |
| Lượt nhấp sau khi gộp dòng trùng lặp | 38.343.063 | 38.343.063 | có |
| Nhóm sinh viên – tài nguyên – ngày bị lặp | 1.614.505 | 1.614.505 | có |
| Số dòng trong các nhóm bị lặp | 3.810.465 | 3.810.465 | có |
| Lượt đăng ký học không có hoạt động | 3.365 | 3.365 | có |
| Lượt đăng ký học không có bài nộp | 6.750 | 6.750 | có |
| Bài nộp trễ | 49.318 | 49.318 | có |
| Bài nộp sau khi kỳ mở kết thúc | 85 | 85 | có |
| Dòng lượt nhấp sau khi hủy đăng ký | 29.440 | 29.440 | có |
| Lượt đăng ký học có lượt nhấp sau khi hủy đăng ký | 1.279 | 1.279 | có |
| Bài nộp sau khi hủy đăng ký (gồm 13 dòng bảo lưu ghi ngày -1) | 601 | 601 | có |
| Dòng lượt nhấp trước ngày 0 | 688.988 | 688.988 | có |

Phép kiểm tra so với mức ngẫu nhiên đối với các dòng lượt nhấp trùng lặp xét 1.311.841 nhóm sinh viên – tài nguyên – ngày có đúng hai dòng. Phép kiểm tra này so sánh tỷ lệ nhóm có số lượt nhấp bằng nhau (31,5%) với tỷ lệ kỳ vọng do ngẫu nhiên, tính từ chính số lượt nhấp của từng tài nguyên (24,0%) hoặc của từng loại hoạt động (21,7%). Bảng A.6 trình bày tỷ lệ quan sát được ở sáu loại hoạt động có nhiều nhóm như vậy nhất.

**Bảng A.6. Tỷ lệ số lượt nhấp bằng nhau trong các nhóm hai dòng, theo loại hoạt động**

| Loại hoạt động | Số nhóm hai dòng | Tỷ lệ bằng nhau quan sát được |
| :---- | :---- | :---- |
| `forumng` | 895.551 | 32,8% |
| `oucontent` | 279.561 | 32,2% |
| `quiz` | 71.751 | 11,5% |
| `ouwiki` | 21.555 | 7,7% |
| `questionnaire` | 14.694 | 6,0% |
| `oucollaborate` | 11.921 | 59,6% |
