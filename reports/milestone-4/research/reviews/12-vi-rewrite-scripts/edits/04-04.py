FILE = "04-04-error-fairness.vi.md"
PAIRS = [
# flag 63
("Kiểm tra này vẫn cần thiết, vì bỏ các thuộc tính này khỏi mô hình không làm mô hình mất khả năng nhận ra các thuộc tính đó: mức hoạt động, số lần học trước hoặc số tín chỉ có thể mang cùng thông tin [35].",
 "Kiểm tra này vẫn cần thiết, vì khi không có các thuộc tính này, mô hình vẫn có thể gián tiếp nhận ra chúng: mức hoạt động, số lần học trước hoặc số tín chỉ có thể mang cùng thông tin [35]."),
# flag 64
("mâu thuẫn với nhau, trừ các trường hợp suy biến [37].",
 "mâu thuẫn với nhau, trừ các trường hợp suy biến (mô hình dự báo hoàn hảo hoặc các nhóm có cùng tỷ lệ nền) [37]."),
# flags 65, 66
("Ngưỡng 400 lượt và mốc 100 sinh viên không hoàn thành dựa trên cùng một phép tính. Với khoảng 100 sinh viên không hoàn thành trong một nhóm và tỷ lệ phát hiện ở mức khoảng 0,5, sai số chuẩn của tỷ lệ phát hiện của nhóm là khoảng 5 điểm phần trăm. Số sinh viên còn lại lớn hơn nhóm nhiều lần, nên sai số chuẩn này là nguồn bất định chính của chênh lệch. Do đó, chênh lệch 10 điểm trong quy tắc FR1 tương đương khoảng hai lần sai số chuẩn của tỷ lệ phát hiện ở nhóm. Ngoài ra, với tỷ lệ thấp nhất là 28%, 400 lượt đăng ký học cho khoảng 112 sinh viên không hoàn thành.",
 "Hai con số này (ngưỡng 400 lượt đăng ký học và mốc 100 sinh viên không hoàn thành) được rút ra từ cùng một phép tính, gồm hai bước. Bước thứ nhất: khi một nhóm có khoảng 100 sinh viên không hoàn thành và tỷ lệ phát hiện ở mức khoảng 0,5, sai số chuẩn của tỷ lệ phát hiện của nhóm là khoảng 5 điểm phần trăm. Các sinh viên còn lại đông hơn nhóm nhiều lần, nên tỷ lệ phát hiện của họ có sai số chuẩn nhỏ hơn nhiều; vì vậy, sai số chuẩn 5 điểm của nhóm là nguồn bất định chính của chênh lệch giữa nhóm và các sinh viên còn lại. Do đó, chênh lệch 10 điểm trong quy tắc FR1 tương đương khoảng hai lần sai số chuẩn của tỷ lệ phát hiện ở nhóm. Bước thứ hai: với tỷ lệ không hoàn thành thấp nhất là 28%, nhóm có 400 lượt đăng ký học sẽ có khoảng 112 sinh viên không hoàn thành (400 × 28%), tức vượt mốc 100."),
# flag 67
("đều tái tạo và khuếch đại nhẹ chênh lệch theo hướng có lợi cho sinh viên nam, đồng thời thiên lệch đối với sinh viên tự khai có khuyết tật biến động thất thường (theo báo cáo của nhóm tác giả nghiên cứu đó) [38].",
 "đều tái tạo và khuếch đại nhẹ chênh lệch theo hướng có lợi cho sinh viên nam. Ngoài ra, mức thiên lệch của các mô hình này đối với nhóm có tình trạng khuyết tật do sinh viên tự khai thay đổi thất thường (theo báo cáo của nhóm tác giả nghiên cứu đó) [38]."),
# flag 50 wording (flag a group → đánh dấu)
("Quy tắc FR1 (Bảng 4.5) nêu tên một nhóm để xem xét lại chứ không loại mô hình, vì khi một nhóm được nêu tên, con người cần đánh giá nguyên nhân của chênh lệch.",
 "Quy tắc FR1 (Bảng 4.5) đánh dấu một nhóm để xem xét lại chứ không loại mô hình, vì khi một nhóm bị đánh dấu, con người cần đánh giá nguyên nhân của chênh lệch."),
# proxy → biến đại diện
("Phép kiểm tra biến thay thế (proxy check)", "Phép kiểm tra biến đại diện (proxy check)"),
# flag 68
("chênh lệch không phụ thuộc ngưỡng; kiểm tra biến thay thế;",
 "chênh lệch về khả năng phân biệt không phụ thuộc ngưỡng (ABROCA); kiểm tra biến đại diện;"),
]
