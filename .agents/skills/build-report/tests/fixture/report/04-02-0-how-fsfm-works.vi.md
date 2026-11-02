## 4.2. Cách FSFM hoạt động

FSFM hoạt động qua hai giai đoạn: một giai đoạn tiền huấn luyện dài để học từ khuôn mặt thật, và một giai đoạn thích ứng ngắn để biến kết quả đó thành các bộ phát hiện [102]. Hình 4.1 trình bày toàn bộ quy trình trong ba bước.

![Hình 4.1. FSFM trong ba bước: che một phần khuôn mặt thật, học với hai tín hiệu, tái sử dụng bộ mã hóa để phát hiện](assets/figures/task2-4-1-fsfm-at-a-glance.png){width=100%}

Ở bước thứ nhất, một khuôn mặt thật được chia thành các mảnh ảnh (patch) vuông nhỏ, và khoảng ba phần tư số mảnh bị che theo các vùng khuôn mặt mà một bộ phân vùng khuôn mặt xác định [102]. Ở bước thứ hai, một mạng nơ-ron gọi là bộ mã hóa chỉ nhìn thấy các mảnh còn lại và học đồng thời từ hai tín hiệu: nó phải dựng lại các điểm ảnh bị che, và cách nó nhìn khuôn mặt bị che một phần phải khớp với những gì một mạng thứ hai, mạng "thầy", nhìn thấy trên khuôn mặt đầy đủ [102]. Nhóm tác giả gọi ba đặc tính mà quá trình này rèn luyện là 3C: tính nhất quán trong từng vùng khuôn mặt (consistency), tính liên kết giữa các vùng (coherency) và sự tương ứng giữa chi tiết cục bộ với toàn bộ khuôn mặt (correspondence) [102].

Ở bước thứ ba, mọi thành phần trừ bộ mã hóa đều được gác lại. Bộ mã hóa, một ViT tiêu chuẩn, được gắn thêm một đầu ra nhỏ riêng cho từng nhiệm vụ và được tinh chỉnh trong thời gian ngắn cho mỗi nhiệm vụ phát hiện [102]. Nhóm tác giả kiểm thử mạng xương sống (backbone) duy nhất này trên 10 tập dữ liệu công khai [102].

Các Mục 4.2.1 đến 4.2.4 lần lượt đi theo các bước này: vì sao mô hình chỉ học từ khuôn mặt thật, cách thiết kế việc che, cách hai tín hiệu học vận hành, và cách một mạng xương sống trở thành ba bộ phát hiện.
