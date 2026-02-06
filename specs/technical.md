# Project Chimera: Technical Specifications

| Metadata | Details |
| :--- | :--- |
| **Database** | PostgreSQL 16 (Relational), Weaviate (Vector), Redis 7 (Cache) |
| **API Style** | REST (Orchestrator), JSON-RPC (MCP) |
| **Language** | Python 3.11+ |
| **Frameworks** | FastAPI, Pydantic, SQLAlchemy |

---

## 1. Data Models (Pydantic Schemas)
These schemas define the payload passed between the Planner, Worker, and Judge agents.

### 1.1 The Agent Task (`Task`)
The atomic unit of work in the Swarm.

```json
{
  "task_id": "uuid-v4",
  "agent_id": "uuid-v4",
  "task_type": "enum(GENERATE_TEXT, GENERATE_IMAGE, POST_SOCIAL, TX_SIGN)",
  "priority": "enum(HIGH, MEDIUM, LOW)",
  "payload": {
    "instruction": "Draft a tweet about ETH Denver.",
    "context_ref": ["mcp://memory/123", "mcp://news/456"],
    "constraints": ["max_chars=280", "tone=witty"]
  },
  "created_at": "timestamp",
  "status": "enum(PENDING, IN_PROGRESS, REVIEW, COMPLETED, FAILED)"
}