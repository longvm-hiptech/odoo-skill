# Đánh giá & Roadmap: Bộ Skills cho PreSale Odoo

> Tài liệu đánh giá (chưa triển khai) — phân tích bộ skill hiện có và đề xuất bộ skill mới phục vụ bộ phận **PreSale** (tư vấn giải pháp / khảo sát / báo giá) cho thị trường Việt Nam.

---

## 1. Tóm tắt

Bộ skill hiện tại (`skills/`, `agents/`, `commands/`) gồm **115 file**, phục vụ **100% cho Developer/Technical** (sinh module, pattern model/view/security, OWL, testing, nâng cấp version...). **Chưa có bất kỳ skill nào phục vụ quy trình PreSale** (khảo sát yêu cầu, demo, fit-gap, báo giá, cạnh tranh, localization VN).

Đề xuất: bổ sung **14 skill files mới** (chia 7 nhóm A–G), ưu tiên các nhóm *Solution Mapping*, *Discovery*, *Proposal/Costing* và *Localization VN* — vì đây là 4 nhóm tạo giá trị nhanh nhất và lấp khoảng trống lớn nhất. Ngoài ra đề xuất 1 agent role mới (`odoo-presales-consultant`) và 3 slash command cho giai đoạn tích hợp sau.

---

## 2. Hiện trạng bộ skill (115 file)

| Nhóm hiện có | Số file (~) | Đối tượng |
|---|---|---|
| Core dev patterns (model, security, module generator, OWL — theo version 14-19) | ~45 | Developer |
| Domain modules (sale-crm, accounting, purchase, stock, hr, project, pricing, product, tax, uom...) | ~12 | Developer |
| Frontend/UI (xml-view, qweb, widget, menu, assets, portal) | ~6 | Developer |
| Workflow/business logic (state machine, onchange, cron, computed field, domain) | ~6 | Developer |
| Data/Integration (external API, import/export, migration, attachment, GitHub verify) | ~5 | Developer |
| Testing/QA, Performance, Troubleshooting | ~6 | Developer |
| Reference/orchestration (agent quick-start, workflow orchestrator, version knowledge...) | ~9 | Developer (AI agent) |
| `odoo-editions.md` (Community vs Enterprise) | 1 | Dev, có thể tái dùng cho PreSale |

→ **Kết luận:** `odoo-editions.md` là file **gần nhất** với nhu cầu PreSale (so sánh edition), nhưng viết theo góc nhìn "dev nên depend module nào", chưa có góc nhìn "bán được gì, giá bao nhiêu, demo thế nào". `sale-crm-patterns.md` hữu ích khi *deal* liên quan đến CRM/Sales nhưng không bao quát toàn bộ quy trình PreSale.

---

## 3. Quy trình PreSale Odoo điển hình & khoảng trống

| Bước quy trình | Mô tả | Skill hỗ trợ hiện tại | Gap |
|---|---|---|---|
| 1. Lead Qualification | Phân loại KH theo quy mô, ngành, hệ thống đang dùng, ngân sách | Không có | ❌ |
| 2. Discovery Workshop | Khảo sát quy trình nghiệp vụ từng phòng ban | Không có | ❌ |
| 3. Solution Mapping | Map nhu cầu → Odoo Apps, chọn Community/Enterprise | `odoo-editions.md` (1 phần) | ⚠️ thiếu "feature matrix" đầy đủ |
| 4. Demo | Dựng demo data + kịch bản theo ngành | Không có | ❌ |
| 5. Fit-Gap Analysis | Báo cáo Fit/Gap chính thức trước khi báo giá | Không có | ❌ |
| 6. Effort Estimation & Costing | Ước lượng man-day & chi phí | Không có | ❌ |
| 7. Proposal/SOW & Đàm phán | Tài liệu đề xuất kỹ thuật + thương mại | Không có | ❌ |
| 8. Đối thủ cạnh tranh | So sánh Odoo vs SAP B1/Misa/Fast/Bravo... | Không có | ❌ |
| 9. Localization VN (kế toán/hoá đơn điện tử) | Trả lời câu hỏi pháp lý/thuế VN | Không có (chỉ có pattern code, không có góc nhìn compliance) | ❌ |
| 10. Bàn giao cho Dev team | Chuyển Proposal → `REQUIREMENT_SPEC.md` cho `odoo-planner` | `agents/odoo-planner.md` (phía nhận) | ⚠️ thiếu "cầu nối" phía PreSale |

