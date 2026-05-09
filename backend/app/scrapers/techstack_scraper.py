"""
Tech stack scraper.

Responsibilities:
- Detect frontend technologies
- Detect backend technologies
- Detect cloud/infrastructure tools
- Detect analytics platforms
"""

from typing import List

from app.core.constants import (
    COMMON_BACKEND_TECH,
    COMMON_CLOUD_TECH,
    COMMON_FRONTEND_TECH,
)
from app.core.logger import setup_logger
from app.services.scrape_service import scrape_service

logger = setup_logger()


class TechStackScraper:
    """
    Technology stack detection scraper.
    """

    # =========================================================
    # DETECT FRONTEND TECHNOLOGIES
    # =========================================================

    def detect_frontend_tech(
        self,
        html: str,
    ) -> List[str]:
        """
        Detect frontend frameworks/libraries.
        """

        detected = []

        html_lower = html.lower()

        mappings = {
            "react": "React",
            "_next": "Next.js",
            "vue": "Vue",
            "angular": "Angular",
            "tailwind": "TailwindCSS",
        }

        for keyword, tech in mappings.items():

            if keyword in html_lower:
                detected.append(tech)

        return list(set(detected))

    # =========================================================
    # DETECT BACKEND TECHNOLOGIES
    # =========================================================

    def detect_backend_tech(
        self,
        html: str,
    ) -> List[str]:
        """
        Detect backend technologies.
        """

        detected = []

        html_lower = html.lower()

        mappings = {
            "django": "Django",
            "flask": "Flask",
            "fastapi": "FastAPI",
            "express": "Express",
            "node": "Node.js",
        }

        for keyword, tech in mappings.items():

            if keyword in html_lower:
                detected.append(tech)

        return list(set(detected))

    # =========================================================
    # DETECT CLOUD PROVIDERS
    # =========================================================

    def detect_cloud_tech(
        self,
        html: str,
    ) -> List[str]:
        """
        Detect cloud/infrastructure providers.
        """

        detected = []

        html_lower = html.lower()

        mappings = {
            "aws": "AWS",
            "amazonaws": "AWS",
            "cloudflare": "Cloudflare",
            "vercel": "Vercel",
            "google-cloud": "GCP",
            "azure": "Azure",
        }

        for keyword, tech in mappings.items():

            if keyword in html_lower:
                detected.append(tech)

        return list(set(detected))

    # =========================================================
    # DETECT ANALYTICS TOOLS
    # =========================================================

    def detect_analytics_tools(
        self,
        html: str,
    ) -> List[str]:
        """
        Detect analytics and tracking tools.
        """

        detected = []

        html_lower = html.lower()

        mappings = {
            "google-analytics": "Google Analytics",
            "gtag": "Google Analytics",
            "segment": "Segment",
            "mixpanel": "Mixpanel",
            "hotjar": "Hotjar",
        }

        for keyword, tool in mappings.items():

            if keyword in html_lower:
                detected.append(tool)

        return list(set(detected))

    # =========================================================
    # FULL TECH STACK ANALYSIS
    # =========================================================

    async def analyze_tech_stack(
        self,
        url: str,
    ) -> dict:
        """
        Analyze website tech stack.
        """

        logger.info(
            f"Analyzing tech stack for {url}"
        )

        html = await scrape_service.fetch_html(
            url
        )

        if not html:
            return {
                "frontend": [],
                "backend": [],
                "cloud": [],
                "analytics": [],
            }

        return {
            "frontend": self.detect_frontend_tech(
                html
            ),
            "backend": self.detect_backend_tech(
                html
            ),
            "cloud": self.detect_cloud_tech(
                html
            ),
            "analytics": self.detect_analytics_tools(
                html
            ),
        }


# Singleton instance
techstack_scraper = TechStackScraper()