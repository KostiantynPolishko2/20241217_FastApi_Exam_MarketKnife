from fastapi import status
from redis import Redis
import json
from typing import List, Union
from app_knife.abstracts.abc_redis_repository import AbcRedisRepository
from app_knife.schemas.response_schema import ResponseSchema
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice

class RedisRepository(AbcRedisRepository):

    def __init__(self, _redis: Redis):
        self._redis = _redis

    def get_products_all(self):
        try:
            cached_data = self._redis.get('products')
            if not cached_data:
                return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property='products none')

            products_json = json.loads(cached_data)
            return [ProductSchemaDtoPrice.model_validate(product_json) for product_json in products_json]

        except Exception as exc:
            return ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'get all products failed due to {exc.__cause__}')

    def get_product_by_model(self, model: str):
        try:
            response: Union[List[ProductSchemaDtoPrice], ResponseSchema] = self.get_products_all()
            if isinstance(response, ResponseSchema):
                return response

            _model = model.lower()
            product = next((product for product in response if product.model == _model), None)
            if product is None:
                return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property=f'product {_model} none')
            return product

        except Exception as exc:
            return ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'get product by name failed due to {exc.__cause__}')