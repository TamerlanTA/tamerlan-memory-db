# Session 2026-05-07 — Post Queue Quality Hardening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Regenerated `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting-final-working.workflow.json`.
- Updated `Normalize URLs and Reject Aggregators` to restore source metadata from `Search Batch Cap` when official Firecrawl nodes return only `{ success, data, creditsUsed, id }`.
- Expanded aggregator filtering for directories and research/forum pages such as `bookimed.com`, `firmy.cz`, `znamylekar.cz`, `whatclinic.com`, `reddit.com`, `mindbodyonline.com`, `topbeautyprague.com`, and `salony-krasy.cz`.
- Tightened `Prague Locality Gate` so generic `CZ`, `Czech Republic`, and `+420` are no longer enough to pass locality.

## Key findings
- Live `Prepare Audit Queue Rows` proved the main Firecrawl -> Normalize -> Locality -> Dedupe -> Prepare path works and can produce 75 queue rows.
- The queue quality issue was metadata loss plus an overly broad locality clue, not a broken Firecrawl search.
- Local smoke test confirmed aggregator rows are filtered and `run_id`, `business_type`, and `source_query` are restored.

## Blockers
- Google Sheets append still requires a real sheet/tab with exact headers before reintroducing any Sheets node.

## Next steps
- Re-import the regenerated final prospecting workflow and rerun.
- Inspect `Prepare Audit Queue Rows` for non-empty metadata and fewer aggregator rows.
- Only after queue quality is acceptable, create the Google Sheet with the required headers and wire append/enrichment.
