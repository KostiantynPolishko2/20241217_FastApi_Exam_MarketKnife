from fastapi import APIRouter, status, Depends
from typing import Annotated, List
from depends import get_db
from sqlalchemy.orm import Session
from schemas.product_schema import ProductSchemaOut, ProductSchemaIn
from schemas.response_schema import ResponseSchema
from models.product import Product

router = APIRouter(
    prefix='/admin/product',
    tags=['Http request: Product'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

@router.post('/new', response_model=ResponseSchema)
def get_products_all(request: ProductSchemaIn, db: Annotated[Session, Depends(get_db)]):
    product = Product(**request.model_dump(exclude_unset=True))
    db.add(product)
    db.commit()
    db.refresh(product)

    return ResponseSchema(code=status.HTTP_201_CREATED, property=f'product id{product.id}')