# Session 2026-06-15 — Project Kickoff

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]
- [[roadmap]]

## What was done
- Reviewed the complete AMIGO project memory and confirmed that planning is complete but implementation has not started.
- Confirmed a two-person working mode: Tamerlan owns business inputs and approvals; Codex owns technical execution, validation, and memory synchronization.
- Identified the original Foundation milestone as overdue and retained the 2026-07-05 launch target pending an explicit go/no-go review.
- Created and pushed the private `TamerlanTA/amigo-mvp` repository at commit `15f7896`.
- Implemented the pnpm/TypeScript monorepo, Fastify/grammY bot API, manager allowlist, environment validation, redacting logs, Drizzle foundation schema, PGMQ worker, tests, CI, and Docker builds.
- Provisioned Supabase `ibebnmlwjjkibfwdnffr` in Frankfurt and applied the Foundation migration.
- Provisioned Railway project `amigo-mvp` and deployed `bot-api` and `worker-foundation`.
- Registered the production Telegram webhook for `@amigomvpbot`.
- Created a draft Russian candidate consent and rendered/visually verified the English hospitality CV DOCX template.

## Key findings
- The first executable work is repository and environment foundation, not further product planning.
- The supplied Telegram and OpenAI credentials were valid and the required service sessions were already authenticated.
- Supabase direct database DNS is IPv6-only in this environment; the production connection uses the project-specific Supavisor session pooler.
- The installed PGMQ version uses `read(queue_name, vt, qty, conditional)`.
- Queue deletion and audit insertion must commit in one transaction to prevent ambiguous processing outcomes.
- The remaining schedule is compressed and requires strict MVP scope.

## Blockers
- CV template and consent text require team/business approval.
- A business privacy contact is still unspecified.
- No application adapter is certified.

## Next steps
- Implement the full manager-led candidate intake and expanded candidate schema.
- Test the first controlled candidate in Telegram.
- Assemble and validate the first 100-employer catalog.
