from enum import Enum

class EnumSellStatus(str, Enum):
    none = None
    sale = 'sale'
    discount = 'discount'
    promotion = 'promotion'
    special_price = 'special_price'
    other = 'string'