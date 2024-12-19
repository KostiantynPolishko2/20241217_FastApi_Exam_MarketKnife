from fastapi import Depends, Path
from typing import Annotated
from sqlalchemy.orm import Session

from app_knife.databases.database import SessionLocal
from app_knife.abstracts.abc_knife_repository import AbcKnifeRepository
from app_knife.abstracts.abc_product_repository import AbcProductRepository
from app_knife.repositories.knife_repository import KnifeRepository

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_knife_repository(db: Annotated[Session, Depends(get_db)])->AbcKnifeRepository:
    return KnifeRepository(db)

def get_product_repository(db: Annotated[Session, Depends(get_db)])->AbcProductRepository:
    return KnifeRepository(db).product_repository

knife_repository = Annotated[AbcKnifeRepository, Depends(get_knife_repository)]
product_repository = Annotated[AbcProductRepository, Depends(get_product_repository)]

model_params = Annotated[str, Path(description='knife model', min_length=2, max_length=12)]