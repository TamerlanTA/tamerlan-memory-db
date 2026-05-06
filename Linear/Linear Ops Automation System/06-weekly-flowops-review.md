# Weekly FlowOps Review

## Related
- [[Linear/Linear Ops Automation System/overview]]
- [[01-daily-command-center]]
- [[05-linear-to-obsidian-memory-sync]]
- [[projects/FlowOps Team/00 - Overview|FlowOps Team]]

## Goal

Create a weekly operating review from Linear so Tamerlan can see what moved, what stalled, and what should be the next focus.

## Trigger

Scheduled weekly.

Recommended:
- Sunday 18:00 Asia/Almaty.

## Linear Inputs

Look back over the last 7 days:
- Completed issues.
- Created issues.
- Issues moved to In Progress.
- Issues still blocked.
- Stale issues.
- Work by assignee.
- Progress by project.
- Urgent/high issues still open.

## Report Format

```md
FlowOps Weekly Review — YYYY-MM-DD

Completed:
- FLO-...

Moved forward:
- ...

Blocked:
- ...

Stale / needs attention:
- ...

By teammate:
- Tamerlan: ...
- Adil: ...
- Aslanbek: ...
- Alexey: ...

Project health:
- Demo Library: ...
- Upwork Radar: ...
- CRM: ...
- Website Audit: ...
- LinkedIn: ...
- Retainer: ...

Recommended next week focus:
1. ...
2. ...
3. ...
```

## Output

Required:
- Telegram message to Tamerlan.

Optional:
- Obsidian weekly note.
- Linear comment on a tracking issue.

## Acceptance Criteria

- Report is generated weekly.
- It separates completed work from stalled work.
- It names blockers and owners.
- It gives a clear top 3 focus for next week.
- It can be saved to Obsidian without large cleanup.

## Obsidian Write Option

Suggested path:
- `projects/FlowOps Team/sessions/YYYY-MM-DD-weekly-linear-review.md`

This should be concise and link to:
- [[00 - Overview]]
- [[What to Do First]]
- [[Team Task Automation]]

## Edge Cases

- If no issues completed, report honestly and highlight blockers.
- If an assignee has too many stale tasks, flag workload/clarity issue.
- If project has no movement for 7 days, mark as stalled.

