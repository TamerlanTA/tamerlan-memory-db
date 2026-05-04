# Session 2026-05-04 — Pipeline C v2 Completed

## Related
- [[../00 - Overview]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]
- [[../06 - Priorities/What to Do First]]
- [[../08 - Выполненные задачи/Completed]]
- [[2026-05-03-pipeline-c-v2-automated-machine]]

## What was done
- Marked Pipeline C v2 as operationally completed after live confirmation from Tamerlan.
- Updated project memory so Pipeline C is no longer tracked as an unimported/template-only build.
- Recorded that the active launch mode is Telegram command, not schedule:
  - `/pipeline_c`
  - `/audit_sites`
  - `запусти pipeline c`
  - `найди сайты для аудита`
- Later same day, upgraded Prospecting to v2.1 after live runs found the same 2 sites and did not produce enough Telegram review cards for the desired 20-30 emails/day operating target.
- Updated `/Users/tamerlan/Desktop/flowopsteamPipelines/build-pipeline-c-v2-workflows.js` and regenerated `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-c-v2-prospecting-workflow.json`.

## Key Findings
- Pipeline C v2 works end-to-end: Firecrawl automated search/scrape, AI audit queue, Airtable CRM writes, Telegram approval cards, and Gmail send after `Approve + Send`.
- WF-06 remains the only active Telegram Trigger and routes both launch commands and `audit_*` approval callbacks.
- The native Gmail node is the correct send path; Gmail OAuth must not be used through generic HTTP Request in n8n.
- v2.1 Prospecting now runs 24 randomized niche/city/intent queries per launch, requests 8 results/query, normalizes up to 120 unique domains, dedupes by domain/company against Airtable, caps scraping at up to 60 new websites, and sends up to 30 review candidates/run.
- `/pipeline_c 20` can be used for a smaller batch; default is 30.
- Fixed Airtable rate-limit failure introduced by larger v2.1 batches. Previous dedupe made one Airtable GET per normalized candidate (up to 120), causing `RATE_LIMIT_REACHED`. Dedupe now makes one batch Airtable GET for recent lead fields and performs domain/company duplicate detection locally in a Code node, including same-run duplicate detection.
- Fixed `Parse Dedupe Result` returning no output after Airtable batch dedupe. Root cause: candidates were stored in `Prepare Airtable Dedupe Query`, but `Parse Dedupe Result` could lose cross-node context and silently parse an empty candidate list. v2.1.1 now tries `$()`, `$items()`, `$node`, and input fallback; if candidate context is still missing, it emits a diagnostic item instead of empty output, and `Only New Websites` blocks diagnostics from scraping.
- Fixed secondary diagnostic logging failure: `dedupe_context_missing` lacked `airtable_base_id/logs_table_id`, causing Airtable log URL `https://api.airtable.com/v0//` and `NOT_FOUND`. v2.1.2 now includes default base/log IDs on diagnostics, labels diagnostic logs as `Warning`, and `Parse Dedupe Result` also attempts recovery from HTTP input items containing `candidates_json`.
- Root-caused repeated `dedupe_context_missing`: `Prepare Airtable Dedupe Query` serialized candidates into `candidates_json` and truncated it at 90k chars, which produced invalid JSON once the larger 120-candidate pool exceeded that size. v2.1.3 now passes candidates as a native `candidates` array plus an untruncated JSON fallback. Smoke test with 120 candidates produced 120 parsed outputs, 2 Airtable duplicates, and 118 new unique candidates.

## Blockers
- No active build blockers for Pipeline C v2.
- Remaining risks are operational: deliverability, reply quality, Firecrawl result quality, Airtable field drift, campaign copy/filter optimization, and Firecrawl/OpenAI cost from larger batches.

## Next Steps
- Re-import or patch the live Prospecting workflow with the regenerated v2.1.3 JSON before expecting stronger lead volume, no Airtable dedupe rate-limit failure, no silent stop after `Parse Dedupe Result`, no invalid truncated candidate JSON, and no empty Airtable log URL.
- Use Pipeline C operationally from Telegram.
- Review and approve/reject cards as they arrive.
- Track replies and iterate niche/query rotation, scoring, and teaser email copy.
- Use Loom selectively for `Need Loom` or high-fit prospects.
