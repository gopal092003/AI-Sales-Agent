"""
Security utilities for the AI Sales Intelligence Agent.

This module contains:
- API key validation helpers
- token utilities
- request sanitization helpers
- basic security functions

Future upgrades:
- JWT authentication
- OAuth
- RBAC
- rate limiting
"""

import re
from typing import Optional


def sanitize_input(value: str) -> str:
    """
    Basic input sanitization.

    Removes excessive whitespace and dangerous characters.
    """

    if not value:
        return ""

    value = value.strip()

    # Remove null bytes
    value = value.replace("\x00", "")

    return value


def is_valid_url(url: str) -> bool:
    """
    Validate URL format.
    """

    pattern = re.compile(
        r"^(https?:\/\/)?"
        r"(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})"
        r"(\/.*)?$"
    )

    return bool(pattern.match(url))


def mask_secret(secret: Optional[str]) -> str:
    """
    Mask sensitive values for logs.
    """

    if not secret:
        return "N/A"

    if len(secret) <= 6:
        return "***"

    return f"{secret[:3]}***{secret[-3:]}"


def validate_api_key(api_key: Optional[str]) -> bool:
    """
    Basic API key validation.
    """

    return bool(api_key and len(api_key.strip()) > 10)