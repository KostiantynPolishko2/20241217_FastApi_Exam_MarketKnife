from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from config_auth import *
from sqlalchemy.orm import Session
from models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str)->bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str)->str:
    return pwd_context.hash(password)

def get_user(username: str, db: Session)->User:
    user = db.query(User).filter(User.username == username.lower()).first()
    if user is not None:
        return user


def authenticate_user(username: str, password: str, db: Session)->User | bool:
    user: User = get_user(username, db)

    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None)->str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt