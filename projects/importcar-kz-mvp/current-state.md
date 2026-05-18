# ImportCar.kz MVP — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## Content
## Status as of 2026-05-16 (updated — premium design overhaul complete)
- Frontend showroom MVP is implemented and deployed.
- **Real Encar data**: 15 real listings from car.encar.com (BMW, Mercedes, Audi, Porsche, Lexus, Genesis, Land Rover, Cadillac). Real photos from Encar CDN at `/cars/encar-*.jpg`. Full Russian localization across all components.
- **Design overhaul applied**: Playfair Display + Inter typography, gold accent (#C9A84C) replacing all green (#16c784/#2fb68a), warm dark hero gradients, warm cream light backgrounds (#F5F2EC). Site no longer looks AI-generic — editorial luxury automotive aesthetic confirmed in browser.
- Main flow works: home → listing → detail → importer comparison → request modal → success.
- Catalog is premium-only demo data and now includes local car image assets under `public/cars/` / deployed `dist/cars/`.
- Pricing uses a versioned estimate engine with explanations, warnings, and importer-specific totals.
- Supabase integration exists for lead submission; public-test schema intentionally allows anonymous insert only on `leads`.
- Admin view is hidden by default and status updates are read-only until authenticated admin access exists.
- Supervisor-audit fixes are present in code:
  - proof case purchase price uses `purchasePriceKrw`
  - importer details button expands inline support details
  - auction sheet button expands a sample report
  - lead form validates phone numbers
  - empty state exists for unavailable country filters
- Playwright is in `devDependencies`; `smoke:test` is wired and documented.
- Latest production deployment refreshed after additional external changes on 2026-05-16.

## Verification completed
- `npm run lint` passes
- `npm run build` passes
- TypeScript — 0 errors
