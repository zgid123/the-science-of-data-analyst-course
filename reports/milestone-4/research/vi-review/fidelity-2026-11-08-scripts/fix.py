import sys, pathlib
base = pathlib.Path(sys.argv[1])
E = [
("01-01-goal-decisions-aqs.vi.md",
 "Quyết định D2 xác định cách Trưởng chương trình đào tạo phân bổ thời gian của phòng hỗ trợ sinh viên và của giảng viên kiêm cố vấn học tập trong mỗi học kỳ.",
 "Quyết định D2 xác định Trưởng chương trình đào tạo dành thời gian của phòng hỗ trợ sinh viên và của giảng viên kiêm cố vấn học tập cho những việc nào trong mỗi học kỳ."),
("01-01-goal-decisions-aqs.vi.md",
 "và theo năm học của sinh viên, thay bằng",
 "và theo năm theo học của sinh viên, thay bằng"),
("01-01-goal-decisions-aqs.vi.md",
 "so danh sách với tỷ lệ nền của kỳ mở, là tỷ lệ sinh viên",
 "so danh sách với tỷ lệ nền của kỳ mở, tức tỷ lệ sinh viên"),
("01-02-prepared-data-entry-gate.vi.md",
 "sau khi mô hình AQ3 đã qua lần kiểm tra duy nhất trên tập kiểm thử.",
 "sau lần kiểm tra duy nhất của mô hình AQ3 trên tập kiểm thử."),
("03-02-descriptive-diagnostic.vi.md",
 "sau khi mô hình AQ3 đã qua lần kiểm tra trên tập kiểm thử (C14)",
 "sau lần kiểm tra duy nhất của mô hình AQ3 trên tập kiểm thử (C14)"),
("08-00-traceability.vi.md",
 "sau khi mô hình AQ3 đã qua lần kiểm tra trên tập kiểm thử,",
 "sau lần kiểm tra duy nhất của mô hình AQ3 trên tập kiểm thử,"),
("03-02-descriptive-diagnostic.vi.md",
 "Mô hình cũng đáp ứng các tiêu chí còn lại trong tám tiêu chí của Mục 3.1.",
 "Các tiêu chí còn lại trong tám tiêu chí của Mục 3.1 được xét như sau."),
("04-00-evaluation-design.vi.md",
 "Chỉ số thứ nhất được tính trên đường cong đặc trưng hoạt động của bộ thu (ROC), là diện tích dưới đường cong ROC (ROC-AUC). Chỉ số thứ hai được tính trên đường cong độ chính xác–tỷ lệ phát hiện, là diện tích dưới đường cong độ chính xác–tỷ lệ phát hiện (PR-AUC).",
 "Chỉ số thứ nhất là diện tích dưới đường cong đặc trưng hoạt động của bộ thu (ROC), gọi tắt là ROC-AUC. Chỉ số thứ hai là diện tích dưới đường cong độ chính xác–tỷ lệ phát hiện, gọi tắt là PR-AUC."),
("04-01-evaluation-cards.vi.md",
 "tỷ lệ phát hiện chỉ tính trên những sinh viên không hoàn thành mà cán bộ còn kịp liên hệ, tức sinh viên",
 "tỷ lệ phát hiện chỉ tính trên những sinh viên không hoàn thành còn liên hệ được, tức sinh viên"),
("04-01-evaluation-cards.vi.md",
 "kiểm định khẳng định về công bằng ở Mục 4.4 phải đạt; nếu kiểm định này nêu tên nhóm nào, nhóm đó phải được xem xét trước khi đưa danh sách vào sử dụng;",
 "kiểm định khẳng định về công bằng ở Mục 4.4 đạt, hoặc mọi nhóm mà kiểm định này nêu tên đều được xem xét lại trước khi đưa danh sách vào sử dụng;"),
("05-02-causal-fairness-use.vi.md",
 "Quy định này bảo đảm sinh viên bị đánh dấu có cơ hội chứng minh dự báo là sai [45], đồng thời nhãn gắn cho sinh viên không làm thiên lệch cách cán bộ nhìn nhận sinh viên đó [46].",
 "Quy định này nhằm để sinh viên bị đánh dấu có cơ hội chứng minh dự báo là sai [45] và để nhãn gắn cho sinh viên không làm thiên lệch cách cán bộ nhìn nhận sinh viên đó [46]."),
]
for f,a,b in E:
    p=base/f; t=p.read_text(); n=t.count(a)
    if n!=1: sys.exit(f"ABORT {f}: {n} matches for {a[:60]}")
for f,a,b in E:
    p=base/f; p.write_text(p.read_text().replace(a,b)); print("ok",f)
