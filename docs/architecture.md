# System Architecture

This document explains the architecture and internal workflow of the AI Sales Intelligence Agent.

---

# High-Level Architecture

```text id="wgnj9u"
                    ┌─────────────────────┐
                    │     Frontend UI     │
                    │      Next.js        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    │   Request Handling  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Agent Orchestrator │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
┌──────────────┐     ┌────────────────┐     ┌────────────────┐
│ Research     │     │ Enrichment     │     │ Scoring Agent  │
│ Agent         │     │ Agent          │     │                │
└──────┬───────┘     └──────┬─────────┘     └──────┬─────────┘
       │                    │                       │
       ▼                    ▼                       ▼
┌──────────────┐     ┌────────────────┐     ┌────────────────┐
│ Website      │     │ Jobs Scraper   │     │ ICP Evaluation │
│ Scraper      │     │ News Scraper   │     │ Lead Scoring   │
│ LLM Analysis │     │ Tech Detection │     │ Ranking Logic  │
└──────────────┘     └────────────────┘     └────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Outreach Agent     │
                    │  LLM Personalization│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Structured Reports  │
                    │ Outreach Messages   │
                    │ Lead Intelligence   │
                    └─────────────────────┘
```

---

# Architecture Goals

The system is designed to:

- Support multi-agent orchestration
- Keep services modular and replaceable
- Enable async scraping and processing
- Separate AI reasoning from scraping logic
- Allow future scalability without major rewrites
- Maintain production-grade backend structure

---

# Core System Components

# 1. Frontend Layer

Technology:
- Next.js
- TypeScript
- TailwindCSS
- shadcn/ui

Responsibilities:
- User interaction
- Dashboard rendering
- Report visualization
- Lead management UI
- API communication

Frontend communicates with the backend using REST APIs.

---

# 2. API Layer (FastAPI)

The FastAPI server acts as the central entry point.

Responsibilities:
- Route handling
- Request validation
- Authentication (future)
- Agent orchestration triggering
- Response formatting

Main routes:

```text id="f50z4m"
/api/health
/api/research
/api/outreach
/api/reports
```

---

# 3. Agent Orchestrator

The orchestrator coordinates all AI agents.

Responsibilities:
- Pipeline execution
- Context passing
- Async task coordination
- Error handling
- Result aggregation

Execution Flow:

```text id="8oh44d"
Research Agent
      ↓
Enrichment Agent
      ↓
Scoring Agent
      ↓
Outreach Agent
      ↓
Final Report Generator
```

The orchestrator is intentionally separated from individual agents to maintain scalability and flexibility.

---

# 4. Research Agent

Purpose:
Extract foundational company intelligence.

Responsibilities:
- Website scraping
- Company summarization
- Business model extraction
- Industry classification
- ICP signal detection

Input:
- Company name
- Company URL

Output:
- Structured company profile

---

# 5. Enrichment Agent

Purpose:
Gather external intelligence signals.

Responsibilities:
- Hiring signal detection
- Job board analysis
- Growth signal extraction
- News aggregation
- Tech stack detection

Data Sources:
- Company websites
- Job boards
- RSS feeds
- Public metadata

Output:
- Hiring insights
- Growth indicators
- Technology stack

---

# 6. Scoring Agent

Purpose:
Evaluate lead quality.

Responsibilities:
- ICP matching
- Growth scoring
- Hiring velocity scoring
- Technology relevance scoring
- Composite lead scoring

Example scoring categories:

| Category | Weight |
|---|---|
| ICP Match | 40% |
| Hiring Signals | 25% |
| Growth Indicators | 20% |
| Tech Relevance | 15% |

Output:
- Numerical lead score
- Lead qualification label

---

# 7. Outreach Agent

Purpose:
Generate personalized outbound messaging.

Responsibilities:
- Cold email generation
- LinkedIn outreach generation
- Follow-up creation
- Pain-point personalization

Input Context:
- Company research
- Hiring signals
- Tech stack
- Growth indicators
- Lead score

LLM Output:
- Personalized messaging
- Outreach variants

---

# 8. Services Layer

The services layer abstracts reusable business logic.

Structure:

```text id="hfz2o6"
services/
├── llm_service.py
├── scrape_service.py
├── scoring_service.py
├── lead_service.py
└── outreach_service.py
```

Purpose:
- Reusability
- Clean separation of concerns
- Easier testing
- Easier model/provider swapping

---

# 9. Scraper Layer

Dedicated scraping modules isolate extraction logic.

Structure:

```text id="rls1c8"
scrapers/
├── website_scraper.py
├── jobs_scraper.py
├── news_scraper.py
└── techstack_scraper.py
```

Responsibilities:
- HTML extraction
- Metadata parsing
- Job detection
- Technology fingerprinting

---

# 10. LLM Layer

The LLM layer abstracts AI providers.

Supported Providers:
- Ollama
- Groq API

Supported Models:
- Llama 3
- Qwen2.5
- DeepSeek-R1

Responsibilities:
- Prompt execution
- Response parsing
- Retry handling
- Provider abstraction

This allows switching between:
- local models
- cloud inference
- future providers

without changing agent logic.

---

# Data Flow

# Input Stage

User submits:
- Company name
or
- Company website URL

---

# Processing Stage

The orchestrator launches:

1. Research pipeline
2. Enrichment pipeline
3. Lead scoring pipeline
4. Outreach generation pipeline

---

# Output Stage

System returns:

```json id="1f5x7m"
{
  "company": {},
  "hiring_signals": [],
  "growth_signals": [],
  "tech_stack": [],
  "lead_score": 87,
  "outreach_messages": [],
  "report": {}
}
```

---

# Database Architecture

Current Database:
- SQLite

Reason:
- Zero-cost setup
- Simplicity
- Local development speed

Future Upgrade Options:
- PostgreSQL
- Supabase
- Neon

---

# Async Architecture

The backend is designed using async-first patterns.

Benefits:
- Faster scraping
- Parallel requests
- Better scalability
- Improved responsiveness

Used In:
- Scrapers
- API routes
- Agent orchestration

---

# Scalability Design

The architecture supports future upgrades including:

- Multi-company batch processing
- CRM integrations
- Vector databases
- Memory systems
- Queue workers
- Distributed agents
- Real-time notifications

---

# Security Considerations

Planned security improvements:
- API authentication
- Rate limiting
- Request validation
- Secret management
- Prompt injection mitigation

---

# Deployment Architecture

# Frontend

Platform:
- Vercel

---

# Backend

Platforms:
- Render
- Railway

---

# Local AI Models

Platform:
- Ollama

---

# Future Architecture Enhancements

Planned improvements:

- Celery / Redis workers
- Event-driven pipelines
- Agent memory systems
- Semantic search
- Embedding storage
- Multi-tenant support
- Workflow persistence

---

# Engineering Philosophy

This project focuses on:

- AI-native architecture
- Real-world production structure
- Modular engineering
- Practical automation
- Clean scalability

The goal is to simulate how modern AI-first startups build GTM intelligence systems.

```