from typing import Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship
from models.base import Game

if TYPE_CHECKING:
    from models.mlb import MLBBoxScore
    from models.mlb import MLBTeam
    from models.mlb import MLBSeason


class MLBGame(Game, table=True):

    __tablename__: str = "mlb_game"

    boxscore_id: Optional[int] = Field(default=None, foreign_key="mlb_boxscore.id")
    home_team_id: int = Field(foreign_key="mlb_team.id")
    away_team_id: int = Field(foreign_key="mlb_team.id")

    box_score: Optional["MLBBoxScore"] = Relationship(back_populates="mlb_game")
    home_team: Optional["MLBTeam"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [home_team_id]}
    )
    away_team: Optional["MLBTeam"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [away_team_id]}
    )
    season: "MLBSeason" = Relationship(back_populates="games")
