#PORT = 8001
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import login, register, logout, unregister

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(login.router, prefix="/auth", tags=["Authentication"])
app.include_router(register.router, prefix="/auth", tags=["Authentication"])
app.include_router(logout.router, prefix="/auth", tags=["Authentication"])
app.include_router(unregister.router, prefix="/auth", tags=["Authentication"])


# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from fastapi.middleware.cors import CORSMiddleware  # CORS 미들웨어 임포트
# from pydantic import BaseModel
# from typing import Optional
# from app.auth.jwt_handler import create_access_token, verify_password
# from app.db.redis_client import get_redis_client
# from app.schema.user_schema import UserCreate

# app = FastAPI()

# # CORS 설정
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 모든 출처 허용 (보안상 필요에 따라 특정 도메인으로 변경)
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# redis_client = get_redis_client()

# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str

# @app.post("/register", response_model=dict)
# async def register(user: UserCreate):
#     # Check if the user already exists
#     if redis_client.exists(user.username):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
#         )

#     # Hash the password
#     hashed_password = verify_password(user.password)

#     # Save user to Redis
#     redis_client.hset(user.username, mapping={"username": user.username, "password": hashed_password})

#     return {"message": "User registered successfully."}


# @app.post("/login", response_model=dict)
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     # Check if the user exists
#     if not redis_client.exists(form_data.username):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password"
#         )

#     # Get user data from Redis
#     stored_password = redis_client.hget(form_data.username, "password").decode()

#     # Verify password
#     if not verify_password(form_data.password, stored_password):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password"
#         )

#     # Create JWT token
#     access_token = create_access_token(data={"sub": form_data.username})

#     return {"access_token": access_token, "token_type": "bearer"}


# @app.post("/logout", response_model=dict)
# async def logout(username: str):
#     # Perform logout action, e.g., invalidate session or token
#     return {"message": f"User {username} logged out successfully."}


# @app.delete("/unregister", response_model=dict)
# async def unregister(username: str):
#     # Check if the user exists
#     if not redis_client.exists(username):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
#         )

#     # Delete user from Redis
#     redis_client.delete(username)

#     return {"message": "User unregistered successfully."}
