from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from models.users import User

from schemas.authentification import Login
from schemas.users import UserOut
from schemas.token import Token

from sqlalchemy.orm import Session

from core.dependices import get_db

from services.hash_password import verify_password, pwd_context
from services.token import create_access_token

router = APIRouter()


@router.post("/login", response_model=Token)
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}