from pydantic import BaseModel, field_validator

class ProductSchemaDtoPrice(BaseModel):
    price: float

    @field_validator('price')
    @classmethod
    def set_price(cls, value: float):
        if value:
            return cls.srt_get_price(value)
        return value

    @staticmethod
    def srt_get_price(value: float)->float:
        return value - 1