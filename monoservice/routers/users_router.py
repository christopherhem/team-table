from fastapi import (
    APIRouter,
    Depends,
    Cookie,
    Response,
    HTTPException,
    status,
    Request,
)
from typing import List, Optional, Union
from queries.users_queries import *
import os
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel


class UserForm(BaseModel):
    username: str
    password: str


class UserToken(Token):
    user: UserOut


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


SIGNING_KEY = os.environ["SIGNING_KEY"]
ALGORITHM = "HS256"
COOKIE_NAME = "users_access_token"

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


async def get_current_user(
    bearer_token: Optional[str] = Depends(oauth2_scheme),
    cookie_token: Optional[str] | None = (Cookie(default=None, alias=COOKIE_NAME)),
    repo: UserQueries = Depends(),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = bearer_token
    if not token and cookie_token:
        token = cookie_token
    try:
        payload = jwt.decode(token, SIGNING_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = repo.get_user(email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.get("/api/users", response_model=Union[List[UserOut], Error])
def get_all_users(
    queries: UserQueries = Depends(),
):
    return queries.get_all()


@router.get("/api/users/{user_id}", response_model=Optional[UserOut])
def get_one_user(
    user_id: int,
    query: UserQueries = Depends(),
) -> UserOut:
    user = query.get_one(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"Username error: User not found.")
    return user


@router.post("/api/users", response_model=Union[UserToken, Error])
async def create_user(
    info: UserIn,
    request: Request,
    response: Response,
    queries: UserQueries = Depends(),
):
    users = queries.get_all()
    for u in users:
        if info.username == u.username:
            raise HTTPException(
                status_code=409,
                detail=f"Username error: {info.username} already exists...",
            )
        if info.email == u.email:
            raise HTTPException(
                status_code=409,
                detail=f"Email error: {info.email} has already been used...",
            )
    hashed_password = authenticator.hash_password(info.password)
    user = queries.create(info, hashed_password)
    form = UserForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, queries)
    return UserToken(user=user, **token.dict())


@router.put("/api/users/", response_model=Union[UserOut, Error])
def update_user(
    user: UserIn,
    query: UserQueries = Depends(),
    userdict=Depends(authenticator.get_current_account_data),
):
    user_id = userdict["id"]
    hashed_password = authenticator.hash_password(user.password)
    return query.update(user_id, user, hashed_password)


@router.delete("/api/users/{user_id}", response_model=bool)
def delete_user(
    user_id: int,
    query: UserQueries = Depends(),
) -> bool:
    return query.delete(user_id)


@router.get("/token", response_model=UserToken | None)
async def get_token(
    request: Request, user: User = Depends(authenticator.try_get_current_account_data)
) -> UserToken | None:
    if user and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "user": user,
        }
