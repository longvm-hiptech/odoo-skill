# Odoo Development — Claude Code Instructions

You are an expert Odoo Developer. Follow these instructions for all tasks in this workspace.

This repo contains Odoo development patterns in `skills/` and subagent role profiles in `agents/`. Always reference them before writing code.

---

## 1. Core Workflow (MANDATORY)

### Step 1: Detect Odoo Version
Always determine the target version first. Look for `__manifest__.py` in the target module and extract version string. If not found, ask the user.

### Step 2: Load Skill Context
Before writing ANY Odoo code:
- Read `SKILL.md` at root for the master index
- Read the matching version-specific skills from `skills/`:
  - `skills/odoo-version-knowledge.md`
  - `skills/odoo-module-generator.md` (or version-specific variant)
  - `skills/odoo-model-patterns.md`
  - `skills/odoo-security-guide.md`
  - Domain-specific: `skills/xml-view-patterns.md`, `skills/report-patterns.md`, etc.
- Read matching agent profile from `agents/` if task matches a role

### Step 3: Verify Patterns Against Official Odoo
When uncertain about version-specific syntax, verify against the official Odoo GitHub repo:
- Raw URL: `https://raw.githubusercontent.com/odoo/odoo/{version}/addons/{module}/models/{file}`
- Use browser tool or curl to fetch reference files
- **If a skill claim turns out to be wrong → log it in `CORRECTIONS_LOG.md` before continuing** (see Section 8)

### Step 4: Generate Code
Follow version-specific patterns from loaded skills.

### Step 5: Validate
- Check Python syntax
- Check XML validity
- Verify security files are complete
- Run tests if test infrastructure is available

---

## 2. Odoo Coding Conventions (Version-Aware)

### Views
- **v17+:** Use `invisible="state != 'draft'"` NOT `attrs`
- **v16:** Both `attrs` and direct attributes work (but prefer direct)
- **v14-v15:** Use `attrs="{'invisible': [('state', '!=', 'draft')]}"`

### Security
- Every model needs a row in `security/ir.model.access.csv`
- **v18+:** Use `_check_company_auto = True` and `check_company=True` on fields
- **v18+:** Use `allowed_company_ids` in record rules (NOT `company_ids`)

### Python
- **v17+:** Use `@api.model_create_multi` (list of vals)
- **v18+:** Type hints recommended
- **v19+:** Type hints REQUIRED, `SQL()` builder REQUIRED

### x2many
- **v16+:** Use `from odoo import Command` and `Command.create({...})` NOT `(0, 0, {...})`

---

## 3. Subagent Roles (agents/ directory)

Load the appropriate agent profile for specialized tasks:

| Task | Agent File |
|------|-----------|
| Planning & requirement analysis | `agents/odoo-planner.md` |
| Code review & audit | `agents/odoo-code-reviewer.md` |
| Writing & running tests | `agents/odoo-tester.md` |
| Version upgrade analysis | `agents/odoo-upgrade-analyzer.md` |
| Context gathering (pre-code) | `agents/odoo-context-gatherer.md` |
| Finding specific patterns | `agents/odoo-skill-finder.md` |
| PreSale / Solution Consulting (discovery, fit-gap, proposal/SOW, demo, VN compliance) | `agents/odoo-presales-consultant.md` |

---

## 4. Tool Name Mapping

The skill and agent files reference generic tool names. Use these Claude Code equivalents:

| Skill Reference | Claude Code Tool |
|----------------|-----------------|
| `Read [file]` | `read_file()` or `cat` in terminal |
| `Glob [pattern]` | `ls` or `glob` in terminal |
| `Grep [pattern]` | `grep` or `search_files` in terminal |
| `WebFetch [url]` | `curl` in terminal or browser tool |
| `WebSearch [query]` | `web_search` tool |
| `command [cmd]` | `Terminal` or `bash` in terminal |

---

## 5. File Organization (THIS WORKSPACE)

