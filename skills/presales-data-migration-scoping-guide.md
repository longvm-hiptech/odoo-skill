---
name: presales-data-migration-scoping-guide
keywords: [presales, data migration, migration du lieu, import du lieu, scoping, master data, chuyen doi du lieu]
description: Hướng dẫn khảo sát & ước lượng phạm vi di chuyển dữ liệu từ hệ thống cũ (Excel, Misa, Fast, phần mềm tự viết...) sang Odoo trước khi báo giá.
odoo_versions: [all]
related_skills: [presales-effort-estimation-guide, presales-discovery-questionnaire, presales-fit-gap-analysis-guide, data-migration-patterns]
---

# Data Migration Scoping Guide (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  DATA MIGRATION SCOPING                                                       ║
║  Khảo sát nguồn dữ liệu → Phân loại theo ưu tiên → Scope doc → Effort         ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Tài liệu này là phần **khảo sát & xác định phạm vi (scoping)** cho hạng mục Data Migration — dùng ở giai đoạn Discovery/Fit-Gap, trước khi điền số man-day vào Proposal. Phần benchmark man-day theo khối lượng/độ phức tạp đã có sẵn ở `presales-effort-estimation-guide.md` (Mục 5) — tài liệu này **không lặp lại** các con số đó, mà tập trung vào: hỏi gì, khảo sát gì, và cách tổ chức scope thành 1 doc rõ ràng để áp benchmark cho đúng.

---

## 1. Cách dùng & Tại sao cần scoping riêng

- Data migration là hạng mục **thường bị ước lượng thấp nhất** trong dự án ERP. Lý do: effort phụ thuộc chủ yếu vào **chất lượng dữ liệu nguồn** (trùng lặp, thiếu chuẩn hoá, format lộn xộn...), chứ không chỉ vào số lượng bản ghi — và chất lượng dữ liệu này **không thể đánh giá chính xác chỉ qua mô tả miệng** của khách, phải xem trực tiếp file mẫu.
- Nếu không làm rõ phạm vi ngay ở giai đoạn Fit-Gap/Proposal, rất dễ xảy ra tranh chấp kiểu "tưởng là included" sau này — vd khách nghĩ toàn bộ 5 năm lịch sử hoá đơn sẽ được đưa vào Odoo, trong khi Proposal chỉ tính migrate số dư đầu kỳ.
- **Cách dùng tài liệu này**:
  1. Dùng Mục 2 (checklist khảo sát) trong buổi Discovery/Fit-Gap để hỏi khách — ghi nhận câu trả lời vào Discovery Notes.
  2. Dùng Mục 3 để phân loại dữ liệu khách có theo độ ưu tiên (bắt buộc go-live vs tuỳ chọn).
  3. Dùng Mục 4 để xác định các yếu tố làm tăng effort ngoài số lượng record thuần tuý.
  4. Điền kết quả vào template Mục 6 ("Data Migration Scope" doc) — đính kèm Proposal/SOW.
  5. Tra man-day theo `presales-effort-estimation-guide.md` (Mục 5) cho từng entity trong scope doc.

---

## 2. Checklist khảo sát nguồn dữ liệu

Hỏi các câu này **càng sớm càng tốt** (lý tưởng là ngay buổi Discovery đầu tiên), vì câu trả lời ảnh hưởng trực tiếp đến việc Proposal có khả thi về thời gian/chi phí hay không.

