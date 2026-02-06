# Project Chimera: Domain Architecture Strategy

## 1. Agent Pattern Selection: The "FastRender" Swarm
**Decision:** Hierarchical Swarm Architecture (Planner-Worker-Judge).
**Rationale:**
We rejected the "Sequential Chain" (A -> B -> C) because it is brittle; one failure stops the pipeline. We rejected a monolithic "God Agent" because it creates context-window overflow.
Instead, we utilize the **FastRender Pattern** (Ref: SRS Section 3.1):
1.  **Planner (Strategist):** Decomposes high-level goals into atomic tasks.
2.  **Worker (Executor):** Stateless, parallel agents that execute tools (Tweet, Generate Image).
3.  **Judge (Gatekeeper):** A distinct agent that reviews Worker output for safety and quality before committing to the database.

## 2. Human-in-the-Loop (HITL) Strategy
**Decision:** Probability-Based Dynamic Intervention.
**Mechanism:**
We do not review *every* action. We utilize a **Confidence Score** attached to every Judge output (SRS Section 5.1).
* **High Confidence (> 0.90):** Auto-Execute.
* **Medium Confidence (0.70 - 0.90):** Async Queue for Human Review (Dashboard).
* **Low Confidence (< 0.70):** Auto-Reject & Retry.
* **Override:** Any content flagged with "Sensitive" keywords (Politics, Finance) forces a route to the HITL queue regardless of confidence.

## 3. Data Persistence Strategy
**Decision:** Hybrid SQL + Vector Architecture.
**Rationale:**
High-velocity metadata requires transactional integrity, while agent "soul" requires semantic retrieval.
* **PostgreSQL (Relational):** The "Source of Truth" for User Data, Campaign Configurations, and Transaction Logs (Ledger). This handles the high-velocity video metadata structure.
* **Weaviate (Vector):** The "Long-Term Memory." Stores agent persona embeddings, past interactions, and "world knowledge" for RAG.
* **Redis (Episodic):** Hot cache for the Task Queue and immediate conversation history.

## 4. Architecture Diagram
```mermaid
graph TD
    User[Network Operator] -->|Sets Goal| Orchestrator
    Orchestrator -->|Push Goal| Planner[Planner Agent]
    
    subgraph "Swarm Runtime"
        Planner -->|Create Tasks| TaskQueue[(Redis Task Queue)]
        TaskQueue -->|Pop Task| Worker[Worker Agent]
        Worker -->|Execute Tool| MCP[MCP Interface]
        MCP -->|External API| Twitter/News
        Worker -->|Output Artifact| ReviewQueue[(Redis Review Queue)]
        ReviewQueue -->|Pop Artifact| Judge[Judge Agent]
    end
    
    Judge -->|Confidence > 0.9| DB[(Postgres/Weaviate)]
    Judge -->|Confidence < 0.7| Planner
    Judge -->|Confidence 0.7-0.9| HITL[Human Review Dashboard]
    HITL -->|Approve| DB
    HITL -->|Reject| Planner