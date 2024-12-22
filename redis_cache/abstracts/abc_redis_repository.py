from abc import ABC, abstractmethod

class AbcRedisRepository(ABC):

    @abstractmethod
    def get_products_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_product_by_model(self, model: str):
        raise NotImplementedError