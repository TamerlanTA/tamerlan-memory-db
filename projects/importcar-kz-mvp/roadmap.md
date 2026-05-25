# ImportCar.kz — Полный продуктовый роадмап

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

---

## Главный продуктовый принцип

**Калькулятор полной стоимости авто под ключ — ядро продукта.**
Каталог, заявки, импортёры, аккаунт и подписки строятся вокруг него.

Новая стратегическая рамка: **AI-assisted import calculator with deterministic pricing engine**.
AI извлекает, нормализует, обогащает, объясняет и флагует риски. AI не является source of truth для финальной цены и не должен самостоятельно "считать итог". Финальную стоимость считает deterministic pricing engine на versioned rules, курсах, логистике, таможне, service fee и buffers.

Внутренняя долгосрочная цель после verified link/VIN/manager confirmation — стремиться к 5-7% error, но публично это не обещать до появления реальных данных. Публичная формулировка: "максимально приближенный расчёт", "предварительный расчёт", "точный расчёт после проверки ссылки/VIN", "финальная стоимость зависит от курса, документов, логистики и актуальных ставок".

Целевая траектория: **PWA → Capacitor App Store build → Expo/React Native при наличии traction**

---

## Центральная воронка (primary flow)

```
Открыл приложение
→ Рассчитал авто вручную или отправил ссылку
→ Проверил/исправил распознанные данные
→ Увидел полную стоимость + структуру платежей
→ Отправил ссылку/VIN
→ Получил точный расчёт
→ Оставил заявку на импорт
```

Каталог — вторичный flow. Аккаунт — третий.

---

## Версионный roadmap

### v0.1 — Production Calculator Web ← ТЕКУЩИЙ ПРИОРИТЕТ
Цель: сильный калькулятор и заявки, можно давать реальным пользователям.

```
CalculatorScreen v2 (главный экран)
Итог в тенге — главное число, ниже ≈ USD
Полная разбивка: авто / доставка / таможня / утильсбор / регистрация / комиссия / резерв
Explainability блок (возраст, объём, ставка, версия правил, курс, предупреждения)
Trust-индикатор точности + disclaimer
CTA после расчёта: точный расчёт / по ссылке / WhatsApp / сохранить
Lead form: имя + телефон + город + ссылка на авто + комментарий
Calculation snapshot в заявке (весь расчёт сохраняется вместе с контактами)
Таблица calculations в Supabase
Admin leads view показывает snapshot расчёта
Analytics events: calculator_opened / calculation_completed / lead_submitted / whatsapp_clicked
Legal disclaimers (предварительный расчёт, не оферта)
```

### v0.2 — Mobile Web App / PWA ✅ ВЫПОЛНЕНО (2026-05-21)
```
PWA manifest ✅
installable app ✅
safe areas ✅
bottom navigation (4 таба) ✅
favorites (localStorage) ✅
mobile-first cards + detail ✅
StickyCta с WhatsApp ✅
```

### Phase AI-0 — Roadmap and Architecture Update ✅ ВЫПОЛНЕНО (2026-05-25)
Цель: зафиксировать AI-assisted стратегию без реализации новых функций.

```
Документировать AI-assisted calculator strategy
Уточнить: AI не final price authority
Сохранить deterministic pricing engine как source of truth
Обновить roadmap/current-state/next-steps/decisions/risks
Не добавлять AI API, Edge Functions, auth, payments, subscriptions, App Store packaging
```

### Phase AI-1 — AI Contracts and Schemas ✅ ВЫПОЛНЕНО (2026-05-25)
Цель: подготовить типы и контракты до реального AI API.

```
VehicleExtractionResult type
Zod validation schema
AI snapshot extension types
Confidence logic design
Strict JSON-only AI output contract
Invalid/missing data cannot silently enter pricing engine
No real AI API yet
No OpenAI/Gemini keys
No frontend secrets
Keep deterministic pricing sanity tests intact
```

Implementation notes:
- Added isolated domain module `src/domain/aiCalculator/`.
- Added Zod runtime validation and safe `parseVehicleExtraction(input)`.
- Added normalization helpers for engine volume, fuel type, currency, and money parsing.
- Added confidence scoring and additive snapshot extension schema.
- Added `npm run ai:contracts`.
- No AI provider, Edge Function, UI, auth, payments, subscriptions, or calculator behavior changes.

