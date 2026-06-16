---
name: vietnam-integration-landscape
keywords: [presales, vietnam, integration, tich hop, vnpay, momo, ghn, ghtk, zalo, e-invoice, banking]
description: Bản đồ các tích hợp bên thứ 3 phổ biến trong dự án Odoo tại Việt Nam (hóa đơn điện tử, ngân hàng, thanh toán, vận chuyển, social commerce) - giúp PreSale ước lượng phạm vi tích hợp ngay từ đầu
odoo_versions: [all]
related_skills: [l10n-vietnam-compliance-guide, presales-effort-estimation-guide, external-api-patterns, presales-fit-gap-analysis-guide]
---

# Vietnam Integration Landscape (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  VIETNAM INTEGRATION LANDSCAPE                                                ║
║  "Khách dùng [NCC X] — Odoo có kết nối sẵn không?" — câu hỏi #2 sau Compliance║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Tài liệu này tổng hợp **các hệ sinh thái bên thứ 3 phổ biến tại Việt Nam** mà một dự án Odoo thường cần kết nối: hóa đơn điện tử, ngân hàng, cổng thanh toán, vận chuyển/logistics, cơ quan thuế/BHXH, và social commerce. Mục tiêu: giúp PreSale **nhận diện ngay trong buổi Discovery** các hạng mục tích hợp tiềm ẩn, gắn độ phức tạp sơ bộ, và đưa vào bảng Fit-Gap đúng nhãn từ đầu — tránh tình trạng "quên" tích hợp rồi phát sinh effort lớn ở giai đoạn sau.

> ⚠️ **Đây là bản đồ định hướng cho PreSale, KHÔNG phải cam kết kỹ thuật.** Mọi mức "Mức độ sẵn có" và "Độ phức tạp" trong các bảng dưới đây là **ước lượng mặc định, cần verify lại** cho đúng version Odoo + đúng nhà cung cấp cụ thể của khách trước khi đưa vào Proposal.

---

## 1. Tổng quan & cách dùng

### 1.1 Nguyên tắc mặc định

Với **MỌI tích hợp** liệt kê trong tài liệu này, mặc định coi là **🔌 Gap (Integration)** trong Fit-Gap (`presales-fit-gap-analysis-guide.md`) — **trừ khi** đã verify (qua `github-verification-guide.md` hoặc kiểm tra trực tiếp Odoo Apps Store/OCA cho đúng version) rằng có module/connector sẵn.

Nói cách khác:
- **Không** mặc định "Odoo chắc có sẵn rồi" chỉ vì đó là tên thương hiệu lớn (VNPay, GHN...).
- **Không** trả lời khách "có thể tích hợp được" mà bỏ qua bước báo effort — mọi tích hợp đều có chi phí, kể cả khi dùng framework có sẵn của Odoo (chỉ là chi phí thấp hơn).
- Khi **đã verify có module sẵn** (vd OCA payment provider cho VNPay ở 1 version cụ thể), hạ nhãn xuống 🔧 Partial Fit (Configuration) — vì vẫn cần cấu hình + test, chỉ là không cần code mới.

### 1.2 Pattern kỹ thuật chung

Khi 1 tích hợp được xác nhận là Gap và cần code mới, pattern kỹ thuật chuẩn để áp dụng là **`external-api-patterns.md`** — bao gồm:
- Lưu trữ credential (API key/secret) qua `ir.config_parameter` hoặc model config riêng (group `base.group_system`).
- HTTP client mixin với retry/backoff, logging, xử lý lỗi.
- Pattern sync: pull (cron import), push (override `write`/`create`), bidirectional, hoặc webhook (incoming/outgoing).
- OAuth2 token management nếu NCC yêu cầu.

Một số tích hợp (payment, shipping) có **framework riêng sẵn trong Odoo core** (`payment.provider`, `delivery.carrier`) — khi đó vẫn dùng `external-api-patterns.md` cho phần gọi API, nhưng **kế thừa framework đó** thay vì viết model hoàn toàn mới (xem Mục 4 và 5).

