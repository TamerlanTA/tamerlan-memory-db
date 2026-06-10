# Session 2026-06-09 — GA4 Pipeline Root Cause

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]
- [[decisions]]

## What was done
- Traced `landing_view` from React mount through `trackConversionEvent` and the production GA4 bootstrap.
- Verified the production bundle executes `initAnalytics()` and contains the correct Measurement ID.
- Verified GA4 property `399976814` data stream uses `G-W5B405NSQE`.
- Audited consent, CSP, guards, runtime errors, and existing analytics tests.

## Key findings
- `landing_view` is implemented and invoked by the mounted Home component.
- The GA4 bootstrap uses `function gtag(...args) { dataLayer.push(args) }`.
- Google's required snippet uses `function gtag(){ dataLayer.push(arguments); }`.
- The app therefore queues ordinary arrays instead of the Google tag command object. Both `config` and `event` commands are not processed; the extra object `{ event: ... }` push has no GTM container to consume it.
- Existing tests only assert that the plain dataLayer object was pushed; they never verify a processed GA4 command or network receipt.
- Umami's syntax error is separate and does not cause the GA4 failure.

## Blockers
- A small code correction and focused regression test are required before GA4 custom events can work.

## Next steps
- Replace the custom gtag wrapper with Google's canonical `arguments` queue contract.
- Remove or clearly separate the GTM-style object push unless a GTM container is introduced.
- Add a test for `config` and `event` command shape, then deploy and repeat Realtime/DebugView validation.
