from fastapi import FastAPI, APIRouter, HTTPException, status
from contextlib import asynccontextmanager
from app_knife.databases.database import SessionLocal
from redis_cache.utils import load_cache, redis_close
from app_knife.depends import _redis


@asynccontextmanager
async def router_lifespan(app: FastAPI):
    try:
        with SessionLocal() as db:
            load_cache(_redis, db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='failed cached loading')
    yield
    redis_close(_redis)


router = APIRouter(
    prefix='/redis_cache/product',
    tags=['Http request: Product'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}},
    lifespan=router_lifespan
)