### 1.3 Cách đọc các bảng dưới đây

Mỗi bảng tích hợp có 4 cột chuẩn:

| Cột | Ý nghĩa |
|---|---|
| **Tên/Nhà cung cấp** | Tên thương hiệu phổ biến tại VN |
| **Loại tích hợp** | 1 chiều (Odoo → NCC hoặc NCC → Odoo) hay 2 chiều (đồng bộ qua lại) |
| **Mức độ sẵn có** | Đánh giá thận trọng — mặc định "Cần verify, hiếm khi có sẵn" trừ khi nêu rõ framework Odoo áp dụng được |
| **Độ phức tạp** | Đơn giản / Trung bình / Phức tạp — tham chiếu tier man-day tại `presales-effort-estimation-guide.md` mục 4 |

---

## 2. Hóa đơn điện tử (HĐĐT)

Hóa đơn điện tử là hạng mục tích hợp **gần như chắc chắn xuất hiện** trong mọi deal kế toán/ERP tại VN (bắt buộc theo Nghị định 123/2020/NĐ-CP + Thông tư 78/2021/TT-BTC). Đây là tích hợp **2 chiều**: Odoo gửi dữ liệu hóa đơn → NCC HĐĐT phát hành + cấp mã CQT → ghi ngược số hóa đơn/mã/link tra cứu vào `account.move`.

> 📌 **Chi tiết pháp lý, khung đánh giá, và câu trả lời mẫu cho khách**: xem `l10n-vietnam-compliance-guide.md` mục 3. Phần dưới đây chỉ tóm tắt nhanh cho mục đích "bản đồ tích hợp".

| Tên/Nhà cung cấp | Loại tích hợp | Mức độ sẵn có | Độ phức tạp |
|---|---|---|---|
| MISA meInvoice | 2 chiều | Cần verify — hiếm khi có module sẵn trong Odoo Community/Enterprise, thường cần custom qua REST API | Trung bình-Phức tạp (8-15 man-day) |
| Viettel S-Invoice / vInvoice | 2 chiều | Cần verify — hiếm khi có module sẵn, thường cần custom qua Web Service/REST API | Trung bình-Phức tạp (8-15 man-day) |
| VNPT Invoice | 2 chiều | Cần verify — hiếm khi có module sẵn, thường cần custom qua API | Trung bình-Phức tạp (8-15 man-day) |
| BKAV eHoadon | 2 chiều | Cần verify — hiếm khi có module sẵn, thường cần custom qua API | Trung bình-Phức tạp (8-15 man-day) |
| FPT eInvoice | 2 chiều | Cần verify — hiếm khi có module sẵn, thường cần custom qua API | Trung bình-Phức tạp (8-15 man-day) |

**Range 8-15 man-day** lấy từ `presales-effort-estimation-guide.md` mục 4 (dòng "Hóa đơn điện tử VN") — biến động theo: số loại hóa đơn cần hỗ trợ (bán, điều chỉnh, thay thế, hủy), chất lượng tài liệu API của NCC, có SDK Python sẵn không.

---

## 3. Ngân hàng (Banking)

Tích hợp ngân hàng phục vụ chủ yếu cho **đối soát công nợ tự động** (bank reconciliation) — đối chiếu giao dịch chuyển khoản của khách hàng/NCC với sổ sách `account.move`/`account.payment` trong Odoo.

| Ngân hàng | Loại tích hợp | Mức độ sẵn có | Độ phức tạp |
|---|---|---|---|
| Vietcombank | 1 chiều (statement → Odoo) | Cần verify — hiếm khi có sẵn, thường cần custom qua SMS/email parsing hoặc Open Banking API | Trung bình-Phức tạp |
| Techcombank | 1 chiều (statement → Odoo) | Cần verify — tương tự | Trung bình-Phức tạp |
| BIDV | 1 chiều (statement → Odoo) | Cần verify — tương tự | Trung bình-Phức tạp |
| MBBank | 1 chiều (statement → Odoo) | Cần verify — tương tự | Trung bình-Phức tạp |
| ACB | 1 chiều (statement → Odoo) | Cần verify — tương tự | Trung bình-Phức tạp |
| VietinBank | 1 chiều (statement → Odoo) | Cần verify — tương tự | Trung bình-Phức tạp |
| TPBank | 1 chiều (statement → Odoo) | Cần verify — tương tự | Trung bình-Phức tạp |

