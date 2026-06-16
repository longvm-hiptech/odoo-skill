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
| 2026-06-16 | `skills/odoo-version-knowledge-19.md` | Version Overview + GitHub Verification URLs | "v19 in development, Release Oct 2024 (Expected), verify against `master` branch" | Odoo 19.0 is released (stable); use branch `19.0` not `master` | Odoo ships yearly Oct; today is 2026-06-16 |
| 2026-06-16 | `skills/odoo-version-knowledge-18-19.md` | GitHub Verification URLs | Verification URLs point to `master` for v19 | Should point to `19.0` branch | Same as above |

---

## Applied Corrections

<!-- After /odoo-skill-update PR is merged, move resolved rows here (add "Applied" date).
     Rows older than 90 days are deleted on next /odoo-skill-update cycle. -->

| Date Logged | Date Applied | Skill File | Change |
|------------|-------------|-----------|--------|