| Câu hỏi | Vì sao quan trọng |
|---|---|
| Hệ thống nguồn là gì (Excel rời rạc / Misa / Fast / phần mềm tự viết / không có hệ thống — sổ giấy)? | Quyết định phương pháp lấy dữ liệu: export tự động (nhanh, rẻ) hay phải nhập tay/scan lại (chậm, đắt, dễ sai). |
| Có khả năng export ra file (Excel/CSV/XML) không, hay phải nhập tay? | Nếu phải nhập tay từ sổ giấy/PDF scan, effort tăng vọt — đây thường là công việc của khách hoặc bên thứ 3 (data entry), không phải của đối tác triển khai Odoo. Cần thống nhất rõ ai làm. |
| Ai ở phía khách có quyền/khả năng export dữ liệu thô? | Nếu người này nghỉ phép/bận, hoặc hệ thống cũ do 1 nhà cung cấp khác quản lý (cần xin quyền/trả phí export) — đây là rủi ro timeline cần nêu sớm. |
| Dữ liệu có đang trùng lặp, thiếu chuẩn hoá (vd 1 khách hàng có 3 tên viết khác nhau) không? | Quyết định có cần thêm bước "data cleansing" riêng hay không (xem Mục 4) — đây là nguyên nhân phổ biến nhất khiến effort vượt benchmark. |
| Đơn vị tính, mã sản phẩm/khách hàng/NCC hiện tại có theo 1 chuẩn nhất quán không? | Nếu mỗi chi nhánh/bộ phận tự đặt mã riêng, cần xây bảng mapping mã cũ → mã Odoo — tốn thêm effort phân tích + transform. |
| Có cần giữ lại lịch sử giao dịch (đơn hàng/hoá đơn cũ) hay chỉ cần số dư đầu kỳ? | Ảnh hưởng lớn nhất đến effort tổng — xem 3 chiến lược ở Mục 3.2. Câu trả lời này nên được hỏi **rõ ràng và ghi vào Proposal**, vì khách thường mặc định "có" mà không nghĩ đến chi phí. |
| Khách có timeline "cutover" cố định (vd đầu năm tài chính mới) không? | Nếu có, toàn bộ kế hoạch migration (mock run, final run) phải khớp với mốc này — ảnh hưởng đến số lần thử nghiệm khả thi và do đó ảnh hưởng effort (xem Mục 4).|

---

## 3. Danh mục dữ liệu theo độ ưu tiên

### 3.1 Master Data (bắt buộc cho go-live)

Đây là nhóm dữ liệu **bắt buộc phải có** trước ngày go-live, vì mọi giao dịch mới trên Odoo đều cần tham chiếu đến chúng.

| Loại dữ liệu | Ví dụ | Ghi chú |
|---|---|---|
| Khách hàng (`res.partner`) | Tên, địa chỉ, mã số thuế, người liên hệ | Kiểm tra trùng lặp trước khi import — xem checklist Mục 2. |
| Nhà cung cấp (`res.partner`) | Tương tự khách hàng | Có thể chung 1 file với khách hàng nếu hệ thống cũ không tách riêng. |
| Sản phẩm/Dịch vụ (`product.template`) | Mã SP, tên, đơn vị tính, giá vốn/giá bán, danh mục | Mã sản phẩm cũ → mã Odoo cần mapping nếu không đồng nhất giữa các nguồn. |
| Bảng giá | Pricelist theo nhóm khách hàng, chiết khấu | Thường đi kèm sản phẩm — kiểm tra xem có nhiều bảng giá song song (theo khu vực/đại lý) không. |
| Chart of Accounts | Hệ thống tài khoản kế toán | **Đặc biệt quan trọng với `l10n_vn`** — số dư phải khớp với báo cáo đã nộp thuế (xem Mục 7). |
| Tồn kho đầu kỳ | Số lượng tồn theo sản phẩm, theo lô/vị trí (nếu có quản lý lot/serial hoặc multi-warehouse) | Nếu khách quản lý theo lô/hạn dùng, cần migrate cả thông tin lô — phức tạp hơn tồn kho theo SP đơn thuần. |
| Số dư công nợ đầu kỳ | Phải thu/phải trả theo từng khách hàng/NCC | Lý tưởng nên giữ chi tiết **theo từng hoá đơn** (không chỉ tổng số dư) để khách có thể tiếp tục theo dõi/đối chiếu thanh toán từng hoá đơn cũ trên Odoo. |
| Nhân viên/Phòng ban | `hr.employee`, cơ cấu tổ chức | Cần thiết nếu có dùng module HR/Project/Timesheets/Approvals từ ngày go-live. |

