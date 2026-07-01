# Session 2026-06-30 — Phase 6 Batch 6 Email Apply

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[phase-6-execution-plan]]

## What was done
- Completed Phase 6 Batch 6 locally by choosing the narrow `email-apply-v1` path.
- Added `EmailApplyAdapter` to `@amigo/application-adapters`.
- Adapter supports only `mailto:` URLs, requires candidate email and approved CV `pdfStorageKey`, composes deterministic subject/body from approved context, and uses approved CV storage key as the attachment reference.
- Adapter defaults to dry-run mode and returns redacted `confirmation_text_hash` evidence without sending.
- Real send is possible only if runtime explicitly constructs the adapter with `dryRun: false` and an injected `sendEmail` function.
- Added tests for fixture certification, dry-run evidence redaction, missing approved document safety stop, and explicit sender-only send behavior.
- Updated `docs/application-adapter-certification.md` to record `email-apply-v1` as the Batch 6 narrow target.

## Key findings
- Batch 6 is local-only and does not enable production auto-submit.
- `email-apply-v1` can produce safe dry-run evidence today; production sending still needs source-level enablement, an email provider/sender, duplicate/rate-limit verification, and one controlled submission or approved dry-run evidence.
- Unsupported/non-email paths remain manual because worker runtime is not wired to execute `email-apply-v1`.

## Blockers
- Phase 6 migration `202606300001_phase6_applications.sql` is still not applied to production.
- `worker-applications` is not deployed/running in production.
- Email provider/sender integration and source-level enable flag are not implemented.
- No real application email has been sent.
- Manual Telegram acceptance for `/application_handoff` and `/manual_actions` is still pending.

## Validation
- `CI=true pnpm check`
- `CI=true pnpm test`
- `CI=true pnpm build`
- `CI=true pnpm format:check`

## Next steps
- Continue with Batch 7 reporting/operational visibility.
- Before any production auto-submit, wire source-level configuration and email sender explicitly, then run controlled evidence review.
