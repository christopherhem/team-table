from pydantic import BaseModel
from typing import Literal

class EventIn(BaseModel):
    shift_start: str
    shift_end: str
    event_type: Literal("shift")
    user_href: str
    team_href: str

class EventOut(BaseModel):
    shift_start: str
    shift_end: str
    event_type: Literal("shift")
    user_href: str
    team_href: str

class TableOut(BaseModel):
    events: list[EventOut]

class UserVoOut(BaseModel):
    href: str
    first_name: str

class TeamVoOut(BaseModel):
    href: str
    name: str
