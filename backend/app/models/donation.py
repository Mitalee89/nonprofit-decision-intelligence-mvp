from __future__ import annotations

from datetime import date

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity


class Donation(BaseEntity, table=True):
    __tablename__ = "donations"

    donor_id: int = Field(foreign_key="donors.id")

    fund_id: int = Field(foreign_key="funds.id")

    amount: float

    donation_date: date

    status: str = "Received"

    donor: "Donor" = Relationship(
        back_populates="donations"
    )

    fund: "Fund" = Relationship(
        back_populates="donations"
    )