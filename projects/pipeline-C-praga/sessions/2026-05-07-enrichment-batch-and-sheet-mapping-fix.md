# Session 2026-05-07 — Enrichment Batch and Sheet Mapping Fix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Updated `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/Pipeline C Praga - Enrichment Audit.json`.
- Renamed/configured read node as `Google Sheets - Read Audit Queue` with `resource: sheet` and `operation: read`.
- Increased `Enrichment Batch Cap` from 40 to 75.
- Updated `Parse Contact and Address Clues` to merge Firecrawl output with original rows from `Enrichment Batch Cap`, preserving `run_id`, company, website, domain, business type, source query, and locality fields.
- Changed `Google Sheets - Append Visit Ready Prospects` to `operation: append`.
- Replaced auto-map with explicit mapping for all 29 `Visit Ready Prospects` columns.

## Key findings
- The live failure had two causes: enrichment was processing only one input by the time it reached OpenAI, and official Firecrawl/OpenAI outputs did not carry original lead metadata unless manually re-merged.
- Local smoke test with two sample rows confirmed both rows survive through parse, locality, dedupe, prompt, and map stages with all 29 output columns present.

## Blockers
- User should clear the bad partial rows already written to `Visit Ready Prospects` before rerunning.

## Next steps
- Re-import the updated enrichment workflow.
- Configure credentials.
- Run from the workflow manual trigger, not by executing only the OpenAI node.
- Check item counts at `Build AI Audit Prompt`, `OpenAI - Structured Audit`, and `Map Visit Ready Table Row`.
