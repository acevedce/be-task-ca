from domain.entities.cart import Cart, CartItem
from domain.repositories.cart_repository import CartRepository

class AddToCart:
    def __init__(self, repo: CartRepository):
        self.repo = repo

    def execute(self, customer_id: int, item_id: int, quantity: int) -> Cart:
        cart = self.repo.get_cart(customer_id)
        for ci in cart.items:
            if ci.item_id == item_id:
                ci.quantity += quantity
                break
        else:
            cart.items.append(CartItem(item_id=item_id, quantity=quantity))
        self.repo.save_cart(cart)
        return cart
