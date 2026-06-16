---
name: presales-discovery-questionnaire
keywords: [presales, discovery, khao sat, requirements gathering, questionnaire, pain points]
description: Bộ câu hỏi khảo sát có cấu trúc theo từng khối nghiệp vụ, giúp PreSale thu thập đủ thông tin để map sang Odoo Apps và chuẩn bị cho Fit-Gap Analysis.
odoo_versions: [all]
related_skills: [odoo-app-feature-matrix, presales-fit-gap-analysis-guide, presales-industry-solution-templates, presales-effort-estimation-guide]
---

# PreSale Discovery Questionnaire

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  DISCOVERY QUESTIONNAIRE                                                      ║
║  Khảo sát yêu cầu khách hàng → Discovery Notes → Fit-Gap Analysis             ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Cách dùng

1. Dùng **Phần 1** cho buổi gặp đầu tiên (kick-off) để hiểu tổng quan khách hàng.
2. Dùng **Phần 2** cho từng buổi workshop chuyên sâu theo phòng ban (mỗi khối ~45-60 phút).
3. Trong khi khảo sát, đối chiếu câu trả lời với `skills/odoo-app-feature-matrix.md` để biết Odoo có đáp ứng sẵn không.
4. Đánh dấu các câu trả lời rơi vào **Phần 3 (Red Flags)** — đây là dấu hiệu cần custom dev, ảnh hưởng lớn đến effort/giá.
5. Tổng hợp toàn bộ vào template **Phần 4 (Discovery Notes)** → chuyển sang `skills/presales-fit-gap-analysis-guide.md`.

---

## Phần 1 — Thông tin tổng quan công ty

| # | Câu hỏi | Ghi chú |
|---|---|---|
| 1 | Ngành nghề kinh doanh chính? Có bao nhiêu mảng kinh doanh khác nhau? | Xác định ngành để tra `presales-industry-solution-templates.md` |
| 2 | Quy mô: số nhân viên, số chi nhánh/kho/cửa hàng, số công ty con (nếu có Group) | Ảnh hưởng `multi-company-patterns.md` |
| 3 | Hệ thống đang sử dụng cho từng mảng (Kế toán, CRM, Kho, Nhân sự...)? Excel, Misa, Fast, SAP, phần mềm tự viết...? | Ảnh hưởng phạm vi data migration (`presales-data-migration-scoping-guide.md`) |
| 4 | Lý do muốn triển khai/đổi hệ thống mới? (mở rộng quy mô, hệ thống cũ rời rạc, thiếu báo cáo, hết hỗ trợ...) | Đây là "pain point" chính để xây ROI trong Proposal |
| 5 | Đã từng triển khai ERP chưa? Nếu có, vì sao không thành công/không dùng nữa? | Cảnh báo sớm các rủi ro tương tự |
| 6 | Số lượng user dự kiến dùng hệ thống (theo từng phòng ban)? | Ảnh hưởng license cost — xem `odoo-licensing-deployment-guide.md` |
| 7 | Đa công ty? Đa chi nhánh hạch toán độc lập? Đa tiền tệ? Đa ngôn ngữ? | `multi-company-patterns.md`, `translation-i18n-patterns.md` |
| 8 | Timeline mong muốn go-live? Có mốc thời gian bắt buộc (đầu năm tài chính, mùa cao điểm...)? | Ảnh hưởng phasing trong SOW |
| 9 | Ngân sách dự kiến (khoảng)? Ưu tiên Community hay sẵn sàng Enterprise? | `odoo-editions.md`, `odoo-licensing-deployment-guide.md` |
| 10 | Ai là người ra quyết định cuối cùng? Ai là "champion"/người dùng chính sẽ làm việc với team triển khai? | Xác định stakeholder cho Proposal |
| 11 | Có yêu cầu bắt buộc về hạ tầng không (on-premise vì lý do bảo mật/quy định ngành)? | `odoo-licensing-deployment-guide.md` |
| 12 | Khách có đang đánh giá song song giải pháp/đối thủ nào khác không? | `presales-competitor-comparison-guide.md` |

---

## Phần 2 — Bộ câu hỏi theo khối nghiệp vụ

### 2.1 Sales & CRM

