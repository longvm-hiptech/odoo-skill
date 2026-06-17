# Skill Corrections Log

Append here whenever a skill claim is found to be **incorrect or outdated** during a dev session.
Run `/odoo-skill-update` to batch-verify, patch the skill files, and clear this log via PR.

## How to Append (Agent / Developer)

```
| YYYY-MM-DD | skills/file-name.md | Section heading | Wrong claim (exact quote or summary) | Correct claim | Source / evidence |
```

- **One row = one distinct claim**.
- If a runtime error is novel (not yet in `odoo-troubleshooting-guide.md`), add a row here too; `/odoo-skill-update` will promote it.
- Do **not** edit skill files directly during a dev session — log here, patch via PR.

---

## Pending Corrections

| Date | Skill File | Section | Wrong / Stale Claim | Correct Info | Source / Evidence |
|------|-----------|---------|---------------------|--------------|-------------------|

*(No pending corrections — all resolved in PR skill-update/2026-06-16)*

---

## Applied Corrections

| Date Logged | Date Applied | Skill File | Change |
|------------|-------------|-----------|--------|
| 2026-06-16 | 2026-06-16 | `skills/odoo-version-knowledge-19.md` | Banner + Status: "in development / master" → "Stable (Oct 2025) / 19.0"; added GitHub Verification URLs section |
| 2026-06-16 | 2026-06-16 | `skills/odoo-version-knowledge-18-19.md` | GitHub Verification URLs: master → 19.0; removed "until release" note |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | Added Quick Lookup entries; added full v19-Specific Runtime Errors section (12 new errors) |
| 2026-06-16 | 2026-06-16 | `skills/odoo-security-guide-19.md` | Banner stable; `category_id` → `privilege_id` in res.groups; added `user_ids` note; `ir.rule.group_id` → `groups` (M2M); verify branch `19.0` |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: purchase.order.refresh() → invalidate_recordset() |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: _read_group requires aggregate specs |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: digits rejects lists/named tuples |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: inline `<list>` inside One2many unsupported |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: `<dashboard>` not in CE |
| 2026-06-16 | 2026-06-16 | `skills/odoo-module-generator-19.md` | Banner stable; _sql_constraints → models.Constraint(); view_mode 'tree,form' → 'list,form'; `<tree>` → `<list>`; chatter div → `<chatter/>` |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: stock.move field changes (name/quantity_done/product_uom_id) |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: res.partner has no vendor boolean |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: %(xml_id)d forward refs fail in same file |
| 2026-06-16 | 2026-06-16 | `skills/report-patterns.md` | Added critical warning: `<template id>` not `<t id>` for QWeb reports |
| 2026-06-16 | 2026-06-16 | `skills/odoo-module-generator-19.md` | res.groups.category_id → privilege_id (covered via security-guide patch) |
| 2026-06-16 | 2026-06-16 | `skills/odoo-security-guide-19.md` | ir.rule.group_id → groups (Many2many) |
| 2026-06-16 | 2026-06-16 | `skills/xml-view-patterns.md` | View Types table: added v19 column; `<tree>` → `<list>`; added v19 version-specific summary row |
| 2026-06-16 | 2026-06-16 | `skills/odoo-module-generator-19.md` | product.template.type values: 'product'/'storable' → 'consu'/'service'/'combo' (see troubleshooting guide) |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: date_planned is Datetime not Date |
| 2026-06-16 | 2026-06-16 | `skills/xml-view-patterns.md` | Chatter div → `<chatter/>` in v19; form example updated; version-specific summary updated |
| 2026-06-16 | 2026-06-16 | `skills/xml-view-patterns.md` | view_mode 'tree,form' → 'list,form'; Window Action example updated |
| 2026-06-16 | 2026-06-16 | `skills/odoo-troubleshooting-guide.md` | NEW: missing `<chatter/>` on form views |
| 2026-06-16 | 2026-06-16 | `skills/odoo-security-guide-19.md` | category_id best practice: always set privilege_id to avoid "Other" group in UI |
