## Phụ lục IX – Chi tiết về nhóm kỹ thuật, nguồn dữ liệu, quy tắc về quyền riêng tư và cách phân loại quyết định

Phụ lục này giải thích lý do chọn từng nhóm kỹ thuật dự kiến ở Mục 5, mô tả các nguồn dữ liệu, rủi ro về chất lượng dữ liệu và các quy tắc về quyền riêng tư và đạo đức ở Mục 6, đồng thời nêu đầy đủ định nghĩa của ba cách phân loại quyết định dùng ở Mục 7.

### 1. Lựa chọn nhóm kỹ thuật

Câu hỏi mô tả và câu hỏi chẩn đoán dùng những nhóm kỹ thuật đơn giản nhất đủ để trả lời. AQ1 cần số lượng và tỷ lệ chia theo học phần, hình thức học và năm theo học, cùng với phép so sánh thời điểm giữa hai nhóm sinh viên. AQ2 so sánh tỷ lệ về sau không hoàn thành học phần giữa sinh viên có và sinh viên không có từng dấu hiệu. Hồi quy dùng để giải thích (explanatory regression) giúp nhóm xem một dấu hiệu còn tạo ra chênh lệch hay không khi đã tính đến các dấu hiệu khác, ví dụ bài bị bỏ lỡ có còn ý nghĩa ngoài mức hoạt động thấp trên LMS hay không. AQ2 báo cáo chênh lệch chứ không báo cáo nguyên nhân, vì hồ sơ hiện có là dữ liệu quan sát: hồ sơ cho biết sinh viên đã làm gì nhưng không cho biết vì sao. Bên cạnh đó, đề bài lưu ý không dùng ngôn ngữ nhân quả khi không có thiết kế nhân quả [1].

Câu hỏi dự báo được đánh giá so với một quy tắc đơn giản. Ở học phần kết hợp dành cho sinh viên năm nhất được mô tả trong Phụ lục V, kết quả đánh giá thường xuyên như bài kiểm tra ngắn và bài tập là yếu tố dự báo sớm mạnh nhất [8]. Vì vậy, một quy tắc chỉ đếm số bài bị bỏ lỡ đã là một mốc so sánh khó vượt qua. Một phương pháp phân loại chỉ đáng dùng khi phương pháp đó phát hiện được nhiều sinh viên về sau trượt hoặc rút học phần hơn quy tắc đơn giản, trên một danh sách có cùng độ dài. Phương pháp được đánh giá trên học kỳ sau (huấn luyện trên các học kỳ trước), đúng như cách phương pháp sẽ được dùng trong thực tế. Với học phần chưa có dữ liệu của các học kỳ trước, nhóm có thể dùng các phương pháp học từ chính các bài sinh viên đã nộp trong học phần đang diễn ra [20]. Phân tích sống sót, tức là phương pháp mô hình hóa thời gian cho đến khi một sự kiện như rút học phần xảy ra, là một lựa chọn dự kiến cho phần rút học phần của biến cần dự đoán.

Câu hỏi chỉ định biến thứ tự sắp xếp của AQ3 thành một danh sách mà cán bộ có thể dùng để hành động. Các quy tắc quyết định cắt thứ tự sắp xếp ở độ dài mà số sinh viên cán bộ liên hệ được mỗi tuần cho phép, áp dụng giới hạn về độ chính xác của danh sách và về tính công bằng, rồi phân luồng liên hệ từng sinh viên cho giảng viên, giảng viên kiêm cố vấn học tập hoặc Phòng Đào tạo. Phân tích giả định (what-if) cho thấy các giới hạn làm danh sách thay đổi ra sao, ví dụ một danh sách 40 tên phát hiện thêm được bao nhiêu sinh viên không hoàn thành học phần so với một danh sách 30 tên. Mỗi tên trong danh sách kèm lý do cụ thể dưới dạng một sự việc quan sát được, ví dụ bỏ lỡ hai bài kiểm tra ngắn kể từ tuần 2, vì cán bộ cho biết một điểm rủi ro không kèm lý do sẽ bị bỏ qua (VCL3, PM9).

### 2. Nguồn dữ liệu

