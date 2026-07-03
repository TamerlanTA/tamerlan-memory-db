# Session 2026-07-01 — Generation Reliability Root-Cause Audit

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Audited the live production deployment, Vercel logs, production DB generation records, client runtime console, and relevant generation server code after Benjamin reported ongoing generation errors.
- Confirmed production is serving deployment `dpl_CWkgLwJ42GA34Mjq7cN4n5ir2shY` at `https://methode.griffesvivienne.com` with bundle `assets/index-CLadMgTo.js`.
- Queried production DB using pulled Vercel Production env without printing secrets.
- Reviewed official Gemini image-generation/image-understanding guidance for multimodal image limits and style-reference expectations.
- No application code was changed in this audit.

## Key findings
- Production DB since `2026-06-30 00:00:00` DB time shows 23 successful completed generations, 9 failed, and 1 stuck `started`; completed failure share is about 28.1%.
- Taffeta is the worst material in the fresh window: 7 successes and 7 failures.
- Live run `252` / request `lg_mr23zt3k_f3mlcf` produced an image, failed woven-textile validation, retried generation, then received Gemini `400 INVALID_ARGUMENT`; the server returned no image to the customer.
- Live run `253` followed the same validator-retry pattern but succeeded, so the system behavior is probabilistic and not demo-safe.
- Code root cause is in `server/nanoBananaService.ts`: validation retry exceptions escape instead of returning the previous generated `lastImageBase64`.
- Taffeta likely amplifies the issue because it can send 5 material/style references; retry then adds previous generated image and source logo, producing a heavier and more fragile multimodal request.
- Browser runtime is not production-clean: broken `/analytics.local/umami`, Clerk development-key warning, and missing `OAUTH_SERVER_URL` log noise.
- Sentry audit was blocked because `SENTRY_AUTH_TOKEN` is unavailable locally.

## Blockers
- Sentry cannot be queried without a token.
- GitHub push remains blocked by local HTTPS credential setup from earlier sessions, but this audit made no commits.

## Next steps
- First fix: salvage and return the prior generated image when a validator retry fails.
- Second fix: reduce retry/reference payload complexity, especially for Taffeta.
- Third fix: persist structured generation diagnostics and improve client error mapping.
- Then run a real production smoke matrix on mobile Safari and desktop, including Taffeta.
