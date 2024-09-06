from fastapi import APIRouter, HTTPException, status
from app.db.redis_client import get_redis_client

router = APIRouter()

redis_client = get_redis_client()

@router.delete("/unregister", response_model=dict)
async def unregister(username: str):
    if not redis_client.exists(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
        )

    redis_client.delete(username)
    return {"message": "User unregistered successfully."}
