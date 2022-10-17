from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class CoverEventIn(BaseModel):
    availability_start: datetime
    availability_end: datetime
    team_href: str

class CoverEventOut(BaseModel):
    id: int
    availability_start: datetime
    availability_end: datetime
    user_id: int
    team_href: str

class ShiftSwapEventIn(BaseModel):
    shift_start: datetime
    shift_end: datetime
    availability_start: datetime
    availability_end: datetime
    team_href: str

class ShiftSwapEventOut(BaseModel):
    id: int
    shift_start: datetime
    shift_end: datetime
    availability_start: datetime
    availability_end: datetime
    user_id: int
    team_href: str

class TableOut(BaseModel):
    events: list[ShiftSwapEventOut]

class EventTypeOut(BaseModel):
    id: int
    name: str

class UserVoOut(BaseModel):
    href: str
    first_name: str

class TeamVoOut(BaseModel):
    id: int
    team_href: str
    name: str
    user_id: int

class TeamVoIn(BaseModel):
    team_id: int
    name: str
    username: str
