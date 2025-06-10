from typing import TYPE_CHECKING
from enum import Enum

from sqlmodel import Field, Relationship

from models.base import BaseModel

if TYPE_CHECKING:
    from models.base import Team

class BoxScoreType(str, Enum):
    HITTING = "hitting"
    PITCHING = "pitching"

class BoxScore(BaseModel, table=True):
    box_score_type: BoxScoreType = Field(nullable=False, index=True)

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

    team_1_id: int = Field(foreign_key="team.id")
    team_2_id: int = Field(foreign_key="team.id")
    mlb_game_id: int = Field(foreign_key="mlbgame.id")

