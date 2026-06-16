---
name: odoo-licensing-deployment-guide
keywords: [presales, licensing, pricing, odoo.sh, odoo online, on-premise, hosting, deployment, sizing]
description: Mô hình giá Odoo Enterprise, so sánh phương án triển khai (Odoo.sh / Odoo Online / On-premise) và sizing hạ tầng - dùng để xây Commercial Proposal
odoo_versions: [all]
related_skills: [odoo-editions, presales-proposal-sow-templates, presales-effort-estimation-guide, l10n-vietnam-compliance-guide]
---

# Odoo Licensing & Deployment Guide (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  LICENSING & DEPLOYMENT                                                       ║
║  "Bao nhiêu tiền/user? Đặt ở đâu? Server bao to?" — câu hỏi chốt Proposal     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Tài liệu này tập trung vào góc nhìn **thương mại/triển khai** cho PreSale: nguyên tắc tính giá Odoo Enterprise, so sánh các phương án hosting (Odoo.sh / Odoo Online / On-premise), sizing hạ tầng tham khảo, và ảnh hưởng của data residency tại VN đến lựa chọn hosting. Phần **license/dependency từ góc độ kỹ thuật** (Community vs Enterprise apps, OPL-1 vs LGPL-3) xem `skills/odoo-editions.md` — tài liệu này KHÔNG lặp lại nội dung đó.

> ⚠️ **Disclaimer giá:** Mọi con số giá trong tài liệu này (nếu có) chỉ mang tính **minh họa nguyên tắc**, KHÔNG phải báo giá chính thức. Giá Odoo Enterprise thay đổi theo thời gian và theo khu vực — **luôn tham khảo `odoo.com/pricing` tại thời điểm báo giá thực tế** và xác nhận lại với Odoo (qua kênh Partner) trước khi đưa vào Commercial Proposal.

---

## 1. Mô hình giá Odoo Enterprise

### 1.1 Nguyên tắc chung

Odoo Enterprise được bán theo mô hình **subscription** (thuê bao định kỳ — theo tháng hoặc theo năm, trả theo năm thường có chiết khấu so với trả theo tháng), tính phí dựa trên **số lượng user**. Có 3 trục chính cần làm rõ với khách trong Discovery trước khi đưa ra con số:

1. **Theo số user** — gần như mọi gói Enterprise đều tính `giá / user / tháng`. Số user thực tế dùng hệ thống (không phải tổng nhân viên công ty) quyết định chi phí license hàng tháng/năm.
2. **Theo phạm vi Apps** — Odoo thường có 2 nhóm gói:
   - **Gói "1 App" (One App Free / Single App)**: cho phép dùng **một** app Enterprise cụ thể (ví dụ chỉ Accounting, hoặc chỉ Inventory) — thường có giá thấp hơn đáng kể, đôi khi miễn phí cho 1 user nếu chỉ dùng 1 app.
   - **Gói "Full Suite" (Standard/Custom — toàn bộ Apps Enterprise)**: cho phép dùng **tất cả** apps Enterprise (Accounting, Inventory nâng cao, MRP, Helpdesk, Studio...) — giá/user cao hơn gói 1-App nhưng mở khóa toàn bộ hệ sinh thái.
   - → Khi khách chỉ cần 1-2 phân hệ Enterprise (ví dụ chỉ cần Accounting đầy đủ, còn lại dùng Community), **luôn hỏi Odoo Partner xem gói 1-App có rẻ hơn Full Suite không** — đừng mặc định phải mua Full Suite.
3. **Theo loại user — Internal vs Portal/External**:
   - **Internal user**: nhân viên thao tác trực tiếp trong backend Odoo (sales, kế toán, kho, HR...) — đây là loại user tính phí chính theo subscription.
   - **Portal/External user**: khách hàng, nhà cung cấp chỉ truy cập **Portal** (xem báo giá, đơn hàng, hóa đơn, ticket của chính họ) — loại user này **thường miễn phí hoặc có chính sách giá ưu đãi riêng** (không tính như internal user).
   - → Khi Discovery hỏi "bao nhiêu user", PHẢI tách rõ: bao nhiêu **internal** (nhân viên thao tác hệ thống) vs bao nhiêu **portal** (KH/NCC chỉ xem thông tin) — ảnh hưởng trực tiếp đến license cost trong Proposal.

