# Stale Issue Reminder

## Related
- [[Linear/Linear Ops Automation System/overview]]
- [[03-team-assignment-notifier]]
- [[01-daily-command-center]]

## Goal

Prevent tasks from sitting in `In Progress` without updates.

## Trigger

Scheduled in n8n.

Recommended:
- Every weekday at 18:00 Asia/Almaty.
- Optional daily check at 12:00 for urgent tasks.

## Linear Inputs

Issues where:
- State = In Progress or In Review.
- Not Done/Canceled.
- UpdatedAt older than threshold.

Thresholds:
- Urgent/high: 24 hours.
- Medium/low: 48 hours.
- Blocked: handled by [[02-blocked-decision-bot]].

## Reminder Message

To assignee:

```md
Status update needed — FLO-17

Task: Aslanbek: Build Speed-to-Lead n8n MVP
No update for: 26h

Reply/update Linear with:
1. What was done
2. What is blocking
3. Next step
4. ETA

<Linear URL>
```

To Tamerlan summary:

```md
Stale issues summary

- FLO-17 — Aslanbek — 26h no update
- FLO-16 — Adil — 2d no update
```

## Linear Comment Option

If Telegram is not enough, add a comment:
`Automated reminder: please post a status update with done/blocker/next/ETA.`

Use carefully to avoid noisy Linear comments.

## Acceptance Criteria

- Stale in-progress issues are detected.
- Assignee receives a clear reminder.
- Tamerlan receives summary for unresolved stale tasks.
- No repeated reminders more often than once per 24h per issue.

## Dedupe Rules

Store:
- `stale_reminder:{issue_id}:{date}`.

## Edge Cases

- If assignee is missing, notify Tamerlan.
- If issue has `Blocked: needs decision`, skip stale reminder and route to Blocked Decision Bot.
- If task has a recent comment but Linear `updatedAt` is not updated as expected, use comments list if available.

