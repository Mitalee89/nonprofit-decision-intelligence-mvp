from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from app.models.enums import CampaignStatus


class CampaignCreate(BaseModel):
    name: str
    description: Optional[str] = None

    goal_amount: Decimal

    start_date: date
    end_date: date


class CampaignUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    goal_amount: Optional[Decimal] = None

    start_date: Optional[date] = None
    end_date: Optional[date] = None

    status: Optional[CampaignStatus] = None


class CampaignResponse(BaseModel):
    id: int

    name: str
    description: Optional[str]

    goal_amount: Decimal
    amount_raised: Decimal

    start_date: date
    end_date: date

    status: CampaignStatus

    class Config:
        from_attributes = True