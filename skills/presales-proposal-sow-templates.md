---
name: presales-proposal-sow-templates
keywords: [presales, proposal, sow, statement of work, quotation, bao gia, hop dong, de xuat]
description: Bộ template chuẩn hoá cho Technical Proposal, Commercial Proposal/Quotation, SOW và hồ sơ đấu thầu - input lấy từ Fit-Gap Analysis.
odoo_versions: [all]
related_skills: [presales-fit-gap-analysis-guide, presales-effort-estimation-guide, odoo-licensing-deployment-guide, presales-competitor-comparison-guide]
---

# Proposal & SOW Templates (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  PROPOSAL & SOW TEMPLATES                                                     ║
║  Fit-Gap (đã sign-off) → Technical Proposal + Commercial Proposal + SOW       ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Tài liệu này cung cấp **template chuẩn hoá** cho 3 loại tài liệu PreSale gửi cho khách sau khi bảng Fit-Gap (`presales-fit-gap-analysis-guide.md`) đã được sign-off: **Technical Proposal**, **Commercial Proposal/Quotation**, và **SOW (Statement of Work)**. Mục tiêu là giúp Solution Consultant **không phải soạn từ đầu mỗi lần** — chỉ cần điền số liệu/nội dung cụ thể của từng khách vào khung có sẵn.

> ⚠️ **Nguyên tắc xuyên suốt**: mọi nội dung trong Proposal/SOW (giải pháp đề xuất, effort, chi phí, out of scope) đều phải **truy vết được về 1 dòng cụ thể trong bảng Fit-Gap đã sign-off**. Không thêm cam kết mới ngoài Fit-Gap mà chưa qua workshop — đây là nguồn gốc phổ biến nhất của tranh chấp scope sau go-live.

---

## 1. Tổng quan bộ tài liệu Proposal

Một bộ hồ sơ chào giá đầy đủ thường gồm 3 tài liệu, phục vụ **3 đối tượng đọc khác nhau** trong tổ chức khách hàng — và thường được gửi cùng lúc nhưng có thể tách riêng nếu khách yêu cầu:

| Tài liệu | Đối tượng đọc chính | Mục đích | Tính ràng buộc |
|---|---|---|---|
| **Technical Proposal** | Trưởng phòng IT, Process Owner, đội kỹ thuật của khách | Chứng minh Odoo + đội triển khai **hiểu đúng bài toán** và có giải pháp khả thi | Tham khảo — không phải văn bản pháp lý |
| **Commercial Proposal / Quotation** | Ban Giám đốc, CFO, người duyệt ngân sách | Trả lời câu hỏi "bao nhiêu tiền, khi nào trả, hiệu lực đến khi nào" | Có hiệu lực trong thời hạn nêu rõ (thường 30 ngày) — là cơ sở đàm phán hợp đồng |
| **SOW (Statement of Work)** | Bộ phận pháp chế/mua sắm của khách + PM 2 bên | Định nghĩa **chính xác** scope, deliverables, timeline, trách nhiệm 2 bên | **Phụ lục hợp đồng — ràng buộc pháp lý**, là căn cứ giải quyết tranh chấp scope creep |

**Thứ tự soạn thảo khuyến nghị:**

1. Technical Proposal trước — vì nó buộc consultant phải tổ chức lại toàn bộ giải pháp theo logic "vấn đề → giải pháp" (dễ tái sử dụng nội dung này sang Commercial và SOW).
2. Commercial Proposal — dùng input effort/chi phí đã tính từ `presales-effort-estimation-guide.md` và license cost từ `odoo-licensing-deployment-guide.md`.
3. SOW soạn sau cùng — vì SOW cần con số Phase/Timeline/Milestone đã thống nhất ở Commercial Proposal, và danh sách "Out of scope" lấy trực tiếp từ Fit-Gap.

> 💡 Với khách hàng nhỏ/SMB, có thể **gộp Technical + Commercial** thành 1 tài liệu duy nhất ("Proposal") để giảm thời gian đọc — nhưng SOW vẫn nên tách riêng vì tính chất pháp lý khác (phụ lục hợp đồng).

---

## 2. Technical Proposal — Cấu trúc & Template

Technical Proposal trả lời câu hỏi: *"Odoo có giải quyết được bài toán của chúng tôi không, và giải quyết như thế nào?"* Nội dung **map trực tiếp** từ Discovery Notes + bảng Fit-Gap sang ngôn ngữ "giải pháp", tránh liệt kê tính năng chung chung không gắn với pain point cụ thể của khách.

