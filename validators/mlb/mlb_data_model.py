"""Module that is the MLB Crawled Data Model"""

from typing import List, Dict

from pydantic import BaseModel, field_validator
from pytest import skip

from validators import BaseParsedData


class HitLocation(BaseModel):
    """Hit Location data model"""

    pattern_type: str
    play_type: str
    play_location: str


class PitchZonesRaw(BaseModel):
    """Pitch zones raw data model"""

    vertical_value: float
    horizontal_value: float


class HitLocations(BaseModel):
    """Hit Locations data model"""

    ball_in_play: bool
    location_zones: PitchZonesRaw
    hit_location: HitLocation | None


class RunnersOnBase(BaseModel):
    """Runnes on base data model"""

    runners_1st: int
    runners_2nd: int
    runners_3rd: int


class PitchLocationZones(BaseModel):
    """Pitch location zones data model"""

    vertical_zone: str
    horizontal_zone: str


class PitchLocations(BaseModel):
    """Pitch locations data model"""

    pitch_zone: str
    pitch_zones_raw: PitchZonesRaw
    pitch_locations: PitchLocationZones


class MLBInningPitchSequence(BaseModel):
    """MLB inning pitch sequence data model"""

    pitch_number: str | None
    pitch_outcome: str | None
    pitch_type_result: str | None
    pitch_type: str | None
    pitch_mph: str | None
    pitch_locations: PitchLocations | None
    runners_on_base: RunnersOnBase | None
    hit_location: HitLocations | None


class MLBInningPlays(BaseModel):
    """MLB innin plays data model"""

    play: str
    away_score: str
    home_score: str
    pitch_sequence: List[MLBInningPitchSequence]


class MLBInningSubstitutes(BaseModel):
    """MLB inning substitutes data model"""

    substitute_info: str


class MLBInningPitchers(BaseModel):
    """Mlb inning pitchers data model"""

    player_info: str


class MLBInningData(BaseModel):
    """Mlb inning data data model"""

    away_team: str
    home_team: str
    pitchers: List[MLBInningPitchers]
    substitutes: List[MLBInningSubstitutes]
    plays: List[MLBInningPlays]


class MLBPlayByPlayData(BaseModel):
    """Mlb play by play data model"""

    inning: str
    inning_data: MLBInningData


class MLBPlayByPlayInfo(BaseModel):
    """mlb play by play info data model"""

    game_id: str
    url: str
    path: str


class MLBScoringPlayInfo(BaseModel):
    """mlb scoring plays info data model"""

    inning: str
    scoring_play: str
    away_runs_scored: str
    home_runs_scored: str


class MLBScoringPlays(BaseModel):
    """mlb scoring plays data model"""

    scoring_plays: List[MLBScoringPlayInfo]


class MLBScoringSummary(BaseModel):
    """mlb scoring summary data model"""

    top_inning_info: Dict[str, MLBScoringPlays]
    bottom_inning_info: Dict[str, MLBScoringPlays]


class MLBGlossaryData(BaseModel):
    """mlb glossary data model"""

    notes: List[str]
    categories: Dict[str, Dict[str, str]]


class MLBParsedBoxScores(BaseModel):
    """mlb parsed box scores data model"""

    glossary_data: MLBGlossaryData
    box_score_data: List[Dict[str, str]]


class MLBBoxScoredata(BaseModel):
    """mlb box score data model"""

    # TODO: Uncomment when I want linescore and scoring summary data
    # parsed_linescore: Dict[str, Dict[str, str]]
    parsed_box_scores: List[Dict[str, MLBParsedBoxScores]]
    # scoring_summary: MLBScoringSummary

    # @field_validator("parsed_linescore")
    # def validate_parsed_linescore(cls, values):
    #     """function that validates the parsed linescore data is present"""
    #     # pylint: disable=no-self-argument
    #     if "pitching_data" not in values:
    #         raise ValueError("Key 'pitching_data' must be present in parsed_linescore")
    #     team_keys = [key for key in values.keys() if key != "pitching_data"]
    #     if len(team_keys) != 2:
    #         raise ValueError(
    #             "There must be exactly two team abbreviation keys in parsed_linescore"
    #         )
    #     team_key_columns = {
    #         key for team_key in team_keys for key in values.get(team_key, {}).keys()
    #     }
    #     expected = {"R", "H", "E"}
    #     if not expected.issubset(team_key_columns):
    #         raise ValueError(
    #             f"The following linescore columns must be present: {expected}"
    #         )
    #     return values


class MLBTeamScoreboardValues(BaseModel):
    """mlb team scoreboard values data model"""

    runs: int
    hits: int
    errors: int


class MLBTeamRecords(BaseModel):
    """mlb team records data model"""

    team_records: List[str]
    record_overall: str
    site_record: str


class MLBParsedData(BaseParsedData):
    """mlb parsed data data model"""

    team_1_records: MLBTeamRecords
    team_1_scoreboard_values: MLBTeamScoreboardValues
    team_2_records: MLBTeamRecords
    team_2_scoreboard_values: MLBTeamScoreboardValues
    box_score_data: MLBBoxScoredata
    play_by_play_data_info: MLBPlayByPlayInfo | None = None
    play_by_play_data: List[MLBPlayByPlayData] | None = []