---

## 4. Đề xuất 14 skill files mới

### Bảng tổng hợp

| # | File đề xuất | Nhóm | Ưu tiên |
|---|---|---|---|
| A1 | `presales-discovery-questionnaire.md` | Discovery | 🔴 Cao |
| B1 | `odoo-app-feature-matrix.md` | Solution Mapping | 🔴 Cao (quan trọng nhất) |
| B2 | `presales-fit-gap-analysis-guide.md` | Solution Mapping | 🔴 Cao |
| B3 | `presales-industry-solution-templates.md` | Solution Mapping | 🟡 Trung bình |
| C1 | `presales-demo-environment-guide.md` | Demo | 🟡 Trung bình |
| D1 | `presales-proposal-sow-templates.md` | Proposal | 🔴 Cao |
| D2 | `presales-effort-estimation-guide.md` | Proposal | 🔴 Cao |
| D3 | `odoo-licensing-deployment-guide.md` | Proposal | 🟡 Trung bình |
| E1 | `presales-competitor-comparison-guide.md` | Cạnh tranh | 🟡 Trung bình |
| F1 | `l10n-vietnam-compliance-guide.md` | VN Localization | 🔴 Cao |
| F2 | `vietnam-integration-landscape.md` | VN Localization | 🟡 Trung bình |
| F3 | `presales-glossary-vi.md` | VN Localization | 🟢 Thấp |
| G1 | `presales-data-migration-scoping-guide.md` | Migration & Handoff | 🟡 Trung bình |
| G2 | `presales-to-implementation-handoff-guide.md` | Migration & Handoff | 🔴 Cao |

---

### Nhóm A — Discovery & Requirements Gathering

**A1. `presales-discovery-questionnaire.md`** — 🔴 Cao
- **Mục đích:** Bộ câu hỏi khảo sát có cấu trúc theo từng phòng ban/quy trình, giúp PreSale thu thập đủ thông tin để map sang Odoo Apps mà không bỏ sót.
- **Nội dung chính:**
  - Câu hỏi chung: quy mô DN, số user, hệ thống đang dùng (Excel/Misa/Fast/SAP...), pain points hiện tại
  - Bộ câu hỏi theo module (Sales/CRM, Mua hàng, Kho/Logistics, Sản xuất, Kế toán/Tài chính, Nhân sự, Dự án): quy trình hiện tại, case đặc biệt, báo cáo cần có, tích hợp cần có
  - Checklist "red flags" — yêu cầu thường dẫn tới custom dev lớn (workflow duyệt nhiều cấp phức tạp, tính giá đặc thù, tích hợp hệ thống legacy...)
  - Output template "Discovery Notes" → input cho B2
- **Liên quan:** `sale-crm-patterns.md`, các domain pattern files (purchase/stock/hr/accounting/project) để biết Odoo hỗ trợ sẵn gì.

---

### Nhóm B — Solution Mapping (nền tảng)

