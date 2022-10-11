from pydantic import BaseModel
from typing import Literal

class CoverEventIn(BaseModel):
    availability_start: str
    availability_end: str
    user_id: int
    team_href: str

class CoverEventOut(BaseModel):
    id: int
    availability_start: str
    availability_end: str
    user_id: int
    team_href: str

class ShiftSwapEventIn(BaseModel):
    shift_start: str
    shift_end: str
    availability_start: str
    availability_end: str
    user_id: int
    team_href: str

class ShiftSwapEventOut(BaseModel):
    id: int
    shift_start: str
    shift_end: str
    availability_start: str
    availability_end: str
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
    href: str
    name: str
