# ImportCar.kz MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Content
## Status as of 2026-05-16
- Frontend showroom MVP is implemented and deployed.
- Main flow works: home → listing → detail → importer comparison → request modal → success.
- Catalog is premium-only demo data: BMW, Mercedes-Benz, Porsche, Lexus, Audi.
- Pricing uses a versioned estimate engine with explanations, warnings, and importer-specific totals.
- Supabase integration exists for lead submission; public-test schema intentionally allows anonymous insert only on `leads`.
- Admin view is hidden by default and now read-only for statuses until authenticated admin access exists.
- Recent supervisor-audit issues are closed:
  - proof case pricing reads from typed mock data
  - importer details button expands real content
  - auction report button expands real sample content
  - lead form validates phone numbers
  - non-Korea country filters show a polished empty state
  - Playwright smoke testing is documented and runnable

## Verification completed
- `npm run lint` passes
- `npm run build` passes
- `npm run smoke:test` passes
- Production was redeployed after the latest fixes.
