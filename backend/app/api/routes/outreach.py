from fastapi import APIRouter, HTTPException, status

from app.core.logger import setup_logger
from app.schemas.outreach_schema import (
    OutreachRequest,
)
from app.services.outreach_service import (
    outreach_service,
)

router = APIRouter()

logger = setup_logger()


@router.post(
    "/outreach",
    summary="Generate Personalized Outreach",
)
async def generate_outreach(
    payload: OutreachRequest,
):
    """
    Generate:
    - cold email
    - LinkedIn message
    - follow-up message
    """

    try:
        logger.info(
            f"Outreach generation request for "
            f"{payload.company_name}"
        )

        outreach = (
            await outreach_service.generate_outreach(
                payload=payload,
            )
        )

        return {
            "success": True,
            "data": {
                "company_name": (
                    payload.company_name
                ),
                "lead_score": (
                    payload.lead_score
                ),
                "outreach": {
                    "cold_email": (
                        outreach.cold_email
                    ),
                    "linkedin_message": (
                        outreach.linkedin_message
                    ),
                    "follow_up_message": (
                        outreach.follow_up_message
                    ),
                },
            },
        }

    except Exception as exc:
        logger.error(
            f"Outreach generation failed: {exc}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )