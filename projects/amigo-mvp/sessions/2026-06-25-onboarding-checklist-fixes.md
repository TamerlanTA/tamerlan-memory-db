# Session 2026-06-25 — Manual Acceptance Checklist Fixes

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
Full code review against the 16-item manual acceptance checklist for unified `/candidate_new` onboarding.

**Items verified correct (no fix needed):** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16

**Three issues found and fixed:**

### Fix 1 — Item 13: `/candidate_view` enrichment records (profile.ts)
**Before:** showed only counts ("Опыт работы для CV: 2")
**After:** shows actual records per section:
```
Опыт работы (2):
  • Waiter @ Hilton Resort (2022 — 2024)
  • Runner @ Accor Hotels (2024 — present)
Образование (1):
  • Tourism Academy — Hospitality (2021)
Дополнения (1):
  • [course] Food Safety
```
Queries `candidateWorkExperiences`, `candidateEducation`, `candidateCvExtras` ordered by `sortOrder`.

### Fix 2 — Dead code: `review:finish` redundant status update (cv-enrichment.ts)
Removed `db.update(candidates).set({ status: "intake" })` after `review:finish`.
The candidate is already `intake` at creation; this was a no-op.

### Fix 3 — UX: silent response for text during inline-keyboard steps (handler.ts)
Added `cv_photo_upload` case: "Отправьте портретное фото..."
Added default for `onboardingMode`: "Используйте кнопки выше или /candidate_new..."

## Validation
- `pnpm check` passed (TypeScript)
- `pnpm test` passed: **72 tests** (3 new profile tests added)
- `pnpm build` passed
- `pnpm format:check` passed
- Commit `6e77062` pushed to `main`
- Railway `bot-api` deployed; `/health` OK

## Blockers
None from this session. Remaining pre-pilot blockers:
- Full live Telegram acceptance pass still needed
- First vacancy discovery connector still needed
- Consent text needs legal approval

## Next steps
1. Complete the live `/candidate_new` Telegram acceptance pass using the full checklist
2. Build first read-only vacancy discovery connector (Phase 4 main deliverable)
