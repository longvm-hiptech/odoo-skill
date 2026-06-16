# Odoo Advanced ORM Patterns

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ADVANCED ORM PATTERNS                                                       ║
║  Cache mechanics, write delay, subquery domains, computed field pitfalls     ║
║  Source: Official Odoo Performance Training (Sevestre Vincent, Odoo SA)      ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## ORM Cache Mechanics

Understanding how the ORM cache works is the foundation of writing performant Odoo code.

### How Prefetching Works

```python
foo = my_model.my_field  # Access any field on a record
```

**If in cache** → read from memory (zero SQL queries)

**If not in cache** → prefetch fires:
1. Fetches for the **entire recordset** (up to 2,000 records at once)
2. Fetches **all stored fields** at once
3. Excludes: binary fields, properties, fields with `prefetch=False`
4. Stores all fetched data in memory cache

### The Indexing Anti-Pattern

```python
# WORST — creates a new single-record recordset on each iteration
# self[i] produces a recordset of length 1 → defeats prefetching
@api.depends('name', 'name2')
def _worst_compute(self):
    for i in range(0, len(self)):
        self[i].full_name = f"{self[i].name} {self[i].name2}"
        # Each self[i].name fires a separate query!

# GOOD — iterate over the recordset directly
@api.depends('name', 'name2')
def _compute(self):
    for record in self:
        record.full_name = f"{record.name} {record.name2}"
        # Prefetch fires on first access, cached for all subsequent
```

### Selective Prefetch with fetch()

When a compute method only needs a few fields, pre-declare them to avoid loading all stored fields:

```python
@api.depends('name', 'name2')
def _better_compute(self):
    # Only prefetch 'name' and 'name2' — skip loading 50 other stored fields
    self.fetch({'name', 'name2'})
    for partner in self:
        partner.full_name = f"{partner.name} {partner.name2}"
```

Combined search + selective prefetch:
```python
# One operation: search + load only specified fields
partners = model.search_fetch(domain, {'name', 'name2'})
```

**Warning**: If any downstream compute override or `_inherits` extension accesses a field
NOT in the `fetch()` set, that field will be fetched per-record (not batched). Verify all
compute overrides in the inheritance chain before using `fetch()`.

---

## ORM Write Delay

The ORM does **not** execute SQL immediately when you assign a field value:

```python
myrecord.myfield = 'the_value'  # No SQL query fired here
```

Writes are **grouped and flushed** automatically when:
- ORM needs to read from the DB (to maintain consistency)
- End of the RPC transaction

This is why the ORM is faster than raw SQL for multiple updates to the same record:

```sql
-- Raw SQL in the same transaction: each update is slower than the last
UPDATE res_partner SET name='demo' WHERE id=3;  -- 0.770ms
UPDATE res_partner SET name='demo' WHERE id=3;  -- 7.796ms (10x slower!)

-- ORM: groups both assignments into a single UPDATE at flush time
```

### Explicit Flush

```python
# Flush this recordset's pending writes to DB
self.flush_recordset()

# Flush all pending writes for this model
self.flush_model()

# Flush everything
self.env.flush_all()
```

Use explicit flush before raw SQL queries that need to see pending ORM writes.

---

## Raw SQL — Cache Safety Rules

When mixing ORM and raw SQL, you must manually synchronize the cache:

```python
# BEFORE a raw SELECT — ensure ORM writes are in the DB
self.flush_recordset()

# Execute raw SQL
self.env.cr.execute(SQL("SELECT id, name FROM my_model WHERE state = %s", 'draft'))
results = self.env.cr.dictfetchall()

# AFTER raw UPDATE or DELETE — invalidate the ORM cache
self.invalidate_recordset()    # invalidate only this recordset
self.invalidate_model()        # invalidate all cached records of this model
self.env.invalidate_all()      # invalidate everything
```

### What Raw SQL Bypasses

| Bypassed | Implication |
|----------|-------------|
| Model access rights | Any user can read/write if they can call the method |
| Record rules | No domain filtering applied |
| Python `@api.constrains` | Validation is skipped |
| ORM cache | Must manually flush/invalidate |

**Rule**: Prefer ORM over raw SQL when security matters. Use raw SQL only for bulk performance-critical operations where you control the context.

### SQL vs Python Constraints

