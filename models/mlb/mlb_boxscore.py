from typing import TYPE_CHECKING, Optional

from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, Relationship

from models.base import BaseModel

if TYPE_CHECKING:
    from models.mlb import MLBTeam
    from models.mlb import MLBGame


class MLBBoxScore(BaseModel, table=True):

    __tablename__: str = "mlb_boxscore"

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

    team_1_id: int = Field(
        sa_column=Column(
            "team_1_id",
            ForeignKey("mlb_team.id", name="fk_mlb_boxscore_team_1_id"),
            nullable=False,
        )
    )
    team_2_id: int = Field(
        sa_column=Column(
            "team_2_id",
            ForeignKey("mlb_team.id", name="fk_mlb_boxscore_team_2_id"),
            nullable=False,
        )
    )
    mlb_game_id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            "mlb_game_id",
            ForeignKey("mlb_game.id", name="fk_mlb_boxscore_mlb_game_id"),
            nullable=True,
        ),
    )

    team_1: Optional["MLBTeam"] = Relationship(back_populates="box_scores_as_team_1")
    team_2: Optional["MLBTeam"] = Relationship(back_populates="box_scores_as_team_2")
    mlb_game: Optional["MLBGame"] = Relationship(back_populates="box_score")
