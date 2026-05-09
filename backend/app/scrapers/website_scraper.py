"""
Website scraper.

Responsibilities:
- Website content extraction
- Metadata extraction
- Company information scraping
"""

from typing import Optional

from app.core.logger import setup_logger
from app.services.scrape_service import scrape_service

logger = setup_logger()


class WebsiteScraper:
    """
    Website scraping utility.
    """

    # =========================================================
    # SCRAPE WEBSITE
    # =========================================================

    async def scrape(
        self,
        url: str,
    ) -> dict:
        """
        Scrape website and extract company data.
        """

        logger.info(
            f"Scraping website: {url}"
        )

        result = await scrape_service.scrape_website(
            url
        )

        return {
            "company_url": result.get("url"),
            "title": result.get("title"),
            "description": result.get(
                "description"
            ),
            "content": result.get("text"),
            "success": result.get("success"),
        }

    # =========================================================
    # EXTRACT COMPANY NAME
    # =========================================================

    def extract_company_name(
        self,
        scraped_data: dict,
    ) -> Optional[str]:
        """
        Attempt to infer company name.
        """

        title = scraped_data.get("title")

        if not title:
            return None

        separators = ["|", "-", "•"]

        company_name = title

        for separator in separators:
            if separator in title:
                company_name = (
                    title.split(separator)[0]
                    .strip()
                )
                break

        return company_name

    # =========================================================
    # BUILD COMPANY SUMMARY
    # =========================================================

    def build_summary(
        self,
        scraped_data: dict,
    ) -> str:
        """
        Build concise company summary.
        """

        description = scraped_data.get(
            "description"
        )

        if description:
            return description

        content = scraped_data.get("content")

        if not content:
            return ""

        return content[:500].strip()


# Singleton instance
website_scraper = WebsiteScraper()