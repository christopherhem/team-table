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
    event_type_href : str

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

class PayLevelIn(BaseModel):
    name : str
    max_members: int
    max_roles : int

class PayLevelOut(BaseModel):
    id : int
    name : str
    max_members : int
    max_roles : int

class TeamIn(BaseModel):
    name : str
    type : TeamTypeOut

class TeamOut(BaseModel):
    id : int
    name : str
    type : TeamTypeOut
    description : Optional[str]
    pay_level : PayLevelOut

class UserVoIn(BaseModel):
    user_href : str

class UserVoOut(BaseModel):
    id : int
    name: str

class UserEventVoIn(BaseModel):
    event_href:str

class UserEventVoOut(BaseModel):
    id : int
    user : UserVoOut
    team : TeamOut
    event_start: datetime
    event_end: datetime
    event_type: EventTypeOut

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
    user: UserVoOut
    team: TeamOut
    role: RolesOut

class MemberOut(BaseModel):
    id : int
    user: UserVoOut
    team: TeamOut
    role: RolesOut








