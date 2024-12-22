from abc import ABC, abstractmethod
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.schemas.product_schema import ProductSchemaIn

class AbcProductService(ABC):

    @property
    @abstractmethod
    def knife_repository(self)->AbcKnifeRepository:
        raise NotImplementedError


    @abstractmethod
    def s_create_product_new(self, request: ProductSchemaIn):
        raise NotImplementedError