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
    user_id : Optional[int]

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
    can_invite: bool
    can_approve: bool

class RolesOut(BaseModel):
    id : int
    name : str
    team: int
    can_invite : bool
    can_approve: bool

#permissions models functionality moved to roles model, may change in future dependant on needs.
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

class SafeCoverEventVoOut(BaseModel):
    id :int
    owner: str
    availability_start:datetime
    availability_end:datetime
    mono_id:int

class SafeSwapEventVoOut(BaseModel):
    id :int
    owner: str
    shift_start:datetime
    shift_end:datetime
    availability_start:datetime
    availability_end:datetime
    mono_id:int

class EventsOut(BaseModel):
    swap_events: List[SafeSwapEventVoOut] | SafeSwapEventVoOut
    cover_events: List[SafeCoverEventVoOut] | SafeCoverEventVoOut

class ValidSwapOut(BaseModel):
    user_event : SafeSwapEventVoOut
    valid_swaps : list[SafeSwapEventVoOut]

class ValidCoverUserOut(BaseModel):
    #model for user getting a swap event covered
    user_event: SafeSwapEventVoOut
    valid_swaps : list[SafeCoverEventVoOut]

class ValidUserCoverOut(BaseModel):
    #model for user getting swap events to cover
    user_event: SafeCoverEventVoOut
    valid_swaps: list[SafeSwapEventVoOut]

class ValidSwapListOut(BaseModel):
    swaps : list[ValidSwapOut]

class ValidCoverUserListOut(BaseModel):
    covers_for_user: list[ValidCoverUserOut]

class ValidUserCoverListOut(BaseModel):
    user_covers: list[ValidUserCoverOut]
