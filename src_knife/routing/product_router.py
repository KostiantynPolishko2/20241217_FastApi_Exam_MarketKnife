from fastapi import APIRouter, status, Depends
from fastapi.responses import RedirectResponse
from typing import Annotated, List, Dict
from depends import get_db
from sqlalchemy.orm import Session
from schemas.product_schema import ProductSchemaOut, ProductSchemaIn
from schemas.response_schema import ResponseSchema
from models.product import Product

router = APIRouter(
    prefix='/product',
    tags=['Http request: Product'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

@router.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse(url='/docs')

@router.get('/all')
def get_products_all(db: Annotated[Session, Depends(get_db)])->List[ProductSchemaOut]:
    products = db.query(Product).all()
    if not products:
        return []
    return products

@router.post('/new', response_model=ResponseSchema)
def get_products_all(request: ProductSchemaIn, db: Annotated[Session, Depends(get_db)]):
    product = Product(
        mark=request.mark,
        model=request.model,
        price=request.price,
        is_available=request.is_available,
        sell_status=request.sell_status,
        img_path=request.img_path
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    return ResponseSchema(code=status.HTTP_201_CREATED, property=f'product id{product.id}')
