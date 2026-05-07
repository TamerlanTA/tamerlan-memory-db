from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
)


OUT = "/Users/tamerlan/Desktop/Tamerlan_Togysbayev_Resume_2026-05-Updated.pdf"


def p(text, style):
    return Paragraph(text, style)


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="Name",
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#111827"),
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="Role",
        fontName="Helvetica",
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor("#374151"),
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=11,
        textColor=colors.HexColor("#111827"),
        uppercase=True,
        spaceBefore=10,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        name="BodySmall",
        fontName="Helvetica",
        fontSize=8.4,
        leading=10.2,
        textColor=colors.HexColor("#111827"),
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyTiny",
        fontName="Helvetica",
        fontSize=7.7,
        leading=9.3,
        textColor=colors.HexColor("#111827"),
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Project",
        fontName="Helvetica-Bold",
        fontSize=8.8,
        leading=10.5,
        textColor=colors.HexColor("#111827"),
        spaceBefore=4,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="Meta",
        fontName="Helvetica",
        fontSize=7.7,
        leading=9.3,
        textColor=colors.HexColor("#4B5563"),
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="ResumeBullet",
        parent=styles["BodyTiny"],
        leftIndent=9,
        firstLineIndent=-6,
        bulletIndent=0,
        spaceAfter=2.5,
    )
)
styles.add(
    ParagraphStyle(
        name="SampleTitle",
        fontName="Helvetica-Bold",
        fontSize=8.3,
        leading=10,
        textColor=colors.HexColor("#111827"),
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="SampleText",
        fontName="Helvetica",
        fontSize=7.4,
        leading=8.8,
        textColor=colors.HexColor("#374151"),
    )
)


def bullet(text):
    return Paragraph("• " + text, styles["ResumeBullet"])


story = []
story.append(p("Tamerlan Togysbayev", styles["Name"]))
story.append(p("AI Automation Engineer · Full-Stack AI Systems Builder", styles["Role"]))
story.append(
    p(
        "tamertt931@gmail.com · flowops.agency · github.com/TamerlanTA · Almaty, Kazakhstan · Open to remote",
        styles["Meta"],
    )
)

story.append(p("Summary", styles["Section"]))
story.append(
    p(
        "I build end-to-end automation systems across n8n, Make.com, APIs, LLMs, CRM data models, and full-stack web apps. Recent work includes human-in-the-loop sales pipelines, Telegram command centers, AI website audit generators, Airtable/Linear operating systems, and production AI web products with payments, auth, email, and back-office workflows.",
        styles["BodySmall"],
    )
)

story.append(p("Skills", styles["Section"]))
skills = [
    ("Automation & Orchestration", "n8n, Make.com, Zapier, Google Apps Script, workflow QA, retries, dedupe, error branches"),
    ("AI & LLMs", "OpenAI API / Responses API, Anthropic Claude, Gemini image generation, prompt engineering, structured JSON outputs, multi-agent orchestration"),
    ("Data / CRM", "Airtable, Google Sheets, Supabase/Postgres, MySQL/TiDB, Redis, Drizzle ORM, Linear, Obsidian memory systems"),
    ("Scraping / Prospecting", "Firecrawl search/scrape, Apify, LinkedIn/Upwork lead workflows, website audit generation"),
    ("Frontend / Backend", "React, Next.js, TypeScript, Tailwind CSS, Vite, Node.js, tRPC"),
    ("Messaging / Commerce / Infra", "Telegram Bot API, WhatsApp Business/SellerChat, Kommo CRM, Gmail, Resend, SendGrid, Buffer, Stripe, Vercel, Railway, Git"),
]
table = Table(
    [[p(k, styles["Project"]), p(v, styles["BodyTiny"])] for k, v in skills],
    colWidths=[1.65 * inch, 5.05 * inch],
)
table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ]
    )
)
story.append(table)

story.append(p("Experience", styles["Section"]))
story.append(p("AI Automation Engineer & Founder — FlowOps", styles["Project"]))
story.append(p("2022 – Present · Almaty, Kazakhstan / Remote", styles["Meta"]))
story.append(
    p(
        "Run a small automation and AI integration practice focused on practical business systems: lead generation, CRM automation, approval workflows, AI assistants, and production web apps.",
        styles["BodyTiny"],
    )
)

