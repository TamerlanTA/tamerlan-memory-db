# Make-David — Decisions

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[next-steps]]

---

## Architecture Decisions

### 1. Google Apps Script → Make.com → SellerChat (не напрямую)
**Decision:** Apps Script отправляет webhook в Make.com, Make роутит в SellerChat — не напрямую из Script.
**Why:** Make.com даёт надёжный error handling, data store для дедупликации, и retry logic без усложнения Script.

### 2. Один webhook URL для всех профилей
**Decision:** Один webhook endpoint Make.com, профиль передаётся в payload (`profile: "david|lilia|lyan"`).
**Why:** Масштабируемость — добавление нового профиля не требует нового webhook. Роутинг внутри Make.

### 3. Дедупликация через Data Store
**Decision:** Make.com Data Store `sellerchat_sent_templates` хранит `(account + record_id + template)` как ключ.
**Why:** Предотвращает дублирование отправки при повторных срабатываниях trigger.

### 4. Sequential processing в Make.com
**Decision:** Включить sequential processing (один webhook за раз).
**Why:** Предотвращает race conditions при параллельных редактированиях одной строки.

### 5. n8n для AI-бота (не Make)
**Decision:** WhatsApp AI-бот реализован в n8n, не в Make.
**Why:** n8n лучше подходит для сложных AI workflows с Redis, Supabase, и кастомным JavaScript.

### 6. Статические SellerChat connections в Make
**Decision:** Не использовать динамическое переключение SellerChat аккаунта — по одному route на (профиль + шаблон).
**Why:** SellerChat connections в Make не поддерживают динамический выбор. 6 статических routes (3 профиля × 2 шаблона).

### 7. Redis для conversation buffer
**Decision:** Сообщения буферизуются в Redis с debounce (15 сек) перед обработкой AI.
**Why:** Пользователь может отправить несколько сообщений подряд — нужно дождаться паузы и обработать как одно.

### 8. Страна по умолчанию +57 (Колумбия)
**Decision:** Нормализация номеров предполагает колумбийский код (+57), локальный номер = 10 цифр.
**Why:** Клиент работает в Колумбии.
