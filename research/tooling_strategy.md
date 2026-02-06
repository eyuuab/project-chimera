# Developer Tooling Strategy (MCP)

## 1. Objective
To equip the "Forward Deployed Engineer" (Human + AI Pair) with the necessary Model Context Protocol (MCP) servers to manipulate the codebase safely and effectively.

## 2. Selected MCP Servers (Development Phase)
These servers run locally on the developer's machine to assist in coding.

### A. Filesystem MCP (`@modelcontextprotocol/server-filesystem`)
* **Purpose:** Allows the AI to read specs, write code, and refactor files.
* **Configuration:**
    * `allowed_directories`: `['./src', './tests', './specs', './research']`
    * **Constraint:** AI is strictly forbidden from editing files outside the project root.

### B. Git MCP (`git-mcp`)
* **Purpose:** Allows the AI to read commit history, create branches, and stage changes.
* **Workflow:**
    1.  AI reads `specs/`.
    2.  AI implements code.
    3.  AI uses `git_commit` to save progress with a semantic message.

### C. PostgreSQL MCP (`mcp-server-postgres`)
* **Purpose:** Database schema management and inspection.
* **Usage:** Used during the TDD phase to verify that tables are created correctly matching `specs/technical.md`.

## 3. Tool vs. Skill Distinction
* **Tool:** `filesystem.write_file` (Low-level, dumb).
* **Skill:** `refactor_module` (High-level, creates a plan, writes file, runs tests).