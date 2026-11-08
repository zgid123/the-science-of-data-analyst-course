## 3.5. Nhật ký vấn đề chất lượng dữ liệu

Các phát hiện của Mục 3.1 đến Mục 3.4 được quy về mười chín vấn đề theo mẫu Nhật ký vấn đề chất lượng dữ liệu (Data Quality Issue Log) của đề bài; mỗi vấn đề có bằng chứng, tác động đến các câu hỏi, mức độ nghiêm trọng và quyết định xử lý [1]. Mức độ nghiêm trọng được đánh giá theo tác động đến các AQ. Mức Cao dành cho vấn đề mà nếu bỏ qua sẽ làm thay đổi một tỷ lệ được báo cáo, biến mục tiêu hoặc một đặc trưng tại thời điểm chốt dữ liệu; mức Trung bình dành cho vấn đề làm thay đổi một thước đo với mức thay đổi đã biết; mức Thấp dành cho vấn đề chỉ liên quan đến ít bản ghi hoặc đến một trường không câu hỏi nào sử dụng. Bảng 3.1 liệt kê đủ mười chín vấn đề theo thứ tự, kèm bằng chứng chính; Phụ lục I (Bảng A.4) trình bày toàn bộ bằng chứng, kèm mục tương ứng trong kết quả khảo sát dữ liệu làm căn cứ cho từng số liệu.

**Bảng 3.1. Nhật ký vấn đề chất lượng dữ liệu**

