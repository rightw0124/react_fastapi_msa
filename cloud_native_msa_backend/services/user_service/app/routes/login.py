from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.jwt_handler import create_access_token, verify_password
from app.db.redis_client import get_redis_client

router = APIRouter()

redis_client = get_redis_client()

@router.post("/login", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not redis_client.exists(form_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password"
        )

    stored_password = redis_client.hget(form_data.username, "password").decode()

    if not verify_password(form_data.password, stored_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password"
        )

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
