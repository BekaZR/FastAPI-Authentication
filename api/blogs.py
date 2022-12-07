from turtle import title
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from api.oauth2 import get_current_user, oauth2_scheme

from core.dependices import get_db

from models.blogs import Blog

from schemas.blogs import BlogIn, BlogOut
from schemas.users import UserIn, UserOut

router = APIRouter()

@router.post("/post/", response_model=BlogOut)
def create_blog(blog: BlogIn, db: Session = Depends(get_db)):
    blog_db = Blog(title=blog.title, text=blog.text, user_id=blog.user_id)
    db.add(blog_db)
    db.commit()
    db.refresh(blog_db)
    return blog_db

@router.get("/blogs/", response_model=list[BlogOut])
def get_blogs(db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    print(current_user)
    return db.query(Blog).all()