Các nhu cầu dữ liệu ở Bảng 6.1 lấy từ bốn nguồn. Hệ thống quản lý đào tạo, do Phòng Đào tạo vận hành, lưu đăng ký học phần, kết quả cuối kỳ, tình trạng học tập (đang học, tạm ngừng học, chuyển chương trình đào tạo, thôi học) và năm theo học của từng sinh viên. LMS lưu các trang học phần, dữ liệu bài kiểm tra ngắn và bài tập kèm hạn nộp và ngày nộp, cùng nhật ký hoạt động cho biết mỗi sinh viên đã mở nội dung gì và vào lúc nào. Danh sách điểm danh các buổi học trên lớp chỉ có ở học phần kết hợp và do giảng viên lưu giữ. Lịch phân công cán bộ cho biết số sinh viên mà giảng viên kiêm cố vấn học tập và Phòng Đào tạo liên hệ được mỗi tuần. Theo Cán bộ phụ trách công nghệ học tập và dữ liệu, các nguồn này dùng chung mã sinh viên nhưng không được liên kết tự động, nên hồ sơ phải được đối chiếu thủ công (DO1).

**Rủi ro về chất lượng.** Năm rủi ro có thể khiến dữ liệu làm sai lệch kết quả phân tích; dự án có cách xử lý cho từng rủi ro. Thứ nhất, dữ liệu tình trạng
học tập có thể ghi chung tạm ngừng học có phép và chuyển chương trình đào tạo với thôi học thực sự (DO3, VPM2), nên số liệu của các năm dùng làm mức cơ sở được tính lại
theo các định nghĩa của Thông tư 83/2026 [4], đúng như Trưởng chương trình đào tạo đề nghị (VPM8). Thứ hai, cùng một chỉ số trên LMS mang ý nghĩa khác nhau ở các học phần
được thiết lập khác nhau (DO2), nên hoạt động chỉ được so sánh trong cùng học phần và dữ liệu về bài kiểm tra ngắn và bài tập là nguồn chính
(VDO1). Thứ ba, hoạt động không đồng nghĩa với việc học, vì sinh viên vẫn có thể đăng nhập đều đặn trong khi đang bị tụt lại (CL3, VST1) [22]. Do đó,
bài bỏ lỡ và bài nộp trễ là dấu hiệu chính; một cán bộ kiểm tra từng tên trong danh sách. Thứ tư, các bản ghi được đối chiếu thủ công với
độ trễ khoảng một tuần (DO1, DO4); các thời điểm chốt dữ liệu đã tính đến độ trễ này. Thứ năm, nhóm sinh viên nhỏ cho tỷ lệ không ổn định và có thể làm lộ danh tính
từng sinh viên, nên kết quả theo nhóm chỉ được báo cáo khi nhóm vượt mức tối thiểu đã thống nhất.

Bảng A.20 trình bày năm rủi ro về chất lượng dữ liệu và tính khả thi ở Mục 6.2, nơi mỗi rủi ro được nêu ra và cách dự án xử lý từng rủi ro.

**Bảng A.20. Rủi ro về chất lượng dữ liệu và tính khả thi**

| Rủi ro | Người nêu | Cách xử lý |
| :---- | :---- | :---- |
| Dữ liệu tình trạng học tập ghi chung tạm ngừng học có phép và chuyển chương trình đào tạo với thôi học thật sự, làm sai lệch biến kết quả | Cán bộ phụ trách công nghệ học tập và dữ liệu và Trưởng chương trình đào tạo (DO3, VPM2); Thông tư 83/2026 [4] | Tính lại số liệu của các năm dùng làm mức cơ sở theo định nghĩa của Thông tư 83/2026 (VPM8) |
| Cùng một chỉ số trên LMS mang ý nghĩa khác nhau ở các học phần được thiết lập khác nhau | Cán bộ phụ trách công nghệ học tập và dữ liệu (DO2) | So sánh hoạt động trong cùng học phần; chủ yếu dựa vào dữ liệu bài kiểm tra ngắn và bài tập (VDO1) |
| Hoạt động không đồng nghĩa với việc học: sinh viên có thể vẫn đăng nhập đều đặn trong khi đang bị tụt lại | Giảng viên và sinh viên (CL3, VST1); nghiên cứu đã công bố [22] | Lấy bài bị bỏ lỡ và bài nộp trễ làm dấu hiệu chính; cán bộ kiểm tra từng tên trong danh sách |
| Hồ sơ phải đối chiếu thủ công và chậm khoảng một tuần | Cán bộ phụ trách công nghệ học tập và dữ liệu (DO1, DO4) | Dữ liệu đến hết tuần 2 và tuần 4 dùng cho danh sách tuần 3 và tuần 5 (VDO3) |
| Nhóm sinh viên nhỏ có tỷ lệ không ổn định và có thể làm lộ danh tính từng sinh viên | Các phép so sánh giữa nhóm trong AQ2 và AQ3 | Chỉ báo cáo kết quả của những nhóm có số sinh viên vượt mức tối thiểu đã thống nhất |

