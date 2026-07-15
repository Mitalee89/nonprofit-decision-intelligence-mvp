from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from app.models.enums import FundStatus


class FundUpdate(BaseModel):
    name: Optional[str] = None

    balance: Optional[Decimal] = None
    total_received: Optional[Decimal] = None

    status: Optional[FundStatus] = None


class FundResponse(BaseModel):
    id: int

    name: str
    campaign_id: int

    balance: Decimal
    total_received: Decimal

    status: FundStatus

    class Config:
        from_attributes = True