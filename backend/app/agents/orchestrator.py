"""
Agent Orchestrator.

Responsibilities:
- Coordinate multi-agent execution
- Pass shared context between agents
- Aggregate results
- Return structured intelligence report
"""

from app.agents.enrichment_agent import (
    enrichment_agent,
)
from app.agents.outreach_agent import (
    outreach_agent,
)
from app.agents.research_agent import (
    research_agent,
)
from app.agents.scoring_agent import (
    scoring_agent,
)
from app.core.logger import setup_logger

logger = setup_logger()


class AgentOrchestrator:
    """
    Multi-agent orchestration pipeline.
    """

    # =========================================================
    # GENERATE PAIN POINTS
    # =========================================================

    def generate_pain_points(
        self,
        hiring_signals: list[str],
        growth_signals: list[str],
        tech_stack: dict,
    ) -> list[str]:
        """
        Infer possible business pain points.
        """

        pain_points = []

        if hiring_signals:
            pain_points.append(
                "Rapid hiring may create operational scaling challenges"
            )

        if growth_signals:
            pain_points.append(
                "Growth expansion may require workflow automation"
            )

        tech_count = sum(
            len(v)
            for v in tech_stack.values()
            if isinstance(v, list)
        )

        if tech_count >= 5:
            pain_points.append(
                "Complex technology stack may increase integration overhead"
            )

        return pain_points

    # =========================================================
    # RUN PIPELINE
    # =========================================================

    async def run(
        self,
        company_url: str,
        provider: str = "groq",
    ) -> dict:
        """
        Execute full AI sales intelligence workflow.
        """

        logger.info(
            f"Starting orchestration for "
            f"{company_url}"
        )

        # =====================================================
        # STEP 1 — RESEARCH
        # =====================================================

        research_result = await research_agent.run(
            company_url=company_url,
            provider=provider,
        )

        # =====================================================
        # STEP 2 — ENRICHMENT
        # =====================================================

        enrichment_result = (
            await enrichment_agent.run(
                company_url=company_url,
            )
        )

        hiring_signals = (
            enrichment_result[
                "hiring_signals"
            ]
        )

        growth_signals = (
            enrichment_result[
                "growth_signals"
            ]
        )

        tech_stack = (
            enrichment_result["tech_stack"]
        )

        # =====================================================
        # STEP 3 — SCORING
        # =====================================================

        scoring_result = await scoring_agent.run(
            icp_fit=(
                research_result.icp_fit
                or False
            ),
            hiring_signals=hiring_signals,
            growth_signals=growth_signals,
            tech_stack=tech_stack,
        )

        lead_score = scoring_result[
            "lead_score"
        ]

        qualification = scoring_result[
            "qualification"
        ]

        # =====================================================
        # STEP 4 — PAIN POINT ANALYSIS
        # =====================================================

        pain_points = (
            self.generate_pain_points(
                hiring_signals=hiring_signals,
                growth_signals=growth_signals,
                tech_stack=tech_stack,
            )
        )

        # =====================================================
        # STEP 5 — OUTREACH
        # =====================================================

        outreach_result = (
            await outreach_agent.run(
                company_name=(
                    research_result.company_name
                ),
                industry=research_result.industry,
                company_summary=(
                    research_result.summary
                ),
                pain_points=pain_points,
                hiring_signals=hiring_signals,
                growth_signals=growth_signals,
                tech_stack=tech_stack,
                lead_score=lead_score,
                provider=provider,
            )
        )

        logger.info(
            f"Completed orchestration for "
            f"{company_url}"
        )

        # =====================================================
        # FINAL RESPONSE
        # =====================================================

        return {
            "company": {
                "name": (
                    research_result.company_name
                ),
                "website": (
                    research_result.website
                ),
                "industry": (
                    research_result.industry
                ),
                "summary": (
                    research_result.summary
                ),
                "business_model": (
                    research_result.business_model
                ),
                "icp_fit": (
                    research_result.icp_fit
                ),
            },
            "hiring_signals": (
                hiring_signals
            ),
            "growth_signals": (
                growth_signals
            ),
            "tech_stack": tech_stack,
            "pain_points": pain_points,
            "lead_score": lead_score,
            "qualification": qualification,
            "outreach": {
                "cold_email": (
                    outreach_result.cold_email
                ),
                "linkedin_message": (
                    outreach_result.linkedin_message
                ),
                "follow_up_message": (
                    outreach_result.follow_up_message
                ),
            },
        }


# Singleton instance
orchestrator = AgentOrchestrator()