## 2.1. Tổng thể, đơn vị phân tích và khóa

**Tổng thể.** Dữ liệu mô tả các sinh viên đăng ký học trong 22 kỳ mở của bảy module OU (bốn module thuộc khối khoa học, công nghệ, kỹ thuật và toán học; ba module thuộc khối khoa học xã hội), được giảng dạy từ xa tại Vương quốc Anh (UK) trong năm 2013 và 2014 [2]. Các module mang mã đã ẩn danh, từ AAA đến GGG [2]. Dữ liệu gồm 32.593 lượt đăng ký học của 28.785 sinh viên; trong đó 3.538 sinh viên đăng ký nhiều hơn một kỳ mở, do học đồng thời hai module hoặc đăng ký cùng module ở một kỳ mở sau. Mã kỳ mở như 2013J kết thúc bằng B nếu kỳ mở bắt đầu vào tháng 2 và bằng J nếu bắt đầu vào tháng 10; các tác giả của bộ dữ liệu khuyến nghị phân tích riêng các kỳ mở B và J [2]. Hình thức học từ xa của sinh viên OU khác với các học phần trực tuyến và học phần kết hợp của chương trình đào tạo tại Việt Nam; Mục 3.4 phân tích ý nghĩa của khác biệt này đối với các kết luận.

**Đơn vị phân tích.** Đơn vị phân tích là lượt đăng ký học, nghĩa là một sinh viên trong một kỳ mở module, vì biến kết quả, mẫu số của KPI và quyết định liên hệ đều xét một sinh viên trong một học phần cụ thể. Một số bảng có đơn vị chi tiết hơn, chẳng hạn một bài nộp hoặc số lượt nhấp trong một ngày trên một tài nguyên. Các bảng này được cộng gộp về mức lượt đăng ký học trước khi nối bảng (Mục 6.2). Nhờ đó, mỗi bảng dữ liệu đã chuẩn bị chỉ có một đơn vị của mỗi dòng (grain) và đơn vị này được nêu rõ.

**Khóa và quan hệ.** Bảng 2.1 là bảng mô tả cấu trúc bộ dữ liệu, tức Dataset Understanding Map mà đề bài yêu cầu. Với mỗi bảng, Bảng 2.1 nêu đơn vị, khóa chính, khóa ngoại và quan hệ với bảng cha, các biến chính, trường thời gian và vai trò trong các câu hỏi [1]. Khóa chính là cột hoặc tổ hợp cột xác định duy nhất một dòng; khóa ngoại trỏ tới dòng của bảng khác mà dòng hiện tại thuộc về. Mỗi khóa trong Bảng 2.1 đều đã được kiểm tra trên dữ liệu.

**Bảng 2.1. Bảng mô tả cấu trúc bộ dữ liệu (Dataset Understanding Map)**

| Tệp / bảng (số dòng) | Đơn vị phân tích | Khóa chính | Khóa ngoại và quan hệ | Biến chính | Trường thời gian | Vai trò trong AQ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses (22) | kỳ mở module | module + kỳ mở | – | độ dài kỳ mở tính theo ngày | độ dài kỳ mở (số ngày) | cho biết ngày kết thúc và tháng bắt đầu của kỳ mở |
| assessments (206) | bài đánh giá | id_assessment | → courses, nhiều – một | loại (TMA, CMA, bài thi), trọng số | ngày đến hạn | bài đến hạn tính đến mỗi thời điểm chốt dữ liệu (AQ1–AQ3) |
| vle (6.364) | tài nguyên học tập | id_site | → courses, nhiều – một | loại hoạt động | tuần theo kế hoạch | loại tài nguyên (AQ2) |
| studentInfo (32.593) | lượt đăng ký học | kỳ mở + sinh viên | → courses, nhiều – một | final_result, đặc điểm cá nhân | – | biến mục tiêu; thuộc tính dùng để kiểm tra công bằng (AQ1–AQ4) |
| studentRegistration (32.593) | lượt đăng ký học | kỳ mở + sinh viên | → studentInfo, một – một | ngày đăng ký và ngày hủy đăng ký | các ngày | các lượt đăng ký học còn hiệu lực tại từng ngày; mẫu số của KPI |
| studentAssessment (173.912) | bài nộp | bài đánh giá + sinh viên | → assessments và studentInfo, nhiều – một | ngày nộp, điểm, cờ kết quả bảo lưu | ngày nộp | bài bỏ lỡ và bài nộp trễ |
| studentVle (10.655.280) | bản ghi lượt nhấp | không có | → vle và studentInfo, nhiều – một | số lượt nhấp | ngày tương tác | hoạt động (AQ2, AQ3) |

Sáu bảng có khóa đều không có giá trị khóa trùng lặp; đồng thời, mọi dòng của bảng con đều tìm thấy dòng tương ứng ở bảng cha. Nhờ đó, mọi bài nộp, bản ghi lượt nhấp và bản ghi đăng ký đều thuộc về một lượt đăng ký học, bài đánh giá hoặc tài nguyên đã biết (Phụ lục I, Hình A.1). Riêng bảng lượt nhấp studentVle không có khóa: cùng một sinh viên, tài nguyên và ngày có thể xuất hiện ở nhiều dòng; Mục 3.1 xem xét hiện tượng này.
