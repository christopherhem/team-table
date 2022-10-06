from fastapi import APIRouter, Depends, Response, HTTPException
from pydantic import BaseModel
from queries.users import UserQueries

router = APIRouter()

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
    password: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    profile_picture_href: str

class UsersOut(BaseModel):
    users: list[UserOut]

@router.get("api/users", response_model=UsersOut)
def users_list(queries: UserQueries = Depends()):
    return {
        "users": queries.get_all_users(),
    }