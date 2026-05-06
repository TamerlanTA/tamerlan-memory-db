# Linear Ops Automation Implementation Plan

## Related
- [[Linear/Linear Ops Automation System/overview]]
- [[01-daily-command-center]]
- [[02-blocked-decision-bot]]
- [[03-team-assignment-notifier]]
- [[04-stale-issue-reminder]]
- [[05-linear-to-obsidian-memory-sync]]
- [[06-weekly-flowops-review]]

## MVP Stack

- n8n for workflows.
- Linear connector/API for issues, projects, labels, comments.
- Telegram bot for notifications.
- Obsidian vault through GitHub/local filesystem for memory writes.
- n8n static data for dedupe in MVP.

## Phase 1 — Build Control Layer

### 1. Daily Command Center
Build first because it gives immediate visibility.

Needed:
- Linear credentials.
- Telegram bot/chat ID for Tamerlan.
- Query logic for priority/blocker/stale/unassigned issues.

### 2. Blocked Decision Bot
Build second because FlowOps already uses `Blocked: needs decision`.

Needed:
- Label ID or label name.
- Telegram reply handling decision.
- Dedupe store.

## Phase 2 — Team Execution Layer

### 3. Team Assignment Notifier
Needed:
- Assignee email -> Telegram chat mapping.
- Linear assignment polling or webhook.
- Message template.

### 4. Stale Issue Reminder
Needed:
- Stale thresholds.
- Which states count as active.
- Whether to comment in Linear or only Telegram.

## Phase 3 — Memory and Review Layer

### 5. Linear to Obsidian Memory Sync
Needed:
- Source-of-truth decision from `FLO-22`.
- File write method.
- Session note naming convention.
- Completed issue filter.

### 6. Weekly FlowOps Review
Needed:
- Weekly schedule.
- Project list.
- Telegram report template.
- Optional Obsidian write.

## Recommended First n8n Workflow

Start with one workflow:
`Linear Ops — Daily Command Center`

Why:
- It is read-only from Linear.
- It only sends Telegram.
- Low risk.
- Immediately useful.

## Implementation Checklist

- [ ] Confirm Telegram chat IDs.
- [ ] Confirm Linear API/connector access in n8n.
- [ ] Decide source-of-truth rule for Linear vs Obsidian.
- [ ] Build Daily Command Center.
- [ ] Build Blocked Decision Bot.
- [ ] Build Assignment Notifier.
- [ ] Build Stale Reminder.
- [ ] Build Linear -> Obsidian Memory Sync.
- [ ] Build Weekly Review.
- [ ] Document every workflow with trigger, credentials, dedupe key, and test cases.

## Linear Task

Track implementation in Linear issue created for Tamerlan:
- `Build Linear Ops automation layer for FlowOps execution system`

