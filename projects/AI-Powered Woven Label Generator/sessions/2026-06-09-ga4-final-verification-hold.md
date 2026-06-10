# Session 2026-06-09 — GA4 Final Verification Hold

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Opened GA4 Realtime for property `399976814`.
- Visited production with validation UTM parameters and retriggered the landing page.
- Opened GA4 DebugView and captured evidence.

## Key findings
- Realtime did not show `landing_view` after the production visit and repeat reload.
- The requested generation and preorder events could not be triggered because the Codex Chrome extension was not allowed to upload a local validation logo.
- DebugView showed zero debug devices and zero events.
- No requested custom event was verified as received by GA4.

## Blockers
- Chrome extension setting `Allow access to file URLs` must be enabled for production logo upload.
- The production custom-event delivery path needs investigation if `landing_view` remains absent after a clean retest.

## Next steps
- Enable local file access for the Codex Chrome extension.
- Repeat the full authenticated production flow while GA4 Realtime is open.
- Enable GA debug mode for DebugView proof or use Realtime as the acceptance surface.
