# Make-David — Risks & Blockers

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

---

## Phase 2 Active Risks

### 🔴 HIGH: SellerChat не умеет передавать exact user input
**Risk:** SellerChat bot flow может не поддерживать capture точного текста пользователя и передачу в webhook.
**Impact:** Вся предложенная архитектура невалидна — нужен другой подход.
**Mitigation:** Проверить SellerChat UI/docs первым делом. Если не поддерживает — рассмотреть альтернативы (polling SellerChat API, fallback на n8n WhatsApp trigger).

### 🟡 MEDIUM: sub-scrape триггерится как sub-workflow, не через webhook
**Risk:** Сейчас sub-scrape.json вызывается внутри основного n8n workflow через internal trigger, не через внешний HTTP endpoint.
**Impact:** Make не сможет вызвать его напрямую без добавления webhook trigger.
**Mitigation:** Добавить webhook trigger в sub-scrape или создать bridge workflow.

### 🟡 MEDIUM: Anti-bot защита на scraped сайтах
**Risk:** SIMIT и другие сайты могут блокировать скрапер (captcha, rate limits, IP ban).
**Impact:** Скрапер перестаёт работать — пользователь получает ошибку.
**Mitigation:** Существующий скрапер, вероятно, уже решал это — уточнить текущий статус у David.

### 🟡 MEDIUM: SellerChat API для отправки ответа
**Risk:** Нужно понять как Make отправляет сообщение обратно в конкретный SellerChat conversation.
**Impact:** Без этого ответ не вернётся пользователю.
**Mitigation:** Проверить SellerChat API docs / Make SellerChat module capabilities.

### 🟢 LOW: Latency (скрапер медленный)
**Risk:** Скрапинг может занять 10-30 сек, пользователь видит задержку.
**Impact:** Плохой UX.
**Mitigation:** Отправить "Procesando, espera un momento..." сразу при получении запроса, до вызова скрапера.

---

## Phase 1 Resolved Risks
- ✅ Make.com scenario создан и работает
- ✅ n8n workflows развёрнуты
- ✅ SellerChat интеграция настроена для 3 профилей
