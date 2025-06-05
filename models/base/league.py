from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from models.base import BaseModel


if TYPE_CHECKING:
    from models.base import Team

class League(BaseModel, table=True):
    year: int = Field(default=None, nullable=False, index=True)
    name: str = Field(default=None, nullable=False, index=True)

    teams: list["Team"] = Relationship(back_populates="league") 
