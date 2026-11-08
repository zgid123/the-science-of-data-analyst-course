FILE = "10-01-candidate-comparison.vi.md"
PAIRS = [
# flag 84
("| Như ứng viên 1, nhưng coi hiệu ứng của mỗi module là giá trị lấy từ phân phối chung của các module |",
 "| Như ứng viên 1, nhưng coi các module là một mẫu lấy từ một tổng thể module lớn hơn, nên hiệu ứng của từng module được ước lượng như một hiệu ứng ngẫu nhiên |"),
# flag 85
("| Nhiều dòng dữ liệu, nhưng các nhánh chia thay đổi giữa các mẫu |",
 "| Nhiều dòng dữ liệu, nhưng cách cây chia nhánh thay đổi giữa các mẫu |"),
("| Không có giả định tham số; các nhánh chia không ổn định |",
 "| Không có giả định tham số; cách chia nhánh không ổn định |"),
# flag 86
("dữ liệu có đủ mọi kỳ mở của các module này, nên hiệu ứng cố định phù hợp với thiết kế [12] |",
 "dữ liệu có đủ mọi kỳ mở của các module này, tức các kỳ mở được quan sát đầy đủ chứ không phải được lấy mẫu, nên hiệu ứng cố định phù hợp với thiết kế [12] |"),
# flag 87 (established term kept, defined in place)
("| Kiểm duyệt không mang thông tin (non-informative censoring); cần mô hình rủi ro cạnh tranh hoặc một mô hình riêng cho Fail |",
 "| Kiểm duyệt không mang thông tin (non-informative censoring): khi một sinh viên bị kiểm duyệt (censored), tức thời điểm rút khỏi module không được quan sát vì việc theo dõi đã dừng, lý do dừng theo dõi được giả định không liên quan đến nguy cơ rút khỏi module; cần mô hình rủi ro cạnh tranh hoặc một mô hình riêng cho Fail |"),
# flag 88
("rủi ro về bảo trì và về sự phụ thuộc chằng chịt giữa các thành phần (entanglement) [10] |",
 "rủi ro về bảo trì và về sự phụ thuộc lẫn nhau giữa các thành phần của hệ thống (entanglement) [10] |"),
# proxy → biến đại diện (first use in the file)
("| Kiểm tra công bằng; kiểm tra biến thay thế |",
 "| Kiểm tra công bằng; kiểm tra biến đại diện (proxy check) |"),
# flag 89 (the comparison with the primary model made explicit)
("Mô hình chỉ dùng đặc điểm cá nhân cho biết bao nhiêu phần của thứ hạng đến từ mức tham gia học tập, chứ không phải từ module và lịch sử học tập.",
 "Khi so với mô hình chính, mô hình chỉ dùng đặc điểm cá nhân (không có dữ liệu hoạt động) cho biết bao nhiêu phần của thứ hạng đến từ mức tham gia học tập, chứ không phải từ module và lịch sử học tập."),
# flag 90
("| Can thiệp được phân bổ ngẫu nhiên hoặc không bị gây nhiễu [9] |",
 "| Cần dữ liệu về can thiệp được phân bổ ngẫu nhiên hoặc không bị yếu tố gây nhiễu làm sai lệch [9] |"),
]