### 1.2 Community = miễn phí license, KHÔNG miễn phí triển khai

Community Edition không tốn chi phí license (LGPL-3, xem `skills/odoo-editions.md`), nhưng PreSale cần làm rõ với khách rằng tổng chi phí dự án (TCO) vẫn gồm:

- Chi phí **triển khai** (implementation, customization, data migration, training).
- Chi phí **hạ tầng** (server, hosting — xem mục 2-3).
- Chi phí **support/bảo trì** sau go-live (SLA, bugfix, upgrade version).

→ "Dùng Odoo Community để khỏi tốn tiền" là hiểu sai phổ biến của khách — cần làm rõ ngay từ Discovery để tránh kỳ vọng sai về tổng ngân sách.

### 1.3 Checklist hỏi khách trước khi tính license

| Câu hỏi | Vì sao quan trọng |
|---|---|
| Số lượng **internal user** dự kiến (theo từng phòng ban)? | Cơ sở tính subscription/tháng |
| Số lượng **portal user** (KH/NCC) dự kiến? | Thường free/rẻ — tránh tính nhầm vào internal |
| Khách thực sự cần bao nhiêu **app Enterprise** khác nhau? | Quyết định gói 1-App vs Full Suite |
| Khách ưu tiên trả theo **tháng hay năm**? Cam kết bao lâu? | Ảnh hưởng chiết khấu, dòng tiền |
| Có kế hoạch **tăng user theo lộ trình** (Phase 2, mở thêm chi nhánh)? | Ảnh hưởng thiết kế Proposal theo Phase — xem `presales-proposal-sow-templates.md` |

---

## 2. So sánh phương án triển khai

| Tiêu chí | Odoo Online | Odoo.sh | On-premise/Self-hosted |
|---|---|---|---|
| Ai quản lý hạ tầng | Odoo | Odoo (qua Git-based platform) | Đối tác/khách hàng tự quản |
| Khả năng customize | Hạn chế (chỉ qua Studio + Apps Store, KHÔNG ssh/code tùy ý) | Đầy đủ (deploy code riêng qua Git, có staging/production branches) | Đầy đủ |
| Yêu cầu Edition | Enterprise only | Enterprise only | Community hoặc Enterprise |
| Backup/SLA | Tự động, Odoo quản lý | Tự động (theo plan), có staging | Đối tác tự thiết lập (cần kế hoạch backup/DR) |
| Phù hợp với | DN nhỏ, ít customize, muốn nhanh | DN cần customize sâu nhưng không muốn tự quản hạ tầng | DN có yêu cầu đặc biệt về data residency/bảo mật, hoặc đã có hạ tầng/IT team |
| Chi phí ẩn | Thấp | Trung bình (giá theo server size) | Cao hơn ban đầu (server, IT, bảo trì) nhưng có thể tối ưu dài hạn |

### 2.1 Odoo Online

**Mô tả:** SaaS thuần — Odoo lưu trữ, vận hành, backup, upgrade toàn bộ. Khách chỉ đăng nhập và dùng.

**Ưu điểm:**
- Triển khai nhanh nhất — go-live trong vài ngày nếu không/ít customize.
- Không cần đội IT vận hành hạ tầng.
- Tự động cập nhật version mới, vá bảo mật.

**Nhược điểm:**
- Customize giới hạn ở **Studio** + cài thêm Apps từ Odoo Apps Store — **không thể** deploy module code tùy chỉnh tự viết (custom Python module) lên Odoo Online theo cách thông thường.
- Không kiểm soát được vị trí đặt server (theo hạ tầng cloud của Odoo, thường ở nước ngoài).

**Ai nên chọn:** DN nhỏ/vừa, quy trình gần với chuẩn Odoo (ít Gap-Custom), ưu tiên tốc độ và OPEX thấp, không có yêu cầu đặc biệt về data residency.

### 2.2 Odoo.sh

**Mô tả:** Platform-as-a-Service (PaaS) dựa trên Git — đối tác/dev đẩy code (module custom) lên repository, Odoo.sh tự động build, test, deploy lên các môi trường (development/staging/production branches).

