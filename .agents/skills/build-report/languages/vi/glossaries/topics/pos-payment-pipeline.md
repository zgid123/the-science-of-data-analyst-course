# Topic glossary: card payments at the point of sale and a fault-tolerant pipeline

The vocabulary of one report, on the POS card-payment pipeline: its title, the six categories and eighteen concerns of its difficulties, the root-cause families and the 47 solution components, and the zones, flows, design principles and cases of the integrated pipeline. General card-payment, legal and engineering terms (authorisation, clearing, settlement, reversal, hold, merchant, idempotency …) come from the domain and common layers; this file fixes only the names the report gives itself, so every file renders each label the same way. Component names keep their code wherever the English places it ("đảo giao dịch có bảo đảm (P04)").

## Title and parts

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| Card Payments at the Point of Sale: Difficulties and a Fault-Tolerant Processing Pipeline | Thanh toán thẻ tại điểm bán: các khó khăn và pipeline xử lý chịu lỗi | Report title, sentence case; the title page sets it in capitals | đường ống xử lý chịu lỗi, đường ống xử lý có khả năng chịu lỗi |
| Card Payments at the Point of Sale (short title) | Thanh toán thẻ tại điểm bán | Running header and slide footer | Thanh toán bằng thẻ tại điểm bán hàng |
| Difficulties the System Must Handle (part title) | Những khó khăn hệ thống cần xử lý | Part title | |
| Solution Components (part title) | Các thành phần giải pháp | Part title | |
| The Integrated Fault-Tolerant Pipeline (part title) | Pipeline chịu lỗi tích hợp | Part title; "pipeline tích hợp" in running text | đường ống tích hợp |
| difficulty / priority difficulty | khó khăn / khó khăn ưu tiên | "144 khó khăn", "13 khó khăn ưu tiên" | độ khó |
| solution component / component (P01–P47) | thành phần giải pháp / thành phần | "47 thành phần, đánh số từ P01 đến P47" | |

## Categories and concerns (part title)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| category (C1–C6) / nested categories | hạng mục / các hạng mục lồng nhau | "sáu hạng mục lồng nhau, từ chung đến riêng"; "hạng mục C4" | phạm trù khó khăn, danh mục khó khăn |
| C1 Common system difficulty / common system category | C1 Khó khăn chung của hệ thống / hạng mục hệ thống chung | Heading form first, then "hạng mục hệ thống chung (C1)" | khó khăn hệ thống thông thường |
| C2 Common banking system difficulty / common banking category | C2 Khó khăn chung của hệ thống ngân hàng / hạng mục ngân hàng chung | "hạng mục ngân hàng chung (C2)" | khó khăn hệ thống ngân hàng thông thường |
| C3 Payment transaction difficulty / payment transaction category | C3 Khó khăn của giao dịch thanh toán / hạng mục giao dịch thanh toán | "hạng mục giao dịch thanh toán (C3)" | |
| C4 Payment by credit card / credit-card payment | C4 Thanh toán bằng thẻ tín dụng / thanh toán bằng thẻ tín dụng | "hạng mục thẻ tín dụng (C4)" | thanh toán thẻ-tín-dụng |
| C5 Payment on a POS terminal / POS payment | C5 Thanh toán qua máy POS / thanh toán qua máy POS | "hạng mục máy POS (C5)" | thanh toán trên thiết bị đầu cuối POS |
| C6 Credit card on a POS terminal / card-present payment | C6 Thẻ tín dụng tại máy POS / thanh toán có thẻ hiện diện | First use "thanh toán có thẻ hiện diện (card-present)", then "hạng mục thẻ hiện diện (C6)" | thẻ có mặt |
| concern / concern group | khía cạnh / nhóm khía cạnh | "mười tám khía cạnh"; "nhóm khía cạnh mà khó khăn đe dọa" | mối quan tâm, mối lo ngại |
| functional (business) concern / non-functional (technical) concern | khía cạnh chức năng (nghiệp vụ) / khía cạnh phi chức năng (kỹ thuật) | Table headers; "mười khía cạnh nghiệp vụ (A1–A10) và tám khía cạnh kỹ thuật (B1–B8)" | |
| A1 Transaction processing and payment lifecycle | A1 Xử lý giao dịch và vòng đời thanh toán | | |
| A2 Authorisation and card validation | A2 Cấp phép và kiểm tra tính hợp lệ của thẻ | | |
| A3 Clearing, settlement and fund transfers | A3 Bù trừ, quyết toán và chuyển tiền | | |
| A4 Transaction reconciliation | A4 Đối soát giao dịch | | |
| A5 Refunds, reversals and chargebacks | A5 Hoàn tiền, đảo giao dịch và bồi hoàn | | |
| A6 Transaction fees and financial calculations | A6 Phí giao dịch và tính toán tài chính | | |
| A7 Invoice and statement generation | A7 Lập hóa đơn và sao kê | | |
| A8 Customer and merchant account management | A8 Quản lý tài khoản khách hàng và đơn vị chấp nhận thẻ | | |
| A9 Transaction reporting and audit trails | A9 Báo cáo giao dịch và dấu vết kiểm toán | | |
| A10 Exception handling and dispute resolution | A10 Xử lý ngoại lệ và giải quyết tra soát | | |
| B1 Availability and reliability | B1 Tính sẵn sàng và độ tin cậy | | |
| B2 Performance and scalability | B2 Hiệu năng và khả năng mở rộng | | |
| B3 Data consistency and integrity | B3 Tính nhất quán và toàn vẹn dữ liệu | | |
| B4 Security and fraud prevention | B4 An toàn, bảo mật và phòng chống gian lận | | |
| B5 Privacy and regulatory compliance | B5 Quyền riêng tư và tuân thủ quy định | | |
| B6 Fault tolerance and disaster recovery | B6 Khả năng chịu lỗi và khôi phục sau thảm họa | | |
| B7 Interoperability and integration | B7 Khả năng tương tác và tích hợp | | |
| B8 Monitoring, logging and traceability | B8 Giám sát, ghi nhật ký và khả năng truy vết | | |
| trigger and consequence | điều kiện phát sinh và hệ quả | Table column header: "Điều kiện phát sinh và hệ quả" | kích hoạt và hậu quả, tác nhân kích hoạt và hệ quả |

