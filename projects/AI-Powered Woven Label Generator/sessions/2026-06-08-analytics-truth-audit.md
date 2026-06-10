# Session 2026-06-08 — Analytics Truth Audit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Audited GA4 initialization, every tracked event callsite, production Vercel env names, the live production bundle, and the live browser runtime.
- Distinguished implementation, deployment, active configuration, and DebugView verification.

## Key findings
- GA4 code and 19 event names are implemented and deployed.
- `VITE_GA4_MEASUREMENT_ID` is missing from Vercel Production.
- Production has no GA4 script, `gtag`, or `dataLayer`; events are not reaching GA4.
- No DebugView/Realtime validation evidence exists.
- Production Umami also fails because `/analytics.local/umami` returns non-JavaScript content.

## Blockers
- GA4 production configuration and redeployment.
- Live DebugView/Realtime validation of the core funnel.

## Next steps
- Follow [[next-steps#Analytics launch gate (2026-06-08)]].
