from typing import Optional

from sqlmodel import Field

from app.models.base import BaseEntity


class Fund(BaseEntity, table=True):
    __tablename__ = "funds"

    campaign_id: int = Field(foreign_key="campaigns.id")

    fund_name: str

    available_amount: float = 0

    allocated_amount: float = 0

    status: str = "Active"