# Telegram Codex Bridge

## Related
- [[agent-memory]]

## Current status
- 2026-04-29: Scaffolded `/Users/tamerlan/telegram-codex-bridge` from `MASTER_CODEX_BRIDGE_PROMPT.md` as a Node.js ESM Telegram ↔ Codex bridge.
- Implemented Telegram polling, one-chat authorization/claiming, command routing, file normalization/downloads, prompt wrapping, `codex exec` runner via `spawn`, `/run` allowlist, logging, state, README, PM2 ecosystem file, `.gitignore`, `local.env`, and `project.json`.
- `project.json` currently points `repoPath` to `/Users/tamerlan/telegram-codex-bridge`.

## Validation
- `npm install` completed and created `package-lock.json`.
- `npm run check` passes syntax checks for all source modules.
- `npm run start` fails correctly until `TELEGRAM_BOT_TOKEN` is set in `local.env`.

## Decisions
- Keep Codex global configuration untouched; bridge only calls existing `codex exec`.
- Use `node-telegram-bot-api` as required by the master prompt.
- Use npm `overrides` to reduce transitive dependency risk where possible without replacing the required Telegram package.

## Risks / blockers
- `npm audit --omit=dev` still reports 6 moderate vulnerabilities from the required `node-telegram-bot-api` → `@cypress/request/request` chain. Critical `form-data`/`qs` issues were reduced via overrides, but `request` itself remains deprecated/vulnerable.
- Real Telegram runtime cannot be verified until `TELEGRAM_BOT_TOKEN` is filled.
- Real Codex Telegram execution cannot be verified until a bot token and allowed chat are configured.

## Next steps
- Fill `TELEGRAM_BOT_TOKEN` in `/Users/tamerlan/telegram-codex-bridge/local.env`.
- Optionally set `TELEGRAM_ALLOWED_CHAT_ID`; otherwise first `/start` claims the bridge.
- Run `npm run start`, send `/start`, `/status`, then `/ask Analyze this repository and explain what it does.`
- If audit risk is unacceptable, replace `node-telegram-bot-api` with a maintained Telegram SDK, but that would deviate from the current master prompt.