```markdown
# TECHNICAL PROPOSAL
## Triển khai Odoo cho [Tên khách hàng]

**Phiên bản tài liệu:** v1.0
**Ngày:** [DD/MM/YYYY]
**Người soạn:** [Tên Solution Consultant / Technical Lead]

---

### 1. Executive Summary

[2-3 đoạn ngắn, viết SAU CÙNG khi đã hoàn thành các phần khác — tóm tắt:
- Bối cảnh khách hàng (ngành, quy mô, lý do tìm giải pháp mới)
- Đề xuất tổng quan (bộ Apps chính + Edition)
- Lợi ích cốt lõi (3-5 điểm, lấy từ Mục 5 - ROI)
- Lộ trình tổng quan (số Phase, timeline tổng)]

---

### 2. Hiện trạng & Pain Points

[Lấy trực tiếp từ Discovery Notes — KHÔNG diễn giải lại bằng số liệu tự suy đoán.
Trình bày theo từng khối nghiệp vụ đã khảo sát:]

#### 2.1. [Tên khối nghiệp vụ — vd "Bán hàng & CRM"]
- **Hệ thống hiện tại:** [vd: Excel + Zalo, không đồng bộ với Kho]
- **Pain points:**
  - [Pain point 1 — trích từ Discovery Notes]
  - [Pain point 2]
- **Tác động:** [vd: mất trung bình X giờ/tuần để đối chiếu thủ công — chỉ ghi nếu khách đã cung cấp số liệu này]

#### 2.2. [Khối nghiệp vụ tiếp theo — lặp lại cấu trúc trên]

---

### 3. Giải pháp đề xuất theo từng phòng ban

[Với mỗi khối nghiệp vụ ở Mục 2, map sang Odoo App tương ứng —
tham chiếu `odoo-app-feature-matrix.md` để đảm bảo đúng tên App/Edition.]

#### 3.1. [Tên khối nghiệp vụ]

| Pain point | Giải pháp Odoo | App | Cách hoạt động |
|---|---|---|---|
| [Pain point 1] | [Tên giải pháp] | [App + Edition] | [Mô tả ngắn gọn quy trình mới, 2-3 câu] |
| [Pain point 2] | ... | ... | ... |

> Với các dòng 🛠️/🔌 trong Fit-Gap thuộc khối này, ghi rõ đây là **hạng mục customize/tích hợp** (xem chi tiết Mục 4) — tránh để khách hiểu nhầm là tính năng có sẵn.

#### 3.2. [Khối nghiệp vụ tiếp theo — lặp lại]

---

### 4. Danh sách Apps & Edition đề xuất

| # | App | Edition (Community/Enterprise) | Số user cần license | Ghi chú |
|---|---|---|---|---|
| 1 | [vd: Sales] | Community | [số user] | — |
| 2 | [vd: Inventory] | Community | [số user] | — |
| 3 | [vd: Accounting] | Enterprise | [số user] | Bắt buộc Enterprise để dùng full kế toán VN |
| 4 | [vd: Field Service] | Enterprise | [số user] | — |

> Chi tiết quy đổi user/license và chi phí, xem `odoo-licensing-deployment-guide.md` — phần này trong Technical Proposal chỉ liệt kê **App + Edition**, KHÔNG ghi giá (giá thuộc Commercial Proposal).

---

### 5. Danh sách Customization & Tích hợp

[Lấy TRỰC TIẾP các dòng 🛠️ Gap-Custom và 🔌 Gap-Integration từ bảng Fit-Gap đã sign-off.
KHÔNG thêm hạng mục mới chưa có trong Fit-Gap.]

| Mã (theo Fit-Gap) | Hạng mục | Loại | Mô tả giải pháp | Phase dự kiến |
|---|---|---|---|---|
| FG-003 | [Tên hạng mục] | 🛠️ Custom | [Mô tả ngắn — KHÔNG đi sâu chi tiết kỹ thuật, đó là việc của SOW/Functional Spec] | Phase 1 |
| FG-004 | [Tên hạng mục] | 🔌 Integration | [Mô tả ngắn] | Phase 2 |

---

### 6. Kiến trúc tổng thể

[Placeholder cho sơ đồ kiến trúc — chèn hình ảnh/diagram thể hiện:
- Các module Odoo và luồng dữ liệu giữa chúng
- Các hệ thống bên ngoài kết nối (e-invoice, sàn TMĐT, ngân hàng, Zalo...)
- Hosting model (On-premise / Odoo.sh / Odoo Online — xem `odoo-licensing-deployment-guide.md`)

[SƠ ĐỒ KIẾN TRÚC — chèn diagram tại đây]

Mô tả luồng chính:
1. [vd: Khách đặt hàng trên Website → tạo Sales Order → trừ tồn kho Inventory]
2. [vd: Sales Order xác nhận → tự động tạo hóa đơn → đẩy sang phần mềm e-invoice qua tích hợp]
3. ...]

---

### 7. Lộ trình triển khai theo Phase

| Phase | Tên Phase | Nội dung chính | Thời gian dự kiến | Điều kiện go-live |
|---|---|---|---|---|
| Phase 0 | Chuẩn bị | Setup hạ tầng, cấu hình công ty, phân quyền cơ bản | [X tuần] | — |
| Phase 1 | [vd: Sales - Kho - Kế toán cơ bản] | Cấu hình + customize Must-have, data migration master data | [X tuần] | UAT pass cho các quy trình core |
| Phase 2 | [vd: Tích hợp + module nâng cao] | Các hạng mục Should-have, tích hợp 3rd-party | [X tuần] | — |
| Phase 3 (nếu có) | [vd: Mở rộng/Phase 2 theo Fit-Gap] | Các hạng mục Could-have / Out of scope đã đưa vào roadmap | [Sau go-live X tháng] | — |

> Phasing nên ưu tiên theo MoSCoW (`presales-fit-gap-analysis-guide.md` Mục 6): Must-have luôn nằm ở Phase 1, Should-have có thể đẩy sang Phase 1.5/2 nếu effort cao.

---

*Tài liệu này là Technical Proposal, không thay thế SOW. Phạm vi chính thức ràng buộc hợp đồng được quy định tại SOW đính kèm.*
```

