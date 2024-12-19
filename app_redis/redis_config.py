from fastapi import FastAPI, HTTPException, status
from redis_om import Migrator
from redis import Redis, ConnectionPool
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
import json
from app_knife.models.product import Product
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice
from app_knife.databases.database import SessionLocal

def redis_open(app: FastAPI)->None:
    pool = ConnectionPool(host='127.0.0.1', port=6379, db=0)
    app.state.redis = Redis(connection_pool=pool, decode_responses=True)
    Migrator().run()


def redis_close(app: FastAPI)->None:
    app.state.redis.flushdb()
    app.state.redis.close()


def load_products(app: FastAPI, db: Session)->None:
    # pass
    products_sql = db.query(Product).all()
    products_pyd = [ProductSchemaDtoPrice.model_validate(product_sql).model_dump() for product_sql in products_sql]
    app.state.redis.set('products', json.dumps(products_pyd))


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        redis_open(app)
        with SessionLocal() as db:
            load_products(app, db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='failed cached loading')
    yield
    redis_close(app)