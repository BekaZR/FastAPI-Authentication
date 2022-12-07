from sqlalchemy import (
    Integer, String, ForeignKey, Column
)
from sqlalchemy.orm import relationship

from core.database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True)
    password = Column(String(500))
    
    


