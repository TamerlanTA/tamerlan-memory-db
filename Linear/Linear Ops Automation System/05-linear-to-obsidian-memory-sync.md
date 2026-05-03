# Linear to Obsidian Memory Sync

## Related
- [[overview]]
- [[projects/FlowOps Team/Team Task Automation]]
- [[projects/FlowOps Team/sessions/2026-05-03-linear-initial-migration]]

## Goal

When important Linear work is completed, preserve the result in Obsidian memory so future agents can understand what changed without reading Linear history.

## Trigger

MVP:
- Scheduled daily check for issues completed in the last 24 hours.

Later:
- Linear webhook when issue moves to Done.

## Scope

Start with FlowOps only.

Sync completed issues from:
- FlowOps OS — Master Build.
- Demo Library — First 10 Loom Assets.
- Upwork Radar — Revenue Pipeline.
- FlowOps CRM — Airtable + Automation.
- Website Audit Generator — Cold Outreach.
- LinkedIn Pain Radar — Warm Outreach.
- Sales Assets + Documentation Kit.
- Retainer Conversion System.

## What to Write

For each meaningful completed issue:
- Issue ID and title.
- Project.
- Assignee.
- Completion date.
- What was done.
- Deliverables/links.
- Blockers resolved or remaining.
- Next steps.

## Where to Write

For FlowOps project work:
- `projects/FlowOps Team/sessions/YYYY-MM-DD-linear-completed-work.md`

If a session note already exists for that date:
- Append under a section `## Linear Completed Work`.

For non-project general Linear operating rules:
- `Linear/Linear Ops Automation System/implementation-log.md`

## Session Note Format

```md
# Session YYYY-MM-DD — Linear Completed Work

## Related
- [[00 - Overview]]
- [[current-state]]
- [[next-steps]]

## What was completed
- FLO-...

## Key findings
- ...

## Blockers
- ...

## Next steps
- ...
```

## Acceptance Criteria

- Completed meaningful Linear issues create concise Obsidian memory.
- Trivial onboarding issues are ignored.
- Existing historical context is not overwritten.
- Every session note links back to FlowOps core notes.
- No secrets are written.

## Dedupe Rules

Store completed issue IDs already synced:
- `linear_memory_synced:{issue_id}`.

## Edge Cases

- If issue description is too long, summarize.
- If deliverables are missing, write `Deliverables not linked in Linear`.
- If the issue is completed but still has unresolved blockers, include them under residual risk.

