# Session 2026-05-09 — FlowOps Opportunity Engine Skill

## Related
- [[../00 - Overview]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]
- [[../02 - Offers/Speed-to-Lead System]]
- [[../06 - Priorities/What to Do First]]
- [[../08 - Выполненные задачи/Completed]]
- [[../../../current-focus]]

## What was done
- Created a new reusable Codex skill:
  - `/Users/tamerlan/.codex/skills/flowops-opportunity-engine/`
- The skill frames FlowOps acquisition as an opportunity radar, not a generic CRM or lead-list workflow.
- Added the required `SKILL.md`, UI metadata, and focused reference files:
  - `references/signal-taxonomy.md`
  - `references/scoring-rubric.md`
  - `references/audit-format.md`
  - `references/outreach-patterns.md`
  - `references/compliance-guardrails.md`

## Key findings
- This belongs to existing FlowOps Team / Pipeline C / Speed-to-Lead context, not a new project folder.
- The skill should be used for trigger-based prospecting across job postings, reviews, websites, tech stack gaps, event/exhibitor pages, local business sources, and enrichment sources.
- Core rule: every outreach output must be based on visible evidence, a specific operational hypothesis, and a concrete FlowOps offer angle.
- The skill explicitly prevents fake Loom claims and requires compliance-safe source/relevance/opt-out tracking.
- Later correction from Tamerlan: this skill must not search Upwork or other freelance platforms because Upwork already has a separate prepared pipeline. FlowOps Opportunity Engine is for direct non-marketplace prospecting from company-owned/public signals.

## Blockers
- No implementation blocker.
- Next operational risk is validating the skill on real prospects and folding the best fields into Airtable/Telegram review cards if useful.

## Next steps
- Test the skill on 5-10 real companies from Pipeline C or event/exhibitor sources.
- Compare generated opportunity briefs against current Pipeline C audit output.
- If quality improves, update n8n prompt templates and Airtable fields to include signal source, confidence, compliance notes, and recommended Loom angle.
- When using the skill for lead search, exclude Upwork, Fiverr, Freelancer.com, Contra, Toptal, PeoplePerHour, Guru, and similar freelance marketplaces.
