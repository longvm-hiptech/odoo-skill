# Odoo Module Checklist

> **Used by:** `agents/planner.md` during task breakdown and execution phases.
>
> Reference this file when building or reviewing an Odoo module to ensure nothing is missed.

---

## MODULE SCAFFOLD — Minimum Required Files

```
{module_name}/
├── __manifest__.py          ← REQUIRED
├── __init__.py              ← REQUIRED
├── models/
│   └── __init__.py          ← REQUIRED if models exist
├── views/                   ← REQUIRED if any UI
└── security/
    └── ir.model.access.csv  ← REQUIRED for every new model
```

### `__manifest__.py` Template

```python
{
    'name': 'Module Display Name',
    'version': '17.0.1.0.0',          # {odoo_version}.{major}.{minor}.{patch}
    'category': 'Human Resources',    # use official Odoo categories
    'summary': 'Short one-line description',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': [
        'base',
        # add Odoo modules you depend on
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_items.xml',
        'views/{model}_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
```

**Rules:**
- Version format: `{odoo_version}.{X}.{Y}.{Z}` — e.g. `17.0.1.0.0`
- Always list `security/ir.model.access.csv` **first** in `data`
- Never import Python files in manifest — use `__init__.py` imports only

---

## TASK CATEGORIES & STANDARD TASKS

### Category A — Foundation (always required)

| Task | File | Notes |
|------|------|-------|
| Scaffold structure | `__manifest__.py`, `__init__.py` | Set version, depends |
| Security groups (if custom) | `security/res_groups.xml` | Define before models |
| Access rights | `security/ir.model.access.csv` | One line per model per group |

### Category B — Models

| Task | File | Notes |
|------|------|-------|
| New model | `models/{name}.py` | Use `models.Model` |
| Inherited model | `models/{name}.py` | Use `_inherit = 'existing.model'` |
| Transient model (wizard) | `wizards/{name}.py` | Use `models.TransientModel` |

**Model checklist:**
- [ ] `_name` defined (required for new models, optional in v19 for inherited)
- [ ] `_description` defined (required, triggers warning if missing)
- [ ] `_order` set if default sort matters
- [ ] `_rec_name` set if not using `name` field
- [ ] All relational fields have `ondelete` set (`'cascade'`, `'restrict'`, `'set null'`)
- [ ] Computed fields have `store=True` only if needed for search/group
- [ ] `@api.constrains` for business rules
- [ ] `@api.onchange` only for UI — never for business logic
- [ ] `name_get()` overridden if display name needs formatting (v16 and below)

### Category C — Views

| Task | File | Notes |
|------|------|-------|
| Form view | `views/{model}_views.xml` | Full record editing |
| List view | `views/{model}_views.xml` | `<list>` (v17+) or `<tree>` (v16-) |
| Kanban view | `views/{model}_views.xml` | For stage-based workflows |
| Search view | `views/{model}_views.xml` | Filters, group-by |
| Action | `views/menu_items.xml` | `ir.actions.act_window` |
| Menu items | `views/menu_items.xml` | Top → Sub → Action |

**View checklist:**
- [ ] XML IDs follow pattern: `{module_name}.{model_underscore}_{view_type}_view`
- [ ] Form view has `<header>` for statusbar if using workflow states
- [ ] List view shows key fields only (4-6 columns max)
- [ ] Search view has at least one `<filter>` and one `<group by>`
- [ ] `invisible` attribute uses correct syntax for target version:
  - v14-v16: `attrs="{'invisible': [('state', '=', 'done')]}"`
  - v17+: `invisible="state == 'done'"`

### Category D — Security

| Task | File | Notes |
|------|------|-------|
| Access rights | `security/ir.model.access.csv` | Required per model |
| Record rules | `security/ir.rule.xml` | For row-level filtering |
| Custom groups | `security/res_groups.xml` | Only if app needs roles |

**`ir.model.access.csv` format:**
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_{model}_{group},{model} {group},model_{model_underscore},{group_xml_id},1,1,1,1
```

**Rules:**
- Always provide at least one access line for each new model
- Use `base.group_user` for standard internal user access
- Use `base.group_system` or custom group for restricted access

### Category E — Advanced (add as needed)

| Task | File | Notes |
|------|------|-------|
| QWeb PDF report | `report/{name}_report.xml` | Inherit `report.layout` |
| Report action | `report/{name}_report.xml` | `ir.actions.report` |
| Scheduled action | `data/cron.xml` | `ir.cron` |
| Email template | `data/mail_template.xml` | `mail.template` |
| Server action | `data/server_action.xml` | `ir.actions.server` |
| HTTP controller | `controllers/main.py` | Inherit `http.Controller` |
| OWL component | `static/src/js/` | Version-specific (1.x/2.x/3.x) |
| Demo data | `demo/demo.xml` | Only for demo/testing |
| Migration script | `migrations/{version}/pre-migrate.py` | Version upgrade hooks |

---

## DEPENDENCY ORDER — Standard Build Sequence

Always follow this order to avoid `XML ID not found` and `Field not defined` errors:

```
1. Scaffold (__manifest__, __init__)
2. Security groups (res_groups.xml)
3. Models (Python files)
4. Access rights (ir.model.access.csv)
5. Views — form, list, search
6. Actions and menus
7. Data files (sequences, stages, config)
8. Reports
9. Controllers
10. OWL components
11. Demo data
12. Tests
```

---

## COMMON PITFALLS — CHECK BEFORE SUBMITTING

### Models
- [ ] No `# -*- coding: utf-8 -*-` header (not needed in Python 3)
- [ ] Using `super()` not `super(ClassName, self)`
- [ ] `@api.depends` lists ALL fields used inside `_compute_` method
- [ ] No business logic inside `@api.onchange` — use `@api.constrains` instead
- [ ] `sudo()` used only when intentional privilege escalation is needed

### Views
- [ ] All XML IDs are unique within the module
- [ ] `inherit_id` references existing view XML ID (verify before use)
- [ ] `<xpath>` uses `position="after"/"before"/"inside"/"replace"` correctly
- [ ] Form view does not reference non-existent fields
- [ ] `domain` and `context` strings are valid Python expressions

### Manifest
- [ ] All XML files listed in `data` actually exist
- [ ] `depends` includes all modules whose models/views are used
- [ ] Version bump when releasing updates

### Security
- [ ] Every new `models.Model` class has a row in `ir.model.access.csv`
- [ ] `model_id:id` follows pattern: `model_{model_name_with_underscores}`
  - Example: `hr.employee` → `model_hr_employee`

---

## VERSION-SPECIFIC REMINDERS

### Odoo 17+
- Use `<list>` instead of `<tree>` for list views
- Use `invisible="python_expr"` instead of `attrs`
- `aggregator=` replaces `group_operator=` on fields

### Odoo 18+
- `_name` optional in inherited models
- New `fields.Html` sanitization behavior — set `sanitize=False` explicitly if needed

### Odoo 19
- OWL 3.x — hooks API changed from 2.x
- Check OCA repo compatibility before adding as dependency
