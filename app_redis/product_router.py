from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from typing import List, Union
from app_knife.depends import product_repository, model_params
from app_knife.schemas.response_schema import ResponseSchema
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice

router = APIRouter(
    prefix='/product/redis',
    tags=['Http request: Product'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}},
)

@router.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse(url='/docs')

@router.get('/all')
def get_redis_product()->str:
    return 'redis product'