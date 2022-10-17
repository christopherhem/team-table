from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class Error(BaseModel):
    message:str

class SubUrlIn(BaseModel):
    url:str

class SubUrlOut(BaseModel):
    id:int
    url:str

class EventVoIn(BaseModel):
    id : int
    team_href: str
    shift_start: Optional[str]
    shift_end: Optional[str]
    availability_start: str
    availability_end: str

class TeamVoIn(BaseModel):
    team_id: int
    name: str
    username: str