### Phase AI-2 — Secure AI Link Extraction MVP ✅ ВЫПОЛНЕНО (2026-05-25)
Цель: безопасно распознавать авто по ссылке без утечки секретов.

```
Supabase Edge Function or secure backend endpoint
Possible endpoint: supabase/functions/analyze-car-link
Server-side AI provider key only
AI provider abstraction
Strict input validation
Strict output validation
Audit trail for extraction attempts
Rate limiting later
Fallback if URL unreadable
```

Input:

```json
{
  "url": "string"
}
```

Output:

```json
{
  "extractedVehicle": {},
  "confidence": 0.86,
  "missingFields": [],
  "warnings": []
}
```

Implementation notes:
- Added Supabase Edge Function structure `supabase/functions/analyze-car-link/`.
- Added `index.ts`, `provider.ts`, `prompt.ts`, and `validation.ts`.
- Provider secrets are read server-side from Supabase Edge Function env only.
- No `VITE_` AI secrets are used.
- Missing provider config returns `AI_PROVIDER_NOT_CONFIGURED`.
- Listing fetch failures fall back to `listingText`.
- If no usable content exists, endpoint returns `LISTING_CONTENT_UNAVAILABLE`.
- AI output is validated before response.
- Minimal validation/normalization logic is mirrored in the function folder for Deno deploy reliability; unify with `src/domain/aiCalculator` later if shared packaging is introduced.
- The endpoint does not calculate final import price.
- Supabase CLI/Deno verification remains a manual deploy step because neither tool is installed in the local workspace.

### Phase AI-3 — User Confirmation + AI-Assisted Calculation ← СЛЕДУЮЩИЙ STRATEGIC IMPLEMENTATION BLOCK
Цель: AI помогает заполнить данные, но пользователь подтверждает, а deterministic engine считает.

```
Calculator mode switch: "Быстрый расчёт" / "По ссылке"
AI extracts vehicle data from listing URL or pasted text
Show extracted vehicle card before calculation
User can edit/confirm extracted fields
Normalized data goes into existing pricing engine
Pricing engine computes final total
AI does not invent final price
```

Example confirmation copy:

```
Мы распознали данные авто:
Genesis GV70, 2021, 2.5 бензин, ₩42,000,000, 47,000 км.
Проверьте данные перед расчётом.
```

### Phase AI-4 — Risk Reviewer + Explanation Layer
Цель: AI добавляет полезный контекст поверх уже рассчитанного результата.

```
AI risk warnings:
- suspiciously low price
- missing VIN
- unclear engine/fuel type
- inconsistent model/engine combination
- missing auction sheet
- exchange rate/logistics uncertainty
- listing not readable

Grounded explanation generator:
- how total was calculated
- what can change final price
- what data should be verified
- why confidence is high/medium/low
```

AI risk reviewer and explanation layer must not overwrite deterministic calculation.

### Phase AI-5 — Accuracy Calibration
Цель: улучшать точность правилами и данными, а не обещаниями.

```
Store estimatedTotalKzt
Store finalManagerTotalKzt
Store differencePercent
Store reasonForDifference
Store logisticsActual
Store exchangeRateUsed
Store finalOutcome
Analyze variance
Adjust logistics buffers, risk buffers, service fees, model/country-specific adjustments
```

### Phase AI-6 — Verified Calculation Workflow
Цель: выделить high-confidence path после проверки менеджером.

```
Manager confirmation
Verified quote status
Verified calculation snapshot
High-confidence calculation path
```

### v0.3 — Auth + User Account
Цель: хранить историю и заявки.
```
Supabase Auth (Phone OTP + Google + Apple)
User profiles table
Saved calculations (history)
User requests (мои заявки)
Favorites synced to account
Авторизация запрашивается только когда нужно: сохранить / отправить заявку / статус
```

### v0.4 — Real Inventory
Цель: каталог перестаёт выглядеть как демо.
```
Curated real listings (30 качественных, не 300 случайных)
Реальные фото + source + дата актуальности
Честные лейблы: "Пример расчёта" vs "Актуально на дату"
Admin inventory management
Demo/active статусы
Фильтры
```

