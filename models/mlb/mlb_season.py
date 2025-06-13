from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey
from sqlmodel import Field, Relationship

from models.base import BaseModel


if TYPE_CHECKING:
    from models.mlb import MLBTeam
    from models.mlb import MLBLeague
    from models.mlb import MLBGame


class MLBSeason(BaseModel, table=True):

    __tablename__: str = "mlb_season"

    year: int = Field(default=None, nullable=False, index=True)

    league_id: int = Field(
        sa_column=Column(
            "league_id",
            ForeignKey("mlb_league.id", name="fk_mlb_season_league_id"),
            nullable=False,
        )
    )

    league: "MLBLeague" = Relationship(back_populates="seasons")
    # teams: list["MLBTeam"] = Relationship(
    #     back_populates="seasons", li_
