from typing import Optional, TYPE_CHECKING

from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, Relationship
from models.base import Game

if TYPE_CHECKING:
    from models.mlb import MLBTeam
    from models.mlb import MLBSeason


class MLBGame(Game, table=True):

    __tablename__: str = "mlb_game"

    team_1_scoreboard_runs: int = Field(default=0, nullable=False)
    team_2_scoreboard_runs: int = Field(default=0, nullable=False)
    team_1_scoreboard_hits: int = Field(default=0, nullable=False)
    team_2_scoreboard_hits: int = Field(default=0, nullable=False)
    team_1_scoreboard_errors: int = Field(default=0, nullable=False)
    team_2_scoreboard_errors: int = Field(default=0, nullable=False)

    team_1_hitting_at_bats: int = Field(default=0, nullable=False)
    team_2_hitting_at_bats: int = Field(default=0, nullable=False)
    team_1_hitting_runs: int = Field(default=0, nullable=False)
    team_2_hitting_runs: int = Field(default=0, nullable=False)
    team_1_hitting_hits: int = Field(default=0, nullable=False)
    team_2_hitting_hits: int = Field(default=0, nullable=False)
    team_1_hitting_runs_batted_in: int = Field(default=0, nullable=False)
    team_2_hitting_runs_batted_in: int = Field(default=0, nullable=False)
    team_1_hitting_home_runs: int = Field(default=0, nullable=False)
    team_2_hitting_home_runs: int = Field(default=0, nullable=False)
    team_1_hitting_base_on_balls: int = Field(default=0, nullable=False)
    team_2_hitting_base_on_balls: int = Field(default=0, nullable=False)
    team_1_hitting_strikeouts: int = Field(default=0, nullable=False)
    team_2_hitting_strikeouts: int = Field(default=0, nullable=False)

    team_1_fielding_errors: int = Field(default=0, nullable=False)
    team_2_fielding_errors: int = Field(default=0, nullable=False)

    team_1_pitching_innings_pitched: float = Field(default=0.0, nullable=False)
    team_2_pitching_innings_pitched: float = Field(default=0.0, nullable=False)
    team_1_pitching_hits: int = Field(default=0, nullable=False)
    team_2_pitching_hits: int = Field(default=0, nullable=False)
    team_1_pitching_runs: int = Field(default=0, nullable=False)
    team_2_pitching_runs: int = Field(default=0, nullable=False)
    team_1_pitching_earned_runs: int = Field(default=0, nullable=False)
    team_2_pitching_earned_runs: int = Field(default=0, nullable=False)
    team_1_pitching_walks: int = Field(default=0, nullable=False)
    team_2_pitching_walks: int = Field(default=0, nullable=False)
    team_1_pitching_strikeouts: int = Field(default=0, nullable=False)
    team_2_pitching_strikeouts: int = Field(default=0, nullable=False)
    team_1_pitching_home_runs: int = Field(default=0, nullable=False)
    team_2_pitching_home_runs: int = Field(default=0, nullable=False)
    team_1_pitching_pitches_thrown: str = Field(default="", nullable=False)
    team_2_pitching_pitches_thrown: str = Field(default="", nullable=False)

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

    home_team: Optional["MLBTeam"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [home_team_id]}
    )

    away_team: Optional["MLBTeam"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": [away_team_id]}
    )

    season: "MLBSeason" = Relationship(back_populates="games")
