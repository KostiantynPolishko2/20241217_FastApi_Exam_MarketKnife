from enum import Enum

class EnumSellStatus(str, Enum):
    none = 'none'
    sale = 'sale'
    discount = 'discount'
    promotion = 'promotion'
    special_price = 'special_price'

class EnumSellSum(int, Enum):
    none = 0
    sale = 10
    discount = 15
    promotion = 25
    special_price = 30