## Root-cause families (part title)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| root-cause family | nhóm nguyên nhân gốc | "15 nhóm nguyên nhân gốc"; "nhóm truyền nhận không chắc chắn (F1)" | họ nguyên nhân gốc, gia đình nguyên nhân gốc, họ căn nguyên |
| F1 Uncertain delivery | F1 Truyền nhận không chắc chắn | "nhóm truyền nhận không chắc chắn (F1)"; Section heading "Truyền nhận không chắc chắn" | giao nhận không chắc chắn, giao hàng không chắc chắn |
| F2 Changing amounts and states | F2 Số tiền và trạng thái thay đổi | Section heading | số lượng và trạng thái thay đổi |
| F3 Operating while degraded | F3 Vận hành ở chế độ suy giảm | Section heading | hoạt động trong khi xuống cấp |
| F4 Exact money | F4 Tính chính xác của số tiền | | |
| F5 Time and business dates | F5 Thời gian và ngày nghiệp vụ | | |
| Exact money and business time (section title) | Số tiền chính xác và thời gian nghiệp vụ | Section heading, covering F4 and F5 | |
| F6 Several versions of the truth | F6 Nhiều phiên bản số liệu giữa các bên | "mỗi bên giữ phiên bản số liệu của riêng mình" | nhiều phiên bản của sự thật, nhiều phiên bản sự thật |
| Capture, settlement and reconciliation (section title) | Ghi nhận, quyết toán và đối soát | Section heading, covering F6 | |
| F7 Prices, rates and charges | F7 Giá, tỷ giá và các khoản phí | Section heading | |
| F8 Periodic documents | F8 Chứng từ định kỳ | Section heading; sao kê, hóa đơn và báo cáo quyết toán gửi theo kỳ | tài liệu định kỳ, văn bản định kỳ |
| F9 Disputes and exceptions | F9 Tra soát và ngoại lệ | Section heading | |
| F10 Fraud and abuse | F10 Gian lận và lạm dụng | | |
| Layered fraud defence (section title) | Phòng chống gian lận nhiều lớp | Section heading and Figure | phòng thủ gian lận phân lớp |
| F11 Protected data and accountable records | F11 Dữ liệu được bảo vệ và hồ sơ có thể giải trình | | hồ sơ có trách nhiệm |
| Data protection and records (section title) | Bảo vệ dữ liệu và lưu trữ hồ sơ | Section heading, covering F11 | |
| F12 Load and infrastructure failure | F12 Tải cao và sự cố hạ tầng | Section heading | lỗi tải và hạ tầng |
| F13 Change and integration | F13 Thay đổi và tích hợp | | |
| F14 Visibility | F14 Khả năng nhận biết sự cố | "nhóm nhận biết sự cố (F14)": phát hiện sự cố trước khi khách hàng nhận ra | tính hiển thị, khả năng hiển thị |
| F15 Changing parties | F15 Các bên thay đổi trạng thái | "nhóm các bên thay đổi trạng thái (F15)" | các bên đang thay đổi |
| Change, visibility and party lifecycle (section title) | Thay đổi, khả năng nhận biết sự cố và vòng đời các bên | Section heading, covering F13–F15 | |
| handles / design / tolerance / limit (component fields) | phạm vi xử lý / thiết kế / khả năng chịu lỗi / giới hạn | Italic field names of each component: "*phạm vi xử lý*, *thiết kế*, *khả năng chịu lỗi* và *giới hạn*" | khả năng dung sai |