```
./
├── SKILL.md                  ← Entry point (read this first)
├── agents/                   ← Subagent role profiles
│   ├── odoo-planner.md
│   ├── odoo-tester.md
│   ├── odoo-code-reviewer.md
│   ├── odoo-context-gatherer.md
│   ├── odoo-upgrade-analyzer.md
│   └── odoo-skill-finder.md
├── skills/                   ← Odoo pattern files
│   ├── odoo-module-generator-{version}.md
│   ├── odoo-model-patterns-{version}.md
│   ├── odoo-security-guide-{version}.md
│   ├── odoo-owl-components-{version}.md
│   ├── odoo-version-knowledge-{version}.md
│   ├── odoo-performance-guide.md
│   ├── odoo-test-patterns.md
│   ├── odoo-troubleshooting-guide.md
│   ├── odoo-test-execution.md
│   ├── xml-view-patterns.md
│   ├── report-patterns.md
│   ├── wizard-patterns.md
│   ├── field-type-reference.md
│   ├── computed-field-patterns.md
│   ├── onchange-dynamic-patterns.md
│   ├── constraint-patterns.md
│   ├── inheritance-patterns.md
│   ├── controller-api-patterns.md
│   ├── multi-company-patterns.md
│   ├── portal-access-patterns.md
│   ├── website-integration-patterns.md
│   ├── mail-notification-patterns.md
│   ├── cron-automation-patterns.md
│   ├── sale-crm-patterns.md
│   ├── stock-inventory-patterns.md
│   ├── purchase-procurement-patterns.md
│   ├── project-task-patterns.md
│   ├── product-variant-patterns.md
│   └── ... (more domain patterns)
├── commands/                 ← Slash commands (Claude Code plugin)
│   ├── odoo-module.md
│   ├── odoo-review.md
│   ├── odoo-upgrade.md
│   ├── odoo-security.md
│   └── odoo-owl.md
└── scripts/                  ← Helper scripts
```

---

## 6. Requirement Input Handling

When user provides requirements via document (Word, Excel, text):

1. **Parse the document** — read file content, extract entities
2. **Identify models** — list of business objects to model
3. **Identify fields** — field names, types, relationships
4. **Identify workflows** — state transitions, approvals
5. **Identify existing modules** to inherit/extend
6. **Create PLAN.md** — structured implementation plan
7. **Confirm with user** before generating code

---

## 7. Checklist (Every Module)

- [ ] Version identified
- [ ] Version-specific skills loaded
- [ ] Security groups defined
- [ ] `ir.model.access.csv` complete for each model
- [ ] Views use correct syntax for target version
- [ ] Tests generated (if requested)
- [ ] Manifest data order: security → data → views → menus
- [ ] Code validated (Python syntax + XML validity)

---

## 8. Skill Maintenance — Corrections Feedback Loop

### Rule: Log before you fix

Whenever a skill claim in `skills/` is found to be **wrong or outdated** during real dev work:

1. **Do NOT edit the skill file directly** during the dev session.
2. **Append one row** to `CORRECTIONS_LOG.md` (root):

   ```
   | YYYY-MM-DD | skills/file.md | Section | Wrong claim | Correct claim | Source |
   ```

3. Continue the dev task using the correct pattern.
4. When the session ends (or after completing a full module), check `CORRECTIONS_LOG.md`:
   - If ≥ 1 pending row → **suggest running `/odoo-skill-update`** to the user.

### Rule: New runtime error not yet in troubleshooting guide

If you hit a runtime/dev error that is not in `skills/odoo-troubleshooting-guide.md`:

1. Add a row to `CORRECTIONS_LOG.md` with the error + fix (Section = "NEW — troubleshooting-guide").
2. `/odoo-skill-update` will promote it to the guide on the next run.

### `/odoo-skill-update` command

See `commands/odoo-skill-update.md` for the full flow. In short:

```
Read CORRECTIONS_LOG → Verify claims vs GitHub source → Patch skill files
→ Prune duplicate troubleshooting entries → Clear log → Open PR to main
```

Run: after completing a module, or when CORRECTIONS_LOG has ≥ 3 pending rows, or monthly.

### Version file structure (do not consolidate)

Each Odoo version keeps its own skill files (`-18.md`, `-19.md`, `-18-19.md` for migration notes).
Do NOT merge version files — breaking changes between versions make them incompatible.
Staleness sweeps (version headers, GitHub branch names) are handled automatically by `/odoo-skill-update`.
