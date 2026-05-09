from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_database
from app.core.logger import setup_logger
from app.models.report import Report

router = APIRouter()

logger = setup_logger()


@router.get(
    "/reports",
    summary="Get All Reports",
)
async def get_reports(
    db: Session = Depends(get_database),
):
    """
    Retrieve all generated reports.
    """

    try:
        reports = (
            db.query(Report)
            .order_by(Report.created_at.desc())
            .all()
        )

        return {
            "success": True,
            "count": len(reports),
            "data": reports,
        }

    except Exception as exc:
        logger.error(
            f"Failed to fetch reports: {exc}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )


@router.get(
    "/reports/{report_id}",
    summary="Get Report By ID",
)
async def get_report_by_id(
    report_id: int,
    db: Session = Depends(get_database),
):
    """
    Retrieve a single report by ID.
    """

    try:
        report = (
            db.query(Report)
            .filter(Report.id == report_id)
            .first()
        )

        if not report:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Report not found",
            )

        return {
            "success": True,
            "data": report,
        }

    except HTTPException:
        raise

    except Exception as exc:
        logger.error(
            f"Failed to fetch report: {exc}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )