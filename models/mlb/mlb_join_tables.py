from sqlmodel import Field, SQLModel


class MLBTeamSeasonLink(SQLModel, table=True):

    __tablename__: str = "mlb_team_season_link"

    team_id: int = Field(foreign_key="mlb_team.id", primary_key=True)
    season_id: int = Field(foreign_key="mlb_season.id", primary_key=True)
