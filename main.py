from fastapi import FastAPI

from core.database import Base, engine

from api import authentification, blogs, users

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(authentification.router)
app.include_router(blogs.router)

