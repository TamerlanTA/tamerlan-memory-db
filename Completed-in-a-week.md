Здесь я записываю то что было выполнено за прошедшую неделю
этот файл будет обновляться каждое воскресенье ночью
## Related
- [[My-tasks]]
- [[agent-memory]]

---

# Неделя 12–18 мая 2026

---

## 🔵 FlowOps — Pipeline C v3 (12–13 мая)

Полный апгрейд автоматизации холодного outreach:

**Auto-Send Scale** — пайплайн теперь запускает 40–120 рандомизированных запросов, собирает до 300 кандидатов, отправляет cold email автоматически — без ручного одобрения в Telegram.

**Mass Personalized Sender** — OpenAI генерирует персональное письмо под каждый сайт: приветствие от Тамерлана, конкретная проблема сайта, оффер FlowOps. Фильтрация по качеству убрана — письма идут всем.

**Batch Gate + Rate Limit Fix** — добавлен поэтапный throttle после реального `RATE_LIMIT_REACHED` на 35-м лиде. Пакеты по 10–30, задержка 5 мин между пачками, 15 сек между записями. Retry/backoff на Airtable (10 попыток), Gmail, OpenAI.

---

## 🔵 FlowOps — Лиды и Проспекты (11–14 мая)

- **10 Almaty-проспектов** (11 мая) — клиники, стоматологии, ремонт. Telegram-ready список с болью и оффер-углом.
- **30 Almaty-проспектов** (13 мая) — смешанные ниши: медицина, детсады, автосервис, ивенты, фитнес, ветклиника.
- **30 Almaty-лидов с оценками** (14 мая) — создан артефакт `Almaty 30 Leads — 2026-05-14.md` со скором, сигналом и оффер-углом для каждой компании.

---

## 🔵 FlowOps — Продажи и КП (14–17 мая)

**Almaty Business Audit Proposal** — создан Codex-скилл, который по публичным данным компании генерирует аудит, Fit Score, Loom-скрипт и полноценное КП.

**КП для Medstyle.kz** — аудит сайта, оффер на WhatsApp AI-ассистент: квалификация, запись, напоминания, aftercare. PDF 11 слайдов, цена 300 000 ₸, срок 1–2 недели.

**Offer Decks — итоговая версия:**
- AI Sales Operating Systems (EN) — первая версия deck
- Bilingual EN+RU Company Deck — одна презентация с двумя языками
- Раздельные EN + RU deck с коммерческой моделью: 300 лидов/мес, экономия 40 ч/мес, +6–12 звонков/мес. Цены: EN от $3 000, RU от 1.5 млн ₸.

---

## 🟠 ProAlp Site — с нуля до MVP (12–14 мая)

**Bootstrap (12 мая)** — Next.js 14 + TypeScript + Tailwind, структура проекта, 10 stub-секций, ru-RU мета.

**Cinematic MVP (12 мая)** — dark premium B2B: анимированное SVG-здание (14 этажей, мигающие окна, альпинист на верёвке), 11 секций полностью на русском, рабочий квиз (5 шагов + валидация + success state), секции Services / Safety / Cases / AI Pipeline / CRM Preview. Build: ✓ 46.9 kB.

**Hero Polish (14 мая)** — заголовок не обрезается на мобиле, CTA ведут на `#quiz` и `#cases`, добавлен reduced-motion.

---

## 🟢 ImportCar.kz MVP (16 мая)

Большой рабочий день по проекту:

- **Реальные фото** — 12 машин с Wikimedia Commons, overlay-атрибуция на карточках
- **Реальные листинги Encar** — 15 люксовых авто с реального API (BMW X7, Mercedes GLS, AMG G63, Porsche Cayenne, Lexus RX 450h+ и др.), реальные цены в ₩
- **Полная русификация** — весь английский убран: карточки, детали, FAQ, форма, калькулятор, CTA
- **Supervisor Audit** — полный аудит кода, 4 открытых бага зафиксированы, TypeScript 0 ошибок
- **Promote Memory** — проект переведён из одного файла в полную canonical memory-структуру
- **3 деплоя на Vercel** — production обновлён после каждого этапа

---

## 🟡 AI-Powered Woven Label Generator (11 мая)

