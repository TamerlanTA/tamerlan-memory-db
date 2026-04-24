# Firecrawl

## Related
- [[agent-memory]]
- [[projects/ai-content-bot]]

## API ключ (Tamerlan)
`fc-031e679123db4ddcba40f963ea4a0970`

## Что это
Firecrawl — сервис и open-source инструмент для **веб-скрапинга и краулинга**, оптимизированный под подачу данных в LLM.

Сайт: https://firecrawl.dev
GitHub: https://github.com/mendableai/firecrawl

---

## n8n нода

**Пакет:** `@mendable/n8n-nodes-firecrawl`
**Node type:** `@mendable/n8n-nodes-firecrawl.firecrawl`
**TypeVersion:** 1
**Credential type:** `firecrawlApi` (поля: `apiKey`, `baseUrl`)
**Base URL по умолчанию:** `https://api.firecrawl.dev/v2`

### Важно: Reddit заблокирован Firecrawl
Firecrawl явно блокирует Reddit (`"We do not support this site"`). Для Reddit использовать RSS-фиды.

---

## Операции (4 ресурса)

### 1. Scraping → `/scrape`
Скрапинг одной страницы → markdown/HTML/screenshot.

**Параметры:**
- `url` — URL страницы
- `formats` — список форматов (`markdown`, `html`, `screenshot`)
- `useCustomBody: true` + `customBody` — для передачи полного JSON тела

**Пример customBody:**
```json
{"url": "https://example.com", "formats": [{"type": "markdown"}]}
```

**Ответ:** `$json.data.markdown` — контент страницы

**Цена:** ~1 кредит/страница

---

### 2. MapSearch → `/search` ⭐ ГЛАВНЫЙ ИНСТРУМЕНТ
Веб-поиск + немедленный скрапинг результатов. Аналог Google Search + Firecrawl в одном.

**Параметры:**
- `query` — поисковый запрос (natural language)
- `sources` — `web`, `news`, `images` (можно несколько)
- `tbs` — фильтр по времени:
  - `qdr:h` — последний час
  - `qdr:d` — последние 24 часа ← **использовать для ежедневного discovery**
  - `qdr:w` — последняя неделя
- `limit` — количество результатов (default: 5)
- `timeout` — таймаут в мс (default: 60000)

**Пример параметров ноды:**
```
resource: MapSearch
operation: search
query: "AI automation tools news"
sources: [news]
tbs: qdr:d
limit: 5
```

**Ответ:** массив items, каждый с полями:
- `$json.url` — URL статьи
- `$json.title` — заголовок
- `$json.markdown` — полный контент страницы
- `$json.description` — meta description

**Normalize код:**
```javascript
const today = new Date().toISOString().split('T')[0];
const title = $json.title || $json.description || '';
const url = $json.url || '';
if (!title || !url) return [];
return [{ json: { date: today, source: 'Firecrawl/Search', headline: title, url, score: 0, status: 'pending' } }];
```

**Цена:** ~1 кредит/результат (поиск на 5 результатов = ~5 кредитов)

---

### 3. MapSearch → `/map`
Возвращает все URL сайта (sitemap + link discovery). Не подходит для daily news.

**Использование:** разовая разведка структуры сайта.

---

### 4. Crawling → `/crawl`
Рекурсивный краулинг всего сайта. Асинхронный, дорогой.

**Использование:** не использовать для daily workflows, только для разовой индексации.

---

### 5. Agent → `/agent`
AI-агент с natural language промптом, сам навигирует по сети.

**Использование:** дорогой, для сложных extraction задач. Не для daily news.

---

### 6. Extract (через API, не в UI ноде)
Structured data extraction с JSON Schema через LLM.

**Использование:** извлечение структурированных данных из конкретных страниц.

---

## Кредиты

| Тариф | Кредиты/мес | Цена |
|---|---|---|
| Free | 500 | $0 |
| Hobby | 3 000 | $16 |
| Standard | 100 000 | $83 |

**Бюджет для WF-07 (daily, Free tier):**
- 500 кредитов / 30 дней = **~16 кредитов/день**
- 2 Search-запроса × 5 результатов = 10 кредитов
- 2 Scrape-страницы = 2 кредита
- Итого: ~12 кредитов/день ✅ вписывается в Free

---

## Оптимальная стратегия для WF-07 (Topic Discovery)

### Что использовать Firecrawl:
| Источник | Операция | Запрос/URL |
|---|---|---|
| AI новости общие | `/search` news, qdr:d | `"AI tools automation news today"` |
| Модели и релизы | `/search` news, qdr:d | `"LLM model OpenAI Anthropic release"` |
| TLDR AI | `/scrape` | `https://tldr.tech/ai` |
| Product Hunt AI | `/scrape` | `https://www.producthunt.com/topics/artificial-intelligence` |

### Что использовать RSS (бесплатно, без лимитов):
| Источник | RSS URL |
|---|---|
| HackerNews | Algolia API (уже есть) |
| TechCrunch AI | `https://techcrunch.com/category/artificial-intelligence/feed/` |
| VentureBeat AI | `https://venturebeat.com/ai/feed/` |
| OpenAI Blog | `https://openai.com/blog/rss.xml` |
| Anthropic News | `https://www.anthropic.com/rss.xml` |
| Hugging Face Papers | `https://huggingface.co/papers.rss` |
| Reddit r/ChatGPT | `https://www.reddit.com/r/ChatGPT/top.rss?t=day&limit=10` |
| Reddit r/LocalLLaMA | `https://www.reddit.com/r/LocalLLaMA/top.rss?t=day&limit=10` |
| Reddit r/ClaudeAI | `https://www.reddit.com/r/ClaudeAI/top.rss?t=day&limit=10` |

---

## Интеграции
- REST API + SDKs: Python, Node.js
- Готовые интеграции: **n8n** (`@mendable/n8n-nodes-firecrawl`), LangChain, LlamaIndex
- MCP-сервер для Claude

## Заметки
- Self-hosted вариант требует Redis + Playwright
- Для большинства задач автоматизации хватает Free или Hobby плана
- Хорошо комбинируется с Supabase и OpenAI/Claude
