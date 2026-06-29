# AMIGO MVP — Phase 5 Execution Plan

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[roadmap]]
- [[technical-architecture]]
- [[data-model]]
- [[integrations]]

## Status
- Phase: Phase 5 — Matching and approval
- Plan status: Canonical execution plan
- Created: 2026-06-28
- Rule: Future Phase 5 implementation must follow this plan in order unless Tamerlan explicitly changes the plan or a verified blocker requires a documented deviation.

## Goal
Build deterministic daily vacancy batches for approved candidates.

Each eligible candidate should receive a manager-reviewed daily batch of 5–10 suitable vacancies plus reserves, with hard-filter safety, weighted scoring, cross-source duplicate suppression, explanation records, and Telegram approve/reject actions.

## Current Verified Context
- Phase 1, Phase 2, Phase 3, Phase 3.5, Phase 4B, Phase 4C.1, and Phase 4C.2 are accepted in memory.
- Vacancy discovery has active SuccessFactors coverage for the Kerzner family.
- Phase 4C.2 duplicate detection is read-only and accepted.
- Production duplicate report found 10 active cross-source duplicate groups / 20 rows, all canonical `apply_url` overlaps.
- Source-scoped `vacancies.dedupe_key` must remain unchanged for Phase 5.
- Phase 5 must consume canonical duplicate groups as a suppression guard before manager-facing batches.
- Scoring, batching, and application decisions must remain deterministic and AI-free.

## Non-Negotiable Execution Rules
1. Do not implement Phase 5 out of order. Complete and validate each batch before starting the next batch.
2. Do not submit applications in Phase 5. Application submission belongs to Phase 6.
3. Do not use AI to decide matching, scoring, eligibility, or approval.
4. Do not rewrite, delete, or merge existing vacancy rows to solve cross-source duplicates.
5. Do not show hard-filter-failed vacancies as approvable.
6. Do not show multiple vacancies from the same canonical duplicate group in one manager-facing batch.
7. Do not include stale/inactive vacancies, prior applications, or employer-blacklisted vacancies in approvable batches.
8. Do not change unrelated candidate intake, document generation, or vacancy discovery behavior unless required by a Phase 5 acceptance criterion.
9. Do not add broad new connector coverage during Phase 5 except small fixtures needed for tests.
10. Any deviation from this plan must be recorded in [[decisions]] or a session note before continuing.

## Phase 5 Scope
In scope:
- role taxonomy and synonym dictionaries;
- candidate eligibility check for matching;
- hard filters;
- weighted score;
- explanation records;
- canonical duplicate suppression;
- daily batch creation with primary and reserve items;
- Telegram manager review and approve/reject actions;
- tests, validation, deployment notes, and memory sync.

Out of scope:
- actual application submission;
- browser/ATS application adapters;
- email apply;
- candidate-facing dashboard;
- broad employer catalog expansion beyond safety-critical fixtures;
- changing Phase 4 vacancy identity storage;
- LLM-generated vacancy reasoning or cover letters.

## Data Model Target
Add or complete the Phase 5 persistence layer with minimal migrations:

- `vacancy_scores`
  - candidate/document/profile identifiers;
  - vacancy identifier;
  - hard filter pass/fail;
  - score 0–100;
  - bucket: `primary`, `reserve`, `rejected`;
  - structured explanation JSON;
  - deterministic input hash / scoring version;
  - created timestamp.

- `daily_batches`
  - candidate;
  - batch date;
  - active document version;
  - status: `preparing`, `pending_approval`, `approved`, `partially_approved`, `rejected`, `expired`;
  - target size;
  - approved/rejected by manager;
  - timestamps.

- `daily_batch_items`
  - batch;
  - vacancy;
  - rank;
  - score reference;
  - duplicate group key used for suppression;
  - decision: `pending`, `approved`, `rejected`;
  - rejection reason;
  - timestamps.

If the existing schema differs, preserve existing naming/patterns and document the mapping.

## Matching Inputs
Candidate can enter Phase 5 only when all are true:
- candidate is not closed;
- candidate has assigned manager;
- required profile fields are complete;
- consent exists;
- exactly one active approved CV/document version exists;
- target countries and target roles exist;
- language level exists.

Vacancy can enter scoring only when all are true:
- vacancy is active/fresh;
- apply URL exists;
- employer/source is active;
- vacancy has normalized title and location data sufficient for filtering;
- vacancy is not already previously applied for that candidate;
- vacancy is not blocked by candidate/employer blacklist.

## Hard Filters
Implement hard filters before scoring:
1. Country / excluded region.
2. Role family / target role compatibility.
3. Relocation and sponsorship compatibility where data exists.
4. Language requirements.
5. Minimum experience / seniority where data exists.
6. Contract type / schedule compatibility where data exists.
7. Candidate or employer blacklist.
8. Vacancy age and freshness.
9. Previous application / existing approved batch item for the same candidate and vacancy.
10. Canonical duplicate suppression for manager-facing batches.

