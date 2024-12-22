from sqlalchemy.orm import Session
from redis import Redis
from abstracts.abc_handle_redis import AbcHandleRedis
from handlers.handle_redis import HandleRedis
from app_knife.abstracts.abc_product_repository import AbcProductRepository
from abstracts.abc_redis_repository import AbcRedisRepository
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.repositories.product_repository import ProductRepository
from repositories.redis_repository import RedisRepository

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


    @property
    def handle_redis(self) ->AbcHandleRedis:
        return HandleRedis(self._redis, self.db)