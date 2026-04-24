# AI Content & Command Center Bot (Telegram)

## Related
- [[agent-memory]]
- [[current-focus]]
- [[projects/linkedin-automation]]

---

## Goal
Централизованный AI Telegram бот для управления всей автоматизацией с телефона:
- Запуск любого воркфлоу голосом/текстом
- Topic Discovery из множества источников
- AI генерация постов + визуала
- Публикация на LinkedIn, X, Threads
- Отчёты по всем таблицам
- Интеграция с существующим LinkedIn Outreach (WF-00..WF-05)

## Stack
- **n8n** — оркестратор всех воркфлоу
- **Telegram Bot** — FlowOpsBot (@FlowOpstg_bot) — единственный UI
- **Claude (Anthropic)** — AI роутер + генерация контента + принятие решений
- **Google Sheets** — база данных (Posts, Stats, Topics + существующие Leads/Queue)
- **Unsplash API** — stock фото (бесплатно)
- **Pexels API** — stock фото fallback (бесплатно)
- **DALL-E 3 / Flux (Replicate)** — AI генерация изображений (~$0.04/img)
- **Buffer** — публикация на все платформы (LinkedIn + X + Threads) через один API
  - API key: `90ofhUZVEdo_z5oOa60G3yd-CYTus7JQ8UZDIGr3b9W`
  - MCP endpoint: `https://mcp.buffer.com/mcp` (HTTP Streamable, Bearer Auth)
  - Все соцсети уже подключены в Buffer ✅
  - В n8n использовать: MCP Client node
- **Apify** — Twitter trending scraping (~$5/мес)
- **Reddit Public API** — без авторизации, JSON endpoints
- **Hacker News API** — публичный, бесплатно
- **Product Hunt GraphQL API** — бесплатный tier
- **RSS Read node** — TechCrunch AI, VentureBeat, The Verge, MIT Tech Review

## Параметры контента
- **Язык:** английский
- **Тон:** живой, личный, от первого лица
- **Ниша:** автоматизация бизнеса, AI новости, максимум пользы из AI, собственные кейсы
- **Частота:** каждый день
- **Платформы:** LinkedIn + X/Twitter + Threads (Instagram — в будущем)
- **Одобрение:** всегда ручное перед публикацией

## Логика изображений (Claude решает сам)
```
Личный кейс/опыт     → DALL-E 3 / Flux (уникальный визуал)
Новость/статья       → OG-изображение из источника
Статистика/данные    → Графическая карточка
Совет/tips           → Unsplash/Pexels stock фото
Мнение/мысль         → Stock фото или AI генерация
```
Пользователь видит результат → одобряет или просит переделать.

## Subreddits для мониторинга
r/artificial, r/ChatGPT, r/MachineLearning, r/automation, r/AINews, r/n8n, r/SideProject, r/Entrepreneur

## Этапы разработки
1. **Этап 1 — AI Router (фундамент)** — Telegram trigger → Claude определяет намерение → роутит к нужному WF
2. **Этап 2 — Topic Discovery** — скрапинг Reddit/HN/ProductHunt/RSS каждое утро в 07:00
3. **Этап 3 — Content Generation + Approval** — выбор темы → генерация постов + визуала → одобрение
4. **Этап 4 — Publishing** — LinkedIn + X + Threads одновременно
5. **Этап 5 — Stats Collection** — автосбор метрик из API платформ
6. **Этап 6 — Outreach интеграция** — подключение WF-00..WF-05 в бот

## Воркфлоу план
| WF | Название | Триггер |
|---|---|---|
| WF-06 | AI Router (Command Center) | Telegram любое сообщение |
| WF-07 | Topic Discovery | Каждый день 07:00 |
| WF-08 | Morning Briefing | 08:00 — топ-5 тем в Telegram |
| WF-09 | Content Generation | Telegram (выбор темы или своя) |
| WF-10 | Post Approval | Telegram callback |
| WF-11 | Publishing | После одобрения |
| WF-12 | Stats Collection | Каждый день 20:00 |
| WF-13 | Outreach Control | Telegram команды |

## Google Sheets — новые листы
- **Posts:** post_id, date, topic, source, linkedin_text, twitter_text, threads_text, image_url, image_type, status, scheduled_at, published_at
- **Stats:** date, platform, post_id, likes, comments, shares, impressions
- **Topics:** date, source, headline, url, status (selected/rejected/pending)

## Стоимость доп. сервисов
- Apify (Twitter scraping): ~$5/мес
- DALL-E 3: ~$0.04/изображение
- Все остальные API: бесплатно

## Stack уточнения
- **GPT-4O (OpenAI)** — используется для генерации контента (WF-09), credential ID: `6Te8klWgg2iLJPap`, name: "OpenAI account"
- Anthropic/Claude — для WF-06 роутера (нода `n8n-nodes-base.anthropic` есть, но нужно выставить credential)

## Статус (2026-04-24)
- WF-07 Topic Discovery ✅ (построен, импортирован)
- WF-08 Morning Briefing ✅ (построен, импортирован)
- WF-09 Content Generation ✅ (построен + улучшен: Fetch Article + OpenAI GPT-4O)
- WF-10 Post Approval ✅ (построен)
- WF-11 Publishing ✅ (построен, Buffer API)
- WF-06 ⏳ нужно перестроить как настоящий оркестратор после готовности всех WF

## WF-06 — что должен делать (оркестратор)
Классифицирует намерение из Telegram → роутит к нужному WF:

| Intent | Действие WF-06 | Вызывает |
|---|---|---|
| `create_post` | Извлекает topic из сообщения | WF-09 с `{topic, source_url, chat_id}` |
| `approve_post` | Извлекает post_id | WF-10 с `{action:'approve', post_id, chat_id}` |
| `skip_post` | Извлекает post_id | WF-10 с `{action:'skip', post_id, chat_id}` |
| `show_post` | — | WF-10 с `{action:'show', chat_id}` |
| `topics` | Читает Topics sheet | Показывает топ-5 pending тем |
| `queue` | Читает Queue sheet | Показывает pending лиды |
| `outreach_stats` | Читает Queue sheet | Считает sent/pending/skip |
| `run_discovery` | — | executeWorkflow WF-00 |
| `post_stats` | Читает Posts sheet | Показывает published посты |
| `unknown` | — | Инструкция как пользоваться |

## WF-09 — входные данные (от WF-06)
```json
{ "topic": "string", "source_url": "string (опционально)", "chat_id": "string" }
```

## WF-10 — входные данные (от WF-06)
```json
{ "action": "approve|skip|show", "post_id": "string (для approve/skip)", "chat_id": "string" }
```

## Next Steps
1. Создать Topics sheet и Posts sheet в Google Sheets
2. Добавить Unsplash API key в WF-09
3. Добавить Anthropic API key в WF-09 (или уже есть OpenAI)
4. Перестроить WF-06 как оркестратор с executeWorkflow вызовами к WF-09/10
5. WF-12 Stats Collection (последний)