| Mã | Biến / bảng | Bằng chứng | Tác động đến AQ | Mức độ nghiêm trọng | Quyết định |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle: dòng trùng lặp hoàn toàn | 787.170 dòng (7,39%); 3,19% số lượt nhấp | Thước đo lượt nhấp (AQ2, AQ3) | Trung bình | Giữ mọi dòng; mỗi đặc trưng lượt nhấp có thêm phiên bản đã bỏ dòng trùng để kiểm tra độ nhạy |
| DQ02 | studentVle: đơn vị của mỗi dòng (grain) | 1.614.505 bộ ba sinh viên – tài nguyên – ngày có nhiều dòng | Số đếm và phép nối bảng ở mức dòng | Trung bình | Cộng lượt nhấp theo lượt đăng ký học và ngày trước mọi phép nối; đếm số ngày hoạt động, không đếm số dòng |
| DQ03 | Hoạt động sau khi hủy đăng ký | 98.745 lượt nhấp và 588 bài nộp sau khi hủy đăng ký | Mức tham gia tính đến lúc rút khỏi module (AQ1, AQ2) | Trung bình | Chỉ tính mức tham gia đến ngày hủy đăng ký |
| DQ04 | final_result và ngày hủy đăng ký | 93 lượt Withdrawn không có ngày; 9 lượt Fail có ngày | Các lượt đăng ký học còn hiệu lực tại từng ngày; thời gian đến khi rút | Thấp | Giữ cả hai trường như đã ghi; gắn cờ cho 93 lượt và 9 lượt này |
| DQ05 | Đăng ký sau ngày 14 | 58 lượt đăng ký vào các ngày 16–167 | Mẫu số của KPI; các lượt đăng ký học còn hiệu lực tại các thời điểm chốt dữ liệu | Thấp | Điều kiện "đang đăng ký học vào ngày d" đòi hỏi đã đăng ký tính đến hết ngày d (C09) |
| DQ06 | Rút trước khi bắt đầu giảng dạy | 3.097 lượt hủy đăng ký tính đến ngày 0; một lượt vào ngày 444 của kỳ mở dài 268 ngày | Mẫu số của KPI | Thấp | Không phải lỗi; nằm ngoài nhóm tính KPI (các lượt đăng ký học còn hiệu lực tại ngày 14); bản ghi ngày 444 được giữ kèm cờ |
| DQ07 | Kết quả bảo lưu | 1.909 kết quả ghi ngày −1 | Thước đo thời điểm nộp và bài bỏ lỡ (AQ1–AQ3) | Trung bình | Không dùng để xác định thời điểm nộp; đếm riêng thành nhóm kết quả bảo lưu, vì kết quả này đã biết ngay từ lúc sinh viên đăng ký |
| DQ08 | Bài thi | 18 trong 24 bài thi không có dòng kết quả | Bài bỏ lỡ đầu tiên (AQ1); dấu hiệu từ bài được chấm điểm (AQ2, AQ3) | Cao | Bài được chấm điểm chỉ gồm TMA và CMA; không dùng điểm thi |
| DQ09 | Trọng số | Bài làm trong kỳ có trọng số 0 ở GGG; CCC năm 2014 có hai bài thi | Đặc trưng điểm có trọng số | Trung bình | Không tính điểm có trọng số; các bài được đếm như nhau |
| DQ10 | Bài nộp trễ | 32.991 trong 69.956 bài CMA và 16.320 trong 97.088 bài TMA nộp trễ | Dấu hiệu nộp trễ (AQ1, AQ2, quy tắc dấu hiệu sớm) | Trung bình | Giữ thông tin nộp trễ theo loại bài; quy tắc dùng nộp trễ TMA (C10) |
| DQ11 | Điểm số | Thiếu 173 điểm TMA | Đặc trưng điểm số | Thấp | Để trống điểm; chỉ dùng điểm đã biết tại thời điểm chốt dữ liệu |
| DQ12 | imd_band | Thiếu 1.111 giá trị; tỷ lệ đạt 65,7% so với 46,6% | Kiểm tra công bằng (AQ4); đặc trưng về đặc điểm cá nhân | Trung bình | Sửa nhãn; giữ "Missing" là một nhóm riêng; không điền giá trị thiếu |
| DQ13 | Ngày đăng ký | Thiếu 45 giá trị, 39 thuộc lượt Withdrawn | Đặc trưng khoảng cách từ ngày đăng ký đến ngày bắt đầu | Thấp | Để trống, kèm biến chỉ báo giá trị thiếu |
| DQ14 | Tuần theo kế hoạch của tài nguyên | Thiếu ở 82,4% tài nguyên | Không có | Thấp | Không sử dụng |
| DQ15 | Ngày không có lượt nhấp nào | Ngày 218–219 của mọi kỳ mở tháng 2 năm 2014 | Chuỗi thời gian theo ngày, sau tuần 30 | Thấp | Xử lý như dữ liệu thiếu, không tính là 0 |
| DQ16 | Giá trị ngoại lai về lượt nhấp và tín chỉ | 2.503 giá trị vượt ngưỡng; 655 tín chỉ | Phương pháp nhạy với thang đo | Thấp | Giữ mọi giá trị; dùng logarit trong ma trận sẵn sàng cho mô hình |
| DQ17 | Lượt đăng ký học không có hoạt động | 3.365 lượt không có lượt nhấp; 6.750 lượt không có bài nộp | Nối trong (inner join) sẽ loại các lượt này | Trung bình | Nối trái từ bảng lượt đăng ký học; số đếm bằng 0 |
| DQ18 | Bài đến hạn tính đến hết thời điểm chốt dữ liệu | Có bài đến hạn tính đến hết ngày 13 ở 1 kỳ mở, đến hết ngày 27 ở 16 kỳ mở | Quy tắc dấu hiệu sớm, dùng làm mốc so sánh cho mô hình ở AQ3; KPI phụ 1 | Cao | Phát biểu lại quy tắc theo các bài thực sự đến hạn (C10) |
| DQ19 | Tính đại diện | Bảy module của UK giai đoạn 2013–2014 | Mọi kết luận; so sánh giữa các nhóm | Cao | Nêu rõ phạm vi; so sánh trong cùng module; kiểm tra lại kết quả trên dữ liệu của trường |

Ba vấn đề được xếp mức Cao. Đối với kết quả bài thi bị thiếu (DQ08), nếu bài thi được tính là bài được chấm điểm thì mọi sinh viên của 5 module không có kết quả thi đều bị tính là bỏ lỡ bài thi; vì vậy, chỉ TMA và CMA được tính là bài được chấm điểm. Do chỉ có ít bài đến hạn tính đến các thời điểm chốt dữ liệu (DQ18), quy tắc dấu hiệu sớm sẽ không đánh dấu được sinh viên nào ở phần lớn kỳ mở, nên quy tắc được phát biểu lại (Mục 4.1). Cuối cùng, tổng thể nghiên cứu hẹp (DQ19) giới hạn mọi kết luận, nên phạm vi được nêu kèm từng kết quả.