---

## 3. Commercial Proposal / Quotation — Cấu trúc & Template

Commercial Proposal trả lời câu hỏi: *"Tổng chi phí bao nhiêu, gồm những gì, thanh toán ra sao?"* Đây là tài liệu **người duyệt ngân sách** đọc kỹ nhất — cần rõ ràng, không có hạng mục "ẩn", và luôn ghi rõ thời hạn hiệu lực.

```markdown
# COMMERCIAL PROPOSAL / BÁO GIÁ
## Triển khai Odoo cho [Tên khách hàng]

**Số báo giá:** [Mã số]
**Ngày:** [DD/MM/YYYY]
**Hiệu lực đến:** [DD/MM/YYYY] — *(thường 30 ngày kể từ ngày phát hành)*

---

### 1. Chi phí License

[Tham chiếu `odoo-licensing-deployment-guide.md` để xác định loại license (Odoo Enterprise
subscription theo user, hoặc One App Free nếu chỉ dùng 1 app Enterprise) và đơn giá hiện hành.]

| Hạng mục | Số lượng | Đơn giá/năm | Thành tiền/năm | Ghi chú |
|---|---|---|---|---|
| Odoo Enterprise Subscription — User chuẩn (Internal User) | [số user] | [đơn giá] | [thành tiền] | Giá theo bảng giá Odoo công bố tại thời điểm báo giá |
| Odoo Enterprise Subscription — User Portal (nếu có) | [số user] | [đơn giá] | [thành tiền] | Thường miễn phí hoặc giá thấp hơn nhiều |
| **Tổng chi phí License/năm** | | | **[tổng]** | Thanh toán theo chu kỳ Odoo quy định (thường hàng năm, trả trước) |

> ⚠️ Chi phí License do **Odoo S.A. thu trực tiếp hoặc qua Partner** — đối tác triển khai **không** được tự ý thay đổi đơn giá. Luôn lấy giá mới nhất tại thời điểm chốt báo giá.

---

### 2. Chi phí Triển khai (Implementation)

[Breakdown theo Phase và/hoặc theo module — lấy effort từ `presales-effort-estimation-guide.md`,
đã áp hệ số điều chỉnh (Mục 7) và buffer (Mục 8) của tài liệu đó.]

| Phase | Hạng mục | Effort (man-day) | Đơn giá (man-day) | Thành tiền |
|---|---|---|---|---|
| Phase 1 | Cấu hình Sales/Kho/Kế toán cơ bản | [X] | [rate] | [thành tiền] |
| Phase 1 | Customization: [tên hạng mục, mã FG-xxx] | [X] | [rate] | [thành tiền] |
| Phase 1 | Data migration master data | [X] | [rate] | [thành tiền] |
| Phase 2 | Tích hợp [tên hệ thống] | [X] | [rate] | [thành tiền] |
| Phase 2 | Customization: [tên hạng mục, mã FG-xxx] | [X] | [rate] | [thành tiền] |
| | Project Management & QA (toàn dự án) | [X] | [rate] | [thành tiền] |
| **Tổng chi phí Triển khai** | | | | **[tổng]** |

> Cột "Effort" và "Đơn giá" có thể **gộp lại thành 1 cột "Trọn gói (fixed price)"** nếu công ty áp dụng chính sách fixed-price thay vì time & material — tuỳ chính sách kinh doanh.

---

### 3. Chi phí Đào tạo

| Hạng mục | Số buổi/nhóm | Đơn giá | Thành tiền |
|---|---|---|---|
| Đào tạo nhóm Sales/CRM | [X buổi] | [đơn giá] | [thành tiền] |
| Đào tạo nhóm Kho | [X buổi] | [đơn giá] | [thành tiền] |
| Đào tạo nhóm Kế toán | [X buổi] | [đơn giá] | [thành tiền] |
| Đào tạo Admin/IT (quản trị hệ thống) | [X buổi] | [đơn giá] | [thành tiền] |
| **Tổng chi phí Đào tạo** | | | **[tổng]** |

> Có thể gộp vào "Chi phí Triển khai" ở Mục 2 nếu công ty không tách riêng dòng này — nhưng nên **tách riêng** để khách thấy rõ giá trị đào tạo (dễ giữ lại hạng mục này khi khách yêu cầu cắt giảm chi phí).

---

### 4. Chi phí Support/Maintenance sau Go-live

| Hạng mục | Mô tả | Chi phí |
|---|---|---|
| Gói Support [tên gói — vd "Standard"] | [X]% / năm trên giá trị [License + Implementation] | [thành tiền/năm] |
| SLA cam kết | [vd: phản hồi trong 4h, xử lý sự cố nghiêm trọng trong 24h] | — |
| Phạm vi | [vd: hỗ trợ vận hành, sửa lỗi phát sinh, KHÔNG bao gồm phát triển tính năng mới] | — |

> Mức phổ biến tại VN: **15-20%/năm** trên giá trị (License + Implementation), tuỳ SLA. Năm đầu tiên đôi khi được **tặng kèm** (miễn phí 3-6 tháng đầu sau go-live) như 1 điểm cộng thương lượng.

---

### 5. Chi phí Hosting

[Chỉ điền nếu khách chọn Odoo.sh hoặc Odoo Online — nếu On-premise, ghi rõ
khách tự chịu chi phí hạ tầng (server, backup) và ghi chú tham chiếu `odoo-licensing-deployment-guide.md`.]

| Hạng mục | Gói | Chi phí/tháng hoặc /năm |
|---|---|---|
| Odoo.sh — [tên gói: Tier 1/2/3] | [Mô tả tài nguyên: CPU/RAM/storage] | [chi phí] |
| Backup & Disaster Recovery | [Theo gói Odoo.sh hoặc bổ sung] | [chi phí nếu có] |

---

### 6. Hạng mục tùy chọn (Optional / báo giá riêng)

| Hạng mục | Lý do tách riêng | Trạng thái |
|---|---|---|
| Tích hợp [tên bên thứ 3 — vd cổng thanh toán, SMS gateway] | Chi phí license/API do bên thứ 3 quy định, đối tác chỉ báo phí tích hợp | Báo giá riêng khi khách xác nhận chọn nhà cung cấp |
| [Hạng mục Could-have/Phase 2 từ Fit-Gap] | Ngoài phạm vi giai đoạn 1, đưa vào khi khách quyết định mở rộng | Tham khảo, chưa tính vào tổng |

---

### 7. Tổng hợp chi phí

| Hạng mục | Năm 1 | Từ năm 2 |
|---|---|---|
| License (Mục 1) | [X]/năm | [X]/năm |
| Triển khai (Mục 2) | [X] (1 lần) | — |
| Đào tạo (Mục 3) | [X] (1 lần) | — |
| Support/Maintenance (Mục 4) | [X]/năm (hoặc miễn phí nếu tặng kèm) | [X]/năm |
| Hosting (Mục 5, nếu có) | [X]/năm | [X]/năm |
| **TỔNG (chưa gồm VAT)** | **[tổng năm 1]** | **[tổng từ năm 2]** |

*Báo giá trên chưa bao gồm VAT [X]% theo quy định hiện hành.*

---

### 8. Điều khoản thanh toán

[Chọn 1 trong các mẫu phổ biến tại VN, hoặc tuỳ chỉnh theo thoả thuận:]

**Mẫu A — Theo % tiến độ tổng thể (phổ biến với dự án ngắn, 1 phase):**
- Đợt 1 (tạm ứng, ký hợp đồng): 30%
- Đợt 2 (hoàn thành UAT): 40%
- Đợt 3 (go-live + nghiệm thu): 30%

**Mẫu B — Theo Milestone từng Phase (phổ biến với dự án nhiều Phase):**

| Milestone | % thanh toán | Điều kiện |
|---|---|---|
| Ký hợp đồng | [X]% | Tạm ứng |
| Hoàn thành Phase 1 — UAT pass | [X]% | Biên bản nghiệm thu UAT Phase 1 |
| Go-live Phase 1 | [X]% | Biên bản go-live |
| Hoàn thành Phase 2 — UAT pass | [X]% | Biên bản nghiệm thu UAT Phase 2 |
| Go-live Phase 2 + nghiệm thu cuối | [X]% | Biên bản nghiệm thu tổng thể |

> License và Hosting (nếu qua đối tác) thường thanh toán **riêng theo chu kỳ Odoo/Odoo.sh** (hàng năm, trả trước), không gộp vào lịch thanh toán Triển khai.

---

*Báo giá có hiệu lực đến hết ngày [DD/MM/YYYY]. Phạm vi chi tiết, deliverables và timeline chính thức được quy định tại SOW đính kèm.*
```