**MOQ 1000 hotfix** — исправление минимальной партии (убрана опция 500 шт.) перенесено на активную ветку `milestone4-auth-completion` без затрагивания Stripe, DB и AI-генерации.

---

## ⏳ Перенесено на следующую неделю

- Импорт Pipeline C v3 в n8n и первый live-тест auto-send
- CRM QA / automation-readiness review
- Первые 5 Demo Library Loom-активов
- Доделать мелкие баги ImportCar.kz (ImporterCard Details, AuctionSheet, валидация телефона)
- Адаптировать offer decks под конкретные ниши (клиники, недвижимость, агентства)

---

*Сгенерировано автоматически · воскресенье 18 мая 2026*

---

# Неделя 5–11 мая 2026

---

## 🤖 Пайплайны и автоматизация

### Pipeline B — LinkedIn Pain Radar — Дедупликация ✔
Исправлена главная проблема: пайплайн возвращал одних и тех же 5 лидов и спамил Telegram при каждом запуске. Добавлена Airtable-дедупликация, которая сохраняется между запусками (по Contact URL, LinkedIn URL и Unique key). Поиск расширен с 5 до 20+ результатов на запрос (до 80 кандидатов за запуск). Hotfix: исправлена невалидная формула в Airtable-узле.

### Pipeline C — Website Audit Generator v2 ✔ → v2.1.3
Подтверждён как операционно завершённый (запуск через Telegram: `/pipeline_c`, `/audit_sites`). Обновлён до v2.1: 24 рандомизированных запроса, 120 уникальных доменов, до 60 новых сайтов/запуск. Исправлены: rate-limit Airtable при больших батчах (→ batch dedupe), потеря кандидатов после `Parse Dedupe Result`, обрезанный JSON при 120 кандидатах. В холодные письма добавлены профильные ссылки (Website / LinkedIn / Upwork).

### Pipeline C Praha — новый проект ✔ (проспектинг готов)
Построен отдельный пайплайн для пражского рынка поверх архитектуры v2. Основные итерации: замена HTTP-метода Firecrawl (POST→GET hotfix), переход на официальный Firecrawl-узел, фикс Normalize-ноды (нет output → исправлено), добавлен Prague Locality Gate, убраны Google Sheets из основного потока (заменены на `Prepare Audit Queue Rows`). Добавлены Enrichment-ноды (Firecrawl + OpenAI). Локальный тест 30 items: Normalize → Locality → Dedupe → Rows — всё проходит.

---

## 📞 AI Caller — n8n (Vapi)

Построены два n8n workflow для исходящих звонков:
- **WF-01 Start Outbound Call** — Ручной запуск → Airtable (фильтр `Ready to call`) → Vapi HTTP вызов → статус-обновление записи.
- **WF-02 Receive Call Result** — Vapi webhook → нормализация → rule-based классификация (interested / no answer / not interested) → Airtable lookup по Call ID → обновление.

Hotfix: Vapi-ассистент `Alex` слал десятки webhook-событий на каждый звонок → исчерпывал n8n Cloud executions. Ограничено до `serverMessages: ["end-of-call-report"]`. Оба workflow валидны (`valid: true`, 0 ошибок).

---

## 🏥 FlowOps Стратегия — Healthcare Wedge

Проведён анализ ниш через метод `unfairgaps`. Лучший near-term wedge: **HIPAA-Safe Intake + Follow-up Cleanup Sprint** для небольших US медицинских/wellness-практик (free audit → paid sprint $1.5–4K). Создан полный бэклог из 7 ниш (Med Spa, Lead Consent, ADA Website, OSHA Safety, Auto Dealer, AI Hiring, Subscription Cancellation). Для Med Spa готов: prompt spec (6-dimension scoring 0–20), 28 JSON-полей, email wrapper, Telegram review card, Airtable field mapping, GTM Strategy Tracker.

---

## 🛠️ FlowOps Opportunity Engine — Codex Skill

Создан новый Codex skill `/Users/tamerlan/.codex/skills/flowops-opportunity-engine/` для trigger-based проспектинга. Включает: таксономию сигналов, scoring rubric, формат audit brief, паттерны outreach, compliance-гарды. Правило: не использовать Upwork и другие фриланс-платформы (для них отдельный Pipeline A).

---

## 🏷️ Griffes Vivienne — AI Label Generator