| # | Câu hỏi |
|---|---|
| 1 | Quy trình từ lead → cơ hội → báo giá → chốt đơn hiện gồm những bước nào? Ai phụ trách từng bước? |
| 2 | Nguồn lead đến từ đâu (website, cold call, hội chợ, giới thiệu, sàn TMĐT)? |
| 3 | Báo giá có cần duyệt qua nhiều cấp không? Theo điều kiện gì (giá trị đơn, % chiết khấu)? |
| 4 | Chính sách giá: có bảng giá riêng theo nhóm khách hàng/khu vực/kênh không? Chiết khấu theo số lượng (bậc thang)? |
| 5 | Có chương trình hoa hồng cho sales/đại lý/CTV không? Công thức tính như thế nào? |
| 6 | Có hợp đồng bán hàng dài hạn/định kỳ (subscription, bảo trì hàng năm) không? |
| 7 | Sau khi chốt đơn, quy trình giao hàng — xuất hóa đơn — thu tiền diễn ra thế nào? |
| 8 | Có quy trình CSKH/bảo hành/ticket sau bán không? |
| 9 | Báo cáo doanh số cần xem theo chiều nào (nhân viên sale, khu vực, sản phẩm, kênh bán, theo thời gian)? |
| 10 | Bán hàng qua nhiều kênh: trực tiếp, đại lý, online, sàn TMĐT (Shopee/Lazada/TikTok Shop)? Có cần đồng bộ tồn/đơn không? |

### 2.2 Mua hàng (Purchasing)

| # | Câu hỏi |
|---|---|
| 1 | Quy trình mua hàng: có bước "đề nghị mua hàng" (Purchase Request) trước khi tạo PO không? |
| 2 | Có yêu cầu duyệt PO theo hạn mức giá trị/phòng ban không? |
| 3 | Số lượng NCC thường xuyên giao dịch? Có đánh giá/xếp hạng NCC định kỳ không? |
| 4 | Có gửi RFQ cho nhiều NCC để so sánh giá trước khi chọn không? |
| 5 | Có nhập khẩu hàng hóa không? Cách tính giá vốn có bao gồm chi phí phụ (thuế NK, vận chuyển, bảo hiểm — landed cost) không? |
| 6 | Có hợp đồng khung/giá cố định theo thời gian với NCC không? |
| 7 | Thanh toán NCC: có lịch thanh toán theo điều khoản công nợ (30/60/90 ngày) không? |

### 2.3 Kho / Logistics (Inventory)

| # | Câu hỏi |
|---|---|
| 1 | Số lượng kho, vị trí địa lý? Có kho ngoại quan/kho thuê ngoài không? |
| 2 | Quy trình nhập kho: hàng về có qua khu vực kiểm tra (QC) trước khi nhập kho chính không (1 bước hay nhiều bước)? |
| 3 | Quy trình xuất kho: có quy trình lấy hàng — đóng gói — giao hàng (pick-pack-ship) tách biệt không? |
| 4 | Có quản lý theo lô (batch)/số serial/hạn sử dụng (FEFO) không? Ngành nào bắt buộc (dược, thực phẩm, điện tử)? |
| 5 | Có dùng máy quét mã vạch/máy in tem nhãn không? |
| 6 | Kiểm kê: định kỳ toàn bộ hay kiểm đếm luân phiên (cycle count)? |
| 7 | Có chuyển kho nội bộ giữa các chi nhánh/kho không? Có cần duyệt phiếu chuyển kho không? |
| 8 | Đơn vị tính: 1 sản phẩm có nhiều đơn vị quy đổi không (thùng/hộp/cái, kg/tấn)? |
| 9 | Có hàng ký gửi (consignment) — của KH gửi tại kho mình hoặc mình gửi tại kho đối tác — không? |

### 2.4 Sản xuất (Manufacturing) — *nếu khách có sản xuất*

| # | Câu hỏi |
|---|---|
| 1 | Sản xuất theo đơn hàng (Make-to-Order) hay theo tồn kho dự báo (Make-to-Stock)? |
| 2 | BOM (định mức NVL) có nhiều cấp không (NVL → bán thành phẩm → thành phẩm)? |
| 3 | Có chia theo công đoạn/máy/work center không? Có cần lập lịch sản xuất (scheduling) không? |
| 4 | Có gia công ngoài (đưa NVL cho bên thứ 3 gia công, nhận lại thành phẩm) không? |
| 5 | Có kiểm tra chất lượng (QC) tại các công đoạn không? |
| 6 | Hiện đang tính giá thành sản phẩm như thế nào (theo định mức, theo thực tế, phân bổ chi phí chung)? |
| 7 | Có quản lý phế phẩm/hao hụt định mức không? |

