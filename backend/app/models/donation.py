from datetime import date

from sqlmodel import Field

from app.models.base import BaseEntity


class Donation(BaseEntity, table=True):
    __tablename__ = "donations"

    donor_id: int = Field(foreign_key="donors.id")

    fund_id: int = Field(foreign_key="funds.id")

    amount: float

    donation_date: date

    status: str = "Received"