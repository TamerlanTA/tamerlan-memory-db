# Next Steps

## Related
- [[projects/pipeline-C-praga/overview]]
- [[projects/pipeline-C-praga/current-state]]
- [[projects/pipeline-C-praga/decisions]]
- [[projects/pipeline-C-praga/risks]]
- [[projects/pipeline-C-praga/prompts]]

## Content
1. Create a Google Sheet with a tab named exactly `Audit Queue`.
2. Put the exact row-1 headers from `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/audit-queue-headers.csv`.
3. Import `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting-with-sheets.workflow.json`.
4. In `Google Sheets - Append Audit Queue`, configure the Google Sheets credential and replace `CONFIGURE_GOOGLE_SHEET_ID` with the real spreadsheet ID.
5. Run the workflow end-to-end and verify 75 rows append to `Audit Queue`.
6. After rows append successfully, import/run `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/Pipeline C Praga - Enrichment Audit.json` against the prepared queue.
7. In the enrichment workflow, configure credentials on `Firecrawl Scrape - Homepage`, `OpenAI - Structured Audit`, and the Google Sheets nodes before running.
8. Re-import the updated enrichment workflow before rerunning; clear the bad partial rows in `Visit Ready Prospects` if needed, then run the whole workflow from the manual trigger rather than executing only the OpenAI step.
