# Session 2026-04-30 — Windows Server n8n Install Guidance

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Prepared operational guidance for installing n8n on a Windows Server accessed over RDP.
- Recommended npm installation over n8n Desktop App because the official desktop app repository is archived/read-only.
- Clarified that local-only n8n UI access works at `http://localhost:5678`, but Telegram webhook workflows need a public HTTPS URL or tunnel to receive live Telegram updates.

## Key findings
- Current official npm docs require Node.js in the supported range `20.19` through `24.x`.
- For Windows Server/n8n v2 behavior, set `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=false`.
- For local-only binding, configure `N8N_LISTEN_ADDRESS=127.0.0.1`, `N8N_HOST=localhost`, and `N8N_PORT=5678`.

## Blockers
- Actual server access and installed Node.js/npm versions were not verified in this session.

## Next steps
- Install Node.js and n8n on the Windows Server.
- Configure credentials and variables in n8n after first login.
- If Telegram bot must work live, add a public HTTPS endpoint/tunnel or reverse proxy.
