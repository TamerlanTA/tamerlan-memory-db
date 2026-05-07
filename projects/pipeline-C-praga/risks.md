# Risks

## Related
- [[projects/pipeline-C-praga/overview]]
- [[projects/pipeline-C-praga/current-state]]
- [[projects/pipeline-C-praga/decisions]]
- [[projects/pipeline-C-praga/next-steps]]
- [[projects/pipeline-C-praga/prompts]]

## Content
- Search APIs may return non-Prague or directory/social results; workflow needs strict Prague evidence checks.
- Duplicate businesses may appear across queries, directories, and localized domains; dedupe by normalized domain, company name, phone, and address.
- Public websites may lack full address/contact data; workflow should mark missing fields and keep rows visit-reviewable rather than silently dropping useful leads.
- n8n generated JSON can be syntactically valid but operationally wrong; require node-level/workflow-level validation loops and a validation report.
- Historical issue: if Firecrawl is implemented as an HTTP Request node with old `typeVersion: 1`, n8n can ignore `method: POST` and default Firecrawl Search to GET, causing `404 Cannot GET /v1/search`. Current regenerated workflows avoid this by using the official Firecrawl node.
- Firecrawl HTTP nodes have now been replaced by the official Firecrawl node, but n8n must have `@mendable/n8n-nodes-firecrawl` installed and loaded. Restart n8n after package installation if the node is missing in the UI.
- Table schema drift can break writes; output should document exact required columns and credential placeholders.
- Avoid sending outreach automatically in v1; this is for manual in-person sales preparation.
