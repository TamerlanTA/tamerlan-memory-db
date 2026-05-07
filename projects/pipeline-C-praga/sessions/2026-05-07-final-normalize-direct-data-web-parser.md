# Session 2026-05-07 — Final Normalize Direct Data.Web Parser

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- User showed Firecrawl returning valid `data.web` arrays while Normalize still emitted `debug_no_search_candidates`.
- Replaced Normalize's recursive/parser variants with a direct parser tailored to the observed official Firecrawl output:
  - reads `response.data.web`, `response.web`, `response.data`, `response.results`, and `response.items`
  - extracts only entries with `url`, `link`, or `website`
  - parses domains with regex instead of `new URL(...)`
- Generated final import file:
  - `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting-final-working.workflow.json`

## Validation
- Final workflow contains no Google Sheets nodes.
- Final Normalize code contains `candidatesFromResponse`.
- Final Normalize code contains no `searchCandidates` and no `collectCandidates`.
- Local realistic test using 30 Firecrawl items with `data.web` produced:
  - Normalize: 32 rows
  - Prague Locality Gate: 32 rows
  - Dedupe: 32 rows
  - Prepare Audit Queue Rows: 32 rows

## Next steps
- Import only `pipeline-c-praga-prospecting-final-working.workflow.json`.
- In n8n, verify Normalize code includes `function candidatesFromResponse`.
- Run workflow and inspect final node `Prepare Audit Queue Rows`.
