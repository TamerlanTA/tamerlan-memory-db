# Session 2026-05-03 — Linear Initial Migration

## Related
- [[00 - Overview]]
- [[What to Do First]]
- [[Team Task Automation]]
- [[CRM Automation Plan]]
- [[Airtable CRM Build Spec]]
- [[Pipeline A — Upwork Radar]]
- [[Pipeline D — Demo Library]]

## What was done
- Used the connected Linear workspace and migrated operational FlowOps memory from `projects/FlowOps Team` plus `My-Team`.
- Confirmed Linear team: `FlowOps Team`.
- Created 18 FlowOps-specific issue labels, including `FlowOps`, `n8n`, `CRM`, `Sales`, `Docs`, `Demo Library`, pipeline labels, offer labels, owner labels for Adil/Aslanbek/Alexey, `MVP`, and `Blocked: needs decision`.
- Created 8 Linear projects:
  - `FlowOps OS — Master Build`
  - `Demo Library — First 10 Loom Assets`
  - `Upwork Radar — Revenue Pipeline`
  - `FlowOps CRM — Airtable + Automation`
  - `Website Audit Generator — Cold Outreach`
  - `LinkedIn Pain Radar — Warm Outreach`
  - `Sales Assets + Documentation Kit`
  - `Retainer Conversion System`
- Created issues `FLO-5` through `FLO-24` from current priorities, active My-Team tasks, completed Aslanbek website redesign, CRM work, sales docs, acquisition pipelines, and retainer conversion.
- Marked Linear onboarding placeholders `FLO-1` through `FLO-4` as done with short explanations.

## Key findings
- Initial Linear read exposed only Tamerlan and the system Linear user, but later issue updates showed assignable users for at least Aslanbek (`kalabayaslanbek@gmail.com`) and Adil (`vlastus11@gmail.com`).
- Owner labels are still useful for filtering, but some issues can now also use real Linear assignees.
- Linear MCP discovery listed initiative/document/status-update tools, but calls to those tools returned `tool not found`; project and issue descriptions now hold the migrated context instead.

## Follow-up update — issue detail pass
- After Tamerlan noted that the first issue pass was too shallow, existing issues `FLO-5` through `FLO-24` were rewritten in-place with clearer task briefs.
- No new issues were created during this pass.
- Updated issue descriptions now generally include context, goal, work steps, deliverables, acceptance/done criteria, and update expectations.
- Important semantic corrections:
  - CRM tasks now assume FlowOps CRM exists and focus on QA/automation readiness instead of base creation from zero.
  - LinkedIn Pain Radar task now treats Pipeline B as completed and asks for operational QA/first batch rather than initial planning.
  - Adil and Aslanbek tasks were rewritten with owner-specific clarity based on `My-Team` profiles.

## Blockers
- Need Alexey to appear as a clear/assignable Linear user and have profile details filled before meaningful ownership can be assigned.
- Need decision on whether Obsidian task files continue syncing into Linear, Linear becomes source of truth, or a bidirectional process is needed.
- Need decisions for blocked active tasks:
  - Speed-to-Lead CRM/storage target.
  - Speed-to-Lead instant reply channel.
  - FlowOps docs platform/format and brand style.

## Next steps
- In Linear, start with `FLO-5`, `FLO-10`, `FLO-13`, and `FLO-17`.
- Confirm assignee mapping for Adil/Aslanbek/Alexey and keep owner labels for filtering.
- Run `FLO-13` as CRM QA/automation-readiness, not as fresh CRM creation.
- Decide task source-of-truth rule for [[Team Task Automation]] before wiring any Obsidian-to-Linear automation.