| Задача | Результат |
|---|---|
| MOQ 500 → 1000 | Изменено в коде, тестах и UI |
| 500 при генерации (R2 missing) | Hotfix: graceful fallback `inline://` вместо throw; re-download вернёт NOT_FOUND пока R2 не настроен |
| Freemium gate → generic error | Исправлено: `GUEST_FREE_TRIAL_EXHAUSTED` → кнопка "Sign up" |
| 25×25 генерировался горизонтально | Исправлен промпт — HD Cotton больше не форсирует long horizontal |

Все тесты и билд: PASS ✅ Коммиты: `35faedc`, `ab9b86c`, `5e54191`, `a8a8e5a`.

---

## 📋 Linear / FLO-48 — Message-Match Audit

Выполнен Week-1 UX audit выходящих outreach-вариантов. Найдены 3 failure: нечёткий CTA Day-1, смешанный sync/async intent, несогласованная метрика proof. Созданы child issues FLO-50 (CTO), FLO-51 (CMO), FLO-52 (UXDesigner) с explicit acceptance criteria.

---

## ⏳ Перенесено на следующую неделю

- Pipeline C: импорт v2.1.3 в n8n, первый batch по Med Spa (Miami / Scottsdale / Austin)
- Pipeline C Praha: добавить Google Sheets после подтверждения output rows
- AI Caller: первый live-тест после сброса n8n Cloud quota
- FLO-50/51/52: внедрение и повторный audit FLO-48
- R2 credentials: добавить в Vercel production (блокирует persistent storage у Griffes Vivienne)

---

*Обновлено автоматически — воскресенье 11 мая 2026*

---

# Неделя 28 апреля — 4 мая 2026

---

## 🤖 Пайплайны и автоматизация

### Pipeline A — Upwork Radar
Собран полный n8n workflow JSON (`upwork-radar-workflow.json`):
Gmail trigger → парсинг URL → дедупликация Google Sheets → Firecrawl scrape → OpenAI скоринг → генерация + валидация предложения → Telegram → запись в Sheets. Добавлен Quiet Hours Gate (02:00–09:00 Almaty). Несколько итераций по формату предложения и валидатору.

### Pipeline B — LinkedIn Pain Radar ✔ ЗАВЕРШЁН
Создан и готов n8n workflow JSON (`pipeline-b-linkedin-pain-radar-crm-workflow.json`): Firecrawl поиск → OpenAI квалификация → скор-гейт → черновик DM → Airtable CRM → Telegram review. Помечен как **готов к операционному использованию**.

### Pipeline C — Website Audit Generator (v1 + v2)
- **v1:** workflow-шаблон + runbook — первичный draft.
- **v2:** разбит на 3 workflow (Prospecting, Audit Queue, Approval Handler) + WF-06 router patch. Прошёл 4 итерации фикса нормализации URL Firecrawl. Gmail-отправка переведена на нативный n8n Gmail-узел. Все 24 Code-ноды валидированы без синтаксических ошибок.
> Статус: import-ready, операционно не завершён (нужен импорт в n8n и первый QA batch).

---

## 🗂 CRM

Airtable CRM FlowOps **создана** (подтверждено). Оформлены `Airtable CRM Build Spec.md` и `CRM Automation Plan.md` — таблицы, поля, view-ы, seed-записи и план автоматизаций.

---

## 📋 Linear — миграция задач

- Создано **18 labels**, **8 проектов** (FlowOps OS, Demo Library, Upwork Radar, CRM, Website Audit Generator, LinkedIn Pain Radar, Sales Assets, Retainer Conversion).
- Создано **issues FLO-5 → FLO-24** с полным контекстом, шагами и acceptance criteria.
- FLO-1–FLO-4 закрыты как onboarding-плейсхолдеры.

---

## 👥 Команда

| Кто | Что назначено |
|---|---|
| **Aslanbek** | Speed-to-Lead MVP в n8n (TASK-2026-04-30-002 / FLO-17) |
| **Adil** | FlowOps documentation kit — КП, аудит, кейсы, портфолио, onboarding (FLO-16) |
| Шаблоны | Созданы папки active-tasks / completed / next-task для всех трёх участников |

---

## 🔔 Team Task Notifier (n8n)

