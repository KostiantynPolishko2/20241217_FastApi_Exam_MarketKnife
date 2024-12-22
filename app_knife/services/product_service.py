from app_knife.abstracts.abc_product_repository import AbcProductRepository
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.abstracts.abc_product_service import AbcProductService
from abc_handle_redis import AbcHandleRedis
from models.product import Product
from schemas.product_schema import ProductSchemaIn, ProductSchemaModify
from app_knife.schemas.response_schema import ResponseSchema


class ProductService(AbcProductService):

    def __init__(self, _knife_repository: AbcKnifeRepository):
        self._knife_repository = _knife_repository
        self.product_repository: AbcProductRepository = _knife_repository.product_repository
        self.handle_redis: AbcHandleRedis = _knife_repository.handle_redis

    @property
    def knife_repository(self) ->AbcKnifeRepository:
        return self._knife_repository

    def s_create_product_new(self, request: ProductSchemaIn):
        response: ResponseSchema = self.product_repository.create_product_new(request)
        if response.code == 201:
            self.handle_redis.update_cache()
        return response

    def s_modify_product_by_model(self, model: str, request: ProductSchemaModify):
        product = self.product_repository.get_product_by_model(model)
        if isinstance(product, ResponseSchema):
            return product

        response: ResponseSchema = self.product_repository.modify_product(product, request)
        if response.code == 202:
            self.handle_redis.update_cache()
        return response

    def s_delete_product(self, model):
        product = self.product_repository.get_product_by_model(model)
        if isinstance(product, ResponseSchema):
            return product

        response: ResponseSchema = self.product_repository.delete_product(product)
        if response.code == 204:
            self.handle_redis.update_cache()
        return response
