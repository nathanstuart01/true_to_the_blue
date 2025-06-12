from datetime import date

from sqlmodel import Field

from models.base import BaseModel


class Game(BaseModel):
    game_date: date = Field(nullable=False)
    year: int = Field(default=None, nullable=False, index=True)
