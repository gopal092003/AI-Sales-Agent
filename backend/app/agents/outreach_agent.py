"""
Outreach Agent.

Responsibilities:
- Personalized outreach generation
- Cold email generation
- LinkedIn messaging
- Follow-up creation
"""

from app.core.logger import setup_logger
from app.schemas.outreach_schema import (
    OutreachContent,
    OutreachRequest,
)
from app.services.outreach_service import (
    outreach_service,
)

logger = setup_logger()


class OutreachAgent:
    """
    Outreach generation agent.
    """

    # =========================================================
    # RUN OUTREACH PIPELINE
    # =========================================================

    async def run(
        self,
        company_name: str,
        industry: str | None,
        company_summary: str | None,
        pain_points: list[str],
        hiring_signals: list[str],
        growth_signals: list[str],
        tech_stack: dict,
        lead_score: float,
        provider: str = "groq",
    ) -> OutreachContent:
        """
        Execute outreach generation pipeline.
        """

        logger.info(
            f"Running outreach agent for "
            f"{company_name}"
        )

        # Flatten tech stack
        all_tech = []

        for values in tech_stack.values():

            if isinstance(values, list):
                all_tech.extend(values)

        all_tech = list(set(all_tech))

        payload = OutreachRequest(
            company_name=company_name,
            industry=industry,
            company_summary=company_summary,
            pain_points=pain_points,
            hiring_signals=hiring_signals,
            growth_signals=growth_signals,
            tech_stack=all_tech,
            lead_score=lead_score,
        )

        outreach = (
            await outreach_service.generate_outreach(
                payload=payload,
                provider=provider,
            )
        )

        logger.info(
            f"Outreach generated for "
            f"{company_name}"
        )

        return outreach


# Singleton instance
outreach_agent = OutreachAgent()