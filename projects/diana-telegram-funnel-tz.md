# Diana Telegram Job Funnel — ТЗ и коммерческое предложение v0.2

## Related
- [[All about Agents/agent-memory]]
- [[current-focus]]
- [[projects/upwork-auto-response-system]]

## Контекст

- Дата: 2026-06-18.
- Клиентка: Diana Kokhanova, Upwork.
- Исходная вакансия: Telegram Automation & Funnel Developer.
- Ниша клиента: beauty-бизнесы / beauty professionals / beauty job marketplace.
- У клиента уже есть собственная платформа.
- Нужно создать нового Telegram-бота и превратить Telegram в новый канал продаж/привлечения пользователей.

## Понимание задачи

Клиенту нужен не просто Telegram bot, а **Telegram acquisition + assisted onboarding system** для существующей платформы.

Проблема, которую должен решать бот:
- часть потенциальных пользователей не разбирается в платформе;
- часть пользователей ленится проходить регистрацию самостоятельно;
- в общей Telegram-группе появляются вопросы вроде “как найти работу?”;
- нужно автоматически подхватывать таких людей, переводить их в личный диалог с ботом, помогать зарегистрироваться на платформе и затем возвращать им подходящие вакансии.

## Основной сценарий работы бота

### 1. Общая Telegram-группа

У клиента есть общая Telegram-группа/чат, где идут:
- уведомления;
- общение с текущими клиентами;
- общение с новыми клиентами;
- вопросы пользователей;
- общий community/support flow.

Новый бот добавляется в эту группу.

### 2. Бот слушает сообщения в группе

Бот должен отслеживать сообщения и подхватывать выражения/намерения, связанные с поиском работы или регистрацией, например:
- “как найти работу?”
- “как устроиться?”
- “где вакансии?”
- “как зарегистрироваться?”
- “помогите найти работу”
- другие ключевые слова/фразы, которые будут согласованы.

Когда бот видит подходящий триггер, он отвечает в группе примерно так:

> @username, напишите мне в личные сообщения, я помогу вам пройти регистрацию и подобрать вакансии.

Важно: Telegram-бот не может первым написать пользователю в личку, пока пользователь сам не нажмет Start/откроет бота. Поэтому бот должен вести пользователя из группы в личный чат через кнопку или ссылку.

### 3. Личный диалог с ботом

Пользователь открывает бота и активирует его.

Бот пошагово помогает пройти регистрацию:
- объясняет простыми словами, что будет происходить;
- задает все необходимые вопросы;
- помогает заполнить профиль;
- собирает данные для создания аккаунта на платформе;
- использует личную почту пользователя;
- при необходимости валидирует ответы и просит исправить неполные данные.

### 4. Передача данных в платформу

После заполнения анкеты бот отправляет данные:
- напрямую в платформу через API, если API есть;
- или во временную базу / Google Sheets / Airtable / admin queue, если API пока нет;
- или в промежуточный backend, который дальше синхронизируется с платформой.

Ожидаемый результат:
- пользователь зарегистрирован на платформе;
- пользователю выдан временный пароль для личного кабинета;
- команда/платформа получает все данные для дальнейшей верификации.

### 5. Верификация на стороне платформы

После регистрации финальная проверка/верификация проходит уже на стороне клиента/платформы.

Бот на этом этапе должен:
- показать пользователю статус “ваш профиль отправлен на проверку”;
- объяснить, что проверка займет некоторое время;
- при наличии API/status webhook уметь обновлять статус пользователя;
- если API статуса нет, статус может обновляться вручную или через импорт.

### 6. Уведомление о готовом аккаунте

Когда аккаунт полностью готов и для пользователя подобраны вакансии, бот пишет пользователю:
- что аккаунт готов;
- что подобраны подходящие вакансии;
- предлагает посмотреть вакансии.

### 7. Отправка подходящих вакансий

