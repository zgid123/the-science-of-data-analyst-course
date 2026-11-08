## 2.1. Tổng thể, đơn vị phân tích và khóa

Một kỳ mở module (presentation) là một lần module được giảng dạy, bắt đầu vào một tháng nhất định; sau câu này, báo cáo gọi tắt là "kỳ mở". Tổng thể là các sinh viên đăng ký học trong 22 kỳ mở của bảy module OU, gồm bốn module thuộc khối khoa học, công nghệ, kỹ thuật và toán học, cùng ba module thuộc khối khoa học xã hội, được giảng dạy từ xa tại Vương quốc Anh (UK) trong năm 2013 và 2014 [2]. Tổng thể này gồm 32.593 lượt đăng ký học của 28.785 sinh viên, trong đó 3.538 sinh viên đăng ký nhiều hơn một kỳ mở. Mã kỳ mở kết thúc bằng B nếu kỳ mở bắt đầu vào tháng 2 và bằng J nếu bắt đầu vào tháng 10; nhóm tác giả bộ dữ liệu khuyến nghị phân tích riêng các kỳ mở B và J [2].

Đơn vị phân tích là lượt đăng ký học, tức một sinh viên trong một kỳ mở. Bảng 2.1 (Dataset Understanding Map, bản mô tả tổng quan bộ dữ liệu) liệt kê bảy tệp dữ liệu gốc. Với mỗi tệp, Bảng 2.1 nêu đơn vị phân tích, khóa, biến chính, trường thời gian và vai trò của tệp trong các AQ. Mọi khóa đều đã được kiểm tra trên dữ liệu.

**Bảng 2.1. Bản mô tả tổng quan bộ dữ liệu**

| Tệp / bảng | Đơn vị | Khóa chính | Khóa ngoại | Biến chính | Thời gian | Vai trò |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses (22) | kỳ mở module | module + kỳ mở | – | độ dài kỳ mở | độ dài kỳ mở | ngày kết thúc, tháng bắt đầu |
| assessments (206) | bài đánh giá | id_assessment | → courses | loại, trọng số | ngày đến hạn | bài đến hạn (AQ1–AQ3) |
| vle (6.364) | tài nguyên học tập | id_site | → courses | loại hoạt động | tuần dự kiến | loại tài nguyên (AQ2) |
| studentInfo (32.593) | lượt đăng ký học | kỳ mở + sinh viên | → courses | final_result, đặc điểm cá nhân | – | biến mục tiêu; kiểm tra công bằng (AQ1–AQ4) |
| studentRegistration (32.593) | lượt đăng ký học | kỳ mở + sinh viên | → studentInfo (1–1) | ngày đăng ký, ngày rút | các ngày | tổng thể, KPI |
| studentAssessment (173.912) | bài nộp | bài đánh giá + sinh viên | → assessments, studentInfo | ngày nộp, điểm | ngày nộp | bài bỏ lỡ, nộp trễ |
| studentVle (10.655.280) | bản ghi lượt nhấp | không có | → vle, studentInfo | số lượt nhấp | ngày tương tác | hoạt động (AQ2, AQ3) |

Sáu bảng có khóa đều có giá trị khóa không trùng lặp và không có dòng con nào thiếu dòng cha (Phụ lục I, Hình A.1); riêng bảng lượt nhấp không có khóa và được xem xét ở Mục 3.1.
