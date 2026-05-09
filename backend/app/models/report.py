from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Report(Base):
    """
    Sales intelligence report model.

    Stores generated research reports and outreach content.
    """

    __tablename__ = "reports"

    # =========================================================
    # PRIMARY KEY
    # =========================================================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # =========================================================
    # RELATIONSHIPS
    # =========================================================

    lead_id: Mapped[int] = mapped_column(
        ForeignKey("leads.id", ondelete="CASCADE"),
        nullable=False,
    )

    lead = relationship("Lead")

    # =========================================================
    # REPORT CONTENT
    # =========================================================

    company_overview: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    pain_points: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    opportunity_areas: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    outreach_strategy: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================================================
    # OUTREACH CONTENT
    # =========================================================

    cold_email: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    linkedin_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    follow_up_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================================================
    # METADATA
    # =========================================================

    generated_by: Mapped[str] = mapped_column(
        String(100),
        default="outreach_agent",
    )

    # =========================================================
    # TIMESTAMPS
    # =========================================================

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    # =========================================================
    # REPRESENTATION
    # =========================================================

    def __repr__(self) -> str:
        return (
            f"<Report(id={self.id}, lead_id={self.lead_id})>"
        )