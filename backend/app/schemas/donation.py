from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.enums import DonationStatus


class DonationCreate(BaseModel):
    donor_id: int
    fund_id: int
    amount: Decimal


class DonationUpdate(BaseModel):
    status: Optional[DonationStatus] = None


class DonationResponse(BaseModel):
    id: int

    donor_id: int
    fund_id: int

    amount: Decimal

    donated_at: datetime

    status: DonationStatus

    model_config = ConfigDict(
        from_attributes=True
    )