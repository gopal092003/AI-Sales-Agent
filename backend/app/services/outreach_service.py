"""
Outreach service layer.

Responsibilities:
- Prompt generation
- Outreach personalization
- Cold email generation
- LinkedIn outreach generation
- Follow-up creation
"""

from app.core.logger import setup_logger
from app.schemas.outreach_schema import (
    OutreachContent,
    OutreachRequest,
)
from app.services.llm_service import llm_service

logger = setup_logger()


class OutreachService:
    """
    Outreach generation service.
    """

    # =========================================================
    # BUILD PROMPT
    # =========================================================

    def build_outreach_prompt(
        self,
        payload: OutreachRequest,
    ) -> str:
        """
        Build structured outreach prompt.
        """

        pain_points = (
            ", ".join(payload.pain_points)
            if payload.pain_points
            else "No major pain points identified"
        )

        hiring_signals = (
            ", ".join(payload.hiring_signals)
            if payload.hiring_signals
            else "No hiring signals detected"
        )

        growth_signals = (
            ", ".join(payload.growth_signals)
            if payload.growth_signals
            else "No growth signals detected"
        )

        tech_stack = (
            ", ".join(payload.tech_stack)
            if payload.tech_stack
            else "No technologies detected"
        )

        return f"""
You are an expert AI SDR.

Generate:
1. A personalized cold email
2. A LinkedIn outreach message
3. A follow-up message

Company Information:
- Company Name: {payload.company_name}
- Industry: {payload.industry}
- Company Summary: {payload.company_summary}

Pain Points:
{pain_points}

Hiring Signals:
{hiring_signals}

Growth Signals:
{growth_signals}

Tech Stack:
{tech_stack}

Lead Score:
{payload.lead_score}

Requirements:
- Keep messaging concise
- Make messaging personalized
- Avoid generic sales language
- Focus on business value
- Sound natural and professional

Return the response in this exact format:

COLD_EMAIL:
<content>

LINKEDIN_MESSAGE:
<content>

FOLLOW_UP:
<content>
"""

    # =========================================================
    # PARSE RESPONSE
    # =========================================================

    def parse_outreach_response(
        self,
        response: str,
    ) -> OutreachContent:
        """
        Parse LLM outreach response into structured schema.
        """

        cold_email = ""
        linkedin_message = ""
        follow_up = ""

        try:
            if "COLD_EMAIL:" in response:
                cold_email = (
                    response.split("COLD_EMAIL:")[1]
                    .split("LINKEDIN_MESSAGE:")[0]
                    .strip()
                )

            if "LINKEDIN_MESSAGE:" in response:
                linkedin_message = (
                    response.split("LINKEDIN_MESSAGE:")[1]
                    .split("FOLLOW_UP:")[0]
                    .strip()
                )

            if "FOLLOW_UP:" in response:
                follow_up = (
                    response.split("FOLLOW_UP:")[1]
                    .strip()
                )

        except Exception as exc:
            logger.error(
                f"Failed to parse outreach response: {exc}"
            )

        return OutreachContent(
            cold_email=cold_email,
            linkedin_message=linkedin_message,
            follow_up_message=follow_up,
        )

    # =========================================================
    # GENERATE OUTREACH
    # =========================================================

    async def generate_outreach(
        self,
        payload: OutreachRequest,
        provider: str = "groq",
    ) -> OutreachContent:
        """
        Generate personalized outreach content.
        """

        prompt = self.build_outreach_prompt(payload)

        logger.info(
            f"Generating outreach for "
            f"{payload.company_name}"
        )

        response = await llm_service.generate(
            prompt=prompt,
            provider=provider,
        )

        return self.parse_outreach_response(response)


# Singleton instance
outreach_service = OutreachService()