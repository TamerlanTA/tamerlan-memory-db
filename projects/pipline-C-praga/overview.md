# Pipeline C Praga Overview

## Related
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[prompts]]
- [[../FlowOps Team/00 - Overview]]
- [[../FlowOps Team/03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]

## Content
Pipeline C Praga is a localized version of FlowOps [[../FlowOps Team/03 - Acquisition Pipelines/Pipeline C — Website Audit Generator|Pipeline C]] for Prague businesses.

The goal is to generate a vetted table of Prague-local businesses that Tamerlan's friend can visit in person and pitch directly. Unlike the existing Pipeline C, this project should prioritize local physical presence, address/neighborhood evidence, visit-readiness, and spreadsheet output over automated cold-email sending.

Core idea:
- Find business websites only in Prague.
- Enrich with public website/contact/address/context data.
- Audit each business for automation opportunities.
- Score for in-person sales fit.
- Save results to a table for manual outreach and deal-making.

Expected automation stack:
- n8n workflows
- Firecrawl Search/Scrape or equivalent web search/scrape path
- OpenAI/LLM audit generation
- Google Sheets or Airtable table output
- robust dedupe, logging, retry, and validation design

