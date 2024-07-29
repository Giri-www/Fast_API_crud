from .database import SessionLocal
from fastapi import Depends

def get_db():
    """
    Dependency that provides a database session.
    
    Yields:
        db (SessionLocal): A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

