# Linear Ops Automation Implementation Log

## Related
- [[Linear/Linear Ops Automation System/overview]]
- [[implementation-plan]]
- [[projects/FlowOps Team/00 - Overview|FlowOps Team]]

## 2026-05-03 — Initial Automation System Spec

### What was done
- Created the `Linear/Linear Ops Automation System/` memory folder.
- Wrote detailed specs for six automations:
  - [[01-daily-command-center]]
  - [[02-blocked-decision-bot]]
  - [[03-team-assignment-notifier]]
  - [[04-stale-issue-reminder]]
  - [[05-linear-to-obsidian-memory-sync]]
  - [[06-weekly-flowops-review]]
- Wrote [[implementation-plan]] with phased build order.
- Added task to [[My-tasks]].
- Created Linear issue `FLO-25`: `Build Linear Ops automation layer for FlowOps execution system`.

### Key decision
- Telegram/voice task creation is excluded. Tamerlan will keep assigning tasks manually with agents.

### Recommended first build
- Start with [[01-daily-command-center]] because it is low risk, read-only from Linear, and immediately useful.
- Then build [[02-blocked-decision-bot]].

### Open decisions
- Confirm Telegram chat IDs for Tamerlan, Adil, Aslanbek, and Alexey.
- Confirm source-of-truth rule. Recommended: Linear for active execution, Obsidian for memory and handoffs.
- Confirm n8n credential setup for Linear, Telegram, and Obsidian/GitHub writes.
- Confirm stale thresholds. Recommended: 24h for urgent/high, 48h for medium/low.
