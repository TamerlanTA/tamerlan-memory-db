# ImportCar.kz MVP — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]
- [[roadmap]]

---

## ЗАВЕРШЕНО: v0.1 — Production Calculator ✅

Все 8 задач выполнены. Калькулятор работает в production-режиме с полным UI.
**Требует**: запустить schema migration в Supabase dashboard перед production-использованием calculator lead form.

---

## СЛЕДУЮЩИЙ БЛОК: Immediate fixes + v0.3

Это следующий обязательный этап. До него не строим подписки, аккаунты, App Store.

### Задачи (в порядке приоритета)

1. **CalculatorScreen v2** — перестроить как главный экран приложения
   - Итог в тенге = главное число (крупно, сверху)
   - Ниже: ≈ USD
   - Полная разбивка: авто / доставка / таможня / утильсбор / регистрация / комиссия / резерв расходов
   - Trust-индикатор точности + disclaimer ("расчёт предварительный, не оферта")

2. **Explainability блок** — блок "Как рассчитана стоимость"
   - Возраст авто, объём двигателя, таможенная категория
   - Версия правил, курс валют, дата обновления
   - Предупреждения

3. **CTA после каждого расчёта**
   - Получить точный расчёт
   - Проверить авто по ссылке
   - Написать в WhatsApp
   - Сохранить расчёт

4. **Lead form с calculation snapshot**
   - Поля: имя / телефон / город / ссылка на авто / комментарий
   - В заявку сохраняется весь snapshot: страна, цена, год, двигатель, топливо, город, итог, разбивка, версия правил, дата расчёта
   - Менеджер видит контекст без уточнений у клиента

5. **Таблица `calculations` в Supabase**
   - Схема: см. roadmap.md
   - Сохранять каждый расчёт (анонимный — user_id NULL)

6. **Admin leads view** — показывать snapshot расчёта рядом с контактами

7. **Analytics events**
   - `calculator_opened`, `calculation_completed`, `lead_submitted`, `whatsapp_clicked`

8. **Legal disclaimers** — на экране калькулятора и в форме заявки

---

## После v0.1 (следующие блоки по roadmap)

- **v0.3** — Supabase Auth: Phone OTP + Google + Apple. Аккаунт запрашивать только при сохранении / заявке
- **v0.4** — Real Inventory: 30 качественных реальных листингов, честные лейблы
- **v0.5** — Payments: Kaspi/Halyk, платный точный расчёт от 1 990 ₸, VIN-проверка
- **v0.6** — Subscriptions: Free / Plus план
- **v0.7** — Importer Partner Layer: B2B монетизация
- **v0.8** — Native App (Capacitor): iOS/Android билды
- **v1.0** — App Store / Google Play публичный релиз

Детали каждого этапа — в [[roadmap]].

---

## Immediate fixes (не зависят от этапа)

- Заменить placeholder WhatsApp `77071234567` в `StickyCta.tsx` и `ProfileScreen.tsx` на реальный номер
- Добавить desktop top-nav для табов (Calculator/Favorites/Profile недоступны с десктопа)
- Деплой на Vercel после финального теста на реальном iPhone
