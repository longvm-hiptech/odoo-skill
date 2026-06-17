# Odoo Profiling & Performance Measurement Guide

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ODOO PROFILING GUIDE                                                        ║
║  From basic log reading to embedded profiler + Speedscope                    ║
║  Rule: Measure first, optimize second. Never guess.                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Tool Selection

| Tool | Overhead | When to Use |
|------|----------|-------------|
| Log reading | None | Always — first step |
| Odoo SH Monitoring | None | Cloud deployments, production |
| `kill -3 PID` | Minimal | Production hang / slow operation |
| Embedded profiler | High | Development, reproducing locally |

---

## 1. Log Reading — Profiling 101

The werkzeug access log is always available. Format:

```
2023-11-03 12:46:31,203 123456 INFO openerp werkzeug:
192.168.0.1 - - [03/Nov/2023 12:46:31] "POST
/web/dataset/call_kw/account.move/web_search_read
HTTP/1.0" 200 - 13 0.059 0.015
              ↑        ↑     ↑
           SQL count  SQL   non-SQL
                      time  time (sec)
```

| Field | Meaning | Warning threshold |
|-------|---------|-------------------|
| `13` | Number of SQL queries fired | > 50 → N+1 problem |
| `0.059` | Time spent in SQL (seconds) | High with low count → missing index |
| `0.015` | Time in Python / network (seconds) | High with low count → CPU-heavy code |

Enable in `odoo.conf`:
```ini
log_level = info  # werkzeug lines always appear at INFO
```

---

## 2. Hardcore Profiling — kill -3

Zero-overhead stack trace dump. Works on production with no preparation.

```bash
# Find Odoo PID
ps aux | grep odoo-bin

# Dump stack trace of all threads to odoo.log
kill -3 <PID>
```

Output in `odoo.log`:
- Full Python stack trace of every running thread at that instant
- Shows exactly which function is executing (useful for hung processes)

**Requirements**: System administrator access to the server.

**When to use**: Production slowdown, process appears stuck, need to identify bottleneck without instrumenting code.

---

## 3. Odoo SH Monitoring

Available in Odoo.sh projects under the Monitoring tab.

### Metrics Available

| Metric | Description |
|--------|-------------|
| `odoo.log` statistics | Query counts and total timing aggregated per route |
| Memory metrics | RAM usage over time per worker |
| CPU Consumption | CPU load per process |
| Slowest routes | Top N endpoints by response time |
| Occurrences | How often each route is called |

### Workflow

1. Check **Slowest routes** → identify the bottleneck endpoint
2. Check **odoo.log statistics** → correlate SQL query count with that endpoint
3. Focus optimization on the highest-impact route first

---

## 4. Odoo Embedded Profiler

Built-in profiler accessible in developer mode. **Do not use on production** — significant overhead.

### Activation

Settings → Activate Developer Mode → Debug menu (bug icon) → "Start Profiling"

Or via URL: `?debug=1` then the debug menu.

### Collectors

| Collector | What it captures | Overhead |
|-----------|-----------------|----------|
| Sync (periodic) | Python call stack sampled at intervals | Medium |
| SQL | Every SQL query + its Python call stack | High |

### Viewing Results with Speedscope

Profiler output opens as a flamegraph in Speedscope:
- **X axis** = time (wider bar = more time spent)
- **Y axis** = call stack (top = outermost frame)
- Click to zoom; wide flat bars are optimization targets

### Profiler Pitfalls

| Pitfall | Explanation |
|---------|-------------|
| Interval too low | Causes memory exhaustion — profiler data accumulates faster than GC clears |
| Interval too high | Short-lived functions (< interval) are never sampled |
| SQL collector overhead | Adds call-stack capture per query — avoid for large bulk operations |
| Memory limit for export | Use `--limit-memory-hard` when exporting large Speedscope JSON |
| GC randomness | Python GC can fire mid-profile, adding noise |
| GIL / C calls | C extensions (psycopg2, lxml) don't appear in Python stack traces |
| Cold cache distortion | First request loads assets/views — always profile the **second** request |

---

## 5. Reproducing Issues with odoo-client-lib

Scripted reproduction is more reliable than manual UI testing.

### Install

```bash
pip install odoo-client-lib
```

### Basic Usage

```python
import odoolib

connection = odoolib.get_connection(
    hostname="localhost",
    database="my_db",
    login="my_user",
    password="xxx",
)

user_model = connection.get_model("res.users")
ids = user_model.search([("login", "=", "admin")])
user_info = user_model.read(ids[0], ["name"])
print(user_info["name"])
```

### Why Scripts Beat UI Testing

- Run the exact same operation N times → consistent timing (remove browser/network noise)
- Before/after comparison: run script, apply fix, run again → clear measurement
- Same XMLRPC code path as real API consumers
- Can be used with **OdooLocust** to simulate concurrent users (load testing)

---

## 6. Generating Realistic Test Data

Demo data is too small for performance testing. Real issues only appear at production scale.

```bash
# Generate 1000x the default record count for res.partner
odoo-bin populate -d my_database --models res.partner --factors 1000

# Multiple models at once
odoo-bin populate -d my_database --models res.partner,sale.order --factors 100
```

**Rules:**
- Never use customer production data (privacy + may not be representative size)
- Demo data is designed for UI testing, not volume testing
- Always reproduce and verify the fix against the same data volume as production

---

## Profiling Workflow Checklist

- [ ] Read werkzeug log first — check SQL count and timing split
- [ ] If production issue: use `kill -3` or SH Monitoring (zero overhead)
- [ ] If development: activate embedded profiler, profile the second request
- [ ] Write odoolib script to reproduce before fixing
- [ ] Generate realistic test data with `odoo-bin populate`
- [ ] Measure timing before AND after fix with the same script
- [ ] Verify SQL count dropped (not just wall-clock time)
