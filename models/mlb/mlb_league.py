from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from models.base import BaseModel

if TYPE_CHECKING:
    from models.mlb import MLBSeason
    from models.mlb import MLBTeam


class MLBLeague(BaseModel, table=True):

    __tablename__: str = "mlb_league"

    year: int = Field(default=None, nullable=False, index=True)
    name: str = Field(default=None, nullable=False, index=True)

    seasons: list["MLBSeason"] = Relationship(back_populates="league")
    teams: list["MLBTeam"] = Relationship(back_populates="league")
