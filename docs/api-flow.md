# API Flow Documentation

This document explains how requests move through the AI Sales Intelligence Agent system.

It covers:
- Request lifecycle
- Agent execution flow
- Service interactions
- Response generation
- Internal processing architecture

---

# High-Level Request Flow

```text id="c9q7nm"
Frontend UI
    ↓
FastAPI API Route
    ↓
Request Validation
    ↓
Agent Orchestrator
    ↓
Research Agent
    ↓
Enrichment Agent
    ↓
Scoring Agent
    ↓
Outreach Agent
    ↓
Response Aggregation
    ↓
Structured JSON Response
    ↓
Frontend Dashboard
```

---

# API Architecture

The backend follows a layered architecture:

```text id="mw6q2f"
Routes Layer
    ↓
Agents Layer
    ↓
Services Layer
    ↓
Scrapers / LLM Providers
    ↓
Database Layer
```

Each layer has a clearly defined responsibility.

---

# Request Lifecycle

# Step 1 — User Submission

The user submits:
- Company name
or
- Company URL

Example:

```json id="8b2c4n"
{
  "company": "stripe.com"
}
```

The frontend sends a POST request to:

```http id="v2x5q1"
POST /api/research
```

---

# Step 2 — FastAPI Route Handling

Route file:

```text id="7g4m1x"
backend/app/api/routes/research.py
```

Responsibilities:
- Parse request body
- Validate payload
- Trigger orchestrator
- Return structured response

Example flow:

```python id="dr0xg8"
@router.post("/research")
async def research_company(payload: ResearchRequest):
    result = await orchestrator.run(payload.company)
    return result
```

---

# Step 3 — Request Validation

Validation is handled using Pydantic schemas.

Schema location:

```text id="k1v8fj"
backend/app/schemas/research_schema.py
```

Example:

```python id="o4h9pl"
class ResearchRequest(BaseModel):
    company: str
```

Validation ensures:
- Required fields exist
- Correct types are provided
- Invalid payloads are rejected early

---

# Step 4 — Agent Orchestrator

File:

```text id="7m2fka"
backend/app/agents/orchestrator.py
```

Purpose:
Coordinate all AI agents.

Execution pipeline:

```text id="l6v0tw"
Research Agent
    ↓
Enrichment Agent
    ↓
Scoring Agent
    ↓
Outreach Agent
```

The orchestrator:
- passes shared context
- handles sequencing
- aggregates results
- manages failures

---

# Step 5 — Research Agent Flow

File:

```text id="5f8r2u"
backend/app/agents/research_agent.py
```

Responsibilities:
- Website scraping
- Business extraction
- Company summarization
- Industry identification

Flow:

```text id="x3k1rt"
Company URL
    ↓
Website Scraper
    ↓
HTML Extraction
    ↓
LLM Analysis
    ↓
Structured Company Profile
```

Example output:

```json id="b9p4za"
{
  "company_name": "Stripe",
  "industry": "FinTech",
  "summary": "Online payment infrastructure platform"
}
```

---

# Step 6 — Enrichment Agent Flow

File:

```text id="0x8fme"
backend/app/agents/enrichment_agent.py
```

Responsibilities:
- Hiring signal detection
- News analysis
- Growth detection
- Tech stack extraction

Data sources:
- Careers pages
- Job boards
- RSS feeds
- Public metadata

Flow:

```text id="s6w2kp"
Company Profile
    ↓
Jobs Scraper
News Scraper
Tech Stack Scraper
    ↓
Enriched Intelligence
```

Example output:

```json id="c5n1tw"
{
  "hiring_signals": [
    "Hiring AI Engineers",
    "Expanding sales team"
  ],
  "tech_stack": [
    "React",
    "AWS",
    "Segment"
  ]
}
```

---

# Step 7 — Scoring Agent Flow

File:

```text id="4p9xzf"
backend/app/agents/scoring_agent.py
```

Responsibilities:
- ICP evaluation
- Lead qualification
- Score calculation