Бот отправляет пользователю вакансии по очереди.

Для каждой вакансии можно дать:
- название;
- город/локацию;
- тип работы;
- требования;
- условия;
- кнопку “Откликнуться”;
- кнопку “Следующая вакансия”;
- кнопку “Не интересно”;
- кнопку “Помощь”.

Отклик может:
- отправляться на платформу через API;
- открывать ссылку на вакансию в личном кабинете;
- фиксироваться в базе/таблице для дальнейшей обработки.

## Вторая часть проекта: продвижение Telegram-канала продаж

Клиент хочет использовать Telegram как новый канал привлечения пользователей.

Задача продвижения:
- привести новых пользователей в Telegram-группу/бота;
- помочь пользователям, которым лень или сложно регистрироваться на платформе;
- превратить группу + бот в работающий acquisition/onboarding funnel.

### Каналы продвижения

1. **Telegram-группа как community hub**
   - Регулярные посты о вакансиях.
   - Закрепленный пост с CTA “Найти работу через бота”.
   - Ответы бота на частые вопросы.
   - Перевод пользователей из обсуждения в личный onboarding.

2. **Telegram Ads / платные размещения**
   - Реклама в тематических Telegram-каналах.
   - Размещения в beauty/job/community каналах.
   - Трафик ведется в группу или сразу в бота.

3. **Instagram / TikTok / Facebook**
   - Короткие видео: “Как найти работу в beauty через Telegram”.
   - Ссылки на бота/группу в bio, stories, captions.
   - UTM/referral links для отслеживания источника.

4. **Сайт и существующая платформа**
   - Видимый CTA: “Need help registering? Use Telegram bot”.
   - Ссылка на бота рядом с регистрацией.
   - Telegram как assisted registration channel для ленивых/неопытных пользователей.

5. **Referral mechanics**
   - Пользователь может пригласить друга/коллегу.
   - Бот фиксирует referral source.
   - Позже можно добавить бонусы/приоритет/доступ.

### Что можно реализовать технически для продвижения

- Tracking links для разных источников.
- Разные `/start` параметры: Instagram, TikTok, Telegram Ads, group, website.
- Сохранение источника пользователя.
- Базовая аналитика: start -> registration complete -> verified -> jobs shown -> apply.
- Сегментация по источникам.
- Скрипты сообщений и CTA для группы.
- Автоматические ответы на частые вопросы в группе.

## Предлагаемая архитектура

### Компоненты

1. **Telegram Group Listener**
   - Бот находится в общей группе.
   - Отслеживает ключевые слова/намерения.
   - Отвечает пользователю в группе.
   - Отправляет пользователя в личный чат с ботом.

2. **Telegram Onboarding Bot**
   - Личный диалог.
   - Пошаговая регистрация.
   - Валидация ответов.
   - Сбор email и данных профиля.
   - Создание/подготовка аккаунта.

3. **Integration Layer**
   - API платформы, если доступен.
   - Webhooks.
   - Database / Airtable / Google Sheets fallback.
   - Очередь на ручную проверку, если автоматическая регистрация ограничена.

4. **User Status & Notifications**
   - Статус регистрации.
   - Статус верификации.
   - Уведомление “аккаунт готов”.
   - Отправка вакансий.

5. **Job Matching Delivery**
   - Получение подходящих вакансий из платформы/API.
   - Отправка вакансий пользователю.
   - Кнопка отклика или перехода на платформу.
   - Фиксация реакции пользователя.

6. **Analytics**
   - Источник пользователя.
   - Количество переходов из группы в личку.
   - Количество начатых регистраций.
   - Количество завершенных регистраций.
   - Количество верифицированных аккаунтов.
   - Количество отправленных вакансий.
   - Количество откликов.

## Scope: MVP

Цель MVP: запустить работающий Telegram-assisted registration flow для платформы и проверить, что Telegram действительно приводит и активирует новых пользователей.

### Входит в MVP

