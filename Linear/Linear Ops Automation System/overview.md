# Linear Ops Automation System

## Related
- [[../Linear Ops Automation System/01-daily-command-center|Daily Command Center]]
- [[../Linear Ops Automation System/02-blocked-decision-bot|Blocked Decision Bot]]
- [[../Linear Ops Automation System/03-team-assignment-notifier|Team Assignment Notifier]]
- [[../Linear Ops Automation System/04-stale-issue-reminder|Stale Issue Reminder]]
- [[../Linear Ops Automation System/05-linear-to-obsidian-memory-sync|Linear to Obsidian Memory Sync]]
- [[../Linear Ops Automation System/06-weekly-flowops-review|Weekly FlowOps Review]]
- [[projects/FlowOps Team/00 - Overview|FlowOps Team]]
- [[projects/FlowOps Team/Team Task Automation]]

## Purpose

Design a practical automation layer around Linear so FlowOps work does not become a passive task board.

Operating model:
- **Linear** = active execution, ownership, issue status, daily priorities.
- **Obsidian** = long-term memory, project history, session notes, reusable context.
- **Telegram** = fast operational notifications and decision prompts.
- **n8n** = automation engine.

## Scope

Build almost all proposed Linear automations except voice/Telegram task creation. Tamerlan will continue assigning tasks manually with an agent.

Included automations:
1. Daily Command Center.
2. Blocked Decision Bot.
3. Team Assignment Notifier.
4. Stale Issue Reminder.
5. Linear to Obsidian Memory Sync.
6. Weekly FlowOps Review.

Excluded:
- Voice/Telegram -> Linear Task Creator.

## Recommended Build Order

### Phase 1 — Control
1. [[01-daily-command-center]]
2. [[02-blocked-decision-bot]]

Why first: these give Tamerlan immediate control over priorities and blockers.

### Phase 2 — Team Execution
3. [[03-team-assignment-notifier]]
4. [[04-stale-issue-reminder]]

Why second: these make Adil, Aslanbek, and Alexey easier to manage without constant manual chasing.

### Phase 3 — Memory and Review
5. [[05-linear-to-obsidian-memory-sync]]
6. [[06-weekly-flowops-review]]

Why third: these preserve continuity and create weekly operating rhythm.

## Shared Design Rules

- Do not create duplicate Linear issues.
- Do not write secrets, API keys, tokens, cookies, or private credentials to Obsidian or Linear comments.
- All automation writes should be traceable through n8n execution logs.
- Telegram messages should be short and action-oriented.
- Linear comments should be factual: status, decision, blocker, result.
- Obsidian memory writes should be concise and operational, not raw dumps.
- If an automation is uncertain, it should ask Tamerlan instead of guessing.

## Key Decisions Needed

- Final source-of-truth rule: Linear only, Obsidian only, or hybrid. Recommended: **Linear for active execution, Obsidian for memory and handoffs**.
- Telegram recipients/chats for Tamerlan and team members.
- Linear API access method and n8n credentials.
- Whether completed issues should create session notes automatically for all projects or only FlowOps.
- Exact stale threshold: recommended 24h for urgent/high and 48h for medium/low.

## Implementation Notes

Use n8n workflows with:
- Linear trigger / scheduled Linear polling.
- Telegram node for notifications.
- GitHub or local filesystem write for Obsidian memory, depending on the deployment environment.
- Static data or a small datastore for dedupe keys.

Each workflow should include:
- Manual trigger for testing.
- Clear error branch.
- Execution summary.
- Dedupe key.
- Test payloads.

