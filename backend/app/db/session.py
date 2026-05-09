from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# =========================================================
# DATABASE ENGINE
# =========================================================

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
    if settings.DATABASE_URL.startswith("sqlite")
    else {},
    echo=settings.DEBUG,
)

# =========================================================
# SESSION FACTORY
# =========================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# =========================================================
# DATABASE DEPENDENCY
# =========================================================

def get_db():
    """
    FastAPI database dependency.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()