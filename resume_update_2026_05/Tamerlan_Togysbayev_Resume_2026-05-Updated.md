# Tamerlan Togysbayev

**AI Automation Engineer · Full-Stack AI Systems Builder**  
tamertt931@gmail.com · flowops.agency · github.com/TamerlanTA · Almaty, Kazakhstan · Open to remote

## Summary

I build end-to-end automation systems across n8n, Make.com, APIs, LLMs, CRM data models, and full-stack web apps. Recent work includes human-in-the-loop sales pipelines, Telegram command centers, AI website audit generators, Airtable/Linear operating systems, and production AI web products with payments, auth, email, and back-office workflows.

## Skills

**Automation & Orchestration:** n8n, Make.com, Zapier, Google Apps Script, workflow QA, retries, dedupe, error branches  
**AI & LLMs:** OpenAI API / Responses API, Anthropic Claude, Gemini image generation, prompt engineering, structured JSON outputs, multi-agent orchestration  
**Data / CRM:** Airtable, Google Sheets, Supabase/Postgres, MySQL/TiDB, Redis, Drizzle ORM, Linear, Obsidian memory systems  
**Scraping / Prospecting:** Firecrawl search/scrape, Apify, LinkedIn/Upwork lead workflows, website audit generation  
**Frontend / Backend:** React, Next.js, TypeScript, Tailwind CSS, Vite, Node.js, tRPC  
**Messaging / Commerce / Infra:** Telegram Bot API, WhatsApp Business/SellerChat, Kommo CRM, Gmail, Resend, SendGrid, Buffer, Stripe, Vercel, Railway, Git

## Experience

### AI Automation Engineer & Founder — FlowOps

2022-Present · Almaty, Kazakhstan / Remote

Run a small automation and AI integration practice focused on practical business systems: lead generation, CRM automation, approval workflows, AI assistants, and production web apps.

#### FlowOps Client Acquisition OS

Internal agency operating system

- Built a multi-channel acquisition architecture around Upwork Radar, LinkedIn Pain Radar, Website Audit Generator, Demo Library, CRM, proposals, and retainer conversion.
- Created a FlowOps Airtable CRM structure with Leads, Opportunities, Messages, Audits, Proposals, Clients, Retainers, Demos, and Automation Logs so automations have a stable operating database.
- Designed automation rules for dedupe, draft generation, follow-up queues, reply/status intake, proposal building, demo recommendation, weekly CRM health reporting, and won-deal handoff.

#### Pipeline C — AI Website Audit Generator

FlowOps prospecting / outreach automation

- Built n8n workflows that use Telegram commands, Firecrawl search/scrape, AI audit generation, CRM writes, Telegram approval cards, and Gmail sending only after explicit approval.
- Created a Prague local-field-sales variant: Firecrawl prospecting, locality/aggregator filters, dedupe, Google Sheets queue, OpenAI structured audits, and visit-ready prospect rows.
- Hardened workflow imports, node versions, Firecrawl output normalization, Google Sheets mappings, batch caps, diagnostics, and metadata preservation to avoid silent failures.

#### LinkedIn Outreach Automation

Personal / agency prospecting

- Built six n8n workflows covering lead discovery via Apify, daily message generation with Claude Haiku, Google Sheets queue/state, Telegram approval, Sourcegeek sending, follow-ups, reply monitoring, and daily stats.
- Solved production constraints such as Telegram callback timeouts, Sourcegeek connection-request limits, n8n Set-node limitations, Anthropic output parsing, and Google Sheets matching-column updates.

#### AI Content Bot

Telegram command center for content ops

- Built a Telegram-first command center backed by n8n workflows for topic discovery, morning briefing, AI post generation, Gemini image generation, approval controls, publishing flow, and stats collection.
- Centralized callback routing through a single Telegram Trigger so one bot can handle messages, inline buttons, outreach queue actions, and content approval without trigger conflicts.

#### Linear Ops Automation System

Execution layer design for FlowOps

- Designed a six-workflow Linear automation layer: Daily Command Center, Blocked Decision Bot, Team Assignment Notifier, Stale Issue Reminder, Linear-to-Obsidian Memory Sync, and Weekly FlowOps Review.
- Defined operating rules for Linear as execution source, Obsidian as long-term memory, Telegram as decision surface, and n8n as the automation engine.

