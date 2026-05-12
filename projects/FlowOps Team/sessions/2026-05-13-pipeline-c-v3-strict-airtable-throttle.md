# Session 2026-05-13 — Pipeline C v3 Strict Airtable Throttle

## Related
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator|Pipeline C — Website Audit Generator]]
- [[../00 - Overview|FlowOps Team — overview]]

## What was done
- Updated `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Audit Queue.json` after another live `RATE_LIMIT_REACHED` at `Airtable Create Lead` item 35.
- Added `Wait Before Airtable Create Lead` directly before `Airtable Create Lead`.
- Split pacing into two layers:
  - light OpenAI stagger before audit generation (`openai_item_gap_seconds`, default 2s)
  - strict Airtable throttle before CRM creation (`airtable_create_lead_wait_seconds`)
- New conservative defaults:
  - `audit_batch_size`: 10
  - `audit_batch_gap_minutes`: 5
  - `audit_item_gap_seconds`: 15
- Strengthened Airtable HTTP retry/backoff:
  - `maxTries: 10`
  - `waitBetweenTries: 15000`
  - `timeout: 180000`
  - HTTP Request batching option: 1 request per 2500ms where supported.

## Key findings
- The previous wait before OpenAI did not guarantee pacing at Airtable because OpenAI/Parse can return many items together.
- The throttle must sit immediately before the rate-limited provider node, especially `Airtable Create Lead`.

## Blockers
- Need re-import into n8n and stop any old active executions still using the prior workflow version.

## Next steps
- Re-import `Pipeline C v3 - Audit Queue.json`.
- Stop older failed/running executions before retesting.
- Retest with `/pipeline_c 100`.
- If Airtable still rate limits, set `audit_batch_size: 5` and `audit_item_gap_seconds: 30`.
