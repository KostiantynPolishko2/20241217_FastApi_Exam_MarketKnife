from fastapi import Depends
from fastapi.responses import RedirectResponse
from app_redis.router_config import router
from app_redis.router_config import get_redis
from typing import Annotated
from redis import Redis
import json
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice


@router.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse(url='/docs')


@router.get('/all')
async def read_products_all(_redis: Annotated[Redis, Depends(get_redis)]):
    # pass
    cached_data = _redis.get('products')
    if not cached_data:
        return []

    products_json = json.loads(cached_data)
    products = [ProductSchemaDtoPrice.model_validate(product_json) for product_json in products_json]

    return products