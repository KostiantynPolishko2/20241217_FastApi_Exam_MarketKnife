from models.product import Product
from sqlalchemy.orm import Session
from infrastructures.product_exception import *
from schemas.response_schema import ResponseSchema
from abstracts.abc_product_repository import AbcProductRepository
from schemas.product_schema import ProductSchemaIn

class ProductRepository(AbcProductRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_products_all(self):
        products = self.db.query(Product).all()
        if not products:
            return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property='products none')

        return products

    def get_product_by_model(self, model: str):
        _model = model.lower()
        product = self.db.query(Product).filter(Product.model == _model).first()
        if not product:
            return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property=f'product {_model} none')

        return product

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

    def delete_product_by_model(self, model: str):
        product = self.get_product_by_model(model)
        if type(product) is ResponseSchema:
            return product

        response: ResponseSchema
        try:
            self.db.delete(product)
            self.db.commit()
            response = ResponseSchema(code=status.HTTP_204_NO_CONTENT, property=f'delete product id{product.id}')
        except Exception as exc:
            response = ResponseSchema(code=status.HTTP_503_SERVICE_UNAVAILABLE, property=f'delete product failed due to {exc.__cause__}')

        return response