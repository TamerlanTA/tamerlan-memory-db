# Workflow: Memory Sync

Use this after meaningful progress, a decision, a blocker, a review, or a handoff-worthy work block.

## Memory Principle

Memory is operational continuity, not a transcript. Write what the next agent needs to continue safely.

## If A Memory System Exists

Read and update the project memory convention already present. Common files:
- `overview.md`
- `current-state.md`
- `decisions.md`
- `risks.md`
- `next-steps.md`
- `prompts.md`
- `sessions/YYYY-MM-DD-topic.md`

Preserve historical decisions. Do not overwrite important context; append or mark stale information.

## If No Memory System Exists

Create a minimal file-based memory folder in one of:
- `/docs/project-memory/`
- `.agent/memory/`

Use:

```txt
project-memory/
  overview.md
  current-state.md
  decisions.md
  risks.md
  next-steps.md
  prompts.md
  sessions/
```

For small or uncertain projects, prefer a single concise memory file over a full folder.

## What To Record

Session note:
- what was done
- key findings
- decisions made
- changed files
- validation run
- blockers
- next steps

Current state:
- actual project status after the work
- accepted behavior
- unaccepted or partial work

Decisions:
- stable choices that affect future work
- tradeoff and reason

Risks:
- unresolved blockers
- production gaps
- known bugs
- untested assumptions

Next steps:
- immediate priorities in execution order
- owner/manual actions
- recommended next agent task

Prompts:
- only reusable prompts worth preserving

## Staleness Markers

Use direct labels:
- `Stale as of YYYY-MM-DD`
- `Unverified`
- `Blocked`
- `Superseded by [decision/date]`

## Memory Update Template

```md
# Session YYYY-MM-DD - Short Topic

## What was done
- ...

## Key findings
- ...

## Decisions
- ...

## Validation
- ...

## Blockers / risks
- ...

## Next steps
- ...
```
