from fastapi import (
    APIRouter, 
    Depends, 
    Response, 
    HTTPException,
    Request,
)
from typing import (
    List, 
    Optional, 
    Union
)
from queries.users import (
    Error,
    User,
    UserIn,
    UserOut,
    UserPut,
    UserQueries,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel

class UserForm(BaseModel):
    username: str
    password: str 
class UserToken(Token):
    user: UserOut

router = APIRouter()

@router.get("/users", response_model=Union[List[UserOut], Error])
def get_all_users(queries: UserQueries = Depends(),):
    return queries.get_all()

@router.get("/users/{user_id}", response_model=Optional[UserOut])
def get_one_user(
    user_id: int,
    query: UserQueries = Depends(),
) -> UserOut:
    user = query.get_one(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f'Username error: User not found.')
    return user

@router.post("/users", response_model=Union[UserToken, Error])
async def create_user(
    info: UserIn,
    request: Request,
    response: Response,
    queries: UserQueries = Depends(),
):
    users = queries.get_all() 
    for u in users:
        if info.username == u.username:
            raise HTTPException(status_code=409, detail=f'Username error: {info.username} already exists...')
        if info.email == u.email:
            raise HTTPException(status_code=409, detail=f'Email error: {info.email} has already been used...')
    hashed_password = authenticator.hash_password(info.password)
    user = queries.create(info, hashed_password)
    form = UserForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, queries)
    return UserToken(user=user, **token.dict())


@router.put("/users/{user_id}", response_model=Union[UserPut, Error])
def update_user(
    user_id: int,
    user: UserIn,
    query: UserQueries = Depends(),
) -> Union[Error, UserPut]:
    return query.update(user_id, user)

@router.delete("/users/{user_id}", response_model=bool)
def delete_user(
    user_id: int,
    query: UserQueries = Depends(),
) -> bool:
    return query.delete(user_id)
