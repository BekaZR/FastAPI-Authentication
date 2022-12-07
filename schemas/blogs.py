from pydantic import BaseModel


class BlogIn(BaseModel):
    title: str
    text: str
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Cars",
                "text": "Your text",
            }
        }


class BlogOut(BaseModel):
    id: int
    title: str
    text: str
    user_id: int
    
    class Config:
        orm_mode=True