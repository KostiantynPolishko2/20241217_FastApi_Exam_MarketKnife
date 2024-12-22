from abc import ABC, abstractmethod
from app_knife.abstracts.abc_product_repository import AbcProductRepository
from app_knife.abstracts.abc_redis_repository import AbcRedisRepository

class AbcKnifeRepository(ABC):

    @property
    @abstractmethod
    def product_repository(self)->AbcProductRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def redis_repository(self)->AbcRedisRepository:
        raise NotImplementedError