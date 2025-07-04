from datetime import date

from sqlmodel import Field

from models.base import BaseModel


class Record(BaseModel):
    record_date: date = Field(nullable=False)
    year: int = Field(default=None, nullable=False, index=True)
    home_wins: int = Field(default=0, nullable=False)
    away_wins: int = Field(default=0, nullable=False)
    home_losses: int = Field(default=0, nullable=False)
    away_losses: int = Field(default=0, nullable=False)
