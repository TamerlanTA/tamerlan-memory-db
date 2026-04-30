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
- 2026-04-29: Added local offline voice transcription without OpenAI API. Installed `whisper-cpp` via Homebrew, downloaded multilingual `models/ggml-base.bin` from Hugging Face, and added `src/localAudioTranscriber.mjs`. Audio/voice files are converted with `ffmpeg` to 16kHz mono WAV under `transcriptions/`, transcribed with `whisper-cli`, and transcript text is injected into the Codex prompt before attached file paths. Tested against existing Telegram voice file; transcript succeeded in ~0.6s.
- 2026-04-29: Latest voice command was transcribed successfully but Codex failed because OpenAI Codex returned usage limit (`You've hit your usage limit. Upgrade to Pro`). Updated `src/codexRunner.mjs` to detect usage-limit errors and return a concise Telegram message instead of echoing the full prompt/stderr. Manually recorded the transcribed task list into `[[My-tasks]]`.
- 2026-04-29: Improved Telegram UX. Added native Telegram command menu registration (`setMyCommands`) with 35 commands, grouped `/help`, usage examples, progressive single-message status edits, output formatter/sanitizer for Codex replies, `/logs` alias, local `/files` and `/read`, command routing for planning/debug/memory/n8n/media sync commands, and `scripts/manualVerification.mjs`.
- 2026-04-29: Adjusted Telegram reply style to be chat-assistant-like. Removed mandatory `Expected response` report sections from prompt builder, added language-aware concise Telegram style instructions, and extended formatter to strip generic report headings (`What I understood`, `Validation performed`, etc.) when they appear.
- 2026-04-29: n8n skill discovery/install request timed out at 300s, but skills were installed under `/Users/tamerlan/.agents/skills`. Increased bridge `timeoutMs` from 300000 to 900000 and changed timeout handling to return partial Codex stdout/stderr when available instead of only "timed out". `/tools` now lists local skills without running Codex.
- 2026-04-29: Added Codex plugins section for Telegram. New commands: `/plugins` lists installed/connected plugins from `/Users/tamerlan/.codex/plugins/cache`; `/plugins <name>` shows details, skills, app connector IDs, and examples; `/plugin <name> <task>` runs Codex with explicit instruction to use that installed plugin, its skills, and connected app when available. Telegram command menu now registers 37 commands.
- 2026-04-30: Updated Obsidian vault templates so generated session/project notes keep correct graph links. `templates/session-template.md` now links to project core notes (`overview`, `current-state`, `next-steps`, plus `decisions`/`risks`), and `templates/project-template.md` now links to `current-focus` and the session template.

## Validation
- `npm install` completed and created `package-lock.json`.
- `npm run check` passes syntax checks for all source modules.
- `npm run start` fails correctly until `TELEGRAM_BOT_TOKEN` is set in `local.env`.
- PM2 status after launch: `telegram-codex-bridge` online, local `logs/bridge.log` contains `bridge.started`.
- After quick health-check patch, `npm run check` passes and PM2 was restarted/saved.
- After removing canned plain-text replies and adding `--skip-git-repo-check`, `npm run check` passes and PM2 was restarted/saved. Manual `codex exec --skip-git-repo-check -` outside sandbox returned `ready`.
- After enabling bypass permissions, `npm run check` passes. Manual `codex exec --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check -` returned `ready`.
- For a received Telegram voice file (`voice-43.ogg`), local inspection confirmed a valid OGG/Opus mono audio file, 55.9s, 219120 bytes. `npm run check` passes.
- Local Whisper validation: `whisper-cli` initially could not read Telegram OGG directly, so `ffmpeg` conversion to WAV was added. Adapter test returned the expected Russian transcript from `uploads/20260429125636_43_566431.ogg`.
- Latest voice transcript was recovered locally from `uploads/20260429131331_47_4cf402.ogg` and used to update `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/My-tasks.md`.
- Telegram UX verification: `npm run check` and `npm run verify:manual` pass. PM2 restarted/saved. Runtime log shows `telegram.commands.registered count=35`.
- Reply-style verification: `npm run check` and `npm run verify:manual` pass. PM2 restarted/saved.
- Timeout fix verification: `npm run check` and `npm run verify:manual` pass. PM2 restarted/saved. Confirmed n8n skills exist locally: `n8n`, `n8n-automation`, `n8n-automation-architect`, `n8n-code-javascript`, `n8n-code-python`, `n8n-expression-syntax`, `n8n-mcp-tools-expert`, `n8n-node-configuration`, `n8n-validation-expert`, `n8n-workflow`, `n8n-workflow-automation`, `n8n-workflow-generator`, `n8n-workflow-patterns`, `n8n-workflow-testing-fundamentals`.
- Plugin registry verification: `npm run check` and `npm run verify:manual` pass. Local registry found Browser Use, Build macOS Apps, Build Web Apps, Computer Use, Documents, Figma, GitHub, Gmail, Notion, Presentations, Spreadsheets, Stripe, Teams, Vercel. Runtime log shows `telegram.commands.registered count=37`.
- Template link verification: both files in `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/templates` contain `## Related` with operational wikilinks.

