from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hash_password: str) -> bool:
    return pwd_context.verify(password, hash_password)

def create_access_token(data: dict, exprires_delta: timedelta = None) -> str:
    if exprires_delta:
        expire = datetime.utcnow() + exprires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    
    to_encode = data.copy()
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
