from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


# =========================================================
# BASE LEAD SCHEMA
# =========================================================

class LeadBase(BaseModel):
    """
    Base lead schema.
    """

    company_name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Company name",
    )

    company_url: Optional[str] = Field(
        default=None,
        description="Company website URL",
    )

    industry: Optional[str] = None

    company_summary: Optional[str] = None


# =========================================================
# CREATE LEAD
# =========================================================

class LeadCreate(LeadBase):
    """
    Schema for creating a lead.
    """

    pass


# =========================================================
# UPDATE LEAD
# =========================================================

class LeadUpdate(BaseModel):
    """
    Schema for updating lead fields.
    """

    industry: Optional[str] = None

    company_summary: Optional[str] = None

    lead_score: Optional[float] = None

    qualification: Optional[str] = None

    hiring_signals: Optional[List[str]] = None

    growth_signals: Optional[List[str]] = None

    tech_stack: Optional[List[str]] = None

    is_contacted: Optional[bool] = None


# =========================================================
# LEAD RESPONSE
# =========================================================

class LeadResponse(LeadBase):
    """
    Lead response schema.
    """

    id: int

    lead_score: float

    qualification: Optional[str] = None

    hiring_signals: Optional[str] = None

    growth_signals: Optional[str] = None

    tech_stack: Optional[str] = None

    is_contacted: bool

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# LEAD SCORE RESPONSE
# =========================================================

class LeadScoreResponse(BaseModel):
    """
    Lead scoring response schema.
    """

    company_name: str

    lead_score: float

    qualification: str


# =========================================================
# LEAD LIST RESPONSE
# =========================================================

class LeadListResponse(BaseModel):
    """
    Paginated lead list response.
    """

    total: int

    items: List[LeadResponse]