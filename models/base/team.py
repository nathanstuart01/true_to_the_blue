from sqlmodel import Field

from models.base import BaseModel


class Team(BaseModel):
    name: str
    year: int = Field(default=None, nullable=False, index=True)
