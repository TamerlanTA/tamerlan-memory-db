# Routing Rules

## Related
- [[agent-memory]]
- [[ОС LLM]]
- [[Obsidian - память агента]]

Use ChatGPT for:
- strategic planning
- task decomposition
- prompt engineering
- cross-project reasoning
- client communication drafting
- summarization and compression

Use Codex for:
- implementation
- refactors
- tests
- file edits
- batch code changes
- local repo operations

Use Claude for:
- architecture decisions
- high-risk debugging
- root cause analysis
- design validation
- final critical review

Default rule:
- Do not use Claude unless the task is high-risk, ambiguous, or architecturally important.
- Prefer Codex for execution.
- Always compress context before passing to any agent.
