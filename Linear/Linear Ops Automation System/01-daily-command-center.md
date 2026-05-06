# Daily Command Center

## Related
- [[Linear/Linear Ops Automation System/overview]]
- [[02-blocked-decision-bot]]
- [[04-stale-issue-reminder]]
- [[projects/FlowOps Team/00 - Overview|FlowOps Team]]

## Goal

Send Tamerlan a daily Telegram digest that turns Linear into a command center instead of a passive board.

## User Story

Every morning, Tamerlan receives one concise message showing what to focus on today, what is blocked, what is stale, and what needs reassignment.

## Trigger

Scheduled daily in n8n.

Recommended time:
- 09:00 Asia/Almaty.

Optional:
- Manual trigger for testing.

## Linear Inputs

Query Linear for:
- Open urgent/high priority issues.
- Issues assigned to Tamerlan.
- Issues assigned to Adil, Aslanbek, Alexey.
- Issues with `Blocked: needs decision`.
- Issues with no assignee.
- Issues updated later than threshold.
- Issues due today/overdue if due dates are used.
- Active projects and their open issue counts.

## Message Format

```md
FlowOps Daily Command Center — YYYY-MM-DD

Top 3 focus:
1. FLO-...
2. FLO-...
3. FLO-...

Blocked decisions:
- FLO-... — decision needed: ...

Team:
- Adil: ...
- Aslanbek: ...
- Alexey: ...

Stale / needs update:
- FLO-... — no update for X days

Unassigned:
- FLO-...

Suggested next move:
- ...
```

## Logic

Top 3 focus ranking:
1. Urgent priority.
2. Blocked issues assigned to Tamerlan.
3. High priority issues in active projects.
4. Issues connected to current FlowOps priorities: Demo Library, Upwork Radar, CRM QA, Speed-to-Lead MVP.

Stale thresholds:
- Urgent/high: no update for 24h.
- Medium/low: no update for 48h.

## Output

Telegram message to Tamerlan.

Optional later:
- Add a Linear comment to a tracking issue with the daily digest.

## Acceptance Criteria

- Digest arrives daily.
- Message fits in one Telegram screen when possible.
- Every item links to the Linear issue.
- It clearly separates focus, blockers, stale tasks, and unassigned work.
- It does not include completed issues unless completed yesterday.

## Edge Cases

- If no urgent/high issues exist, show next active project priorities.
- If Linear API fails, send a short error alert.
- If an issue has no assignee, group it under `Unassigned`.

## Build Notes

Use n8n scheduled trigger + Linear list/search calls + Telegram node.

Deduplication is not critical because this runs once daily, but test manual trigger should mark message as test.

