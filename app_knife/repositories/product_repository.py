from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app_knife.models.product import Product
from app_knife.infrastructures.product_exception import *
from app_knife.schemas.response_schema import ResponseSchema
from app_knife.schemas.product_schema import ProductSchemaIn, ProductSchemaModify
from app_knife.abstracts.abc_product_repository import AbcProductRepository

class ProductRepository(AbcProductRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_products_all(self):
        try:
            products = self.db.query(Product).all()
            if not products:
                return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property='products none')
            return products
        except Exception as exc:
            return ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'get all products failed due to {exc.__cause__}')

    def get_product_by_model(self, model: str):
        try:
            _model = model.lower()
            product = self.db.query(Product).filter(Product.model == _model).first()
            if not product:
                return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property=f'product {_model} none')
            return product
        except Exception as exc:
            return ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'get product by name failed due to {exc.__cause__}')

    def create_product_new(self, request: ProductSchemaIn):
        response: ResponseSchema
        try:
            product = Product(**request.model_dump(exclude_unset=True))
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            response = ResponseSchema(code=status.HTTP_201_CREATED, property=f'new product id{product.id}')
        except Exception as exc:
            response = ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'new product failed due to {exc.__cause__}')

        return response

    def modify_product(self, product: Product, request: ProductSchemaModify):
        response: ResponseSchema
        try:
            request_model = request.model_dump(exclude_unset=True)
            for key, value in request_model.items():
                setattr(product, key, value)

            self.db.commit()
            self.db.refresh(product)
            response = ResponseSchema(code=status.HTTP_202_ACCEPTED, property=f'update product id:{product.id} fields:{jsonable_encoder(request)}')
        except Exception as exc:
            response = ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'update product failed due to {exc.__cause__}')

        return response

    def delete_product(self, product: Product):
        response: ResponseSchema
        try:
            self.db.delete(product)
            self.db.commit()
            response = ResponseSchema(code=status.HTTP_204_NO_CONTENT, property=f'delete product id{product.id}')
        except Exception as exc:
            response = ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'delete product failed due to {exc.__cause__}')

        return response