from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class Error(BaseModel):
    message : str

class EventTypeIn(BaseModel):
    name : str
    event_type_href : str

class EventTypeOut(BaseModel):
    id : int
    name : str
    table_name : str

class TeamTypeIn(BaseModel):
    name: str

class TeamTypeOut(BaseModel):
    id : int
    name : str

class EventTypeTeamTypeIn(BaseModel):
    team_type:TeamTypeOut
    event_type:EventTypeOut

class EventTypeTeamTypeOut(BaseModel):
    id : int
    team_type:TeamTypeOut
    event_type:EventTypeOut

class PayLevelOut(BaseModel):
    id : int
    name : str
    max_members : int
    max_roles : int

class PayLevelsOut(BaseModel):
    pay_levels: list[PayLevelOut]

class TeamIn(BaseModel):
    name : str
    type : TeamTypeOut
    description : Optional[str]

class TeamOut(BaseModel):
    id : int
    name : str
    type : TeamTypeOut
    description : Optional[str]
    pay_level : PayLevelOut

class TeamsOut(BaseModel):
    teams: list[TeamOut]

class EventVoIn(BaseModel):
    event_href: str
    owner: str
    team: int
    shift_start: Optional[datetime]
    shift_end: Optional[datetime]
    availability_start: datetime
    availability_end: datetime

class CoverEventVoOut(BaseModel):
    id : int
    event_href: str
    owner: str
    team: int
    availability_start: datetime
    availability_end: datetime

class SwapEventVoOut(BaseModel):
    id:int
    event_href: str
    owner: str
    team: int
    shift_start: datetime
    shift_end: datetime
    availability_start: datetime
    availability_end: datetime
    

class RolesIn(BaseModel):
    name: str
    team: TeamOut

class RolesOut(BaseModel):
    id : int
    name : str
    team: TeamOut

class PermissionsIn(BaseModel):
    role : RolesOut
    approve_swaps: bool
    invite_members: bool
    add_roles:bool

class PermissionsOut(BaseModel):
    id : int
    role : RolesOut
    approve_swaps: bool
    invite_members: bool
    add_roles:bool

class MemberIn(BaseModel):
    member: str
    role: RolesOut

class MemberOut(BaseModel):
    id : int
    member: str
    role: RolesOut
