# Prompts

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]

## Content
## New session boot prompt

```text
Read the memory for project storehouse-n8n, get in sync with the current state, and then I will give you the next task.
```

## Implementation handoff prompt template

```text
Project: storehouse-n8n
Memory: /Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/projects/storehouse-n8n
Workspace: /Users/tamerlan/Desktop/storehouse-n8n

Goal:
[state the concrete implementation goal]

Context:
[summarize current state, key decisions, blockers, and relevant files]

Constraints:
- Read project memory before implementation.
- Preserve existing user changes.
- Update memory after significant work.
- Validate with the appropriate commands for the stack once it exists.

Expected output:
- Changed files
- Validation run
- Risks/blockers
- Next steps
```

