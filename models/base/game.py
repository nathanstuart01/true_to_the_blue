from typing import Optional, TYPE_CHECKING
from datetime import date

from sqlmodel import Field, Relationship

from models.base import BaseModel

if TYPE_CHECKING:
    from models.base import Team


class Game(BaseModel, table=False):
    game_date: date = Field(nullable=False)
    year: int = Field(default=None, nullable=False, index=True)
    home_team_id: int = Field(foreign_key="team.id")
    away_team_id: int = Field(foreign_key="team.id")

    home_team: Optional["Team"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [home_team_id]}
    )
    away_team: Optional["Team"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [away_team_id]}
    )
