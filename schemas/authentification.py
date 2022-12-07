from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True