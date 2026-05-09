# Deployment Guide

This document explains how to deploy the AI Sales Intelligence Agent.

Deployment architecture:

- Frontend → Vercel
- Backend → Render or Railway
- Database → SQLite (initially)
- AI Models → Ollama locally or Groq API remotely

---

# Deployment Overview

```text id="0x5c1m"
Frontend (Next.js)
        ↓
Vercel Hosting
        ↓
FastAPI Backend
        ↓
Render / Railway
        ↓
SQLite Database
        ↓
Groq API / Ollama
```

---

# Production Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js |
| Backend | FastAPI |
| Hosting | Vercel + Render |
| Database | SQLite |
| AI Provider | Groq API |
| Local AI | Ollama |

---

# Environment Variables

# Frontend Environment Variables

File:

```text id="v1x4nh"
frontend/.env.local
```

Example:

```env id="5u8n3y"
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Production:

```env id="j8k2qp"
NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
```

---

# Backend Environment Variables

File:

```text id="o7f3wa"
backend/.env
```

Example:

```env id="9m2rxt"
APP_NAME=AI Sales Intelligence Agent
DEBUG=False

GROQ_API_KEY=your_groq_api_key

OLLAMA_BASE_URL=http://localhost:11434

DATABASE_URL=sqlite:///./sales_agent.db
```

---

# Frontend Deployment (Vercel)

# Step 1 — Push Repository to GitHub

```bash id="g6v2rz"
git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin https://github.com/yourusername/ai-sales-agent.git

git push -u origin main
```

---

# Step 2 — Import Project into Vercel

Go to:
- https://vercel.com

Then:
1. Import GitHub repository
2. Select `frontend/` as root directory
3. Configure environment variables
4. Deploy

---

# Step 3 — Configure Build Settings

Recommended:

| Setting | Value |
|---|---|
| Framework | Next.js |
| Root Directory | frontend |
| Build Command | npm run build |
| Output Directory | .next |

---

# Step 4 — Add Environment Variables

Add:

```env id="4c7pjs"
NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com
```

---

# Backend Deployment (Render)

# Step 1 — Create Render Account

Go to:
- https://render.com

---

# Step 2 — Create New Web Service

Connect GitHub repository.

Select:
- Root Directory → `backend`

---

# Step 3 — Configure Build Settings

| Setting | Value |
|---|---|
| Runtime | Python |
| Build Command | pip install -r requirements.txt |
| Start Command | bash start.sh |

---

# Step 4 — Add Environment Variables

Add:

```env id="2f8qwk"
APP_NAME=AI Sales Intelligence Agent
DEBUG=False

GROQ_API_KEY=your_groq_api_key

DATABASE_URL=sqlite:///./sales_agent.db
```

---

# Step 5 — Deploy

Render automatically:
- installs dependencies
- builds backend
- exposes public API URL

Example:

```text id="k9t3px"
https://ai-sales-agent.onrender.com
```

---

# Railway Deployment (Alternative)

# Step 1 — Create Railway Project

Go to:
- https://railway.app

---

# Step 2 — Connect GitHub Repository

Select backend folder.

---

# Step 3 — Add Environment Variables

Same variables as Render.

---

# Step 4 — Deploy

Railway auto-detects:
- Python environment
- dependencies
- startup commands

---

# Backend Start Script

File:

```text id="m1w6zd"
backend/start.sh
```

Recommended content:

```bash id="8p4zjn"
#!/usr/bin/env bash

uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Make executable:

```bash id="n5u8rf"
chmod +x start.sh
```

---

# SQLite Notes

SQLite is used initially because:
- zero cost
- simple setup
- fast development

Limitations:
- not ideal for heavy concurrent writes
- limited scalability

Future upgrade path:
- PostgreSQL
- Supabase
- Neon

---

# Ollama Deployment Strategy

# Local Development

Run Ollama locally:

```bash id="r3x7mv"
ollama serve
```

Pull model:

```bash id="y2k9fj"
ollama pull llama3
```

---

# Production Recommendation

Use:
- Groq API

Reason:
- easier cloud deployment
- no GPU hosting required
- faster inference
- simpler scaling

---

# CORS Configuration

Backend should allow frontend origin.

Example:

```python id="c8m1wy"
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://your-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

# Health Check Endpoint

Required for deployment platforms.

Endpoint:

```http id="0t6zql"
GET /api/health
```

Expected response:

```json id="z4w9pe"
{
  "status": "ok"
}
```

---

# CI/CD Workflow

Deployment pipeline:

```text id="u3f7rh"
Git Push
    ↓
GitHub Repository
    ↓
Automatic Build Trigger
    ↓
Vercel / Render Deployment
    ↓
Production Release
```

Benefits:
- automatic deployment
- faster iteration
- consistent releases

---

# Recommended Production Settings

# Frontend

```env id="p2n5vk"
NODE_ENV=production
```

---

# Backend

```env id="a7m4qs"
DEBUG=False
```

---

# Security Recommendations

Production improvements:

- API authentication
- Rate limiting
- HTTPS only
- Secret rotation
- Environment isolation
- Request validation

---

# Logging Recommendations

Suggested tools:
- Render logs
- Railway logs
- Sentry (future)
- Structured JSON logging

---

# Monitoring Recommendations

Future monitoring stack:
- Prometheus
- Grafana
- Sentry
- OpenTelemetry

---

# Future Infrastructure Upgrades

Planned improvements:

- Dockerization
- Redis queues
- Celery workers
- PostgreSQL
- Vector databases
- Kubernetes deployment
- Multi-agent distributed execution

---

# Dockerization (Future)

Potential architecture:

```text id="f5j8nx"
Frontend Container
Backend Container
Redis Container
Worker Container
Database Container
```

---

# Production Architecture (Future)

```text id="x8q2lm"
Users
   ↓
Vercel Frontend
   ↓
FastAPI API
   ↓
Redis Queue
   ↓
Agent Workers
   ↓
PostgreSQL + Vector DB
```

---

# Deployment Checklist

Before production deployment:

- [ ] Environment variables configured
- [ ] API URLs updated
- [ ] CORS configured
- [ ] Health endpoint working
- [ ] Build passes locally
- [ ] Secrets excluded from git
- [ ] Database initialized
- [ ] Logging enabled

---

# Recommended Initial Deployment Strategy

Best zero-budget setup:

| Component | Platform |
|---|---|
| Frontend | Vercel |
| Backend | Render |
| Database | SQLite |
| AI Provider | Groq API |

This setup minimizes infrastructure complexity while keeping the system production-demo ready.

```