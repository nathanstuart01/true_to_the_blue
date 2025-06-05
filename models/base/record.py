from typing import Optional, TYPE_CHECKING
from datetime import date

from sqlmodel import Field, Relationship

from models.base import BaseModel

if TYPE_CHECKING:
    from models.base import Team


class Record(BaseModel, table=True):
    record_date: date = Field(nullable=False)
    year: int = Field(default=None, nullable=False, index=True)
    home_wins: int = Field(default=0, nullable=False)
    away_wins: int = Field(default=0, nullable=False)
    home_losses: int = Field(default=0, nullable=False)
    away_losses: int = Field(default=0, nullable=False)
    team_id: int = Field(foreign_key="team.id")

    team: Optional["Team"] = Relationship(back_populates="records")
