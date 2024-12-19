from pydantic import BaseModel
from models.user import User
from schemas.user_schema import UserSchemaInDB

class MapHandler(BaseModel):

    @staticmethod
    def map_property_orm_schema_to_sql(request: User, orm_model_class: type[UserSchemaInDB]) -> UserSchemaInDB:
        return orm_model_class(**request.model_dump())