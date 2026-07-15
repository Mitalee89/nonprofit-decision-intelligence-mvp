from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.enums import GrantStatus


class GrantCreate(BaseModel):
    title: str
    organization: str
    amount: float
    eligibility: Optional[str] = None
    deadline: date


class GrantUpdate(BaseModel):
    title: Optional[str] = None
    organization: Optional[str] = None
    amount: Optional[float] = None
    eligibility: Optional[str] = None
    deadline: Optional[date] = None
    status: Optional[GrantStatus] = None


class GrantResponse(BaseModel):
    id: int

    title: str
    organization: str
    amount: float
    eligibility: Optional[str]
    deadline: date

    status: GrantStatus

    model_config = ConfigDict(
        from_attributes=True
    )