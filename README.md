# TRP 1 - MCP Setup & AI Agent Orchestration

This repository documents the successful configuration of a modern AI-driven development environment, featuring the **Tenx MCP server** and a custom **Boris Cherny-inspired** rules configuration for autonomous coding agents.

## 🚀 Task 1: Environment Setup
I have successfully configured my local IDE (Ubuntu) with the Tenx MCP (10 Academy) server. 

- **IDE:** VS Code 
- **Connection Status:** Active & Verified.
- **Workflow:** Established an interaction loop involving agent-led file creation, modification, and terminal execution.

## 🧠 Task 2: Research & Agent Configuration
To move beyond basic "chatbot" behavior, I implemented a custom rules file (`.github/copilot-instructions.md` / `.cursor/rules/agent.mdc`) based on research into the workflows of Boris Cherny (Claude Code) and other industry leaders.

### Key Rules Implemented:
* **The "Plan Mode" Protocol:** The agent must propose a plan and wait for confirmation before executing multi-file edits.
* **The Verification Loop:** Mandatory use of `pytest` and `ruff` (Python-specific) to verify code quality before task completion.
* **Stateful Memory:** A "Learning Log" section allows the agent to self-correct and avoid repeating past mistakes.
* **Environment Safety:** Specific instructions to manage Python virtual environments and avoid "bare" exception handling.

## 📝 Task 3: Documentation & Insights

### What I Did
1.  Connected the **Tenx MCP** server to log agent interactions.
2.  Researched **agentic engineering patterns** (workflow parallelization and compounding engineering).
3.  Updated the agent's instructions to prioritize **Pythonic (PEP 8)** code and strict type-hinting.
4.  Tested the agent by building a Python script and forcing it to verify its work through the CLI.

### What Worked
* **MCP Integration:** The agent successfully used tools to read the filesystem and run bash commands.
* **Rule Enforcement:** The agent correctly followed the "Plan-Before-Code" rule, which helped in identifying logic errors *before* they were written.
* **Context Awareness:** Using `ls` and `grep` rules ensured the agent didn't hallucinate file paths.

### Insights Gained
* **Alignment is Key:** Rules transform an AI from a "predictor" into a "collaborator." By defining a clear operational playbook, the agent's behavior aligned perfectly with my intent.
* **The Flywheel Effect:** The "Learning Log" creates a flywheel where the agent becomes more specialized to my specific coding style over time.
* **Orchestration vs. Coding:** My role shifted from writing every line of code to **orchestrating a workflow** where I verify plans and the agent handles the implementation.

---
*Completed as part of the TRP 1 - MCP Setup Challenge.*