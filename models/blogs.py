from sqlalchemy import (
    Integer, String, ForeignKey, Column
)
from sqlalchemy.orm import relationship

from core.database import Base


class Blog(Base):
    __tablename__ = "blog"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    text = Column(String(500))
    user_id = Column(Integer, ForeignKey("user.id"))
    
    user = relationship("User", back_populates="blog")
