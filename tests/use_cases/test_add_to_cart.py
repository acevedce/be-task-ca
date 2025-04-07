from use_cases.cart.add_to_cart import AddToCart
from domain.entities.cart import Cart, CartItem

class InMemoryCartRepo:
    def __init__(self):
        self.storage = {}

    def get_cart(self, customer_id: int):
        return self.storage.get(customer_id, Cart(customer_id=customer_id, items=[]))

    def save_cart(self, cart: Cart):
        self.storage[cart.customer_id] = cart

def test_add_to_cart():
    repo = InMemoryCartRepo()
    use_case = AddToCart(repo)

    cart = use_case.execute(customer_id=1, item_id=101, quantity=2)
    assert len(cart.items) == 1
    assert cart.items[0].item_id == 101
    assert cart.items[0].quantity == 2

    # Add same item again
    cart = use_case.execute(customer_id=1, item_id=101, quantity=3)
    assert len(cart.items) == 1
    assert cart.items[0].quantity == 5

    # Add different item
    cart = use_case.execute(customer_id=1, item_id=102, quantity=1)
    assert len(cart.items) == 2
    assert cart.items[1].item_id == 102
    assert cart.items[1].quantity == 1