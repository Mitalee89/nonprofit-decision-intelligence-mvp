from datetime import date
from typing import TYPE_CHECKING, Optional
from decimal import Decimal

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity
from app.models.enums import CampaignStatus

if TYPE_CHECKING:
    from app.models.fund import Fund
    from app.models.donor_match import DonorMatch
    from app.models.grant_match import GrantMatch


class Campaign(BaseEntity, table=True):
    __tablename__ = "campaigns"

    name: str = Field(index=True, max_length=200)

    description: Optional[str] = Field(
        default=None,
        max_length=1000,
    )
    goal_amount: Decimal = Field(default=Decimal("0.00"), ge=0)
    amount_raised: Decimal = Field(default=Decimal("0.00"), ge=0)
    start_date: date
    end_date: date
    status: CampaignStatus = Field(
        default=CampaignStatus.DRAFT
    )
