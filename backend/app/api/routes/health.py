from fastapi import APIRouter

from app.core.constants import APP_VERSION

router = APIRouter()


@router.get(
    "/health",
    summary="Health Check",
)
async def health_check():
    """
    Basic API health check endpoint.
    """

    return {
        "status": "ok",
        "service": "AI Sales Intelligence Agent",
        "version": APP_VERSION,
    }