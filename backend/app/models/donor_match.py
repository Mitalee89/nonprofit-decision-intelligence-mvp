from __future__ import annotations

from sqlmodel import Field, Relationship

from app.models.base import BaseEntity


class DonorMatch(BaseEntity, table=True):
    __tablename__ = "donor_matches"

    campaign_id: int = Field(foreign_key="campaigns.id")

    donor_id: int = Field(foreign_key="donors.id")

    confidence_score: float

    reasoning: str
