from __future__ import annotations

from datetime import date
from typing import Optional

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity
from app.models.enums import GrantStatus


class Grant(BaseEntity, table=True):
    __tablename__ = "grants"

    title: str

    organization: str

    amount: float

    eligibility: Optional[str] = None

    deadline: date



    status: GrantStatus = Field(
        default=GrantStatus.OPEN
    )
