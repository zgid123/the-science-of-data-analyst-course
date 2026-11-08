## 4.2. Quyết định xử lý khoảng trống dữ liệu và dữ liệu giả lập

Đề bài phân biệt giá trị thiếu với biến không được thu thập. Giá trị thiếu xuất hiện khi biến có tồn tại nhưng một số bản ghi không có giá trị; biến không được thu thập là biến mà bộ dữ liệu chưa từng ghi nhận, nên không được điền giá trị thiếu hoặc sinh dữ liệu cho biến đó như thể đó là dữ liệu thật [1]. Bảng 4.2 xếp các khoảng trống của OULAD vào những loại này, cùng với trường hợp không có bản ghi: dữ liệu không có dòng nào vì sự việc không xảy ra, nên giá trị được tính là 0.

**Bảng 4.2. Giá trị thiếu, trường hợp không có bản ghi và biến không được thu thập**

| Loại | Trường hợp trong OULAD | Cách xử lý |
| :---- | :---- | :---- |
| Giá trị thiếu | imd_band, ngày đăng ký, điểm TMA, ngày rút khỏi module của 93 lượt đăng ký học có kết quả Withdrawn | Nhóm riêng hoặc biến chỉ báo; không điền giá trị thiếu trong các bảng dữ liệu đã chuẩn bị |
| Không có bản ghi (tính là 0) | Không có dòng lượt nhấp hoặc dòng bài nộp; ngày hủy đăng ký để trống | Số đếm bằng 0 (không có hoạt động hoặc không nộp bài); ngày trống nghĩa là sinh viên không rút khỏi module |
| Biến không được thu thập | Năm theo học, hình thức học, điểm danh, tạm ngừng học, lượt liên hệ, số lượt liên hệ tối đa mỗi tuần, ngày công bố điểm | Không điền giá trị thiếu, không mô phỏng; thu hẹp hoặc hoãn AQ |
| Thiếu biến mục tiêu | Không có | Có sẵn biến mục tiêu cho học có giám sát |

Không bộ dữ liệu mở nào bù được các biến không được thu thập, vì không bộ nào trong bảy bộ dữ liệu ứng viên của Milestone 2 ghi nhận lượt liên hệ, điểm danh hoặc năm theo học. Do đó, theo thứ tự ưu tiên mà đề bài quy định, các AQ được thu hẹp và phần đánh giá việc liên hệ sinh viên của AQ4 được hoãn lại [1]. Bản ghi giả lập duy nhất là một số lượt đăng ký học kiểm thử có gắn nhãn trong thư mục `tests/` của Gói dữ liệu đã chuẩn bị, dùng để kiểm tra công thức tính đặc trưng; đây là dữ liệu kiểm thử quy trình chuẩn bị dữ liệu (pipeline) mà đề bài cho phép [1]. Các bản ghi này không bao giờ đi vào bảng dữ liệu đã chuẩn bị nào.
