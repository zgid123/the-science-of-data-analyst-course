### 4.2.3. Hai tín hiệu học

Bộ mã hóa được cải thiện nhờ hai tín hiệu phối hợp với nhau, tín hiệu này bù đắp điểm hạn chế của tín hiệu kia [102].

Tín hiệu thứ nhất là tái tạo. Một bộ giải mã nhỏ nhận đầu ra của bộ mã hóa và dự đoán điểm ảnh của từng mảnh bị che, và sai số của dự đoán đó là hàm mất mát thứ nhất; một hàm mất mát thứ hai, nhỏ hơn, kiểm tra riêng vùng bị che kín [102]. Đây là thiết kế của bộ tự mã hóa có che (MAE), ở đây được dẫn dắt bởi cách che có xét đến khuôn mặt của Mục 4.2.2 [102]. Tín hiệu này dạy chi tiết cục bộ tinh và cách các vùng lân cận khớp với nhau.

Tín hiệu thứ hai là đối khớp. Một mạng "thầy" nhìn cùng khuôn mặt đó mà không bị che, và bản tóm tắt của bộ mã hóa về khuôn mặt bị che một phần phải hướng cùng chiều với bản tóm tắt của mạng thầy về khuôn mặt đầy đủ [102]. Mạng thầy không được huấn luyện trực tiếp; nó chậm rãi đi theo bộ mã hóa dưới dạng trung bình trượt của các trọng số, nhờ đó các mục tiêu của nó luôn ổn định [102]. Tín hiệu này dạy mối liên kết giữa các bộ phận cục bộ và khuôn mặt như một tổng thể.

Mục tiêu huấn luyện cộng ba thành phần với các trọng số cố định [102]:

$$L = L_1 + 0.007 \cdot L_2 + 0.1 \cdot L_3$$

Trong đó $L_1$ là sai số tái tạo trên toàn bộ các mảnh bị che, $L_2$ là sai số tái tạo của vùng bị che kín, và $L_3$ là mức bất đồng giữa bộ mã hóa và mạng thầy; nhóm tác giả chọn cả hai trọng số bằng thực nghiệm [102]. Vì vậy, một bước huấn luyện có thể được đọc như sau:

```text
for each batch of real face images:
    regions  = face_parser(image)                      # mắt, mũi, miệng, ...
    visible, hidden, covered = crfr_p_mask(image, regions, ratio=0.75)
    features = encoder(visible)                        # bộ mã hóa chỉ thấy khoảng 25% khuôn mặt
    L1 = rebuild_error(decoder(features), hidden)      # mọi mảnh bị che
    L2 = rebuild_error(decoder(features), covered)     # vùng bị che kín
    L3 = disagreement(features, teacher(image))        # mạng thầy thấy toàn bộ khuôn mặt
    update encoder and decoder to reduce L1 + 0.007*L2 + 0.1*L3
    teacher = running_average(teacher, encoder)        # mạng thầy đi theo một cách chậm rãi
```

Hình 4.3, tái hiện từ bài báo, cho thấy kết quả mà hai tín hiệu đạt được. Với những khuôn mặt bị che 75% số mảnh, mô hình huấn luyện bằng cả hai tín hiệu dựng lại khuôn mặt với kết cấu tinh hơn trong từng vùng và quan hệ giữa các vùng nhất quán hơn so với các mô hình chỉ huấn luyện bằng tái tạo [102].

![Hình 4.3. Khuôn mặt được dựng lại từ 75% mảnh bị che: (a) MAE với cách che ngẫu nhiên, (b) với cách che CRFR-P, (c) FSFM. Tái hiện từ Wang và cộng sự [102]](assets/figures/task2-4-3-paper-reconstructions.png){width=80%}