### 3.1 Hai phương thức tích hợp phổ biến

| Phương thức | Ưu điểm | Nhược điểm |
|---|---|---|
| **SMS Banking / Email statement parsing** | Rẻ hơn, không cần thủ tục cấp quyền phức tạp với ngân hàng, triển khai nhanh | Kém tin cậy (phụ thuộc format SMS/email có thể thay đổi không báo trước), thường vẫn cần **đối soát thủ công định kỳ** để bắt sai sót, dễ bỏ sót giao dịch nếu mất kết nối |
| **Open Banking API / Corporate API** | Chính thống, dữ liệu đầy đủ và tin cậy hơn, có thể chủ động pull lịch sử giao dịch | Cần ngân hàng **cấp quyền doanh nghiệp (corporate banking)** — thủ tục pháp lý + kỹ thuật phức tạp hơn nhiều (hợp đồng riêng, KYC doanh nghiệp), một số ngân hàng **tính phí dịch vụ API** theo giao dịch/tháng, thời gian chờ cấp quyền có thể kéo dài (vài tuần đến vài tháng) — **ảnh hưởng trực tiếp đến timeline dự án** |

**Khuyến nghị PreSale:**
- Hỏi khách ngay từ Discovery: hiện đang đối soát ngân hàng thế nào (thủ công 100%, hay đã dùng phần mềm kế toán có tích hợp)?
- Nếu khách kỳ vọng tự động hoàn toàn qua Open Banking API → **cảnh báo sớm** về thời gian chờ cấp quyền từ ngân hàng (có thể là rủi ro timeline, không phải rủi ro kỹ thuật của Odoo).
- Độ phức tạp **Trung bình-Phức tạp tùy ngân hàng** — một số ngân hàng có API/SDK tốt hơn (đặc biệt nhóm ngân hàng số, fintech-friendly), một số gần như không có API doanh nghiệp công khai → khi đó SMS/email parsing là lựa chọn thực tế duy nhất.

---

## 4. Cổng thanh toán (Payment Gateways)

| Cổng thanh toán | Loại tích hợp | Mức độ sẵn có | Độ phức tạp |
|---|---|---|---|
| VNPay | 2 chiều (redirect/IPN) | Cần verify — có thể đã có module cộng đồng (OCA hoặc Odoo Apps Store) cho 1 số version, PHẢI VERIFY trước khi cam kết | Đơn giản-Trung bình nếu có sẵn/dùng framework `payment.provider`; Phức tạp nếu tự xây từ đầu |
| Momo | 2 chiều (redirect/IPN) | Cần verify — tương tự VNPay, kiểm tra Apps Store/OCA theo version cụ thể | Đơn giản-Trung bình nếu dùng `payment.provider`; Phức tạp nếu tự xây |
| ZaloPay | 2 chiều (redirect/IPN) | Cần verify — hiếm khi có sẵn, thường cần custom theo `payment.provider` | Đơn giản-Trung bình nếu dùng `payment.provider`; Phức tạp nếu tự xây |
| OnePay | 2 chiều (redirect/IPN) | Cần verify — hiếm khi có sẵn | Đơn giản-Trung bình nếu dùng `payment.provider`; Phức tạp nếu tự xây |
| Payoo | 2 chiều (redirect/IPN) | Cần verify — hiếm khi có sẵn | Đơn giản-Trung bình nếu dùng `payment.provider`; Phức tạp nếu tự xây |
| ShopeePay | 2 chiều (redirect/IPN) | Cần verify — hiếm khi có sẵn | Đơn giản-Trung bình nếu dùng `payment.provider`; Phức tạp nếu tự xây |

