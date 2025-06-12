from datetime import datetime
from typing import Optional

from pendulum import now
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    id: int = Field(default=None, primary_key=True, index=True)
    created_at: datetime = Field(default_factory=now, nullable=False)
    updated_at: Optional[datetime] = Field(default=None, nullable=True)

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
