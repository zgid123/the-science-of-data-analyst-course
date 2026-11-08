# 3. Chiến lược tìm kiếm bộ dữ liệu mở

**Điểm xuất phát của quá trình tìm kiếm.** Nhóm chúng em bắt đầu tìm kiếm từ các yêu cầu ở Mục 2, không phải từ những bộ dữ liệu chúng em đã biết, để chính các câu hỏi quyết định cần tìm gì [1]. Từ khóa tìm kiếm được rút ra từ ma trận yêu cầu, gồm: hoàn thành học phần, thôi học và rút học phần; tương tác trên hệ thống quản lý học tập hoặc môi trường học tập ảo (VLE), là nền tảng trực tuyến nơi sinh viên mở tài liệu và nộp bài; nộp bài được chấm điểm; dữ liệu lượt nhấp (clickstream), là bản ghi từng lượt nhấp của sinh viên trên nền tảng đó; giáo dục đại học; phân tích học tập (learning analytics); bỏ học trong khóa học trực tuyến mở đại trà (MOOC).

**Các nguồn được tìm kiếm.** Phạm vi tìm kiếm gồm các nguồn đề bài gợi ý [1]; Kho dữ liệu học máy của Đại học California tại Irvine (UCI); các kho dữ liệu cấp mã định danh đối tượng số (DOI), tức là mã tham chiếu cố định cho một bộ dữ liệu, như figshare, Harvard Dataverse và Zenodo; trang của các nhóm nghiên cứu công bố bộ dữ liệu; tìm kiếm chung trên web.

**Ba quy tắc cho mọi kết quả.** Theo yêu cầu của đề bài, chúng em áp dụng ba quy tắc cho mọi bộ dữ liệu tìm được [1]. Thứ nhất, chúng em đọc tài liệu mô tả và giấy phép trước khi đánh giá dữ liệu. Thứ hai, bộ dữ liệu tìm thấy trên Kaggle, trên blog hoặc ở một bản sao khác được truy nguyên về nhà cung cấp đã công bố bộ dữ liệu đó. Thứ ba, các bản đăng lại không rõ nguồn gốc bị loại.

**Kết quả tìm kiếm.** Nhật ký tìm kiếm ở Phụ lục I ghi lại 16 mục, gồm 11 lượt tìm kiếm và các kết quả phát sinh thêm từ những lượt đó, kể cả các kết quả bị loại. Các kết quả bị loại gồm bản sao của bài mô tả dữ liệu mà chúng em đã có; địa chỉ web cũ đã được thay thế; dữ liệu KDD Cup 2015 do bên thứ ba đăng lại; các bản mô tả bộ dữ liệu từ nguồn thứ cấp. Sau khi loại các kết quả này, chúng em còn lại bảy bộ dữ liệu ứng viên, nhiều hơn ba bộ mà đề bài yêu cầu; thông tin về mỗi bộ đều lấy từ trang chính thức hoặc bài mô tả dữ liệu của bộ đó. Bảng 3.1 tóm tắt bảy ứng viên này: nhà cung cấp, tổng thể được mô tả, đơn vị phân tích, biến kết quả và cách ghi nhận thời gian trong khóa học.

**Bảng 3.1. Các bộ dữ liệu mở ứng viên**

| Ứng viên | Nhà cung cấp và nguồn | Tổng thể | Đơn vị phân tích | Biến kết quả | Mốc thời gian trong khóa học |
| :---- | :---- | :---- | :---- | :---- | :---- |
| A. OULAD | The Open University (UK); trang của nhà cung cấp và bài mô tả dữ liệu [2], [3] | Sinh viên của bảy module đào tạo từ xa, 2013–2014 [3] | Sinh viên – module – kỳ mở module [3] | Kết quả cuối cùng, gồm cả giá trị Withdrawal kèm ngày hủy đăng ký [3] | Ngày đến hạn và ngày nộp của bài được chấm điểm; số lượt nhấp theo ngày [3] |
| B. UCI 697 Dropout and Academic Success | Polytechnic Institute of Portalegre; trang UCI và bài mô tả dữ liệu [4], [5] | Sinh viên đại học của một trường, 2008–2019 [5] | Sinh viên [4] | Thôi học, đang học hoặc đã tốt nghiệp [4] | Chỉ có số liệu gộp theo học kỳ [5] |
| C. UCI 320 Student Performance | Hai trường trung học ở Bồ Đào Nha; trang UCI [6] | Học sinh trung học [6] | Học sinh – môn học [6] | Điểm từ 0 đến 20 [6] | Ba điểm trong mỗi năm học [6] |
| D. UCI 856 Higher Education Students Performance Evaluation | Một đợt thu thập năm 2019; trang UCI [7] | Sinh viên của hai khoa [7] | Câu trả lời bảng hỏi [7] | Điểm chữ [7] | Không có [7] |
| E. Dữ liệu bỏ học MOOC của XuetangX | Đại học Thanh Hoa, MOOCData [8], [9] | Người dùng một nền tảng MOOC ở Trung Quốc, 2015–2017 [8] | Người dùng – khóa học [8] | Bỏ học hoặc không bỏ học [8] | Hành động có dấu thời gian [8] |
| F. HarvardX Person-Course 2013 | HarvardX, Harvard Dataverse [10] | Người học của HarvardX, 2012–2013 [10] | Số liệu gộp theo người học – khóa học [10] | Được cấp chứng chỉ | Chỉ có thời điểm hoạt động đầu tiên và cuối cùng [10] |
| G. xAPI-Edu-Data | Dữ liệu từ nền tảng Kalboard 360; trang Kaggle của nhóm tác giả [11] | Học sinh ở nhiều quốc gia [11] | Học sinh [11] | Khoảng điểm [11] | Tài liệu không nêu |

Bảng trên đã cho thấy điểm khác biệt chính giữa các ứng viên. Chỉ OULAD và dữ liệu XuetangX ghi lại thời điểm sinh viên thực hiện từng hoạt động trong khóa học, là thông tin AQ2 và AQ3 cần đến. Ngoài ra, chỉ OULAD kết hợp thông tin thời gian đó với biến kết quả có ghi nhận việc rút khỏi module và với các bài được chấm điểm có ngày. Mục 4 kiểm tra nhận định ban đầu này bằng các điều kiện bắt buộc và các tiêu chí của đề bài.
