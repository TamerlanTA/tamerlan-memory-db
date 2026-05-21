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

Целевая траектория: **PWA → Capacitor App Store build → Expo/React Native при наличии traction**

---

## Центральная воронка (primary flow)

```
Открыл приложение
→ Рассчитал авто
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
```

---

## Analytics events (обязательные)

```
calculator_opened
calculation_completed
calculation_saved
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
