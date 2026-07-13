from __future__ import annotations

from typing import Optional

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity


class Donor(BaseEntity, table=True):
    __tablename__ = "donors"

    name: str

    email: str

    city: Optional[str] = None

    interests: Optional[str] = None

    preferred_cause: Optional[str] = None

    capacity: float = 0

    donations: list["Donation"] = Relationship(
        back_populates="donor"
    )

    donor_matches: list["DonorMatch"] = Relationship(
        back_populates="donor"
    )