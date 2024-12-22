from fastapi import FastAPI, APIRouter, HTTPException, status
from contextlib import asynccontextmanager
from redis_om import Migrator
from app_knife.databases.database import SessionLocal
from app_knife.redis.utils import load_products, redis_close
from app_knife.depends import _redis

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