- Новый Telegram bot.
- Добавление бота в общую группу.
- Настройка триггеров по ключевым словам/фразам.
- Ответ в группе с переводом пользователя в личный чат.
- Личный onboarding flow.
- Сбор данных для регистрации на платформе.
- Валидация обязательных полей.
- Передача данных в платформу/API или временную базу.
- Выдача временного пароля, если платформа поддерживает это через API или согласованный процесс.
- Статус “регистрация отправлена / ожидает проверки”.
- Уведомления администратору о новом пользователе.
- Базовая отправка “аккаунт готов” и списка вакансий, если есть способ получить статус и вакансии.
- Tracking source для пользователей из группы/внешних ссылок.
- Базовая документация и handoff.

### Не входит в MVP, если отдельно не согласовано

- Полноценная AI-модерация всех сообщений группы.
- Сложный AI-чат без сценарных ограничений.
- Полная CRM/платформа-разработка на стороне клиента.
- Исправление/доработка их основной платформы.
- Автоматическая верификация пользователей, если она требует бизнес-решений на стороне клиента.
- Полноценная рекламная кампания “под ключ”.
- Создание большого количества рекламных креативов.
- Advanced dashboard.
- Платежи, subscriptions, membership.

## Ключевая зависимость

Финальная цена и срок зависят от того, есть ли у платформы:

- API для создания пользователя;
- API для установки временного пароля;
- API/status webhook для проверки статуса верификации;
- API для получения подходящих вакансий;
- API для отправки отклика на вакансию;
- тестовая среда/sandbox;
- техническая документация.

Если API нет, нужно будет делать промежуточную базу/админ-очередь или согласовать manual/semi-automatic process.

## Вопросы к Диане перед финальным утверждением

1. Есть ли API у платформы? Можно ли создавать пользователя через API?
2. Можно ли через API выдавать временный пароль?
3. Как сейчас проходит регистрация пользователя на платформе?
4. Какие поля обязательны для регистрации?
5. Как проходит верификация и где хранится статус верификации?
6. Можно ли получить список подходящих вакансий через API?
7. Кто подбирает вакансии: алгоритм платформы, менеджер или вручную?
8. Как пользователь должен откликаться на вакансию: внутри Telegram или через ссылку на платформу?
9. Какие языки нужны в боте?
10. Сколько типов пользователей есть?
11. Какие ключевые фразы бот должен отслеживать в группе?
12. Есть ли ограничения по тому, как бот может отвечать в группе?
13. Нужно ли логировать все действия пользователя?
14. Какие рекламные каналы они хотят тестировать первыми: Telegram channels, Telegram Ads, Instagram, TikTok, Facebook, сайт?

## Рекомендуемые пакеты и цены

### Option A — MVP Assisted Registration Bot

**Цена:** $1,800  
**Срок:** 10-14 рабочих дней после получения доступов и подтверждения flow.

Подходит, если нужно быстро запустить первый рабочий сценарий: группа -> бот -> регистрация -> передача данных.

Включает:
- Новый Telegram bot.
- Group keyword triggers.
- Перевод пользователя из группы в личный чат.
- Assisted registration flow.
- До 10-12 вопросов регистрации.
- Валидация обязательных полей.
- Передача данных в API или Google Sheets/Airtable/database.
- Уведомления администратору.
- Базовый статус регистрации.
- Tracking source.
- Testing и handoff.

Не включает сложную автоматическую выдачу вакансий, если для этого нет готового API.

### Option B — Recommended: Assisted Registration + Job Notification Funnel

**Цена:** $3,200  
**Срок:** 3-4 недели.

Рекомендуемый вариант, потому что задача клиента включает не только регистрацию, но и дальнейшее возвращение пользователя с подходящими вакансиями.

