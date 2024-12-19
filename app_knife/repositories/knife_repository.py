from abstracts.abc_product_repository import AbcProductRepository
from abstracts.abc_knife_repository import AbcKnifeRepository
from sqlalchemy.orm import Session
from repositories.product_repository import ProductRepository

class KnifeRepository(AbcKnifeRepository):

    def __init__(self, db: Session):
        self.db = db

    @property
    def product_repository(self) ->AbcProductRepository:
        return ProductRepository(self.db)