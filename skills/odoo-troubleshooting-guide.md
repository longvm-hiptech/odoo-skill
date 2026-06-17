# Odoo Troubleshooting Guide

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  TROUBLESHOOTING GUIDE                                                       ║
║  Common errors, causes, and solutions for Odoo module development            ║
║  Organized by error type and affected versions                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Quick Error Lookup Table

| Error Pattern | Likely Cause | Version | Solution |
|---------------|--------------|---------|----------|
| `'api' has no attribute 'multi'` | Using @api.multi | v15+ | Remove decorator |
| `attrs attribute is no longer supported` | Using attrs= | v17+ | Use invisible= |
| `states attribute is not allowed` | Using states= on button | v17+ | Use invisible= |
| `create() takes 2 positional arguments` | Single create() | v17+ | Use @api.model_create_multi |
| `check_company failed` | Cross-company relation | v18+ | Add check_company=True |
| `SQL string query deprecated` | String SQL | v19 | Use SQL() builder |
| `<tree> not recognized` / view parse error | Using `<tree>` tag | v19 | Use `<list>` tag |
| Form renders without chatter | Old chatter div syntax | v19 | Use `<chatter/>` tag |
| `'purchase.order' has no attribute 'refresh'` | Wrong method name | v19 | Use invalidate_recordset() |
| `_read_group() missing argument` | Missing aggregate specs | v19 | Pass `['__count']` as 2nd arg |
| `digits` TypeError / list not accepted | Wrong digits format | v19 | Use tuple (16, 2) or omit |
| `<list> inside One2many` parse error | Inline list in O2m | v19 | Use separate view reference |
| `<dashboard> unknown view type` | Dashboard not in CE | v19 CE | Use form + oe_button_box |
| `External ID not found` | Missing XML reference | All | Check file order in manifest |
| `Access Denied` | Missing security rules | All | Add ir.model.access.csv |
| `KeyError: 'field_name'` | Field not in vals | All | Use .get() or check field |
| `RecursionError` | Circular compute | All | Check @api.depends |
| `MissingError` | Deleted record access | All | Check record.exists() |

## Version-Specific Errors

### v15+ Errors

#### Error: `AttributeError: module 'odoo.api' has no attribute 'multi'`

**Cause**: Using `@api.multi` decorator removed in v15

**Wrong (v14)**:
```python
@api.multi
def action_confirm(self):
    for record in self:
        record.state = 'confirmed'
```

**Correct (v15+)**:
```python
def action_confirm(self):
    for record in self:
        record.state = 'confirmed'
```

**Fix**: Remove all `@api.multi` decorators - they are now the default behavior.

---

### v16+ Errors

#### Error: `DeprecationWarning: attrs attribute is deprecated`

**Cause**: Using `attrs=` in XML views (deprecated in v16, removed in v17)

**Wrong (v14-v15)**:
```xml
<field name="partner_id"
       attrs="{'invisible': [('state', '=', 'draft')]}"/>
```

**Correct (v16+)**:
```xml
<field name="partner_id"
       invisible="state == 'draft'"/>
```

**Fix**: Replace `attrs=` with inline visibility expressions.

---

### v17+ Errors

#### Error: `ValueError: attrs attribute is no longer supported`

**Cause**: `attrs=` completely removed in v17

**Solution**: Same as v16 - use inline expressions

**Additional v17 expressions**:
```xml
<!-- Readonly -->
<field name="amount" readonly="state != 'draft'"/>

<!-- Required -->
<field name="partner_id" required="state == 'confirmed'"/>

<!-- Column invisible in tree -->
<field name="internal_notes" column_invisible="True"/>
```

---

#### Error: `TypeError: create() takes 2 positional arguments but 3 were given`

**Cause**: Using single-record create in v17+ where `@api.model_create_multi` is required

**Wrong (v14-v16)**:
```python
@api.model
def create(self, vals):
    # Single dict
    return super().create(vals)
```

**Correct (v17+)**:
```python
@api.model_create_multi
def create(self, vals_list):
    # List of dicts
    return super().create(vals_list)
```

---

### v18+ Errors

#### Error: `ValidationError: check_company failed`

**Cause**: Related record belongs to different company without proper configuration

**Wrong**:
```python
class MyModel(models.Model):
    _name = 'my.model'

    company_id = fields.Many2one('res.company')
    partner_id = fields.Many2one('res.partner')  # No company check
```

**Correct (v18+)**:
```python
class MyModel(models.Model):
    _name = 'my.model'
    _check_company_auto = True  # Enable automatic checking

    company_id = fields.Many2one('res.company', required=True)
    partner_id = fields.Many2one('res.partner', check_company=True)
```

