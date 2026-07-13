from sqlmodel import SQLModel, create_engine

from app.core.config import settings

# Import models so SQLModel registers the tables
from app.models import (  # noqa: F401
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
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)