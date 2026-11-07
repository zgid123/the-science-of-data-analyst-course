# 3. Chiến lược tìm kiếm bộ dữ liệu mở

Nhóm phân tích dữ liệu bắt đầu tìm kiếm từ các yêu cầu ở Mục 2, không phải từ những bộ dữ liệu đã biết. Từ khóa tìm kiếm được rút ra từ ma trận yêu cầu, gồm: hoàn thành học phần, thôi học và rút học phần; tương tác trên hệ thống quản lý học tập hoặc môi trường học tập ảo; nộp bài được chấm điểm; dữ liệu lượt nhấp (clickstream); giáo dục đại học; phân tích học tập (learning analytics); và bỏ học trong khóa học trực tuyến mở đại trà (MOOC). Phạm vi tìm kiếm gồm các nguồn đề bài gợi ý [1]; Kho dữ liệu học máy của Đại học California tại Irvine (UCI); các kho dữ liệu có mã định danh đối tượng số (DOI), gồm figshare, Harvard Dataverse và Zenodo; trang của các nhóm nghiên cứu cung cấp dữ liệu; và tìm kiếm trên web. Với mọi kết quả tìm được, nhóm áp dụng ba quy tắc: đọc tài liệu mô tả và giấy phép trước khi đánh giá dữ liệu; truy nguyên về nhà cung cấp mọi bộ dữ liệu tìm thấy trên Kaggle, blog hoặc bản sao; và loại các bản đăng lại không rõ nguồn gốc dữ liệu [1].

Nhật ký tìm kiếm ở Phụ lục I ghi lại 16 truy vấn cùng các kết quả tìm được, kể cả những kết quả bị loại. Các kết quả bị loại gồm bản sao của bài mô tả dữ liệu mà nhóm đã có; địa chỉ cũ đã được thay thế; dữ liệu KDD Cup 2015 do bên thứ ba đăng lại; và metadata từ nguồn thứ cấp. Sau khi loại các kết quả này, còn lại bảy bộ dữ liệu ứng viên; thông tin về mỗi bộ lấy từ trang chính thức hoặc bài mô tả dữ liệu của bộ đó. Bảng 3.1 tóm tắt bảy ứng viên này.

**Bảng 3.1. Các bộ dữ liệu mở ứng viên**

| Ứng viên | Nhà cung cấp và nguồn | Tổng thể | Đơn vị phân tích | Biến kết quả | Mốc thời gian trong khóa học |
| :---- | :---- | :---- | :---- | :---- | :---- |
| A. OULAD | The Open University (UK); trang của nhà cung cấp, bài mô tả dữ liệu [2], [3] | Bảy module đào tạo từ xa, 2013–2014 [3] | Sinh viên – module – kỳ mở module [3] | Kết quả cuối cùng (có giá trị Withdrawal), kèm ngày hủy đăng ký [3] | Ngày đến hạn và ngày nộp của bài được chấm điểm; số lượt nhấp theo ngày [3] |
| B. UCI 697 Dropout and Academic Success | Polytechnic Institute of Portalegre; UCI và bài mô tả dữ liệu [4], [5] | Sinh viên đại học của một trường, 2008–2019 [5] | Sinh viên [4] | Thôi học, đang học hoặc đã tốt nghiệp [4] | Chỉ có số liệu gộp theo học kỳ [5] |
| C. UCI 320 Student Performance | Hai trường trung học ở Bồ Đào Nha; UCI [6] | Học sinh trung học [6] | Học sinh – môn học [6] | Điểm 0–20 [6] | Điểm của ba giai đoạn [6] |
| D. UCI 856 Higher Education Students Performance Evaluation | Một đợt thu thập năm 2019; UCI [7] | Sinh viên của hai khoa [7] | Bảng hỏi của từng sinh viên [7] | Điểm chữ [7] | Không có [7] |
| E. Dữ liệu bỏ học MOOC của XuetangX | Đại học Thanh Hoa, MOOCData [8], [9] | Người dùng MOOC ở Trung Quốc, 2015–2017 [8] | Người dùng – khóa học [8] | Bỏ học hoặc không bỏ học [8] | Hành động có dấu thời gian [8] |
| F. HarvardX Person-Course 2013 | HarvardX, Harvard Dataverse [10] | Người học của HarvardX, 2012–2013 [10] | Số liệu gộp theo người học – khóa học [10] | Được cấp chứng chỉ | Chỉ có mốc thời gian của sự kiện đầu tiên và sự kiện cuối cùng [10] |
| G. xAPI-Edu-Data | Dữ liệu của Kalboard 360, trang Kaggle của nhóm tác giả [11] | Học sinh ở nhiều quốc gia [11] | Học sinh [11] | Khoảng điểm [11] | Tài liệu không nêu |
