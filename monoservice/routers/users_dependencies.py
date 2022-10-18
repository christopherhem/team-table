from fastapi import (
    Depends,
    Cookie, 
    Response, 
    HTTPException,
    status,
    Header
)
from typing import (
    Optional, 
)
import os

from fastapi.security import OAuth2AuthorizationCodeBearer

from jose import JWTError, jwt


SIGNING_KEY = os.environ["SIGNING_KEY"]
ALGORITHM = "HS256"
oauth2_scheme = OAuth2AuthorizationCodeBearer(authorizationUrl="",tokenUrl="token", auto_error=False)

async def get_current_user(
    # token: Optional[str] = Depends(oauth2_scheme),
    authorization: str | None = Header(default=None)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    if not authorization or not authorization.startswith("Bearer"):
        raise credentials_exception
    token = authorization[7:].strip()
    try:
        return jwt.decode(token, SIGNING_KEY, algorithms=[ALGORITHM])
    except (JWTError, AttributeError) as e:
        print(e)
        raise credentials_exception
