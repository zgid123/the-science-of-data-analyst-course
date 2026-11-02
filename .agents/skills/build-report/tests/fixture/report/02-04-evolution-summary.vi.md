## 2.4. Tổng hợp quá trình phát triển kỹ thuật

Ba giai đoạn tạo thành một mạch phát triển liên tục, trong đó mỗi giai đoạn kế thừa bài toán còn bỏ ngỏ của giai đoạn trước. Bảng 2.10 tổng hợp chúng theo thời kỳ, cách tiếp cận, phương pháp tiêu biểu, khả năng tổng quát hóa và trọng tâm về mối đe dọa.

**Bảng 2.10. Ba giai đoạn của PAD khuôn mặt**

| Khía cạnh | Giai đoạn 1: tín hiệu thủ công | Giai đoạn 2: bộ phân loại sâu với giám sát phụ trợ | Giai đoạn 3: tổng quát hóa và tấn công chèn dữ liệu |
| :---- | :---- | :---- | :---- |
| Thời kỳ chủ đạo | Khoảng 2005–2017; phương pháp sâu từ 2014 [30], [49] | Khoảng 2018–2020 [45], [57] | Khoảng 2020–2026 [44], [66], [67] |
| Cách tiếp cận | Đặc trưng kết cấu, chất lượng ảnh, chuyển động và chớp mắt thủ công với bộ phân loại truyền thống [45], [30] | Mạng sâu được giám sát bằng độ sâu và rPPG; CDC và tìm kiếm kiến trúc [45], [57] | Tổng quát hóa miền; ViT thị giác – ngôn ngữ tiền huấn luyện [44], [42], [66] |
| Phương pháp tiêu biểu | Optical Flow Lines (2005), chớp mắt (2007), LBP (2011), kết cấu màu (2016) [30], [51], [37] | Giám sát phụ trợ (2018), CDCN++ (2020) [45], [57] | MADDG (2019), SSDG (2020), FLIP (2023) [44], [42], [66] |
| Tập dữ liệu điển hình | NUAA, CASIA-FASD, Replay-Attack, MSU-MFSD; 15–50 đối tượng [35], [54] | OULU-NPU, SiW, SiW-M, CASIA-SURF, CeFA; tới 1.607 đối tượng [43], [45], [56], [58], [59] | Giao thức loại trừ từng tập O/C/I/M trên bốn tập dữ liệu [44], [42] |
| Khả năng tổng quát hóa | HTER kiểm thử chéo gần 50% với chuyển động, LBP và LBP-TOP; 30,3–37,7% với kết cấu màu [45] | ACER dưới 5% trong cùng tập dữ liệu, HTER trên 20% khi kiểm thử chéo với phần lớn mô hình [35]; ACER 12,7–23,6% với tấn công chưa từng gặp [57], [56] | HTER trung bình trên O/C/I/M từ 23,09% (2019) xuống 3,01% (2023) [44], [66] |
| Trọng tâm mối đe dọa | Ảnh in và phát lại tại cảm biến [35] | Tấn công trình diện đa dạng hơn, kể cả mặt nạ 3D; 13 kiểu tấn công trong SiW-M [56] | DIA và deepfake trong xác minh danh tính từ xa [67], [10] |

Hai mạch tiến bộ xuyên suốt bảng này. Khả năng tổng quát hóa được cải thiện đều đặn, từ những bộ phát hiện thất bại ngoài tập dữ liệu của chính chúng đến những mô hình có sai số trung bình khoảng 3% trên các tập dữ liệu chưa từng gặp [66]. Đồng thời, mối đe dọa đã vượt ra ngoài camera, khiến PAD giờ đây hoạt động song song với phát hiện tấn công chèn dữ liệu [68]. Phần 3 theo dõi mạch song song của tiêu chuẩn, chứng nhận và pháp luật đã biến các kết quả kỹ thuật này thành yêu cầu, và Phần 4 phân tích một mô hình nền tảng được thiết kế để bảo vệ khuôn mặt một cách hợp nhất trước cả tấn công trình diện lẫn tấn công số.
