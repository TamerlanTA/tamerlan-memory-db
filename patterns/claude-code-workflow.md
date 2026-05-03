# Claude Code Workflow Pattern

## Related
- [[knowledge/claude-code-32-hacks]]
- [[agent-memory]]
- [[routing-rules]]

## Pattern
Use Claude Code / Codex as an execution agent only after the task has enough context, constraints, and success criteria.

Preferred flow:
- Read the relevant project memory first.
- Define the active scope and files.
- Ask for a plan before high-risk changes.
- Keep context small and avoid unrelated exploration.
- Use a self-checking task list for multi-step work.
- Verify with tests, diffs, screenshots, or tool-specific validation.
- Write back concise memory updates after meaningful work.

## When to use
- Coding tasks with multiple files or risk of regressions.
- n8n / automation builds where workflow logic, credentials, retries, and manual review paths matter.
- Project handoffs where another agent needs a precise continuation point.

## Avoid
- Giving the agent the whole vault or repo when a narrow slice is enough.
- Skipping verification because the implementation "looks right".
- Writing memory updates that are too vague to guide the next session.
