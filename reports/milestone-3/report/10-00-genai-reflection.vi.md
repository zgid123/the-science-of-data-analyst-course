# 10. Sử dụng AI tạo sinh và phản tư của nhóm

**Vai trò.** Trí tuệ nhân tạo (AI) tạo sinh hỗ trợ milestone này ở cả bảy vai trò mà đề bài cho phép; đúng như đề bài yêu
cầu, mọi phát hiện về dữ liệu đều được xác nhận bằng mã, số liệu thống kê, tài liệu hoặc kiểm tra trực tiếp trên bộ dữ
liệu [1]. AI không bao giờ được xem là nguồn dữ liệu: không câu trả lời nào của AI được dùng làm bằng chứng rằng một bộ
dữ liệu có bao nhiêu bản ghi, rằng sinh viên có xu hướng hành xử theo một cách nào đó hoặc rằng biến này gây ra biến kia
[1]. Trong mỗi lượt rà soát, tức một vòng soạn thảo rồi phản biện, một tác tử AI (agent, là hệ thống AI được giao một nhiệm vụ riêng) soạn sản phẩm và một tác tử AI khác phản biện sản phẩm đó; thành viên
nhóm kiểm chứng các quyết định. Bảy vai trò, kèm tên tiếng Anh trong đề bài, là: (1) AI diễn giải từ điển dữ liệu (data
dictionary interpreter); (2) AI hỗ trợ phân tích khám phá dữ liệu (EDA) và lập danh mục kiểm tra chất lượng (EDA and quality
checklist partner); (3) trợ lý viết mã (code assistant); (4) AI phản biện quy trình chuẩn bị (preparation critic); (5) AI gợi ý xây
dựng đặc trưng (feature engineering ideator); (6) trợ lý viết tài liệu (documentation assistant); và (7) trợ lý tạo dữ liệu giả lập
(synthetic-data assistant). Phụ lục V mô tả AI đã làm gì trong từng vai trò và kết quả được kiểm chứng ra sao. Bảng 10.1
nêu các mục chính của Nhật ký quyết định về AI (AI Decision Log) theo mẫu của đề bài: đề xuất của AI, quyết định của nhóm,
đề xuất được chấp nhận hay bị từ chối, bằng chứng dùng để kiểm chứng và tác động đến quy trình chuẩn bị dữ liệu
(pipeline) [1].

**Bảng 10.1. Nhật ký quyết định về AI, các mục chính**

| Đề xuất của AI | Quyết định của nhóm | Chấp nhận / Từ chối | Bằng chứng dùng để kiểm chứng | Tác động đến pipeline |
| :---- | :---- | :---- | :---- | :---- |
| Điểm CMA được công bố trong vòng 7 ngày và CMA không thể nộp trễ (chính sách năm 2025 của OU) | Dùng độ trễ 7 ngày cho điểm CMA; không áp dụng quy định cấm nộp trễ cho giai đoạn 2013–2014 | Chấp nhận một phần | 32.991 trên 69.956 bài nộp CMA sau ngày đến hạn | Điểm CMA chỉ lấy từ các bài nộp sớm hơn thời điểm chốt dữ liệu ít nhất 7 ngày; số bài nộp trễ được đếm theo loại bài |
| Kiểm tra xem các dòng lượt nhấp trùng lặp hoàn toàn có phải là bản sao hay không | So sánh với mức ngẫu nhiên trên các cặp dòng cùng sinh viên, cùng tài nguyên và cùng ngày | Chấp nhận | 31,5% số cặp có số lượt nhấp bằng nhau, so với 24,0% nếu chỉ do ngẫu nhiên | Giữ mọi dòng; dựng phiên bản đã bỏ dòng trùng |
| Giới hạn 50% cho độ chính xác của danh sách nằm gần tỷ lệ nền; nên đo lift và tỷ lệ phát hiện so với mức tối đa có thể đạt | Phát biểu lại giới hạn của AQ4 (C13) | Chấp nhận | Tỷ lệ không hoàn thành là 45,3% và 44,2% tại hai thời điểm chốt dữ liệu | Bảng độ dài danh sách; chất lượng danh sách đo bằng lift và tỷ lệ phát hiện |
| Việc nộp trễ CMA, vốn chưa rõ ý nghĩa, chi phối quy tắc dấu hiệu sớm | Quy tắc dùng việc nộp trễ TMA; giữ một biến thể có tính nộp trễ CMA | Chấp nhận | 47,2% số bài nộp CMA bị trễ, so với 16,8% số bài nộp TMA | early_sign_rule và early_sign_rule_cma (C10) |
| Báo cáo tỷ lệ kết quả của các lượt đăng ký học trong tập kiểm thử thuộc sinh viên đã có mặt năm 2013, trước khi lập mô hình | Hiện chỉ báo cáo số lượng các lượt này | Chấp nhận một phần | Nguyên tắc: xem kết quả của tập kiểm thử trong lúc chuẩn bị dữ liệu sẽ làm mất tính độc lập của phép đánh giá trên tập kiểm thử | 1.962 lượt được đánh dấu; kết quả để lại cho Milestone 4 |
| Các bài đến hạn trước ngày đăng ký bị tính là bỏ lỡ; phép kiểm tra rò rỉ thông tin không thể báo lỗi (FAIL), kể cả khi có rò rỉ | Sửa công thức và phép kiểm tra | Chấp nhận | 6 bài bị tính nhầm là bỏ lỡ tại ngày 27; kiểm tra bằng cách đọc mã nguồn | Chỉ tính bỏ lỡ khi bài đến hạn vào hoặc sau ngày đăng ký; V13 có thể báo lỗi (FAIL) |