**Ưu điểm:**
- Customize **đầy đủ** (toàn quyền viết module Python/JS riêng) nhưng **không cần tự quản server** (Odoo lo phần OS, DB, backup, scaling cơ bản).
- Quy trình dev chuẩn: branch development → staging → production, có thể test trước khi lên production.
- Vẫn được Odoo tự động vá bảo mật/hạ tầng.

**Nhược điểm:**
- Chi phí phụ thuộc vào **kích thước server** (số lượng "workers"/CPU/RAM của plan) — cần ước lượng tải hệ thống để chọn plan phù hợp.
- Vẫn không kiểm soát hoàn toàn vị trí đặt server (theo data center của Odoo.sh).

**Ai nên chọn:** DN cần customize sâu (nhiều module Gap-Custom, tích hợp phức tạp) nhưng KHÔNG có/không muốn đầu tư đội IT quản trị hạ tầng — "best of both worlds" giữa Online và On-premise.

### 2.3 On-premise / Self-hosted

**Mô tả:** Cài đặt Odoo (Community hoặc Enterprise) trên server riêng — đặt tại data center do đối tác/khách hàng lựa chọn, hoặc trên private/public cloud (AWS, GCP, Azure, hoặc nhà cung cấp cloud trong nước).

**Ưu điểm:**
- Toàn quyền kiểm soát: vị trí đặt server (data residency), cấu hình hạ tầng, networking, tích hợp hệ thống nội bộ (AD/LDAP, ERP cũ, máy chấm công nội bộ...).
- Có thể dùng **Community** (miễn phí license) nếu không cần app Enterprise → tối ưu chi phí dài hạn cho DN ít cần tính năng Enterprise.
- Không phụ thuộc kết nối internet ra ngoài để truy cập hệ thống nội bộ (nếu deploy on-prem thật sự, không phải cloud).

**Nhược điểm:**
- Chi phí ban đầu cao hơn: mua/thuê server, license OS, setup, cấu hình bảo mật, SSL, backup/DR — và cần đội ngũ (nội bộ hoặc thuê đối tác) **vận hành liên tục** (vá bảo mật OS, monitoring, upgrade Odoo version).
- Trách nhiệm SLA/uptime/backup hoàn toàn thuộc về đối tác/khách hàng — phải có kế hoạch rõ ràng (xem mục 3).

**Ai nên chọn:**
- DN có yêu cầu **bắt buộc về data residency** hoặc bảo mật theo ngành (xem mục 4).
- DN đã có sẵn hạ tầng/đội IT, muốn tận dụng tài nguyên có sẵn.
- DN chỉ cần Community (không cần app Enterprise) — on-premise là lựa chọn DUY NHẤT khả thi về license (Odoo Online/Odoo.sh yêu cầu Enterprise).

---

## 3. Sizing hạ tầng (cho On-premise/Self-hosted)

> ⚠️ Bảng dưới đây là **ước lượng tham khảo ban đầu** để PreSale có con số đưa vào Proposal — **luôn ghi chú rõ với khách rằng cần benchmark/load testing thực tế theo workload cụ thể** (số lượng giao dịch/ngày, độ phức tạp report, số lượng module cài đặt...) trước khi chốt cấu hình server cuối cùng, đặc biệt với dự án từ "50-150 users" trở lên.

| Số user đồng thời | CPU | RAM | Ghi chú |
|---|---|---|---|
| < 10 users | 2 vCPU | 4-8 GB RAM | Có thể chạy chung Odoo + PostgreSQL trên 1 server |
| 10-50 users | 4 vCPU | 8-16 GB RAM | Vẫn có thể gộp chung server, nhưng nên theo dõi tải DB |
| 50-150 users | 8 vCPU | 16-32 GB RAM | Cân nhắc **tách DB server riêng** (PostgreSQL trên server/instance riêng) để tối ưu I/O |
| > 150 users | Cần **load testing riêng** | Cần **load testing riêng** | Cân nhắc **horizontal scaling** (nhiều Odoo workers/server đứng sau load balancer), DB server riêng với **SSD**, theo dõi kỹ các module nặng (report PDF, accounting, MRP) |

