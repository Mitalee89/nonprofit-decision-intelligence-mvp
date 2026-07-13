from datetime import date
from typing import Optional

from sqlmodel import Field

from app.models.base import BaseEntity


class Grant(BaseEntity, table=True):
    __tablename__ = "grants"

    title: str

    organization: str

    amount: float

    eligibility: Optional[str] = None

    deadline: date

    status: str = "Open"