---

## 4. SOW (Statement of Work) — Cấu trúc & Template

SOW là **phụ lục hợp đồng** — văn bản duy nhất trong bộ 3 có giá trị ràng buộc pháp lý đầy đủ về scope, timeline, trách nhiệm. Mọi điều khoản mơ hồ trong SOW đều có thể trở thành tranh chấp khi go-live trễ hoặc phát sinh chi phí.

```markdown
# STATEMENT OF WORK (SOW)
## Phụ lục Hợp đồng triển khai Odoo — [Tên khách hàng]

**Số SOW:** [Mã số] | **Đính kèm Hợp đồng số:** [Mã hợp đồng]
**Ngày hiệu lực:** [DD/MM/YYYY]

---

### 1. Deliverables theo từng Phase

| Phase | Deliverable | Mô tả | Định dạng bàn giao |
|---|---|---|---|
| Phase 1 | Hệ thống Odoo đã cấu hình (Sales/Kho/Kế toán) | Theo đúng Fit-Gap đã sign-off, mã FG-001 đến FG-0xx | Môi trường UAT + Production |
| Phase 1 | [Customization #1 — mã FG-xxx] | [Mô tả deliverable] | Module cài trên Production |
| Phase 1 | Tài liệu hướng dẫn sử dụng (User Manual) | Theo từng vai trò người dùng | File PDF/Wiki |
| Phase 1 | Báo cáo migration | Đối chiếu số liệu cũ vs mới | File Excel đối chiếu |
| Phase 2 | [Tích hợp #1 — mã FG-xxx] | [Mô tả deliverable] | Kết nối live với hệ thống đối tác |

---

### 2. Timeline & Milestones

| # | Milestone | Ngày dự kiến | Phụ thuộc (Dependency) |
|---|---|---|---|
| M1 | Kick-off & xác nhận môi trường | [Tuần 1] | Khách cung cấp danh sách user, hạ tầng (nếu on-premise) |
| M2 | Hoàn thành cấu hình + customization Phase 1 | [Tuần X] | — |
| M3 | UAT Phase 1 | [Tuần X+2] | Khách bố trí người dùng test theo lịch |
| M4 | Go-live Phase 1 | [Tuần X+4] | UAT pass + dữ liệu migration đã đối chiếu |
| M5 | Hoàn thành tích hợp + customization Phase 2 | [Tuần X+8] | — |
| M6 | UAT & Go-live Phase 2 | [Tuần X+10] | — |
| M7 | Kết thúc giai đoạn bảo hành | [Go-live + X tháng] | — |

> Mỗi mốc trễ do **phía khách** (chậm cung cấp data, chậm phản hồi UAT) có thể làm dịch các mốc tiếp theo tương ứng — ghi rõ điều khoản này để tránh đối tác chịu phạt trễ tiến độ do nguyên nhân khách quan.

---

### 3. Bảng RACI — Trách nhiệm 2 bên

| Hạng mục | Khách hàng | Đối tác triển khai |
|---|---|---|
| Cung cấp dữ liệu master data (KH/NCC/SP) theo template chuẩn | **R/A** — chuẩn bị, làm sạch, cung cấp đúng hạn | C — cung cấp template, hướng dẫn chuẩn hoá |
| Quyết định nghiệp vụ (vd phê duyệt công thức tính giá, workflow duyệt) | **A** — người có thẩm quyền quyết định trong [X ngày làm việc] | R — đề xuất phương án, tư vấn |
| Bố trí người dùng tham gia UAT theo lịch | **R** — đúng số lượng, đúng vai trò, đúng lịch | C — chuẩn bị kịch bản test, hỗ trợ trong buổi UAT |
| Hạ tầng (nếu On-premise: server, network, SSL) | **R/A** | C — tư vấn cấu hình tối thiểu |
| Cấu hình hệ thống Odoo theo Fit-Gap | I | **R/A** |
| Phát triển customization/tích hợp | I | **R/A** |
| Đào tạo người dùng cuối | C — bố trí người tham gia | **R/A** — chuẩn bị tài liệu, thực hiện đào tạo |
| Vận hành & support sau go-live (trong giai đoạn bảo hành) | I | **R/A** — theo SLA Mục 4 Commercial Proposal |

*(R = Responsible — người thực hiện, A = Accountable — người chịu trách nhiệm cuối cùng/duyệt, C = Consulted — được hỏi ý kiến, I = Informed — được thông báo)*

---

### 4. Assumptions (Giả định)

[Liệt kê các điều kiện mà ước lượng effort/timeline dựa vào — nếu điều kiện
thay đổi, effort/timeline cần điều chỉnh tương ứng (xem Mục 6 - Change Request).]

- Số lượng user: [X user Internal, Y user Portal] — theo đúng số đã báo giá License.
- Dữ liệu master data do khách cung cấp đã được chuẩn hoá theo template Odoo, không cần xử lý merge từ nhiều nguồn ngoài phạm vi đã nêu ở Mục 5 Fit-Gap.
- Khách phản hồi các yêu cầu quyết định nghiệp vụ trong vòng [X ngày làm việc].
- Hạ tầng (nếu On-premise) đáp ứng yêu cầu cấu hình tối thiểu do đối tác cung cấp trước [mốc thời gian].
- Phạm vi customization giới hạn theo đúng Functional Spec được duyệt cho từng hạng mục mã FG-xxx.

---

### 5. Out of Scope

[Lấy TRỰC TIẾP các dòng ⏸️ Out of scope / Won't-have từ bảng Fit-Gap đã sign-off —
đây là phần quan trọng nhất để tránh tranh chấp "tại sao Odoo không làm được X".]

| Mã (theo Fit-Gap) | Hạng mục | Lý do | Ghi chú |
|---|---|---|---|
| FG-008 | [vd: Dự báo nhu cầu bằng AI] | Chưa cấp thiết / để Phase 2 | Có thể đưa vào Change Request hoặc hợp đồng Phase 2 riêng |
| FG-0xx | [Hạng mục khác] | [Lý do] | — |

> Ngoài các dòng từ Fit-Gap, bổ sung các loại trừ chung thường gặp:
> - Không bao gồm việc viết lại quy trình nghiệp vụ (BPR) ngoài phạm vi đã thống nhất tại Fit-Gap.
> - Không bao gồm chi phí bản quyền phần mềm bên thứ 3 (đã nêu tại Mục 6 Commercial Proposal — "Hạng mục tùy chọn").
> - Không bao gồm đào tạo bổ sung ngoài số buổi đã nêu tại Mục 3 Commercial Proposal.

---

### 6. Quy trình Change Request (Yêu cầu thay đổi scope)

1. **Đề xuất**: Bên đề xuất (khách hoặc đối tác) gửi **Change Request Form** mô tả: hạng mục mới/thay đổi, lý do, mức độ ưu tiên.
2. **Đánh giá**: Đối tác đánh giá impact trong [X ngày làm việc] — ước lượng effort bổ sung (theo `presales-effort-estimation-guide.md`) và impact lên timeline các milestone còn lại.
3. **Phê duyệt**: Khách xác nhận bằng văn bản (email hoặc ký Change Request Form) trước khi đối tác bắt đầu thực hiện.
4. **Định giá**: Effort bổ sung tính theo rate card đã thống nhất trong Commercial Proposal (Mục 9, `presales-effort-estimation-guide.md`) — không áp dụng giá ưu đãi của gói trọn gói ban đầu trừ khi 2 bên thoả thuận khác.
5. **Cập nhật**: Sau khi hoàn thành, Change Request được đính kèm SOW như 1 phụ lục bổ sung.

---

### 7. Acceptance Criteria theo từng Milestone

| Milestone | Tiêu chí nghiệm thu |
|---|---|
| M3 — UAT Phase 1 | Tất cả test case trong kịch bản UAT (do đối tác chuẩn bị, khách xác nhận trước) đạt **Pass**; các lỗi mức "Critical/Blocker" = 0; lỗi mức "Minor" có kế hoạch fix rõ ràng |
| M4 — Go-live Phase 1 | Hệ thống vận hành ổn định trong [X ngày] đầu tiên không phát sinh sự cố Critical; dữ liệu migration đã đối chiếu khớp với báo cáo Mục 1 (Deliverables) |
| M6 — Go-live Phase 2 | Tương tự M4, áp dụng cho phạm vi Phase 2 |
| M7 — Kết thúc bảo hành | Không còn lỗi tồn đọng (open bug) thuộc phạm vi đã bàn giao; bàn giao tài liệu vận hành đầy đủ |

---

### 8. Bảo hành & Hỗ trợ sau Go-live

- **Thời hạn bảo hành**: [X tháng] kể từ ngày Go-live của từng Phase (tính riêng cho mỗi Phase).
- **Phạm vi bảo hành**: sửa lỗi phát sinh từ customization/cấu hình do đối tác thực hiện, **KHÔNG bao gồm**:
  - Lỗi do khách tự thay đổi cấu hình/customization sau go-live mà không thông báo.
  - Yêu cầu tính năng mới (xử lý qua Change Request, Mục 6).
  - Lỗi từ bản thân Odoo core (báo lên Odoo S.A. nếu có Enterprise Support, hoặc cộng đồng nếu Community).
- **Sau thời hạn bảo hành**: chuyển sang gói Support/Maintenance đã thoả thuận tại Mục 4 Commercial Proposal.

---

*SOW này là phụ lục không tách rời của Hợp đồng số [Mã hợp đồng]. Mọi thay đổi đối với SOW phải được thực hiện qua Quy trình Change Request (Mục 6) và xác nhận bằng văn bản bởi đại diện có thẩm quyền của 2 bên.*
```

