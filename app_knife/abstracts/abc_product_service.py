from abc import ABC, abstractmethod
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.schemas.product_schema import ProductSchemaIn, ProductSchemaModify
from app_knife.models.product import Product

class AbcProductService(ABC):

    @property
    @abstractmethod
    def knife_repository(self)->AbcKnifeRepository:
        raise NotImplementedError

    @abstractmethod
    def s_get_products_all(self):
        raise NotImplementedError

    @abstractmethod
    def s_get_product_by_model(self, model: str):
        raise NotImplementedError

    @abstractmethod
    def s_create_product_new(self, request: ProductSchemaIn):
        raise NotImplementedError

    @abstractmethod
    def s_modify_product_by_model(self, model: str, request: ProductSchemaModify):
        raise NotImplementedError

    @abstractmethod
    def s_delete_product(self, model: str):
        raise NotImplementedError