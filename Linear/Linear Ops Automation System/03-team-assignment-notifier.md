# Team Assignment Notifier

## Related
- [[Linear/Linear Ops Automation System/overview]]
- [[04-stale-issue-reminder]]
- [[projects/FlowOps Team/00 - Overview|FlowOps Team]]

## Goal

Notify team members when they are assigned a Linear issue, with enough context to start without asking what the task means.

## Team Mapping

Known from memory / Linear:
- Tamerlan: Linear admin / owner.
- Aslanbek: `kalabayaslanbek@gmail.com`.
- Adil: `vlastus11@gmail.com`.
- Alexey: profile incomplete; mapping needs confirmation.

Telegram chat IDs need confirmation.

## Trigger

MVP:
- Scheduled polling every 10-15 minutes for recently updated issues where assignee changed or issue is newly assigned.

Later:
- Linear webhook on issue assignment.

## Linear Inputs

For each assigned issue:
- ID and URL.
- Title.
- Assignee.
- Project.
- Priority.
- Due date if set.
- Description.
- Labels.
- State.

## Message Format

```md
New Linear task assigned

Issue: FLO-17 — Aslanbek: Build Speed-to-Lead n8n MVP
Priority: Urgent
Project: FlowOps OS — Master Build

What to do:
<short extracted goal>

Done when:
<short extracted done criteria>

Link:
<Linear URL>
```

## Context Extraction

Prefer these sections from issue description:
- `# Goal`
- `# Work steps`
- `# Deliverables`
- `# Done when`

If too long, summarize to:
- one goal line;
- top 3 work steps;
- done criteria.

## Output

Telegram DM or group mention to assignee.

Optional:
- Comment on Linear: `Assignment notification sent to <person> at <time>.`

## Acceptance Criteria

- Assignee receives a readable task notification within 15 minutes.
- Notification includes issue link, goal, priority, and done criteria.
- Same assignment does not notify repeatedly unless assignee changes.
- If assignee Telegram ID is unknown, notify Tamerlan instead.

## Dedupe Rules

Store:
- `assignment_notified:{issue_id}:{assignee_id}`.

If assignee changes, notify new assignee.

## Edge Cases

- If issue has weak description, notify Tamerlan that the task needs clarification.
- If task is assigned to Tamerlan, include it in Daily Command Center instead of separate spam unless priority is urgent.

