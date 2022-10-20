from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List, Union

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

# class EventTypeTeamTypeIn(BaseModel):
#     team_type:TeamTypeOut
#     event_type:EventTypeOut

# class EventTypeTeamTypeOut(BaseModel):
#     id : int
#     team_type:TeamTypeOut
#     event_type:EventTypeOut

class PayLevelOut(BaseModel):
    id : int
    name : str
    max_members : int
    max_roles : int

class TeamIn(BaseModel):
    name : str
    type : int
    description : Optional[str]

class TeamOut(BaseModel):
    id : int
    name : str
    type : int
    description : Optional[str]
    pay_level : int

class EventVoIn(BaseModel):
    id : int
    team_href: str
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
    team: int

class RolesOut(BaseModel):
    id : int
    name : str
    team: int

class PermissionsIn(BaseModel):
    role : int
    approve_swaps: bool
    invite_members: bool
    add_roles:bool

class PermissionsOut(BaseModel):
    id : int
    role : int
    approve_swaps: bool
    invite_members: bool
    add_roles:bool

class MemberIn(BaseModel):
    member_username: str
    role: int

class MemberOut(BaseModel):
    id : int
    member_username: str
    role: int

class EventsOut(BaseModel):
    swap_events: Optional[Union[SwapEventVoOut,List[SwapEventVoOut]]]
    cover_events: Optional[Union[CoverEventVoOut,List[CoverEventVoOut]]]

