"""
Application-wide constants.
"""

# =========================================================
# APP
# =========================================================

APP_VERSION = "1.0.0"

# =========================================================
# API
# =========================================================

API_PREFIX = "/api"

# =========================================================
# AGENTS
# =========================================================

RESEARCH_AGENT = "research_agent"
ENRICHMENT_AGENT = "enrichment_agent"
SCORING_AGENT = "scoring_agent"
OUTREACH_AGENT = "outreach_agent"

# =========================================================
# LEAD SCORING
# =========================================================

MAX_LEAD_SCORE = 100

ICP_MATCH_WEIGHT = 0.40
HIRING_SIGNAL_WEIGHT = 0.25
GROWTH_SIGNAL_WEIGHT = 0.20
TECH_STACK_WEIGHT = 0.15

# =========================================================
# LEAD QUALIFICATION
# =========================================================

HIGH_PRIORITY_THRESHOLD = 80
MEDIUM_PRIORITY_THRESHOLD = 50

LEAD_QUALIFICATIONS = {
    "HIGH": "High Priority",
    "MEDIUM": "Medium Priority",
    "LOW": "Low Priority",
}

# =========================================================
# SCRAPING
# =========================================================

DEFAULT_REQUEST_TIMEOUT = 30

SUPPORTED_CONTENT_TYPES = [
    "text/html",
    "application/xhtml+xml",
]

# =========================================================
# TECH STACK DETECTION
# =========================================================

COMMON_FRONTEND_TECH = [
    "React",
    "Next.js",
    "Vue",
    "Angular",
    "TailwindCSS",
]

COMMON_BACKEND_TECH = [
    "Node.js",
    "FastAPI",
    "Django",
    "Flask",
    "Express",
]

COMMON_CLOUD_TECH = [
    "AWS",
    "GCP",
    "Azure",
    "Cloudflare",
    "Vercel",
]

# =========================================================
# JOB SIGNAL KEYWORDS
# =========================================================

HIRING_KEYWORDS = [
    "hiring",
    "careers",
    "jobs",
    "join our team",
    "open positions",
]

GROWTH_KEYWORDS = [
    "expanding",
    "growth",
    "funding",
    "scale",
    "launch",
    "new office",
]

# =========================================================
# OUTREACH
# =========================================================

MAX_COLD_EMAIL_LENGTH = 1200
MAX_LINKEDIN_MESSAGE_LENGTH = 300

# =========================================================
# REPORTS
# =========================================================

DEFAULT_REPORT_SECTIONS = [
    "company_overview",
    "hiring_signals",
    "growth_signals",
    "tech_stack",
    "lead_score",
    "outreach",
]

# =========================================================
# LOGGING
# =========================================================

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
    "<cyan>{line}</cyan> - <level>{message}</level>"
)