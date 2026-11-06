## 6.1. Yêu cầu dữ liệu theo từng câu hỏi

Ở Milestone 1, nhu cầu dữ liệu chỉ được nêu ở mức khái niệm và chưa có dữ liệu nào được xử lý [1]. Các nhu cầu này dựa trên bốn nguồn mà nhà trường đã có:
hệ thống quản lý đào tạo, LMS, danh sách điểm danh của các học phần kết hợp và lịch phân công cán bộ. LMS và hồ sơ đào tạo dùng chung một mã
sinh viên, nhưng không có cơ chế liên kết tự động nên các bản ghi phải được đối chiếu thủ công (DO1). Danh sách điểm danh do
giảng viên lưu giữ và cũng phải đối chiếu thủ công. Phụ lục IX mô tả nội dung của từng nguồn.

Một nguồn hiện chưa có: sổ theo dõi liên hệ đã định nghĩa ở Mục 3.3, là nguồn mà AQ4 và cả hai KPI phụ đều cần.

Bảng 6.1 liệt kê, cho từng câu hỏi, dữ liệu cần có, nguồn có thể dùng, mức chi tiết và khoảng thời gian, tình trạng sẵn có
và lưu ý về quyền riêng tư. Tình trạng sẵn có phản ánh lời kể của Cán bộ phụ trách công nghệ học tập và dữ liệu và vẫn là giả định
cho đến đợt rà soát dữ liệu ở Milestone 2.

**Bảng 6.1. Yêu cầu dữ liệu sơ bộ**

| AQ | Dữ liệu và biến cần có | Nguồn có thể dùng | Mức chi tiết và thời gian | Tình trạng sẵn có | Lưu ý về quyền riêng tư và đạo đức |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Đăng ký học phần, kết quả cuối kỳ, tình trạng học tập, học phần, hình thức học, năm theo học; hạn nộp và ngày nộp các bài được chấm điểm | Hệ thống quản lý đào tạo; LMS | Một dòng cho mỗi lượt đăng ký học phần trong mỗi học kỳ; năm học 2024–2025 và 2025–2026 | Đã có; dữ liệu tình trạng học tập có thể ghi chung tạm ngừng học và chuyển chương trình đào tạo với thôi học (DO3) | Chương trình đào tạo chỉ nhận số liệu theo nhóm, không kèm tên sinh viên |
| AQ2 | Dữ liệu của AQ1, thêm các bài bỏ lỡ và nộp trễ, hoạt động trên LMS so với mức trung bình của học phần, số bài bỏ lỡ ở các học phần khác và điểm danh ở học phần kết hợp, trong tuần 1–4 | LMS; danh sách điểm danh | Một dòng cho mỗi lượt đăng ký học phần trong mỗi tuần | Nằm ở các hệ thống riêng và phải đối chiếu thủ công (DO1) | Không dùng các loại dữ liệu cá nhân nhạy cảm như sức khỏe hoặc dân tộc |
| AQ3 | Dữ liệu của AQ2 ghi nhận đến hết tuần 2 và đến hết tuần 4; kết quả học phần cuối học kỳ | Như AQ2 | Một dòng cho mỗi lượt đăng ký học phần tại mỗi thời điểm chốt dữ liệu | Có sẵn, cập nhật trễ khoảng một tuần (DO4) | Chỉ cán bộ trực tiếp hành động mới được xem; không có quyết định tự động |
| AQ4 | Kết quả của AQ3; số sinh viên mỗi phòng liên hệ được mỗi tuần; sổ theo dõi liên hệ (ai liên hệ, khi nào, bằng cách nào, kết quả ra sao) | AQ3; lịch phân công cán bộ; một sổ theo dõi liên hệ dùng chung cần lập mới | Một dòng cho mỗi sinh viên tại mỗi đợt lập danh sách | Sổ theo dõi liên hệ chưa có (VCL4, VAD1) | Chỉ dùng để hỗ trợ sinh viên; không bao giờ thông báo cho gia đình hoặc nơi làm việc của sinh viên (VST2) |

Nếu hồ sơ của nhà trường không sử dụng được kịp thời, Milestone 2 có thể thử hướng tiếp cận này trên một bộ dữ liệu mở.
Open University Learning Analytics Dataset là một nguồn có thể dùng. Bộ dữ liệu này gồm 22 kỳ mở module và 32.593
bản ghi sinh viên của một trường đại học đào tạo từ xa ở Vương quốc Anh, kèm kết quả các bài đánh giá và số liệu gộp hằng ngày về
hoạt động của sinh viên trong môi trường học tập ảo [21]. Ngày của các bài đánh giá, bản ghi hoạt động, kết quả cuối kỳ và
ngày rút khỏi module trong bộ dữ liệu này có thể hỗ trợ AQ1–AQ3, trong khi phần phân luồng liên hệ của AQ4 và cả hai KPI phụ cần
sổ theo dõi liên hệ của chính nhà trường. Mức phù hợp của bộ dữ liệu này, cùng giới hạn khi chuyển kết quả từ bộ dữ liệu này sang một
trường đại học Việt Nam, sẽ được đánh giá ở Milestone 2.
