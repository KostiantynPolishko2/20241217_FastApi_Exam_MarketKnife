from abstracts.abc_handle_redis import AbcHandleRedis
from redis import Redis
from sqlalchemy.orm import Session
import json
from app_knife.models.product import Product
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice

class HandleRedis(AbcHandleRedis):

    def __init__(self, r: Redis, db: Session):
        self.r = r
        self.db = db


    def load_cache(self) ->None:
        # pass
        products_sql = self.db.query(Product).all()
        if not products_sql:
            raise ValueError
        products_pyd = [ProductSchemaDtoPrice.model_validate(product_sql).model_dump() for product_sql in products_sql]
        self.r.set('products', json.dumps(products_pyd))

    def update_cache(self) ->None:
        self.r.flushdb()
        self.load_cache()

