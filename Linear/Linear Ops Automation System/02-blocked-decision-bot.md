# Blocked Decision Bot

## Related
- [[overview]]
- [[01-daily-command-center]]
- [[projects/FlowOps Team/Team Task Automation]]

## Goal

When a Linear issue is blocked by a decision, notify Tamerlan with a clear question and record the decision back into Linear.

## Trigger

Two possible MVP approaches:
1. Scheduled polling every 15-30 minutes for issues with label `Blocked: needs decision`.
2. Linear webhook when a label is added.

Recommended MVP: scheduled polling first, webhook later.

## Linear Inputs

Issues with:
- Label: `Blocked: needs decision`.
- State not Done/Canceled.

Useful fields:
- Issue ID.
- Title.
- Description.
- Assignee.
- Project.
- Latest comments.
- Labels.

## Decision Extraction

For MVP, the automation should not rely on perfect AI extraction.

Decision text can be found from:
- `# Blockers` section in issue description.
- Latest comment containing `decision`, `blocked`, `need`, `choose`, `confirm`.
- Fallback: ask Tamerlan to open the issue and decide.

## Telegram Message Format

```md
Decision needed — FLO-17

Task: Aslanbek: Build Speed-to-Lead n8n MVP
Project: FlowOps OS — Master Build
Blocked by:
- CRM/storage target
- Instant reply channel

Reply with decision, or open:
<Linear URL>
```

## Optional Reply Handling

If Telegram reply handling is enabled:
- Tamerlan replies to the bot.
- n8n adds the reply as a Linear comment.
- If reply starts with `Decision:` then add comment and optionally remove `Blocked: needs decision`.

Example:
`Decision: use FlowOps CRM for storage and Telegram draft-only for first reply test.`

## Output

Required:
- Telegram notification to Tamerlan.

Optional:
- Linear comment with decision.
- Remove blocker label after explicit decision.

## Acceptance Criteria

- Tamerlan is notified when a new blocked issue appears.
- Same issue does not spam repeatedly unless still blocked after 24h.
- Decision is written back as a Linear comment.
- Blocker label is removed only when the response clearly contains a decision.

## Dedupe Rules

Store last notified blocked issue IDs in n8n static data:
- Key: `blocked_decision:{issue_id}:{updated_at_or_label_added_at}`.
- Re-notify after 24h if still blocked.

## Edge Cases

- If multiple blocked issues exist, group them in the daily digest but send immediate alert only for urgent/high issues.
- If Telegram reply is ambiguous, comment it but do not remove blocker.

