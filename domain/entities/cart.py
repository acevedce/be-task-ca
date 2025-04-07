from dataclasses import dataclass
from typing import List

@dataclass
class CartItem:
    item_id: int
    quantity: int

@dataclass
class Cart:
    customer_id: int
    items: List[CartItem]