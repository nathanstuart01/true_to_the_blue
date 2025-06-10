from sqlmodel import Field

from models.base import Game

class MLBGame(Game, table=True):
    """
    MLB Game model inheriting from the base Game model.
    This class can be extended with MLB-specific fields and methods.
    """
    __tablename__: str = "mlbgame"
    
    boxscore_id: int = Field(foreign_key="boxscore.mlb_game_id", primary_key=True)

