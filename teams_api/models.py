from pydantic import BaseModel
from typing import Optional

class Error(BaseModel):
    message : str

class TeamIn(BaseModel):
    name : str
    type : int

class TeamOut(BaseModel):
    id : int
    name : str
    type : int
    description : Optional[str]
    pay_level : int

class TeamTypeIn(BaseModel):
    name: str

class TeamTypeOut(BaseModel):
    id : int
    name : str

class EventTypesIn(BaseModel):
    name : str
    event_type_href : str

class EventTypesOut(BaseModel):
    id : int
    name : str
    event_type_href : str

class PayLevelIn(BaseModel):
    name : str
    max_members: int
    max_roles : int

class PayLevelOut(BaseModel):
    id : int
    name : str
    max_members : int
    max_roles : int


