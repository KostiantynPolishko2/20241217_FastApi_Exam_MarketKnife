from pydantic import field_validator
from schemas.product_schema import ProductSchemaIn
from schemas.enum_schema import EnumSellSum, EnumSellStatus

class ProductSchemaDtoPrice(ProductSchemaIn):
    sell_status: str

    @field_validator('price')
    @classmethod
    def set_price(cls, value: float, values: dict):
        if value:
            sell_status = values.data.get('sell_status')
            return cls.srt_get_price(value, sell_status)
        return value

    @staticmethod
    def srt_get_price(value: float, sell_status: str)->float:
        if sell_status not in EnumSellStatus:
            return value
        return value * (1 - EnumSellSum[sell_status].value/100)