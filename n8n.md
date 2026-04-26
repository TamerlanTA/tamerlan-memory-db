- [[ОС LLM]]
- [[agent-memory]]
## Правила работы для агентов с n8n

- править JSON не по одному символу, а структурно через Node: это безопаснее для n8n export-формата, потому что сохраняет валидный JSON и точечно меняет nodes/connections/parameters. 

## Рекомендации от ГПТ


## **1. Сначала сделать “n8n Automation Architect Skill”**

Тебе нужен отдельный skill/инструкция для Claude Code и Codex, который будет заставлять их работать по одному стандарту.

Идея skill:

```md
# Skill: n8n Automation Architect

You are an expert n8n automation architect.

Your job is not to immediately generate a workflow.
Your job is to design production-ready n8n workflows with correct business logic, clean node structure, error handling, retries, logging, and maintainability.

Before building any workflow, always produce:

1. Business goal
2. Trigger source
3. Inputs and expected data shape
4. Required external systems
5. Happy path
6. Edge cases
7. Error handling strategy
8. Deduplication/idempotency strategy
9. Data mapping table
10. Node-by-node workflow plan
11. Test cases
12. Final n8n workflow JSON only after the logic is approved or fully specified

Never create vague workflows.
Never skip validation nodes.
Never assume field names without listing assumptions.
Never hardcode credentials.
Never ignore API pagination, rate limits, or failed requests.
```

Это база. Агент должен понимать: **он не “рисует ноды”, он строит бизнес-систему**.

---

## **2. Дай агентам фиксированный формат работы**

Для каждого n8n проекта лучше использовать не один промпт, а pipeline из 4 этапов:

### **Этап 1 — Discovery**

Агент должен понять бизнес-процесс.

Он должен ответить:

```md
## Business Process Understanding

Goal:
What exactly should be automated?

Actors:
Who starts the process? Who receives the result?

Systems:
Which tools are involved? Example: Gmail, Airtable, ClickUp, Slack, HubSpot, OpenAI, Google Sheets.

Trigger:
What starts the workflow?

Input:
What data comes in?

Output:
What should happen at the end?

Rules:
What decisions should the automation make?

Failure cases:
What can go wrong?
```

На этом этапе он **не должен писать JSON**.

---

### **Этап 2 — Logic Blueprint**

Потом агент делает чистую бизнес-логику.

Пример:

```md
## Workflow Logic Blueprint

1. Trigger: New email received
2. Extract sender, subject, body, attachments
3. Check if email already processed
4. Classify email with AI
5. If category = urgent:
   - Create task in ClickUp
   - Send Slack alert
6. If category = normal:
   - Add row to Google Sheet
7. If AI confidence < 0.7:
   - Send to manual review
8. Save processing status
9. Log result
```

Вот тут ты уже видишь, правильная ли логика. Это намного дешевле, чем потом чинить 40 нод.

---

### **Этап 3 — n8n Node Plan**

Только потом агент должен перевести логику в ноды:

```md
## n8n Node Plan

1. Gmail Trigger
   Purpose: Detect new inbound email
   Output fields: sender, subject, body, messageId

2. Set: Normalize Email Data
   Purpose: Convert raw email into standard object

3. Google Sheets: Check Processed Messages
   Purpose: Prevent duplicate processing

4. IF: Already Processed?
   True: Stop workflow
   False: Continue

5. OpenAI / Claude HTTP Request
   Purpose: Classify email
   Expected JSON:
   {
     "category": "urgent | normal | irrelevant",
     "confidence": 0-1,
     "summary": "string"
   }

6. Switch: Route by category

7. ClickUp Create Task / Google Sheets Add Row / Slack Message

8. Google Sheets: Save processing log
```

Это самый важный этап. Если node plan хороший, JSON уже проще.

---

### **Этап 4 — n8n JSON / Implementation**

Только после этого просить:

