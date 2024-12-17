from abc import ABC, abstractmethod
from models.product import Product
from schemas.product_schema import ProductSchemaIn, ProductSchemaOut

class AbcProductRepository(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_model(self, model: str):
        raise NotImplementedError