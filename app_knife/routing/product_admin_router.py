from fastapi import APIRouter, status, Depends
from typing import Annotated
from schemas.product_schema import ProductSchemaIn, ProductSchemaModify
from schemas.response_schema import ResponseSchema
from app_knife.depends import product_repository, model_params
from depends import get_current_active_user
from schemas.user_schema import UserSchema

router = APIRouter(
    prefix='/product/admin',
    tags=['Http request: Product-Admin'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

@router.post('/new')
def create_product_new(request: ProductSchemaIn,
                       repository: product_repository,
                       authorization: Annotated[UserSchema, Depends(get_current_active_user)])->ResponseSchema:
    return repository.create_product_new(request)


@router.patch('/{model}')
def modify_product_by_model(model: model_params,
                            request: ProductSchemaModify,
                            repository: product_repository,
                            authorization: Annotated[UserSchema, Depends(get_current_active_user)])->ResponseSchema:
    response = repository.get_product_by_model(model)
    if isinstance(response, ResponseSchema):
        return response

    return repository.modify_product(response, request)

@router.delete('/{model}')
def delete_product_by_model(model: model_params,
                            repository: product_repository,
                            authorization: Annotated[UserSchema, Depends(get_current_active_user)])->ResponseSchema:
    response = repository.get_product_by_model(model)
    if isinstance(response, ResponseSchema):
        return response

    return repository.delete_product(response)