---

## 5. ROI / Giá trị mang lại — Talking points

Phần "giá trị mang lại" là nội dung **thuyết phục nhất** trong Technical/Commercial Proposal — nhưng cũng là phần **dễ bị lạm dụng nhất** nếu dùng số liệu không có căn cứ. Dùng template "before vs after" dưới đây, **chỉ điền số liệu khách tự cung cấp trong Discovery** (Mục 4 Discovery Notes — tình trạng hiện tại).

```markdown
### Giá trị mang lại (ước tính dựa trên thông tin khách cung cấp)

| Quy trình | Hiện tại (Before) | Sau triển khai (After — ước tính) | Cơ sở ước tính |
|---|---|---|---|
| Thời gian xử lý 1 đơn hàng (từ lúc nhận yêu cầu đến khi xuất hóa đơn) | [X giờ — số khách cung cấp] | [Y giờ — ước tính] | Loại bỏ bước nhập liệu trùng lặp giữa [hệ thống A] và [hệ thống B] (theo mô tả Discovery Mục [#]) |
| Thời gian chốt sổ cuối tháng (kế toán) | [X ngày] | [Y ngày] | Đối chiếu công nợ/tồn kho tự động thay vì tổng hợp Excel thủ công |
| Tỷ lệ tồn kho dư thừa / chậm luân chuyển | [Z%] | [giảm ước tính] | Báo cáo tồn kho real-time + cảnh báo min/max stock |
| Thời gian có báo cáo quản trị (doanh số, công nợ, tồn kho) | [X — vd "chờ kế toán tổng hợp cuối tuần"] | Real-time / theo yêu cầu | Dashboard tích hợp dữ liệu trực tiếp từ các module |
| [Quy trình khác đặc thù theo khách] | [X] | [Y] | [Cơ sở] |

> ⚠️ **QUY TẮC BẮT BUỘC**: cột "Hiện tại (Before)" PHẢI lấy từ số liệu khách tự nói trong Discovery (ghi rõ nguồn — vd "theo anh A, Trưởng phòng Kế toán, trao đổi ngày .../.../..."). Cột "Sau triển khai" là **ước tính có căn cứ** (giải thích ngắn gọn ở cột "Cơ sở ước tính"), KHÔNG cam kết bằng số tuyệt đối trừ khi đó là 1 KPI đã thống nhất tại Acceptance Criteria của SOW.
>
> Nếu khách **chưa cung cấp số liệu cụ thể** ở bất kỳ dòng nào, để trống hoặc ghi "Sẽ đo lường sau khi go-live (baseline)" — KHÔNG bịa số để bảng "đẹp" hơn. Một bảng ROI với 2-3 dòng có số liệu thật đáng tin hơn nhiều so với 1 bảng đầy đủ nhưng số liệu không kiểm chứng được.
```

