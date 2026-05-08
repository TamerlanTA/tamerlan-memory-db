from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = "/Users/tamerlan/Desktop/Tamerlan_Togysbayev_Business_Owner_Resume.pdf"

INK = colors.HexColor("#111827")
MUTED = colors.HexColor("#4B5563")
FAINT = colors.HexColor("#F3F4F6")
LINE = colors.HexColor("#D8DEE8")
BLUE = colors.HexColor("#2563EB")
GREEN = colors.HexColor("#047857")
AMBER = colors.HexColor("#B45309")
NAVY = colors.HexColor("#101828")
PAPER = colors.HexColor("#FBFCFE")


styles = getSampleStyleSheet()
styles.add(ParagraphStyle("HeroName", fontName="Helvetica-Bold", fontSize=28, leading=31, textColor=colors.white, spaceAfter=6))
styles.add(ParagraphStyle("HeroRole", fontName="Helvetica", fontSize=12.5, leading=15, textColor=colors.HexColor("#DBEAFE"), spaceAfter=8))
styles.add(ParagraphStyle("HeroBody", fontName="Helvetica", fontSize=10.5, leading=14, textColor=colors.HexColor("#F9FAFB"), spaceAfter=8))
styles.add(ParagraphStyle("Contact", fontName="Helvetica", fontSize=8.2, leading=10, textColor=colors.HexColor("#D1D5DB")))
styles.add(ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=12.5, leading=15, textColor=INK, spaceBefore=12, spaceAfter=7))
styles.add(ParagraphStyle("Kicker", fontName="Helvetica-Bold", fontSize=7.5, leading=9, textColor=BLUE, spaceAfter=3))
styles.add(ParagraphStyle("Body", fontName="Helvetica", fontSize=8.7, leading=11.2, textColor=INK, spaceAfter=4))
styles.add(ParagraphStyle("Small", fontName="Helvetica", fontSize=7.8, leading=9.8, textColor=MUTED, spaceAfter=3))
styles.add(ParagraphStyle("Tiny", fontName="Helvetica", fontSize=7.0, leading=8.5, textColor=MUTED, spaceAfter=2))
styles.add(ParagraphStyle("CardTitle", fontName="Helvetica-Bold", fontSize=9.2, leading=11, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle("CaseTitle", fontName="Helvetica-Bold", fontSize=11.2, leading=13.2, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle("Metric", fontName="Helvetica-Bold", fontSize=15.5, leading=17, textColor=INK, alignment=TA_CENTER, spaceAfter=2))
styles.add(ParagraphStyle("MetricLabel", fontName="Helvetica", fontSize=7.2, leading=8.6, textColor=MUTED, alignment=TA_CENTER))
styles.add(ParagraphStyle("Quote", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=colors.HexColor("#0F172A"), spaceAfter=4))
styles.add(ParagraphStyle("SampleTitle", fontName="Helvetica-Bold", fontSize=8.5, leading=10.2, textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle("SampleText", fontName="Helvetica", fontSize=7.2, leading=8.7, textColor=MUTED))


def P(text, style="Body"):
    return Paragraph(text, styles[style])


class Card(Flowable):
    def __init__(self, width, height, fill=colors.white, stroke=LINE, radius=8, title=None):
        super().__init__()
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.radius = radius
        self.title = title

    def draw(self):
        c = self.canv
        c.setFillColor(self.fill)
        c.setStrokeColor(self.stroke)
        c.setLineWidth(0.7)
        c.roundRect(0, 0, self.width, self.height, self.radius, fill=1, stroke=1)
        if self.title:
            c.setFillColor(MUTED)
            c.setFont("Helvetica-Bold", 7)
            c.drawString(10, self.height - 14, self.title)


class ScreenshotSlot(Flowable):
    def __init__(self, width, height, title, subtitle, tag="SCREENSHOT SLOT"):
        super().__init__()
        self.width = width
        self.height = height
        self.title = title
        self.subtitle = subtitle
        self.tag = tag

    def draw(self):
        c = self.canv
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#C7D2FE"))
        c.setLineWidth(0.8)
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=1)
        c.setFillColor(colors.HexColor("#EEF2FF"))
        c.roundRect(9, self.height - 24, 82, 14, 5, fill=1, stroke=0)
        c.setFillColor(BLUE)
        c.setFont("Helvetica-Bold", 5.8)
        c.drawString(15, self.height - 19.5, self.tag)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 8.5)
        title_lines = wrap_text(self.title, self.width - 24, "Helvetica-Bold", 8.5)
        y_title = self.height - 42
        for line in title_lines[:2]:
            c.drawString(12, y_title, line)
            y_title -= 10
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 6.5)
        lines = wrap_text(self.subtitle, self.width - 24, "Helvetica", 6.5)
        y = y_title - 2
        for line in lines[:3]:
            c.drawString(12, y, line)
            y -= 8
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setDash(3, 3)
        c.line(14, 16, self.width - 14, 16)
        c.setDash()