Hard-filter output must include machine-readable reasons.

## Weighted Scoring
Use the existing Phase 5 scoring model from [[integrations]]:

| Component | Points |
|---|---:|
| Role/title match | 30 |
| Experience/seniority | 20 |
| Country/relocation | 15 |
| Language | 10 |
| Hospitality segment | 10 |
| Schedule/contract | 5 |
| Salary | 5 |
| Freshness | 5 |

Buckets:
- 70–100: primary batch candidate;
- 55–69: reserve;
- below 55: rejected.

Scoring must be deterministic. Identical candidate/vacancy inputs and scoring version must produce identical hard-filter output, score, bucket, rank, and explanation.

## Explanation Contract
Every scored vacancy needs an explanation record with:
- hard filter result;
- hard filter fail reasons, if any;
- score breakdown by component;
- final score;
- bucket;
- rank inputs;
- duplicate group key, if any;
- prior-application or blacklist exclusion signal, if any;
- scoring version.

Telegram can show a concise human summary, but the DB should keep structured details.

## Execution Batches

### Batch 0: Baseline Audit and Phase 5 Lock
Objective:
- Confirm current repo schema, commands, package structure, and Phase 4 duplicate helper API.

Actions:
- Inspect `packages/db/src/schema.ts`, migrations, `packages/vacancy-discovery/src/duplicates.ts`, bot command structure, and queue contracts.
- Confirm whether Phase 5 tables already exist.
- Confirm validation commands from `package.json`.

Validation:
- No code changes required unless audit discovers a stale memory mismatch.

Exit criteria:
- Implementation files and gaps are known.
- Any plan mismatch is documented before coding.

### Batch 1: Schema and Contracts
Objective:
- Add Phase 5 database tables/enums and typed contracts.

Actions:
- Add migrations for `vacancy_scores`, `daily_batches`, and `daily_batch_items`.
- Add Drizzle schema/types following existing repo style.
- Add queue contract for `vacancy.match` / `batch.prepare` only if missing.
- Add indexes/unique constraints for idempotency:
  - one batch per candidate/date/scoring version unless explicitly regenerated;
  - one item per batch/vacancy;
  - no duplicate application/batch item for same candidate/vacancy where applicable.

Validation:
- Typecheck.
- Migration generation/application path verified locally where possible.
- Unit tests for schema-adjacent helpers if added.

Exit criteria:
- Phase 5 persistence is ready and backwards-compatible.

### Batch 2: Taxonomy and Hard Filters
Objective:
- Implement deterministic eligibility and hard-filter engine.

Actions:
- Add role taxonomy and synonym dictionaries.
- Implement candidate eligibility check.
- Implement vacancy eligibility check.
- Implement hard filters with reason codes.
- Reuse existing candidate profile/completeness logic where possible.
- Add tests for each hard filter and edge cases.

Validation:
- Unit tests cover pass/fail reasons.
- Tests prove hard-filter failures cannot enter approvable output.

Exit criteria:
- Filtering is deterministic, tested, and independent from Telegram UI.

### Batch 3: Scoring and Explanation Engine
Objective:
- Implement weighted scoring with structured explanation records.

Actions:
- Implement score components exactly from this plan.
- Add scoring version constant.
- Persist score records.
- Add deterministic ranking tie-breakers:
  1. higher score;
  2. fresher vacancy;
  3. employer name;
  4. normalized title;
  5. vacancy id.
- Add tests for identical inputs producing identical scores/rank.

Validation:
- Unit tests for score breakdown, thresholds, tie-breakers, and explanations.

Exit criteria:
- Scoring output is reproducible and explainable.

### Batch 4: Cross-Source Duplicate Suppression
Objective:
- Ensure manager-facing batches show only one vacancy per canonical duplicate group.

Actions:
- Reuse Phase 4C.2 canonical duplicate logic.
- Suppress duplicates before final batch presentation.
- Keep source-scoped `dedupe_key` unchanged.
- Prefer the highest-scoring vacancy in a duplicate group; use deterministic tie-breakers if scores match.
- Record suppressed duplicate information in explanation/metadata where useful.

Validation:
- Tests cover broad Kerzner + property-level duplicate groups.
- Tests prove duplicate suppression does not delete or mutate vacancy rows.

Exit criteria:
- No manager-facing batch can contain two active rows from the same canonical duplicate group.

### Batch 5: Daily Batch Generation
Objective:
- Create primary and reserve daily batches per eligible candidate.

Actions:
- Implement batch preparation service/worker or CLI following existing worker patterns.
- Select 5–10 primary vacancies when available.
- Attach reserve vacancies from 55–69 range or overflow primary candidates.
- Persist batch and items idempotently.
- Classify eligible vacancy shortage explicitly; do not lower hard filters to hit volume.
- Add regeneration behavior only if needed and clearly controlled.