**Lưu ý quan trọng:**

- **"User đồng thời" (concurrent users) khác với "tổng số user license"** — một công ty có 100 user nhưng chỉ ~30 người thao tác cùng lúc giờ cao điểm thì sizing theo ~30 concurrent, không phải 100. Cần làm rõ pattern sử dụng (giờ hành chính cố định vs ca kíp 24/7) khi Discovery.
- **Storage (dung lượng ổ cứng) phụ thuộc nhiều vào attachment** — hình ảnh sản phẩm, file đính kèm (hợp đồng, chứng từ scan), báo cáo PDF được lưu trữ (đặc biệt nếu dùng app Documents hoặc archive hóa đơn điện tử). Khoản này **cần ước lượng riêng** dựa trên: số lượng SKU có hình ảnh, tần suất phát sinh chứng từ/tháng, chính sách lưu trữ (bao nhiêu năm). Không gộp chung vào sizing CPU/RAM ở trên.
- **Kế hoạch backup** (tần suất, retention, vị trí lưu backup — cùng server hay tách riêng/offsite) cần được lên kèm với sizing storage — backup full DB + filestore của Odoo có thể chiếm dung lượng đáng kể, đặc biệt nếu giữ nhiều bản backup.
- Với plan **Odoo.sh**, sizing tương tự dùng để tham khảo chọn **plan size** (số workers) — Odoo.sh tự quản OS/DB nhưng vẫn cần chọn đúng tier theo tải dự kiến.

---

## 4. VN Data Residency — ảnh hưởng đến lựa chọn hosting

Mở rộng từ `skills/l10n-vietnam-compliance-guide.md` (mục 6 — Bảo vệ dữ liệu cá nhân):

- **Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân** (hiệu lực từ 01/07/2023) đặt ra yêu cầu về xử lý/lưu trữ dữ liệu cá nhân của công dân VN. Một số nhóm khách hàng — **DNNN (doanh nghiệp nhà nước), tổ chức tài chính/ngân hàng, y tế**, hoặc đơn giản là khách có **chính sách nội bộ nghiêm ngặt** về bảo mật dữ liệu — có thể yêu cầu dữ liệu phải được lưu trữ **trong lãnh thổ Việt Nam**.
- **Odoo Online và Odoo.sh đặt server tại data center của Odoo (thường ở nước ngoài, ví dụ châu Âu)** → với nhóm khách hàng nêu trên, 2 phương án này **có thể KHÔNG đáp ứng** yêu cầu data residency.

### 4.1 Phương án khi khách yêu cầu data residency VN

1. **On-premise tại data center VN** — đặt server tại trung tâm dữ liệu trong nước (ví dụ Viettel IDC, VNPT, FPT Telecom, CMC Telecom...) → đáp ứng chắc chắn yêu cầu "lãnh thổ VN".
2. **Private cloud tại VN** — thuê instance cloud từ nhà cung cấp có data center đặt tại VN.

### 4.2 Lưu ý quan trọng khi xác nhận yêu cầu

- **"Khu vực Đông Nam Á/gần VN" KHÔNG đồng nghĩa với "lãnh thổ VN"** — ví dụ AWS region `ap-southeast-1` (Singapore) vẫn là **nước ngoài** về mặt pháp lý, dù gần về địa lý/độ trễ mạng. Nếu yêu cầu của khách (theo chính sách nội bộ hoặc theo cách diễn giải Nghị định 13 mà khách áp dụng) là "dữ liệu không được rời khỏi lãnh thổ VN", thì Singapore **không đáp ứng**.
- → Trong Discovery, **luôn hỏi RÕ và bằng văn bản**: yêu cầu của khách là (a) "phải đặt server trong lãnh thổ VN" hay (b) "khu vực Đông Nam Á/gần VN là chấp nhận được"? Đây là 2 yêu cầu khác nhau hoàn toàn về phương án kỹ thuật và chi phí — xác nhận sai có thể dẫn đến chọn sai phương án hosting và phải làm lại.
- Nếu khách không chắc, khuyến nghị khách trao đổi với bộ phận pháp chế/an ninh thông tin nội bộ trước khi PreSale chốt phương án — đây là quyết định của khách hàng, PreSale chỉ đưa ra các lựa chọn kỹ thuật tương ứng.