---

### v19 Errors

#### Error: `DeprecationWarning: SQL string queries are deprecated`

**Cause**: Using string SQL instead of SQL() builder

**Wrong (v14-v18)**:
```python
self.env.cr.execute("""
    SELECT id FROM my_model WHERE state = %s
""", ('draft',))
```

**Correct (v19)**:
```python
from odoo.tools import SQL

self.env.cr.execute(SQL(
    "SELECT id FROM my_model WHERE state = %s",
    'draft'
))
```

---

#### Error: Type hint related warnings

**Cause**: Missing type hints (recommended in v18, required in v19)

**Add type hints**:
```python
def action_confirm(self) -> bool:
    for record in self:
        record.state = 'confirmed'
    return True

@api.model_create_multi
def create(self, vals_list: list[dict]) -> 'MyModel':
    return super().create(vals_list)
```

---

## XML/View Errors

### Error: `ValueError: External ID not found in the system: module.xml_id`

**Cause**: Reference to undefined XML ID (wrong file order in manifest)

**Wrong manifest order**:
```python
'data': [
    'views/my_views.xml',           # References groups
    'security/my_security.xml',     # Groups defined here - TOO LATE!
]
```

**Correct manifest order**:
```python
'data': [
    # 1. Security (groups MUST come first)
    'security/my_security.xml',     # Groups defined
    'security/ir.model.access.csv', # Uses groups

    # 2. Data files
    'data/sequences.xml',

    # 3. Views (may use groups)
    'views/my_views.xml',

    # 4. Menus (use views/actions)
    'views/menuitems.xml',
]
```

---

### Error: `lxml.etree.XMLSyntaxError: Opening and ending tag mismatch`

**Cause**: Malformed XML

**Common mistakes**:
```xml
<!-- Wrong: Self-closing with content -->
<field name="name"/>Some text</field>

<!-- Correct -->
<field name="name">Some text</field>

<!-- Wrong: Unescaped special characters -->
<field name="domain">[('amount', '>', 100) & ('state', '=', 'draft')]</field>

<!-- Correct: Escaped ampersand -->
<field name="domain">[('amount', '>', 100), ('state', '=', 'draft')]</field>
```

---

### Error: `View inheritance may not use attribute 'position'`

**Cause**: Using position without xpath

**Wrong**:
```xml
<record id="view_partner_form_inherit" model="ir.ui.view">
    <field name="name">res.partner.form.inherit</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="base.view_partner_form"/>
    <field name="arch" type="xml">
        <field name="email" position="after">  <!-- Wrong: direct field -->
            <field name="custom_field"/>
        </field>
    </field>
</record>
```

**Correct**:
```xml
<record id="view_partner_form_inherit" model="ir.ui.view">
    <field name="name">res.partner.form.inherit</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="base.view_partner_form"/>
    <field name="arch" type="xml">
        <xpath expr="//field[@name='email']" position="after">
            <field name="custom_field"/>
        </xpath>
    </field>
</record>
```

---

## Security Errors

### Error: `AccessError: You are not allowed to access 'Model Name' (my.model) records`

**Cause**: Missing access rights in ir.model.access.csv

**Solution**: Create/update security file

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,base.group_user,1,1,1,0
access_my_model_manager,my.model.manager,model_my_model,my_module.group_manager,1,1,1,1
```

**Checklist**:
- [ ] Model name uses dots: `my.model` → `model_my_model`
- [ ] CSV is in manifest 'data' list
- [ ] Security file comes after groups XML
- [ ] Group external ID is correct

---

### Error: `AccessError: The requested operation cannot be completed due to security restrictions`

**Cause**: Record rules blocking access

**Debug steps**:
```python
# Check user's groups
self.env.user.groups_id.mapped('full_name')

# Check record rules for model
rules = self.env['ir.rule'].search([
    ('model_id.model', '=', 'my.model')
])
for rule in rules:
    print(f"{rule.name}: {rule.domain_force}")

# Test with sudo to confirm it's a security issue
records = self.env['my.model'].sudo().search([])
```

---

## ORM Errors

### Error: `KeyError: 'field_name'` in create/write

**Cause**: Accessing field that may not be in vals

**Wrong**:
```python
@api.model_create_multi
def create(self, vals_list):
    for vals in vals_list:
        if vals['state'] == 'draft':  # KeyError if not provided
            vals['date'] = fields.Date.today()
    return super().create(vals_list)
```

**Correct**:
```python
@api.model_create_multi
def create(self, vals_list):
    for vals in vals_list:
        if vals.get('state') == 'draft':  # Safe access
            vals['date'] = fields.Date.today()
    return super().create(vals_list)
