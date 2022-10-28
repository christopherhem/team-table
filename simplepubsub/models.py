from pydantic import BaseModel
from typing import Optional

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
    user_id: Optional[int]

class TeamVoIn(BaseModel):
    id : int
    name : str
    type : int
    description : Optional[str]
    pay_level : int

class MemberIn(BaseModel):
    id: int
    member_username: str
    role: int
    team_href: str
