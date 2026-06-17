# PostgreSQL Indexing Guide for Odoo

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  POSTGRESQL INDEXING GUIDE                                                   ║
║  EXPLAIN, index types, Odoo-specific patterns, cost trade-offs               ║
║  Source: Official Odoo Performance Training (Sevestre Vincent, Odoo SA)      ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Why Indexing Matters

Without an index, PostgreSQL performs a **Sequential Scan** — it reads every row in the table.
On a table with 10 million rows, a seq scan on an unindexed column can take seconds.

---

## EXPLAIN — Analyzing Query Plans

Always analyze before adding an index. Adding indexes without EXPLAIN is guessing.

```sql
-- Shows the plan without executing (safe on production)
EXPLAIN SELECT name, color FROM people WHERE color = 'Blue';

-- Executes and shows actual timing (use on dev/staging)
EXPLAIN ANALYZE SELECT name, color FROM people WHERE color = 'Blue';

-- Full diagnostics — recommended for complex queries
EXPLAIN (ANALYZE, BUFFERS, COSTS, VERBOSE)
    SELECT name, color FROM people WHERE color = 'Blue';
```

For complex plans, paste the output into: **https://explain.dalibo.com**

### Reading the Plan

```
QUERY PLAN
-------------------------------------------------------
Seq Scan on people  (cost=0.00..1880701.60 rows=1 width=36)
  Filter: ((color)::text = 'Blue'::text)
```

| Node type | Meaning |
|-----------|---------|
| `Seq Scan` | Full table scan — candidate for indexing |
| `Index Scan` | Using an index to locate rows then fetching from table |
| `Index Only Scan` | Index contains all needed data — never touches main table |
| `Bitmap Heap Scan` | Index used to build bitmap, then table fetched in order |
| `Nested Loop` / `Hash Join` | JOIN strategies — check JOIN columns are indexed |

**Cost field**: `cost=start..total` — higher total = more expensive. Compare before/after.

---

## When PostgreSQL Uses an Index (Urban Legend Debunked)

**Myth**: "Adding an index makes PostgreSQL use it."

**Reality**: PostgreSQL uses the query planner with statistics to decide:

| Statistic | What PostgreSQL tracks |
|-----------|----------------------|
| Row buckets | Distribution of values across equal-sized buckets |
| Most frequent values | Top N values and their frequencies |
| NULL proportion | Fraction of NULL entries |

**PostgreSQL will NOT use an index when:**
- The index filters very few rows (e.g., index on `active` where 99% are `True` — seq scan is cheaper)
- Table is small (< ~1,000 rows — seq scan fits in memory)
- Field values are correlated with physical row order
- The index is on a column used with a non-supported operator

**Always verify with `EXPLAIN ANALYZE` after adding an index.**

---

## Index Types

### 1. Standard (B-tree)

```sql
CREATE INDEX people_color_idx ON people (color);
```

### 2. Unique Index

```sql
CREATE UNIQUE INDEX people_email_idx ON people (email);
```

- Enforces that no two rows have the same value
- Automatically created for PRIMARY KEY and UNIQUE constraints

### 3. Compound Index

```sql
-- Column ORDER MATTERS
CREATE INDEX people_color_name_idx ON people (color, name);
```

**The left-prefix rule:**
A compound index on `(x, y, z)` will be used for queries filtering on:
- `x` ✅
- `x, y` ✅
- `x, y, z` ✅
- `y` ❌ (not the leftmost column)
- `z` ❌
- `y, z` ❌

**Guidance:** Put the most-selective column (most distinct values) first. A compound index is usually better than two single-column indexes when queries consistently filter on both columns.

### 4. Partial Index

```sql
-- Only index rows where active = True (much smaller index)
CREATE INDEX people_active_color_idx ON people (color)
WHERE active = True;
```

**When to use:**
- Table has many rows but queries only touch a subset (e.g., `state IN ('draft', 'open')`)
- Dramatically reduces index size and write overhead
- The WHERE condition does not need to appear in the query — only the indexed column does

### 5. Covering Index

```sql
-- Includes extra columns so the query never touches the main table
CREATE INDEX people_color_cover_idx ON people (color) INCLUDE (id, name);
```

**When to use:** Your query only needs columns available in the index → PostgreSQL uses an **Index Only Scan** (fastest possible, avoids heap fetch entirely).

### 6. Functional Index

```sql
-- Standard index — NOT used for LOWER(color) queries
CREATE INDEX people_color_idx ON people (color);

-- Functional — indexes the transformed value
CREATE INDEX people_color_lower_idx ON people (LOWER(color));
```

**Rules:**
- Only used when the query applies the **same function**: `WHERE LOWER(color) = 'blue'`
- Function must be **immutable** (same input always produces same output)
- Type conversion is implicitly a function — watch out for implicit casts breaking index usage

---

## PostgreSQL Index Methods

| Method | Command | Best for |
|--------|---------|----------|
| **B-tree** | `USING btree` (default) | Equality, range, ORDER BY, IN, BETWEEN |
| **GIN + Trigram** | `USING gin(col gin_trgm_ops)` | LIKE, ILIKE, regex, similarity |
| **Hash** | `USING hash` | Equality only (=) — slightly faster than B-tree for pure equality |
| **BRIN** | `USING brin` | Very large tables with natural ordering (timestamps, sequential IDs) |
| **GiST** | `USING gist` | Geometric/geographic, range types, full-text |
| **SP-GiST** | `USING spgist` | Non-balanced structures (IP ranges, phone numbers) |
| **Bloom** | `USING bloom` | Multi-column equality queries with low cardinality |