## Components P01–P47 (part title)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| P01 Transaction identity | P01 Định danh giao dịch | "định danh giao dịch (P01)" | danh tính giao dịch |
| P02 Idempotent receivers | P02 Bộ tiếp nhận lũy đẳng | First use "bộ tiếp nhận lũy đẳng (idempotent receiver)" | người nhận lũy đẳng, máy thu lũy đẳng |
| P03 Timeout budget along the chain | P03 Quỹ thời gian chờ dọc chuỗi xử lý | Short "quỹ thời gian chờ (P03)"; first use "quỹ thời gian chờ (timeout budget)" | ngân sách thời gian chờ, ngân sách hết giờ |
| P04 Guaranteed reversal | P04 Đảo giao dịch có bảo đảm | "đảo giao dịch có bảo đảm (P04)" | đảo ngược được đảm bảo, đảo ngược đảm bảo, hoàn tác đảm bảo |
| P05 Transactional outbox and ordered event stream | P05 Outbox giao dịch và luồng sự kiện có thứ tự | First use "outbox giao dịch (transactional outbox)"; short "outbox giao dịch (P05)" | hộp thư đi giao dịch |
| P06 Cash-register link and electronic receipt | P06 Kết nối máy tính tiền và biên lai điện tử | Short "kết nối máy tính tiền (P06)" | liên kết quầy thu ngân, liên kết máy đếm tiền |
| P07 Transaction state machine with amount invariants | P07 Máy trạng thái giao dịch với ràng buộc bất biến về số tiền | Short "máy trạng thái giao dịch (P07)" | bất biến số lượng |
| P08 Hold and credit-limit service (issuer) | P08 Dịch vụ giữ tiền và hạn mức tín dụng (phía tổ chức phát hành thẻ) | Short "dịch vụ giữ tiền và hạn mức tín dụng (P08)" | |
| P09 Refund controls | P09 Kiểm soát hoàn tiền | | |
| P10 Offline acceptance policy and store-and-forward | P10 Chính sách chấp nhận ngoại tuyến và lưu rồi chuyển tiếp | First use "lưu rồi chuyển tiếp (store-and-forward)"; short "chính sách chấp nhận ngoại tuyến (P10)" | lưu trữ và chuyển tiếp ngoại tuyến |
| P11 Circuit breakers and stand-in processing | P11 Bộ ngắt mạch và xử lý thay thế | First use "bộ ngắt mạch (circuit breaker)"; short "bộ ngắt mạch và xử lý thay thế (P11)" until STIP is defined (section title), then "bộ ngắt mạch và STIP (P11)", since "xử lý thay thế" is the full form of STIP | cầu dao ngắt mạch, xử lý đứng thay |
| P12 Dependency failure policy | P12 Chính sách ứng phó sự cố của thành phần phụ thuộc | Short "chính sách ứng phó sự cố phụ thuộc (P12)" | chính sách thất bại phụ thuộc |
| P13 Payment HSM cluster | P13 Cụm HSM thanh toán | | |
| P14 Double-entry, append-only ledger | P14 Sổ cái bút toán kép, chỉ ghi thêm | Short "sổ cái bút toán kép (P14)" | sổ cái nhập kép, sổ cái chỉ nối thêm |
| P15 Read-consistency rules | P15 Quy tắc nhất quán khi đọc | | luật nhất quán đọc |
| P16 Time and business-calendar service | P16 Dịch vụ thời gian và lịch nghiệp vụ | | dịch vụ lịch kinh doanh |
| P17 Batch capture and totals check | P17 Ghi nhận lô giao dịch và kiểm tra số tổng | Short "ghi nhận lô giao dịch (P17)" | bắt giữ lô |
| P18 Clearing and settlement engine | P18 Bộ máy bù trừ và quyết toán | | động cơ bù trừ, động cơ thanh toán |
| P19 Reconciliation chain | P19 Chuỗi đối soát | | chuỗi hòa giải |
| P20 Merchant aggregation, funding and reserves | P20 Tổng hợp, chi trả và ký quỹ dự phòng cho đơn vị chấp nhận thẻ | Short "chi trả cho đơn vị chấp nhận thẻ (P20)" for "merchant funding" | cấp vốn cho người bán, tài trợ người bán |
| P21 Versioned pricing and fee engine | P21 Bộ máy định giá và tính phí có phiên bản | Short "bộ máy định giá và tính phí (P21)" | động cơ định giá |
| P22 Exchange rates and DCC | P22 Tỷ giá và DCC | DCC is defined earlier in the report ("chuyển đổi ngoại tệ động (DCC)"), so the name keeps the abbreviation, as in English | chuyển đổi tiền tệ động |
| P23 Cardholder interest, fees and repayments | P23 Lãi, phí và thanh toán dư nợ của chủ thẻ | | |
| P24 Idempotent cycle scheduler | P24 Bộ lập lịch chu kỳ lũy đẳng | Short "bộ lập lịch chu kỳ (P24)" | |
| P25 Snapshot and tie-out | P25 Snapshot và đối chiếu cân số | Same tie-out form as the domain glossary ("đối chiếu cân số (tie-out)") | buộc chặt số liệu, đối chiếu khớp số |
| P26 Document versioning and merchant invoices | P26 Quản lý phiên bản chứng từ và hóa đơn cho đơn vị chấp nhận thẻ | Short "quản lý phiên bản chứng từ (P26)" | |
| P27 Delivery outbox | P27 Outbox gửi chứng từ | | hộp thư đi giao nhận |
| P28 E-invoice gateway | P28 Cổng hóa đơn điện tử | | |
| P29 Dispute and chargeback case management | P29 Quản lý hồ sơ tra soát và bồi hoàn | Short "quản lý hồ sơ tra soát (P29)" for "dispute case management" | quản lý trường hợp tranh chấp |
| P30 Complaint handling | P30 Xử lý khiếu nại | | |
| P31 Exception workbench | P31 Bàn xử lý ngoại lệ | "bàn xử lý ngoại lệ (P31)": hàng đợi ngoại lệ tập trung có người phụ trách | bàn làm việc ngoại lệ, bàn thợ ngoại lệ |
| P32 Secure terminal and key management | P32 Máy POS an toàn và quản lý khóa | Short "máy POS an toàn (P32)" | thiết bị đầu cuối bảo mật |
| P33 EMV acceptance policy and real-time risk scoring | P33 Chính sách chấp nhận EMV và chấm điểm rủi ro thời gian thực | The architecture table splits it into "phía máy POS" and "phía hệ thống chủ (host)" | |
| P34 Merchant risk monitoring | P34 Giám sát rủi ro đơn vị chấp nhận thẻ | | giám sát rủi ro người bán |
| P35 AML and sanctions screening | P35 Sàng lọc AML và cấm vận | AML is defined earlier in the report ("phòng, chống rửa tiền (AML)"), so the name keeps the abbreviation, as in English; "sàng lọc AML và cấm vận (P35)" | sàng lọc chống rửa tiền và trừng phạt, sàng lọc AML và danh sách cấm vận |
| P36 Tokenisation and cardholder-data environment | P36 Token hóa và môi trường dữ liệu chủ thẻ | First use "token hóa (tokenisation)", "môi trường dữ liệu chủ thẻ (CDE)" | mã thông báo hóa |
| P37 Data governance | P37 Quản trị dữ liệu | | |
| P38 Reporting store and audit log | P38 Kho dữ liệu báo cáo và nhật ký kiểm toán | | cửa hàng báo cáo |
| P39 Capacity and load management | P39 Quản lý năng lực xử lý và tải | | quản lý dung lượng và tải |
| P40 Fault isolation | P40 Cô lập lỗi | | |
| P41 Multi-site operation and recovery | P41 Vận hành đa trung tâm và khôi phục | Short "vận hành đa trung tâm (P41)"; "site" in this report is "trung tâm dữ liệu" | vận hành đa trang web, vận hành đa site |
| P42 Security baseline | P42 Chuẩn bảo mật tối thiểu | | đường cơ sở bảo mật, đường cơ sở an ninh |
| P43 Gateway and canonical message model | P43 Cổng kết nối và mô hình thông điệp chuẩn hóa | | mô hình thông điệp kinh điển |
| P44 Release and vendor management | P44 Quản lý bản phát hành và nhà cung cấp | | quản lý phát hành và nhà bán |
| P45 Terminal fleet management | P45 Quản lý tập trung máy POS | | quản lý đội thiết bị đầu cuối, quản lý hạm đội |
| P46 Observability | P46 Khả năng quan sát hệ thống | First use "khả năng quan sát (observability)" | tính quan sát được |
| P47 Customer, merchant and card lifecycle | P47 Vòng đời khách hàng, đơn vị chấp nhận thẻ và thẻ | | |