projects = [
    (
        "FlowOps Client Acquisition OS",
        "Internal agency operating system",
        [
            "Built a multi-channel acquisition architecture around Upwork Radar, LinkedIn Pain Radar, Website Audit Generator, Demo Library, CRM, proposals, and retainer conversion.",
            "Created a FlowOps Airtable CRM structure with Leads, Opportunities, Messages, Audits, Proposals, Clients, Retainers, Demos, and Automation Logs so automations have a stable operating database.",
            "Designed automation rules for dedupe, draft generation, follow-up queues, reply/status intake, proposal building, demo recommendation, weekly CRM health reporting, and won-deal handoff.",
        ],
    ),
    (
        "Pipeline C — AI Website Audit Generator",
        "FlowOps prospecting / outreach automation",
        [
            "Built n8n workflows that use Telegram commands, Firecrawl search/scrape, AI audit generation, CRM writes, Telegram approval cards, and Gmail sending only after explicit approval.",
            "Created a Prague local-field-sales variant: Firecrawl prospecting, locality/aggregator filters, dedupe, Google Sheets queue, OpenAI structured audits, and visit-ready prospect rows.",
            "Hardened workflow imports, node versions, Firecrawl output normalization, Google Sheets mappings, batch caps, diagnostics, and metadata preservation to avoid silent failures.",
        ],
    ),
    (
        "LinkedIn Outreach Automation",
        "Personal / agency prospecting",
        [
            "Built six n8n workflows covering lead discovery via Apify, daily message generation with Claude Haiku, Google Sheets queue/state, Telegram approval, Sourcegeek sending, follow-ups, reply monitoring, and daily stats.",
            "Solved production constraints such as Telegram callback timeouts, Sourcegeek connection-request limits, n8n Set-node limitations, Anthropic output parsing, and Google Sheets matching-column updates.",
        ],
    ),
    (
        "AI Content Bot",
        "Telegram command center for content ops",
        [
            "Built a Telegram-first command center backed by n8n workflows for topic discovery, morning briefing, AI post generation, Gemini image generation, approval controls, publishing flow, and stats collection.",
            "Centralized callback routing through a single Telegram Trigger so one bot can handle messages, inline buttons, outreach queue actions, and content approval without trigger conflicts.",
        ],
    ),
    (
        "Linear Ops Automation System",
        "Execution layer design for FlowOps",
        [
            "Designed a six-workflow Linear automation layer: Daily Command Center, Blocked Decision Bot, Team Assignment Notifier, Stale Issue Reminder, Linear-to-Obsidian Memory Sync, and Weekly FlowOps Review.",
            "Defined operating rules for Linear as execution source, Obsidian as long-term memory, Telegram as decision surface, and n8n as the automation engine.",
        ],
    ),
    (
        "StoreHouse n8n Warehouse Automation",
        "Inventory / invoice automation",
        [
            "Generated and validated three n8n workflows: AI invoice/photo recognition, low-stock alerts, and suspicious activity monitoring.",
            "Implemented Telegram photo/text intake, OpenAI Vision parsing, confidence checks, StoreHouse API handoff assumptions, cursor-based dedupe, dynamic chat IDs, error branches, and Google Sheets logging.",
        ],
    ),
]

for title, meta, bullets in projects:
    story.append(KeepTogether([p(title, styles["Project"]), p(meta, styles["Meta"])] + [bullet(b) for b in bullets]))