```

---

### Error: `RecursionError: maximum recursion depth exceeded`

**Cause**: Circular dependency in computed fields or infinite loop

**Common causes**:

1. **Computed field depends on itself**:
```python
# Wrong
total = fields.Float(compute='_compute_total', store=True)

@api.depends('total')  # Depends on itself!
def _compute_total(self):
    pass
```

2. **Write triggering itself**:
```python
# Wrong
def write(self, vals):
    res = super().write(vals)
    self.write({'computed_date': fields.Date.today()})  # Infinite loop!
    return res

# Correct
def write(self, vals):
    if 'computed_date' not in vals:
        vals['computed_date'] = fields.Date.today()
    return super().write(vals)
```

3. **Circular computed dependencies**:
```python
# Wrong
field_a = fields.Float(compute='_compute_a', store=True)
field_b = fields.Float(compute='_compute_b', store=True)

@api.depends('field_b')
def _compute_a(self):
    pass

@api.depends('field_a')  # Circular!
def _compute_b(self):
    pass
```

---

### Error: `MissingError: Record does not exist or has been deleted`

**Cause**: Accessing deleted record

**Wrong**:
```python
def process_records(self):
    for record in self:
        record.unlink()
        print(record.name)  # MissingError!
```

**Correct**:
```python
def process_records(self):
    for record in self:
        name = record.name  # Read before delete
        record.unlink()
        print(name)

# Or check existence
def safe_access(self, record_id):
    record = self.browse(record_id)
    if record.exists():
        return record.name
    return False
```

---

### Error: `psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint`

**Cause**: SQL constraint violation

**Debug**:
```python
# Check existing records
existing = self.search([('code', '=', vals.get('code'))])
if existing:
    raise UserError(f"Code {vals.get('code')} already exists!")
```

**Prevention**:
```python
_sql_constraints = [
    ('code_uniq', 'unique(code, company_id)',
     'Code must be unique per company!'),
]
```

---

## Performance Errors

### Error: Slow page load / timeout

**Cause**: N+1 query problem

**Detect**: Enable SQL logging
```
# In odoo.conf
log_level = debug_sql
```

**Wrong**:
```python
for order in orders:
    print(order.partner_id.name)  # Query per order
```

**Correct**:
```python
orders.mapped('partner_id')  # Prefetch all partners
for order in orders:
    print(order.partner_id.name)  # No additional queries
```

---

### Error: `MemoryError` or server crash

**Cause**: Loading too many records

**Wrong**:
```python
all_records = self.search([])  # Millions of records
for record in all_records:
    process(record)
```

**Correct**:
```python
batch_size = 1000
offset = 0
while True:
    records = self.search([], limit=batch_size, offset=offset)
    if not records:
        break
    for record in records:
        process(record)
    self.env.cr.commit()
    self.env.invalidate_all()
    offset += batch_size
```

---

## OWL Component Errors

### v15 OWL 1.x Errors

#### Error: `Component is not defined`

**Cause**: Missing import or wrong class name

```javascript
// Wrong
class MyComponent extends Component { }

// Correct
const { Component } = owl;
class MyComponent extends Component { }
```

### v16-v18 OWL 2.x Errors

#### Error: `Cannot read property 'render' of undefined`

**Cause**: Component not properly registered

```javascript
// Ensure registration
import { registry } from "@web/core/registry";
registry.category("actions").add("my_action", MyComponent);
```

### v19 OWL 3.x Errors

#### Error: `Invalid hook call`

**Cause**: Using hooks outside setup()

**Wrong**:
```javascript
class MyComponent extends Component {
    myState = useState({ value: 0 });  // Wrong place
}
```

**Correct**:
```javascript
class MyComponent extends Component {
    setup() {
        this.state = useState({ value: 0 });
    }
}
```

---

## Module Installation Errors

### Error: `Module not found` or `No module named`

**Checklist**:
- [ ] Module folder is in addons path
- [ ] `__manifest__.py` exists (not `__openerp__.py`)
- [ ] `__init__.py` imports all Python files
- [ ] Module name matches folder name
- [ ] No syntax errors in Python files

**Verify addons path**:
```bash
./odoo-bin --addons-path=/path/to/addons -d testdb -i my_module
```

---

### Error: `ParseError: "..." while parsing`

**Cause**: Syntax error in Python or XML

**Debug Python**:
```bash
python3 -m py_compile /path/to/module/models/my_model.py
```

**Debug XML**:
```bash
xmllint --noout /path/to/module/views/my_views.xml
```

---

## Database Errors

### Error: `relation "table_name" does not exist`

**Cause**: Table not created (model not installed)

**Solutions**:
1. Run module upgrade: `-u my_module`
2. Check `_name` matches expected table
3. Verify `_auto = True` (default)

---

### Error: `column "field_name" does not exist`

**Cause**: Field added but module not upgraded

**Solution**:
```bash
./odoo-bin -d mydb -u my_module --stop-after-init
```

---

## Debug Techniques

### Enable Developer Mode

```python
# In shell
self.env['ir.config_parameter'].set_param('web.base.url', 'http://localhost:8069')
```

Or: Settings → Activate Developer Mode

### Shell Debugging

```bash
./odoo-bin shell -d mydb

