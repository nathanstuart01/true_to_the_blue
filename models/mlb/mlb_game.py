from typing import Optional, TYPE_CHECKING

from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, Relationship
from models.base import Game

if TYPE_CHECKING:
    from models.mlb import MLBBoxScore
    from models.mlb import MLBTeam
    from models.mlb import MLBSeason


class MLBGame(Game, table=True):

    __tablename__: str = "mlb_game"

    boxscore_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            "boxscore_id",
            ForeignKey("mlb_boxscore.id", name="fk_mlb_game_boxscore_id"),
            nullable=True,
        ),
    )

    home_team_id: int = Field(
        sa_column=Column(
            "home_team_id",
            ForeignKey("mlb_team.id", name="fk_mlb_game_home_team_id"),
            nullable=False,
        )
    )

    away_team_id: int = Field(
        sa_column=Column(
            "away_team_id",
            ForeignKey("mlb_team.id", name="fk_mlb_game_away_team_id"),
            nullable=False,
        )
    )

    box_score: Optional["MLBBoxScore"] = Relationship(back_populates="mlb_game")

    home_team: Optional["MLBTeam"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [home_team_id]}
    )

    away_team: Optional["MLBTeam"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [away_team_id]}
    )

    season: "MLBSeason" = Relationship(back_populates="games")