**B1. `odoo-app-feature-matrix.md`** — 🔴 Cao (file nền tảng, quan trọng nhất)
- **Mục đích:** "Từ điển" toàn bộ Apps Odoo (Sales, CRM, Inventory, MRP, Accounting, Invoicing, HR suite, Project, Timesheet, Helpdesk, Field Service, Subscriptions, Rental, POS, eCommerce, Website, Marketing Automation, Studio, Sign, Documents, Knowledge, Planning, Quality, Maintenance, Approvals...).
- **Nội dung chính:**
  - Bảng: App | Nhóm | Community/Enterprise | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Ngành thường dùng
  - Mapping ngược "Khách nói X → App/feature Y" (vd: "quản lý lô/hạn dùng" → Inventory + Lot/Serial)
  - Liên kết tới skill kỹ thuật tương ứng (vd Inventory → `stock-inventory-patterns.md`) để khi cần demo sâu, biết tra tài liệu nào
- **Liên quan:** Kế thừa & mở rộng `odoo-editions.md` (thêm góc nhìn "bán được gì" thay vì chỉ "dev cần gì").

**B2. `presales-fit-gap-analysis-guide.md`** — 🔴 Cao
- **Mục đích:** Phương pháp luận + template chuẩn cho buổi Fit-Gap Workshop — tài liệu quan trọng nhất khách hàng nhận trước khi ký hợp đồng.
- **Nội dung chính:**
  - Quy trình chạy workshop (ai tham gia, thời lượng, cách ghi nhận)
  - Template bảng Fit-Gap: Mã yêu cầu | Mô tả | Phòng ban | Ưu tiên (Must/Should/Could) | Đánh giá (Fit/Partial-Config/Gap-Custom/Gap-3rd-party) | Giải pháp đề xuất | Effort ước tính (link D2)
  - Cách phân loại Gap → Customize / đổi quy trình / tích hợp bên thứ 3
  - Output → input trực tiếp cho D1 (Proposal) và G2 (Handoff)
- **Liên quan:** B1 (đánh giá Fit), D2 (effort), G2 (handoff).

**B3. `presales-industry-solution-templates.md`** — 🟡 Trung bình
- **Mục đích:** Blueprint giải pháp dựng sẵn theo ngành phổ biến tại VN — demo nhanh, định hướng phạm vi ngay từ đầu.
- **Nội dung chính** (mỗi ngành: Phân phối/Thương mại, Sản xuất, Bán lẻ/F&B, Xây dựng & Dự án, Dịch vụ chuyên nghiệp, Xuất nhập khẩu/Logistics):
  - Combo Apps đề xuất (core + optional)
  - Quy trình nghiệp vụ điển hình (sơ đồ luồng ngắn)
  - Customization thường gặp với ngành đó
  - Đối thủ chuyên ngành (link E1)
- **Liên quan:** B1, E1, F2.

---

### Nhóm C — Demo

**C1. `presales-demo-environment-guide.md`** — 🟡 Trung bình
- **Mục đích:** Hướng dẫn dựng môi trường demo ấn tượng — database mẫu theo ngành, kịch bản theo persona (CEO, Kế toán trưởng, Trưởng kho...).
- **Nội dung chính:**
  - Cách load/tuỳ biến nhanh demo data Odoo (tên công ty, logo, dữ liệu mẫu tiếng Việt)
  - Kịch bản demo mẫu theo ngành (kết hợp B3): thứ tự thao tác, "wow moments" cần nhấn
  - Checklist chuẩn bị trước demo (data, user, dashboard, mobile app)
  - Dùng Odoo Studio để "demo customize" trực tiếp trước khách
- **Liên quan:** B3, B1.

---

### Nhóm D — Thương mại / Proposal

**D1. `presales-proposal-sow-templates.md`** — 🔴 Cao
- **Mục đích:** Bộ template tài liệu đề xuất chuẩn hoá.
- **Nội dung chính:**
  - Cấu trúc Technical Proposal (Phạm vi, giải pháp theo phòng ban, Apps sử dụng, danh sách customization từ Fit-Gap)
  - Cấu trúc Commercial Proposal/Quotation (license, implementation, training, support/maintenance, hosting)
  - Cấu trúc SOW: Deliverables, Timeline/Milestones, Assumptions, Out-of-scope, Change Request process
  - Mục "ROI/Giá trị" — luận điểm bán hàng định lượng
  - Lưu ý hồ sơ đấu thầu (DNNN/cơ quan nhà nước)