**Các đề xuất được chấp nhận và bị từ chối.** AI phản biện quy trình chuẩn bị nêu 12 nhận xét; nhóm tác giả chấp nhận 9 nhận xét
và chấp nhận một phần 3 nhận xét, không nhận xét nào bị từ chối. Bên cạnh đó, AI kiểm tra rò rỉ thông tin (leakage auditor) nêu 8 phát hiện, đều được chấp nhận. Tác tử này là một phần của vai trò AI phản biện quy trình chuẩn bị và
không tìm thấy trường hợp nào dùng dữ liệu có ngày sau thời điểm chốt dữ liệu. Các lượt rà soát định hình bốn quy tắc mà pipeline áp dụng. Thứ nhất, danh sách của AQ4 được đánh giá theo mức vượt so với một danh sách chọn ngẫu nhiên (lift), vì giới hạn 50% cho độ chính xác của danh sách nằm sát tỷ lệ nền (C13). Thứ hai, việc nộp trễ CMA, gặp ở 47,2% số bài nộp CMA so với 16,8% số bài nộp TMA, không được đưa vào
quy tắc dấu hiệu sớm (C10). Thứ ba, một bài chỉ bị tính là bỏ lỡ khi đến hạn vào hoặc sau ngày đăng ký của sinh viên; AI
kiểm tra rò rỉ thông tin đã chỉ ra sáu bài tại ngày 27 có ngày đến hạn trước ngày sinh viên đăng ký. Thứ tư, phép kiểm tra
rò rỉ thông tin được xây dựng sao cho có thể báo lỗi (FAIL), đúng như AI kiểm tra rò rỉ thông tin yêu cầu.

Trong 12 nhận xét của AI phản biện quy trình chuẩn bị, nhận xét thứ tư (Phụ lục V) chỉ được chấp nhận một phần, vì nhóm tác giả luôn giữ nguyên tắc không xem kết quả của tập kiểm thử trong lúc chuẩn bị dữ liệu. Nhận xét này đề nghị báo cáo tỷ lệ kết quả của các lượt đăng ký học trong
tập kiểm thử thuộc sinh viên đã có mặt năm 2013 trước khi lập mô hình. Nhóm tác giả báo cáo số lượng các lượt này (1.962) nhưng không báo cáo kết quả, vì nếu xem kết quả, tập kiểm thử sẽ tham gia vào bước chuẩn bị, điều mà đề bài không cho phép [1].

Phụ lục V trình bày Nhật ký quyết định về AI với đủ mười ba mục, các prompt, mọi quyết định về các nhận xét và phát hiện,
và phần tự đánh giá những điểm mà các lượt rà soát giúp ích nhiều nhất.