# In shell
>>> record = env['my.model'].browse(1)
>>> record.read()
>>> env['ir.model.access'].search([('model_id.model', '=', 'my.model')])
```

### Logging

```python
import logging
_logger = logging.getLogger(__name__)

def my_method(self):
    _logger.info("Starting method with %s records", len(self))
    _logger.debug("Values: %s", self.read())
    _logger.warning("Potential issue detected")
    _logger.error("Something went wrong: %s", error)
```

### SQL Debugging

```python
# Log all SQL
import logging
logging.getLogger('odoo.sql_db').setLevel(logging.DEBUG)

# Count queries
from odoo.tests.common import QueryCounter
with QueryCounter(self.env.cr) as qc:
    # Your code
    pass
print(f"Queries: {qc.count}")
```

---

---

## v19-Specific Runtime Errors

### Error: `states` attribute is not allowed on button elements

**Cause**: `states` attribute removed in v17+ for buttons (and all elements)

**Wrong (v14-v16)**:
```xml
<button name="action_confirm" string="Confirm" states="draft"/>
```

**Correct (v17+)**:
```xml
<button name="action_confirm" string="Confirm" invisible="state != 'draft'"/>
```

---

### Error: `<tree>` element not recognized / view parse error in v19

**Cause**: `<tree>` renamed to `<list>` in v19; `view_mode='tree,form'` also invalid

**Wrong (v14-v18)**:
```xml
<tree>...</tree>
<!-- and in actions: -->
<field name="view_mode">tree,form</field>
```

**Correct (v19)**:
```xml
<list>...</list>
<!-- and in actions: -->
<field name="view_mode">list,form</field>
```

---

### Error: Form renders without chatter / messaging section missing

**Cause**: v19 requires `<chatter/>` self-closing tag instead of the old `<div class="oe_chatter">` block

**Wrong (v14-v18 style in v19 context)**:
```xml
<div class="oe_chatter">
    <field name="message_follower_ids"/>
    <field name="activity_ids"/>
    <field name="message_ids"/>
</div>
```

**Correct (v19)**:
```xml
<chatter/>
```

Place `<chatter/>` after `</sheet>`, before `</form>`.

---

### Error: `ir.cron` field AttributeError — `numbercall`, `hour`, `minute` not found

**Cause**: `ir.cron` was restructured in v19 — it now fully inherits `ir.actions.server` and no longer
has `numbercall`, `hour`, `minute`, `dayofweek`, etc. as direct fields.

**Wrong (v14-v18)**:
```xml
<record id="my_cron" model="ir.cron">
    <field name="name">My Scheduled Action</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="code">model.action_run()</field>
    <field name="interval_number">1</field>
    <field name="interval_type">days</field>
    <field name="numbercall">-1</field>
</record>
```

**Correct (v19)**: Use `ir.actions.server` schedule fields — check official v19 `ir.cron` definition for the current field API.

---

### Error: `AttributeError: 'purchase.order' object has no attribute 'refresh'`

**Cause**: No `refresh()` method exists on Odoo models; `invalidate_recordset()` is the correct way to clear the ORM cache.

**Wrong**:
```python
order.refresh()
```

**Correct**:
```python
order.invalidate_recordset()
```

---

### Error: `_read_group() missing 1 required positional argument` or wrong result count

**Cause**: `_read_group` API changed in v19 — requires explicit aggregate specifications

**Wrong (v14-v18)**:
```python
result = self.env['my.model']._read_group([('state', '=', 'draft')], ['state'])
```

**Correct (v19)**:
```python
result = self.env['my.model']._read_group(
    [('state', '=', 'draft')],
    groupby=['state'],
    aggregates=['__count'],
)
```

---

### Error: `TypeError: digits argument must be a tuple, not list`

**Cause**: `digits` parameter on Float fields does not accept lists or named tuples like `[('Tax Rate', 2)]`

**Wrong**:
```python
amount = fields.Float(digits=[('Tax Rate', 2)])
tax_rate = fields.Float(digits=('Tax Rate', 2))  # named tuple also wrong
```

**Correct**:
```python
amount = fields.Float(digits=(16, 2))   # simple (total_digits, decimal_places)
# or omit for default precision
tax_rate = fields.Float()
# or use a precision parameter name string
tax_rate = fields.Float(digits='Product Price')
```

---

### Error: Inline `<list>` inside One2many field not supported

**Cause**: Inline `<list>` (formerly `<tree>`) directly inside a One2many field definition is not supported in v19.

**Wrong**:
```xml
<field name="line_ids">
    <list editable="bottom">
        <field name="name"/>
    </list>