### 3.2 Historical/Transactional Data (tuỳ chọn)

Nhóm dữ liệu **lịch sử** — không bắt buộc cho go-live, nhưng khách thường mong muốn có để tra cứu/báo cáo về sau.

| Loại dữ liệu | Ví dụ | Ghi chú |
|---|---|---|
| Lịch sử đơn bán/đơn mua | Đơn hàng đã hoàn thành các năm trước | Khối lượng thường lớn nhất trong nhóm lịch sử. |
| Lịch sử bút toán kế toán | Sổ cái, sổ chi tiết các kỳ trước | Liên quan trực tiếp đến yêu cầu đối chiếu thuế (Mục 7). |
| Lịch sử sản xuất | Lệnh sản xuất, tiêu hao NVL các kỳ trước | Thường ít được yêu cầu migrate đầy đủ trừ khi phục vụ truy xuất nguồn gốc. |

Có **3 chiến lược** xử lý dữ liệu lịch sử — cần thảo luận với khách và chốt rõ trong Proposal (chiến lược nào cũng có thể áp dụng, và có thể áp dụng **khác nhau cho từng loại dữ liệu**, vd: đơn bán dùng chiến lược (b), công nợ chi tiết dùng chiến lược (a)):

1. **(a) Migrate đầy đủ vào Odoo** — đắt nhất, vì mỗi bản ghi lịch sử cần đi qua đầy đủ pipeline Extract → Clean → Map → Transform → Load → Validate (Mục 5). Chỉ nên chọn khi khách thực sự cần thao tác (sửa, đối chiếu, in lại) trên dữ liệu đó từ Odoo.
2. **(b) Migrate tóm tắt/số dư + đính kèm file PDF/Excel báo cáo cũ làm tài liệu tham khảo** — rẻ hơn nhiều, **phổ biến nhất**. Odoo chỉ cần số dư đúng tại thời điểm cutover; chi tiết lịch sử được lưu dưới dạng file đính kèm (attachment) trên record liên quan hoặc trong 1 thư mục Documents dùng để tra cứu khi cần.
3. **(c) Giữ nguyên hệ thống cũ ở chế độ read-only song song một thời gian (Parallel run)** — không tốn effort migrate, nhưng phát sinh chi phí duy trì hệ thống cũ (license, server, người quản trị) trong thời gian song song. Phù hợp khi khách cần tra cứu lịch sử thường xuyên trong giai đoạn đầu nhưng chưa muốn/chưa kịp migrate đầy đủ.

---

## 4. Yếu tố ảnh hưởng effort

Ngoài số lượng bản ghi, các yếu tố sau làm **tăng đáng kể** effort so với benchmark cơ bản — cần rà soát từng yếu tố khi điền effort vào scope doc (Mục 6):

| Yếu tố | Tác động |
|---|---|
| Số lượng bản ghi (theo từng entity) | Yếu tố cơ bản nhất — tra benchmark theo tier tại `presales-effort-estimation-guide.md` (Mục 5: <5,000 / 5,000-50,000 / >50,000 bản ghi). |
| Số lượng nguồn dữ liệu khác nhau cần hợp nhất | Vd 3 chi nhánh, mỗi chi nhánh 1 file Excel format khác nhau → effort tăng theo **số nguồn**, không chỉ tổng record (mỗi nguồn cần phân tích format + mapping riêng trước khi gộp). |
| Độ sạch dữ liệu (trùng lặp, thiếu trường bắt buộc, sai định dạng) | Có thể cần thêm bước "data cleansing" riêng — **trách nhiệm của khách hoặc đối tác cần thống nhất rõ ai làm và tính phí riêng** trước khi đưa vào effort migration. |
| Độ phức tạp mapping field | 1-1 (field nguồn → field Odoo trực tiếp) vs cần transform/lookup (vd mã đơn vị tính cũ → unit of measure Odoo, mã kho cũ → location Odoo) — mapping càng nhiều bước transform, effort càng tăng. |
| Số lần thử nghiệm (mock run) | Mock run để khách review + ít nhất 1 final run sát ngày go-live — **mỗi lần mock run cũng tốn effort** (chạy lại script, đối chiếu kết quả với khách), cần tính số lần dự kiến vào effort tổng, không chỉ tính 1 lần load duy nhất. |

