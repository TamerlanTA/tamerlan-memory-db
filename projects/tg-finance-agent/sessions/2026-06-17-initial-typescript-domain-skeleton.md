# Session 2026-06-17 — Initial TypeScript Domain Skeleton

## Related
- [[../overview|overview]]
- [[../current-state|current-state]]
- [[../next-steps|next-steps]]
- [[../decisions|decisions]]
- [[../risks|risks]]

## What was done
- Created Node.js + TypeScript project skeleton in `/Users/tamerlan/Desktop/tg-finance-agent`.
- Added modular `src` structure: `domain`, `categorization`, `statements`, `reports`, `storage`.
- Added core domain types for `Transaction`, `StatementPeriod`, `AccountBalance`, `CategoryRule`, `PersonRule`, `MerchantRule`, `MonthlySummary`, `IncomeSummary`, `ExpenseSummary`, and `UncategorizedTransaction`.
- Added category taxonomy including real income, internal transfers, refunds/debt returns, business categories, expense categories, and review categories.
- Added docs: `docs/architecture.md` and `docs/category-system.md`.
- Added starter JSON rules: `data/category_rules.json`, `data/people_rules.json`, `data/merchant_rules.json`.
- Installed TypeScript dev dependencies and generated `package-lock.json`.
- Added `.gitignore`.

## Key findings
- `npm run typecheck` passes.
- The project is intentionally still only a domain/documentation skeleton.
- Telegram bot, n8n workflows, real PDF parsing, persistent storage, and AI calls are not implemented yet.

## Decisions made
- Keep incoming payments conservative: do not count all inflows as real income.
- Treat `С карты другого банка`, `Перевод на свой счет`, and ATM-related movement as internal/cash movement rather than real income by default.
- Treat `PAYPAL` and `UPWORK` as likely business/freelance income with inspectable confidence.
- Treat unknown people transfers as `Needs Review` until the user defines a durable rule.

## Files changed
- `/Users/tamerlan/Desktop/tg-finance-agent/package.json`
- `/Users/tamerlan/Desktop/tg-finance-agent/package-lock.json`
- `/Users/tamerlan/Desktop/tg-finance-agent/tsconfig.json`
- `/Users/tamerlan/Desktop/tg-finance-agent/.gitignore`
- `/Users/tamerlan/Desktop/tg-finance-agent/README.md`
- `/Users/tamerlan/Desktop/tg-finance-agent/src/**`
- `/Users/tamerlan/Desktop/tg-finance-agent/docs/**`
- `/Users/tamerlan/Desktop/tg-finance-agent/data/**`

## Blockers
- Need a real or anonymized Kaspi PDF statement to validate parser assumptions.
- Need to choose storage backend.

## Next steps
- Implement deterministic categorization loader and matching engine.
- Add tests around income safety behavior.
- Start parser spike with a sample Kaspi statement.

