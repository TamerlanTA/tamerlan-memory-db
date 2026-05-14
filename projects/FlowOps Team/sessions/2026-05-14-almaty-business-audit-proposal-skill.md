# Session 2026-05-14 — Almaty Business Audit Proposal Skill

## Related
- [[../00 - Overview|overview]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator|Pipeline C — Website Audit Generator]]
- [[../03 - Acquisition Pipelines/Pipeline D — Demo Library|Pipeline D — Demo Library]]
- [[../Sales Steps]]

## What was done
- Created Codex skill `almaty-business-audit-proposal` at `/Users/tamerlan/.codex/skills/almaty-business-audit-proposal/`.
- The skill turns public evidence from Almaty/Kazakhstan businesses into website/business audits, Fit Scores, Loom scripts, outreach, and complete КП/commercial proposals.
- Added reference files for audit checklist, scoring, and proposal template.
- Validated the skill with `quick_validate.py`; result: valid.

## Key findings
- This complements `flowops-opportunity-engine`: the older skill is broader prospect diagnosis/outreach; the new skill is specifically for local Almaty business audits and full commercial proposals.
- The skill defaults to Russian owner-facing output and emphasizes WhatsApp, 2GIS/Google/Instagram, missed calls, booking, CRM, follow-up, and practical sprint offers.

## Blockers
- No blockers.
- Pricing is intentionally left as user-provided or assumption-based placeholders to avoid fake market certainty.

## Next steps
- Use `$almaty-business-audit-proposal` when preparing КП for specific Almaty businesses.
- If repeated proposals converge on standard package pricing, add those prices to the skill or FlowOps offer notes.
- Forward-test the skill on 2-3 real Almaty businesses before using it for scaled outbound.