Validation:
- Tests for target size, reserves, shortage, idempotency, no prior applications, no blacklist, no duplicate groups.

Exit criteria:
- A candidate can receive a pending approval batch without application submission.

### Batch 6: Telegram Manager Review
Objective:
- Add Telegram review and approval workflow for daily batches.

Actions:
- Implement or complete `/candidate_batch`.
- Show candidate selection/search using existing manager ownership rules.
- Show batch summary with primary and reserves.
- Provide approve/reject actions for item and whole batch.
- Require rejection reason for rejected items when practical.
- Enforce manager ownership and current batch status on every callback.
- Prevent stale inline buttons from mutating old batches.

Validation:
- Bot unit tests/callback tests for ownership, stale callback, approve, reject, hard-filter safety.
- Manual local/production acceptance checklist prepared.

Exit criteria:
- Manager can approve/reject pending batch items from Telegram.

### Batch 7: Phase 6 Handoff Boundary
Objective:
- Stop Phase 5 at the correct boundary while preparing clean handoff to applications.

Actions:
- After manager approval, create only the next intended queue/event boundary if already defined; do not submit applications.
- If Phase 6 queue creation is not safe yet, mark approved batch ready for Phase 6 instead of enqueueing application jobs.
- Document exact Phase 6 handoff state.

Validation:
- Tests prove approval does not submit applications.

Exit criteria:
- Phase 5 produces approved batches and a clear Phase 6 input.

### Batch 8: QA, Production Readiness, and Memory Sync
Objective:
- Validate Phase 5 end to end before acceptance.

Actions:
- Run full local validation:
  - `CI=true pnpm check`
  - `CI=true pnpm test`
  - `CI=true pnpm build`
  - `CI=true pnpm format:check`
- Run focused matching/batch tests.
- Verify no secrets are logged.
- Verify migrations are production-safe.
- Prepare manual Telegram acceptance checklist.
- Update [[current-state]], [[next-steps]], [[risks]], and a session note.

Exit criteria:
- Build/tests pass or failures are documented with owner and next step.
- Changed files are listed.
- Phase 5 acceptance evidence is recorded.

## Acceptance Criteria
Phase 5 is complete only when:
- eligible candidates with approved CVs can get pending daily batches;
- identical inputs produce identical scores, ranks, and explanations;
- hard-filter failures cannot be approved accidentally;
- stale/inactive vacancies are excluded;
- prior applications and employer blacklists are excluded;
- manager-facing batches suppress canonical cross-source vacancy duplicates;
- daily batches include 5–10 primary vacancies plus reserves when enough eligible vacancies exist;
- shortage is reported honestly when not enough eligible vacancies exist;
- Telegram approve/reject actions work with ownership and stale-callback protection;
- approval does not submit applications;
- full validation commands pass or documented failures are accepted explicitly;
- memory is updated with actual completion evidence.

## Risk Register
| Risk | Evidence | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|
| Duplicate vacancies reach managers | Phase 4C.2 found 10 active duplicate groups / 20 rows | Manager confusion, duplicate applications later | Consume canonical duplicate groups before batch presentation | Codex | Open |
| Hard filters are under-specified for sparse vacancy data | Current sources may lack salary/schedule/experience fields | Good roles may be rejected or unsafe roles may pass | Treat unknown optional fields conservatively; never bypass required filters | Codex + Tamerlan | Open |
| No approved/enriched pilot candidates available | Manual unified onboarding acceptance remains pending | Cannot fully validate real candidate matching | Use fixtures first, then run manual pilot candidate acceptance | Tamerlan + Codex | Open |
| Telegram batch UI becomes too dense | 5–10 vacancies plus reserves can exceed comfortable chat length | Manager friction | Paginate, concise summaries, item detail callbacks | Codex | Open |
| Phase 5 drifts into Phase 6 applications | Application adapters are not certified | Unsafe submissions | Stop at approved batch / Phase 6 handoff boundary | Codex | Open |

## Manual Acceptance Checklist
- Run duplicate report before batch generation.
- Pick one approved candidate with target roles/countries.
- Generate a pending batch.
- Confirm batch has no duplicate canonical `apply_url` groups.
- Confirm all primary items have score >= 70 unless shortage behavior is explicitly shown.
- Confirm reserves are visible or stored.
- Approve one item.
- Reject one item with reason.
- Try a stale callback and confirm it is blocked.
- Try a manager without ownership and confirm it is blocked.
- Confirm no application submission happened.

## Next Action
Start Batch 0: audit current schema, duplicate helper API, bot command patterns, queue contracts, and validation commands. Do not begin schema implementation until Batch 0 findings are known.