| Aspect | SQL Constraints | Python Constraints |
|--------|----------------|-------------------|
| Speed | Faster (DB-enforced) | Slower |
| Safety | Safer — cannot be bypassed by raw SQL | Can be bypassed by raw SQL |
| Update | Harder (requires migration) | Easy |
| Maintenance | Harder | Easy |
| Expressions | Limited (SQL expressions only) | Full ORM toolbox available |

**Guidance**: Use SQL constraints for uniqueness and simple range checks. Use Python constraints when you need ORM access or complex cross-record validation.

---

## Computed Field Pitfalls

### Pitfall 1: Mixing Stored and Non-Stored in Same Compute

```python
# DANGEROUS — can crash production
class Partner(models.Model):
    _inherit = 'res.partner'

    full_name = fields.Char(
        compute='_compute_full_name',
        store=True,         # stored in DB
    )
    full_name_inv = fields.Char(
        compute='_compute_full_name',
        store=False,        # NOT stored — mixed in same method!
    )

# What happens when user requests full_name_inv:
# → triggers _compute_full_name
# → method tries to SET full_name (stored)
# → ORM schedules a DB write
# → triggers another recompute of full_name_inv
# → infinite recursion → crash
```

**Rule**: Never mix `store=True` and `store=False` fields sharing the same compute method.

### Pitfall 2: compute_sudo on Stored Fields

```python
# RISKY: stored field with compute_sudo=True
class Partner(models.Model):
    _inherit = 'res.partner'

    full_name = fields.Char(
        compute='_compute_full_name',
        compute_sudo=True,  # runs as superuser
        store=True,
    )
    full_name_inv = fields.Char(
        compute='_compute_full_name',
        compute_sudo=True,
        store=True,
    )
```

Key facts about stored computed fields:
- Recomputed **only when dependencies change**, regardless of which user triggered it
- With `compute_sudo=True`: runs as admin → sees all records including restricted ones
- The stored value is **shared for all users** — one user's action triggers recompute for everyone

**Rule**: Stored computed fields must be **idempotent** — the same result regardless of who triggers the recompute. If `compute_sudo=True` is needed, ensure the logic is truly user-independent and does not leak security-sensitive data.

---

## Advanced Domain & Search Patterns

### _read_group for Batch Aggregation (v17+ API)

```python
# BAD: N queries inside computed field loop
@api.depends('related_id')
def _compute_count(self):
    for record in self:
        domain = [('related_id', '=', record.id)]
        record.count = other_model.search_count(domain)  # 1 query per record

# GOOD: single query for the entire batch (v17+ _read_group API)
@api.depends('related_id')
def _compute_count(self):
    domain = [('related_id', 'in', self.ids)]
    counts_data = other_model._read_group(
        domain,
        groupby=['related_id'],
        aggregates=['__count'],
    )
    # _read_group returns list of (record, count) tuples
    mapped_data = dict(counts_data)
    for record in self:
        record.count = mapped_data.get(record, 0)
```

### Override _search for Custom Filtering

When an ORM domain field requires complex SQL:

```python
class MyModel(models.Model):
    _name = 'my.model'

    custom_field = fields.Char(
        compute='_compute_custom_field',
        search='_search_custom_field',
    )

    def _search_custom_field(self, operator, value):
        # Use SQL() builder — returns list of matching IDs
        self.env.cr.execute(SQL("""
            SELECT DISTINCT m.id
            FROM my_model m
            JOIN related_table r ON r.model_id = m.id
            WHERE r.value {op} %s
        """.format(op=operator), value))

        return [('id', 'in', [r[0] for r in self.env.cr.fetchall()])]
```

**Warning**: Custom `_search` bypasses record rules. The returned `[('id', 'in', ids)]` domain
will be filtered by record rules in the final `search()` call, so this is usually safe —
but verify if using complex SQL that filters users or companies.

### Subquery Pattern — _search() vs search()

```python
# BAD: Two queries + potentially thousands of IDs passed in memory
lines = Line.search([
    ('product_id', '=', product_id),
    ('product_uom_qty', '>=', 2),
])
orders = Order.search([
    ('line_ids', 'in', lines.ids),  # can be a list of 50k IDs
])

# GOOD: _search() returns a Query object (SQL subquery) — no IDs in memory
line_query = Line._search([
    ('product_id', '=', product_id),
    ('product_uom_qty', '>=', 2),
])
orders = Order.search([
    ('line_ids', 'in', line_query),  # one efficient EXISTS/IN subquery in SQL
])
```

