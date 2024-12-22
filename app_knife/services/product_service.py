from typing import Union, List
from app_knife.abstracts.abc_product_repository import AbcProductRepository
from abstracts.abc_redis_repository import AbcRedisRepository
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.abstracts.abc_product_service import AbcProductService
from abstracts.abc_handle_redis import AbcHandleRedis
from schemas.product_schema import ProductSchemaIn, ProductSchemaModify
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice
from app_knife.schemas.response_schema import ResponseSchema


class ProductService(AbcProductService):

    def __init__(self, _knife_repository: AbcKnifeRepository):
        self._knife_repository = _knife_repository
        self.product_repository: AbcProductRepository = _knife_repository.product_repository
        self.redis_repository: AbcRedisRepository = _knife_repository.redis_repository
        self.handle_redis: AbcHandleRedis = _knife_repository.handle_redis

    @property
    def knife_repository(self) ->AbcKnifeRepository:
        return self._knife_repository

    def s_get_products_all(self)->Union[List[ProductSchemaDtoPrice], ResponseSchema]:
        products = self.redis_repository.get_products_all()
        if isinstance(products, ResponseSchema):
            return products

        return [ProductSchemaDtoPrice.model_validate(product) for product in products]

    def s_get_product_by_model(self, model: str)->Union[ProductSchemaDtoPrice, ResponseSchema]:
        product = self.redis_repository.get_product_by_model(model)
        if isinstance(product, ResponseSchema):
            return product

        return ProductSchemaDtoPrice.model_validate(product)

    def s_create_product_new(self, request: ProductSchemaIn)->ResponseSchema:
        response: ResponseSchema = self.product_repository.create_product_new(request)
        if response.code == 201:
            self.handle_redis.update_cache()
        return response

    def s_modify_product_by_model(self, model: str, request: ProductSchemaModify)->ResponseSchema:
        product = self.product_repository.get_product_by_model(model)
        if isinstance(product, ResponseSchema):
            return product

        response: ResponseSchema = self.product_repository.modify_product(product, request)
        if response.code == 202:
            self.handle_redis.update_cache()
        return response

    def s_delete_product(self, model)->ResponseSchema:
        product = self.product_repository.get_product_by_model(model)
        if isinstance(product, ResponseSchema):
            return product

        response: ResponseSchema = self.product_repository.delete_product(product)
        if response.code == 204:
            self.handle_redis.update_cache()
        return response
