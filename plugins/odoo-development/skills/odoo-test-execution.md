---
name: odoo-test-execution
description: Use when running, executing, or debugging automated unit tests and integration tests for Odoo modules.
---

# Odoo Test Execution

## Overview
Executing and validating Odoo tests requires running the python server in a test-enabled mode against a targeted database. This skill covers launching tests, configuring logs, and debugging traceback exceptions.

## When to Use
Use this skill when:
- Running a test suite for a custom or inherited Odoo module.
- Verifying security groups, record rules, or constraints before committing changes.
- Diagnosing Odoo Server Error log messages containing `AssertionError`, `AccessError`, or `ValidationError`.
- Running TDD (Test-Driven Development) cycles on Odoo logic.

---

## Core Command Patterns

### 1. Run All Module Tests (Full Install and Run)
Use this command to install the module on a test database and run its entire test suite.
```powershell
& "C:\Program Files\Odoo 19.0.20260531\python\python.exe" "C:\Program Files\Odoo 19.0.20260531\server\odoo-bin" -c "C:\Program Files\Odoo 19.0.20260531\server\odoo.conf" -d qphatt -i <module_name> --test-enable --stop-after-init
```

### 2. Run Specific Test Class or Tag
Use `--test-tags` to run a subset of tests, bypassing other tests for speed.
```powershell
& "C:\Program Files\Odoo 19.0.20260531\python\python.exe" "C:\Program Files\Odoo 19.0.20260531\server\odoo-bin" -c "C:\Program Files\Odoo 19.0.20260531\server\odoo.conf" -d qphatt --test-tags <module_name>.<TestClass> --stop-after-init
```

### 3. Run Security-Only Tests
```powershell
& "C:\Program Files\Odoo 19.0.20260531\python\python.exe" "C:\Program Files\Odoo 19.0.20260531\server\odoo-bin" -c "C:\Program Files\Odoo 19.0.20260531\server\odoo.conf" -d qphatt --test-tags security --stop-after-init
```

---

## Parsing Log Exceptions

| Log Exception | Meaning / Root Cause | Common Solution |
|---------------|----------------------|-----------------|
| `AssertionError` | Test assertion failed. Logic return value doesn't match expectation. | Check model method logic or test data setup values. |
| `AccessError` | Access rights or Record Rules prevent user from executing CRUD. | Review `security/ir.model.access.csv` or record rules. |
| `ValidationError` | Model constraint violated (e.g. `@api.constrains`). | Ensure test values comply with constraints, or adjust constraints logic. |
| `KeyError` | Missing field, model, or XML ID in environment context. | Verify model `_inherit` syntax or ensure XML data is loaded in manifest. |
| `ProgrammingError` | DB structure out-of-sync or SQL syntax error. | Restart Odoo server and update the module with `-u <module_name>`. |

---

## Common Mistakes

- **Mismatching Database**: Running tests on a production database instead of a test database. This can cause data corruption.
- **Forgetting Module Install (`-i`)**: Tests will not run if the module isn't explicitly flagged for install/update when the database doesn't have it.
- **Missing `@tagged` Decorators**: If tests are not tagged with `'post_install'`, Odoo may run them at install phase before demo data or views are properly compiled.
- **Relying on Outdated Rules**: In Odoo 19, company checks (`_check_company_auto`) are strictly enforced. Standard tests must create records that belong to the correct company context.
