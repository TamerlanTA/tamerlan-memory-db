# Telegram Codex Bridge

## Related
- [[agent-memory]]

## Current status
- 2026-04-29: Scaffolded `/Users/tamerlan/telegram-codex-bridge` from `MASTER_CODEX_BRIDGE_PROMPT.md` as a Node.js ESM Telegram ↔ Codex bridge.
- Implemented Telegram polling, one-chat authorization/claiming, command routing, file normalization/downloads, prompt wrapping, `codex exec` runner via `spawn`, `/run` allowlist, logging, state, README, PM2 ecosystem file, `.gitignore`, `local.env`, and `project.json`.
- `project.json` currently points `repoPath` to `/Users/tamerlan/telegram-codex-bridge`.
- 2026-04-29: User filled `local.env`; bridge started under PM2 as `telegram-codex-bridge`, status online, `pm2 save` completed.
- 2026-04-29: First plain Telegram health-check text (`Привет ты на связи?`) was routed as `/ask`, causing a full `codex exec` run that took ~203s. Added `/ping` and quick greeting/health-check handling so simple availability checks reply immediately without invoking Codex.
- 2026-04-29: Plain casual text `как дела?` also triggered full `codex exec` and took ~260s before being stopped. Added direct casual replies for `как дела` / `что делаешь` style messages while preserving plain-text Codex launch for real work tasks. Also changed Codex prompt passing from CLI argument to stdin (`codex exec -`) so task text is not exposed in `ps`, and added long-running progress Telegram messages at 30s/120s.

## Validation
- `npm install` completed and created `package-lock.json`.
- `npm run check` passes syntax checks for all source modules.
- `npm run start` fails correctly until `TELEGRAM_BOT_TOKEN` is set in `local.env`.
- PM2 status after launch: `telegram-codex-bridge` online, local `logs/bridge.log` contains `bridge.started`.
- After quick health-check patch, `npm run check` passes and PM2 was restarted/saved.
- After casual-routing/stdin/progress patch, `npm run check` passes and PM2 was restarted/saved.

## Decisions
- Keep Codex global configuration untouched; bridge only calls existing `codex exec`.
- Use `node-telegram-bot-api` as required by the master prompt.
- Use npm `overrides` to reduce transitive dependency risk where possible without replacing the required Telegram package.

## Risks / blockers
- `npm audit --omit=dev` still reports 6 moderate vulnerabilities from the required `node-telegram-bot-api` → `@cypress/request/request` chain. Critical `form-data`/`qs` issues were reduced via overrides, but `request` itself remains deprecated/vulnerable.
- Real Telegram command flow still needs user verification from Telegram (`/start`, `/status`, `/ask ...`).
- Simple Telegram text is still `/ask` by design except recognized health-check phrases (`ping`, `пинг`, `привет`, `hello`, `hi`, and `привет/hello/hi ... на связи`).
- Casual/social text now receives a direct bridge reply; real plain-text work requests still launch Codex without requiring `/ask`.
- Full reboot autostart is not yet enabled: `pm2 startup` produced a sudo launchd command that must be run manually.

## Next steps
- In Telegram, send `/start`, `/status`, then `/ask Analyze this repository and explain what it does.`
- For fast bot availability checks, use `/ping` or `привет ты на связи?`.
- For casual check, `как дела?` should answer immediately; for real work, send the task as normal text.
- For reboot autostart, run: `sudo env PATH=$PATH:/opt/homebrew/Cellar/node/25.8.0/bin /opt/homebrew/lib/node_modules/pm2/bin/pm2 startup launchd -u tamerlan --hp /Users/tamerlan`, then `pm2 save`.
- If audit risk is unacceptable, replace `node-telegram-bot-api` with a maintained Telegram SDK, but that would deviate from the current master prompt.
