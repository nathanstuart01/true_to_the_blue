from typing import Optional, TYPE_CHECKING
from datetime import date

from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, Relationship

from models.base import BaseModel

if TYPE_CHECKING:
    from models.mlb import MLBTeam


class MLBRecord(BaseModel, table=True):

    __tablename__: str = "mlb_record"

    record_date: date = Field(nullable=False)
    year: int = Field(default=None, nullable=False, index=True)
    home_wins: int = Field(default=0, nullable=False)
    away_wins: int = Field(default=0, nullable=False)
    home_losses: int = Field(default=0, nullable=False)
    away_losses: int = Field(default=0, nullable=False)

    team_id: int = Field(
        sa_column=Column(
            "team_id",
            ForeignKey("mlb_team.id", name="fk_mlb_record_mlb_team_id"),
            nullable=False,
        )
    )

    team: Optional["MLBTeam"] = Relationship(back_populates="records")
