from jose import jwt
from datetime import datetime, timedelta
from typing import Dict
from hashlib import sha256
from fastapi import HTTPException, status

SECRET_KEY = "your_secret_key"  # 이 값을 환경 변수로 설정하거나 안전하게 보관하세요
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: Dict) -> str:
    """
    JWT 액세스 토큰 생성 함수
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Dict:
    """
    JWT 토큰 디코딩 및 유효성 검증
    """
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_password_hash(password: str) -> str:
    """
    비밀번호를 SHA-256 해시로 변환
    """
    return sha256(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    평문 비밀번호와 해시된 비밀번호 비교
    """
    return get_password_hash(plain_password) == hashed_password


# import jwt
# from datetime import datetime, timedelta
# from typing import Dict
# from hashlib import sha256
# from fastapi import HTTPException, status

# SECRET_KEY = "your_secret_key"  # 이 값을 환경 변수로 설정하거나 안전하게 보관하세요
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# def create_access_token(data: Dict):
#     """
#     JWT 액세스 토큰 생성 함수
#     """
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     """
#     평문 비밀번호와 해시된 비밀번호 비교
#     """
#     return get_password_hash(plain_password) == hashed_password

# def get_password_hash(password: str) -> str:
#     """
#     비밀번호를 SHA-256 해시로 변환
#     """
#     return sha256(password.encode()).hexdigest()

# def decode_access_token(token: str) -> Dict:
#     """
#     JWT 토큰 디코딩 및 유효성 검증
#     """
#     try:
#         decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return decoded_jwt
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Token expired",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     except jwt.InvalidTokenError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
