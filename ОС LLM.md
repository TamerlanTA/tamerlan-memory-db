Система работы со всеми моими LLM
qwdqqwwwdw

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[Obsidian - память агента]]
- [[projects/AI-Powered Woven Label Generator/overview|AI-Powered Woven Label Generator]]

## A. Claude Code = Chief Reasoning Agent

Использовать для:

- сложных задач
    
- архитектуры
    
- больших code reviews
    
- RCA
    
- validation планов
    
- проектной continuity через Obsidian

Но:
**не тратить Claude на рутину**.

## B. Codex = Primary Execution Agent

Использовать для:

- batch implementation
    
- исправление кода
    
- написание тестов
    
- рефакторинг
    
- миграции
    
- локальные правки
    
- генерацию файлов
    
- обновление memory notes по готовому формату
    

Codex должен делать **80% производственной работы**.

## **C. ChatGPT = Orchestrator / Strategic Control Plane**

Использовать меня для:

- проектирования задач
    
- упаковки контекста
    
- маршрутизации задач между агентами
    
- составления batch prompt’ов
    
- сокращения токенов
    
- выжимки из больших обсуждений
    
- handoff between agents
    
- client communication
    
- decision framing
    
- final synthesis

## **Пример работы схемы**

**ChatGPT** - упаковал задачу

**Codex** - сделал реализацию

**Claude** - проверил только то, что реально рискованно

# 1. Самая важная идея: работаем не “чатами”, а “единицами работы”

Каждая задача должна проходить через pipeline.

## **Pipeline задачи**

### Stage 1. Classification

Определяем тип задачи:

- стратегическая
    
- архитектурная
    
- implementation
    
- debugging
    
- review
    
- communication
    
- research
    
- memory update

### Stage 2. Routing

Отправляем её правильному агенту.

### Stage 3. Context packaging

Даем только нужный контекст, не весь мир.

### Stage 4. Execution

Агент делает батчем.

### Stage 5. Compression

Результат сжимается в:

- summary
    
- decisions
    
- changed files
    
- risks
    
- next steps

### **Stage 6. Memory write-back**

Итог записывается в Obsidian.


# Правило №1: всегда работать батчами

## один сильный batch prompt

в котором сразу есть:

- цель
    
- ограничения
    
- контекст
    
- список файлов
    
- требования к реализации
    
- обработка edge cases
    
- тесты
    
- expected output format

Это резко уменьшает расход лимитов.


# Правило №2: не передавать сырой контекст, передавать “операционный контекст”

Не надо скармливать агенту 200 сообщений чата.

Нужно давать короткий structured handoff.
Это в разы дешевле и лучше, чем “вот переписка за два дня”.


# 2. Как оптимизировать под лимиты Claude

Claude надо включать только в 5 случаях:

## 1. Архитектурный выбор

Когда неправильное решение дорого стоит.

## 2. Сложный debugging / RCA

Когда есть системный баг, непонятный root cause.

## 3. Design review / validation

Когда Codex уже что-то сделал, и нужен умный критик.

## 4. Prompt design for other agents

Когда нужно выжать максимум из Codex или другого агента.

## 5. Big project steering

Когда нужно понять, куда двигать milestone / проект дальше.

# 3. Многоуровневая память


## Layer 1 — Active Context

то что ты видишь прямо сейчас в чате. 200к токенов, живёт только в этой сессии. Когда закроешь - исчезнет.

## Layer 2 — Project Memory
  
**Obsidian vault** (~/obsidian-vault) - долгосрочная память в markdown-файлах. Сессионные заметки, исследования, контент, agent-memory.md с общей базой знаний агентов. Читаю и пишу через файловую систему

- статус
    
- решения
    
- архитектура
    
- риски
    
- milestones
    
- client preferences

## Layer 3 — Session Notes

Краткий лог последней работы:

- что сделали
    
- что нашли
    
- что дальше
  
## Layer 4 — Reusable Knowledge

**Файлы конфигурации** - CLAUDE.md, агент-файлы в ~/.claude/agents/, скиллы в ~/.claude/skills/. Это не память" в классическом смысле но именно здесь живут правила роли и поведение - и они persist между сессиями постоянно.

# 4. структура Obsidian

MemoryDB/
├── agent-memory.md
├── current-focus.md
├── routing-rules.md
├── prompts/
│   ├── codex-task-packet.md
│   ├── claude-review-packet.md
│   ├── handoff-summary-template.md
│   └── client-reply-template.md
├── knowledge/
│   ├── debugging-patterns.md
│   ├── upwork-proposal-patterns.md
│   ├── vercel-deploy-checklist.md
│   └── n8n-audit-patterns.md
├── projects/
│   ├── griffes-vivienne/
│   │   ├── overview.md
│   │   ├── current-state.md
│   │   ├── decisions.md
│   │   ├── risks.md
│   │   ├── next-steps.md
│   │   ├── prompts.md
│   │   └── sessions/
│   ├── whatsapp-kommo-bot/
│   │   ├── overview.md
│   │   ├── current-state.md
│   │   ├── decisions.md
│   │   ├── risks.md
│   │   ├── next-steps.md
│   │   ├── prompts.md
│   │   └── sessions/
│   ├── shannon-clickup-jotform/
│   │   ├── overview.md
│   │   ├── current-state.md
│   │   └── sessions/
│   └── upwork-system/
│       ├── overview.md
│       ├── patterns.md
│       └── sessions/
└── inbox/


# 5. Нужны артефакты промежуточного состояния

Чтобы не объяснять всё заново, каждый проект должен иметь стандартные файлы.

Для больших проектов:
projects/project-name/
  overview.md - Что это за проект
  current-state.md - Где проект сейчас
  decisions.md - Подтвержденные решения
  risks.md - Текущие риски и блокеры
  next-steps.md - Ближайшие действия
  prompts.md - Сильные повторно используемые промпты.

# 6. Work cycle

## Step 1

ChatGPT формируешь задачу и маршрут.
## Step 2

Получаешь готовый task packet.
## Step 3

Отдаешь Codex или Claude.
## Step 4

Возвращаешь результат.
## Step 5

ChatGPT:

- проверяет,
    
- сжимает,
    
- формирует next action,
    
- готовит memory update.

Так ты сильно уменьшаешь хаос.


# 7. Режим для долгих проектов

Для больших проектов не вести “вечный один чат”.

Нужно вести:
## A. Project memory in Obsidian

Это источник истины.
## B. Ephemeral execution chats

Короткие рабочие треды под конкретные задачи.
## C. Summaries after each task

Чтобы любая сессия могла умереть без потери контекста.

Это критично для лимитов.

# 8. Пропмт для начала нового чата LLM

Read the memory for project [project-name], get in sync with the current state, and then I will give you the next task.

# 9. Пропмты для обновления памяти

## При завершении рабочего блока

Do a memory sync for [project-name].
## При смене агента

Do a handoff sync for [project-name].
## В конце дня

Do an end-of-day sync for [project-name].