def wrap_text(text, max_width, font, size):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if stringWidth(trial, font, size) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def bullet(text):
    return P("• " + text, "Body")


def small_bullet(text):
    return P("• " + text, "Small")


def draw_header(canvas, doc):
    canvas.saveState()
    if doc.page == 1:
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
    else:
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(0.7 * inch, 10.35 * inch, 7.8 * inch, 10.35 * inch)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7)
        canvas.drawString(0.72 * inch, 10.47 * inch, "Tamerlan Togysbayev — AI Automation Engineer")
        canvas.drawRightString(7.8 * inch, 10.47 * inch, f"Page {doc.page}")
    canvas.restoreState()


def metric_card(value, label):
    return [P(value, "Metric"), P(label, "MetricLabel")]


story = []

# Page 1: Business-owner promise
story.append(P("Tamerlan Togysbayev", "HeroName"))
story.append(P("AI Automation Engineer for owners who want fewer manual processes, faster lead response, and systems that keep running.", "HeroRole"))
story.append(P("I turn messy operations into practical automation systems: CRM pipelines, AI assistants, approval workflows, reporting loops, and customer-facing AI products. I do not just connect tools. I design the business flow, build the automation, add human control where risk matters, and harden the system so it can survive real use.", "HeroBody"))
story.append(P("tamertt931@gmail.com · flowops.agency · github.com/TamerlanTA · Almaty, Kazakhstan · Remote", "Contact"))
story.append(Spacer(1, 0.2 * inch))

metrics = Table(
    [
        [
            metric_card("128", "nodes in WhatsApp legal intake bot"),
            metric_card("24", "search queries per Pipeline C run"),
            metric_card("9", "CRM tables in FlowOps sales OS"),
            metric_card("3", "warehouse automation workflows"),
        ]
    ],
    colWidths=[1.62 * inch] * 4,
)
metrics.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.white),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#334155")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
]))
story.append(metrics)
story.append(Spacer(1, 0.18 * inch))

story.append(P("WHAT I HELP OWNERS FIX", "Kicker"))
owner_pains = Table(
    [
        [P("Slow lead response", "CardTitle"), P("Manual follow-up", "CardTitle"), P("No visibility", "CardTitle")],
        [
            P("New leads sit in inboxes, chats, spreadsheets, or CRM views until someone remembers to act.", "Small"),
            P("Teams lose deals because reminders, drafts, approvals, and status updates live in people's heads.", "Small"),
            P("Owners cannot see what is working, what is blocked, and which client or lead needs attention now.", "Small"),
        ],
        [P("AI without control", "CardTitle"), P("Disconnected tools", "CardTitle"), P("Fragile workflows", "CardTitle")],
        [
            P("AI can draft, score, summarize, and respond, but sensitive steps need approval gates and audit trails.", "Small"),
            P("Telegram, WhatsApp, Airtable, Sheets, Linear, Gmail, CRMs, and web apps need one operating model.", "Small"),
            P("A workflow is only useful if it handles bad data, missing credentials, duplicates, API errors, and retries.", "Small"),
        ],
    ],
    colWidths=[2.08 * inch] * 3,
)
owner_pains.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#E2E8F0")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(owner_pains)
story.append(Spacer(1, 0.16 * inch))