```md
Now generate the n8n workflow JSON based on the approved node plan.

Requirements:
- Use clear node names
- Use expressions correctly
- Do not include real credentials
- Use placeholder credential names
- Add sticky notes explaining major sections
- Include error branches where possible
- Use Set nodes for normalization
- Use IF/Switch nodes for routing
- Use Code nodes only when necessary
```

---

## 

## 

## 

## 

## **3. Сделай общий**

**`CLAUDE.md`**

**/**

**`AGENTS.md`**

**для n8n проектов**

Я бы сделал такой файл в корне каждого automation-проекта:

```md
# Automation Project Rules

This project is focused on building production-ready n8n workflows.

## Core Principles

1. Business logic first, n8n nodes second.
2. Never generate workflow JSON before defining the full workflow blueprint.
3. Every workflow must include:
   - Clear trigger
   - Input normalization
   - Validation
   - Deduplication or idempotency
   - Main business logic
   - Error handling
   - Logging
   - Testing checklist
4. Avoid hardcoded values.
5. Use environment variables or n8n credentials for secrets.
6. Prefer simple node chains over complex Code nodes.
7. Use Code nodes only for transformations that are hard to do with native n8n nodes.
8. Every AI node must return structured JSON.
9. Every external API call must define:
   - method
   - endpoint
   - headers
   - body
   - expected response
   - failure handling
10. Every workflow must be understandable by a human client.

## Required Output Format

For every new automation, respond in this order:

1. Business Process Summary
2. Assumptions
3. Required Credentials
4. Data Model
5. Workflow Logic Blueprint
6. Node-by-Node Plan
7. Error Handling Plan
8. Testing Plan
9. n8n JSON or implementation instructions

## n8n Naming Rules

Use section prefixes:

- TRIGGER — for starting nodes
- SET — for data formatting
- VALIDATE — for checks
- AI — for LLM calls
- ROUTER — for IF/Switch nodes
- ACTION — for final business actions
- LOG — for logs
- ERROR — for failure handling

Example:

TRIGGER — New Email  
SET — Normalize Email Data  
VALIDATE — Required Fields  
AI — Classify Inquiry  
ROUTER — By Inquiry Type  
ACTION — Create ClickUp Task  
LOG — Save Processing Result  
ERROR — Notify Admin
```

---

## **4. Обязательно заставь их делать Data Contract**

Это прям must-have.

Перед созданием workflow агент должен описать структуру данных:

```md
## Data Contract

Input object:

{
  "source": "gmail",
  "messageId": "string",
  "senderEmail": "string",
  "senderName": "string",
  "subject": "string",
  "body": "string",
  "receivedAt": "ISO date"
}

Normalized object:

{
  "leadId": "string",
  "email": "string",
  "name": "string",
  "requestType": "string",
  "summary": "string",
  "priority": "low | medium | high",
  "status": "new | processing | completed | failed"
}

Output object:

{
  "success": true,
  "actionTaken": "created_task",
  "externalRecordId": "string",
  "processedAt": "ISO date"
}
```

Почему это важно: большинство n8n ошибок начинается с того, что одна нода ожидает `email`, а другая возвращает `sender.email` или `from.value[0].address`.

Data contract решает это заранее.

---

## **5. Для AI-ноды всегда требуй strict JSON**

Для любых Claude/OpenAI/Gemini нод нельзя просить “проанализируй письмо”. Нужно просить строго:

```md
Return only valid JSON.
Do not include markdown.
Do not include explanations.

Schema:

{
  "category": "sales_lead | support_request | spam | other",
  "confidence": number,
  "summary": string,
  "recommended_action": string,
  "missing_information": string[],
  "priority": "low | medium | high"
}
```

И после AI-ноды обязательно:

```md
VALIDATE — Parse AI JSON
VALIDATE — Check Required AI Fields
ROUTER — If AI confidence is too low, send to manual review
```

Иначе AI иногда сломает весь workflow.

---

## **6. Нужен отдельный “n8n Workflow Review Skill”**

Очень советую сделать второй skill не для создания, а для проверки.

```md
# Skill: n8n Workflow Reviewer

You are a senior n8n workflow reviewer.

Review the workflow for:
1. Business logic gaps
2. Missing validation
3. Missing error handling
4. Duplicate processing risk
5. Bad node naming
6. Incorrect expressions
7. Credential/security issues
8. Missing logging
9. Overuse of Code nodes
10. Missing test cases

Output:

## Verdict
PASS / PASS WITH RISKS / FAIL

## Critical Issues

## Logic Issues

## n8n Implementation Issues

## Suggested Fixes

## Final Checklist
```

Вот это будет очень полезно: один агент строит, второй проверяет.

Например:

**Claude Code** — проектирует workflow.  
**Codex** — проверяет логику, expressions, JSON, edge cases.

Или наоборот.

---

## **7. Не проси “сделай workflow”, проси “сделай automation package”**

Лучший формат задачи для агента:

```md
Create a complete n8n automation package for the following business process.

The package must include:

1. Business process summary
2. Assumptions and open questions
3. Data contract
4. Workflow logic blueprint
5. Node-by-node n8n plan
6. Required credentials
7. Environment variables
8. Error handling strategy
9. Deduplication strategy
10. Logging strategy
11. Testing checklist
12. Final n8n workflow JSON if possible
13. Client handoff notes
```

Так ты получаешь не просто JSON, а нормальную систему.

---

## **8. Правильная структура папки проекта**

Для каждого большого n8n проекта я бы сделал так:

```txt
client-project/
  README.md
  AGENTS.md
  workflow-spec.md
  data-contract.md
  node-plan.md
  test-plan.md
  handoff-notes.md
  workflows/
    main-workflow.json
    error-handler-workflow.json
  prompts/
    ai-classifier-prompt.md
    ai-response-generator-prompt.md
  samples/
    sample-input.json
    sample-output.json
  docs/
    api-notes.md
    credentials-needed.md
    client-questions.md
```

Тогда Claude/Codex не будут терять контекст.

Особенно важные файлы:

```txt
workflow-spec.md
data-contract.md
node-plan.md
test-plan.md
```

---

## **9. Для Codex/Claude дай правило: сначала симулировать workflow**

Перед JSON агент должен прогнать 3–5 сценариев:

```md
## Simulation Tests

Scenario 1: Valid lead
Input: ...
Expected path:
Trigger → Normalize → Validate → AI Classify → Create CRM Lead → Log Success

Scenario 2: Missing email
Expected path:
Trigger → Normalize → Validate → Error → Manual Review

Scenario 3: Duplicate message
Expected path:
Trigger → Normalize → Dedup Check → Stop

Scenario 4: AI low confidence
Expected path:
Trigger → Normalize → AI Classify → Manual Review

Scenario 5: API failure
Expected path:
Trigger → Normalize → CRM Create Failed → Retry → Error Alert
```

Это резко уменьшает количество переделок.

---

## **10. Что именно хранить в памяти проекта**

Для больших n8n проектов обязательно храни:

```md
# Current State

## Client Goal
...

## Systems Involved
...

## Approved Business Logic
...

## Final Data Contract
...

## Credentials Needed
...

## Known Risks
...

## Decisions
...

## Current Workflow Version
...

## Next Steps
...
```

И каждый раз перед новой задачей агент должен читать:

```md
1. AGENTS.md
2. workflow-spec.md
3. data-contract.md
4. node-plan.md
5. latest session note
```

Это особенно важно для тебя, потому что ты часто работаешь итерациями с клиентом.

---

# **Готовый главный промпт для Claude Code / Codex**

Можешь прямо использовать:

```md
You are helping me build production-ready n8n automations for a real business process.

Important:
Do not immediately generate n8n JSON.
First, think like a senior automation architect.

Your job is to produce a complete automation package with correct business logic, maintainable n8n structure, error handling, deduplication, logging, and test scenarios.

Follow this exact process:

1. Understand the business process
2. Define assumptions
3. Define required systems and credentials
4. Define the input, normalized, and output data contract
5. Design the workflow logic blueprint
6. Create the node-by-node n8n implementation plan
7. Define error handling and retry logic
8. Define deduplication/idempotency logic
9. Define logging and monitoring
10. Simulate at least 5 test scenarios
11. Only then generate n8n JSON or implementation instructions

Rules:
- Use clear node names.
- Use Set nodes to normalize data.
- Use IF/Switch nodes for routing.
- Use Code nodes only when native n8n nodes are not enough.
- Never hardcode credentials or secrets.
- Use placeholders for credentials.
- Every AI step must return strict JSON.
- Every external API call must include expected request and response shape.
- Every workflow must have a manual review path for uncertain or failed cases.
- Every workflow must prevent duplicate processing where relevant.
- Every workflow must log success and failure states.
- Explain all assumptions clearly.

Project details:

[PASTE CLIENT REQUIREMENTS HERE]

Deliver the result in this format:

# 1. Business Process Summary

# 2. Assumptions

# 3. Required Credentials

# 4. Data Contract

## Input Data

## Normalized Data

## Output Data

# 5. Workflow Logic Blueprint

# 6. n8n Node-by-Node Plan

# 7. Error Handling Strategy

# 8. Deduplication / Idempotency Strategy

# 9. Logging Strategy

# 10. Test Scenarios

# 11. Final n8n Workflow JSON or Build Instructions

# 12. Client Handoff Notes
```

---

# **Готовый промпт для проверки workflow**

```md
You are a senior n8n workflow reviewer.

Review this n8n automation as if it will be used by a real client in production.

Check for:
- Broken or unclear business logic
- Missing validation
- Missing deduplication
- Missing error handling
- Missing retry logic
- Missing logging
- Bad data mapping
- Weak AI prompt structure
- Unstable expressions
- Overuse of Code nodes
- Security issues
- Credentials or secrets hardcoded
- Missing manual review path
- Missing test coverage

Return your review in this format:

# Verdict
PASS / PASS WITH RISKS / FAIL

# Critical Issues

# Logic Issues

# n8n Implementation Issues

# Data Mapping Issues

# AI Prompt Issues

# Error Handling Issues

# Recommended Fixes

# Final Production Checklist

Here is the workflow/spec:

[PASTE WORKFLOW OR SPEC HERE]
```

---

## **Самая сильная схема работы для тебя**

Я бы делал так:

**Шаг 1.** Ты скидываешь клиентский brief в Claude Code.  
**Шаг 2.** Claude делает workflow-spec, data-contract, node-plan.  
**Шаг 3.** Ты даешь это Codex с reviewer prompt.  
**Шаг 4.** Codex находит логические дыры.  
**Шаг 5.** Claude правит спецификацию.  
**Шаг 6.** Только потом генерируешь n8n JSON или собираешь workflow вручную по node-plan.  
**Шаг 7.** Агент делает test-plan и handoff-notes для клиента.

То есть не “один агент сразу всё сделал”, а:

```txt
Architect → Reviewer → Builder → Tester → Handoff
```

Это реально уменьшит переделки.

---

## **Мой совет конкретно тебе**

Для твоего стиля работы лучше не пытаться заставить агента сразу идеально генерировать n8n JSON. Лучше сделать так, чтобы агент идеально создавал:

```txt
1. бизнес-логику
2. node-by-node план
3. data mapping
4. AI prompts
5. test scenarios
```

А сам workflow можно собрать быстрее и безопаснее уже по этому плану в n8n. Потому что n8n JSON часто ломается из-за версий нод, credentials, ID, expressions и UI-специфики.

Главная цель: **агент должен быть не генератором workflow, а архитектором логики**. Тогда ты будешь тратить меньше времени на переделки и сможешь быстрее продавать/сдавать большие автоматизации.

