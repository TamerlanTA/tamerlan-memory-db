# Session 2026-05-07 — Firecrawl Search HTTP Method Hotfix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated Firecrawl Search failure in `Pipeline C Praga - Prospecting`.
- Root cause: n8n UI showed `Firecrawl Search - Prague Queries` using `GET`; Firecrawl `/v1/search` requires `POST` with a JSON body.
- Updated `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/build-pipeline-c-praga-workflows.mjs` so HTTP Request nodes use `typeVersion: 4.2`.
- Regenerated all workflow JSON and documentation.

## Key findings
- The exported node parameters already had `method: "POST"`, but the node itself was `typeVersion: 1`, which can import into n8n with the method ignored/defaulted to `GET`.
- Regenerated workflow now verifies:
  - `Firecrawl Search - Prague Queries`: `typeVersion=4.2`, `method=POST`, `sendBody=true`, `contentType=json`
  - `Firecrawl Scrape - Homepage`: `typeVersion=4.2`, `method=POST`
  - `OpenAI HTTP - Structured Audit`: `typeVersion=4.2`, `method=POST`

## Blockers
- The live n8n instance shown in the browser was not directly updated through an API in this session; re-import/update the workflow JSON or manually switch the node to POST in the UI.

## Next steps
- Re-import `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting.workflow.json` into n8n.
- Run `Firecrawl Search - Prague Queries` again and confirm the response is search JSON rather than `404 Cannot GET /v1/search`.