**Why `_search()` is better:**
- Returns a `Query` object (lazy SQL) instead of executing and returning IDs
- No large list of IDs transferred between Python and PostgreSQL
- PostgreSQL can optimize the subquery as a single execution plan
- Respects `_order` only when needed (no useless ORDER BY in the subquery)

### `any` Operator — Best Pattern for Child Matching

```python
# BEST: single SQL statement with EXISTS subquery
orders = Order.search([
    ('line_ids', 'any', [
        ('product_id', '=', product_id),
        ('product_uom_qty', '>=', 2),
    ]),
    ('state', '=', 'sale'),
])
```

`any` compiles to an `EXISTS` subquery — the most efficient SQL pattern for
"find parent records that have at least one matching child record."

**Comparison:**

| Pattern | SQL operations | Memory |
|---------|---------------|--------|
| `search()` → `ids` → `search('in', ids)` | 2 queries + large `IN (...)` list | IDs in Python memory |
| `_search()` → `Query` → `search('in', query)` | 1 query with subquery | No IDs in memory |
| `search('any', subdomain)` | 1 query with EXISTS | No IDs in memory |

### Beware _order with Many2one Fields

```python
class Session(models.Model):
    _name = 'openacademy.session'
    _order = 'course_id, instructor_id, id'
    #         ↑ Many2one field — DANGER
```

Ordering by a Many2one field means PostgreSQL sorts by that model's **own `_order` clause**,
which may itself order by another Many2one — cascading JOINs and sorts.

```python
class Course(models.Model):
    _name = 'openacademy.course'
    _order = 'responsible_id, name, id'
    # responsible_id is also a Many2one → another JOIN!
```

**Solutions:**

```python
# Option 1: Add a stored computed field with the sort key as a plain Char/Int
class Session(models.Model):
    course_name = fields.Char(
        related='course_id.name',
        store=True,
        index=True,
    )
    _order = 'course_name, id'

# Option 2: Accept the overhead if dataset is small (< 10k records)
# Option 3: Use _order = 'id' and sort in Python for small UI lists
```

---

## End-User Anti-Patterns

Performance issues often originate from poorly designed filters that users create in the UI.

| Anti-pattern | Why it's slow | Solution |
|--------------|--------------|---------|
| Filter on tag present in 90% of records | Index barely helps — PostgreSQL prefers seq scan for high-cardinality matches | Filter the 10% without the tag instead |
| Exclude-based filters ("not in EU") | `NOT IN` with large list forces full scan + set subtraction | Restructure to include the target set |
| Filter by M2o name (type-to-search) | `name_search` uses `ILIKE '%text%'` — no standard index can help | Add `index='trigram'` to the target model's name field |

```python
# SLOW: name_search on res.partner.name without trigram index
self.env['sale.order'].search([('partner_id.name', 'ilike', 'Acme')])
# → ILIKE '%Acme%' → seq scan on res_partner

# SOLUTION: add trigram index to the searched model
class ResPartner(models.Model):
    _inherit = 'res.partner'
    name = fields.Char(index='trigram')
    # Now ILIKE '%Acme%' uses the GIN trigram index → fast
```

---

## ORM Performance Quick Reference

| Pattern | Queries | Verdict |
|---------|---------|---------|
| `for r in self: r.field` | 1 prefetch batch | ✅ Best |
| `for i in range(len(self)): self[i].field` | N queries | ❌ Worst |
| `self.fetch({'a', 'b'})` before loop | 1 selective batch | ✅ Best when few fields needed |
| `model.search_fetch(domain, {'a', 'b'})` | 1 combined | ✅ Best for search + read |
| `records.write({'state': 'done'})` | 1 UPDATE | ✅ Best |
| `for r in records: r.state = 'done'` | 0 then 1 flush | ✅ Same as batch write |
| `Line._search(domain)` → `search('in', query)` | 1 subquery | ✅ Best for cross-model |
| `search('any', subdomain)` | 1 EXISTS | ✅ Best for parent/child matching |
| `_read_group(domain, ['id'], ['__count'])` | 1 GROUP BY | ✅ Best for batch aggregation |
| `for r in self: search_count([...r.id...])` | N queries | ❌ Worst in computed fields |