## Architecture, principles and flows (part title)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| zone / five zones | vùng / năm vùng | "năm vùng của pipeline"; keep "phân vùng" for data partitions | |
| time scale (of a zone) | thang thời gian | Table column "Thang thời gian" | |
| Edge: cash register, terminal and fleet | Vùng biên: máy tính tiền, máy POS và quản lý thiết bị | Short "vùng biên" | |
| Real-time core: acquirer and issuer | Lõi thời gian thực: tổ chức thanh toán thẻ và tổ chức phát hành thẻ | Short "lõi thời gian thực" | |
| Money core | Lõi quản lý tiền | | lõi tiền tệ |
| Post-transaction: capture, settlement, reconciliation, pricing, documents | Vùng hậu giao dịch: ghi nhận, quyết toán, đối soát, định giá, chứng từ | Short "vùng hậu giao dịch" | |
| Cases and control | Vùng xử lý hồ sơ và kiểm soát | | các trường hợp và kiểm soát |
| platform / platform band | tầng nền tảng / dải nền tảng | Table row "Tầng nền tảng, nằm dưới mọi vùng"; "dải nền tảng" when describing Figure | băng nền tảng |
| Exactly-once outcome from at-least-once delivery | Kết quả đúng một lần trên nền truyền nhận ít nhất một lần | Principle (1); first use with "(exactly-once)" and "(at-least-once)" | |
| Nested timeouts | Thời gian chờ lồng nhau | Principle (2) | hết giờ lồng nhau |
| Record before acting | Ghi nhận trước khi thực hiện | Principle (3) | ghi lại trước khi hành động |
| Money moves forward only | Tiền chỉ ghi tiến, không sửa ngược | Principle (4): corrections are new balanced entries | tiền chỉ di chuyển về phía trước |
| Every truth is checked against another | Mọi số liệu đều được đối chiếu với một nguồn khác | Principle (5) | mọi sự thật được kiểm tra |
| Degrade within explicit limits | Suy giảm trong giới hạn được xác định rõ | Principle (6) | xuống cấp trong giới hạn |
| Prove it under failure | Kiểm chứng trong điều kiện sự cố | Principle (7) | chứng minh nó khi thất bại |
| One writer per account and per site | Mỗi tài khoản và mỗi trung tâm chỉ có một bên ghi | Principle (8) | một người viết |
| Defence in layers | Phòng vệ nhiều lớp | Principle (9) | phòng thủ theo lớp |
| flow / Flow 1 … Flow 6 | luồng / Luồng 1 … Luồng 6 | "sáu luồng của pipeline" | |
| Flow 1: card-present purchase online | Luồng 1: giao dịch mua có thẻ hiện diện ở chế độ trực tuyến | Section heading "Giao dịch mua có thẻ hiện diện ở chế độ trực tuyến" | |
| Flow 2: purchase while degraded | Luồng 2: giao dịch mua ở chế độ suy giảm | Section heading; Figure "các quyết định ở chế độ suy giảm và kết quả trong giới hạn" | mua hàng khi xuống cấp |
| Flow 3: from end of day to merchant funds | Luồng 3: từ cuối ngày đến khi đơn vị chấp nhận thẻ nhận tiền | Section heading "End of Day, Settlement and Reconciliation" → "Cuối ngày, quyết toán và đối soát" | |
| Flow 4: reconciliation | Luồng 4: đối soát | | |
| Flow 5: billing cycle and document streams | Luồng 5: chu kỳ sao kê và các luồng chứng từ | Section heading "Billing Cycle, Documents and Exceptions" → "Chu kỳ sao kê, chứng từ và ngoại lệ" | chu kỳ thanh toán hóa đơn |
| Flow 6: exceptions that arrive weeks later | Luồng 6: ngoại lệ phát sinh nhiều tuần sau giao dịch | | |
| bounded outcome / bounded state / bounded exposure | kết quả trong giới hạn / trạng thái trong giới hạn / mức rủi ro trong giới hạn | "mỗi quyết định dẫn đến một kết quả trong giới hạn" | kết quả bị chặn, trạng thái bị chặn |
| end state | trạng thái cuối | Table column header | trạng thái kết thúc cuối cùng |
| path through the pipeline | đường đi qua pipeline | Table column header | |
| Tolerance of the priority difficulties (section title) | Khả năng chịu lỗi trước các khó khăn ưu tiên | Section heading | dung sai của các khó khăn ưu tiên |
| checkpoint 1 … 5 (reconciliation chain) | điểm đối soát 1 … 5 | "năm điểm đối soát của chuỗi đối soát (P19)" | trạm kiểm soát |

