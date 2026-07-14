from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity
from app.models.enums import FundStatus
from decimal import Decimal

if TYPE_CHECKING:
    from app.models.campaign import Campaign
    from app.models.donation import Donation


class Fund(BaseEntity, table=True):
    __tablename__ = "funds"

    name: str = Field(index=True, max_length=200)
    balance: Decimal = Field(default=Decimal("0.00"), ge=0)
    total_received: Decimal = Field(default=Decimal("0.00"), ge=0)
    status: FundStatus = Field(
        default=FundStatus.OPEN
    )

    # One Fund belongs to one Campaign
    campaign_id: int = Field(
        foreign_key="campaigns.id",
        unique=True,
        nullable=False,
    )