#### StoreHouse n8n Warehouse Automation

Inventory / invoice automation

- Generated and validated three n8n workflows: AI invoice/photo recognition, low-stock alerts, and suspicious activity monitoring.
- Implemented Telegram photo/text intake, OpenAI Vision parsing, confidence checks, StoreHouse API handoff assumptions, cursor-based dedupe, dynamic chat IDs, error branches, and Google Sheets logging.

## Selected Product & Client Builds

### AI-Powered Woven Label Generator — Griffes Vivienne (France)

- Built a production AI product where users upload a brand/logo, choose material, color, size, and order mode, then receive a realistic woven-label mockup.
- Implemented Next.js/React, tRPC, Drizzle, MySQL/Railway, Vercel, Stripe checkout, credit packs, guest free-trial gating, Resend quote/preorder emails, bilingual FR/EN i18n, Clerk auth styling, admin sales/ops visibility, and asset retrieval.
- Hardened AI generation with input validation, upload-size safeguards, product-photo/logo interpretation, white-logo contrast handling, generation error taxonomy, credit-safety tests, R2 storage fallback behavior, SEO/legal pages, and MOQ/business-rule updates.

### WhatsApp AI Bot — Traffic Fine Disputes (Colombia)

- Built an end-to-end intake and response automation for fotomulta cases: WhatsApp message intake, Redis session checks, Supabase conversation history, Kommo CRM lookup, government-database scraping sub-workflow, and structured AI response.
- Built a separate outbound pipeline: Google Sheets -> Google Apps Script webhook -> Make.com -> SellerChat -> WhatsApp templates. Main n8n workflow runs 128 nodes.

### FlowOps Agency Website — flowops.agency

- Built the agency homepage around a live AI-generated automation architecture diagram: visitor describes an automation need, backend calls OpenAI Responses API with a structured schema, and deterministic fallback handles staging/no-key cases.
- Lead capture routes into Telegram, Google Sheets, and SendGrid, turning the website into both a portfolio surface and an inbound workflow.

## Freelance

Independent automation and integration work through Upwork and direct clients: CRM connections, API integrations, low-code/no-code workflow builds, AI agents, and operations automations for small businesses.

## Education

**Kazakh-British Technical University (KBTU)**  
Bachelor's in Information Systems · 2021 · Almaty, Kazakhstan

## Work Samples

Suggested screenshot slots for the visual portfolio page. Replace placeholders with real screenshots from n8n, Airtable/Sheets, Telegram, Linear, Vercel/admin screens, and shipped product UI.

1. **Pipeline C — Website Audit Generator:** n8n overview showing Telegram trigger, Firecrawl search/scrape, AI audit, CRM/Sheets write, Telegram approval, and Gmail send path.
2. **Pipeline C Prague — Visit-Ready Prospects:** Google Sheets / Airtable output with business type, website, address/neighborhood, pain signal, fit score, and next action.
3. **FlowOps CRM:** Airtable base view showing Leads, Opportunities, Messages, Audits, Proposals, Clients, Retainers, Demos, and Automation Logs.
4. **LinkedIn Outreach — Telegram Approval:** Telegram card with approve/skip buttons plus the n8n WF-05 approval flow that sends via Sourcegeek and loops to the next lead.
5. **AI Content Bot — Command Center:** Telegram command or inline-button flow + n8n WF-06 showing routing to content generation, stats, topic discovery, and outreach tools.
6. **Linear Ops Automation System:** Linear project/issues view or n8n prototype/spec screen showing Daily Command Center / Blocked Decision Bot / stale reminder workflows.
7. **Griffes Vivienne — Result + Quote Flow:** Generated woven-label result, quote/preorder CTA, admin preorder/asset visibility, or Resend quote email proof.
8. **WhatsApp Traffic Fines Bot:** Main 128-node n8n workflow or a sanitized WhatsApp/SellerChat flow showing intake, CRM lookup, scrape sub-flow, and AI response.
9. **StoreHouse Warehouse Bot:** n8n workflow showing Telegram photo intake, OpenAI Vision parsing, StoreHouse API handoff, confidence check, and Sheets log.
