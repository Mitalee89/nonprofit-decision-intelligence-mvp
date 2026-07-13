from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from sqlmodel import Field

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