### 3. Các quy tắc về quyền riêng tư và đạo đức

Các quy tắc về quyền riêng tư và đạo đức ở Mục 6.2, cùng nguồn của từng quy tắc, được trình bày dưới đây.

**Quyền riêng tư và đạo đức.** Quyền riêng tư và đạo đức đặt ra những giới hạn chặt chẽ cho dự án. Luật Bảo vệ dữ liệu cá nhân của Việt Nam,
có hiệu lực từ ngày 01/01/2026, gắn sự đồng ý với một mục đích được nêu rõ và không coi im lặng là đồng ý [18]. Bên cạnh đó, Bộ Giáo dục
và Đào tạo yêu cầu các trường đại học bảo vệ an toàn cơ sở dữ liệu giáo dục và báo cáo sự cố lộ lọt dữ liệu
trong vòng 72 giờ [23]. Các bộ quy tắc thực hành về phân tích dữ liệu học tập bổ sung những quy tắc mà dự án áp dụng. Cụ thể, mục đích,
dữ liệu, người được truy cập và cách sử dụng kết quả được giải thích cho cán bộ và sinh viên [11]. Sinh viên được thông báo ngay từ đầu
học phần và được hỏi ý kiến về cách sử dụng dữ liệu cá nhân [22]. Sự đồng ý được xin trước mọi biện pháp hỗ trợ dành riêng cho cá nhân [11].
Quyền truy cập chỉ dành cho cán bộ có nhu cầu công việc chính đáng [11]. Dữ liệu chỉ được lưu trong thời hạn đã thống nhất [22]. Kết quả không bao giờ được dùng để chấm điểm, lập hồ sơ (profiling) sinh viên hoặc đánh giá giảng viên [11].

Hai quy tắc nữa đến từ các cuộc phỏng vấn và từ các công trình đã công bố. Khi đã biết một sinh viên đang gặp
khó khăn, trường có nghĩa vụ hành động [22]. Cán bộ phụ trách công nghệ học tập và dữ liệu cũng cảnh báo rằng đánh dấu những sinh viên mà không ai có thời gian
liên hệ lại còn tệ hơn không biết (DO10); vì vậy, danh sách không bao giờ dài hơn số sinh viên cán bộ liên hệ được. Gia đình và nơi làm việc của
sinh viên không bao giờ được thông báo về một lần liên hệ, đúng như sinh viên đề nghị (VST2). Cuối cùng, dữ liệu thật của sinh viên
không được đưa vào các công cụ AI công cộng, theo yêu cầu của đề bài [1].

### 4. Cách phân loại quyết định

Đề bài yêu cầu ba cách phân loại [1], mỗi cách lấy từ một khung lý thuyết đã được thừa nhận. Cách thứ nhất là cấp quyết định. Gorry và Scott Morton [24] dựa trên ba cấp hoạt động quản lý của Anthony: hoạch định chiến lược quyết định mục tiêu của tổ chức và nguồn lực dùng để đạt mục tiêu đó; kiểm soát quản lý bảo đảm nguồn lực được sử dụng có hiệu lực và hiệu quả để hướng tới các mục tiêu này; kiểm soát tác nghiệp bảo đảm từng công việc cụ thể được thực hiện. Ba cấp này tương ứng với cấp chiến lược, cấp chiến thuật và cấp tác nghiệp trong đề bài. Cách thứ hai xét quyết định có theo quy trình có sẵn hay không (programmed / non-programmed). Gorry và Scott Morton cũng dựa trên Simon: theo Simon, một quyết định càng lặp lại và mang tính thường lệ, với một cách xử lý xác định đã được xây dựng sẵn, thì càng gần loại theo quy trình có sẵn; quyết định càng mới, thiếu cấu trúc và hệ trọng thì càng gần loại không theo quy trình có sẵn. Hai loại này là hai đầu của một thang liên tục chứ không phải hai nhóm tách bạch [24]. Cách thứ ba là khả năng đảo ngược. Bezos phân biệt quyết định khó đảo ngược (one-way door), là những quyết định hệ trọng, gần như không thể đảo ngược và phải được đưa ra chậm rãi, cân nhắc kỹ và tham khảo ý kiến rộng rãi, với quyết định đảo ngược được (two-way door), là những quyết định có thể đảo ngược nên có thể đưa ra nhanh [25].
