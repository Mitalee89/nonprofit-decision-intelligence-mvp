from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity
from app.models.enums import DonationStatus

if TYPE_CHECKING:
    from app.models.donor import Donor
    from app.models.fund import Fund


class Donation(BaseEntity, table=True):
    __tablename__ = "donations"

    amount: Decimal = Field(
        default=Decimal("0.00"),
        ge=0,
    )

    donated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    status: DonationStatus = Field(
        default=DonationStatus.RECEIVED
    )

    donor_id: int = Field(
        foreign_key="donors.id",
        nullable=False,
    )

    fund_id: int = Field(
        foreign_key="funds.id",
        nullable=False,
    )
