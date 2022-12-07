from core.database import Session

from core.settings import Settings


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

