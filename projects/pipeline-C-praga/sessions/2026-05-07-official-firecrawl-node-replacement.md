# Session 2026-05-07 — Official Firecrawl Node Replacement

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Replaced Firecrawl HTTP Request nodes in the generated n8n workflows with the official Firecrawl node type `@mendable/n8n-nodes-firecrawl.firecrawl`.
- Installed `@mendable/n8n-nodes-firecrawl@2.1.1` into local n8n community nodes at `~/.n8n/nodes`.
- Regenerated workflow JSON, runbook, and validation report.

## Key findings
- Official Firecrawl node uses credential type `firecrawlApi`.
- Search node parameters now use Resource `MapSearch`, Operation `search`, Query `{{$json.source_query}}`, Sources `web`, and dynamic Limit.
- Scrape node parameters now use Resource `Scraping`, Operation `scrape`, URL `{{$json.website}}`, and markdown scrape options.
- Normalization was updated to read Firecrawl v2 search shape `data.web` and preserve upstream metadata from `Search Batch Cap`.
- Scrape parsing was updated to preserve upstream row metadata from `Enrichment Batch Cap`.

## Blockers
- If n8n was already running during package installation, it likely needs a restart before the official Firecrawl node appears.

## Next steps
- Restart n8n if needed.
- Re-import the regenerated prospecting and enrichment workflow JSON.
- Attach Firecrawl API credentials to both Firecrawl nodes and run a small manual test.