---

## 5. Quy trình Migration điển hình

```
Extract (khách export)
    │
    ▼
Clean (chuẩn hoá, loại trùng)
    │
    ▼
Map (field mapping doc)
    │
    ▼
Transform
    │
    ▼
Load thử (staging/test database)
    │
    ▼
Validate (khách đối chiếu số liệu) ──── cần SIGN-OFF của khách
    │
    ▼
Load chính thức (production, gần ngày go-live)
    │
    ▼
Reconciliation (đối chiếu số dư cuối cùng với hệ thống cũ trước khi tắt hệ thống cũ)
```

> **Quan trọng**: bước **Validate** phải có **sign-off bằng văn bản của khách** trước khi chuyển sang Load chính thức. Nếu khách phát hiện sai lệch sau khi đã go-live (đặc biệt với số dư kế toán/công nợ — xem Mục 7), việc sửa chữa trên hệ thống production phức tạp và rủi ro hơn rất nhiều so với sửa ở bước Load thử.

> Phần kỹ thuật của từng bước (script Python, ORM `load()`, xử lý batch, mapping XML ID...) — xem `data-migration-patterns.md`. Tài liệu đó là **pattern thực thi kỹ thuật** mà đội Dev sẽ dùng; tài liệu hiện tại chỉ phục vụ scoping/ước lượng ở giai đoạn PreSale.

---

## 6. Template "Data Migration Scope" doc

Dùng bảng dưới để liệt kê từng entity cần migrate — đính kèm Proposal/SOW. Mỗi dòng = 1 loại dữ liệu (đối chiếu với Mục 3).

```markdown
| Entity | Nguồn dữ liệu | Format | Số lượng ước tính | Ai chịu trách nhiệm "clean" (Khách/Đối tác) | Migrate lịch sử? (Có/Không/Tóm tắt) | Effort ước tính (man-day) |
|---|---|---|---|---|---|---|
| Khách hàng (res.partner) | Misa + Excel chi nhánh HCM | Export CSV từ Misa, Excel rời cho chi nhánh | ~3,200 | Đối tác (sau khi khách export thô) | Không áp dụng | 2-3 |
| Sản phẩm (product.template) | Excel (3 file, 3 kho) | Excel | ~1,800 | Khách (gộp về 1 mã chuẩn trước khi gửi) | Không áp dụng | 3-5 |
| Tồn kho đầu kỳ | Phần mềm kho tự viết | Export CSV | ~1,800 dòng (theo SP x kho) | Đối tác | Không áp dụng | 2-3 |
| Công nợ đầu kỳ (phải thu) | Misa | Export Excel | ~450 hoá đơn mở | Đối tác | Có (chi tiết theo hoá đơn) | 3-5 |
| Lịch sử đơn bán 3 năm | Phần mềm tự viết | Export Excel theo năm | ~28,000 | Khách | Tóm tắt (đính kèm file Excel/PDF) | 1-2 |
| Sổ cái kế toán các kỳ trước | Misa | Export Excel | — | — | Không (giữ song song read-only 6 tháng) | 0 |
```

> Cột "Effort ước tính" tra theo tier tại `presales-effort-estimation-guide.md` (Mục 5), điều chỉnh theo các yếu tố ở Mục 4 (vd nhiều nguồn cần merge → lấy mức cao của range).