---

## 6. Hồ sơ năng lực & Đấu thầu (DNNN/cơ quan nhà nước)

Khi khách hàng là **Doanh nghiệp Nhà nước (DNNN)** hoặc cơ quan nhà nước, quy trình mua sắm thường qua **đấu thầu** — khác đáng kể so với bộ Proposal/SOW thông thường ở trên về cấu trúc, thủ tục và tiêu chí đánh giá.

### 6.1. Hồ sơ năng lực (Company Profile / Capability Statement)

Tài liệu **giới thiệu chung**, dùng cho mọi cơ hội (không chỉ đấu thầu) — chuẩn bị sẵn 1 bản và cập nhật định kỳ:

- **Giới thiệu công ty**: lịch sử thành lập, quy mô nhân sự, đối tác công nghệ (vd Odoo Official Partner — ghi rõ cấp độ Partner nếu có: Silver/Gold/Ready).
- **Chứng chỉ**: chứng chỉ Odoo (Functional/Technical Certification của từng consultant chủ chốt), ISO (nếu có, đặc biệt ISO 9001 cho quy trình triển khai, ISO 27001 cho bảo mật — thường là điểm cộng/yêu cầu bắt buộc trong đấu thầu).
- **Case study / Dự án tham chiếu**: 3-5 dự án tiêu biểu, ưu tiên **cùng ngành** hoặc **quy mô tương đương** với khách đang chào — mỗi case study nêu: bài toán, giải pháp, kết quả (nếu có số liệu được khách cũ đồng ý công bố).
- **Đội ngũ**: sơ đồ tổ chức đội triển khai điển hình (PM, Functional Consultant, Technical Developer), kinh nghiệm trung bình.

