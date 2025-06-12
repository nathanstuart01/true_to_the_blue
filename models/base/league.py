from sqlmodel import Field

from models.base import BaseModel


class League(BaseModel):
    year: int = Field(default=None, nullable=False, index=True)
    name: str = Field(default=None, nullable=False, index=True)
