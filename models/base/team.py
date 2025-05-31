from typing import List

from sqlmodel import SQLModel, Field, Relationship

from models.base.league import League

class Team(SQLModel, table=True):
    name: str
    year: int = Field(default=None, nullable=False, index=True)
    league_id: int = Field(foreign_key="league.id")
    league: League = Relationship(back_populates="teams")

    #records: List[Record] = Relationship(back_populates="team")