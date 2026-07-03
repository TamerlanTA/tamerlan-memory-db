# Session 2026-07-01 — Mobile Upload Storage Hotfix

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Investigated the user-provided mobile screen recording where upload preview appeared successfully, then the app immediately showed the generic fallback error after pressing continue.
- Implemented `cac32db` (`Prevent mobile logo upload storage crashes`) to harden the client upload/storage path.
- Deployed production directly through Vercel CLI as `dpl_CWkgLwJ42GA34Mjq7cN4n5ir2shY`, READY and aliased to `https://methode.griffesvivienne.com`.

## Key findings
- The failure is not the Gemini generation error UI. It happens before visible generation during the upload-to-prepare transition.
- Most likely root cause: large iPhone raster uploads were stored as full DataURLs in `localStorage` (`logoPreview` and `gv_original_logo_data_url`), which can trigger Safari `QuotaExceededError` and the React fallback screen.
- The previous mobile payload hotfix reduced the request sent to generation, but did not stop the large upload from being persisted locally before generation.

## Changes
- `Home.tsx` now rasterizes all supported uploads into a capped PNG preview before storing/continuing.
- Oversized original uploads are not read into generator state or persisted; generation proceeds with the lightweight preview.
- `useGeneratorStore.tsx` now guards localStorage reads/writes/removes so storage quota failures no longer crash the app.
- `configFromLegacyStorage()` now catches localStorage hydration failures.
- Added tests for heavy-original skipping and storage quota rejection.

## Verification
- `node_modules/.bin/vitest run` PASS: 41 files, 245 tests.
- `node_modules/.bin/tsc --noEmit` PASS.
- Vite production build PASS.
- Server esbuild bundles PASS.
- Live domain returns HTTP 200 and serves `assets/index-CLadMgTo.js`, which contains the new storage guard strings.

## Blockers
- GitHub push is still blocked by local HTTPS credentials; branch is ahead of origin by 4 commits.
- Real iPhone Safari smoke test is still needed with the same logo/photo from the screen recording.

## Next steps
- Ask user/client to hard refresh or reopen Safari tab, then retry the same upload on iPhone.
- Run one full mobile generation and one desktop control generation on production.
- Push `d25e7b1`, `69751ed`, `883ca3c`, and `cac32db` once GitHub credentials are available.
