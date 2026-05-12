# Session 2026-05-12 — Project bootstrap

## Related
- [[../overview]]
- [[../current-state]]
- [[../decisions]]
- [[../next-steps]]

## What was done
- Создан проект памяти `projects/promalp-site/` с каноническими файлами: overview, current-state, decisions, risks, next-steps, prompts, sessions/.
- Создан скелет в `/Users/tamerlan/Desktop/promalpsite`:
  - Next.js 14 (App Router) + TypeScript + Tailwind.
  - 10 stub-секций (`Hero`, `SocialProof`, `Services`, `Quiz`, `Cases`, `Safety`, `Process`, `Testimonials`, `Faq`, `Contact`) — точно по слайду 5 деки.
  - `app/layout.tsx` с ru-RU метаданными, Inter font.
  - Токены деки (синий градиент + белый минимализм) в Tailwind config и `globals.css`.
  - `.gitignore`, `tsconfig.json`, `next.config.mjs`, `postcss.config.mjs`, `tailwind.config.ts`.

## Key findings
- Стек идентичен FlowOps2 → можно целиком скопировать `/api/contact` как основу для `/api/lead`.
- Структура 10 секций жёстко приходит из деки (`[[../industrial-climbers-flowops]]` слайд 5) — менять её без согласования с клиентом не стоит.

## Blockers
- Нет контента, реквизитов, параметров Airtable/Telegram, матрицы расчёта квиза. См. `[[../risks]]`.

## Next steps
- `npm install` + dev-сервер + git init.
- Discovery-неделя с клиентом.
- См. `[[../next-steps]]`.
