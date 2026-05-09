"""
Validation utilities for the application.
"""

import re
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """
    Validate URL format.
    """

    if not url:
        return False

    parsed = urlparse(url)

    return bool(parsed.scheme and parsed.netloc)


def is_valid_email(email: str) -> bool:
    """
    Validate email format.
    """

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.match(pattern, email))


def is_valid_company_name(company_name: str) -> bool:
    """
    Validate company name.
    """

    if not company_name:
        return False

    return len(company_name.strip()) >= 2


def validate_lead_score(score: float) -> bool:
    """
    Ensure lead score is between 0 and 100.
    """

    return 0 <= score <= 100


def validate_text_length(
    text: str,
    min_length: int = 1,
    max_length: int = 5000,
) -> bool:
    """
    Validate text length boundaries.
    """

    if text is None:
        return False

    text_length = len(text.strip())

    return min_length <= text_length <= max_length


def validate_outreach_message(message: str) -> bool:
    """
    Validate outreach message quality.
    """

    if not message:
        return False

    if len(message.strip()) < 20:
        return False

    return True