from sqlmodel import Field

from app.models.base import BaseEntity


class GrantMatch(BaseEntity, table=True):
    __tablename__ = "grant_matches"

    campaign_id: int = Field(foreign_key="campaigns.id")

    grant_id: int = Field(foreign_key="grants.id")

    confidence_score: float

    reasoning: str