### v0.5 — Payments
Цель: первые деньги.
```
Платный точный расчёт (по ссылке) — от 1 990 ₸
Платная проверка авто / история — от 4 990–9 990 ₸
Kaspi / Halyk / CloudPayments / Freedom Pay
Payment records в БД
Receipt/status
```

### v0.6 — Subscriptions
Цель: recurring revenue.
```
Free plan: базовый калькулятор, 3 сохранённых расчёта, каталог, избранное локально, заявка
Plus plan (1 990–4 990 ₸/мес): неограниченные расчёты, история, уведомления о курсе, расширенная разбивка, приоритетная проверка
Billing page, subscription status
```

### v0.7 — Importer Partner Layer
Цель: монетизировать через партнёров.
```
Importer profiles с verified badges
Lead routing к импортёрам
Operator assignment
Partner dashboard (light)
Монетизация: плата за лид / комиссия / премиум-размещение / B2B подписка 30–150k ₸/мес
```

### v0.8 — Native App Preparation
Цель: тестовая сборка на телефоне.
```
Capacitor setup
iOS build (Xcode)
Android build (Android Studio)
Native safe areas, push notification foundation
App icons (192x192, 512x512 PNG)
Splash screen
Privacy settings
App Store assets (screenshots, описание, keywords)
```

### v1.0 — App Store / Google Play Release
Цель: публичный релиз.
```
Apple Developer Program + Google Play Console
Production Supabase project
Domain imcar.kz / importcar.kz
Privacy policy URL + Terms URL + Support URL
Screenshots для iPhone + Android
Crash/error monitoring (Sentry)
Analytics (PostHog / Firebase)
Whislist: Apple IAP для digital subscriptions, external payment для real-world services
```

---

## База данных (целевая схема)

```sql
users/profiles       — id, phone, email, name, city, created_at
calculations         — id, user_id (null ok), session_id, country, vehicle_price, currency,
                       year, engine_volume, fuel_type, delivery_city, result_total_kzt,
                       result_total_usd, breakdown_json, explanation_json,
                       pricing_rule_version, created_at
leads/requests       — id, user_id (null ok), calculation_id, name, phone, city,
                       car_url, vin, comment, status, source, assigned_to, created/updated_at
cars                 — id, brand, model, year, mileage, engine_volume, fuel_type,
                       price_foreign, currency, estimated_total_kzt, country,
                       source_url, image_urls, status, is_demo, last_checked_at
favorites            — id, user_id, car_id, created_at
importers            — id, name, city, description, service_fee, rating, verified,
                       documents_verified, created_at
request_events       — id, request_id, status, note, created_by, created_at
subscriptions        — id, user_id, plan, status, provider, started_at, expires_at
payments             — id, user_id, request_id (null ok), amount, currency,
                       provider, status, created_at
ai_extractions       — id, user_id (null ok), source_url, provider, model,
                       confidence, missing_fields, warnings, raw_response_json,
                       normalized_vehicle_json, status, created_at
calibration_records  — id, calculation_id, request_id, estimated_total_kzt,
                       final_manager_total_kzt, difference_percent,
                       reason_for_difference, logistics_actual,
                       exchange_rate_used, final_outcome, created_at
```

## AI-assisted snapshot extension

Future calculation snapshots should support:

```json
{
  "inputSource": "manual | ai_link | manager_verified",
  "aiExtraction": {
    "provider": "string",
    "model": "string",
    "confidence": 0.86,
    "extractedAt": "ISO datetime",
    "sourceUrl": "string",
    "missingFields": [],
    "warnings": [],
    "rawExtractionId": "string"
  },
  "normalizedVehicle": {
    "brand": "string",
    "model": "string",
    "year": 2021,
    "price": 42000000,
    "currency": "KRW",
    "mileageKm": 47000,
    "engineVolumeCc": 2497,
    "fuelType": "petrol",
    "vin": "string",
    "trim": "string"
  }
}
```

## AI extraction contract

Vehicle listing extraction should return strict JSON only:

