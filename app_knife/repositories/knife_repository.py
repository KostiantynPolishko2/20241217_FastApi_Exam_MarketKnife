from sqlalchemy.orm import Session
from redis import Redis
from app_knife.abstracts.abc_product_repository import AbcProductRepository
from app_knife.abstracts.abc_redis_repository import AbcRedisRepository
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.repositories.product_repository import ProductRepository
from app_knife.repositories.redis_repository import RedisRepository

class KnifeRepository(AbcKnifeRepository):

    def __init__(self, db: Session, _redis: Redis):
        self.db = db
        self._redis = _redis

    @property
    def product_repository(self) ->AbcProductRepository:
        return ProductRepository(self.db)

    @property
    def redis_repository(self) -> AbcRedisRepository:
        return RedisRepository(self._redis)