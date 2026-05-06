# Prompts

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[../FlowOps Team/03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]

## Content
Reusable Night Runner task prompt for building Pipeline C Praga:

```md
# Task name
Pipeline C Praga — n8n Local Business Prospecting System

## Goal
Build an import-ready n8n automation system that finds only Prague-local business websites, audits them for FlowOps-style automation opportunities, and saves visit-ready results into a table so Tamerlan's friend can personally visit the businesses and negotiate deals.

## Memory
Project memory directory:
`projects/pipline-C-praga`

Before implementation, read `.agent/reports/memory-preload.md` if it exists. Treat it as bounded prior context. Do not independently scan Obsidian.

Use FlowOps Pipeline C as the architectural reference:
- Existing Pipeline C v2 split: Prospecting, Audit Queue, Approval Handler.
- Keep the strong patterns: Firecrawl search/scrape, dedupe, AI audit generation, logging, retry/error handling, no silent failures, capped batches.
- Adapt the output for Prague field sales: table rows for manual/in-person outreach, not automatic cold email.

## Scope
Only create or update files under:
- `pipline-C-praga/`

Expected files:
- `pipline-C-praga/build-pipeline-c-praga-workflows.mjs`
- `pipline-C-praga/workflows/pipeline-c-praga-prospecting.workflow.json`
- `pipline-C-praga/workflows/pipeline-c-praga-enrichment-audit.workflow.json`
- `pipline-C-praga/workflows/pipeline-c-praga-error-handler.workflow.json`
- `pipline-C-praga/table-schema.md`
- `pipline-C-praga/runbook.md`
- `pipline-C-praga/validation-report.md`

You may add additional files inside `pipline-C-praga/` only if they are directly required for validation or import readiness.

Use only Node.js built-ins for local generation/validation scripts. Do not install dependencies.

## Required n8n skill usage
Use all relevant n8n skills available in the environment. At minimum, apply the guidance from:
- `n8n-automation`
- `n8n-automation-architect`
- `n8n-workflow-automation`
- `n8n-workflow-patterns`
- `n8n-workflow-generator`
- `n8n-node-configuration`
- `n8n-code-javascript`
- `n8n-expression-syntax`
- `n8n-validation-expert`
- `n8n-workflow-testing-fundamentals`
- `n8n-mcp-tools-expert`

If n8n MCP tools are available, use them for node discovery and validation:
- search/get relevant nodes before finalizing node types
- validate important node configs
- validate complete workflow JSON
- iterate until errors are fixed or document exactly why validation cannot be completed

If n8n MCP tools are not available, do local validation instead and document that limitation in `validation-report.md`.

## Workflow requirements
Design this as a robust n8n system, not a loose draft.

The system should include:
1. Manual Trigger for local testing.
2. Optional Schedule Trigger, inactive by default, for periodic Prague prospecting.
3. Prague-only prospecting queries.
4. Firecrawl Search or equivalent HTTP Request search path.
5. Strict result normalization:
   - normalize website URL and domain
   - reject social networks, Google/Maps result pages, directories, marketplaces, job boards, irrelevant aggregator pages unless used only as weak fallback evidence
   - reject or flag results without Prague-local evidence
6. Prague locality gate:
   - accept only businesses with evidence such as Prague address, `Praha`, `Prague`, Prague districts, Czech phone/address clues, or website content indicating Prague operations
   - include `locality_evidence` and `locality_confidence`
7. Dedupe:
   - domain
   - company name
   - phone
   - address
   - same-run duplicate detection
8. Scrape/enrichment:
   - homepage
   - contact page if discoverable
   - services/about page if discoverable
   - public text only
9. AI audit generation:
   - business type/niche
   - observed bottleneck
   - automation opportunity
   - suggested FlowOps offer
   - in-person pitch angle
   - fit score 1-10
   - confidence
   - short Czech/English-friendly notes for a human visit
10. Table write:
   - Google Sheets preferred unless Airtable is easier to model
   - no credentials/secrets in JSON
   - use placeholder credential names only
11. Logging:
   - run_id
   - started/completed timestamps
   - counts: found, rejected, duplicates, scraped, audited, written
   - error rows
12. Error handling:
   - retries/backoff for external APIs where n8n supports it
   - failed item queue/table
   - no silent failure
13. Batch controls:
   - cap total search queries
   - cap scrape count
   - cap table rows per run
   - document default values and how to change them

## Prague search strategy
Include a practical search plan focused on businesses a person can physically visit in Prague.

Use query packs for niches such as:
- dental clinics Prague / zubní klinika Praha
- beauty salons Prague / kosmetický salon Praha
- med spas / aesthetic clinics Prague
- gyms and fitness studios Prague
- restaurants and cafes Prague
- real estate agencies Prague / realitní kancelář Praha
- coworking spaces Prague
- language schools Prague / jazyková škola Praha
- private clinics Prague / soukromá klinika Praha
- local service businesses Prague

Queries should include Prague district/location variants:
- Prague, Praha
- Praha 1 through Praha 10
- Vinohrady, Karlín, Žižkov, Smíchov, Dejvice, Holešovice, Anděl, Nové Město, Staré Město

## Table schema
Create `table-schema.md` with exact columns. Include at least:
- Run ID
- Date found
- Company
- Website
- Domain
- Business type
- Prague address
- Neighborhood / district
- Phone
- Email
- Contact page
- Source query
- Locality evidence
- Locality confidence
- Website notes
- Bottleneck
- Automation opportunity 1
- Automation opportunity 2
- Suggested offer
- Fit score
- Confidence
- Visit priority
- In-person pitch angle
- Suggested first sentence
- Status
- Next action
- Owner
- Notes
- Last checked

## Do not touch
Do not modify app/source files outside `pipline-C-praga/`.
Do not modify `.env`, credentials, deployment files, billing files, or package/dependency files.
Do not install dependencies.
Do not write to Obsidian memory directly.
Do not create workflows that send cold email automatically in v1.
Do not include real API keys, secrets, tokens, or credential IDs.

## Acceptance criteria
- `pipline-C-praga/build-pipeline-c-praga-workflows.mjs` exists and uses only Node.js built-ins.
- Running the builder creates the workflow JSON files under `pipline-C-praga/workflows/`.
- All generated workflow JSON files parse successfully.
- Workflow JSON is import-oriented n8n JSON with `name`, `nodes`, `connections`, `settings`, and `active: false`.
- Workflows include Prague-only locality gates and table output.
- Workflows include dedupe, logging, batch caps, and error handling.
- `table-schema.md` documents the output table fields.
- `runbook.md` explains setup, credentials, import steps, test steps, operating steps, and troubleshooting.
- `validation-report.md` documents all validation performed, including n8n MCP validation if available, local JSON parse validation, Code node syntax checks, and any remaining risks.
- No files outside `pipline-C-praga/` are modified.

## Validation commands
- `node --check pipline-C-praga/build-pipeline-c-praga-workflows.mjs`
- `node pipline-C-praga/build-pipeline-c-praga-workflows.mjs`
- `node -e "const fs=require('fs'); for (const f of fs.readdirSync('pipline-C-praga/workflows').filter(f=>f.endsWith('.json'))) { const p='pipline-C-praga/workflows/'+f; const j=JSON.parse(fs.readFileSync(p,'utf8')); if (!j.name || !Array.isArray(j.nodes) || !j.connections || !j.settings || j.active !== false) throw new Error('Invalid n8n workflow shape: '+p); } console.log('workflow json ok');"`
- `git status`

## Final report requirements
In `.agent/reports/executor-report.md`, include:
- files created
- architecture summary
- how Prague-only filtering works
- table destination and schema summary
- n8n skills/MCP validation used
- validation command results
- risks/manual setup still required
```

Use this project memory directory for Memory Preload:

```json
{
  "project_memory_dir": "projects/pipline-C-praga"
}
```
