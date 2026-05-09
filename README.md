# AI Sales Intelligence Agent

An AI-native multi-agent sales intelligence system that autonomously researches companies, detects growth signals, scores leads, and generates personalized outreach using LLM-powered reasoning pipelines.

---

# Overview

This project simulates a modern AI SDR (Sales Development Representative) workflow.

The system can:

- Research companies in real time
- Extract hiring and growth signals
- Analyze technology stacks
- Score leads based on ICP fit
- Generate personalized cold outreach
- Produce structured sales intelligence reports

The architecture is designed to mimic real-world AI GTM systems used in modern startups.

---

# Core Features

## Company Research Agent
- Website analysis
- Business model extraction
- Industry classification
- Company summarization

## Hiring & Growth Signal Detection
- Job posting analysis
- Expansion signal tracking
- Hiring trend extraction

## Tech Stack Analysis
- Detect frontend/backend technologies
- Identify analytics and CRM tools
- Cloud infrastructure detection

## Lead Scoring Engine
Scores leads using:
- ICP alignment
- Hiring velocity
- Growth indicators
- Technology relevance

## AI Outreach Generator
Generates:
- Cold emails
- LinkedIn outreach
- Follow-ups
- Personalized messaging

## Sales Intelligence Reports
Structured reports including:
- Company overview
- Pain points
- Opportunity analysis
- Outreach strategy
- Lead score

## Multi-Agent Orchestration
Agents:
- Research Agent
- Enrichment Agent
- Scoring Agent
- Outreach Agent

---

# Tech Stack

## Frontend
- Next.js
- TypeScript
- TailwindCSS
- shadcn/ui

## Backend
- FastAPI
- SQLite
- Async Python

## AI / LLM
- Ollama
- Groq API
- Llama 3
- Qwen2.5
- DeepSeek-R1

## Scraping
- BeautifulSoup
- Playwright
- RSS feeds
- Job board parsing

## Deployment
- Vercel
- Render / Railway

---

# Project Architecture

```text
Frontend (Next.js)
        ↓
FastAPI Backend
        ↓
Agent Orchestrator
        ↓
Research Agent
Enrichment Agent
Scoring Agent
Outreach Agent
        ↓
Services Layer
        ↓
Scrapers + LLM Services
        ↓
Structured Intelligence Report
```

---

# Folder Structure

```text
ai-sales-agent/
│
├── frontend/          # Next.js frontend
├── backend/           # FastAPI backend
├── docs/              # Architecture & deployment docs
│
├── README.md
├── .gitignore
└── LICENSE
```

---

# Local Development Setup

# 1. Clone Repository

```bash
git clone https://github.com/yourusername/ai-sales-agent.git
cd ai-sales-agent
```

---

# 2. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# 3. Backend Setup

```bash
cd backend

python -m venv venv
```

Activate virtual environment:

## Windows

```bash
venv\Scripts\activate
```

## Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# Environment Variables

## Frontend

Create:

```text
frontend/.env.local
```

Example:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Backend

Create:

```text
backend/.env
```

Example:

```env
APP_NAME=AI Sales Intelligence Agent
DEBUG=True

GROQ_API_KEY=your_api_key

OLLAMA_BASE_URL=http://localhost:11434
```

---

# API Endpoints

## Health Check

```http
GET /api/health
```

## Company Research

```http
POST /api/research
```

## Outreach Generation

```http
POST /api/outreach
```

## Reports

```http
GET /api/reports
```

---

# Development Roadmap

## Phase 1
- Backend foundation
- Frontend setup
- Health APIs
- Database setup

## Phase 2
- Website scraping
- Company research agent
- LLM integration

## Phase 3
- Hiring signal detection
- Lead scoring engine
- Outreach generation

## Phase 4
- Dashboard UI
- Reports system
- Deployment

## Phase 5
- CRM integration
- Batch processing
- Multi-agent memory
- Vector search

---

# Deployment

## Frontend
Deploy on:
- Vercel

## Backend
Deploy on:
- Render
- Railway

---

# Future Improvements

- CRM integrations
- Chrome extension
- Email automation
- Multi-company enrichment
- AI memory systems
- Vector search pipelines

---

# Resume Bullet

> Built an AI-native sales intelligence system that autonomously performs company research, lead scoring, and personalized outreach generation using multi-agent orchestration, real-time web scraping, and LLM-based reasoning pipelines.

---

# License

MIT License

---

# Author

Your Name

```