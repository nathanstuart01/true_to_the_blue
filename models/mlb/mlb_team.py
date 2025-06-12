from typing import TYPE_CHECKING

from sqlmodel import Relationship, Field

from models.base import Team

if TYPE_CHECKING:
    from models.mlb import MLBBoxScore
    from models.mlb import MLBSeason
    from models.mlb import MLBLeague
    from models.mlb import MLBRecord


class MLBTeam(Team, table=True):
    __tablename__: str = "mlb_team"

    league_id: int = Field(foreign_key="league.id")
    season_id: int = Field(foreign_key="season.id")

    seasons: list["MLBSeason"] = Relationship(
        back_populates="teams", link_model="MLBTeamSeasonLink"
    )
    league: "MLBLeague" = Relationship(back_populates="teams")
    records: list["MLBRecord"] = Relationship(back_populates="team")
    box_scores_as_team_1: list["MLBBoxScore"] = Relationship(back_populates="team_1")
    box_scores_as_team_2: list["MLBBoxScore"] = Relationship(back_populates="team_2")
