### 1.3.2. Tín hiệu chuyển động và sinh lý

Nếu các phương pháp kết cấu kiểm tra một bề mặt, thì các phương pháp phát hiện sự sống tìm kiếm dấu hiệu sự sống theo thời gian. Các tín hiệu sự sống được dùng phổ biến nhất là chuyển động, như cử động đầu và biểu cảm khuôn mặt, và những thay đổi cường độ rất nhỏ do mạch máu gây ra [30]. Các tín hiệu động đã được khai thác cho PAD gồm chớp mắt, cử động đầu, theo dõi ánh nhìn và tín hiệu sinh lý thu từ xa [35].

Tín hiệu chuyển động xuất hiện trước. Pan và cộng sự mô hình hóa việc chớp mắt bằng trường ngẫu nhiên có điều kiện với đầu vào là chuỗi ảnh theo thời gian [30], nhờ đó một lần chớp mắt hiện ra như một chuỗi trạng thái của mắt mà ảnh chụp không thể tạo ra. Các phương pháp luồng quang học phát hiện sự khác biệt về kiểu chuyển động giữa ảnh chụp phẳng và khuôn mặt ba chiều thật [30].

Mạch máu cung cấp một tín hiệu mà ngay cả bản sao hoàn hảo về ngoại hình khuôn mặt cũng không có. Đo quang thể tích từ xa (rPPG) khôi phục những thay đổi cường độ trên da do mạch đập từ một video thông thường [30]. Cách tiếp cận của Li và cộng sự, trình bày tại Hội nghị Quốc tế về Nhận dạng mẫu năm 2016, dựa trên thực tế rằng "tín hiệu mạch tồn tại trên khuôn mặt người sống thật nhưng không có trên bất kỳ vật liệu mặt nạ hay ảnh in nào" [39]. Phương pháp xây dựng tín hiệu từ nửa dưới khuôn mặt, được phát hiện như một vùng quan tâm trong từng khung hình [30]. Liu và cộng sự mở rộng ý tưởng này năm 2016 bằng cách trích xuất tín hiệu rPPG từ nhiều vùng khuôn mặt thay vì chỉ nửa dưới, và năm 2018 bằng cách kết hợp ước lượng giả rPPG được học với tín hiệu hình học 3D [30]. Nhờ đó, rPPG trở thành một tín hiệu sự sống nội tại, đặc biệt trước tấn công bằng mặt nạ 3D [40], và phát hiện được tấn công bằng ảnh cũng như cả mặt nạ 3D chất lượng cao [30].

Mỗi tín hiệu cũng có phạm vi hoạt động rõ ràng. rPPG nhìn chung không phát hiện được tấn công phát lại video [30], vì cử động đầu và tín hiệu rPPG dễ bị một video phát lại bắt chước [35]. Tín hiệu sinh lý thường được thu từ các video tương tác dài, điều này bất tiện khi triển khai thực tế [35]. Các phương pháp rPPG trước đây chống mặt nạ cần 10 đến 12 giây quan sát, và phương pháp TSrPPG, trình bày tại Hội nghị Mùa đông về Ứng dụng Thị giác máy tính năm 2020, rút ngắn thời gian quan sát xuống dưới một giây mà vẫn giữ được hiệu năng [40]. Bảng 1.8 tổng hợp các tín hiệu chuyển động và sinh lý.

**Bảng 1.8. Tín hiệu chuyển động và sinh lý**

| Tín hiệu | Phát hiện điều gì | Công trình tiêu biểu | Phạm vi hoạt động |
| :---- | :---- | :---- | :---- |
| Chớp mắt | Chuỗi trạng thái mắt mở và nhắm [30] | Pan và cộng sự, trường ngẫu nhiên có điều kiện [30] | Cần đầu vào video [35] |
| Luồng quang học | Chuyển động phẳng của ảnh chụp so với chuyển động 3D của khuôn mặt [30] | Nhóm phương pháp trong công trình tổng quan [30] | Bị video phát lại bắt chước [35] |
| Mạch rPPG | Có mạch trên da, không có trên mặt nạ và ảnh in [39] | Li và cộng sự 2016; Liu và cộng sự 2016 và 2018 [39], [30] | Phát hiện ảnh và mặt nạ 3D, không phát hiện video phát lại [30]; thời gian quan sát rút xuống dưới một giây [40] |