- **Liên quan:** B2 (input), D2, D3, E1.

**D2. `presales-effort-estimation-guide.md`** — 🔴 Cao
- **Mục đích:** Bảng benchmark effort (man-day) cho hạng mục triển khai/customization phổ biến — giúp PreSale tự ước lượng mà không cần hỏi dev mỗi lần.
- **Nội dung chính:**
  - Bảng effort chuẩn: cấu hình module theo app | custom field/view đơn giản | custom report | custom workflow/approval | tích hợp 3rd-party (theo độ phức tạp) | data migration (theo volume)
  - Hệ số điều chỉnh theo version Odoo, kinh nghiệm team, độ rõ ràng yêu cầu
  - Quy đổi effort → giá (rate card mẫu)
  - Buffer/risk contingency khuyến nghị (%)
- **Liên quan:** B2, D1, các skill kỹ thuật để hiểu độ phức tạp thực tế.

**D3. `odoo-licensing-deployment-guide.md`** — 🟡 Trung bình
- **Mục đích:** Mô hình giá Odoo Enterprise (theo user/app), so sánh phương án triển khai & sizing hạ tầng.
- **Nội dung chính:**
  - Cách tính subscription Enterprise (per-user, app-based)
  - So sánh Odoo.sh vs Odoo Online vs On-premise/Self-hosted (chi phí, ai quản trị, khả năng customize, backup/SLA)
  - Sizing theo số user/data volume
  - Lưu ý lưu trữ dữ liệu tại VN (Nghị định 13/2023 về bảo vệ dữ liệu cá nhân) khi tư vấn cloud
- **Liên quan:** Kế thừa `odoo-editions.md`.

---

### Nhóm E — Cạnh tranh

**E1. `presales-competitor-comparison-guide.md`** — 🟡 Trung bình
- **Mục đích:** So sánh Odoo vs đối thủ + "battle card" đối đáp objection thường gặp.
- **Nội dung chính:**
  - Đối thủ quốc tế: SAP Business One, Microsoft Dynamics 365 BC, NetSuite, Salesforce/HubSpot (deal CRM-only)
  - Đối thủ nội địa VN: Misa AMIS, Fast Business/Accounting, Bravo, 1C, 3TSoft, EFFECT...
  - Bảng so sánh theo tiêu chí: TCO, mức độ tuỳ biến, hệ sinh thái apps, support, tốc độ triển khai
  - Battle card: câu trả lời gợi ý cho objection phổ biến ("Odoo support tiếng Việt thế nào?", "Sao đắt hơn Misa?"...)
- **Liên quan:** B3, F1.

---

### Nhóm F — Việt Nam Localization (ưu tiên theo yêu cầu)

**F1. `l10n-vietnam-compliance-guide.md`** — 🔴 Cao
- **Mục đích:** Tổng hợp yêu cầu pháp lý kế toán/thuế VN và mức độ đáp ứng của module `l10n_vn` — câu hỏi gần như luôn gặp trong mọi deal VN.
- **Nội dung chính:**
  - Chuẩn mực kế toán VN (TT200/TT133) — Chart of Accounts mà `l10n_vn` hỗ trợ
  - Hoá đơn điện tử (Nghị định 123/2020 & TT78/2021): yêu cầu pháp lý, các nhà cung cấp tích hợp phổ biến (MISA meInvoice, Viettel S-Invoice, VNPT, BKAV eHoadon, T-VAN...) và hiện trạng kết nối với Odoo (có sẵn / OCA / cần custom)
  - Báo cáo thuế (VAT, TNCN, TNDN) — cái nào Odoo có sẵn, cái nào cần custom report
  - Quy định lưu trữ chứng từ điện tử, chữ ký số
- **Liên quan:** D3 (data residency), G2.

