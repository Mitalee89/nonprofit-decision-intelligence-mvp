from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import ConfigDict, BaseModel, EmailStr


class DonorCreate(BaseModel):
    name: str
    email: str
    city: str | None = None
    interests: str | None = None
    preferred_cause: str | None = None
    capacity: Decimal = Decimal("0.00")


class DonorUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    city: Optional[str] = None
    interests: Optional[str] = None
    preferred_cause: Optional[str] = None
    capacity: Optional[Decimal] = None


class DonorResponse(BaseModel):
    id: int

    name: str
    email: str
    city: Optional[str]
    interests: Optional[str]
    preferred_cause: Optional[str]
    capacity: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True