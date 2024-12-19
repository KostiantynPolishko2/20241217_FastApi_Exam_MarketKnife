from pydantic import BaseModel
from app_knife.models.product import Product
from app_knife.schemas.product_schema import ProductSchemaOut

class MapHandler(BaseModel):

    @staticmethod
    def props_schema_in_to_props_model(_property: ProductSchemaOut, orm_model_class: type[Product]) -> Product:
        return orm_model_class(**_property.model_dump())