---

## 5. Khung quyết định nhanh (Decision Framework)

Dùng chuỗi câu hỏi sau để nhanh chóng thu hẹp phương án triển khai phù hợp trong buổi Discovery/Proposal:

```
1. Khách BẮT BUỘC data residency tại VN?
   ├── CÓ  → On-premise hoặc Private Cloud đặt tại VN (xem mục 4)
   └── KHÔNG → tiếp câu 2

2. Khách cần customize sâu (nhiều module Gap-Custom, tích hợp phức tạp)?
   ├── CÓ  → Odoo.sh (nếu không có IT team) hoặc On-premise (nếu có IT team)
   └── KHÔNG → tiếp câu 3

3. Khách CÓ hoặc sẵn sàng đầu tư đội IT quản trị hạ tầng?
   ├── CÓ  → On-premise khả thi (tối ưu chi phí dài hạn, đặc biệt nếu chỉ cần Community)
   └── KHÔNG → tiếp câu 4

4. Ngân sách ưu tiên OPEX thấp, quy trình gần chuẩn Odoo, ít customize?
   └── → Odoo Online
```

**Cách dùng:** Đây là điểm khởi đầu để PreSale đề xuất phương án trong buổi trao đổi — KHÔNG thay thế việc xác nhận lại với khách và (nếu cần) với Odoo Partner trước khi đưa vào Proposal chính thức. Một dự án có thể kết hợp: ví dụ Phase 1 dùng Odoo Online để go-live nhanh, Phase 2 chuyển sang Odoo.sh khi cần customize sâu hơn — nếu vậy, cần nêu rõ chi phí/rủi ro của việc **migrate giữa các phương án hosting** trong Proposal.

---

## 6. Đưa vào Commercial Proposal

Khi đưa phương án triển khai đã chọn vào Proposal, liệt kê **các dòng chi phí riêng biệt** (không gộp chung thành 1 dòng "license" mơ hồ) — giúp khách so sánh minh bạch và tránh phát sinh sau này:

| Hạng mục | Áp dụng cho | Ghi chú |
|---|---|---|
| **License/Subscription Enterprise** | Odoo Online, Odoo.sh, On-premise (nếu dùng Enterprise) | Theo số internal user x đơn giá tại thời điểm báo giá (xem mục 1) — ghi rõ "tham khảo odoo.com/pricing, có thể thay đổi" |
| **Hosting/Server** | Odoo.sh (theo plan size), On-premise (mua/thuê server, cloud instance) | Với On-premise: tách riêng chi phí server vs chi phí setup ban đầu |
| **Domain & SSL Certificate** | On-premise (và Odoo.sh nếu dùng custom domain) | Thường là chi phí định kỳ nhỏ nhưng cần liệt kê |
| **Backup & Disaster Recovery (DR)** | On-premise (bắt buộc tự thiết lập), Odoo.sh (theo plan) | On-premise cần nêu rõ: tần suất backup, retention, có DR site không |
| **Support hạ tầng (Infrastructure Support/SLA)** | On-premise chủ yếu | Chi phí định kỳ cho việc vá bảo mật OS, monitoring, xử lý sự cố hạ tầng — KHÁC với support ứng dụng Odoo (functional/bugfix) |

→ Sau khi hoàn thiện bảng chi phí hosting/license, ghép cùng chi phí triển khai (effort estimation) để ra Commercial Proposal đầy đủ — xem `skills/presales-effort-estimation-guide.md` và `skills/presales-proposal-sow-templates.md`.

---

## Liên kết

- Chi tiết Community vs Enterprise (license, dependency rules, app availability — góc độ Dev): `skills/odoo-editions.md`
- VN Data Residency & Nghị định 13/2023/NĐ-CP (góc độ compliance): `skills/l10n-vietnam-compliance-guide.md` (mục 6)
- Cấu trúc Commercial Proposal/SOW: `skills/presales-proposal-sow-templates.md`
- Ước lượng effort triển khai (đi kèm chi phí hosting để ra tổng giá): `skills/presales-effort-estimation-guide.md`
