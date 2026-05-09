"""
Scoring Agent.

Responsibilities:
- ICP evaluation
- Lead score calculation
- Lead qualification
"""

from app.core.logger import setup_logger
from app.services.scoring_service import (
    scoring_service,
)

logger = setup_logger()


class ScoringAgent:
    """
    Lead scoring agent.
    """

    # =========================================================
    # RUN SCORING
    # =========================================================

    async def run(
        self,
        icp_fit: bool,
        hiring_signals: list[str],
        growth_signals: list[str],
        tech_stack: dict,
    ) -> dict:
        """
        Execute scoring pipeline.
        """

        logger.info(
            "Running scoring agent"
        )

        # Flatten tech stack
        all_tech = []

        for values in tech_stack.values():

            if isinstance(values, list):
                all_tech.extend(values)

        # Remove duplicates
        all_tech = list(set(all_tech))

        # Calculate score
        lead_score = (
            scoring_service.calculate_total_score(
                icp_fit=icp_fit,
                hiring_signals=hiring_signals,
                growth_signals=growth_signals,
                tech_stack=all_tech,
            )
        )

        qualification = (
            scoring_service.get_lead_qualification(
                lead_score
            )
        )

        logger.info(
            f"Lead scored: {lead_score}"
        )

        return {
            "lead_score": lead_score,
            "qualification": qualification,
        }


# Singleton instance
scoring_agent = ScoringAgent()