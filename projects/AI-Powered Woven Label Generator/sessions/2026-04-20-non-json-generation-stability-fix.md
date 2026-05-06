# Session 2026-04-20 — Non-JSON Generation Stability Fix

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done
- Audited the client-reported `Unexpected token 'R', "Request En..." is not valid JSON` failure path.
- Identified the affected request as `Result.tsx` -> `trpc.label.generate` -> `/api/trpc/label.generate`.
- Fixed the generation request payload so it no longer always sends both the tinted generation PNG and the original upload data URL when the combined body would exceed the safe client budget.
- Capped the client-side tinted logo canvas output to `1280px` on the largest side to prevent huge mobile/source logos from producing oversized PNG data URLs.
- Added a tRPC fetch wrapper that normalizes unexpected non-JSON API responses into JSON tRPC error envelopes instead of allowing raw JSON parse crashes.
- Added a server-side schema guard for oversized `label.generate` logo payload strings.

## Key findings
- The client error prefix `Request En...` matches an upstream/body-parser style plain-text `Request Entity Too Large` response.
- The frontend tRPC transport previously assumed `/api/trpc` responses were JSON, so a plain-text gateway/body-size response surfaced as a raw JSON parser error toast and generic error state.
- The risky payload shape came from sending `logoDataUrl` plus `originalLogoDataUrl` in one `label.generate` request; large uploads made this unstable on deployment limits.

## Blockers
- No production logs were available in-session, so the fix is grounded in code path audit plus simulated non-JSON transport tests.
- Production smoke test with a large/high-resolution logo is still needed after deploy.

## Next steps
- Deploy and test one large mobile/high-resolution PNG/JPG logo through Result generation.
- In browser devtools, confirm `/api/trpc/label.generate` no longer returns plain text `Request Entity Too Large` and no `Unexpected token 'R'` toast appears.
- Continue keeping moodboard/generation reference changes out of this stability fix unless a separate generation-quality task requires them.
