from datetime import datetime, UTC
from typing import Optional

from sqlmodel import SQLModel, Field


class BaseEntity(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))