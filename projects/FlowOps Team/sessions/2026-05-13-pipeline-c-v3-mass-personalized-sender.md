# Session 2026-05-13 — Pipeline C v3 Mass Personalized Sender

## Related
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator|Pipeline C — Website Audit Generator]]
- [[../00 - Overview|FlowOps Team — overview]]

## What was done
- Reworked `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Prospecting.json` so the live cap is no longer 100:
  - default review/audit candidate cap is now 300
  - accepted command caps include 250 and 300
  - query cap raised to 120
  - normalized candidate cap raised to 700
  - scrape cap raised to 360
- Reworked `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Audit Queue.json` from a quality-filter review queue into a mass personalized outbound sender:
  - `Only Qualified Audits` is bypassed; score no longer blocks sending.
  - `Parse Audit JSON` now returns fallback audit/email data instead of hard-failing on malformed OpenAI JSON.
  - OpenAI prompt now forces a personal cold email structure:
    1. greeting and intro as Tamerlan from FlowOps
    2. personal/visible website problem
    3. cooperation offer
    4. automatic signature block appended by parser
  - Recipient selection now uses discovered emails first, then safely infers `info@domain` when no explicit email exists.
  - Airtable post-send updates are sequential instead of four parallel branches.

## Key findings
- Previous run showed `Audit Queue` got only 100 from ~300 found candidates because `Prospecting` still had a 100 candidate cap.
- 46 were filtered by score; this is incompatible with mass outbound mode, so the score gate was bypassed.
- Only 9 were sent because only 9 had explicit recipient emails; inferred `info@domain` fallback should allow most domain-backed leads to receive a message.

## Blockers
- Inferred `info@domain` addresses may bounce more often than discovered emails. This increases reach but should be monitored for Gmail/domain reputation.
- Need live re-import and controlled test run.

## Next steps
- Re-import both updated v3 JSON files into n8n.
- Stop any old active executions using the previous workflow version.
- Run `/pipeline_c 300`.
- Confirm counts:
  - candidates entering Audit Queue near 300
  - score filter no longer removes candidates
  - missing-email branch is low because `info@domain` fallback fills most recipients
  - Gmail sends gradually under throttle