Включает все из Option A, плюс:
- Интеграция со статусом верификации, если доступен API/webhook/manual import.
- Уведомление пользователя, когда аккаунт готов.
- Получение/загрузка подходящих вакансий.
- Отправка вакансий пользователю по очереди.
- Кнопки: откликнуться / следующая / не интересно / помощь.
- Фиксация реакции пользователя.
- Базовая аналитика funnel stages.
- Более аккуратная обработка edge cases.
- 1 цикл улучшений после pilot launch.

### Option C — Full Telegram Sales Channel

**Цена:** $5,500-8,000+  
**Срок:** 5-7 недель.

Подходит, если клиент хочет полноценный Telegram acquisition channel с автоматизацией, аналитикой и продвижением.

Включает все из Option B, плюс по согласованию:
- Расширенный FAQ/intent detection в группе.
- Больше сценариев и сегментов.
- Referral tracking.
- Advanced analytics dashboard.
- Несколько рекламных источников с attribution.
- AI-assisted answers в пределах согласованных правил.
- A/B testing сообщений.
- Больше job matching logic.
- Расширенные admin commands.
- 2-3 цикла оптимизации после запуска.

### Promotion Setup Add-On

**Цена:** $700-1,200  
**Срок:** 5-7 рабочих дней.

Может быть отдельным модулем или частью Option C.

Включает:
- Telegram group CTA structure.
- Tracking links для Telegram/Instagram/TikTok/Facebook/website.
- Referral/start parameter logic.
- Черновики сообщений для группы.
- Рекомендации по рекламным размещениям.
- Базовая таблица/дашборд источников.

Не включает закуп рекламных размещений, медиабюджет и ежедневное ведение рекламы.

### Monthly Support / Optimization

**Цена:** $600-1,000/month после запуска.

Может включать:
- Monitoring.
- Bug fixes.
- Улучшение onboarding flow.
- Новые ключевые фразы для группы.
- Улучшение текстов и CTA.
- Малые изменения в логике.
- Performance review.
- Поддержка интеграций.

## Рекомендуемая коммерческая позиция

Не продавать это как “Telegram bot”. Продавать как **Telegram-assisted onboarding and job funnel**.

Ключевая формулировка:

> The value is not only the bot. The value is that Telegram becomes a new acquisition and onboarding channel: users ask questions in the group, the bot moves them into a guided registration flow, sends the data to the platform, waits for verification, and then brings them back with relevant jobs.

Рекомендуемый вариант для предложения:

- Предложить **Option B за $3,200** как основной.
- Если клиентка хочет осторожный старт, предложить **Option A за $1,800**, но явно сказать, что job notifications станут Phase 2.
- Если они хотят сразу канал продаж + продвижение, предлагать **Option C или Option B + Promotion Add-On**.

## Предлагаемые этапы работы

### Phase 1 — Discovery & Technical Mapping

- Подтвердить registration fields.
- Получить документацию/API платформы.
- Описать group trigger logic.
- Описать private onboarding flow.
- Согласовать статусы пользователя и вакансий.

### Phase 2 — Bot Foundation

- Создать Telegram bot.
- Подключить к группе.
- Настроить group keyword triggers.
- Реализовать переход в личный чат.
- Реализовать базовый onboarding.

### Phase 3 — Platform Integration

- Подключить API или fallback database.
- Отправлять registration data.
- Настроить admin notifications.
- Обрабатывать ошибки и неполные данные.

### Phase 4 — Verification & Job Delivery

- Получать/обновлять статус аккаунта.
- Отправлять “account ready”.
- Получать или импортировать подходящие вакансии.
- Отправлять вакансии пользователю.
- Фиксировать отклики/интерес.

### Phase 5 — Tracking & Promotion Foundation

- Настроить source tracking.
- Создать start links для разных каналов.
- Настроить базовую аналитику.
- Подготовить CTA/сообщения для группы и внешних источников.

### Phase 6 — Testing & Launch

