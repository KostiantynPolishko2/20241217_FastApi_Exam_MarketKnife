from enum import Enum

class EnumSellStatus(str, Enum):
    sale = 'sale'
    discount = 'discount'
    promotion = 'promotion'
    special_price = 'special_price'