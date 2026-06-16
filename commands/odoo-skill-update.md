---
name: odoo-skill-update
description: |
  Invoke to close the skill feedback loop: verify pending corrections in CORRECTIONS_LOG.md
  against official Odoo GitHub source, patch the affected skill files, prune stale entries from
  odoo-troubleshooting-guide.md, clear the log, and open a PR to main.
  Also performs a staleness sweep of all version-knowledge headers.
  Trigger: "update skill", "fix skill", "skill corrections", "/odoo-skill-update",
  or automatically after completing a module if CORRECTIONS_LOG has pending rows.
arguments:
  - name: verify_only
    description: "true = report what would change without patching files (default: false)"
    required: false
input_examples:
  - description: "Apply all pending corrections and open PR"
    arguments: {}
  - description: "Dry-run — show what would be patched without writing files"
    arguments:
      verify_only: "true"
---

# /odoo-skill-update Command

Closes the feedback loop: errors discovered during real dev work → verified → patched into
skill files → PR to main → corrections log cleared.

---

## Execution Flow

### Step 1: Load input

1. Read `CORRECTIONS_LOG.md` — collect all rows under **Pending Corrections**.
2. Read `skills/github-verification-guide.md` — get the correct GitHub branch per Odoo version.
3. If Pending Corrections is empty, proceed to Step 3 (staleness sweep) only.

---

### Step 2: Verify each pending correction

For each row in Pending Corrections:

1. Determine the GitHub raw URL from `github-verification-guide.md`:
   - Pattern: `https://raw.githubusercontent.com/odoo/odoo/{branch}/{path}`
   - v19 → branch `19.0` (not `master`, unless the stable branch does not yet exist)
2. Fetch the relevant section or file to confirm the correct claim.
3. Label the row:
   - ✅ **Verified** — source confirms the correction is right → add to patch list.
   - ⚠️ **Disputed** — source is ambiguous or contradicts the correction → keep in Pending, add `[NEEDS HUMAN REVIEW]` marker, skip patching.
   - ❌ **Wrong correction** — source shows the original claim was right → remove from Pending, add explanation comment.

---

### Step 3: Staleness sweep (always run)

For every file matching `skills/odoo-version-knowledge-*.md`:

1. Read the **Version Overview** table — check "Release Date" and "Status".
   - If Status is "In Development" but (today − expected release date) > 6 months → flag: update Status to "Stable" and update branch reference.
2. Read **GitHub Verification URLs** section — if any URL references `master` for a version with a known stable branch → flag: replace `master` with the version branch (e.g. `19.0`).
3. Add all flagged items to the patch list automatically (no manual verification needed for date/branch staleness).

---

### Step 4: Patch skill files (skip if `verify_only=true`)

For each ✅ Verified correction and each staleness flag:

1. Edit the target skill file — replace the stale/wrong text with correct info.
2. If the file has a "Last verified" date in its header, update it to today; otherwise add:
   ```
   > Last verified: YYYY-MM-DD against branch {branch}
   ```

---

### Step 5: Prune `odoo-troubleshooting-guide.md`

1. For each error in `odoo-troubleshooting-guide.md`, check if the same error pattern is **fully explained with a code example** in the relevant version-knowledge or model-patterns skill file.
2. If **fully covered** → replace the troubleshooting entry body with a one-liner:
   ```
   → See: `skills/odoo-version-knowledge-19.md#common-issues`
   ```
   Keep the error heading and Quick Error Lookup table row so the guide remains scannable.
3. **Keep** entries for:
   - Runtime / environment errors (module install, DB, server config) not covered in skill files.
   - ORM errors (recursion, MissingError, N+1) that are dev-pattern errors, not version-syntax.
   - Any entry that provides concrete debug steps not elsewhere documented.

---

### Step 6: Update `CORRECTIONS_LOG.md`

1. Move all ✅ patched rows from **Pending Corrections** to **Applied Corrections**, adding today's date in "Date Applied".
2. Delete any row in Applied Corrections where Date Applied is older than **90 days** (info is now in skill files — log entry is clutter).
3. Leave ⚠️ Disputed rows in Pending with `[NEEDS HUMAN REVIEW]` marker.

---

### Step 7: Commit, push, create PR

1. Stage all changed files:
   - Modified skill files
   - `CORRECTIONS_LOG.md`
   - `skills/odoo-troubleshooting-guide.md` (if pruned)
2. Commit:
   ```
   fix(skills): apply corrections + staleness fixes (YYYY-MM-DD)

   - {N} corrections verified and applied
   - Staleness sweep: updated {X} version headers
   - Troubleshooting guide: pruned {Y} entries now covered in skill files
   ```
3. Push to branch `skill-update/YYYY-MM-DD`.
4. Open PR targeting `main`:
   - **Title**: `Skill update: {N} corrections + {X} staleness fixes ({date})`
   - **Body**: table of patched files, list corrections applied, flag any Disputed items needing human review.

---

## AI Agent Instructions

1. **READ**: `CORRECTIONS_LOG.md` → get pending rows; `github-verification-guide.md` → get branch map
2. **VERIFY**: fetch GitHub raw source for each pending correction; label ✅ / ⚠️ / ❌
3. **SWEEP**: check all `odoo-version-knowledge-*.md` for stale Status / branch references
4. **PATCH**: edit skill files for all ✅ items + staleness fixes
5. **PRUNE**: replace fully-duplicated troubleshooting entries with cross-references
6. **CLEAR**: update `CORRECTIONS_LOG.md` (move to Applied; delete > 90 days)
7. **PR**: commit → push `skill-update/{date}` → open PR to main; list Disputed items in PR body

---

## When to Run

| Trigger | Who |
|---------|-----|
| `CORRECTIONS_LOG.md` has ≥ 3 pending rows | Agent (proactive, end of session) |
| User types `/odoo-skill-update` | User |
| After completing a full module (`PLAN.md` all tasks done) | Agent (suggest to user) |
| Monthly cadence | User / scheduled |