</field>
```

**Correct**: Define a separate list view and reference it:
```xml
<!-- Separate view definition -->
<record id="my_line_view_list" model="ir.ui.view">
    <field name="name">my.line.list</field>
    <field name="model">my.model.line</field>
    <field name="arch" type="xml">
        <list editable="bottom">
            <field name="name"/>
        </list>
    </field>
</record>

<!-- Reference in parent form -->
<field name="line_ids" mode="list,form"/>
```

---

### Error: `<dashboard>` view type not available / unknown view type

**Cause**: `<dashboard>` is an Enterprise-only view type; not available in Odoo 19 Community Edition.

**Workaround (CE)**: Use a form view with `oe_button_box` for stat buttons / KPI navigation:
```xml
<form>
    <sheet>
        <div class="oe_button_box" name="button_box">
            <button class="oe_stat_button" icon="fa-list">
                <field name="order_count" widget="statinfo" string="Orders"/>
            </button>
        </div>
    </sheet>
</form>
```

---

### Error: `stock.move` field AttributeError — `name`, `quantity_done`, `product_uom_id` wrong

**Cause**: Several `stock.move` fields changed in v19:

| Old field (v14-v18) | v19 replacement |
|---------------------|-----------------|
| `name` | `description_picking` |
| `quantity_done` | `quantity` |
| `product_uom_id` | `product_uom` |

```python
# Wrong (v14-v18)
move.name = "description"
move.quantity_done = 5.0
uom = move.product_uom_id

# Correct (v19)
move.description_picking = "description"
move.quantity = 5.0
uom = move.product_uom
```

---

### Error: `%(xml_id)d` forward reference fails within same XML file

**Cause**: `%(xml_id)d` references that point forward to records defined later in the same XML file fail at load time.

**Wrong**: Defining an action that references a view in the same file, where the view comes after the action.

**Correct**: Split into separate files — define views/actions that are referenced in a file loaded earlier in the manifest:
```python
'data': [
    'views/my_model_views.xml',   # defines the view
    'views/menu_actions.xml',     # references the view — must come AFTER
]
```

---

### Error: `purchase.order.line` field AttributeError — `product_uom`, `taxes_id` not found

**Cause**: `purchase.order.line` field names changed in v19:

| Old field (v14-v18) | v19 replacement |
|---------------------|-----------------|
| `product_uom` | `product_uom_id` |
| `taxes_id` | `tax_ids` |

```python
# Correct (v19)
line.product_uom_id = uom
line.tax_ids = tax_records
```

---

### Error: `purchase.order.date_planned` type mismatch — expected Datetime

**Cause**: `date_planned` on `purchase.order` is a **Datetime** field (not Date) in v19.

```python
# Wrong
order.date_planned = fields.Date.today()

# Correct
order.date_planned = fields.Datetime.now()
# or
from datetime import datetime
order.date_planned = datetime(2026, 6, 16, 12, 0, 0)
```

---

### Error: `res.partner` has no attribute `vendor` — AttributeError

**Cause**: `res.partner.vendor` boolean field was removed in v14+. No direct `vendor` boolean exists.

**Correct approach**:
```python
# Check if partner is a company (closest equivalent)
is_company = partner.is_company

# Or filter by supplier_rank for purchase vendor context
suppliers = self.env['res.partner'].search([('supplier_rank', '>', 0)])
```

---

## Common Fixes Summary

| Problem | Quick Fix |
|---------|-----------|
| Module won't install | Check `__init__.py` imports |
| Fields not showing | Upgrade module, clear cache |
| Access denied | Add ir.model.access.csv |
| View not loading | Check xpath expressions |
| Computed not updating | Check @api.depends |
| Slow performance | Use search_read, prefetch |
| v17+ attrs error | Use inline expressions |
| v17+ create error | Use @api.model_create_multi |
| v18+ company error | Add check_company=True |
| v19 SQL warning | Use SQL() builder |