---

## 7. Lưu ý đặc thù Việt Nam

- **Số dư kế toán đầu kỳ** (công nợ, tồn kho, tài sản) **PHẢI khớp** với báo cáo tài chính/báo cáo thuế đã nộp gần nhất — không thể "làm tròn" tuỳ tiện. Sai lệch giữa số dư trên Odoo và số liệu đã kê khai có thể gây vấn đề khi quyết toán thuế hoặc khi cơ quan thuế đối chiếu sau này. Bước Reconciliation (Mục 5) với nhóm này cần có sự tham gia của Kế toán trưởng phía khách, không chỉ người vận hành dữ liệu.
- Nếu khách đang dùng phần mềm hoá đơn điện tử (xem `l10n-vietnam-compliance-guide.md`), cần làm rõ **ngay từ Proposal**: các hoá đơn điện tử **đã phát hành trước go-live** có cần đồng bộ vào Odoo hay không, hay chỉ áp dụng từ ngày go-live trở đi. Đây là điểm khách thường giả định "có" mà không lường trước effort — nếu cần đồng bộ ngược, đây thực chất là 1 hạng mục tích hợp/migration riêng cần ước lượng thêm (tham khảo Mục 4 — Hóa đơn điện tử VN trong `presales-effort-estimation-guide.md`).

---

## 8. Đưa scope doc vào Proposal/SOW

Sau khi hoàn thiện template Mục 6, đưa thẳng vào Proposal/SOW dưới 2 dạng — cả hai đều cần thiết để tránh tranh chấp scope sau này (xem Mục 1):

- **Phần "In Scope"**: liệt kê từng entity ở Mục 6 cùng nguồn dữ liệu, số lượng ước tính và việc có migrate lịch sử hay không (Có/Không/Tóm tắt) — đây là cam kết cụ thể với khách, không chỉ ghi chung chung "migrate dữ liệu khách hàng/sản phẩm".
- **Phần "Out of Scope" / Assumptions**: ghi rõ các điều kiện effort ở Mục 6 dựa trên — vd "Giả định: dữ liệu khách hàng do khách cung cấp dưới dạng 1 file Excel theo template chuẩn của đối tác, đã loại trùng. Nếu khách cung cấp dữ liệu thô từ Misa + 3 file Excel chi nhánh chưa hợp nhất, effort sẽ điều chỉnh theo Mục 4." Phần này là "lưới an toàn" khi thực tế khác với giả định ban đầu — nếu phát sinh, áp dụng quy trình change request thay vì âm thầm gánh thêm effort.
- Nếu khách yêu cầu migrate **toàn bộ lịch sử giao dịch** (chiến lược (a) ở Mục 3.2) cho 1 hoặc nhiều entity, effort tương ứng nên tách thành **dòng riêng** trong bảng Fit-Gap/Proposal (không gộp chung với Master Data) — vì đây thường là quyết định "nice to have" mà khách có thể chọn bỏ để giảm chi phí/timeline khi review giá.

---

## Liên kết

- `presales-effort-estimation-guide.md` — benchmark man-day theo khối lượng/độ phức tạp (Mục 5: Data Migration), dùng để điền cột "Effort" trong template Mục 6.
- `presales-discovery-questionnaire.md` — checklist khảo sát tổng quát; checklist Mục 2 ở đây bổ sung riêng cho data migration.
- `presales-fit-gap-analysis-guide.md` — định dạng bảng Fit-Gap chung, dùng khi data migration phát sinh thành 1 hạng mục Gap riêng (vd cần xây tool merge nhiều nguồn).
- `data-migration-patterns.md` — pattern kỹ thuật (script, ORM, batch processing) mà đội Dev sử dụng để thực thi quy trình ở Mục 5.
- `l10n-vietnam-compliance-guide.md` — chi tiết về hoá đơn điện tử và Chart of Accounts theo TT200/TT133, liên quan đến Mục 7.
