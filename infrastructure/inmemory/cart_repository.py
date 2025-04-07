from domain.entities.cart import Cart, CartItem
from domain.repositories.cart_repository import CartRepository

class InMemoryCartRepository(CartRepository):
    def __init__(self):
        self.storage = {}

    def get_cart(self, customer_id: int):
        return self.storage.get(customer_id, Cart(customer_id=customer_id, items=[]))

    def save_cart(self, cart: Cart):
        self.storage[cart.customer_id] = cart
