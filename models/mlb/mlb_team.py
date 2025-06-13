from typing import TYPE_CHECKING

from sqlmodel import Relationship, Field
from sqlalchemy import Column, ForeignKey

from models.base import Team

if TYPE_CHECKING:
    from models.mlb import MLBBoxScore
    from models.mlb import MLBSeason
    from models.mlb import MLBLeague
    from models.mlb import MLBRecord


class MLBTeam(Team, table=True):
    __tablename__: str = "mlb_team"

    league_id: int = Field(
        sa_column=Column(
            "league_id",
            ForeignKey("mlb_league.id", name="fk_mlb_team_league_id"),
            nullable=False,
        )
    )
    season_id: int = Field(
        sa_column=Column(
            "season_id",
            ForeignKey("mlb_season.id", name="fk_mlb_team_season_id"),
            nullable=False,
        )
    )

    # seasons: list["MLBSeason"] = Relationship(
    #     back_populates="teams", link_model="MLBTeamSeasonLink"
    # )
    league: "MLBLeague" = Relationship(back_populates="teams")
    records: list["MLBRecord"] = Relationship(back_populates="team")
    box_scores_as_team_1: list["MLBBoxScore"] = Relationship(back_populates="team_1")
    box_scores_as_team_2: list["MLBBoxScore"] = Relationship(back_populates="team_2")
