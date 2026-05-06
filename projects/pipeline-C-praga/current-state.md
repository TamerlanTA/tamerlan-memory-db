# Current State

## Related
- [[projects/pipeline-C-praga/overview]]
- [[projects/pipeline-C-praga/decisions]]
- [[projects/pipeline-C-praga/risks]]
- [[projects/pipeline-C-praga/next-steps]]
- [[projects/pipeline-C-praga/prompts]]

## Content
- Project created on 2026-05-07 as a new FlowOps-related workstream.
- No n8n workflow JSON has been built yet.
- Desired deliverable is a production-ready n8n architecture/workflow JSON package for Prague-only business prospecting.
- Source reference is FlowOps Pipeline C v2/v2.1, but this project must adapt it for offline/local field sales rather than email-first outbound.

## Known source context
- Existing Pipeline C v2 uses Telegram command launch, Firecrawl search/scrape, Airtable dedupe, AI audit generation, Telegram review cards, and Gmail send only after approve.
- Prague version should keep the strong parts: split architecture, dedupe, logging, validation, no silent failures, and bounded candidate batches.
- Prague version should change the output: table rows for local visits, including address, neighborhood, business type, website, contact info, observed pain, automation opportunity, fit score, and next action.