### 2.5 Kế toán / Tài chính (Accounting & Finance)

| # | Câu hỏi |
|---|---|
| 1 | Đang dùng phần mềm kế toán nào? Có cần chạy song song trong giai đoạn đầu không? |
| 2 | Áp dụng chế độ kế toán nào: Thông tư 200 hay Thông tư 133? |
| 3 | Có xuất hóa đơn điện tử không? Đang dùng nhà cung cấp nào (MISA, Viettel, VNPT, BKAV...)? *(xem `l10n-vietnam-compliance-guide.md`)* |
| 4 | Đa công ty có hạch toán độc lập không? Có giao dịch nội bộ giữa các công ty (intercompany) cần loại trừ khi hợp nhất không? |
| 5 | Có giao dịch đa tiền tệ không? Tỷ giá lấy theo nguồn nào (NHNN, ngân hàng thương mại)? |
| 6 | Quy trình đối chiếu ngân hàng hiện tại — có import sao kê tự động không? |
| 7 | Có lập ngân sách (budget) theo phòng ban/dự án/khoản mục không, và theo dõi thực tế vs ngân sách? |
| 8 | Ngoài báo cáo tài chính bắt buộc (BCTC, tờ khai thuế), còn cần báo cáo quản trị nào đặc thù? |
| 9 | Có quản lý tài sản cố định (khấu hao) không? |

### 2.6 Nhân sự (HR)

| # | Câu hỏi |
|---|---|
| 1 | Số lượng nhân viên? Phân bổ theo bao nhiêu địa điểm làm việc? |
| 2 | Hiện chấm công bằng cách nào (máy chấm công hãng gì, app riêng)? Có cần Odoo kết nối với máy chấm công hiện có không? |
| 3 | Tính lương: in-house hay thuê ngoài (outsourcing)? |
| 4 | Quy tắc lương có phức tạp không (ca kíp, tăng ca, phụ cấp, KPI thưởng theo doanh số)? |
| 5 | Quy trình tuyển dụng hiện tại — có cần đăng tin lên website/portal không? |
| 6 | Có chu kỳ đánh giá hiệu suất (appraisal) định kỳ không? |
| 7 | Quản lý hợp đồng lao động, BHXH/BHYT — có cần xuất file theo mẫu cơ quan BHXH không? |

### 2.7 Dự án (Project) — *nếu khách quản lý theo dự án*

| # | Câu hỏi |
|---|---|
| 1 | Loại dự án: trọn gói (fixed price) hay theo thời gian + vật tư (time & material)? |
| 2 | Cách tính chi phí dự án: nhân công (timesheet), vật tư (từ kho/mua hàng), chi phí khác? |
| 3 | Xuất hóa đơn cho khách theo tiến độ (milestone billing) hay theo timesheet thực tế? |
| 4 | Có cần Gantt chart, quản lý phụ thuộc giữa các task, phân bổ nguồn lực (resource planning) không? |
| 5 | Dự án có liên kết với mua hàng/kho (vật tư cho công trình) không? |

### 2.8 Website / eCommerce / Kênh online — *nếu liên quan*

| # | Câu hỏi |
|---|---|
| 1 | Đã có website chưa? Đang dùng nền tảng nào (WordPress, Shopify, tự code...)? |
| 2 | Có cần website mới xây trên Odoo, hay chỉ tích hợp 2 chiều (tồn kho/giá/đơn hàng) với website hiện tại? |
| 3 | Bán trên các sàn TMĐT (Shopee, Lazada, TikTok Shop) — có cần đồng bộ đơn hàng/tồn kho 2 chiều không? |
| 4 | Có chatbot/Zalo OA dùng để bán hàng/CSKH cần tích hợp không? *(xem `vietnam-integration-landscape.md`)* |

---

## Phần 3 — Checklist "Red Flags" (dấu hiệu Custom Dev lớn)

