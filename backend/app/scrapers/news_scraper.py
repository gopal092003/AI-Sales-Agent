"""
News scraper.

Responsibilities:
- Extract growth-related signals
- Detect expansion indicators
- Parse news and announcement pages
"""

from typing import List

from app.core.constants import GROWTH_KEYWORDS
from app.core.logger import setup_logger
from app.services.scrape_service import scrape_service

logger = setup_logger()


class NewsScraper:
    """
    Growth signal scraper.
    """

    # =========================================================
    # EXTRACT GROWTH SIGNALS
    # =========================================================

    async def extract_growth_signals(
        self,
        url: str,
    ) -> List[str]:
        """
        Detect growth-related signals from website content.
        """

        logger.info(
            f"Extracting growth signals from {url}"
        )

        html = await scrape_service.fetch_html(
            url
        )

        if not html:
            return []

        soup = scrape_service.parse_html(html)

        page_text = soup.get_text(
            separator=" "
        ).lower()

        signals = []

        for keyword in GROWTH_KEYWORDS:

            if keyword in page_text:
                signals.append(
                    f"Detected growth keyword: {keyword}"
                )

        return list(set(signals))

    # =========================================================
    # EXTRACT NEWS LINKS
    # =========================================================

    def extract_news_links(
        self,
        soup,
        base_url: str,
    ) -> List[str]:
        """
        Extract possible news/blog URLs.
        """

        links = []

        keywords = [
            "news",
            "blog",
            "press",
            "updates",
            "announcements",
        ]

        for anchor in soup.find_all(
            "a",
            href=True,
        ):
            href = anchor["href"].lower()

            for keyword in keywords:

                if keyword in href:

                    full_url = (
                        href
                        if href.startswith("http")
                        else f"{base_url.rstrip('/')}/{href.lstrip('/')}"
                    )

                    links.append(full_url)

        return list(set(links))


# Singleton instance
news_scraper = NewsScraper()