## Decisions
- Keep Codex global configuration untouched; bridge only calls existing `codex exec`.
- Use `node-telegram-bot-api` as required by the master prompt.
- Use npm `overrides` to reduce transitive dependency risk where possible without replacing the required Telegram package.

## Risks / blockers
- `npm audit --omit=dev` still reports 6 moderate vulnerabilities from the required `node-telegram-bot-api` → `@cypress/request/request` chain. Critical `form-data`/`qs` issues were reduced via overrides, but `request` itself remains deprecated/vulnerable.
- Real Telegram command flow still needs user verification from Telegram (`/start`, `/status`, `/ask ...`).
- All plain text now routes to Codex without requiring `/ask`; do not add canned content replies unless explicitly requested. Bridge-only messages should be operational status only, e.g. task accepted/progress/error.
- Full reboot autostart is not yet enabled: `pm2 startup` produced a sudo launchd command that must be run manually.
- Telegram-triggered Codex now runs with `danger-full-access` and no approval prompts. This is intentional per user request but high-risk if Telegram token/chat authorization is compromised.
- Audio is now transcribed locally via `ffmpeg` + `whisper-cli` + `models/ggml-base.bin`. No external API is used. If the model or tools are missing, bridge should still pass file path and include transcription failure details.
- Codex can still fail after transcription when subscription usage limit is reached; bridge now reports that clearly, but cannot bypass account usage limits.
- Output formatting is heuristic: it strips common Codex CLI headers, raw prompt echoes, debug/tool-call-like lines, bold markdown markers, and noisy links for normal replies. `/debug` and `/logs` intentionally expose more raw detail.
- `/plugin` can guide Codex to use a plugin and connected app, but actual plugin/app execution still depends on Codex CLI session capabilities, account auth, and plugin availability in the underlying Codex runtime.

## Next steps
- In Telegram, send `/start`, `/status`, then `/ask Analyze this repository and explain what it does.`
- For fast bot availability checks, use `/ping` or `привет ты на связи?`.
- Test Telegram plain text again; expected behavior is immediate “Принял. Запускаю Codex.” followed by Codex output.
- For reboot autostart, run: `sudo env PATH=$PATH:/opt/homebrew/Cellar/node/25.8.0/bin /opt/homebrew/lib/node_modules/pm2/bin/pm2 startup launchd -u tamerlan --hp /Users/tamerlan`, then `pm2 save`.
- If audit risk is unacceptable, replace `node-telegram-bot-api` with a maintained Telegram SDK, but that would deviate from the current master prompt.
- Test a fresh Telegram voice message end-to-end; expected behavior: immediate “Принял. Готовлю данные для Codex.”, local transcription log `audio.transcription.finished`, then Codex output based on transcript.
