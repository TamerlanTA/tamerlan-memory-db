# Session 2026-05-12 — Dark cinematic MVP build

## Related
- [[../overview]]
- [[../current-state]]
- [[../decisions]]
- [[../next-steps]]

## What was done
- Полностью переделана палитра и шейпинг скелета под **dark cinematic premium B2B**:
  - Tailwind tokens: `bg #04070D / bg-deep #020409 / bg-elev #0A1322 / cyan #22D3EE / safety #FF7A1A / ink #E6EDF6`.
  - Кастомные keyframes: `flicker`, `scanY`, `ropeFall`, `pulse`.
  - Backgrounds: `bg-radial-cyan`, `bg-radial-safety`, `grid-fine` + utility `.grid-overlay`.
  - Шрифты: Inter (cyrillic) + JetBrains Mono для технических меток.
- Добавлены зависимости: `framer-motion ^11.3.8`, `lucide-react ^0.408.0`.
- Старые секции удалены (`SocialProof`, `Testimonials`, `Process`, `Contact`, `Section`).
- Новые UI-примитивы: `SectionShell` (eyebrow + index `NN / 11` + gradient-title), `Button` (variants: primary safety-orange / secondary glass / ghost), `StatusDot` (pulsing dot + uppercase mono).
- Хедер `Navbar.tsx` — pill nav со статусом «Алматы», телефоном и CTA-pill «Получить расчёт».
- Футер `Footer.tsx` — контакты, документы, часы работы.
- Hero: анимированное SVG-здание (`HeroBuilding.tsx`): 14 этажей × 5 окон, детерминированный паттерн «лит/тёмное», CSS-flicker, scan-line, верёвка из safety-orange, дот «альпиниста» с halo, координаты «43.238° N · 76.945° E», HUD-баджи. Плюс floating data-ribbon снизу.
- 11 секций, все на ru-RU, реалистичные демо-формулировки:
  - Hero + Trust Bar + Problem/Risk + Services (6 карт) + Safety (6 столпов) + Cases (3 объекта с задачей/сроком/бригадой/результатом) + Quiz (5 шагов + успешный финал) + AI Pipeline (6 узлов + анимированный data-packet) + CRM/Telegram Preview (карточка Airtable + Telegram-пузырь) + FAQ accordion + Final CTA с двумя кнопками.
- Квиз реально работает: useState/AnimatePresence, прогресс-бар, валидация на каждом шаге, fake-submit с задержкой, success-state точно по копиратингу спеки.
- Webhook-якоря оставлены комментариями в `Quiz.tsx` (`submitLead`) и `CRMPreview.tsx` с env-vars и порядком вызовов (n8n → Airtable → Vapi → Telegram → WhatsApp).
- Проверка: `npm install` OK, `npm run build` → ✓ Compiled successfully, route `/` 46.9 kB / 134 kB First Load JS.

## Key findings
- Framer Motion + SVG-trick без R3F полностью достаточно для cinematic-hero: SVG-здание с CSS keyframes + motion.g для климбера выглядит «технологично» и не тянет лишние ~150 кб бандла R3F.
- Детерминированные паттерны окон (`(r*7 + c*13 + 5) % 11 < 5`) избегают SSR/CSR hydration mismatch — критично, потому что Math.random() в SSR-Math.random() в CSR ломает гидрацию.
- Safety-orange как primary CTA + cyan как secondary accent работает лучше, чем cyan-CTA — даёт промышленный B2B-tone (как у самой профессии).

## Blockers
- Контент / реквизиты / параметры Airtable / Telegram / Vapi не подтверждены клиентом — см. `[[../risks]]`.
- Lead-API сейчас stub: лид логируется в `console.info`.

## Next steps
- Discovery-неделя с клиентом → реальные кейсы, фото, отзывы, юр.реквизиты, домен.
- Реализовать `/app/api/lead/route.ts` → n8n webhook → Airtable + Telegram + Vapi.
- Согласовать матрицу расчёта квиза с бригадиром (₸ за п.м. / м² по типу работ × этажности × срочности).
- Подключить Vercel-проект и домен.
- См. `[[../next-steps]]`.
