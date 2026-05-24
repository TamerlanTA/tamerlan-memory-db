# Example: Review Report

```md
## Review Report

Verdict: Fix required

Findings:
- [High] Workflow send step: Gmail can still run when `approvalStatus` is missing. This violates the requirement that outbound email only sends after explicit approval.
- [Medium] `src/lib/leads.ts`: phone is stored without normalization, which may cause duplicate leads for the same user.
- [Low] `README.md`: new `AIRTABLE_BASE_ID` env var is not documented.

Validation evidence:
- `pnpm build` passed.
- No end-to-end Telegram approval test was provided.
- Diff reviewed for changed workflow JSON and lead utility files.

Scope check:
- Changed files are mostly in scope.
- One unrelated formatting change in `src/App.tsx` should be reverted unless required.

Residual risks:
- Gmail credentials were not available, so actual send behavior remains unverified.

Required fixer prompt:
Fix the approval gate so Gmail only runs when `approvalStatus === "approved"`, normalize phone before dedupe, document `AIRTABLE_BASE_ID`, and revert unrelated formatting in `src/App.tsx`. Run build and report changed files.

Next action:
Send the fixer prompt and require one end-to-end approval test before accepting.
```
