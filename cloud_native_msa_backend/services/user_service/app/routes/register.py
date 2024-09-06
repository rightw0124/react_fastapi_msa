from fastapi import APIRouter, HTTPException, status
from app.schema.user_schema import UserCreate
from app.db.redis_client import get_redis_client
from app.auth.jwt_handler import verify_password

router = APIRouter()

redis_client = get_redis_client()

@router.post("/register", response_model=dict)
async def register(user: UserCreate):
    if redis_client.exists(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    hashed_password = verify_password(user.password)
    redis_client.hset(user.username, mapping={"username": user.username, "password": hashed_password})

    return {"message": "User registered successfully."}
