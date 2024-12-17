from models.product import Product
from sqlalchemy.orm import Session
from infrastructures.product_exception import *
from schemas.response_schema import ResponseSchema
from abstracts.abc_product_repository import AbcProductRepository

class ProductRepository(AbcProductRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        products = self.db.query(Product).all()
        if not products:
            return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property='products none')

        return products

    def get_by_model(self, model: str):
        _model = model.lower()
        product = self.db.query(Product).filter(Product.model == _model).first()
        if not product:
            return ResponseSchema(code=status.HTTP_404_NOT_FOUND, property=f'product {_model} none')

        return product
