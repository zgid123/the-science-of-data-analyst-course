## 6.1. Các phát hiện về chất lượng dữ liệu

Ở Milestone 3, nhóm chúng em chuyển kết quả khảo sát dữ liệu thành Nhật ký vấn đề chất lượng dữ liệu (Data Quality
Issue Log) gồm mười chín vấn đề, mỗi vấn đề được xếp mức độ nghiêm trọng theo tác động đến các câu hỏi: Cao khi bỏ qua
vấn đề sẽ làm thay đổi một tỷ lệ, biến mục tiêu hoặc một đặc trưng; Trung bình khi vấn đề làm một đại lượng đo thay đổi
và mức thay đổi đó tính được; Thấp trong các trường hợp còn lại. Bảng 6.2 trình bày nhật ký này cùng quyết định xử lý từng vấn
đề; Bảng A.15 (Phụ lục VI) bổ sung bằng chứng. Mỗi vấn đề mức Cao đều làm thay đổi phương pháp. Thứ nhất, kết quả bài
thi bị thiếu ở 5 module, nên bài được chấm điểm chỉ gồm TMA và CMA (DQ08). Thứ hai, không kỳ mở nào năm 2013 có bài đến
hạn tính đến hết ngày 13 và chỉ 7 trong 9 kỳ mở có bài đến hạn tính đến hết ngày 27, nên quy tắc dấu hiệu sớm có thêm
phần hoạt động (DQ18). Thứ ba, phạm vi dữ liệu hẹp giới hạn mọi khẳng định (DQ19). Ngoài ra, hai vấn đề mức Trung bình
có thể làm thay đổi kết luận, với mức thay đổi tính được. Nếu tính cả CMA nộp trễ, tỷ lệ sinh viên bị quy tắc dấu hiệu sớm
đánh dấu tại ngày 27 sẽ tăng từ 28,8% lên 41,2%; vì vậy, quy tắc chỉ xét TMA nộp trễ, còn CMA nộp trễ được đưa vào một
phép kiểm tra độ nhạy (DQ10). Bên cạnh đó, các dòng lượt nhấp trùng lặp chiếm 7,39% số dòng của bảng lượt nhấp, nhưng nếu gộp các dòng này thì chỉ mất 3,19% tổng số lượt nhấp; chúng em kiểm tra ảnh hưởng này bằng một phiên bản đã bỏ dòng trùng của mỗi đặc trưng dựa trên lượt nhấp (DQ01). Các phát hiện trên dẫn đến
các thay đổi từ C09 đến C13 trong Nhật ký thay đổi (Bảng A.8); không thay đổi nào ảnh hưởng đến Business Goal (mục tiêu của tổ chức) hay các quyết định. Trong bảng dưới đây, ngày được đếm từ ngày bắt đầu kỳ mở (ngày 0). Kết quả bảo lưu là
kết quả của một bài được chấm điểm mà sinh viên chuyển từ một kỳ mở trước của module; OULAD ghi các kết quả này vào
ngày −1, tức đã có từ trước khi kỳ mở bắt đầu, nên chúng không được dùng để xác định thời điểm nộp bài.

**Bảng 6.2. Nhật ký vấn đề chất lượng dữ liệu**

| Mã | Vấn đề | Mức độ nghiêm trọng | Quyết định |
| :---- | :---- | :---- | :---- |
| DQ01, DQ02 | Dòng lượt nhấp trùng lặp (7,39% số dòng); nhiều dòng cho cùng một ngày | Trung bình | Giữ các dòng; cộng theo ngày; thêm phiên bản đã bỏ dòng trùng |
| DQ03 | Hoạt động sau ngày hủy đăng ký | Trung bình | Cắt dữ liệu tại ngày hủy đăng ký |
| DQ04–DQ06 | Tình trạng không khớp giữa các bảng; 58 lượt đăng ký muộn; sinh viên rời khỏi module sớm | Thấp | Gắn cờ; quy tắc xác định phạm vi dữ liệu (C09) |
| DQ07 | Kết quả bảo lưu ghi ngày −1 | Trung bình | Không dùng để xác định thời điểm |
| DQ08 | 18 trong 24 bài thi không có dòng kết quả | Cao | Bài được chấm điểm chỉ gồm TMA và CMA |
| DQ09, DQ10 | Trọng số khác nhau giữa các module; CMA và TMA nộp trễ | Trung bình | Không dùng trọng số cho bài; quy tắc chỉ xét TMA nộp trễ |
| DQ11–DQ14 | Thiếu điểm, mức khó khăn của khu vực, ngày đăng ký, tuần theo kế hoạch | Thấp–Trung bình | Nhóm "Thiếu" hoặc biến chỉ báo; không điền giá trị ước tính |
| DQ15–DQ17 | Hai ngày hệ thống không ghi lượt nhấp; giá trị ngoại lai; lượt đăng ký học không có hoạt động | Thấp–Trung bình | Lần lượt: coi hai ngày đó là thiếu, không phải 0; giữ nguyên giá trị ngoại lai; dùng phép nối trái (left join) |
| DQ18 | Ít bài đến hạn tính đến hết các thời điểm chốt dữ liệu | Cao | Quy tắc có thêm phần hoạt động (C10) |
| DQ19 | Bảy module ở UK trong năm 2013–2014 | Cao | Nêu rõ phạm vi; so sánh trong cùng module |
