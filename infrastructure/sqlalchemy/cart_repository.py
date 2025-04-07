from domain.entities.cart import Cart, CartItem
from domain.repositories.cart_repository import CartRepository
from infrastructure.sqlalchemy.models import CartItemModel
from sqlalchemy.orm import Session

class SQLAlchemyCartRepository(CartRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_cart(self, customer_id: int) -> Cart:
        items = (
            self.db.query(CartItemModel)
            .filter(CartItemModel.customer_id == customer_id)
            .all()
        )
        return Cart(
            customer_id=customer_id,
            items=[CartItem(item_id=i.item_id, quantity=i.quantity) for i in items]
        )

    def save_cart(self, cart: Cart) -> None:
        self.db.query(CartItemModel).filter_by(customer_id=cart.customer_id).delete()
        for item in cart.items:
            new_item = CartItemModel(
                customer_id=cart.customer_id,
                item_id=item.item_id,
                quantity=item.quantity,
            )
            self.db.add(new_item)
        self.db.commit()