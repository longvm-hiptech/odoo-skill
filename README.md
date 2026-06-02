# Odoo Development Skill & Multi-Agent Workspace

🚀 **A standardized, multi-agent workspace for advanced Odoo development, planning, testing, and security review across versions 14 to 19.**

This repository follows the clean directory conventions popularized by frameworks like `obra/superpowers` to ensure 100% compatibility with auto-discovery, custom commands, and subagent orchestration in modern AI coding agents and IDEs.

---

## 📂 Repository Structure

The workspace is organized to promote the Odoo development skills, agents, commands, and scripts directly to the root, preventing nested lookup issues and allowing instant discovery:

```
.
├── SKILL.md                      # Main Odoo Development Skill with YAML frontmatter
├── skills/                       # Curated Odoo pattern markdown guides (120+ files)
├── agents/                       # Specialized subagent system profiles (e.g. planner, reviewer)
├── commands/                     # Slash commands for custom agent tasks
├── scripts/                      # Executable helper scripts (e.g. run_tests.py)
├── qms_sop_management/           # The target Odoo module under active development
├── docs/                         # Documentation, guides, and archives (e.g. token-killer guide)
│   └── token-killer/             # Standalone OTK guide (kept separate from active dev)
├── data/                         # [Ignored] Private files and requirements specification
└── git_repo/                     # [Ignored] Legacy nested development files
```

---

## 🛠️ Multi-Agent Setup Guide

Here is how to configure and load this repository with various AI agents and IDEs:

### 1. Claude Code
Claude Code automatically discovers root-level `skills/`, `agents/`, `commands/`, and `scripts/`. We also provide a manifest under `.claude-plugin/plugin.json`:
* **Installation (Local)**: Claude Code will automatically read and load this plugin on start in this workspace.
* **Usage**: You can execute custom commands like `/odoo-test` or spawn subagents directly.

### 2. Cursor IDE
Cursor uses the root `.cursorrules` to feed instructions into its inline and chat models:
* Cursor reads `.cursorrules` on startup. It is configured to direct the model to retrieve context from the `/skills/` directory before writing code.
* **Usage**: Just open this folder in Cursor and talk to the AI. It will use the local knowledge base.

### 3. VS Code & GitHub Copilot
GitHub Copilot reads custom instructions from `.vscode/copilot-instructions.md`:
* We have created `.vscode/copilot-instructions.md` directing Copilot Chat to read Odoo patterns from the `/skills/` directory.

### 4. Codex
Codex utilizes the `.codex-plugin/plugin.json` configuration manifest at the root:
* Codex will load the plugin and make all Odoo code patterns available in its context window.

### 5. Gemini Code Assist & Antigravity
The workspace is configured with `gemini-extension.json`:
* This file links the model directly to the root `SKILL.md` index and `/skills/` directory, allowing Gemini/Antigravity to use local tool configurations and code runners.

### 6. OpenClaw
OpenClaw loads system instructions using `openclaw-agent.json`:
* The configuration registers our root `SKILL.md` as the system instruction and exposes the `skills/` directory and test runners (`scripts/run_tests.py`) as tools.

### 7. Hermes
Hermes uses the configuration file `hermes-agent.json` to load the specialist profile, mapping all Odoo code guides as context sources.

---

## 💾 Test Verification

A custom dynamic Python runner is located at `scripts/run_tests.py`.
To validate custom Odoo logic (e.g., `qms_sop_management` or other models):
```bash
python scripts/run_tests.py
```
This script dynamically sets up custom test execution overrides and checks Odoo modules inside this workspace.
