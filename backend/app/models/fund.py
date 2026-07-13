from __future__ import annotations

from typing import Optional

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity


class Fund(BaseEntity, table=True):
    __tablename__ = "funds"

    campaign_id: int = Field(
    foreign_key="campaigns.id",
    unique=True
    )

    fund_name: str

    available_amount: float = 0

    allocated_amount: float = 0

    status: str = "Active"

    campaign: Optional["Campaign"] = Relationship(
        back_populates="fund"
    )

    donations: list["Donation"] = Relationship(
        back_populates="fund"
    )