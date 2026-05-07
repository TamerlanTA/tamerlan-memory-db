# Current State

## Related
- [[projects/pipeline-C-praga/overview]]
- [[projects/pipeline-C-praga/decisions]]
- [[projects/pipeline-C-praga/risks]]
- [[projects/pipeline-C-praga/next-steps]]
- [[projects/pipeline-C-praga/prompts]]

## Content
- Project created on 2026-05-07 as a new FlowOps-related workstream.
- Importable n8n workflow JSON package now exists in `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/`.
- Generated workflows:
  - `pipeline-c-praga-prospecting.workflow.json`
  - `pipeline-c-praga-enrichment-audit.workflow.json`
  - `pipeline-c-praga-error-handler.workflow.json`
- 2026-05-07 hotfix: Firecrawl/OpenAI HTTP Request nodes were regenerated as `typeVersion: 4.2`; Firecrawl Search now imports as `POST` with JSON body instead of falling back to `GET`.
- 2026-05-07 follow-up: Firecrawl HTTP Request nodes were replaced with the official Firecrawl n8n community node type `@mendable/n8n-nodes-firecrawl.firecrawl`.
- Local n8n node package installed in `~/.n8n/nodes`: `@mendable/n8n-nodes-firecrawl@2.1.1`.
- Prospecting uses Firecrawl `MapSearch/search`; enrichment uses Firecrawl `Scraping/scrape`.
- 2026-05-07 second follow-up: `Normalize URLs and Reject Aggregators` was made robust for official Firecrawl output (`success: true`, `data.web: [...]`) and no longer depends unsafely on `$items('Search Batch Cap')` during manual step execution.
- 2026-05-07 third follow-up: Normalize code was simplified further to remove all `$items`/upstream-node dependencies and emit a diagnostic item if no URL candidates are found, so n8n no longer silently stops after the node.
- 2026-05-07 fourth follow-up: Normalize code now recursively extracts URL candidates from official Firecrawl output and handles `data.web` whether n8n represents it as an array or object. Local tests confirmed Normalize outputs leads and `Prague Locality Gate` passes Prague rows.
- 2026-05-07 hardening pass: generated a ready Prospecting workflow with Google Sheets removed from the main path. The final node is `Prepare Audit Queue Rows`; this avoids `Could not retrieve the column data!` errors while validating Firecrawl -> Normalize -> Locality -> Dedupe. Import file: `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting-ready-no-sheets.workflow.json`.
- 2026-05-07 final Normalize fix: generated `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting-final-working.workflow.json`. Normalize now uses direct `candidatesFromResponse(response.data.web)` parsing and no longer uses `searchCandidates`, `collectCandidates`, or the global `URL` constructor.
- 2026-05-07 quality hardening: final prospecting workflow was regenerated after live `Prepare Audit Queue Rows` produced 75 rows but with blank `run_id`, `business_type`, and `source_query`, plus aggregator/directories in the queue. Normalize now restores metadata from `Search Batch Cap`, filters more aggregator domains (`bookimed`, `firmy`, `znamylekar`, `whatclinic`, `reddit`, `mindbodyonline`, etc.), and `Prague Locality Gate` no longer treats generic `CZ`, `Czech Republic`, or `+420` as Prague-local evidence.
- 2026-05-07 Google Sheets step: generated `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting-with-sheets.workflow.json`. It keeps the working prospecting path and adds `Google Sheets - Append Audit Queue` after `Prepare Audit Queue Rows`, appending to the `Audit Queue` tab with `autoMapInputData`. Header helper file generated at `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/audit-queue-headers.csv`.
- 2026-05-07 enrichment Firecrawl replacement: user-provided enrichment import file `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/Pipeline C Praga - Enrichment Audit.json` now uses the official Firecrawl node type `@mendable/n8n-nodes-firecrawl.firecrawl` for `Firecrawl Scrape - Homepage` with `resource: Scraping`, `operation: scrape`, `url: {{$json.website}}`, markdown output, retries, and `continueRegularOutput`.
- 2026-05-07 enrichment OpenAI replacement: the same enrichment import file now uses the official OpenAI node type `@n8n/n8n-nodes-langchain.openAi` for `OpenAI - Structured Audit` with `resource: text`, `operation: message`, model `gpt-4.1-mini`, JSON output, and temperature `0.2`. `Map Visit Ready Table Row` was hardened to merge original rows from `Build AI Audit Prompt` with the OpenAI output so business metadata is not lost.
- 2026-05-07 enrichment batch/Sheets fix: `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/Pipeline C Praga - Enrichment Audit.json` now reads `Audit Queue` explicitly with Google Sheets `operation: read`, caps enrichment at 75 rows, preserves source lead metadata after Firecrawl scrape, writes `Visit Ready Prospects` with `operation: append`, and maps all 29 visit-ready columns explicitly. Local smoke test with 2 sample queue rows confirmed both rows survive through parse/gate/dedupe/prompt/map and all output columns are present.
- Runbook, table schema, and validation report are generated in `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/`.
- Source reference is FlowOps Pipeline C v2/v2.1, but this project must adapt it for offline/local field sales rather than email-first outbound.

## Known source context
- Existing Pipeline C v2 uses Telegram command launch, Firecrawl search/scrape, Airtable dedupe, AI audit generation, Telegram review cards, and Gmail send only after approve.
- Prague version should keep the strong parts: split architecture, dedupe, logging, validation, no silent failures, and bounded candidate batches.
- Prague version should change the output: table rows for local visits, including address, neighborhood, business type, website, contact info, observed pain, automation opportunity, fit score, and next action.
