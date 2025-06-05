from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from models.base import BaseModel


if TYPE_CHECKING:
    from models.base import League
    from models.base import Record
    from models.base import Season


class Team(BaseModel, table=True):
    name: str
    year: int = Field(default=None, nullable=False, index=True)
    league_id: int = Field(foreign_key="league.id")
    season_id: int = Field(foreign_key="season.id")

    season: "Season" = Relationship(back_populates="teams")
    league: "League" = Relationship(back_populates="teams")
    records: list["Record"] = Relationship(back_populates="team")
