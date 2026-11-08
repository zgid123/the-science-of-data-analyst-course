import sys, pathlib
base = pathlib.Path(sys.argv[1])
E = [
("04-00-evaluation-design.vi.md",
 "Chỉ số thứ nhất là diện tích dưới đường cong đặc trưng hoạt động của bộ thu (ROC), gọi tắt là ROC-AUC. Chỉ số thứ hai là diện tích dưới đường cong độ chính xác–tỷ lệ phát hiện, gọi tắt là PR-AUC.",
 "Chỉ số thứ nhất dựa trên đường cong đặc trưng hoạt động của bộ thu (ROC): đó là diện tích dưới đường cong ROC (ROC-AUC). Chỉ số thứ hai là diện tích dưới đường cong độ chính xác–tỷ lệ phát hiện (PR-AUC)."),
("04-01-evaluation-cards.vi.md",
 "ở Mục 4.4 đạt, hoặc mọi nhóm",
 "ở Mục 4.4 đạt hoặc mọi nhóm"),
]
for f,a,b in E:
    p=base/f; t=p.read_text()
    if t.count(a)!=1: sys.exit(f"ABORT {f}")
for f,a,b in E:
    p=base/f; p.write_text(p.read_text().replace(a,b)); print("ok",f)
