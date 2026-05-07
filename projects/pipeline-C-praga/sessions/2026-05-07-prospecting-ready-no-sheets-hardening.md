# Session 2026-05-07 — Prospecting Ready No-Sheets Hardening

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- User requested a full pass instead of one-error-at-a-time fixes.
- Reworked the Prospecting workflow so Google Sheets nodes are not in the main execution path.
- Added final Code node `Prepare Audit Queue Rows` that outputs import-ready rows inside n8n.
- Wrote a duplicate hardened import file:
  - `/Users/tamerlan/Desktop/pipeline-C-praga/pipline-C-praga/workflows/pipeline-c-praga-prospecting-ready-no-sheets.workflow.json`
- Removed the potentially invalid `settings.errorWorkflow` name reference from generated workflows.
- Regenerated workflow JSON and documentation.

## Key findings
- The live n8n screenshot still showed old Normalize code with `searchCandidates`; the regenerated code uses `collectCandidates`.
- `Could not retrieve the column data!` is a Google Sheets schema/config issue caused by missing/unconfigured workbook/tab/header data. It cannot be fixed reliably in workflow JSON alone.
- The safe path is to validate Firecrawl -> Normalize -> Locality -> Dedupe first, then wire Sheets after the workbook exists.

## Validation
- JSON parse passed for all generated workflow files.
- Connection validation passed for all generated workflow files.
- Ready no-sheets workflow contains no Google Sheets nodes and no `errorWorkflow` setting.
- Local realistic data-flow test with 30 Firecrawl response items produced:
  - Normalize: 31 rows
  - Prague Locality Gate: 31 rows
  - Dedupe: 31 rows
  - Prepare Audit Queue Rows: 31 rows

## Next steps
- Import only `pipeline-c-praga-prospecting-ready-no-sheets.workflow.json` for the next test.
- Configure Firecrawl credential.
- Run the workflow and inspect `Prepare Audit Queue Rows`.
- Add Google Sheets only after the output rows are confirmed and the sheet has required tabs/header rows.
