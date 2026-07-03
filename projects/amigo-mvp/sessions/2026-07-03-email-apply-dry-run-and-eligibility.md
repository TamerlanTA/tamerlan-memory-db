# Session 2026-07-03 — Email Apply Dry Run And Eligibility

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]
- [[risks]]
- [[phase-6-execution-plan]]

## What was done
- Implemented `email-apply-v1` dry-run execution mode in `worker-applications`.
- Added worker persistence for adapter dry-run evidence using `application_evidence.confirmation_text_hash`.
- Kept dry-run applications actionable by routing them to manual action instead of marking them `applied`.
- Added `/adapter_eligibility` in Telegram and matching report logic for approved batch items.
- Deployed `bot-api` and `worker-applications` to Railway.

## Key findings
- Production still has 0 active `mailto:` vacancies and all 85 sources have `application_adapter = null`, so the new email path is deployed but not yet naturally exercised by current sources.
- Telegram `getMyCommands` includes `/adapter_eligibility`.
- `worker-applications` started fresh at `2026-07-03T10:23:14Z`.
- Production queues are empty: `application_submit = 0`, `application_manual_action = 0`, `report_daily = 0`.
- Production applications remain manual-only: `manual-deep-link-v1` has 10 applied and 11 skipped; evidence has 10 `manual_confirmation` rows.

## Validation
- `pnpm --filter @amigo/application-adapters test && pnpm --filter @amigo/application-adapters check`
- `pnpm --filter @amigo/matching test && pnpm --filter @amigo/matching check`
- `pnpm --filter @amigo/worker-applications test && pnpm --filter @amigo/worker-applications check`
- `pnpm --filter @amigo/bot-api test && pnpm --filter @amigo/bot-api check`
- Affected package builds passed.
- `pnpm format:check`
- Production `/health` OK after deploy.

## Blockers
- No production email-capable source is configured yet.
- Live email sending remains intentionally disabled until source allowlist, sender config, rate limits, duplicate prevention review, and controlled evidence review are complete.
- Temporary Railway token shared in chat still needs rotation.

## Next steps
- Use `/adapter_eligibility` after the next approved batch.
- Add or discover real email-apply hospitality sources, then mark only those sources as `email-apply-v1`.
- Run one dry-run handoff for an email-capable source and verify `confirmation_text_hash` evidence plus manual action.
- After dry-run acceptance, wire live sender behind explicit env flag/source allowlist.
