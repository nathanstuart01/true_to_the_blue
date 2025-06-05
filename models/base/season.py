from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from models.base import BaseModel


if TYPE_CHECKING:
    from models.base import Team
    from models.base import League
    from models.base import Game

class Season(BaseModel, table=True):
    year: int = Field(default=None, nullable=False, index=True)
    league_id: int = Field(foreign_key="league.id")

    league: "League" = Relationship(back_populates="seasons")
    teams: list["Team"] = Relationship(back_populates="season")
    games: list["Game"] = Relationship(back_populates="season")
