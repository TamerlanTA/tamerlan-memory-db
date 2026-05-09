# Session 2026-05-09 — AI Caller Start Outbound Call Workflow

## Related
- [[../00 - Overview]]
- [[../02 - Offers/AI Chatbot & Voice Agent]]
- [[../02 - Offers/Speed-to-Lead System]]
- [[../05 - CRM Structure/CRM Automation Plan]]
- [[../06 - Priorities/What to Do First]]
- [[../../../current-focus]]

## What was done
- Created inactive n8n workflow `FlowOps AI Caller — 01 Start Outbound Call`.
- n8n workflow ID: `24uEUBFodgUpYyrT`.
- Flow: Manual Trigger -> Google Sheets ready-lead read -> validation -> one-lead limit -> Vapi HTTP call -> normalize response -> success/failed Google Sheets update.
- Added sticky notes for setup placeholders, lead source assumptions, Vapi environment variables, and mock sample data.

## Key findings
- n8n instance API is reachable through MCP.
- Google Sheets is the primary lead source; workflow uses existing `Google Sheets account` credential reference and placeholder sheet IDs/names.
- Google Sheets update nodes use `appendOrUpdate` with `Email` as the matching column because this n8n Google Sheets version validates that pattern cleanly. Email should be unique, or the match key should be changed to a stable record/lead ID before production.
- Vapi placeholders are non-secret: `VAPI_API_KEY`, `VAPI_ASSISTANT_ID`, `VAPI_PHONE_NUMBER_ID`.
- Vapi HTTP node uses one-lead manual safety cap, retries, and `onError: continueRegularOutput` so failed call attempts can route to a failed-status update.

## Validation
- `n8n_validate_workflow` returned `valid: true`, `errorCount: 0`.
- Remaining warnings are mostly expected UI/metadata warnings: Code nodes can throw, placeholder resource locators lack cached display names, IF false branch is interpreted as an error-output warning, and Google Sheets nodes have no separate error workflow.
- `n8n_test_workflow` cannot execute this workflow externally because it uses a Manual Trigger; the MCP test endpoint only supports webhook/form/chat triggers. No real Vapi call was made.

## Blockers
- Real `GOOGLE_SHEET_ID`, sheet tab/range, and Vapi IDs/API key still need to be inserted.
- First live test requires a single row with `Status = Ready to call` and valid phone number.
- Production use should add a stable unique lead ID instead of relying on `Email` as the update match key.

## Next steps
- Replace `GOOGLE_SHEET_ID`, confirm sheet tab is `Leads` or update all three Google Sheets nodes.
- Set Vapi env vars or replace placeholders in the HTTP node/body.
- Run manually with exactly one test lead.
- Confirm Vapi response ID maps into `Call ID`; adjust `Normalize Vapi Response` if Vapi returns a different ID field.
- Build the follow-up webhook workflow for call result handling after this first call-start workflow is verified.
