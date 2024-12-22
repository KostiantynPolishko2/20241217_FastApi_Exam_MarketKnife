from fastapi.responses import RedirectResponse
from typing import List, Union
from app_knife.depends import model_params3, product_service
from app_knife.schemas.response_schema import ResponseSchema
from app_knife.schemas.product_schema_dto import ProductSchemaDtoPrice
from app_knife.routing.config import router

@router.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse(url='/docs')


@router.get('/all')
def get_products_all(service: product_service)\
        ->Union[List[ProductSchemaDtoPrice], ResponseSchema]:
    return service.s_get_products_all()


@router.get('/{model}')
def get_product_by_name(model: model_params3, service: product_service)\
        ->Union[ProductSchemaDtoPrice, ResponseSchema]:
    return service.s_get_product_by_model(model)
