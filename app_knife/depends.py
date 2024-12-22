from fastapi import Depends, Path
from typing import Annotated
from sqlalchemy.orm import Session
from redis import Redis
from app_knife.databases.database import SessionLocal
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.abstracts.abc_product_repository import AbcProductRepository
from app_knife.abstracts.abc_redis_repository import AbcRedisRepository
from app_knife.repositories.knife_repository import KnifeRepository
from redis_cache.utils import redis_open
from abc_handle_redis import AbcHandleRedis
from app_knife.abstracts.abc_product_service import AbcProductService
from app_knife.services.product_service import ProductService
from app_knife.schemas.lower_case_path import LowerCasePath

_redis = redis_open()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Dependency to access Redis
def get_redis()->Redis:
    if not _redis:
        raise RuntimeError('redis_cache is not initialized!')
    yield _redis


def get_knife_repository(db: Annotated[Session, Depends(get_db)])->AbcKnifeRepository:
    return KnifeRepository(db, _redis)

def get_redis_repository(db: Annotated[Session, Depends(get_db)], _redis: Annotated[Redis, Depends(get_redis)])->AbcRedisRepository:
    return KnifeRepository(db, _redis).redis_repository

def get_handle_redis(db: Annotated[Session, Depends(get_db)], _redis: Annotated[Redis, Depends(get_redis)])->AbcHandleRedis:
    return KnifeRepository(db, _redis).handle_redis

def get_product_repository(db: Annotated[Session, Depends(get_db)])->AbcProductRepository:
    return KnifeRepository(db, _redis).product_repository

def get_product_service(_knife_repository: Annotated[AbcKnifeRepository, Depends(get_knife_repository)])->AbcProductService:
    return ProductService(_knife_repository)

knife_repository = Annotated[AbcKnifeRepository, Depends(get_knife_repository)]
redis_repository = Annotated[AbcRedisRepository, Depends(get_redis_repository)]
handle_redis = Annotated[AbcHandleRedis, Depends(get_handle_redis)]
product_repository = Annotated[AbcProductRepository, Depends(get_product_repository)]
product_service = Annotated[AbcProductService, Depends(get_product_service)]

model_params = Annotated[str, Path(description='knife model', min_length=2, max_length=12)]
model_params2 = Annotated[LowerCasePath, Path(description="knife model", min_length=2, max_length=12)]

def to_lowercase(model: str = Path(description="knife model", min_length=2, max_length=12)) -> str:
    return model.lower()

model_params3 = Annotated[str, Depends(to_lowercase)]