story.append(P("POSITIONING", "Kicker"))
story.append(P("I am strongest when the problem is not simply “build a workflow,” but “make this business process reliable enough that the owner can stop babysitting it.”", "HeroBody"))
story.append(P("Core stack: n8n, Make.com, OpenAI, Claude, Gemini, Firecrawl, Apify, Airtable, Google Sheets, Telegram Bot API, WhatsApp/SellerChat, Kommo, Linear, Obsidian, React/Next.js, TypeScript, Node.js, tRPC, Drizzle, MySQL, Supabase, Stripe, Vercel, Railway.", "HeroBody"))

story.append(PageBreak())

# Page 2: Case studies
story.append(P("Case Studies", "Section"))
story.append(P("Each project below shows the kind of business outcome I build toward: faster response, cleaner operations, safer AI, and clearer owner visibility.", "Body"))

case_data = [
    (
        "FlowOps Client Acquisition OS",
        "Problem: owner-led agency needed a repeatable way to find leads, score opportunities, draft outreach, approve sends, track follow-ups, and keep the CRM clean.",
        [
            "Built the operating model around Upwork Radar, LinkedIn Pain Radar, Website Audit Generator, Demo Library, CRM, proposals, and retainer conversion.",
            "Designed Airtable CRM with Leads, Opportunities, Messages, Audits, Proposals, Clients, Retainers, Demos, and Automation Logs.",
            "Added safety rules: dedupe before writes, AI drafts before sends, approval gates, traceable logs, and weekly health reporting.",
        ],
        "Owner value: turns prospecting from scattered tasks into a sales machine with queue, approval, follow-up, and reporting.",
        "Screenshot: Airtable CRM + Pipeline C n8n overview",
    ),
    (
        "Pipeline C — AI Website Audit Generator",
        "Problem: cold outreach is weak when it sounds generic. Business owners respond better when the message points to a real issue on their website or operations flow.",
        [
            "Built n8n workflows using Telegram command launch, Firecrawl search/scrape, AI audit generation, CRM/Sheets writes, Telegram approval cards, and Gmail send only after Approve + Send.",
            "Created a Prague local-field-sales variant that produces visit-ready prospect rows with address, website, business type, pain signal, fit score, and next action.",
            "Hardened Firecrawl parsing, node imports, batch caps, Google Sheets mapping, aggregator filters, and diagnostic outputs so failures are visible.",
        ],
        "Owner value: generates specific, reviewable outreach assets instead of blank-page prospecting.",
        "Screenshot: Telegram approval card + Visit Ready Prospects table",
    ),
    (
        "AI-Powered Woven Label Generator — Griffes Vivienne",
        "Problem: a fashion supplier needed more than a demo. They needed a user-facing AI product connected to quote/order flow, email, payment logic, and back-office visibility.",
        [
            "Built a production product where users upload brand artwork, choose material/color/size, and receive a realistic woven-label mockup.",
            "Implemented guest trial gating, credits, Stripe checkout, Resend quote emails, bilingual FR/EN UI, Clerk auth styling, admin preorder visibility, asset retrieval, and legal/SEO pages.",
            "Hardened AI generation around upload limits, product-photo/logo interpretation, white-logo contrast, error taxonomy, credit safety, storage fallback, and MOQ business rules.",
        ],
        "Owner value: turns AI generation into a commercial quote funnel, not a toy.",
        "Screenshot: Result page + admin preorder/asset visibility",
    ),
]

