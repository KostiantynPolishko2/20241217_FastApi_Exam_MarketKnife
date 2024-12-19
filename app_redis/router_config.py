from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from contextlib import asynccontextmanager
from app_redis.utils import redis_open, redis_close, load_products
from app_knife.databases.database import SessionLocal
from redis import Redis, ConnectionPool
from redis_om import Migrator

_redis = redis_open()

@asynccontextmanager
async def router_lifespan(app: FastAPI):
    try:
        Migrator().run()
        with SessionLocal() as db:
            load_products(_redis, db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='failed cached loading')
    yield
    redis_close(_redis)


router = APIRouter(
    prefix='/redis/product',
    tags=['Http request: Product'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}},
    lifespan=router_lifespan
)


# Dependency to access Redis
def get_redis()->Redis:
    if not _redis:
        raise RuntimeError('redis is not initialized!')
    yield _redis