Khi nghe các câu trả lời sau, **đánh dấu ngay** — đây là các yêu cầu thường vượt khỏi cấu hình chuẩn và cần ước lượng effort riêng (xem `presales-effort-estimation-guide.md`):

- [ ] Quy trình phê duyệt **>3 cấp** với điều kiện rẽ nhánh phức tạp (theo giá trị, theo loại, theo người)
- [ ] Công thức tính giá/hoa hồng/chiết khấu có **nhiều biến số kết hợp** (không phải bảng giá đơn giản)
- [ ] Yêu cầu tích hợp **2 chiều, real-time** với hệ thống cũ **không có API** sẵn
- [ ] Báo cáo phải đúng **mẫu cứng** của cơ quan nhà nước/đối tác (mẫu Excel/PDF cố định, không thể thay đổi layout)
- [ ] Quy trình đặc thù ngành **chưa có module chuẩn** (vd: nghiệm thu khối lượng hoàn thành theo QS trong xây dựng, quản lý theo m²/khối lượng thay vì số lượng)
- [ ] Yêu cầu **chạy song song lâu dài** 2 hệ thống (không có kế hoạch migrate dứt điểm)
- [ ] Dữ liệu lịch sử **khối lượng lớn, không chuẩn hóa** (nhiều file Excel khác cấu trúc, nhiều năm)
- [ ] Yêu cầu **redesign UI/UX** khác hẳn giao diện chuẩn Odoo
- [ ] Tích hợp **thiết bị phần cứng đặc thù** (cân điện tử, máy đóng gói, máy CNC...) chưa có driver/API công khai
- [ ] Yêu cầu tuân thủ **quy định ngành đặc biệt** (dược phẩm - GDP/GSP, thực phẩm - HACCP, tài chính - SBV...)

> Mỗi mục được đánh dấu nên có **1 dòng riêng trong bảng Fit-Gap** (`presales-fit-gap-analysis-guide.md`) và **không** được ước lượng effort theo benchmark "cấu hình chuẩn".

---

## Phần 4 — Output Template: Discovery Notes

Sau khi khảo sát xong, tổng hợp vào file `Discovery_Notes_{TenKhachHang}.md` theo cấu trúc:

```markdown
# Discovery Notes — {Tên khách hàng}

**Ngày khảo sát:** {date}
**Ngành:** {industry}
**Người tham gia (KH):** {names, roles}
**Người tham gia (PreSale):** {names}

## 1. Tổng quan
- Quy mô: {số NV, số chi nhánh, số công ty}
- Hệ thống hiện tại: {liệt kê theo mảng}
- Pain points chính: {...}
- Ngân sách / timeline: {...}
- Edition xu hướng: {Community / Enterprise / chưa rõ}

## 2. Theo từng khối nghiệp vụ
### 2.1 Sales & CRM
- Hiện trạng: ...
- Yêu cầu chính: ...
- App đề xuất sơ bộ: ... (tra `odoo-app-feature-matrix.md`)
- Red flags: ...

### 2.2 Mua hàng
... (lặp lại cấu trúc trên cho từng khối ở Phần 2)

## 3. Bảng tổng hợp Apps đề xuất sơ bộ
| App | Edition | Khối nghiệp vụ | Ghi chú |
|---|---|---|---|

## 4. Red Flags tổng hợp
| # | Mô tả | Khối | Mức độ ảnh hưởng (Cao/TB/Thấp) |
|---|---|---|---|

## 5. Bước tiếp theo
- [ ] Demo theo ngành — `presales-demo-environment-guide.md`
- [ ] Fit-Gap Workshop — `presales-fit-gap-analysis-guide.md`
- [ ] Sơ bộ effort/ngân sách — `presales-effort-estimation-guide.md`
```

---

## Liên kết

- Map câu trả lời sang Apps: `skills/odoo-app-feature-matrix.md`
- Bước tiếp theo (Fit-Gap): `skills/presales-fit-gap-analysis-guide.md`
- Blueprint theo ngành (giúp hỏi đúng trọng tâm hơn): `skills/presales-industry-solution-templates.md`
- Câu hỏi riêng về kế toán/hóa đơn điện tử VN: `skills/l10n-vietnam-compliance-guide.md`
