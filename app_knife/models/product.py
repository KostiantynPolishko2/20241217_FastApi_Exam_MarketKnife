from sqlalchemy import (Column, Integer, Float, Boolean, String, UniqueConstraint, CheckConstraint)
from app_knife.databases.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    mark = Column(String, nullable=False)
    is_available = Column(Boolean, name='availability', default=True)
    price = Column(Float)
    sell_status = Column(String, nullable=True)
    img_path = Column(String, nullable=True)

    __table_args__ = (
        UniqueConstraint('model', name='uq_product_model'),
        CheckConstraint('price >= 300', name='ck_price_minimum')
    )