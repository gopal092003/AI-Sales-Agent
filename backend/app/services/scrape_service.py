"""
Scraping service layer.

Responsibilities:
- Website fetching
- HTML parsing
- Metadata extraction
- Async HTTP requests
"""

from typing import Optional

import httpx
from bs4 import BeautifulSoup

from app.core.config import settings
from app.core.logger import setup_logger

logger = setup_logger()


class ScrapeService:
    """
    Website scraping and parsing service.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": settings.USER_AGENT,
        }

    # =========================================================
    # FETCH HTML
    # =========================================================

    async def fetch_html(
        self,
        url: str,
    ) -> Optional[str]:
        """
        Fetch website HTML content.
        """

        try:
            async with httpx.AsyncClient(
                timeout=settings.REQUEST_TIMEOUT,
                headers=self.headers,
                follow_redirects=True,
            ) as client:

                response = await client.get(url)

                response.raise_for_status()

                return response.text

        except Exception as exc:
            logger.error(
                f"Failed to fetch HTML from {url}: {exc}"
            )

            return None

    # =========================================================
    # PARSE HTML
    # =========================================================

    def parse_html(
        self,
        html: str,
    ) -> BeautifulSoup:
        """
        Parse HTML using BeautifulSoup.
        """

        return BeautifulSoup(html, "lxml")

    # =========================================================
    # EXTRACT PAGE TITLE
    # =========================================================

    def extract_title(
        self,
        soup: BeautifulSoup,
    ) -> Optional[str]:
        """
        Extract page title.
        """

        if soup.title:
            return soup.title.text.strip()

        return None

    # =========================================================
    # EXTRACT META DESCRIPTION
    # =========================================================

    def extract_meta_description(
        self,
        soup: BeautifulSoup,
    ) -> Optional[str]:
        """
        Extract meta description.
        """

        meta = soup.find(
            "meta",
            attrs={"name": "description"},
        )

        if meta and meta.get("content"):
            return meta["content"].strip()

        return None

    # =========================================================
    # EXTRACT CLEAN TEXT
    # =========================================================

    def extract_text(
        self,
        soup: BeautifulSoup,
    ) -> str:
        """
        Extract visible text from HTML.
        """

        # Remove scripts/styles
        for tag in soup(
            ["script", "style", "noscript"]
        ):
            tag.decompose()

        text = soup.get_text(separator=" ")

        # Clean excessive whitespace
        cleaned = " ".join(text.split())

        return cleaned

    # =========================================================
    # FULL WEBSITE SCRAPE
    # =========================================================

    async def scrape_website(
        self,
        url: str,
    ) -> dict:
        """
        Full website scraping pipeline.
        """

        html = await self.fetch_html(url)

        if not html:
            return {
                "success": False,
                "url": url,
                "title": None,
                "description": None,
                "text": None,
            }

        soup = self.parse_html(html)

        return {
            "success": True,
            "url": url,
            "title": self.extract_title(soup),
            "description": self.extract_meta_description(soup),
            "text": self.extract_text(soup),
        }


# Singleton instance
scrape_service = ScrapeService()