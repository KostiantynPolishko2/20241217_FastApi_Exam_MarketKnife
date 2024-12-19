from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from schemas.user_schema import UserSchema
from schemas.token_schema import TokenSchemaData
from infrastructures.credential_exception import credentials_exc401
from config_auth import *
import jwt
from jwt.exceptions import InvalidTokenError
from app_auth.utils import get_user
from databases.database import get_db
from sqlalchemy.orm import Session
from repositories.auth_repository import AuthRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/authorization/token')

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db:Annotated[Session, Depends(get_db)]):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exc401

        token_data = TokenSchemaData(username=username)

    except InvalidTokenError:
        raise credentials_exc401

    user = get_user(token_data.username, db)
    if user is None:
        raise credentials_exc401
    return user


async def get_current_active_user(current_user: Annotated[UserSchema, Depends(get_current_user)],):
    if current_user.is_disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_auth_repository(db: Annotated[Session, Depends(get_db)]):
    yield AuthRepository(db)
