# Session 2026-05-13 — Pipeline C v3 Batch Gate

## Related
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator|Pipeline C — Website Audit Generator]]
- [[../00 - Overview|FlowOps Team — overview]]

## What was done
- Updated `/Users/tamerlan/Desktop/flowopsteamPipelines/Pipeline C v3 - Audit Queue.json`.
- Added an audit queue batch gate before OpenAI/Airtable/Gmail work:
  - `Assign Audit Queue Batch Delay`
  - `Wait Batch Window`
- Default pacing is 30 items per batch with a 5 minute gap.
- The gate is configurable through incoming fields:
  - `audit_batch_size`
  - `send_batch_size`
  - `batch_size`
  - `audit_batch_gap_minutes`
  - `send_batch_gap_minutes`
  - `batch_gap_minutes`
- Batch metadata is carried through the workflow and added to Lead notes/log snapshots.

## Key findings
- A single Wait path is safer than splitting into direct/wait branches because it preserves candidate context for `Parse Audit JSON` after delayed batches.
- `Parse Audit JSON` now uses `Wait Batch Window` as the primary candidate source, with fallback to `Assign Audit Queue Batch Delay` and `When Called by Prospecting`.

## Blockers
- Need live n8n import/run validation to confirm the Wait node behavior in the user’s exact n8n version.

## Next steps
- Import the updated Audit Queue JSON.
- Run `/pipeline_c 100` and confirm batch 1 starts almost immediately, batch 2 waits ~5 minutes, batch 3 waits ~10 minutes, etc.
- If Gmail deliverability/rate limits still complain, lower to `audit_batch_size: 15` and `audit_batch_gap_minutes: 10`.
