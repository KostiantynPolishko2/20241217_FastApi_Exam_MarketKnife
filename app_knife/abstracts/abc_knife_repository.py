from abc import ABC, abstractmethod
from abstracts.abc_product_repository import AbcProductRepository

class AbcKnifeRepository(ABC):
    @property
    @abstractmethod
    def product_repository(self)->AbcProductRepository:
        raise NotImplementedError