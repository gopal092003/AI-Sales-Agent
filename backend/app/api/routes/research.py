from fastapi import APIRouter, HTTPException, status

from app.agents.orchestrator import orchestrator
from app.core.logger import setup_logger
from app.schemas.research_schema import (
    ResearchRequest,
)

router = APIRouter()

logger = setup_logger()


@router.post(
    "/research",
    summary="Run Company Research Pipeline",
)
async def research_company(
    payload: ResearchRequest,
):
    """
    Run the full AI sales intelligence workflow.

    Pipeline:
    - Research
    - Enrichment
    - Scoring
    - Outreach generation
    """

    try:
        logger.info(
            f"Research request received for "
            f"{payload.company}"
        )

        result = await orchestrator.run(
            company_url=payload.company,
        )

        return {
            "success": True,
            "data": result,
        }

    except Exception as exc:
        logger.error(
            f"Research pipeline failed: {exc}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )