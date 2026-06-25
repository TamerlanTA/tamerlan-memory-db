# Session 2026-06-25 — Memory Sync

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Full memory read and sync across both memory stores (TamerMemoryDB and local Claude project memory).
- Updated `/Users/tamerlan/.claude/projects/-Users-tamerlan-Documents-amigo-mvp/memory/project_status.md`
  to reflect complete current state: Phases 1–4 foundation, Phase 3.5 enrichment, portrait embedding, unified onboarding.
- Created `/Users/tamerlan/.claude/projects/-Users-tamerlan-Documents-amigo-mvp/memory/tech_decisions.md`
  with full stack, architecture decisions, queue names, security rules, and budget guardrails.
- Updated `MEMORY.md` index in local memory.

## Key findings
- TamerMemoryDB project files were already up-to-date as of 2026-06-24.
- Local Claude project memory (`project_status.md`) was 8 days old and missing Phases 3.5, 4 foundation, portrait embedding, and unified onboarding. Now current.
- No new commits since 2026-06-24 (`8145245` is the latest — unify candidate onboarding flow).
- One pending production action: manager `405182031` has an `awaiting_form` session — send `/candidate_new` to resume.
- Document version `84e1f6bf-fe95-40c8-b294-4e6e9588d3a8` is `pending_approval` (portrait visible, grounded).

## Blockers
- No first discovery connector yet (Phase 4 main deliverable).
- Employer catalog at 25/100.
- Unified onboarding not completed in a real live Telegram session.
- Consent text needs business/legal approval.
- WebP portrait uploads not supported — managers must re-upload as JPEG/PNG.
- No ATS adapters.

## Next steps
1. Complete one real `/candidate_new` acceptance pass in Telegram.
2. Build first read-only vacancy discovery connector (Accor or Kerzner).
3. Implement `vacancies.dedupe_key` upsert logic.
4. Expand employer catalog from 25 → 100.