### 6.2. Hồ sơ dự thầu (Bidding Documents) — khác biệt so với Proposal thông thường

| Khía cạnh | Proposal thông thường | Hồ sơ dự thầu |
|---|---|---|
| Cấu trúc | Linh hoạt theo template ở Mục 2-4 | **Bắt buộc theo mẫu** trong Hồ sơ mời thầu (HSMT/RFP) — sai cấu trúc có thể bị loại |
| Thời hạn | Linh hoạt | **Tuyệt đối** — nộp trễ dù 1 phút cũng bị loại |
| Bảo lãnh dự thầu (Bid Bond) | Không áp dụng | Thường yêu cầu — 1 khoản tiền/bảo lãnh ngân hàng (thường 1-3% giá dự thầu), bị mất nếu trúng thầu mà không ký hợp đồng |
| Hồ sơ pháp lý đính kèm | Không bắt buộc | Bắt buộc: Giấy phép kinh doanh, BCTC 2-3 năm gần nhất, chứng chỉ năng lực, hợp đồng tương tự đã thực hiện (có xác nhận của chủ đầu tư cũ) |
| Cách trình bày giá | Tổng hợp, có thể đàm phán | **Đơn giá chi tiết theo từng hạng mục** trong Bảng tiên lượng/Dự toán (Bill of Quantities) — không được tự ý gộp dòng |

