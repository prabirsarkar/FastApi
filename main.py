from fastapi import FastAPI

from database.connection import engine, Base

# Import models
from models.user import User
from models.employee import Employee

# Import routers (IMPORTANT)
from routers import users, employees

app = FastAPI(
    title="FastAPI MySQL Project",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(users.router)
app.include_router(employees.router)


@app.get("/")
def home():
    return {
        "message": "FastAPI API is running successfully"
    }