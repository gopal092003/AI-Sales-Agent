"""
Lead scoring service.

Responsibilities:
- ICP scoring
- Hiring signal scoring
- Growth scoring
- Technology relevance scoring
- Final qualification calculation
"""

from app.core.constants import (
    GROWTH_SIGNAL_WEIGHT,
    HIGH_PRIORITY_THRESHOLD,
    HIRING_SIGNAL_WEIGHT,
    ICP_MATCH_WEIGHT,
    LEAD_QUALIFICATIONS,
    MAX_LEAD_SCORE,
    MEDIUM_PRIORITY_THRESHOLD,
    TECH_STACK_WEIGHT,
)
from app.core.logger import setup_logger

logger = setup_logger()


class ScoringService:
    """
    Lead scoring engine.
    """

    # =========================================================
    # ICP SCORE
    # =========================================================

    def calculate_icp_score(
        self,
        icp_fit: bool,
    ) -> float:
        """
        Calculate ICP fit score.
        """

        return (
            ICP_MATCH_WEIGHT * MAX_LEAD_SCORE
            if icp_fit
            else 0
        )

    # =========================================================
    # HIRING SIGNAL SCORE
    # =========================================================

    def calculate_hiring_score(
        self,
        hiring_signals: list[str],
    ) -> float:
        """
        Score based on hiring activity.
        """

        if not hiring_signals:
            return 0

        normalized = min(
            len(hiring_signals) / 5,
            1,
        )

        return (
            normalized
            * HIRING_SIGNAL_WEIGHT
            * MAX_LEAD_SCORE
        )

    # =========================================================
    # GROWTH SIGNAL SCORE
    # =========================================================

    def calculate_growth_score(
        self,
        growth_signals: list[str],
    ) -> float:
        """
        Score based on growth indicators.
        """

        if not growth_signals:
            return 0

        normalized = min(
            len(growth_signals) / 5,
            1,
        )

        return (
            normalized
            * GROWTH_SIGNAL_WEIGHT
            * MAX_LEAD_SCORE
        )

    # =========================================================
    # TECH STACK SCORE
    # =========================================================

    def calculate_tech_score(
        self,
        tech_stack: list[str],
    ) -> float:
        """
        Score based on relevant technologies detected.
        """

        if not tech_stack:
            return 0

        normalized = min(
            len(tech_stack) / 8,
            1,
        )

        return (
            normalized
            * TECH_STACK_WEIGHT
            * MAX_LEAD_SCORE
        )

    # =========================================================
    # FINAL LEAD SCORE
    # =========================================================

    def calculate_total_score(
        self,
        icp_fit: bool,
        hiring_signals: list[str],
        growth_signals: list[str],
        tech_stack: list[str],
    ) -> float:
        """
        Calculate total lead score.
        """

        score = (
            self.calculate_icp_score(icp_fit)
            + self.calculate_hiring_score(
                hiring_signals
            )
            + self.calculate_growth_score(
                growth_signals
            )
            + self.calculate_tech_score(
                tech_stack
            )
        )

        final_score = round(
            min(score, MAX_LEAD_SCORE),
            2,
        )

        logger.info(
            f"Calculated lead score: {final_score}"
        )

        return final_score

    # =========================================================
    # LEAD QUALIFICATION
    # =========================================================

    def get_lead_qualification(
        self,
        score: float,
    ) -> str:
        """
        Convert score into qualification category.
        """

        if score >= HIGH_PRIORITY_THRESHOLD:
            return LEAD_QUALIFICATIONS["HIGH"]

        if score >= MEDIUM_PRIORITY_THRESHOLD:
            return LEAD_QUALIFICATIONS["MEDIUM"]

        return LEAD_QUALIFICATIONS["LOW"]


# Singleton instance
scoring_service = ScoringService()