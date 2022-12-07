from sqlalchemy import orm
from models.users import User


import jwt
from fastapi import Depends, HTTPException
from core.dependices import get_db
from api.oauth2 import oauth2_scheme
from schemas.users import UserIn, UserOut

from services.token import SECRET_KEY



def get_current_user(
    db: orm.Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = db.query(User).filter(User.username == payload["username"]).first()
    except:
        raise HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )

    return UserOut.from_orm(user)