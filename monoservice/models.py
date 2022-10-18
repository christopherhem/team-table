from pydantic import BaseModel
from typing import Literal, Optional
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

<<<<<<< HEAD:monoservice/routers/models.py
class TeamVoIn(BaseModel):
    team_id: int
    name: str
    username: str
=======

class Error(BaseModel):
    message: str

class User(BaseModel):
    id: int
    username: str
    hashed_password: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    profile_picture_href: str

class UserIn(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    profile_picture_href: str

class UserOut(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    profile_picture_href: Optional[str]

class UserPut(BaseModel):
    id: int
    hashed_password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    profile_picture_href: Optional[str]
>>>>>>> main:monoservice/models.py
