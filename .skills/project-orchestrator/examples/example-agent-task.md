# Example: High-Quality Agent Task

```md
You are the implementation agent for a SaaS/web app project.

## Objective
Add saved calculator leads to the existing ImportCar.kz MVP without changing the public calculator flow.

## Project Context
- Goal: Let users save a car import calculation and submit contact details for follow-up.
- Current state: Calculator UI works locally; Supabase is used for persistence; admin view is feature-gated.
- Active stage: Stage 3 integration moving into Stage 5 QA.
- Relevant decisions: Keep the public flow lightweight. Admin view must stay disabled in production unless `VITE_ENABLE_ADMIN_VIEW=true`.
- Known risks: Supabase env vars may be missing locally; production migration must be run manually.

## Inspect First
- `src/lib/supabase.ts`
- `src/components/Calculator.tsx`
- `src/pages/Admin.tsx`
- `supabase/migrations/`
- `package.json`

## Required Changes
1. Add a Supabase migration for saved calculations/leads metadata if it does not already exist.
2. Add a save-request UI state to the calculator after a successful calculation.
3. Persist lead name, phone, selected vehicle data, estimate fields, and timestamp.
4. Keep admin view behind the existing feature flag.
5. Add basic error and success states.

## Constraints
- Do not redesign the landing page.
- Do not replace the existing calculator logic.
- Do not expose Supabase service-role keys.
- Preserve existing styles and component structure.

## Out Of Scope
- Phone OTP auth.
- Payment flow.
- CRM integration.
- Full admin analytics dashboard.

## Validation
Run:
- `pnpm lint`
- `pnpm build`

Manual check:
- Calculate a vehicle.
- Submit a save request.
- Confirm success/error state behaves correctly.
- Confirm admin route is unavailable when the feature flag is false.

## Acceptance Criteria
- User can submit a saved calculation request.
- Build and lint pass, or failures are explained with evidence.
- Changed files are listed.
- Untested areas are clearly stated.

## Expected Output
Return:
- Summary of changes
- Changed files
- Validation commands and results
- Risks or follow-up needed
```
