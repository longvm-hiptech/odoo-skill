---
name: odoo-test
description: |
  MUST be invoked when user asks to "run tests", "execute tests", "test module", "check test results", "debug tests".
  CRITICAL: This command MUST invoke the odoo-tester agent for test execution and parsing logs.
  DO NOT run tests manually - ALWAYS use the specialized agent.
arguments:
  - name: module
    description: Technical name of the Odoo module to test (e.g., qms_sop_management)
    required: true
  - name: database
    description: Target database to run tests against (defaults to active log database or qphatt)
    required: false
  - name: tag
    description: Specific test tag or test class to run (e.g., security, standard)
    required: false
input_examples:
  - description: "Run tests for qms_sop_management"
    arguments:
      module: "qms_sop_management"
  - description: "Run security tests on qphatt database"
    arguments:
      module: "qms_sop_management"
      database: "qphatt"
      tag: "security"
---

# /odoo-test Command

Run and debug automated unit, integration, and security tests for Odoo modules.

## CRITICAL: MANDATORY AGENT INVOCATION

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  You MUST invoke the odoo-tester agent to perform the test run.              ║
║  DO NOT run or debug Odoo tests manually.                                    ║
║                                                                              ║
║  Invoke: Task tool with subagent_type="odoo-development:odoo-tester"         ║
║  Prompt: "Run tests for module [module] on database [database] with tag [tag]"║
║                                                                              ║
║  NEVER skip this step. Agent-based testing is MANDATORY.                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### NO PARALLEL LOG TAMPERING WHILE THE AGENT RUNS

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  When dispatching odoo-tester, you MUST NOT in the same message              ║
║  (or while waiting for its result) run custom commands that read or write to ║
║  the Odoo log file. The tester agent executes the tests and reads the logs   ║
║  systematically; duplicating this work wastes resources.                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Execution Flow

### Step 1: Discover Parameters
1. If `database` is not specified, query the active logs or check the active database list (default to `qphatt`).
2. Verify that the module directory exists under the workspace or addons path.

### Step 2: Invoke the Tester Agent
1. Trigger the `odoo-tester` subagent.
2. Provide the module name, target database, and optional test tags.
3. Wait for the agent's report.

### Step 3: Present Results
Render the structured report from the agent, detailing passes, failures, stack traces, and recommended fixes.

## Example Usage

```
# Run all tests for a module
/odoo-test qms_sop_management

# Run specific tag on a custom database
/odoo-test approvals_workflow qphatt security
```