story.append(p("Selected Product & Client Builds", styles["Section"]))
client_projects = [
    (
        "AI-Powered Woven Label Generator — Griffes Vivienne (France)",
        [
            "Built a production AI product where users upload a brand/logo, choose material, color, size, and order mode, then receive a realistic woven-label mockup.",
            "Implemented Next.js/React, tRPC, Drizzle, MySQL/Railway, Vercel, Stripe checkout, credit packs, guest free-trial gating, Resend quote/preorder emails, bilingual FR/EN i18n, Clerk auth styling, admin sales/ops visibility, and asset retrieval.",
            "Hardened AI generation with input validation, upload-size safeguards, product-photo/logo interpretation, white-logo contrast handling, generation error taxonomy, credit-safety tests, R2 storage fallback behavior, SEO/legal pages, and MOQ/business-rule updates.",
        ],
    ),
    (
        "WhatsApp AI Bot — Traffic Fine Disputes (Colombia)",
        [
            "Built an end-to-end intake and response automation for fotomulta cases: WhatsApp message intake, Redis session checks, Supabase conversation history, Kommo CRM lookup, government-database scraping sub-workflow, and structured AI response.",
            "Built a separate outbound pipeline: Google Sheets → Google Apps Script webhook → Make.com → SellerChat → WhatsApp templates. Main n8n workflow runs 128 nodes.",
        ],
    ),
    (
        "FlowOps Agency Website — flowops.agency",
        [
            "Built the agency homepage around a live AI-generated automation architecture diagram: visitor describes an automation need, backend calls OpenAI Responses API with a structured schema, and deterministic fallback handles staging/no-key cases.",
            "Lead capture routes into Telegram, Google Sheets, and SendGrid, turning the website into both a portfolio surface and an inbound workflow.",
        ],
    ),
]
for title, bullets in client_projects:
    story.append(KeepTogether([p(title, styles["Project"])] + [bullet(b) for b in bullets]))

story.append(p("Freelance", styles["Section"]))
story.append(
    p(
        "Independent automation and integration work through Upwork and direct clients: CRM connections, API integrations, low-code/no-code workflow builds, AI agents, and operations automations for small businesses.",
        styles["BodyTiny"],
    )
)

story.append(p("Education", styles["Section"]))
story.append(p("Kazakh-British Technical University (KBTU)", styles["Project"]))
story.append(p("Bachelor’s in Information Systems · 2021 · Almaty, Kazakhstan", styles["BodyTiny"]))

story.append(PageBreak())
story.append(p("Work Samples", styles["Section"]))
story.append(
    p(
        "Suggested screenshot slots for the visual portfolio page. Replace placeholders with real screenshots from n8n, Airtable/Sheets, Telegram, Linear, Vercel/admin screens, and shipped product UI.",
        styles["BodyTiny"],
    )
)

sample_rows = [
    (
        "Pipeline C — Website Audit Generator",
        "n8n overview showing Telegram trigger, Firecrawl search/scrape, AI audit, CRM/Sheets write, Telegram approval, and Gmail send path.",
    ),
    (
        "Pipeline C Prague — Visit-Ready Prospects",
        "Google Sheets / Airtable output with business type, website, address/neighborhood, pain signal, fit score, and next action.",
    ),
    (
        "FlowOps CRM",
        "Airtable base view showing Leads, Opportunities, Messages, Audits, Proposals, Clients, Retainers, Demos, and Automation Logs.",
    ),
    (
        "LinkedIn Outreach — Telegram Approval",
        "Telegram card with approve/skip buttons plus the n8n WF-05 approval flow that sends via Sourcegeek and loops to the next lead.",
    ),
    (
        "AI Content Bot — Command Center",
        "Telegram command or inline-button flow + n8n WF-06 showing routing to content generation, stats, topic discovery, and outreach tools.",
    ),
    (
        "Linear Ops Automation System",
        "Linear project/issues view or n8n prototype/spec screen showing Daily Command Center / Blocked Decision Bot / stale reminder workflows.",
    ),
    (
        "Griffes Vivienne — Result + Quote Flow",
        "Generated woven-label result, quote/preorder CTA, admin preorder/asset visibility, or Resend quote email proof.",
    ),
    (
        "WhatsApp Traffic Fines Bot",
        "Main 128-node n8n workflow or a sanitized WhatsApp/SellerChat flow showing intake, CRM lookup, scrape sub-flow, and AI response.",
    ),
    (
        "StoreHouse Warehouse Bot",
        "n8n workflow showing Telegram photo intake, OpenAI Vision parsing, StoreHouse API handoff, confidence check, and Sheets log.",
    ),
]
cards = []
for title, desc in sample_rows:
    cards.append([p(title, styles["SampleTitle"]), p(desc, styles["SampleText"])])

sample_table = Table(cards, colWidths=[2.1 * inch, 4.6 * inch])
sample_table.setStyle(
    TableStyle(
        [
            ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD5E1")),
            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F8FAFC")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]
    )
)
story.append(sample_table)

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    rightMargin=0.75 * inch,
    leftMargin=0.75 * inch,
    topMargin=0.62 * inch,
    bottomMargin=0.55 * inch,
)
doc.build(story)
print(OUT)
