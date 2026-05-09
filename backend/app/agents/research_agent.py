"""
Research Agent.

Responsibilities:
- Website research
- Company analysis
- Business intelligence extraction
- ICP signal detection
"""

from app.core.logger import setup_logger
from app.schemas.research_schema import CompanyProfile
from app.scrapers.website_scraper import website_scraper
from app.services.llm_service import llm_service

logger = setup_logger()


class ResearchAgent:
    """
    Company research agent.
    """

    # =========================================================
    # LOAD PROMPT
    # =========================================================

    def load_prompt(self) -> str:
        """
        Load company research prompt.
        """

        with open(
            "app/prompts/company_research.txt",
            "r",
            encoding="utf-8",
        ) as file:
            return file.read()

    # =========================================================
    # BUILD PROMPT
    # =========================================================

    def build_prompt(
        self,
        company_url: str,
        scraped_content: str,
    ) -> str:
        """
        Build research prompt.
        """

        base_prompt = self.load_prompt()

        return f"""
{base_prompt}

Company URL:
{company_url}

Website Content:
{scraped_content[:12000]}

Return:
- company name
- industry
- summary
- business model
- ICP fit
"""

    # =========================================================
    # PARSE RESPONSE
    # =========================================================

    def parse_response(
        self,
        response: str,
        fallback_name: str,
        company_url: str,
    ) -> CompanyProfile:
        """
        Parse LLM response into structured profile.
        """

        lines = [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

        industry = None
        summary = None
        business_model = None
        icp_fit = False

        for line in lines:

            lower = line.lower()

            if "industry" in lower:
                industry = (
                    line.split(":")[-1].strip()
                )

            elif "summary" in lower:
                summary = (
                    line.split(":")[-1].strip()
                )

            elif "business model" in lower:
                business_model = (
                    line.split(":")[-1].strip()
                )

            elif "icp fit" in lower:
                value = (
                    line.split(":")[-1]
                    .strip()
                    .lower()
                )

                icp_fit = value in [
                    "true",
                    "yes",
                ]

        return CompanyProfile(
            company_name=fallback_name,
            website=company_url,
            industry=industry,
            summary=summary,
            business_model=business_model,
            icp_fit=icp_fit,
        )

    # =========================================================
    # RUN RESEARCH
    # =========================================================

    async def run(
        self,
        company_url: str,
        provider: str = "groq",
    ) -> CompanyProfile:
        """
        Execute research pipeline.
        """

        logger.info(
            f"Running research agent for "
            f"{company_url}"
        )

        scraped_data = await website_scraper.scrape(
            company_url
        )

        if not scraped_data["success"]:
            raise ValueError(
                "Failed to scrape website."
            )

        company_name = (
            website_scraper.extract_company_name(
                scraped_data
            )
            or company_url
        )

        summary = (
            website_scraper.build_summary(
                scraped_data
            )
        )

        prompt = self.build_prompt(
            company_url=company_url,
            scraped_content=summary,
        )

        response = await llm_service.generate(
            prompt=prompt,
            provider=provider,
        )

        return self.parse_response(
            response=response,
            fallback_name=company_name,
            company_url=company_url,
        )


# Singleton instance
research_agent = ResearchAgent()