### 4.1 Lưu ý quan trọng — framework `payment.provider`

Odoo **có sẵn framework "Payment Provider"** (`payment.provider`, trước đây gọi là "Payment Acquirer") cho thanh toán online trên Sales/eCommerce/Invoicing — đây là phần **core đã có sẵn**, không phải Gap. Framework này xử lý sẵn: luồng redirect đến cổng thanh toán, callback/IPN xác nhận giao dịch, tạo `payment.transaction`, link với `sale.order`/`account.move`.

Một số cổng thanh toán VN **có thể** đã có module implement sẵn cho `payment.provider` (qua Odoo Apps Store hoặc OCA) — nhưng **PHẢI VERIFY cho đúng version cụ thể** trước khi cam kết với khách (dùng `github-verification-guide.md`).

**2 kịch bản:**
1. **Đã có module cho NCC + version của khách** → 🔧 Partial Fit (Configuration) — chỉ cần cài module, cấu hình API key/merchant ID, test sandbox. Độ phức tạp: **Đơn giản-Trung bình**.
2. **Chưa có module** → 🔌 Gap (Integration), nhưng **viết theo framework `payment.provider` có sẵn** (kế thừa `payment.provider` + `payment.transaction`, implement các method xử lý redirect/IPN theo tài liệu API của cổng thanh toán) — effort **thấp hơn đáng kể** so với xây 1 model thanh toán hoàn toàn mới từ đầu, vì đã tận dụng được UI, luồng nghiệp vụ, và liên kết với `sale.order`/`account.move` có sẵn. Pattern kỹ thuật cho phần gọi API: `external-api-patterns.md`.

→ Độ phức tạp tổng: **Đơn giản-Trung bình** nếu rơi vào kịch bản 1 hoặc 2 (dùng framework); **Phức tạp** chỉ khi vì lý do nào đó phải tự xây luồng thanh toán từ đầu (hiếm khi cần thiết).

---

## 5. Vận chuyển / Logistics (Shipping)

| Đơn vị vận chuyển | Loại tích hợp | Mức độ sẵn có | Độ phức tạp |
|---|---|---|---|
| GHN (Giao Hàng Nhanh) | 2 chiều (tính phí + tạo vận đơn + tracking) | Cần verify — kiểm tra module Community/Enterprise/OCA theo version cụ thể, hiếm khi có sẵn | Trung bình |
| GHTK (Giao Hàng Tiết Kiệm) | 2 chiều | Cần verify — tương tự | Trung bình |
| J&T Express | 2 chiều | Cần verify — tương tự | Trung bình |
| Viettel Post | 2 chiều | Cần verify — tương tự | Trung bình |
| Ahamove | 2 chiều | Cần verify — tương tự | Trung bình |
| BEST Express | 2 chiều | Cần verify — tương tự | Trung bình |
| Ninja Van | 2 chiều | Cần verify — tương tự | Trung bình |

### 5.1 Lưu ý quan trọng — framework `delivery.carrier`

Tương tự payment, Odoo **có sẵn framework "Delivery Carrier"** (`delivery.carrier`) cho: tính phí vận chuyển (shipping rate) ngay trên Sales Order/Website checkout, tạo vận đơn (shipment) khi giao hàng (`stock.picking`), và nhận tracking number.

**Kiểm tra module có sẵn cho từng hãng** (Community/Enterprise/OCA) theo đúng version của khách trước. Nếu chưa có:
- Implement theo framework `delivery.carrier` — kế thừa và override các method tính phí (`rate_shipment`) và tạo vận đơn (`send_shipping`), gọi API của hãng vận chuyển theo `external-api-patterns.md`.
- Việc tận dụng framework có sẵn giúp **giảm effort đáng kể** so với xây luồng "tính phí ship + tạo vận đơn" từ đầu, vì đã có sẵn UI cấu hình carrier, liên kết với `stock.picking`, và hiển thị phí ship trên Sales Order/Website.

