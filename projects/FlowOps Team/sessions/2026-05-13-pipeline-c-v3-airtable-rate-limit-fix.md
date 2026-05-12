# Session 2026-05-13 — Pipeline C v3 Airtable Rate Limit Fix

## Related
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator|Pipeline C — Website Audit Generator]]
- [[../00 - Overview|FlowOps Team — overview]]

## What was done
- Fixed Airtable `RATE_LIMIT_REACHED` in `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Audit Queue.json`.
- The previous batch gate delayed whole batches but released all items inside a batch together.
- `Assign Audit Queue Batch Delay` now adds per-item stagger inside each batch:
  - default batch size: 30
  - default batch gap: 5 minutes
  - default item gap: 3 seconds
  - item wait formula: batch offset + item index inside batch * item gap
- Added retry/backoff to Airtable HTTP nodes in both Prospecting and Audit Queue:
  - `retryOnFail: true`
  - `maxTries: 6`
  - `waitBetweenTries: 7000`
  - HTTP timeout: 120000ms
- Added retry/backoff to `Gmail Auto Send Email`:
  - `retryOnFail: true`
  - `maxTries: 4`
  - `waitBetweenTries: 10000`

## Key findings
- Airtable failed at `Airtable Create Lead` item 40 because items inside the first/second batch were still being processed too concurrently.
- Real pacing needs both batch spacing and per-item staggering, not just batch-level waits.

## Blockers
- Needs live n8n re-import and production run validation.

## Next steps
- Re-import updated Prospecting and Audit Queue JSON files.
- Run `/pipeline_c 100`.
- If Airtable still rate limits, lower input overrides to `audit_batch_size: 15` and `audit_item_gap_seconds: 5`.
