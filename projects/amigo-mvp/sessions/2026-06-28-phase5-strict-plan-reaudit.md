# Session 2026-06-28 — Phase 5 Strict Plan Re-Audit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]
- [[phase-5-execution-plan]]

## What was done
- Rechecked Phase 5 implementation against the canonical [[phase-5-execution-plan]] after production deployment.
- Fixed pending-batch regeneration safety in `@amigo/matching`: existing `pending_approval`, `approved`, or `partially_approved` batches are returned as-is instead of deleting/recreating items and losing manager decisions.
- Fixed strict role-family filtering:
  - unknown non-target roles now fail with `role_mismatch` unless the vacancy title explicitly contains a target role;
  - broad F&B markers were removed from waiter-family matching because they made kitchen/host/stewarding roles approvable;
  - added regression tests for unknown non-target roles and known non-target families.
- Redeployed `bot-api` on Railway after the strict role-filter fix, final deployment `31084239-e787-4e1e-976d-50e25e5fa9a3`.
- Intentionally expired and regenerated the acceptance-test production batch `c7c7fcb1-58a3-4f0a-bc24-e66eb8906877` under the stricter filter.

## Key findings
- The initial production Phase 5 batch had passed broad F&B/role signals too loosely; `Public Area Attendant`, `Stewarding Supervisor`, `Sushi Commis Chef`, `Restaurant Hostess`, and `F&B Intern` are now rejected with `role_mismatch`.
- Final strict production batch for candidate `61ac04f1-b04c-4f35-a324-0a8c99182109` has:
  - 6 primary items;
  - 0 reserves;
  - shortage `eligible_vacancy_shortage:6/10`;
  - rank 1 `approved`;
  - rank 2 `rejected` with reason `phase5_reaudit_acceptance_test`;
  - remaining items `pending`.
- Re-running prepare/persist for the pending batch preserved the rank 1 and rank 2 decisions.
- Production smoke after final deploy passed: `/health` database OK, logs show bot commands registered and server listening, Telegram webhook pending updates 0.
- Full local validation passed: `CI=true pnpm check`, `CI=true pnpm test`, `CI=true pnpm build`, `CI=true pnpm format:check`.

## Blockers
- Manual Telegram UI click-through of `/candidate_batch` remains recommended before manager rollout.
- Product/business approval is needed for strict shortage behavior: the first accepted candidate now has 6/10 primary vacancies rather than forcing weak matches.

## Next steps
- Run `/candidate_batch` manually in Telegram as the manager and verify visible cards plus inline approve/reject callbacks.
- Resolve remaining pending items in batch `c7c7fcb1-58a3-4f0a-bc24-e66eb8906877` if using it as the pilot acceptance batch.
- Start Phase 6 only after agreeing how approved/partially approved batches create application jobs.
