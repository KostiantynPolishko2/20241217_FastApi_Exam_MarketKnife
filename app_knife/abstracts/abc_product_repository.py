from abc import ABC, abstractmethod
from app_knife.models.product import Product
from app_knife.schemas.product_schema import ProductSchemaIn, ProductSchemaModify

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
    def modify_product(self, product: Product, request: ProductSchemaModify):
        raise NotImplementedError

    @abstractmethod
    def delete_product(self, product: Product):
        raise NotImplementedError