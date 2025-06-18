"""Base module represnting parsed data model"""

from pydantic import BaseModel, Field
from datetime import datetime


class BaseParsedData(BaseModel):
    """Class representing base parsed data model"""

    internal_id: str
    timestamp: int
    date: str
    team_1_name: str
    team_1_home_away: str
    team_2_name: str
    team_2_home_away: str


class ErrorData(BaseModel):
    """Class representing error data model"""

    error: str
    url: str | None = None
    timestamp: int | None = Field(
        default_factory=lambda: int(datetime.now().timestamp())
    )
