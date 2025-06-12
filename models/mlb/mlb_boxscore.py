from typing import TYPE_CHECKING, Optional

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

    team_1_id: int = Field(foreign_key="mlb_team.id")
    team_2_id: int = Field(foreign_key="mlb_team.id")
    mlb_game_id: Optional[int] = Field(default=None, foreign_key="mlb_game.id")

    team_1: Optional["MLBTeam"] = Relationship(back_populates="box_scores_as_team_1")
    team_2: Optional["MLBTeam"] = Relationship(back_populates="box_scores_as_team_2")
    mlb_game: Optional["MLBGame"] = Relationship(back_populates="box_score")
