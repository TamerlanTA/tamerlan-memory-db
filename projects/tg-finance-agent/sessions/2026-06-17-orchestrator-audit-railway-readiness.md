# Session 2026-06-17 — Orchestrator Audit and Railway Readiness

## Related
- [[../overview|overview]]
- [[../current-state|current-state]]
- [[../next-steps|next-steps]]
- [[../decisions|decisions]]
- [[../risks|risks]]

## What was done
- Used project-orchestrator review/final-audit framing to audit the implemented TG Finance Agent.
- Verified current commands:
  - `npm run typecheck`
  - `npm run parse:sample`
  - `npm run categorize -- ./data/sample_outputs/parsed_statement.json`
  - `npm run report -- ./data/sample_outputs/categorized_statement.json`
  - `npm run reminder:check -- --chatId 999003 --now 2026-07-03T04:00:00.000Z --day 3`
- Checked for obvious committed secrets; only `.env.example` and code references to env vars were found.
- Confirmed workspace is still not a git repository.

## Key findings
- The project is a working local MVP skeleton, not production-ready yet.
- Railway deployment is plausible for the Telegram bot, but needs production start/build config and storage decisions.
- Local JSON persistence will require a Railway volume or migration to Supabase/SQLite.
- Current n8n sample workflow uses local Execute Command and is not suitable for a separate Railway-hosted bot unless n8n can reach a real HTTP endpoint.

## Blockers
- Need real `TELEGRAM_BOT_TOKEN`.
- Need real/anonymized Kaspi PDF for parser validation.
- Need deployment storage decision: Railway volume vs Supabase/SQLite.
- Need decide whether to add HTTP server endpoints for n8n reminders before deployment.

## Next steps
- Get required deployment inputs from Tamerlan.
- Implement Railway hardening batch: production build/start scripts, optional `railway.toml`, storage path config, and optional HTTP endpoints for reminder contracts.

