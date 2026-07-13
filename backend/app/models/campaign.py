from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity


class CampaignStatus(str, Enum):
    DRAFT = "Draft"
    ACTIVE = "Active"
    COMPLETED = "Completed"


class Campaign(BaseEntity, table=True):
    __tablename__ = "campaigns"

    name: str

    description: Optional[str] = None

    goal_amount: float

    start_date: date

    end_date: date

    status: CampaignStatus = Field(default=CampaignStatus.DRAFT)

    fund: Optional["Fund"] = Relationship(back_populates="campaign")

    donor_matches: list["DonorMatch"] = Relationship(
        back_populates="campaign"
    )

    grant_matches: list["GrantMatch"] = Relationship(
        back_populates="campaign"
    )