"""
Formatting utilities for reports, outreach, and API responses.
"""

from typing import List


def format_company_summary(
    company_name: str,
    industry: str | None,
    summary: str | None,
) -> str:
    """
    Format company overview text.
    """

    parts = [f"Company: {company_name}"]

    if industry:
        parts.append(f"Industry: {industry}")

    if summary:
        parts.append(f"Summary: {summary}")

    return "\n".join(parts)


def format_lead_score(score: float) -> str:
    """
    Format lead score display.
    """

    return f"{round(score, 2)}/100"


def format_signal_list(signals: List[str]) -> str:
    """
    Format signals into readable bullet points.
    """

    if not signals:
        return "No signals detected."

    return "\n".join(f"- {signal}" for signal in signals)


def format_tech_stack(tech_stack: List[str]) -> str:
    """
    Format tech stack display.
    """

    if not tech_stack:
        return "No technologies detected."

    return ", ".join(tech_stack)


def format_outreach_preview(message: str, limit: int = 150) -> str:
    """
    Create shortened outreach preview.
    """

    if not message:
        return ""

    if len(message) <= limit:
        return message

    return message[:limit].rstrip() + "..."


def format_api_response(
    success: bool,
    message: str,
    data=None,
):
    """
    Standardized API response structure.
    """

    return {
        "success": success,
        "message": message,
        "data": data,
    }