Scoring Inputs:
- Company profile
- Hiring signals
- Growth indicators
- Tech stack

Example logic:

```text id="w8v5oj"
ICP Match         → 40%
Hiring Signals    → 25%
Growth Indicators → 20%
Tech Relevance    → 15%
```

Example output:

```json id="j0n3uv"
{
  "lead_score": 86,
  "qualification": "High Priority"
}
```

---

# Step 8 — Outreach Agent Flow

File:

```text id="h5s8dx"
backend/app/agents/outreach_agent.py
```

Responsibilities:
- Personalized email generation
- LinkedIn message generation
- Follow-up creation

Inputs:
- Company research
- Pain points
- Hiring trends
- Lead score

Flow:

```text id="t7y1lm"
Research Context
    ↓
Prompt Templates
    ↓
LLM Service
    ↓
Personalized Outreach
```

Example output:

```json id="r9v3fe"
{
  "cold_email": "...",
  "linkedin_message": "...",
  "follow_up": "..."
}
```

---

# Step 9 — Response Aggregation

The orchestrator combines all outputs into a single structured response.

Final structure:

```json id="n1x6zw"
{
  "company": {},
  "hiring_signals": [],
  "growth_signals": [],
  "tech_stack": [],
  "lead_score": 0,
  "qualification": "",
  "outreach": {},
  "report": {}
}
```

---

# Step 10 — Frontend Rendering

Frontend receives the JSON response and renders:

- Company overview
- Lead score cards
- Hiring signals
- Outreach messages
- Intelligence reports

Relevant frontend components:

```text id="m4c8zk"
components/dashboard/
components/reports/
```

---

# Internal Services Flow

# LLM Service

File:

```text id="v0j4ny"
backend/app/services/llm_service.py
```

Responsibilities:
- Model abstraction
- Prompt execution
- Provider switching
- Retry handling

Supported Providers:
- Ollama
- Groq API

---

# Scrape Service

File:

```text id="e8u2sq"
backend/app/services/scrape_service.py
```

Responsibilities:
- Website fetching
- HTML parsing
- Data extraction
- Async requests

---

# Scoring Service

File:

```text id="z2n7bh"
backend/app/services/scoring_service.py
```

Responsibilities:
- Score normalization
- ICP weighting
- Ranking logic

---

# Outreach Service

File:

```text id="q9r5dc"
backend/app/services/outreach_service.py
```

Responsibilities:
- Prompt formatting
- Message generation
- Personalization logic

---

# Database Flow

Database:
- SQLite

Current Usage:
- Lead storage
- Report persistence
- Activity logging

Future:
- PostgreSQL
- Vector database
- Multi-tenant storage

---

# Async Processing Model

The backend uses async-first architecture.

Benefits:
- Parallel scraping
- Faster execution
- Better scalability

Async operations include:
- Website scraping
- News fetching
- LLM requests
- Agent execution

---

# Error Handling Strategy

The system uses:
- Route-level validation
- Service-level exception handling
- Agent fallback responses
- Structured API errors

Example:

```json id="7x3kpl"
{
  "error": true,
  "message": "Unable to scrape company website"
}
```

---

# Future API Improvements

Planned upgrades:

- Background job queues
- Streaming responses
- WebSocket updates
- Batch processing
- Authentication
- Rate limiting
- API versioning

---

# Example End-to-End Flow

```text id="6v9mxa"
User submits company URL
        ↓
FastAPI validates request
        ↓
Orchestrator starts workflow
        ↓
Research Agent scrapes website
        ↓
Enrichment Agent detects signals
        ↓
Scoring Agent ranks lead
        ↓
Outreach Agent generates messaging
        ↓
Structured report returned
        ↓
Frontend displays intelligence dashboard
```

---

# Design Philosophy

The API architecture is designed for:
- modularity
- scalability
- maintainability
- AI-native workflows
- production-grade extensibility

Each agent and service can evolve independently without affecting the entire system.

```