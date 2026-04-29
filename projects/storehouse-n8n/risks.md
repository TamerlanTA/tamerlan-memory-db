# Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

## Content
## Open risks

- No git repository exists yet, so change history and rollback strategy are not established.
- Workflow JSON files have passed static JSON/name/connection/no-Code-node checks but have not yet been imported and smoke-tested inside a live n8n instance.
- Google Sheets node parameter compatibility may need minor adjustment depending on the target n8n version and credential naming.
- Telegram Trigger setup and credential binding must be confirmed in the target n8n instance.
- StoreHouse HTTP Request nodes now point to `/api/sh5exec`, but real host/port/credentials/procedure names must be configured on-site.
- Exact StoreHouse procedure names and response payload shapes remain unknown until `/api/sh5`, `/api/sh5struct`, and live tests are run on the client server.
- The main Agent tools are connected as n8n AI tools, but end-to-end behavior must be verified in n8n because tool execution details vary by n8n version.
- WF1 photo branch currently builds a Telegram file URL using the bot token inside the OpenAI vision image URL; this should be replaced with binary image handoff or a token-safe temporary URL.
- WF1 StoreHouse agent tool calls use `toolHttpRequest` directly, so they do not have deterministic `VALIDATE — SH Response OK` / Telegram / log branches inside the tool execution path.
- WF2 low-stock scheduled workflow may duplicate alerts because the comparison Set node runs once per `min_thresholds` row after Google Sheets read.
- WF1 `check_low_stock` agent tool only returns threshold rows and relies on the agent to combine them with stock balances, rather than returning deterministic low-stock results.
- WF1 tool HTTP placeholders send numeric parameters such as `quantity` and `limit` as strings.

В роли надсмоторщика я провел детальный аудит предоставленных n8n-воркфлоу.

  Помимо уже известных вам проблем (P1.1, P1.2, P1.3, P2.1, P2.2), я обнаружил

  ряд критических логических дыр и архитектурных рисков.

  **🔴 P1 — Критические ошибки логики и безопасности**

  **1.4 — WF1: Попытка кражи токена из выражения (Logic Fail)**

   * **Проблема:** В ноде ACTION — OpenAI vision parse invoice используется

     выражение {{ $credentials.telegramApi.accessToken }}.

   * **Почему это фатально:** В n8n переменная $credentials **недоступна** внутри

     выражений (expressions) из соображений безопасности. Это поле вернет

     undefined, и URL для OpenAI превратится в

     https://api.telegram.org/file/botundefined/..., что приведет к ошибке

     404/401. 

   * **Решение:** (Связано с фиксом P1.2) — Передавать файл как бинарный объект, а

     не строить URL.

  **1.5 — WF3: Ложноположительный "Suspicious Activity" (Logic Loop)**

   * **Проблема:** Фильтр suspicious = rows.filter(r => r.source !== 'telegram_bot')

     в WF3.

   * **Почему это фатально:** В WF1 нода ACTION — SH API: Create Incoming Invoice **не**

     **передает** параметр source: 'telegram_bot' в StoreHouse. Следовательно, SH

     запишет накладную как созданную через API/User. WF3 увидит её, не найдет

     метку telegram_bot и отправит админу алерт о "подозрительной активности". 

   * **Результат:** Бот будет доносить сам на себя на каждое своё успешное действие.

   * **Решение:** Добавить source: 'telegram_bot' в параметры всех процедур записи в

     SH в WF1.

  **1.6 — WF1: Ответ в никуда (UX/Logic)**

   * **Проблема:** Во всех Telegram нодах ответа (ACTION — Telegram send agent

     response и др.) используется статический chatId: {{ $vars.TELEGRAM_CHAT_ID

     }}.

   * **Почему это плохо:** Если бот добавлен в группу или им пользуются несколько

     человек, он всегда будет отвечать в один "админский" чат, а не тому, кто

     задал вопрос.

   * **Решение:** Использовать {{ $json.message.chat.id }} для контекстных ответов.

  ---



  **🟡 P2 — Проблемы надежности и обработки данных**

  

  **2.3 — WF3: "Слепое пятно" в алерте**

   * **Проблема:** Если за 15 минут произошло 5 подозрительных действий, алерт в SET

     — Build suspicious activity alert берет только первое: const first =

     suspicious[0].

   * **Почему это плохо:** Админ увидит только одну операцию, хотя их было много. 

   * **Решение:** Использовать .map() для создания списка всех подозрительных

     операций в тексте сообщения, аналогично тому, как это сделано в WF2.

  

  **2.4 — WF1: Обрыв цепи при скачивании файла**

   * **Проблема:** Нода ACTION — Telegram get invoice file имеет onError:

     continueErrorOutput, но её второй выход (ошибка) **никуда не подключен**.

   * **Результат:** Если файл не скачался (например, истек срок ссылки в TG), поток

     пойдет в OpenAI с пустыми данными. OpenAI упадет с технической ошибкой, и

     пользователь получит невнятный алерт.

   * **Решение:** Подключить выход ошибки к ERROR — Telegram invoice failure alert.

  

  **2.5 — WF2/WF3: Риск "пропусков" или "дублей" по времени**

   * **Проблема:** Триггеры запускаются каждые 15/30 минут и запрашивают данные за

     последние 15/30 минут.

   * **Риск:** Если выполнение воркфлоу задержится на 1 секунду, или время сервера

     SH чуть разойдется с n8n, одна и та же накладная может либо попасть в два

     окна проверки (дубль алерта), либо не попасть ни в одно (пропуск).

   * **Решение:** Использовать ноду Static Data (или запись в Google Sheets) для

     хранения last_processed_id или last_timestamp.

  

  ---

  

  **🟢 P3 — Чистота кода и оптимизация**

  

   * **WF1 (Regex):** Регулярка replace(/\\\json|\\\/g, '') в ноде VALIDATE — Parse

     invoice JSON хороша, но OpenAI иногда пишет текст **после** закрывающих

     кавычек. Безопаснее искать контент между первой { и последней }.

   * **WF1 (Data Bloat):** Вы тащите объект message (весь лог сообщения TG) через 5

     SET-нод. Это раздувает размер execution data в базе n8n. В automation_log

     лучше сохранять только нужные поля (ID сообщения, текст).

  

  **Вердикт:** Воркфлоу выглядят рабочими на 70%, но **P1.5 (самодонос)** и **P1.4 (ошибка**

  **токена)** гарантированно сломают "боевую" эксплуатацию. Рекомендую начать с

  исправления этих пунктов.

## Resolved risks

- Initial project scope clarified enough to generate mock n8n workflow exports.
- Empty workspace risk resolved by adding workflow JSON exports and a generator script.
- Old 6-file workflow output was replaced by the requested 3-file AI Agent architecture.
- StoreHouse mock nodes removed; generated workflow files now contain zero `MOCK —` nodes.
