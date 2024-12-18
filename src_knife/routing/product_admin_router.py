from fastapi import APIRouter, status, Depends
from schemas.product_schema import ProductSchemaOut, ProductSchemaIn
from schemas.response_schema import ResponseSchema
from depends import product_repository, model_params

router = APIRouter(
    prefix='/product/admin',
    tags=['Http request: Product-Admin'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

@router.post('/new')
def create_product_new(request: ProductSchemaIn, repository: product_repository)->ResponseSchema:
    return repository.create_product_new(request)

@router.delete('/{model}')
def create_product_new(model: model_params, repository: product_repository)->ResponseSchema:
    return repository.delete_product_by_model(model)