from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from core.settings import settings
from schemas.token import TokenData
from schemas.users import UserOut

from services.token import ALGORITHM

import jwt

from jwt import PyJWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        pk: int = payload.get("user_pk")
        if pk is None:
            raise credentials_exception
        username: str = payload.get("username")
        if pk is None:
            raise credentials_exception
        
        user = UserOut(id=pk, username=username)
    except PyJWTError:
        raise credentials_exception
    
    return user
