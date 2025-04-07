from typing import Protocol
from domain.entities.cart import Cart

class CartRepository(Protocol):
    def get_cart(self, customer_id: int) -> Cart:
        ...

    def save_cart(self, cart: Cart) -> None:
        ...
