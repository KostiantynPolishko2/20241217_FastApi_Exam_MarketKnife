from pydantic import BaseModel, Field, field_validator
from app_knife.schemas.enum_schema import EnumSellStatus

class ProductSchemaIn(BaseModel):
    model: str = Field(min_length=5, max_length=12)
    mark: str = Field(min_length=5, max_length=12)
    sell_status: EnumSellStatus = Field(default=None, description='the selling status of the product')
    price: float = Field(ge=300)
    is_available: bool = Field(default=True)
    img_path: str | None

    @field_validator('mark')
    def set_mark_lowercase(cls, value: str):
        if value:
            return value.lower()
        return value

    @field_validator('model')
    def set_model_lowercase(cls, value: str):
        if value:
            return value.lower()
        return value

    # Configure the model to allow validation from SQLAlchemy attributes
    model_config = {'from_attributes': True}

class ProductSchemaOut(ProductSchemaIn):
    id: int

class ProductSchemaModify(BaseModel):
    price: float = Field(ge=300)
    is_available: bool
    sell_status: EnumSellStatus = Field(default=None, description='the selling status of the product')