### B-tree (default — use for most cases)

```sql
CREATE INDEX people_color_idx ON people (color);
-- Equivalent:
CREATE INDEX people_color_idx ON people USING btree(color);
```

Supports: `=`, `<`, `>`, `<=`, `>=`, `BETWEEN`, `IN`, `IS NULL`, `ORDER BY`, `LIKE 'prefix%'`

### GIN + Trigram (for text search / ILIKE)

```sql
-- Enable extension once per database
CREATE EXTENSION pg_trgm;

-- Create trigram index
CREATE INDEX people_name_trgm_idx ON people USING gin(name gin_trgm_ops);
```

- Supports `LIKE '%text%'`, `ILIKE '%text%'`, `~` regex, similarity functions
- Larger index than B-tree
- In Odoo: `index='trigram'` handles this automatically

---

## Indexing in Odoo

### Field-Level `index` Attribute

```python
class MyModel(models.Model):
    _name = 'my.model'

    # B-tree index (standard)
    state = fields.Selection([...], index=True)           # or index='btree'
    company_id = fields.Many2one('res.company', index=True)
    date = fields.Date(index=True)

    # Exclude NULLs — smaller, faster for optional/sparse fields
    reference = fields.Char(index='btree_not_null')

    # Trigram — enables efficient ILIKE / name_search
    name = fields.Char(index='trigram')

    # No index (default)
    notes = fields.Text()
```

### Class-Level Unique Index (v17+)

```python
class MyModel(models.Model):
    _name = 'my.model'

    # Replaces _sql_constraints unique entries in v19+
    _name_company_uniq = models.UniqueIndex(
        '(name, company_id)',
        "Name must be unique per company",
    )
```

### Custom Indexes via `init()` Method

For Partial, Covering, Functional, or multi-operator indexes not expressible via field attributes:

```python
class MyModel(models.Model):
    _name = 'my.model'

    def init(self):
        # Partial index — only active records
        self.env.cr.execute("""
            CREATE INDEX IF NOT EXISTS my_model_active_state_idx
            ON my_model (state)
            WHERE active = True
        """)

        # Trigram with unaccent support
        self.env.cr.execute("""
            CREATE INDEX IF NOT EXISTS my_model_name_trgm_idx
            ON my_model USING gin(name gin_trgm_ops)
        """)

        # Covering index for frequent read-only queries
        self.env.cr.execute("""
            CREATE INDEX IF NOT EXISTS my_model_covering_idx
            ON my_model (company_id, state)
            INCLUDE (name, partner_id)
            WHERE active = True
        """)

        super().init()
```

### translate=True Fields

Fields with `translate=True` store data as JSONB. Trigram indexes on translated fields
use `jsonb_path_query_array` — Odoo handles this automatically when `index='trigram'`
is set on a translated field. Odoo also integrates with the `unaccent` extension for
accent-insensitive searches.

---

## Cost of Indexes

| Aspect | Impact |
|--------|--------|
| Read (SELECT) | ↑ Faster — index lookup replaces seq scan |
| Write (INSERT/UPDATE/DELETE) | ↓ Slower — every write must update index structures |
| Storage | Index is a stored data structure — adds disk and RAM usage |
| Planner decision | Even if present, may not be used (statistics-based decision) |

**Rule: Only add indexes that are actually used.** Over-indexing slows writes with no benefit.

---

## Quick Tips (from Odoo Tech Team)

| Tip | Explanation |
|-----|-------------|
| Seq scan filters most rows | If a seq scan skips > 90% of rows, that's an index candidate |
| `id` vs `TId` | Accessing by `id` (PK, always indexed) is always fast; raw `TId` is not |
| Compound vs multiple | Compound `(a, b)` is usually better than two indexes `(a)` + `(b)` when queries filter both |
| Boolean/Selection | Usually NOT worth indexing — use a **partial index** instead (e.g., `WHERE state = 'draft'`) |
| B-tree ORDER | B-tree supports `ORDER BY col ASC/DESC` — index ORDER BY columns in list views |
| JOIN columns | Index the foreign key on the "many" side of every JOIN |
| Sparse M2o fields | Use partial index `WHERE col IS NOT NULL` for optional Many2one fields |
| CASCADE triggers | FK CASCADE deletes update child table indexes — profile CASCADE operations on write-heavy tables |
| translate=True | `index='trigram'` on a translated field requires special jsonb handling — let Odoo do it automatically |

---

## Indexing Checklist

- [ ] Run `EXPLAIN ANALYZE` before adding any index
- [ ] Index all fields used in `search()` domains and record rules
- [ ] Index Many2one FK fields on the "many" side (if used in search/filter)
- [ ] Use `index='btree_not_null'` for optional fields to reduce index size
- [ ] Use `index='trigram'` on Char fields used for name_search / ILIKE
- [ ] Add compound index for queries that always filter on multiple columns
- [ ] Use partial index for filtered subsets (active records, specific states)
- [ ] Run `EXPLAIN ANALYZE` again after adding index to confirm it's used
- [ ] Monitor write performance after adding indexes on high-write tables
