from fastapi import APIRouter, Depends, Response, HTTPException
from typing import List, Optional, Union
from fastapi.encoders import jsonable_encoder
from queries.users import (
    Error,
    UserIn,
    UserOut,
    UserPut,
    UserQueries,
)

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

@router.post("/users", response_model=Union[UserOut, Error])
def create_user(
    user: UserIn,
    queries: UserQueries = Depends(),
):
    users = queries.get_all() 
    for u in users:
        if user.username == u.username:
            raise HTTPException(status_code=409, detail=f'Username error: {user.username} already exists...')
        if user.email == u.email:
            raise HTTPException(status_code=409, detail=f'Email error: {user.email} has already been used...')
    return queries.create(user)


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
