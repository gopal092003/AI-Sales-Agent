"""
Lead service layer.

Responsibilities:
- Lead creation
- Lead retrieval
- Lead updates
- Lead persistence
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.core.logger import setup_logger
from app.models.lead import Lead
from app.schemas.lead_schema import LeadCreate, LeadUpdate

logger = setup_logger()


class LeadService:
    """
    Service for managing leads.
    """

    # =========================================================
    # CREATE LEAD
    # =========================================================

    def create_lead(
        self,
        db: Session,
        payload: LeadCreate,
    ) -> Lead:
        """
        Create a new lead.
        """

        lead = Lead(
            company_name=payload.company_name,
            company_url=payload.company_url,
            industry=payload.industry,
            company_summary=payload.company_summary,
        )

        db.add(lead)
        db.commit()
        db.refresh(lead)

        logger.info(
            f"Lead created: {lead.company_name}"
        )

        return lead

    # =========================================================
    # GET LEAD BY ID
    # =========================================================

    def get_lead_by_id(
        self,
        db: Session,
        lead_id: int,
    ) -> Optional[Lead]:
        """
        Retrieve lead by ID.
        """

        return (
            db.query(Lead)
            .filter(Lead.id == lead_id)
            .first()
        )

    # =========================================================
    # GET LEAD BY COMPANY NAME
    # =========================================================

    def get_lead_by_company(
        self,
        db: Session,
        company_name: str,
    ) -> Optional[Lead]:
        """
        Retrieve lead by company name.
        """

        return (
            db.query(Lead)
            .filter(
                Lead.company_name == company_name
            )
            .first()
        )

    # =========================================================
    # GET ALL LEADS
    # =========================================================

    def get_all_leads(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Lead]:
        """
        Retrieve all leads.
        """

        return (
            db.query(Lead)
            .offset(skip)
            .limit(limit)
            .all()
        )

    # =========================================================
    # UPDATE LEAD
    # =========================================================

    def update_lead(
        self,
        db: Session,
        lead: Lead,
        payload: LeadUpdate,
    ) -> Lead:
        """
        Update lead fields.
        """

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():

            # Convert lists to comma-separated text
            if isinstance(value, list):
                value = ", ".join(value)

            setattr(lead, field, value)

        db.commit()
        db.refresh(lead)

        logger.info(
            f"Lead updated: {lead.company_name}"
        )

        return lead

    # =========================================================
    # DELETE LEAD
    # =========================================================

    def delete_lead(
        self,
        db: Session,
        lead: Lead,
    ) -> None:
        """
        Delete lead.
        """

        db.delete(lead)
        db.commit()

        logger.info(
            f"Lead deleted: {lead.company_name}"
        )


# Singleton instance
lead_service = LeadService()