```json
{
  "sourceUrl": "string",
  "country": "Korea",
  "brand": "Genesis",
  "model": "GV70",
  "year": 2021,
  "productionDate": "string",
  "price": 42000000,
  "currency": "KRW",
  "mileageKm": 47000,
  "engineVolumeCc": 2497,
  "fuelType": "petrol",
  "transmission": "automatic",
  "trim": "string",
  "vin": "string",
  "confidence": 0.86,
  "missingFields": [],
  "warnings": []
}
```

Use schema validation, preferably Zod. Invalid or missing data must not silently enter the pricing engine.

## Confidence levels

```
Быстрый расчёт — ориентировочный
Расчёт по ссылке — точнее
Расчёт по VIN/документам — высокий уровень
Проверенный менеджером расчёт — максимально точный
```

Confidence depends on data completeness:
- price present
- year present
- engine volume present
- fuel type present
- source URL present
- VIN/auction sheet present
- logistics route known
- current rates available

## Data source/fallback reality

Encar/listing pages may be dynamic, blocked, or not readable from backend.

Fallbacks:
- user pastes listing text
- user uploads screenshot later
- user manually edits extracted fields
- manager verifies hot leads

---

## Analytics events (обязательные)

```
calculator_opened
calculation_completed
calculation_saved
ai_link_submitted
ai_extraction_completed
ai_extraction_failed
extracted_vehicle_confirmed
lead_started
lead_submitted
whatsapp_clicked
car_viewed
car_favorited
request_status_viewed
payment_started
payment_completed
```

---

## Навигация (UX-структура)

### Bottom navigation — до аккаунта
```
Калькулятор | Каталог | Избранное | Заявки
```

### Bottom navigation — после аккаунта
```
Калькулятор | Каталог | Заявки | Профиль
```

---

## Монетизация — правильный порядок

```
1. Сначала: бесплатный калькулятор + бесплатная заявка → WhatsApp-конверсия
2. Потом: платный точный расчёт по ссылке / VIN-проверка
3. Потом: подписка Plus для активных покупателей
4. Потом: B2B подписка для импортёров
```

**Разовые услуги вероятно конвертируют лучше подписки на раннем этапе.**
Подписка требует привычки. Проверка авто — понятная ценность здесь и сейчас.

---

## Технический стек

### Сейчас и Web/PWA
```
React + TypeScript + Vite
Supabase (DB + Auth + RLS)
Vercel (hosting)
PWA (manifest, safe areas)
```

### Добавить для production web
```
Supabase Auth (Phone OTP / Google / Apple)
PostHog (analytics)
Sentry (error tracking)
Kaspi/Halyk/CloudPayments (payments)
Resend/Postmark (email)
WhatsApp Business
```

### App Store path
```
Capacitor → iOS / Android build
Xcode + Android Studio
Apple IAP / Google Play Billing (для цифровых подписок)
External payment (для реальных услуг — может не требовать IAP)
```

---

## Главные риски и решения

| Риск | Решение |
|------|---------|
| Нет доверия к расчёту | Explainability + versioned rules + disclaimers + manual verification CTA |
| AI "галлюцинирует" цену | AI never calculates final price; deterministic pricing engine remains source of truth |
| AI extraction ошибается | Strict JSON + Zod validation + user confirmation/edit before calculation |
| Listing page не читается | Paste text / screenshot later / manual edit / manager verification fallback |
| Секреты AI провайдера | AI calls only via Supabase Edge Function or secure backend; no frontend secrets |
| Фейковый каталог | Curated real examples + demo labels + source/date |
| Слишком ранняя регистрация | Сначала расчёт без аккаунта, потом аккаунт по необходимости |
| App Store слишком рано | Сначала PWA + traction, потом Capacitor |
| Сложная монетизация | Сначала paid reports, подписки позже |

---

## Сервисы

| Категория | Выбор |
|-----------|-------|
| DB / Backend | Supabase |
| Auth | Supabase Auth |
| Hosting | Vercel |
| Analytics | PostHog (приоритет) + Firebase для app |
| Error tracking | Sentry |
| Email | Resend |
| Payments KZ | Kaspi / Halyk / CloudPayments |
| Payments App Store | Apple IAP / Google Play Billing |
| Messaging | WhatsApp Business + Telegram Bot |
| App packaging | Capacitor → Expo/RN если нужна полная нативность |
