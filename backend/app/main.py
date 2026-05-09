from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from app.api.routes.health import router as health_router
from app.api.routes.reports import router as reports_router
from app.api.routes.research import router as research_router
from app.api.routes.outreach import router as outreach_router
from app.core.config import settings
from app.core.logger import setup_logger

# Initialize logger
logger = setup_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events.
    """

    logger.info("Starting AI Sales Intelligence Agent API...")

    yield

    logger.info("Shutting down AI Sales Intelligence Agent API...")


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    debug=settings.DEBUG,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# ROUTES
# =========================================================

app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Health"],
)

app.include_router(
    research_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Research"],
)

app.include_router(
    outreach_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Outreach"],
)

app.include_router(
    reports_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Reports"],
)


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
async def root():
    return {
        "message": "AI Sales Intelligence Agent API",
        "status": "running",
        "version": "1.0.0",
    }