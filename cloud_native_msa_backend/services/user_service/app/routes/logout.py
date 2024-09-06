from fastapi import APIRouter

router = APIRouter()

@router.post("/logout", response_model=dict)
async def logout(username: str):
    # 로그아웃 관련 로직
    return {"message": f"User {username} logged out successfully."}

