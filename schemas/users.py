from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True


class UserIn(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "Beka",
                "password": "1234"
            }
        }

