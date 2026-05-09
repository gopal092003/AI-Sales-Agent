from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


# =========================================================
# REQUEST SCHEMAS
# =========================================================

class ResearchRequest(BaseModel):
    """
    Incoming company research request.
    """

    company: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Company name or company website URL",
        examples=["https://stripe.com", "OpenAI"],
    )


# =========================================================
# COMPANY PROFILE
# =========================================================

class CompanyProfile(BaseModel):
    """
    Structured company profile extracted from research.
    """

    company_name: str

    website: Optional[str] = None

    industry: Optional[str] = None

    summary: Optional[str] = None

    business_model: Optional[str] = None

    icp_fit: Optional[bool] = None


# =========================================================
# SIGNAL SCHEMAS
# =========================================================

class HiringSignal(BaseModel):
    """
    Hiring signal schema.
    """

    title: str

    description: Optional[str] = None


class GrowthSignal(BaseModel):
    """
    Growth signal schema.
    """

    title: str

    description: Optional[str] = None


# =========================================================
# TECH STACK
# =========================================================

class TechStackResponse(BaseModel):
    """
    Technology stack schema.
    """

    frontend: List[str] = []

    backend: List[str] = []

    cloud: List[str] = []

    analytics: List[str] = []


# =========================================================
# RESEARCH RESPONSE
# =========================================================

class ResearchResponse(BaseModel):
    """
    Final research pipeline response.
    """

    company: CompanyProfile

    hiring_signals: List[HiringSignal] = []

    growth_signals: List[GrowthSignal] = []

    tech_stack: TechStackResponse

    lead_score: float = 0

    qualification: str = "Low Priority"

    model_config = ConfigDict(from_attributes=True)