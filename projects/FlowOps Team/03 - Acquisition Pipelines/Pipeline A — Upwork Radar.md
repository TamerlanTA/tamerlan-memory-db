# 📡 Pipeline A — Upwork Hot Lead Radar

#flowops #pipeline #upwork

> Цель: 50–100 качественных откликов в неделю на самые горячие заказы.

---

## Логика работы

Каждые 15–30 минут система проверяет новые jobs на Upwork → фильтрует мусор → считает fit score → генерирует proposal draft → отправляет топ в Telegram → сохраняет в базу.

---

## Ключевые Keywords для мониторинга

**Automation tools:**
- n8n, Make.com, Zapier
- AI automation, AI agent, workflow automation
- CRM automation

**Data & ops:**
- Airtable, ClickUp, Notion
- OpenAI API, Claude API

**Voice & chat:**
- Vapi, Retell
- Chatbot, WhatsApp automation

**E-commerce:**
- Shopify automation

---

## Fit Score — Критерии оценки

| Критерий | Вес |
|----------|-----|
| Бюджет $300+ | Высокий |
| Конкретная бизнес-проблема описана | Высокий |
| Упоминаются CRM / API / webhooks | Средний |
| Похоже на наши кейсы | Высокий |
| Мало proposals (< 10) | Средний |
| Payment verified | Средний |
| НЕТ охоты на дешёвого исполнителя | Высокий |
| Retainer potential | Высокий |

**Фильтровать в мусор если:**
- Бюджет < $100
- "Looking for cheapest"
- Слишком размыто без конкретной проблемы
- Ищут full-time сотрудника

---

## Структура записи в базе

| Поле | Описание |
|------|----------|
| Job URL | Ссылка на заказ |
| Budget | Бюджет клиента |
| Client info | Рейтинг, страна, история |
| Pain summary | Краткое описание боли |
| Fit score | 1–10 |
| Recommended offer | Какой оффер предложить |
| Proposal draft | Готовый черновик |
| Smart questions | Уточняющие вопросы |
| Status | new / sent / replied / won / lost |
| Follow-up date | Дата следующего касания |

---

## Структура хорошего Proposal

1. **Открытие** — показать, что понял боль клиента
2. **Один конкретный инсайт** — что мы увидели, чего не написали другие
3. **Как решим** — коротко workflow
4. **Похожий кейс** — "I built something similar for..."
5. **Призыв к действию** — "Happy to send a quick Loom showing how this would work?"

---

## Связанные страницы

- [[Sales Steps]] — что делать после ответа
- [[Message Templates]] — шаблоны proposals
- [[Speed-to-Lead System]] — основной оффер для Upwork
- [[Ops Automation Sprint]] — второй популярный оффер
- [[Pipeline D — Demo Library]] — демо для proposals
- [[What to Do First]] — приоритет этого пайплайна

---

*#flowops #pipeline #upwork*
