from typing import List

from sqlmodel import Field, Relationship

from models.base.base import BaseModel
from models.base.team import Team

class League(BaseModel, table=True):
    year: int = Field(default=None, nullable=False, index=True)
    name: str = Field(default=None, nullable=False, index=True)

    teams: List[Team] = Relationship(back_populates="league") 
