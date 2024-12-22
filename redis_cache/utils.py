from redis import Redis, ConnectionPool
from redis_om import Migrator
from sqlalchemy.orm import Session
import json
from app_knife.models.product import Product
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice

def redis_open()->Redis:
    #pass
    pool = ConnectionPool(host='127.0.0.1', port=6379, db=0)
    _redis = Redis(connection_pool=pool, decode_responses=True)
    Migrator().run()

    return _redis


def redis_close(r: Redis)->None:
    # pass
    r.flushdb()
    r.close()


def load_cache(r: Redis, db: Session)->None:
    # pass
    products_sql = db.query(Product).all()
    if not products_sql:
        raise ValueError
    products_pyd = [ProductSchemaDtoPrice.model_validate(product_sql).model_dump() for product_sql in products_sql]
    r.set('products', json.dumps(products_pyd))

def update_cache(r: Redis, db: Session) -> None:
    r.flushdb()
    load_cache(r, db)
