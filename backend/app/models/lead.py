from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text

from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Lead(Base):
    """
    Lead database model.

    Stores researched company intelligence and scoring data.
    """

    __tablename__ = "leads"

    # =========================================================
    # PRIMARY KEY
    # =========================================================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # =========================================================
    # COMPANY INFO
    # =========================================================

    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    company_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    industry: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    company_summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================================================
    # SCORING
    # =========================================================

    lead_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    qualification: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # =========================================================
    # SIGNALS
    # =========================================================

    hiring_signals: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    growth_signals: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    tech_stack: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================================================
    # STATUS
    # =========================================================

    is_contacted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
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
            f"<Lead(id={self.id}, "
            f"company_name='{self.company_name}', "
            f"lead_score={self.lead_score})>"
        )