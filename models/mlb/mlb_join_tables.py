from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, SQLModel


class MLBTeamSeasonLink(SQLModel, table=True):

    __tablename__: str = "mlb_team_season_link"

    team_id: int = Field(
        sa_column=Column(
            "team_id",
            ForeignKey("mlb_team.id", name="fk_team_season_link_team_id"),
            primary_key=True,
            nullable=False,
        )
    )

    season_id: int = Field(
        sa_column=Column(
            "season_id",
            ForeignKey("mlb_season.id", name="fk_team_season_link_season_id"),
            primary_key=True,
            nullable=False,
        )
    )
