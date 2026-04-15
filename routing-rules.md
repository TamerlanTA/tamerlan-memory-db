# Routing Rules

## Related
- [[agent-memory]]
- [[ОС LLM]]
- [[Obsidian - память агента]]

---

## Agent roles (from ОС LLM pattern)

### Claude Code → Chief Reasoning Agent
Use for:
- architecture decisions and validation
- hard debugging / root cause analysis
- design review of complex or risky deliverables
- prompt engineering for other agents
- high-stakes implementation where ambiguity is high
- big project steering / milestone planning
- reading Obsidian memory and writing back project state

**Do not** use for routine implementation — it is expensive and reserved for high-value reasoning.

### Codex → Primary Execution Agent
Use for:
- batch implementation
- code fixes and refactors
- writing tests
- file edits and migrations
- local repo operations
- generating files following a clear spec
- updating memory notes in a pre-defined format

**Codex does ~80% of production work.**

### ChatGPT → Orchestrator / Strategic Control Plane
Use for:
- task decomposition and routing decisions
- context packaging and compression
- batch prompt construction for Codex or Claude
- cross-project reasoning
- client communication drafting
- summarization and handoff synthesis
- final synthesis after execution

---

## Default rule
1. Start with ChatGPT to frame and package the task
2. Route implementation to Codex
3. Escalate to Claude Code only when the task is high-risk, ambiguous, or architecturally important
4. Always compress context before passing to any agent — never dump raw chat history

---

## Context for new chat sessions
```
Read the memory for project [project-name], get in sync with the current state, and then I will give you the next task.
```

## Memory sync triggers
- End of work block: `memory sync`
- Agent handoff: `handoff sync`
- End of day: `end-of-day sync`
