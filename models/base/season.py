from sqlmodel import Field, Relationship

from models.base import BaseModel


class Season(BaseModel):
    year: int = Field(default=None, nullable=False, index=True)
