from fastapi import FastAPI

from core.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

