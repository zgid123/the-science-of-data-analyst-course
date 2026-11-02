### 2.1.2. Phát hiện sự sống dựa trên chuyển động và chớp mắt

Hướng phát hiện sự sống của Giai đoạn 1 còn bắt đầu sớm hơn phân tích kết cấu. Năm 2005, Kollreider và cộng sự đề xuất Optical Flow Lines, một phương pháp phát hiện khác biệt về chuyển động giữa ảnh chụp phẳng và khuôn mặt 3D thật [30]. Tín hiệu này mang tính hình học: "một ảnh chụp bị dịch chuyển tạo ra chuyển động như nhau trên mọi vùng khuôn mặt" [30], trong khi các bộ phận của một khuôn mặt thật chuyển động khác nhau. Năm 2009, Bao và cộng sự cũng dùng luồng quang học để phân biệt khuôn mặt 3D với tấn công bằng ảnh phẳng [30]. Các phương pháp luồng quang học tỏ ra nhạy cảm với môi trường xung quanh, vì chúng "không bền vững trước thay đổi của phông nền và ánh sáng" [30].

Chớp mắt cung cấp tín hiệu thứ hai mang tính sinh lý. Pan, Sun, Wu và Lao trình bày phương pháp chống giả mạo dựa trên chớp mắt bằng webcam thông thường tại Hội nghị Quốc tế về Thị giác máy tính của IEEE năm 2007 [51], và bài báo có 462 trích dẫn trên Crossref tính đến ngày 2/10/2026 [51]. Chớp mắt "thường diễn ra 15 đến 30 lần mỗi phút" [30], nên bất kỳ camera nào chạy từ 15 khung hình mỗi giây trở lên đều thu được hai khung hình trở lên cho mỗi lần chớp mắt, và người dùng không cần được hướng dẫn [30]. Do đó, phát hiện chớp mắt mặc định là thụ động và chỉ trở thành chủ động khi hệ thống yêu cầu người dùng chớp mắt, theo nghĩa của Mục 1.2.2.

Đến năm 2011, các tín hiệu này đã có bộ đánh giá chuẩn công khai. Anjos và Marcel công bố cơ sở dữ liệu Print-Attack cùng một biện pháp đối phó cơ sở tại Hội nghị Liên hợp Quốc tế về Sinh trắc học năm 2011, nơi nó phục vụ cuộc thi đầu tiên [47]. Phạm vi hoạt động của các tín hiệu sự sống cũng trở nên rõ ràng trong cùng giai đoạn: các phương pháp dựa trên chớp mắt "có thể phát hiện hiệu quả tấn công bằng ảnh in, nhưng không phát hiện được tấn công phát lại video hay ảnh khoét lỗ mắt" [30]. Bảng 2.2 tổng hợp các mốc của hướng phát hiện sự sống.

**Bảng 2.2. Trình tự thời gian các tín hiệu chuyển động và chớp mắt của Giai đoạn 1**

| Năm | Phương pháp | Tín hiệu | Phạm vi hoạt động |
| :---- | :---- | :---- | :---- |
| 2005 | Kollreider và cộng sự, Optical Flow Lines [30] | Chuyển động của ảnh phẳng so với khuôn mặt 3D [30] | Không bền vững trước thay đổi phông nền và ánh sáng [30] |
| 2007 | Pan và cộng sự, phát hiện chớp mắt [51] | Chớp mắt tự nhiên, 15 đến 30 lần mỗi phút [30] | Phát hiện ảnh in; không phát hiện video phát lại hay ảnh khoét lỗ mắt [30] |
| 2009 | Bao và cộng sự, luồng quang học [30] | Chuyển động phẳng so với chuyển động 3D [30] | Không bền vững trước thay đổi phông nền và ánh sáng [30] |
| 2011 | Anjos và Marcel, mốc cơ sở Print-Attack [47] | Bộ đánh giá chuẩn và mốc cơ sở cho tấn công bằng ảnh in [47] | Tấn công bằng ảnh in [47] |

Vì tín hiệu chớp mắt không ngăn được tấn công phát lại video [30], các tập dữ liệu có tấn công phát lại được mô tả trong Mục 2.1.3 đã đưa sự chú ý quay trở lại các tín hiệu kết cấu và chất lượng ảnh.
