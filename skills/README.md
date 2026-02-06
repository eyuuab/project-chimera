# Agent Skills Registry

This directory contains the **Cognitive Skills** available to the Chimera Agent Fleet. 

## Definition
A **Skill** is a self-contained Python module that orchestrates multiple MCP Tool calls to achieve a higher-order objective. Unlike raw tools, Skills contain business logic, error handling, and retry loops.

## The Skill Interface
All skills must adhere to this usage pattern:

```python
async def execute(ctx: Context, payload: Dict) -> SkillResult:
    """
    1. Validate input payload.
    2. Call MCP tools (e.g., fetch news).
    3. Process data (e.g., summarize with LLM).
    4. Return structured result.
    """