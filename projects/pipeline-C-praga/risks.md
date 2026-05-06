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
- Table schema drift can break writes; output should document exact required columns and credential placeholders.
- Avoid sending outreach automatically in v1; this is for manual in-person sales preparation.