Собран workflow для Telegram-уведомлений о новых задачах команды из GitHub/Obsidian-папок. Версии v1→v4: авто-бутстрап при первом запуске, фильтр template-файлов, корректный формат Telegram-сообщений.

---

## 📊 Продажи / Контент

Подготовлена PPTX-презентация для клиента: **AI-система для YouTube Shorts** (Nate Friedman-style). Фреймворк: MVP $1.5–2.5K → Production $4–7K → Autonomous $8–15K.

---

## ⏳ Ещё не закрыто (перенесено на следующую неделю)

- CRM QA / automation-readiness — не сделан
- Pipeline C: импорт v2 в n8n, первый QA batch, первые реальные аудиты
- Upwork Radar: импорт в n8n, reconnect, первый тест
- Alexey: профиль роли не заполнен, задачи не назначены

---

*Обновлено автоматически — воскресенье 4 мая 2026*

---

# Неделя 21–27 апреля 2026

---

## 🏷️ Griffes Vivienne — AI Label Generator

### Безопасность и баги (21 апр)
- Исправлен баг безопасности: `previewImageUrl` теперь принимает только `https://` URL — закрыта инъекция в письма
- Исправлена двойная генерация при back/forward навигации — кредит больше не списывается дважды
- Выровнен дефолт `logoType`: клиент и сервер теперь оба используют `SYMBOL_ONLY`
- Добавлена типизированная система ошибок генерации — пользователь не видит технические сообщения провайдера

### UI / Коммерция (21–22 апр)
- Переработан `/sign-in` в брендированную страницу Griffes Vivienne с FR/EN локализацией
- Исправлен предпросмотр: белые логотипы больше не теряются на белом фоне
- Flow переименован: "Order" → "Request a quote" во всём интерфейсе и письмах
- В письма-квоты добавлены реальные цены из прайс-листа; стоимость сэмпла (€320/€380) с пометкой «100% зачисляется в производство»
- Добавлен формат `20 x 50 mm + fold` и текст времени ожидания на loading-экране

### Юридические страницы (21 апр)
- Добавлены `/terms`, `/privacy`, `/legal`, `/faq` с полным FR/EN контентом
- Интегрированы официальные данные компании (SIRET, адрес, хостинг) из клиентского документа
- Все тексты приведены в соответствие с реальной логикой приложения (guest-first, quote flow)

### Качество генерации (23–24 апр)
- Исправлена обработка фото продуктов: промпт изолирует логотип, игнорирует одежду/фон
- Исправлена регрессия «wave/swirl» — фон этикетки снова выглядит ровно и премиально
- Добавлен hardening по всем материалам (HD, Cotton, Satin, Taffeta)
- Восстановлен баланс: явные логотипы → строгая fidelity, `AUTO` → conditional isolation

### SEO и деплой (24 апр)
- Установлен `react-helmet-async`, добавлены title/meta/OG для всех ключевых страниц
- Добавлен `FAQPage` JSON-LD и `Organization` JSON-LD; расширены ответы FAQ (15 вопросов)
- Обнаружен забытый push — ветка синхронизирована, Vercel задеплоил актуальный коммит

---

## 🤖 AI Content Bot (n8n / FlowOps)

### Архитектура (24–25 апр)
- WF-06 перестроен: AI-agent-only → детерминированный роутер + AI как fallback
- `создай пост`, `approve`, `skip` теперь идут напрямую, минуя LLM
- Разделены `briefing` (читать топики) и `discovery` (обновлять) — были перепутаны
- Полный JSON-аудит всех WF-00–WF-12: дедупликация, broken links, плейсхолдеры

### Buffer и публикация (25 апр)
- Переход с Buffer REST API на GraphQL; получены реальные channel IDs (LinkedIn, X, Threads)
- Исправлен `ShareMode`: `"now"` → `"shareNow"`
- Убраны все `$env`-ссылки из WF-11 (n8n Cloud их блокировал)
- Исправлен routing кнопок: approve/skip теперь передают `{action, post_id, chat_id}`, не `{ok, result}`

### Изображения (26 апр)
- Добавлен Cloudinary upload в WF-09 — Gemini-изображение получает публичный URL для Buffer
- Промпт обновлён: от пустых карточек к «save-worthy» инфографике (4:5, заголовок, буллеты, тёплый стиль)

---

## 💼 Бизнес / Личное

- Создал консультацию и проект на Upwork
- Созвонился с Алдияром — согласован план автоматизации на **1 700 000 тг**
- Получена оплата за **Milestone 5** (Griffes Vivienne)
- Заполнен LinkedIn-профиль, изучен Claude Design
- Сделан overview-видео и редизайн сайта FlowOps

---

*Обновлено автоматически — воскресенье 27 апреля 2026*

---

# Неделя 14–20 апреля 2026

---

## 🏷️ Griffes Vivienne — AI Label Generator

### Конверсия и UX-полировка (15 апр)
- Реализован email capture для гостей на границе заказа
- Добавлен реальный логотип бренда (PNG, без CSS-фильтров)
- Исправлен баг logout в `Account.tsx` (Clerk-токен не инвалидировался)
- Добавлены FR/EN переводы для всех новых строк

### Email подтверждения предзаказа (15–16 апр)
- Письмо стало двуязычным (EN/FR) по языку пользователя
- Добавлена миниатюра сгенерированного лейбла в письмо
- Переработан текст: unit-pricing, Reply-To на devis@griffesvivienne.com, CTA-кнопка
- Убран ошибочный `mailto:` CTA (открывал новое письмо, терял контекст треда)
- Все тесты и билд прошли ✅

### Back-office / продажи (17 апр) — 4 батча
- **Батч 1:** Новый таб `Preorders` в `/admin/stats` — список предзаказов с PO-ссылкой, email, статусом письма, поиском
- **Батч 2:** Улучшена вкладка Generations — превью мокапа, контекст клиента и продукта, парсинг `configSnapshotJson`
- **Батч 3:** В БД записана точная связка `generationId → sourceAssetId → resultAssetId` на каждый предзаказ (миграция `0013`)
- **Батч 4:** Оперативное получение логотипа, превью и вектор-ассета прямо из карточки предзаказа (signed URL on-demand)

### Исправление порядка заказа (18 апр)
- Убрано двойное нажатие: CTA на Result теперь сразу создаёт order intent и отправляет на страницу-подтверждение
- `/order-preview` стал экраном «Отправлено» с retry только при ошибке
- Тесты + билд: PASS ✅

### Исправление цвета лейбла (18 апр)
- Найден и исправлен баг цветовой несогласованности: AI получал оригинальный многоцветный логотип вместо одноцветного силуэта
- Loading-экран, конфиг-превью и генерация теперь все используют один и тот же затинтованный логотип
- Тесты: 152/165 PASS (13 ошибок pre-existing, не связаны с фиксом) ✅

### Утечка брендов конкурентов (19 апр)
- Найдена критическая проблема: AI генерировал лейблы с "Chloé Stora", "DIOR", "SAINT LAURENT" из референс-изображений
- Заменены все референс-изображения на текстурные кропы без текста (6 новых файлов)
- Убраны все упоминания брендов из промптов в `moodboards.ts`
- Исправлен баг мобильной загрузки HEIC/HEIF — теперь принимаются только PNG/JPG/WEBP/SVG
- Улучшена видимость белых логотипов в превью (нейтральный фон + тень)

---

## 🤖 Make-David (WhatsApp автоматизация, Колумбия)

- Проведён полный анализ проекта (15 апр): GAS-скрипт готов (553 строки), n8n workflows построены
- Создана документация в `projects/David/` — архитектура, стек, риски, следующие шаги
- Главный блокер: Make.com сценарий ещё не создан в UI → шаблонные сообщения не работают

---

## 🗂️ Память и система (15 апр)

- Полностью переписан `agent-memory.md` — добавлены стек, паттерн мультиагентной системы, конвенции
- Обновлён `current-focus.md` — реальный статус проекта вместо заглушки
- Исправлен `routing-rules.md` — Claude Code добавлен как явная роль
- Добавлена база знаний `knowledge/firecrawl.md`
- Создан приватный GitHub-репозиторий `TamerlanTA/tamerlan-memory-db` для версионирования хранилища
- Реклассификация структуры vault: паттерны → `patterns/`, знания → `knowledge/`, история → `sessions/`
- Созданы шаблоны: `patterns/batch-prompt-template.md`, `prompts/handoff-summary-template.md`

---

*Обновлено автоматически — воскресенье 20 апреля 2026*
