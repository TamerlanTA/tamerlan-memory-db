# Session 2026-05-09 — AI Caller Receive Call Result Workflow

## Related
- [[../00 - Overview]]
- [[../02 - Offers/AI Chatbot & Voice Agent]]
- [[../02 - Offers/Speed-to-Lead System]]
- [[../05 - CRM Structure/CRM Automation Plan]]
- [[../06 - Priorities/What to Do First]]
- [[2026-05-09-ai-caller-start-outbound-call-workflow]]

## What was done
- Created inactive n8n workflow `FlowOps AI Caller — 02 Receive Call Result`.
- n8n workflow ID: `mON3HKIm1sjYar29`.
- Webhook path: `flowops-vapi-call-result`.
- Flow: Webhook POST -> normalize Vapi payload -> missing-call-ID response branch -> final-event filter -> rule-based classification -> Airtable lookup by `Call ID` -> Airtable update -> JSON webhook response.
- Added sticky notes explaining Vapi webhook URL placement, Airtable Call ID matching, optional fields, rule-based classification, and lead-not-found behavior.

## Key findings
- Workflow uses existing Airtable credential `Airtable Personal Access Token account` (`airtableTokenApi`, id `y5xm6HYmXkLSv042`).
- Airtable target remains `Flowops CRM`, base `apppMcDUQaQwijvIV`, table `Leads to call`.
- Airtable lookup formula matches `{Call ID}='<normalized call id>'`.
- Update writes only guaranteed fields to avoid schema failures: `Status`, `Call Summary`, `Next Action`.
- Optional values are prepared internally but not sent until Airtable fields are confirmed: `Transcript`, `Recording URL`, `Call Outcome`, `Last Call At`.
- 2026-05-10 incident: Vapi assistant `Alex` had default/broad `serverMessages` enabled (`conversation-update`, `speech-update`, `status-update`, `assistant.started`, etc.), causing many webhook hits per call and rapidly exhausting n8n Cloud executions. Updated Vapi assistant via API to `serverMessages: ["end-of-call-report"]`.

## Validation
- `n8n_validate_workflow` returned `valid: true`, `errorCount: 0`.
- Remaining warnings are static/expected: Code nodes can throw, IF false branches are interpreted as error outputs, dynamic Airtable URL expressions lack visible literal protocol, and chain length suggestion.
- Local mock tests passed for:
  - interested/send info -> `Send info`
  - no answer -> `No answer`
  - not interested -> `Not interested`
  - missing call ID -> `{ ok: false, reason: "missing_call_id" }`
- 2026-05-10: execution #3568 showed failure at `Webhook — Vapi Call Result` before workflow logic ran: `Execution limit reached`. This confirms the failure was n8n Cloud quota/pre-execution, not Airtable or code logic.

## Blockers
- Workflow is inactive; production webhook URL becomes useful after activation.
- Public n8n base URL was not exposed via MCP/env, so use the production webhook URL shown inside n8n.
- Optional Airtable fields are not written yet by design; add them only after confirming the schema.
- Do not reactivate until n8n Cloud execution quota resets or plan is upgraded; otherwise even the reduced single final webhook can still be rejected at the trigger.

## Next steps
- After n8n execution quota resets, activate workflow when ready.
- Paste the Production webhook URL ending in `/webhook/flowops-vapi-call-result` into Vapi Assistant Server URL.
- Run one real call result test from Vapi and confirm Airtable record matching by `Call ID`.
- After first real payload, inspect whether Vapi ID path matches the current normalization; adjust if Vapi sends a different final call ID.
