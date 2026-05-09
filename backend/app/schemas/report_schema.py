from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


# =========================================================
# BASE REPORT SCHEMA
# =========================================================

class ReportBase(BaseModel):
    """
    Base report schema.
    """

    company_overview: Optional[str] = None

    pain_points: Optional[str] = None

    opportunity_areas: Optional[str] = None

    outreach_strategy: Optional[str] = None


# =========================================================
# CREATE REPORT
# =========================================================

class ReportCreate(ReportBase):
    """
    Schema for creating a report.
    """

    lead_id: int = Field(
        ...,
        gt=0,
        description="Associated lead ID",
    )

    cold_email: Optional[str] = None

    linkedin_message: Optional[str] = None

    follow_up_message: Optional[str] = None


# =========================================================
# UPDATE REPORT
# =========================================================

class ReportUpdate(BaseModel):
    """
    Schema for updating reports.
    """

    company_overview: Optional[str] = None

    pain_points: Optional[str] = None

    opportunity_areas: Optional[str] = None

    outreach_strategy: Optional[str] = None

    cold_email: Optional[str] = None

    linkedin_message: Optional[str] = None

    follow_up_message: Optional[str] = None


# =========================================================
# REPORT RESPONSE
# =========================================================

class ReportResponse(ReportBase):
    """
    Report response schema.
    """

    id: int

    lead_id: int

    cold_email: Optional[str] = None

    linkedin_message: Optional[str] = None

    follow_up_message: Optional[str] = None

    generated_by: str

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# FULL SALES INTELLIGENCE REPORT
# =========================================================

class SalesIntelligenceReport(BaseModel):
    """
    Combined intelligence report returned to frontend.
    """

    company_name: str

    industry: Optional[str] = None

    company_summary: Optional[str] = None

    lead_score: float

    qualification: str

    hiring_signals: list[str] = []

    growth_signals: list[str] = []

    tech_stack: list[str] = []

    pain_points: list[str] = []

    opportunity_areas: list[str] = []

    cold_email: Optional[str] = None

    linkedin_message: Optional[str] = None

    follow_up_message: Optional[str] = None