### 6.3. Tiêu chí đánh giá: Kỹ thuật vs Tài chính

Hầu hết gói thầu CNTT đánh giá theo **2 bước, có thang điểm**:

1. **Đánh giá kỹ thuật (thường 60-80% trọng số)**: chấm điểm theo từng tiêu chí trong HSMT — vd "Giải pháp đáp ứng yêu cầu nghiệp vụ" (map từ Fit-Gap), "Kinh nghiệm đội dự án", "Phương pháp luận triển khai", "Cam kết tiến độ/bảo hành". Phải đạt **điểm sàn kỹ thuật** (vd ≥ 70/100) mới được mở Hồ sơ tài chính.
2. **Đánh giá tài chính (phần trọng số còn lại)**: thường chấm theo công thức (giá thấp nhất / giá dự thầu) × điểm tối đa — nhà thầu giá thấp nhất được điểm tài chính cao nhất.
3. **Điểm tổng hợp** = Điểm kỹ thuật × trọng số KT + Điểm tài chính × trọng số TC → nhà thầu điểm tổng cao nhất và đáp ứng đủ điều kiện pháp lý/năng lực sẽ trúng thầu.

> 💡 **Lưu ý cho PreSale**: với khách DNNN, áp hệ số điều chỉnh "tài liệu/quy trình bài bản" (x1.1-1.3) ở `presales-effort-estimation-guide.md` Mục 7 — vì khối lượng tài liệu (Functional Spec, Test Case, biên bản nghiệm thu từng bước) thường nhiều hơn đáng kể so với khách thương mại thông thường, và quy trình phê duyệt nội bộ của khách (qua nhiều cấp/ban) cũng kéo dài timeline.

---

## Liên kết

- **Nguồn input bắt buộc**: `presales-fit-gap-analysis-guide.md` — bảng Fit-Gap đã sign-off là nguồn của mục "Giải pháp đề xuất" (Technical Proposal Mục 3), "Customization & Tích hợp" (Mục 5), và "Out of Scope" (SOW Mục 5).
- **Effort & chi phí triển khai**: `presales-effort-estimation-guide.md` — dùng cho Commercial Proposal Mục 2 và Change Request (SOW Mục 6).
- **Chi phí License & lựa chọn Hosting**: `odoo-licensing-deployment-guide.md` — dùng cho Commercial Proposal Mục 1 và Mục 5, Technical Proposal Mục 6 (kiến trúc/hosting).
- **Luận điểm khác biệt hoá vs đối thủ** (SAP, Oracle NetSuite, phần mềm Việt...): `presales-competitor-comparison-guide.md` — hữu ích khi viết Executive Summary của Technical Proposal hoặc trả lời câu hỏi "vì sao chọn Odoo" trong hồ sơ dự thầu.
- **Tra cứu App/tính năng** khi soạn Mục 3-4 Technical Proposal: `odoo-app-feature-matrix.md`.
