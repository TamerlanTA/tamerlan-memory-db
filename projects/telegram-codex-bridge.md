# Telegram Codex Bridge

## Related
- [[agent-memory]]

## Current status
- 2026-04-29: Scaffolded `/Users/tamerlan/telegram-codex-bridge` from `MASTER_CODEX_BRIDGE_PROMPT.md` as a Node.js ESM Telegram ↔ Codex bridge.
- Implemented Telegram polling, one-chat authorization/claiming, command routing, file normalization/downloads, prompt wrapping, `codex exec` runner via `spawn`, `/run` allowlist, logging, state, README, PM2 ecosystem file, `.gitignore`, `local.env`, and `project.json`.
- `project.json` currently points `repoPath` to `/Users/tamerlan/telegram-codex-bridge`.
- 2026-04-29: User filled `local.env`; bridge started under PM2 as `telegram-codex-bridge`, status online, `pm2 save` completed.
- 2026-04-29: First plain Telegram health-check text (`Привет ты на связи?`) was routed as `/ask`, causing a full `codex exec` run that took ~203s. Added `/ping` and quick greeting/health-check handling so simple availability checks reply immediately without invoking Codex.
- 2026-04-29: Plain casual routing was rejected by user; user wants Codex for normal plain text, not canned bridge answers. Removed casual/health phrase interception for plain text. `/ping` now also routes through Codex. `codex exec -` initially failed because bridge repo is not a trusted/git directory; fixed by adding `--skip-git-repo-check` to `project.json` `codexArgs`. Kept stdin prompt passing and progress status messages.
- 2026-04-29: User explicitly requested full filesystem/action access from Telegram bridge and acknowledged the security risk. Updated `project.json` `codexArgs` to `["exec", "--dangerously-bypass-approvals-and-sandbox", "--skip-git-repo-check"]`. Manual check showed Codex starts with `approval: never` and `sandbox: danger-full-access`. PM2 restarted/saved.
- 2026-04-29: Voice/audio attachment flow verified at repository level. The bridge downloads Telegram voice/audio files and includes local paths in Codex prompts, but it does not yet contain an audio transcription adapter or transcription dependency.

## Validation
- `npm install` completed and created `package-lock.json`.
- `npm run check` passes syntax checks for all source modules.
- `npm run start` fails correctly until `TELEGRAM_BOT_TOKEN` is set in `local.env`.
- PM2 status after launch: `telegram-codex-bridge` online, local `logs/bridge.log` contains `bridge.started`.
- After quick health-check patch, `npm run check` passes and PM2 was restarted/saved.
- After removing canned plain-text replies and adding `--skip-git-repo-check`, `npm run check` passes and PM2 was restarted/saved. Manual `codex exec --skip-git-repo-check -` outside sandbox returned `ready`.
- After enabling bypass permissions, `npm run check` passes. Manual `codex exec --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check -` returned `ready`.
- For a received Telegram voice file (`voice-43.ogg`), local inspection confirmed a valid OGG/Opus mono audio file, 55.9s, 219120 bytes. `npm run check` passes.

## Decisions
- Keep Codex global configuration untouched; bridge only calls existing `codex exec`.
- Use `node-telegram-bot-api` as required by the master prompt.
- Use npm `overrides` to reduce transitive dependency risk where possible without replacing the required Telegram package.

## Risks / blockers
- `npm audit --omit=dev` still reports 6 moderate vulnerabilities from the required `node-telegram-bot-api` → `@cypress/request/request` chain. Critical `form-data`/`qs` issues were reduced via overrides, but `request` itself remains deprecated/vulnerable.
- Real Telegram command flow still needs user verification from Telegram (`/start`, `/status`, `/ask ...`).
- Simple Telegram text is still `/ask` by design except recognized health-check phrases (`ping`, `пинг`, `привет`, `hello`, `hi`, and `привет/hello/hi ... на связи`).
- All plain text now routes to Codex without requiring `/ask`; do not add canned content replies unless explicitly requested. Bridge-only messages should be operational status only, e.g. task accepted/progress/error.
- Full reboot autostart is not yet enabled: `pm2 startup` produced a sudo launchd command that must be run manually.
- Telegram-triggered Codex now runs with `danger-full-access` and no approval prompts. This is intentional per user request but high-risk if Telegram token/chat authorization is compromised.
- Audio is accepted and forwarded to Codex as a file path, but actual speech-to-text is not configured. Voice messages cannot be transcribed automatically until an adapter is added.

## Next steps
- In Telegram, send `/start`, `/status`, then `/ask Analyze this repository and explain what it does.`
- For fast bot availability checks, use `/ping` or `привет ты на связи?`.
- Test Telegram plain text again; expected behavior is immediate “Принял. Запускаю Codex.” followed by Codex output.
- For reboot autostart, run: `sudo env PATH=$PATH:/opt/homebrew/Cellar/node/25.8.0/bin /opt/homebrew/lib/node_modules/pm2/bin/pm2 startup launchd -u tamerlan --hp /Users/tamerlan`, then `pm2 save`.
- If audit risk is unacceptable, replace `node-telegram-bot-api` with a maintained Telegram SDK, but that would deviate from the current master prompt.
- Add a transcription adapter for `kind: "audio"` attachments, likely behind explicit env configuration for a speech-to-text provider, then inject transcript text into the Codex prompt before the file list.
