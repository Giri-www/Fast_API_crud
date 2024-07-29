from fastapi import FastAPI
from app.database import engine, Base
from app.routers import items

# Create the FastAPI app instance
app = FastAPI()

# Create all database tables
Base.metadata.create_all(bind=engine)

# Include the router for item-related endpoints
app.include_router(items.router, prefix="/items", tags=["items"])

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD project"}
