from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


# =========================================================
# OUTREACH REQUEST
# =========================================================

class OutreachRequest(BaseModel):
    """
    Outreach generation request schema.
    """

    company_name: str = Field(
        ...,
        min_length=1,
        max_length=255,
    )

    industry: Optional[str] = None

    company_summary: Optional[str] = None

    pain_points: List[str] = []

    hiring_signals: List[str] = []

    growth_signals: List[str] = []

    tech_stack: List[str] = []

    lead_score: Optional[float] = 0


# =========================================================
# GENERATED OUTREACH CONTENT
# =========================================================

class OutreachContent(BaseModel):
    """
    Generated outreach messages.
    """

    cold_email: str

    linkedin_message: str

    follow_up_message: str


# =========================================================
# OUTREACH RESPONSE
# =========================================================

class OutreachResponse(BaseModel):
    """
    Outreach API response schema.
    """

    company_name: str

    lead_score: float

    outreach: OutreachContent

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# EMAIL VARIANT
# =========================================================

class ColdEmailVariant(BaseModel):
    """
    Cold email variation schema.
    """

    subject: str

    body: str


# =========================================================
# MULTI-VARIANT RESPONSE
# =========================================================

class OutreachVariantsResponse(BaseModel):
    """
    Multiple outreach variations.
    """

    company_name: str

    variants: List[ColdEmailVariant]