from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from models.base import BaseModel


if TYPE_CHECKING:
    from models.base import Team
    from models.base import Season


class League(BaseModel, table=True):
    year: int = Field(default=None, nullable=False, index=True)
    name: str = Field(default=None, nullable=False, index=True)

    seasons: list["Season"] = Relationship(back_populates="league")
    teams: list["Team"] = Relationship(back_populates="league")
