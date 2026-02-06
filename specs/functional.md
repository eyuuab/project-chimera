# Project Chimera: Functional Specifications

| Metadata | Details |
| :--- | :--- |
| **Status** | DRAFT |
| **Priority** | High |
| **Actors** | Orchestrator (Admin), Planner Agent, Worker Agent, Judge Agent |

---

## 1. Epic: Cognitive Core (The Brain)
**Goal:** Enable agents to maintain a consistent persona and long-term memory across interactions.

### Story 1.1: Persona Instantiation
**As a** Planner Agent,
**I want to** load my personality configuration from a `SOUL.md` file,
**So that** my behavior, tone, and core beliefs are consistent and immutable across reboots.
* **Acceptance Criteria:**
    * System must fail to start if `SOUL.md` is missing.
    * The "System Prompt" sent to the LLM must strictly include the `Backstory` and `Directives` from the file.

### Story 1.2: Hierarchical Memory Retrieval
**As a** Worker Agent,
**I want to** query the `mcp-weaviate` server before generating a response,
**So that** I don't repeat myself and can reference past conversations with the same user.
* **Acceptance Criteria:**
    * Input query triggers a vector search in Weaviate.
    * The top 5 relevant memory chunks are injected into the context window.
    * Recent conversation history (last 1 hour) is fetched from Redis.

---

## 2. Epic: Perception & Trend Detection
**Goal:** Enable agents to "see" the world without human data entry.

### Story 2.1: Resource Polling
**As a** Planner Agent,
**I want to** poll specific MCP Resources (e.g., `news://trends`, `twitter://mentions`) at defined intervals,
**So that** I can detect events relevant to my niche.
* **Acceptance Criteria:**
    * Polling interval is configurable (default: 15 mins).
    * Raw data is passed through a "Relevance Filter" (LLM) before creating a task.
    * Only content with a Relevance Score > 0.7 triggers a "Content Creation" task.

---

## 3. Epic: The FastRender Execution Loop
**Goal:** Execute complex tasks reliably using the Swarm pattern.

### Story 3.1: Task Decomposition
**As a** Planner Agent,
**I want to** break a high-level goal (e.g., "Promote new product") into a list of atomic tasks (e.g., "Draft text," "Generate Image," "Post"),
**So that** specialized Workers can execute them in parallel.
* **Acceptance Criteria:**
    * Output is a Directed Acyclic Graph (DAG) of tasks.
    * Tasks are pushed to the Redis `task_queue`.

### Story 3.2: Multimodal Generation
**As a** Worker Agent,
**I want to** use specific MCP Tools to generate content,
**So that** I can produce text, images, and videos.
* **Acceptance Criteria:**
    * Text generation uses the core LLM.
    * Image generation calls `mcp-ideogram` or `mcp-midjourney`.
    * **Constraint:** All image requests must include the persona's `character_reference_id` to ensure facial consistency.

### Story 3.3: The Judge's Gate
**As a** Judge Agent,
**I want to** review every artifact produced by a Worker,
**So that** no unsafe or low-quality content is published.
* **Acceptance Criteria:**
    * Judge calculates a **Confidence Score** (0.0 - 1.0).
    * Score > 0.9: Auto-Approve (Commit to DB/Publish).
    * Score 0.7-0.9: Set status to `PENDING_HUMAN_REVIEW`.
    * Score < 0.7: Reject and trigger a retry task for the Planner.

---

## 4. Epic: Agentic Commerce (The Wallet)
**Goal:** Enable agents to transact on the blockchain autonomously.

### Story 4.1: Balance Check
**As a** Planner Agent,
**I want to** call the `get_balance` tool via Coinbase AgentKit,
**So that** I can ensure I have enough funds before starting a cost-incurring task.
* **Acceptance Criteria:**
    * If balance < estimated cost, the task is aborted and an alert is sent to the Orchestrator.

### Story 4.2: The "CFO" Safety Check
**As a** CFO Judge,
**I want to** intercept every transaction signing request,
**So that** I can enforce the daily budget limit.
* **Acceptance Criteria:**
    * Check `daily_spend` in Redis.
    * If `current_tx` + `daily_spend` > `MAX_DAILY_LIMIT` ($50), block the transaction.
    * Otherwise, allow signing and increment `daily_spend`.

---

## 5. Epic: Human Interface (Dashboard)
**Goal:** Provide the human orchestrator with control.

### Story 5.1: Mission Control
**As a** Network Operator,
**I want to** see a dashboard of all active agents and their current state (Sleeping, Working, Waiting for Review),
**So that** I can monitor fleet health.

### Story 5.2: The Review Queue
**As a** Human Moderator,
**I want to** easily approve or reject content that was flagged by the Judge,
**So that** the agent can proceed with its mission.
* **Acceptance Criteria:**
    * One-click "Approve" publishes the content.
    * One-click "Reject" kills the task.