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
├── qms_sop_management/           # [Ignored] The target Odoo module under active development
├── docs/                         # Documentation, guides, and archives (e.g. token-killer guide)
│   └── token-killer/             # Standalone OTK guide (kept separate from active dev)
├── data/                         # [Ignored] Private files and requirements specification
└── git_repo/                     # [Ignored] Legacy nested development files
```

---

## 🤝 PreSale / Solution Consulting Track

Bên cạnh nhánh **Developer** (sinh module, pattern code...), workspace này có thêm nhánh **PreSale / Solution Consulting** dành cho đội tư vấn giải pháp tại Việt Nam — từ khảo sát khách hàng đến bàn giao cho đội Dev:

```
Discovery → Solution Mapping & Fit-Gap → Demo → Estimation & Proposal/SOW
   → (VN Compliance check nếu cần) → Handoff (REQUIREMENT_SPEC.md) → Dev team
```

- **Entry point**: `agents/odoo-presales-consultant.md` — role "Senior Odoo PreSales Consultant", điều phối qua 5 phase ở trên (xem cũng mục "PreSale / Solution Consulting Workflow" trong `SKILL.md`).
- **Skill files** (flat trong `skills/`, prefix `presales-`/`l10n-`/`vietnam-`): bộ câu hỏi khảo sát, feature matrix Apps Odoo, phương pháp Fit-Gap, blueprint theo 6 ngành phổ biến, demo guide, effort estimation, licensing/deployment, competitor battle card, và localization Việt Nam (kế toán/hoá đơn điện tử/tích hợp ngân hàng-vận chuyển-thanh toán).
- **Slash commands**: `/odoo-presales-discovery [industry]`, `/odoo-fit-gap`, `/odoo-proposal`.
- **Vòng lặp khép kín**: output cuối cùng (`REQUIREMENT_SPEC.md`) tương thích trực tiếp với `agents/odoo-planner.md` ở nhánh Developer — xem `skills/presales-to-implementation-handoff-guide.md`.

Tất cả các platform tích hợp ở mục dưới đây (Cursor, Hermes, Gemini, Codex...) đều tự động có quyền truy cập nhánh PreSale này vì nó nằm cùng cấu trúc `skills/`/`agents/`/`commands/` flat với nhánh Developer.

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
GitHub Copilot reads custom instructions from `.github/copilot-instructions.md` (cross-IDE, works in VS Code, JetBrains, and others):
- Configured to direct the model to read Odoo patterns from the `skills/` directory before writing code.
- **Usage**: Just open this folder in VS Code and use Copilot Chat. Instructions are loaded automatically.

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

### 8. Cline & Roo Code
Modern VS Code extensions like Cline and Roo Code automatically load rule guidelines from the root level:
* We have created `.clinerules` which mirrors the `.cursorrules` to instruct Cline/Roo Code to read `/skills/` and enforce the same TDD, plan, and review loop workflow.

### 9. Continue.dev (VS Code / JetBrains / Emacs)
Continue is a popular open-source Copilot alternative.
* **Codebase Indexing**: Continue automatically indexes files under `/skills/` for `@codebase` semantic search.
* **Custom Slash Commands**: Add custom commands to your `~/.continue/config.json` that reference our local markdown templates:
  ```json
  {
    "slashCommands": [
      {
        "name": "odoo-plan",
        "description": "Plan Odoo feature using local guidelines",
        "prompt": "Read the odoo-planner agent details under agents/odoo-planner.md and create a plan for: {{{ input }}}"
      }
    ]
  }
  ```

### 10. Aider (CLI Agent)
Aider is a terminal-based AI pair programmer.
* **Automatic Load**: Start Aider and instruct it to read the skills repository:
  ```bash
  aider --read skills/
  ```
  Alternatively, you can add `read: [skills/]` to your `.aider.conf.yml` at the root of the project to automatically load the patterns.

### 11. Custom Web UIs (Open WebUI / LibreChat)
For web-based chat interfaces connected to local LLMs (e.g. Ollama, OpenRouter, self-hosted API):
* **Open WebUI (Knowledge Bases)**: Under the **Workspace** tab, create a new Knowledge Base named `Odoo Developer Skill` and upload the markdown files from the `/skills/` directory. Attach this Knowledge Base to your custom Odoo Agent.
* **LibreChat (Custom Agents)**: Create an agent, set the system instructions to the contents of `SKILL.md` at root, and upload files in `skills/` to the Agent's file attachment storage for RAG retrieval.

### 12. Local Developer Frameworks (CrewAI / AutoGen / LangChain)
If building custom autonomous Python agents:
* **Tool-based Loading**: Instantiate a `DirectoryReadTool` (from CrewAI Tools) or `DirectoryLoader` (from LangChain) pointing to the `./skills/` directory:
  ```python
  from crewai_tools import DirectoryReadTool
  
  # Give the Odoo developer agent read access to our curated patterns
  odoo_skills_tool = DirectoryReadTool(directory='./skills')
  ```


---

## 💾 Test Verification

A custom dynamic Python runner is located at `scripts/run_tests.py`.
To validate custom Odoo logic (e.g., `qms_sop_management` or other models):
```bash
python scripts/run_tests.py
```
This script dynamically sets up custom test execution overrides and checks Odoo modules inside this workspace.
