"""
General helper utilities used across the application.
"""

from datetime import datetime
from typing import Any, Optional
from urllib.parse import urlparse


def get_current_timestamp() -> datetime:
    """
    Return current UTC timestamp.
    """

    return datetime.utcnow()


def normalize_company_name(company: str) -> str:
    """
    Normalize company names for consistency.
    """

    if not company:
        return ""

    company = company.strip()

    # Remove protocol if present
    company = company.replace("https://", "")
    company = company.replace("http://", "")

    # Remove www
    company = company.replace("www.", "")

    # Remove trailing slash
    company = company.rstrip("/")

    return company


def extract_domain(url: str) -> Optional[str]:
    """
    Extract domain from URL.
    """

    if not url:
        return None

    parsed = urlparse(url)

    return parsed.netloc or parsed.path


def safe_get(data: dict, key: str, default: Any = None):
    """
    Safely retrieve dictionary value.
    """

    return data.get(key, default)


def truncate_text(text: str, max_length: int = 300) -> str:
    """
    Truncate text safely.
    """

    if not text:
        return ""

    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."


def list_to_text(values: list[str]) -> str:
    """
    Convert list into comma-separated text.
    """

    if not values:
        return ""

    return ", ".join(values)


def text_to_list(value: str) -> list[str]:
    """
    Convert comma-separated text into list.
    """

    if not value:
        return []

    return [item.strip() for item in value.split(",") if item.strip()]