for title, problem, bullets, value, shot in case_data:
    left = [P(title, "CaseTitle"), P(problem, "Small")] + [small_bullet(b) for b in bullets] + [P(value, "Quote")]
    right = [ScreenshotSlot(2.1 * inch, 1.15 * inch, shot.split(": ")[1], "Drop real screenshot here. The slot is intentionally sized for n8n, Airtable/Sheets, Telegram, or product UI proof.")]
    t = Table([[left, right]], colWidths=[4.35 * inch, 2.25 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(KeepTogether([t, Spacer(1, 0.1 * inch)]))

story.append(PageBreak())

# Page 3: Portfolio grid + how I work
story.append(P("Automation Portfolio", "Section"))
story.append(P("This is the proof layer I want business owners to see: not abstract skills, but concrete systems with control points, logs, and business context.", "Body"))

portfolio = [
    ("WhatsApp AI Bot — Traffic Fines", "128-node n8n intake/response system: WhatsApp, Redis sessions, Supabase history, Kommo CRM, scraping sub-flow, structured AI response, and outbound Make/SellerChat pipeline."),
    ("LinkedIn Outreach Automation", "Six n8n workflows: Apify lead discovery, Claude-personalized messages, Google Sheets queue, Telegram approval, Sourcegeek sending, follow-up, reply monitoring, daily stats."),
    ("AI Content Bot", "Telegram command center with n8n routing, topic discovery, morning briefing, GPT-4o tools, Gemini image generation, approval controls, publishing flow, and stats."),
    ("StoreHouse Warehouse Automation", "Three validated workflows for invoice/photo recognition, low-stock alerts, and suspicious activity monitoring with cursor dedupe, Telegram intake, OpenAI Vision, and Sheets logs."),
    ("Linear Ops Automation System", "Operating design for daily command center, blocked-decision bot, team assignment notifier, stale issue reminder, Linear-to-Obsidian sync, and weekly FlowOps review."),
    ("FlowOps Agency Website", "Homepage AI architecture generator: visitor describes an automation need, OpenAI Responses API returns structured diagram data, fallback handles staging, leads route to Telegram/Sheets/SendGrid."),
]
rows = []
for i in range(0, len(portfolio), 2):
    row = []
    for title, desc in portfolio[i:i+2]:
        row.append([P(title, "CardTitle"), P(desc, "Small")])
    rows.append(row)

grid = Table(rows, colWidths=[3.25 * inch, 3.25 * inch])
grid.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.white),
    ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#E2E8F0")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
story.append(grid)

story.append(P("How I Build", "Section"))
process = Table(
    [
        [P("1. Map the business flow", "CardTitle"), P("I clarify what should happen, who approves, where data lives, and what can safely be automated.", "Small")],
        [P("2. Build the working path", "CardTitle"), P("I connect APIs/tools, model the CRM or Sheets state, and make the happy path usable quickly.", "Small")],
        [P("3. Add control and resilience", "CardTitle"), P("I add dedupe, retries, logs, error branches, approval gates, and clear owner notifications.", "Small")],
        [P("4. Make it operational", "CardTitle"), P("I leave runbooks, test payloads, validation notes, and memory/handoff context so the system can keep improving.", "Small")],
    ],
    colWidths=[2.2 * inch, 4.3 * inch],
)
process.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
    ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#E2E8F0")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 9),
    ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
]))
story.append(process)

story.append(P("Screenshot Pack Needed", "Section"))
shots = [
    ("Pipeline C n8n canvas", "show Telegram trigger, Firecrawl, OpenAI, CRM/Sheets, approval, Gmail"),
    ("Airtable FlowOps CRM", "show Leads/Opportunities/Messages/Audits/Automation Logs"),
    ("Telegram approval card", "show approve/skip buttons for outreach or content"),
    ("Griffes Vivienne result/admin", "show generated label + quote/admin visibility"),
    ("LinkedIn WF-05 or AI Content WF-06", "show command center / approval routing"),
    ("WhatsApp or StoreHouse n8n canvas", "show one complex client automation as proof"),
]
shot_rows = [[P(name, "SampleTitle"), P(desc, "SampleText")] for name, desc in shots]
shot_table = Table(shot_rows, colWidths=[2.35 * inch, 4.15 * inch])
shot_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EFF6FF")),
    ("BACKGROUND", (1, 0), (1, -1), colors.white),
    ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#E2E8F0")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(shot_table)

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    rightMargin=0.72 * inch,
    leftMargin=0.72 * inch,
    topMargin=0.66 * inch,
    bottomMargin=0.55 * inch,
)
doc.build(story, onFirstPage=draw_header, onLaterPages=draw_header)
print(OUT)
