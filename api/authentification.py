from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from models.users import User

from schemas.authentification import Login

from sqlalchemy.orm import Session

from core.dependices import get_db
from schemas.users import UserOut

from services.hash_password import verify_password, pwd_context

router = APIRouter()


@router.post("/login", response_model=UserOut)
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    
    return user