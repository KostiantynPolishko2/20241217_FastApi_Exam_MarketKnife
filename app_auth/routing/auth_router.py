from django.db.models.functions import Trunc
from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse
# from fastapi.security import OAuth2PasswordRequestForm
from app_auth.depends import get_current_active_user
from schemas.user_schema import *
from schemas.product_schema_response import ProductSchemaResponse
from schemas.token_schema import TokenSchema
from schemas.custom_request_form_schema import CustomOAuth2PasswordRequestFormSchema
from infrastructures.user_exception import new_user_exc406
from infrastructures.auth_exception import auth_exc401
from config_auth import *
from utils import authenticate_user, create_access_token
from datetime import timedelta
from databases.database import get_db
from sqlalchemy.orm import Session
from models.user import User
from repositories.auth_repository import AuthRepository
from typing import Annotated
from app_auth.depends import get_auth_repository

router = APIRouter(
    prefix='/authorization',
    tags=['Http request: Authorization'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

@router.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')

@router.post('/signup', summary="register new user", status_code=status.HTTP_201_CREATED)
async def create_user(request: UserSchemaAuth, auth_repository: Annotated[AuthRepository, Depends(get_auth_repository)])->ProductSchemaResponse:

    auth_repository.is_exist_user(request.username)
    response = auth_repository.add_user_to_db(request)

    if response == 0:
        raise new_user_exc406

    return ProductSchemaResponse(code=status.HTTP_201_CREATED, status='created', property=f'username: {request.username}')

@router.post("/token")
async def login(form_data: Annotated[CustomOAuth2PasswordRequestFormSchema, Depends()], db: Annotated[Session, Depends(get_db)])->TokenSchema:
    user: User = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise auth_exc401

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return TokenSchema(access_token=access_token, token_type="bearer")


@router.get("/{username}", include_in_schema=False)
async def get_username(username: str, authorization: Annotated[UserSchema, Depends(get_current_active_user)], auth_repository: Annotated[AuthRepository, Depends(get_auth_repository)]):
    if len(username) <= 5:
        raise ValueError('Argument cannot be null')

    return auth_repository.get_user(username)