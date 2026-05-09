"""
Jobs scraper.

Responsibilities:
- Detect hiring pages
- Extract hiring signals
- Parse careers/job content
"""

from typing import List

from bs4 import BeautifulSoup

from app.core.constants import HIRING_KEYWORDS
from app.core.logger import setup_logger
from app.services.scrape_service import scrape_service

logger = setup_logger()


class JobsScraper:
    """
    Hiring signal scraper.
    """

    # =========================================================
    # FIND CAREERS PAGE
    # =========================================================

    def find_careers_links(
        self,
        soup: BeautifulSoup,
        base_url: str,
    ) -> List[str]:
        """
        Find potential careers/job links.
        """

        links = []

        for anchor in soup.find_all("a", href=True):

            href = anchor["href"].lower()
            text = anchor.get_text(strip=True).lower()

            for keyword in HIRING_KEYWORDS:

                if (
                    keyword in href
                    or keyword in text
                ):
                    full_url = (
                        href
                        if href.startswith("http")
                        else f"{base_url.rstrip('/')}/{href.lstrip('/')}"
                    )

                    links.append(full_url)

        return list(set(links))

    # =========================================================
    # EXTRACT HIRING SIGNALS
    # =========================================================

    async def extract_hiring_signals(
        self,
        url: str,
    ) -> List[str]:
        """
        Detect hiring-related signals from website.
        """

        logger.info(
            f"Extracting hiring signals from {url}"
        )

        html = await scrape_service.fetch_html(
            url
        )

        if not html:
            return []

        soup = scrape_service.parse_html(html)

        signals = []

        page_text = soup.get_text(
            separator=" "
        ).lower()

        for keyword in HIRING_KEYWORDS:

            if keyword in page_text:
                signals.append(
                    f"Detected hiring keyword: {keyword}"
                )

        careers_links = self.find_careers_links(
            soup=soup,
            base_url=url,
        )

        if careers_links:
            signals.append(
                f"Found careers page ({len(careers_links)} links)"
            )

        return list(set(signals))


# Singleton instance
jobs_scraper = JobsScraper()