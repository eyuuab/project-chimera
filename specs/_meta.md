# Project Chimera: High-Level Vision & Constraints

| Metadata | Details |
| :--- | :--- |
| **Version** | 1.0.0 |
| **Status** | DRAFT |
| **Last Updated** | 2026-02-05 |
| **Owner** | Lead Architect (FDE) |
| **SRS Reference** | Chimera 2026 Edition (SRS 1.0 - 1.3) |

---

## 1. Vision & Strategic Scope
Project Chimera transitions AiQEM from simple content automation to **Autonomous Influencer Agents**. These are persistent, goal-directed digital entities capable of perception, reasoning, creative expression, and economic agency.

### 1.1 The "Why"
Traditional automation is fragile. It requires humans to script every step. Chimera Agents are designed to be **anti-fragile**: given a high-level goal (e.g., "Grow audience in the sustainable fashion niche"), the agent autonomously determines the *how*, executing tasks, managing its own budget, and learning from engagement data.

### 1.2 The "What"
We are building a **Fractal Orchestration System** utilizing the **FastRender Swarm** pattern. A single human orchestrator manages a fleet of thousands of agents, supported by a hierarchy of AI Managers (Planners) and Workers.

---

## 2. Core Architectural Pillars
These are the non-negotiable technical foundations (Source: SRS 1.1).

### 2.1 The FastRender Swarm (Internal Cognition)
We reject the monolithic "God Agent." All complex tasks must be decomposed into the **Planner-Worker-Judge** cycle:
* **Planner:** Maintains state and strategy.
* **Worker:** Stateless execution of atomic tasks.
* **Judge:** Quality assurance and safety gating before commit.

### 2.2 Model Context Protocol (External Connectivity)
* **Constraint:** Agents **MUST NOT** contain hard-coded API logic.
* **Requirement:** All interactions with the outside world (Social Media, Crypto, News) **MUST** occur via the **Model Context Protocol (MCP)**.
    * *Perception:* Reading `mcp://resources` (e.g., `twitter://mentions`).
    * *Action:* Calling `mcp://tools` (e.g., `generate_image`, `send_transaction`).

### 2.3 Agentic Commerce (Economic Agency)
* Agents are Economic Entities. They possess non-custodial crypto wallets (Coinbase AgentKit).
* They are authorized to transact on-chain for self-sustainability (paying for compute, art, or tipping).

---

## 3. Operational Constraints & Guardrails

### 3.1 The "CFO" Rule (Financial Safety)
* **Strict Limit:** No agent may execute a transaction > $50.00 USDC without human approval.
* **Mechanism:** A specialized "CFO Judge" agent must validate every wallet signature request against the daily budget `specs/technical.md`.

### 3.2 The "Honesty" Directive (Ethical AI)
* If queried about its nature ("Are you a bot?"), the agent **MUST** disclose its artificial identity.
* All generated media must carry metadata tags (e.g., `is_generated=True`) where platform APIs allow.

### 3.3 Human-in-the-Loop (HITL)
* **Confidence Thresholds:**
    * **< 70%:** Auto-Reject.
    * **70% - 90%:** Queue for Human Review.
    * **> 90%:** Auto-Publish.
* **Sensitive Topics:** Any content hitting "Politics" or "Finance" keywords triggers mandatory HITL.

---

## 4. Success Metrics (North Star)
1.  **Autonomy Level:** % of tasks completed without human intervention (Target: >95%).
2.  **Economic Viability:** Ability of an agent to fund its own inference costs via on-chain revenue.
3.  **Safety:** 0 incidents of brand-damaging hallucinations published to live platforms.