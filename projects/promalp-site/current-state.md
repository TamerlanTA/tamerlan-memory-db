# Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

## 2026-05-12 — Bootstrap + MVP-сборка
- Память: `projects/promalp-site/` со всеми каноническими файлами (overview, current-state, decisions, risks, next-steps, prompts, sessions/).
- Скелет переделан под **dark cinematic premium B2B**:
  - Стек: Next.js 14 (App Router) + TS + Tailwind + Framer Motion + lucide-react.
  - Цветовая система: `#04070D` фон, `#22D3EE` cyan-акцент, `#FF7A1A` safety-orange, mono-метки JetBrains Mono.
  - Визуал: grid overlays, radial-glow, кинематографические fade-маски, glass-карточки, status-dots, HUD-углы.
  - Хедер/футер: `Navbar.tsx` (pill-навигация со статусом и CTA), `Footer.tsx` (контакты, документы, рабочие часы).
- Реализованы все 11 секций в соответствии с MVP-спекой:
  01 Hero — анимированное SVG-здание (14 этажей, мерцающие окна, спускающийся «альпинист» на верёвке, scan-line, координаты), CTA-кнопки, micro-stats.
  02 TrustBar — 4 trust-метки.
  03 ProblemRisk — 4 карточки риска.
  04 Services — 6 карточек услуг.
  05 Safety — 6 столпов безопасности + футер с CTA на пакет документов.
  06 Cases — 3 кейса (ЖК / БЦ / частный дом) с задачей, сроком, бригадой, результатом + SVG-визуал.
  07 Quiz — интерактивный 5-шаговый квиз (state, прогресс-бар, валидация, framer-motion переходы), success-state «Заявка принята. Ассистент уже готовит уточняющий звонок.»
  08 AIPipeline — 6-узловой pipeline с пульсирующими статусами и анимированным data-packet вдоль линии.
  09 CRMPreview — карточка Airtable (#2451, AI score 9/10) + Telegram-пузырь бригадиру.
  10 Faq — accordion на 6 вопросов с AnimatePresence.
  11 FinalCTA — две кнопки (расчёт + WhatsApp), 3 trust-плитки.
- UI-примитивы: `Button`, `StatusDot`, `SectionShell` (eyebrow + index `NN / 11` + title + subtitle).
- Lead-API не реализован — комментарии-якоря для интеграции стоят в `Quiz.tsx` (`submitLead`) и `CRMPreview.tsx`. Сейчас лид логируется в console + fake-success.
- `npm run build`: ✓ `Compiled successfully`, route `/` = 46.9 kB / First Load JS 134 kB.
- `npm install` отработал, `node_modules` создан.
- Git не инициализирован, Vercel-проект не создан, домен не выбран.
- Контент в секциях — реалистичные демо-формулировки на ru-RU, готов к замене на реальный материал после Discovery.

## 2026-05-14 — Hero адаптив и UI polish
- Исправлена светлая editorial-версия сайта `Vysota`: главный hero-заголовок больше не обрезается на широком desktop и mobile.
- Hero переведён на более устойчивый fluid type scale: меньше mobile-size, меньше desktop max-size, спокойнее горизонтальные отступы строк, CTA стали якорями на `#quiz` и `#cases`.
- Добавлены недостающие Tailwind/UI токены и утилиты, которые уже использовались компонентами (`bg-deep`, `bg-elev`, `line-strong`, `ink-dim`, `ink-muted`, `cyan`, `.mono`, `.grid-overlay`, `.gradient-text`).
- Добавлен `#contact` на финальный CTA, чтобы nav/footer inquiry links не вели в пустой якорь.
- Проверка: `npm run build` проходит; Playwright screenshots сняты на 2048×1242, 390×844 и секцию services.
