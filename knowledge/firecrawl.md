# Firecrawl

## Related
- [[agent-memory]]

## API ключ (Tamerlan)
`fc-031e679123db4ddcba40f963ea4a0970`

## Что это
Firecrawl — сервис и open-source инструмент для **веб-скрапинга и краулинга**, оптимизированный под подачу данных в LLM.

Сайт: https://firecrawl.dev
GitHub: https://github.com/mendableai/firecrawl

## Ключевые возможности
- **Scrape** — превращает любую веб-страницу в чистый Markdown или структурированный JSON
- **Crawl** — рекурсивно обходит весь сайт и возвращает данные всех страниц
- **Extract** — извлекает структурированные данные по заданной схеме (через LLM)
- **Map** — возвращает карту всех URL сайта
- **Search** — веб-поиск с немедленным преобразованием результатов в Markdown
- Обходит JavaScript-рендеринг (headless browser под капотом)
- Автоматически убирает навигацию, рекламу, футеры — оставляет только контент

## Интеграции
- REST API + SDKs: Python, Node.js
- Готовые интеграции: **n8n**, LangChain, LlamaIndex, CrewAI, Dify, Zapier
- MCP-сервер для Claude (можно подключить как MCP)

## Тарифы (на момент записи)
- Free: 500 кредитов/мес
- Hobby: $16/мес — 3 000 кредитов
- Standard: $83/мес — 100 000 кредитов
- Self-hosted: бесплатно (Docker)

## Где применять в работе
- Сбор данных с сайтов для AI-пайплайнов (n8n + Firecrawl → LLM)
- Мониторинг конкурентов / парсинг каталогов
- RAG: наполнение векторных баз данных контентом сайтов
- Автоматическая генерация датасетов из веб-источников
- Замена ручного копирования контента в промпты

## Быстрый старт (Python)
```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_KEY")

# Одна страница → Markdown
result = app.scrape_url("https://example.com", formats=["markdown"])
print(result["markdown"])

# Весь сайт
crawl = app.crawl_url("https://example.com", limit=50)
```

## Быстрый старт (n8n)
Используй ноду **Firecrawl** (community node) или HTTP Request с API:
- `POST https://api.firecrawl.dev/v1/scrape` — скрапинг одной страницы
- `POST https://api.firecrawl.dev/v1/crawl` — запуск краулинга
- Header: `Authorization: Bearer fc-YOUR_KEY`

## Заметки
- Self-hosted вариант требует Redis + Playwright — чуть сложнее, но бесплатен
- Для большинства задач автоматизации хватает Free или Hobby плана
- Хорошо комбинируется с Supabase (сохранение результатов) и OpenAI/Claude (обработка)
