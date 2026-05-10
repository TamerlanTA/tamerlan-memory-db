# n8n Local Docker Setup on Mac

## Related
- [[All about Agents/agent-memory|agent-memory]]
- [[current-focus]]

## Purpose
Локальный n8n на Mac лучше запускать через **Docker Desktop + n8n container**. Для self-hosting это самый стабильный вариант: окружение изолировано, меньше проблем с версиями Node/npm, проще обновлять и переносить на VPS.

Использовать:
- локально через Docker — для тестов, разработки и дебага;
- VPS — для production workflows, где Telegram, Vapi, WhatsApp, клиенты и webhooks должны работать 24/7;
- локальный n8n + ngrok — только для временных webhook-тестов.

## Quick Start with Docker

### 1. Install Docker Desktop
Скачать и установить **Docker Desktop for Mac**. После установки открыть Docker и дождаться, пока он полностью запустится.

Проверка:

```bash
docker --version
```

Если терминал показывает версию Docker, установка работает.

### 2. Create n8n Folder

```bash
mkdir -p ~/n8n-local
cd ~/n8n-local
```

### 3. Create `docker-compose.yml`

```bash
nano docker-compose.yml
```

Содержимое:

```yaml
version: "3.8"
services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n-local
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - TZ=Asia/Almaty
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - N8N_SECURE_COOKIE=false
    volumes:
      - ./n8n_data:/home/node/.n8n
```

Сохранить в nano:

```text
Ctrl + O -> Enter -> Ctrl + X
```

### 4. Start n8n

```bash
docker compose up -d
```

Открыть:

```text
http://localhost:5678
```

При первом запуске появится экран создания owner account. Создать логин и пароль, после этого n8n будет работать локально.

## Useful Commands

Остановить n8n:

```bash
docker compose down
```

Запустить снова:

```bash
docker compose up -d
```

Посмотреть логи:

```bash
docker logs -f n8n-local
```

Обновить n8n:

```bash
docker compose pull
docker compose up -d
```

## Webhooks

Локальный n8n доступен только на этом компьютере:

```text
http://localhost:5678
```

Если внешним сервисам нужно отправлять webhooks в локальный n8n, им нужен публичный URL. Это актуально для Vapi, Telegram, Meta WhatsApp, Stripe, ClickUp, Make, Airtable и других интеграций.

Для тестов можно использовать ngrok:

```bash
ngrok http 5678
```

ngrok выдаст URL примерно такого вида:

```text
https://abc123.ngrok-free.app
```

После этого в `docker-compose.yml` лучше добавить переменную:

```yaml
      - WEBHOOK_URL=https://abc123.ngrok-free.app
```

Затем перезапустить контейнер:

```bash
docker compose down
docker compose up -d
```

Минус бесплатного ngrok: URL часто меняется. Для постоянной работы и клиентских production workflows лучше использовать VPS.

## Alternative: npm Install

Можно запустить n8n без Docker:

```bash
npm install -g n8n
n8n
```

Но для долгосрочной работы Docker предпочтительнее: стабильнее, проще обновлять, проще переносить окружение на сервер.

## Recommended FlowOps Setup

Для FlowOps и AI/voice/webhook проектов:

1. Локально через Docker — разработка, тесты, дебаг.
2. VPS — production workflows, которым нужен стабильный 24/7 webhook endpoint.
3. n8n + ngrok — временные локальные webhook-тесты.

Минимальный старт:

```bash
mkdir -p ~/n8n-local
cd ~/n8n-local
nano docker-compose.yml
docker compose up -d
```

Затем открыть:

```text
http://localhost:5678
```
