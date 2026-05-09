"""
Enrichment Agent.

Responsibilities:
- Hiring signal extraction
- Growth signal detection
- Tech stack analysis
- External intelligence enrichment
"""

from app.core.config import settings
from app.core.logger import setup_logger
from app.scrapers.jobs_scraper import jobs_scraper
from app.scrapers.news_scraper import news_scraper
from app.scrapers.techstack_scraper import (
    techstack_scraper,
)
from app.utils.async_utils import run_async_tasks

logger = setup_logger()


class EnrichmentAgent:
    """
    Intelligence enrichment agent.
    """

    # =========================================================
    # RUN ENRICHMENT
    # =========================================================

    async def run(
        self,
        company_url: str,
    ) -> dict:
        """
        Execute enrichment pipeline.
        """

        logger.info(
            f"Running enrichment agent for "
            f"{company_url}"
        )

        tasks = []

        # Hiring signals
        if settings.ENABLE_HIRING_SIGNALS:
            tasks.append(
                jobs_scraper.extract_hiring_signals(
                    company_url
                )
            )
        else:
            tasks.append([])

        # Growth signals
        if settings.ENABLE_NEWS_SCRAPING:
            tasks.append(
                news_scraper.extract_growth_signals(
                    company_url
                )
            )
        else:
            tasks.append([])

        # Tech stack
        if settings.ENABLE_TECHSTACK_DETECTION:
            tasks.append(
                techstack_scraper.analyze_tech_stack(
                    company_url
                )
            )
        else:
            tasks.append({})

        results = await run_async_tasks(tasks)

        hiring_signals = (
            results[0]
            if isinstance(results[0], list)
            else []
        )

        growth_signals = (
            results[1]
            if isinstance(results[1], list)
            else []
        )

        tech_stack = (
            results[2]
            if isinstance(results[2], dict)
            else {}
        )

        return {
            "hiring_signals": hiring_signals,
            "growth_signals": growth_signals,
            "tech_stack": tech_stack,
        }


# Singleton instance
enrichment_agent = EnrichmentAgent()