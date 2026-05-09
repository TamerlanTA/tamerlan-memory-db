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
- Initial flow used Google Sheets, then was updated per user request to use Airtable.
- Current flow: Manual Trigger -> Airtable ready-lead read -> validation -> one-lead limit -> Vapi HTTP call -> normalize response -> success/failed Airtable update.
- Added/updated sticky notes for setup state, Airtable source, Vapi values, and mock sample data.

## Key findings
- n8n instance API is reachable through MCP.
- Airtable is the lead source: base `apppMcDUQaQwijvIV` (`Flowops CRM`), table name `Leads to call`.
- Workflow uses existing n8n credential `Airtable Personal Access Token account` (`airtableTokenApi`, id `y5xm6HYmXkLSv042`) for Airtable reads/updates.
- Airtable source query filters `{Status}='Ready to call'`, then workflow limits output to 1 lead for manual safety.
- Airtable updates use the returned `record.id` (`airtable_record_id`), not Email matching.
- User provided Vapi assistant ID, phone number ID, and API key in an RTFD note; values were inserted into the workflow. Do not expose the full API key in reports.
- Vapi HTTP node uses one-lead manual safety cap, retries, and `onError: continueRegularOutput` so failed call attempts can route to a failed-status update.

## Validation
- `n8n_validate_workflow` returned `valid: true`, `errorCount: 0`, `warningCount: 6` after Airtable conversion.
- Remaining warnings are expected/static: Code nodes can throw, and the IF false branch is interpreted as an error-output warning.
- Local mock test confirmed Ready-to-call filtering, Vapi request body mapping, and Airtable update payload mapping without making a real call.
- `n8n_test_workflow` cannot execute this workflow externally because it uses a Manual Trigger; the MCP test endpoint only supports webhook/form/chat triggers. No real Vapi call was made.

## Blockers
- First live test requires exactly one intended Airtable record with `Status = Ready to call` and a valid E.164-style phone number.
- Workflow is intentionally inactive; run manually first to avoid accidental outbound calling.
- Airtable field names must match the workflow expectations exactly: `Company`, `Contact Name`, `Phone`, `Email`, `Website`, `Industry`, `Business Summary`, `Website Observations`, `Pain Points`, `Recommended Automation`, `Offer Angle`, `Status`, `Call ID`, `Call Summary`, `Next Action`.

## Next steps
- In Airtable, set only one safe test lead to `Status = Ready to call`.
- Run workflow manually in n8n and verify Airtable updates the same record to `Call started` with Vapi call ID.
- Confirm Vapi response ID maps into `Call ID`; adjust `Normalize Vapi Response` if Vapi returns a different ID field.
- Build the follow-up webhook workflow for call result handling after this first call-start workflow is verified.
