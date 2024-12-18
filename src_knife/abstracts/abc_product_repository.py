from abc import ABC, abstractmethod
from models.product import Product
from schemas.product_schema import ProductSchemaIn, ProductSchemaOut

class AbcProductRepository(ABC):

    @abstractmethod
    def get_products_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_product_by_model(self, model: str):
        raise NotImplementedError

    @abstractmethod
    def create_product_new(self, request: ProductSchemaIn):
        raise NotImplementedError

    @abstractmethod
    def delete_product_by_model(self, model: str):
        raise NotImplementedError