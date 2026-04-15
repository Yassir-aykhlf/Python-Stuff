from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

class UserCreate(BaseModel):
    username: str
    email: str

@router.get("/")
async def get_users(skip: int = 0, limit: int = 10):
    return {"message": "Fetching list of users", "skip": skip, "limit": limit}

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "message": "Fetching specific user"}

@router.post("/")
async def create_user(user: UserCreate):
    return {"message": "User created successfully", "user_data": user}