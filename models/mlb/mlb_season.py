from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from models.base import BaseModel


if TYPE_CHECKING:
    from models.mlb import MLBTeam
    from models.mlb import MLBLeague
    from models.mlb import MLBGame


class MLBSeason(BaseModel, table=True):

    __tablename__: str = "mlb_season"

    year: int = Field(default=None, nullable=False, index=True)
    league_id: int = Field(foreign_key="league.id")

    league: "MLBLeague" = Relationship(back_populates="seasons")
    teams: list["MLBTeam"] = Relationship(
        back_populates="seasons", link_model="MLBTeamSeasonLink"
    )
    games: list["MLBGame"] = Relationship(back_populates="season")