## Tolerance cases W1–W11 (part title)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| case (W1–W11) | tình huống | "mười một tình huống, từ W1 đến W11" | ca sự cố |
| Cases W1–W4: uncertain delivery | Tình huống W1–W4: truyền nhận không chắc chắn | Table caption | |
| Cases W5–W8: infrastructure and documents | Tình huống W5–W8: hạ tầng và chứng từ | Table caption | |
| Cases W9–W11: fraud and gray failure | Tình huống W9–W11: gian lận và sự cố ngầm | Table caption; first use "sự cố ngầm (gray failure)" | lỗi xám, sự cố xám |
| W1 Link lost after approval | W1 Mất kết nối sau khi được chấp thuận | | mất liên kết sau phê duyệt |
| W2 Terminal gives up first | W2 Máy POS hết thời gian chờ trước | | thiết bị đầu cuối bỏ cuộc trước |
| W3 Card fails its final check | W3 Thẻ từ chối ở bước kiểm tra cuối | | |
| W4 Batch uploaded twice | W4 Lô giao dịch bị tải lên hai lần | "tải lên" as in the matching difficulty's name | lô giao dịch bị gửi hai lần |
| W5 Tết peak | W5 Cao điểm Tết | | đỉnh Tết |
| W6 Site lost at the cut-off | W6 Mất trung tâm dữ liệu vào giờ chốt | | mất địa điểm tại thời điểm cắt |
| W7 Statement run interrupted and repeated | W7 Đợt lập sao kê bị gián đoạn rồi chạy lại | | |
| W8 Chargeback after the statement | W8 Bồi hoàn sau khi đã gửi sao kê | | |
| W9 POS cash-out | W9 Rút tiền mặt qua máy POS | | |
| W10 Skimmer forces fallback | W10 Thiết bị skimmer buộc giao dịch chuyển sang dải từ | First use "chuyển sang dải từ (fallback)" | |
| W11 Gray failure on an issuer route | W11 Sự cố ngầm trên tuyến kết nối tới tổ chức phát hành thẻ | | |
| traceability summary | bảng truy vết | Table caption "Truy vết từ nhóm nguyên nhân gốc đến thành phần, vùng và tình huống" | |
