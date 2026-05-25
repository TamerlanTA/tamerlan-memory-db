# ImportCar.kz MVP — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]
- [[roadmap]]

---

## Стратегические решения

- **Продукт**: Калькулятор — ядро. Всё остальное строится вокруг него
- **Траектория**: MVP → Production Calculator → Lead Capture → AI-assisted calculator contracts → Secure AI link extraction → User confirmation + deterministic calculation → Auth → Real Inventory → Payments → Subscriptions → Partner Layer → PWA polish → App Store
- **App path**: PWA → Capacitor (быстро в App Store) → React Native / Expo при наличии traction
- **Монетизация порядок**: сначала бесплатный калькулятор + WhatsApp-конверсия → платные разовые проверки → подписка Plus → B2B для импортёров
- **AI direction**: ImportCar.kz becomes an AI-assisted calculator, not an AI-only calculator. AI extracts/normalizes/explains/flags risks; deterministic pricing engine calculates final totals.

## Архитектура

- Vite + React + TypeScript + Supabase — стек остаётся
- State-based navigation (no React Router) — `activeTab` + `detailSource` для back-навигации
- Мобильный bottomNav hidden на ≥ 720px; desktop получит top-nav позже
- Аккаунт запрашивать только когда нужно: сохранить / заявка / статус, не при первом открытии

## Калькулятор

- Итог в тенге — главное число. KRW/USD — вспомогательный контекст
- Калькулятор — инструмент оценки, не юридический/налоговый совет
- Версионирование правил расчёта обязательно; explainability открыта пользователю
- Каждый расчёт сохраняется как snapshot вместе с заявкой (менеджер не спрашивает заново)
- AI не является authority для финальной цены и не должен "придумывать" итоговую стоимость.
- AI output для link extraction должен быть strict JSON only и проходить schema validation (предпочтительно Zod) до передачи в pricing engine.
- Пользователь должен подтвердить/отредактировать распознанные AI данные перед расчётом.
- Confidence уровни: быстрый расчёт — ориентировочный; по ссылке — точнее; по VIN/документам — высокий уровень; проверенный менеджером — максимально точный.
- Публично не обещать "5-7% accuracy" до накопления реальной статистики estimate vs final.

## Дизайн

- Emerald #16c784 (--showroom-accent) — текущий цвет системы
- System sans-serif ('Avenir Next', 'Segoe UI', Arial)
- Mobile-first; карточки, кнопки, поля — под iPhone

## Каталог

- Лучше 30 реальных, чем 300 случайных
- Честные лейблы: "Пример расчёта" vs "Актуально на дату: XX.XX.XXXX"
- Не запускать агрессивный scraping без понимания рисков

## Данные и безопасность

- Anonymous lead insert разрешён для MVP; read/update — только authenticated admin
- Supabase RLS не ослаблять
- Admin status controls read-only до появления authenticated admin access
- calculations таблица: user_id может быть NULL (анонимные расчёты)
- Будущие AI API calls нельзя делать из frontend. Использовать Supabase Edge Function или secure backend endpoint с server-side provider key.
- Будущий AI extraction должен иметь audit trail, strict input/output validation и позже rate limiting.

## Избранное

- localStorage (key: `importcar_favorites`) — без авторизации
- После появления аккаунта — синхронизировать с Supabase

## PWA

- theme_color: #16c784, display: standalone, viewport-fit=cover
- WhatsApp — placeholder 77071234567, заменить до реального запуска
- Реальные PNG иконки нужны для manifest перед App Store

## Монетизация (приоритеты)

- НЕ запускать подписку слишком рано
- Разовые услуги (проверка авто, точный расчёт) вероятно конвертируют лучше подписки на старте
- B2B (импортёры) — только после появления реального спроса
- Apple IAP требуется для цифровых подписок в iOS-приложении; external payment может быть допустим для реальных услуг (импорт, проверка)

## Платежи для Казахстана

- Kaspi / Halyk / CloudPayments / Freedom Pay — для web/PWA
- Apple IAP / Google Play Billing — для digital subscriptions в app
- Разделять: digital subscription vs real-world service payment — это влияет на App Store review
