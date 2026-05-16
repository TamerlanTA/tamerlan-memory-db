# ImportCar.kz MVP — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

## Content
- Keep Vite + React + TypeScript for MVP speed and extensibility.
- Keep frontend car/importer inventory mocked while backend scope remains narrow.
- Use local UI state rather than adding routing/auth/payment before they are necessary.
- Make final KZT price the primary commercial signal; show source KRW price as supporting context.
- Treat the calculator as an estimate engine, not legal/tax advice.
- Version pricing rules and expose calculation reasoning instead of hiding uncertainty.
- Allow anonymous lead insert for public testing, but do not allow anonymous lead read/update.
- Keep admin status controls read-only until authenticated admin access exists.
- Use model-safe premium visual placeholders rather than risky mismatched remote car photos.
- Reposition the product visually from generic marketplace to cinematic private showroom without changing the core conversion flow.
- Treat all catalog entries as demo/sample listings, not live offers.
