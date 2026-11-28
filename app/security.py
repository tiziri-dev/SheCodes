from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os

SECRET = os.getenv("JWT_SECRET", "change_me")
ALGO = os.getenv("JWT_ALGORITHM", "HS256")
EXPIRE = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(p): return pwd_context.hash(p)
def verify_password(plain, hashed): return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=EXPIRE)
    return jwt.encode(to_encode, SECRET, algorithm=ALGO)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGO])
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token invalide")

def require_role(*roles):
    def checker(user=Depends(get_current_user)):
        if user.get("role") not in roles:
            raise HTTPException(403, "Accès refusé")
        return user
    return checker