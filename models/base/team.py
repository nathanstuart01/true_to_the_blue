from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from models.base import BaseModel


if TYPE_CHECKING:
    from models.base import League

class Team(BaseModel, table=True):
    name: str
    year: int = Field(default=None, nullable=False, index=True)
    league_id: int = Field(foreign_key="league.id")
    league: "League" = Relationship(back_populates="teams")

    #records: List[Record] = Relationship(back_populates="team")