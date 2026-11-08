## 6.3. Chiến lược chia dữ liệu và kiểm soát rò rỉ thông tin

Rò rỉ thông tin là việc dùng thông tin về biến mục tiêu mà tại thời điểm dự báo chưa thể có; hiện tượng này làm hiệu
năng ước lượng được cao hơn thực tế [10], [11]. Bảng 6.2 gắn mỗi rủi ro mà đề bài nêu với một biện pháp kiểm soát và một
phép kiểm tra.

**Bảng 6.2. Các rủi ro rò rỉ thông tin và biện pháp kiểm soát**

| Rủi ro (đề bài) | Trường hợp trong OULAD | Biện pháp kiểm soát | Kiểm tra |
| :---- | :---- | :---- | :---- |
| Rò rỉ biến mục tiêu (target leakage) | Kết quả cuối cùng, ngày rút, các sự kiện về sau, điểm TMA | Chỉ dùng sự kiện tính đến hết thời điểm chốt dữ liệu; điểm CMA chỉ dùng sau 7 ngày kể từ ngày nộp | V11, V13, V14 |
| Lẫn dữ liệu giữa tập huấn luyện và tập kiểm thử | Trung vị, tham số chuẩn hóa thang đo và danh sách nhóm giá trị của biến phân loại được ước lượng (fit) trên mọi kỳ mở | Chỉ ước lượng trên các kỳ mở năm 2013 | V12 |
| Rò rỉ theo sinh viên (student leakage) | 1.962 lượt đăng ký học trong tập kiểm thử thuộc về sinh viên đã có mặt trong năm 2013 | Đánh dấu; các fold (phần chia trong kiểm định chéo) giữ mỗi sinh viên ở cùng một phía của phép chia | V15 |
| Rò rỉ theo thời gian (temporal leakage) | Chia ngẫu nhiên qua các năm | Huấn luyện trên năm 2013 (9 kỳ mở), kiểm thử trên năm 2014 (13 kỳ mở) | V15 |
| Rò rỉ do tăng cường dữ liệu (augmentation leakage) | Không có | Không tăng cường dữ liệu | – |

Cách chia dữ liệu theo thời gian dựa trên thực tiễn của OU: xây dựng mô hình nhận diện sinh viên có nguy cơ trên các
kỳ mở trước của một module rồi áp dụng cho kỳ mở đang diễn ra [12]. Cách chia này cũng áp dụng nguyên tắc dữ liệu
phụ thuộc thời gian phải được đánh giá trên các quan sát tương lai [13]. Một số phép biến đổi cần học tham số từ dữ liệu, ví dụ điền giá trị thiếu
và chuẩn hóa thang đo; các tham số này chỉ được ước lượng (fit) trên các kỳ mở huấn luyện [11]. Để kiểm tra điều đó,
nhóm tác giả cố ý thay đổi giá trị của mọi dòng kiểm thử rồi ước lượng lại các phép biến đổi: các tham số vẫn giữ nguyên,
chứng tỏ tập kiểm thử không ảnh hưởng đến chúng. Các fold phải giữ mỗi sinh viên ở cùng một phía [13]. Do đó, bước tinh
chỉnh siêu tham số ở Milestone 4 dùng các fold loại trừ từng kỳ mở (leave-one-run-out) trong năm 2013: mỗi fold để riêng
một kỳ mở làm phần đánh giá, đồng thời các fold được nhóm theo sinh viên, nên một sinh viên học hai kỳ mở năm 2013
vẫn chỉ nằm trong một fold. Ngoài ra, kết quả kiểm thử còn được báo
cáo riêng cho 4 kỳ mở không có kỳ mở tương ứng trong năm 2013 và cho tập kiểm thử đã bỏ 89 lượt đăng ký học tại
ngày 13 có kết quả Withdrawn nhưng không có ngày rút.
