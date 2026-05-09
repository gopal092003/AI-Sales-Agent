"""
Database initialization utility.
"""

from app.db.base import Base
from app.db.session import engine

# Import models here so SQLAlchemy can detect them
from app.models.activity import Activity  # noqa: F401
from app.models.lead import Lead  # noqa: F401
from app.models.report import Report  # noqa: F401


def init_db():
    """
    Initialize database tables.
    """

    Base.metadata.create_all(bind=engine)

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_db()