- Проверить group trigger path.
- Проверить private registration path.
- Проверить data sync.
- Проверить verification/job notification path.
- Исправить ошибки.
- Передать инструкцию.

## Черновик сообщения Диане

Hi Diana,

Thank you for the call. Based on our discussion, I understand the project as a Telegram-assisted onboarding and job funnel for your existing beauty platform.

The main idea is:

1. A user asks something in the Telegram group, for example “how can I find a job?”
2. The bot detects this intent and replies in the group, inviting the user to continue in private messages.
3. In private chat, the bot guides the user through registration step by step.
4. The bot collects all required information and sends it to your platform or database.
5. The user receives a temporary password or next instructions.
6. Verification happens on your platform side.
7. When the account is ready and matching jobs are available, the bot notifies the user and sends relevant jobs one by one.
8. The user can open or apply to the job from Telegram/platform.

I also see Telegram as a new acquisition channel, not only a support tool. We can track where users come from, use the group as a community entry point, and connect traffic from Instagram, TikTok, Facebook, website, Telegram placements, or Telegram Ads.

Before I finalize the exact scope, I need to confirm the technical side:

1. Does your platform have an API for user registration?
2. Can we create users and temporary passwords via API?
3. Can we get verification status via API or webhook?
4. Can we get matched jobs for a user via API?
5. Should “apply to job” happen inside Telegram or on the platform?

Estimated options:

- MVP Assisted Registration Bot: $1,800, around 10-14 working days.
- Recommended Assisted Registration + Job Notification Funnel: $3,200, around 3-4 weeks.
- Full Telegram Sales Channel: $5,500-8,000+, depending on promotion tracking, analytics, referral logic, AI, and advanced integrations.

My recommendation is Option B, because your project is not only registration. The important value is the full journey: group question -> private guided registration -> platform sync -> verification -> relevant jobs -> application.

If you want to start smaller, we can launch Option A first and then add job notifications and promotion tracking as Phase 2.

## Open risks

- Нужно подтвердить API платформы. Это главный фактор цены и сроков.
- Telegram-бот не может первым писать пользователю в личку; пользователь должен сам открыть бота через кнопку/link.
- Автоматическая обработка сообщений в группе должна быть аккуратной, чтобы бот не спамил и не раздражал участников.
- Верификация и matching вакансий зависят от логики платформы клиента.
- Если вакансии нельзя получить через API, нужна semi-manual схема импорта или админ-очередь.
- Продвижение Telegram-канала продаж требует отдельного медиабюджета и тестов источников.

## Next steps

1. Tamerlan confirms this understanding with Diana.
2. Get platform API/docs or confirm no API.
3. Finalize selected package and milestones.
4. Prepare Upwork milestone proposal.

## PDF deliverable

- 2026-06-18: Client-ready FlowOps-style PDF created.
- Working folder: `/Users/tamerlan/Desktop/diana-telegram-job-funnel-spec`
- 2026-06-19: PDF reframed from technical specification into client-facing commercial proposal.
- Current final PDF: `/Users/tamerlan/Desktop/diana-telegram-job-funnel-spec/Diana_Telegram_Job_Funnel_Commercial_Proposal_FlowOps.pdf`
- Older technical-spec PDF kept in the same folder but should not be sent unless explicitly needed.
- Source HTML: `/Users/tamerlan/Desktop/diana-telegram-job-funnel-spec/index.html`
- Build script: `/Users/tamerlan/Desktop/diana-telegram-job-funnel-spec/build_index.py`
- Structure: 12 A4 pages covering context, problem map, user journey, architecture, registration flow, verification/jobs, promotion, data/API dependencies, quality controls, implementation plan, commercial options, and next steps.
- Current pricing included: $1,250 MVP registration bot, $2,250 recommended funnel, $250-500 promotion setup add-on, $450-700/month support.
- Removed the larger `Full Telegram Sales Channel` option to avoid scaring the client and keep the proposal focused on the immediate launch.