**F2. `vietnam-integration-landscape.md`** — 🟡 Trung bình
- **Mục đích:** Bản đồ tích hợp bên thứ 3 phổ biến trong dự án Odoo tại VN — ước lượng phạm vi tích hợp ngay từ đầu.
- **Nội dung chính:**
  - Hoá đơn điện tử (xem F1)
  - Ngân hàng: sao kê/SMS Banking/Open API (Vietcombank, Techcombank, BIDV, MBBank...)
  - Cổng thanh toán: VNPay, Momo, ZaloPay, OnePay, Payoo
  - Vận chuyển: GHN, GHTK, J&T Express, Viettel Post, Ahamove, Grab/Be
  - Thuế điện tử: kê khai qua eTax/Tổng cục Thuế
  - Social/Sales channel: Zalo OA/ZNS, Facebook/TikTok Shop, Shopee/Lazada
  - Mỗi tích hợp: mức độ sẵn có (có sẵn/OCA/cần code mới), độ phức tạp ước tính (link D2)
- **Liên quan:** D2, F1.

**F3. `presales-glossary-vi.md`** — 🟢 Thấp (nice-to-have)
- **Mục đích:** Từ điển song ngữ Anh-Việt thuật ngữ Odoo/ERP — diễn giải cho khách không rành kỹ thuật, đảm bảo nhất quán tài liệu.
- **Nội dung chính:** Bảng thuật ngữ theo nhóm module (Sales Order = Đơn bán hàng, Quotation = Báo giá, Pick-Pack-Ship = Lấy hàng-Đóng gói-Giao hàng, Landed Cost = Chi phí mua hàng phân bổ...).
- **Liên quan:** Tất cả các nhóm.

---

### Nhóm G — Migration & Handoff

**G1. `presales-data-migration-scoping-guide.md`** — 🟡 Trung bình
- **Mục đích:** Ước lượng phạm vi & effort di chuyển dữ liệu từ hệ thống cũ (Excel, Misa, Fast, phần mềm tự viết).
- **Nội dung chính:**
  - Checklist khảo sát nguồn dữ liệu (loại hệ thống, format export, chất lượng dữ liệu)
  - Danh mục dữ liệu theo ưu tiên (Master data: KH/NCC/SP/tồn đầu kỳ vs Historical data)
  - Yếu tố ảnh hưởng effort: số bản ghi, độ sạch dữ liệu, mapping field phức tạp
  - Template "Data Migration Scope" doc
- **Liên quan:** D2.

**G2. `presales-to-implementation-handoff-guide.md`** — 🔴 Cao
- **Mục đích:** Đóng vòng lặp — chuyển output PreSale (Fit-Gap B2 + Proposal D1) thành `REQUIREMENT_SPEC.md` mà `agents/odoo-planner.md` (đội Dev) sử dụng, tránh thất thoát thông tin.
- **Nội dung chính:**
  - Mapping bảng Fit-Gap → cấu trúc `REQUIREMENT_SPEC.md` (Models, Fields, Workflows, Security, Reports, Integrations — theo format hiện có trong `SKILL.md`/`odoo-planner`)
  - Checklist bàn giao: tài liệu cần có, ai ký-off
  - Mẫu agenda "Handoff Meeting" PreSale ↔ Dev
- **Liên quan:** B2, D1, tham chiếu trực tiếp `agents/odoo-planner.md` và format `REQUIREMENT_SPEC.md` trong `SKILL.md`.

---

## 5. Giai đoạn tiếp theo: Agent + Slash Commands (sau khi có bộ skill)

**`agents/odoo-presales-consultant.md`** (mới) — Role "Senior Odoo Presales Consultant":
1. Discovery (A1, theo ngành B3)
2. Solution Mapping & Fit-Gap (B1, B2)
3. Estimation & Proposal (D1, D2, D3)
4. VN Compliance check (F1, F2) nếu khách VN
5. Output: `REQUIREMENT_SPEC.md` (theo G2) sẵn sàng bàn giao cho `odoo-planner`

