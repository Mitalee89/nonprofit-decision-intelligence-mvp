from sqlmodel import SQLModel, Session, create_engine

from app.core.config import settings

# Import all models so SQLModel registers them
from app.models import (
    Campaign,
    Donation,
    Donor,
    DonorMatch,
    Fund,
    Grant,
    GrantMatch,
)

engine = create_engine(
    settings.database_url,
    echo=True,
    connect_args={"check_same_thread": False},  # Required for SQLite
)


def create_db_and_tables() -> None:
    """Create all database tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency for FastAPI routes."""
    with Session(engine) as session:
        yield session