from __future__ import annotations

from datetime import date
from typing import Optional

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity


class Grant(BaseEntity, table=True):
    __tablename__ = "grants"

    title: str

    organization: str

    amount: float

    eligibility: Optional[str] = None

    deadline: date

    from app.domain.enums import GrantStatus

    status: GrantStatus = Field(
        default=GrantStatus.OPEN
    )

    grant_matches: list["GrantMatch"] = Relationship(
        back_populates="grant"
    )