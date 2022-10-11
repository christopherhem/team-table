from pydantic import BaseModel
from typing import Optional, List

class Error(BaseModel):
    message:str

class SubUrlIn(BaseModel):
    url:str

class SubUrlOut(BaseModel):
    id:int
    url:str