**Slash commands đề xuất:**
| Command | Chức năng |
|---|---|
| `/odoo-presales-discovery [industry]` | Sinh bộ câu hỏi khảo sát theo ngành (A1 + B3) |
| `/odoo-fit-gap` | Từ Discovery Notes → bảng Fit-Gap (B2) |
| `/odoo-proposal` | Từ Fit-Gap → draft Proposal/SOW (D1) |

---

## 6. Roadmap triển khai theo Phase

| Phase | Nội dung | Files |
|---|---|---|
| **1 — Nền tảng** | B1, A1, B2, F1 | 4 |
| **2 — Thương mại** | D1, D2, D3 | 3 |
| **3 — Demo & Ngành** | C1, B3, F2 | 3 |
| **4 — Cạnh tranh & Bàn giao** | E1, G1, G2 | 3 |
| **5 — Nice-to-have** | F3 | 1 |
| **6 — Tích hợp Agent/Command** | `agents/odoo-presales-consultant.md` + 3 slash commands + cập nhật `SKILL.md`/`CLAUDE.md` | - |

Phase 1 tạo giá trị nhanh nhất: trả lời được "Odoo có làm được X không, app nào, Community hay Enterprise" (B1), "khảo sát khách thế nào" (A1), "tài liệu Fit-Gap chuẩn" (B2), và câu hỏi VN luôn gặp về kế toán/hoá đơn điện tử (F1).

---

## 7. Cấu trúc thư mục đề xuất

- **Option A (khuyến nghị):** Giữ flat trong `skills/` với prefix `presales-`/`l10n-`/`vietnam-` — nhất quán với 115 file hiện có (toàn bộ đều flat), không cần kiểm tra lại cơ chế discovery của `.claude-plugin/plugin.json`, `hermes-agent.json`, `openclaw-agent.json`, `gemini-extension.json`, `.cursorrules`, `.clinerules`.
- **Option B:** Tạo `skills/presales/` subdirectory — gọn hơn về tổ chức nhưng cần verify các config trên có recurse vào subfolder không trước khi áp dụng.

→ Đề xuất **Option A** cho lần triển khai đầu tiên.

---

## 8. Tích hợp với hệ thống hiện có

- **`SKILL.md`**: Hiện là entry point cho Dev (Odoo 18+). Đề xuất tạo entry point song song (vd `SKILL-PRESALES.md`) hoặc thêm 1 section "PreSale Workflow" trỏ tới `agents/odoo-presales-consultant.md` + skill index nhóm A-G.
- **`CLAUDE.md`**: Thêm dòng vào bảng "Subagent Roles" (mục 3) trỏ tới `agents/odoo-presales-consultant.md`.
- **`README.md`**: Thêm đoạn giới thiệu nhánh PreSale bên cạnh nhánh Dev cho các platform tích hợp khác (Cursor, Hermes, Gemini...).
- **Vòng lặp PreSale ↔ Dev**: G2 là cầu nối bắt buộc — đảm bảo `REQUIREMENT_SPEC.md` do PreSale tạo ra tương thích 100% với input mà `agents/odoo-planner.md` mong đợi (đã đọc và đối chiếu format trong `SKILL.md`).

---

## 9. Next steps đề xuất

1. Review danh sách 14 file — điều chỉnh phạm vi/độ ưu tiên theo thực tế đội PreSale (vd: nếu công ty không tham gia đấu thầu nhà nước, có thể bỏ phần đó trong D1).
2. Bắt đầu với **Phase 1** (B1, A1, B2, F1) — yêu cầu Claude tạo nội dung đầy đủ theo format `skills/SKILL_TEMPLATE.md`.
3. Sau khi có Phase 1-2, đánh giá lại nhu cầu cho Phase 3-6 (demo/ngành, cạnh tranh, agent/command tích hợp).