**Độ phức tạp: Trung bình** — phần lớn API của các hãng GHN/GHTK/Viettel Post... có tài liệu REST tương đối đầy đủ (tạo đơn, tính phí, hủy đơn, tra cứu trạng thái), nhưng vẫn cần xử lý mapping địa chỉ (tỉnh/huyện/xã theo mã của từng hãng — mỗi hãng có bộ mã địa giới hành chính riêng, không đồng nhất), và đồng bộ trạng thái giao hàng 2 chiều (webhook hoặc polling).

---

## 6. Thuế điện tử / Cơ quan nhà nước

| Hệ thống | Mô tả | Hiện trạng tích hợp Odoo |
|---|---|---|
| **eTax / Thuế điện tử** (thuedientu.gdt.gov.vn) | Kê khai thuế GTGT, TNDN, TNCN... | Thường **KHÔNG tích hợp trực tiếp** với Odoo — workflow thực tế là **xuất file/báo cáo đúng định dạng từ Odoo**, sau đó kế toán nộp thủ công qua cổng eTax |
| **BHXH điện tử** | Khai báo bảo hiểm xã hội cho nhân viên | Tương tự — thường là **export file theo mẫu** quy định, không có API công khai để tích hợp trực tiếp |

**Khuyến nghị PreSale:**
- **Không chào** "tích hợp trực tiếp với eTax/BHXH điện tử" — đây là hệ thống của cơ quan nhà nước, gần như không có API mở cho doanh nghiệp/bên thứ 3 tích hợp trực tiếp, và độ phức tạp/rủi ro pháp lý nếu cố làm là rất cao (Phức tạp/hiếm khi làm).
- Thay vào đó, đề xuất giải pháp **"export đúng định dạng"**: custom report (`report-patterns.md`) hoặc export Excel/XML theo đúng mẫu tờ khai mà Tổng cục Thuế/BHXH quy định, để kế toán tải lên cổng eTax/BHXH thủ công.
- Đây vẫn là 1 dòng **🛠️ Gap (Customize)** trong Fit-Gap (không phải Gap-Integration) — effort tham khảo "Custom QWeb report" tại `presales-effort-estimation-guide.md` mục 3.

---

## 7. Social Commerce & Communication

| Tên/Nhà cung cấp | Loại tích hợp | Mức độ sẵn có | Độ phức tạp |
|---|---|---|---|
| Zalo OA / ZNS (Zalo Notification Service) | 1 chiều (Odoo → Zalo, gửi thông báo đơn hàng/OTP/nhắc nợ) | Cần verify — Odoo không có connector Zalo sẵn, cần custom qua Zalo Official Account API | Trung bình |
| Facebook/TikTok Shop | 2 chiều (đồng bộ đơn hàng/tồn kho qua Open API) | Cần verify — hiếm khi có sẵn, API sàn thay đổi thường xuyên | Trung bình-Phức tạp |
| Shopee | 2 chiều (đồng bộ đơn hàng/tồn kho qua Shopee Open API) | Cần verify — hiếm khi có sẵn | Trung bình-Phức tạp |
| Lazada | 2 chiều (đồng bộ đơn hàng/tồn kho qua Lazada Open API) | Cần verify — hiếm khi có sẵn | Trung bình-Phức tạp |

**Lưu ý Zalo OA/ZNS:** Tại thị trường VN, Zalo OA/ZNS thường đóng vai trò **thay thế cho app "WhatsApp"** trong Odoo Enterprise (xem `odoo-app-feature-matrix.md` mục 7) — Odoo Enterprise có sẵn tích hợp WhatsApp Business API (template message, 2 chiều với khách hàng), nhưng **không có connector Zalo tương đương**. Khi khách hỏi "Odoo có gửi Zalo cho khách không?" → trả lời rõ đây là **custom integration** với Zalo OA/ZNS API, dùng pattern `external-api-patterns.md` (outgoing webhook/REST call khi có sự kiện trong Odoo — vd xác nhận đơn hàng, nhắc thanh toán).

**Lưu ý sàn TMĐT (Shopee/Lazada/TikTok Shop):** Độ phức tạp **Trung bình-Phức tạp** không chỉ vì khối lượng mapping dữ liệu (sản phẩm, biến thể, tồn kho, đơn hàng, trạng thái vận chuyển, khuyến mãi của sàn) mà còn vì **API của các sàn thay đổi thường xuyên** (versioning, rate limit, chính sách mới) — cần tính thêm **chi phí bảo trì sau go-live** (không chỉ chi phí build ban đầu), nên trao đổi rõ với khách về SLA bảo trì tích hợp này trong Proposal.

---

## 8. Bảng tổng hợp ưu tiên khảo sát

Dùng bảng này trong buổi Discovery (`presales-discovery-questionnaire.md`) để hỏi khách **ngay từ đầu** xem có đang/sẽ cần tích hợp nào dưới đây — tránh phát hiện muộn ở giai đoạn Fit-Gap hoặc UAT.

| Nhóm tích hợp | Câu hỏi cần hỏi khách trong Discovery |
|---|---|
| **Hóa đơn điện tử** | Công ty đang dùng nhà cung cấp HĐĐT nào (MISA/Viettel/VNPT/BKAV/FPT...)? Có bắt buộc giữ nguyên NCC này không? Cần hỗ trợ những loại hóa đơn nào (bán, điều chỉnh, thay thế, hủy)? *(xem `presales-discovery-questionnaire.md` Phần 2.5 + `l10n-vietnam-compliance-guide.md` mục 3)* |
| **Ngân hàng** | Công ty dùng ngân hàng nào cho giao dịch chính? Hiện đối soát ngân hàng thế nào (thủ công/đã có phần mềm hỗ trợ)? Có khả năng xin được quyền Open Banking/Corporate API từ ngân hàng không, hay chỉ có thể dùng SMS/email statement? *(xem `presales-discovery-questionnaire.md` Phần 2.4, câu 6)* |
| **Cổng thanh toán** | Có bán hàng online cần thanh toán trực tuyến không? Khách hàng thường thanh toán qua kênh nào (VNPay/Momo/ZaloPay/chuyển khoản/COD)? |
| **Vận chuyển** | Công ty tự giao hàng hay dùng đơn vị vận chuyển ngoài? Đang dùng hãng nào (GHN/GHTK/J&T/Viettel Post...)? Có cần tính phí ship tự động trên đơn hàng/website không? Có cần tạo vận đơn + tracking từ Odoo không? |
| **Thuế điện tử/BHXH** | Quy trình hiện tại nộp tờ khai thuế GTGT/TNDN/TNCN, BHXH như thế nào? Đang xuất file từ phần mềm kế toán cũ theo mẫu nào? |
| **Social Commerce** | Có bán trên sàn TMĐT (Shopee/Lazada/TikTok Shop) không — cần đồng bộ đơn/tồn 2 chiều? Có dùng Zalo OA để CSKH/gửi thông báo đơn hàng không? *(xem `presales-discovery-questionnaire.md` Phần 2.6, câu 3-4)* |

---

## Liên kết

- Chi tiết pháp lý + đánh giá `l10n_vn` cho HĐĐT/báo cáo thuế: `skills/l10n-vietnam-compliance-guide.md`
- Tier man-day cho từng mức độ phức tạp tích hợp: `skills/presales-effort-estimation-guide.md` (mục 4)
- Pattern kỹ thuật chung khi build tích hợp (REST/SOAP, webhook, OAuth2, retry): `skills/external-api-patterns.md`
- Đưa từng tích hợp vào bảng Fit-Gap với nhãn 🔌 Gap (Integration): `skills/presales-fit-gap-analysis-guide.md`
- Câu hỏi Discovery liên quan tích hợp theo từng khối nghiệp vụ: `skills/presales-discovery-questionnaire.md`
- So sánh Zalo OA/ZNS với WhatsApp app của Odoo Enterprise: `skills/odoo-app-feature-matrix.md` (mục 7)
