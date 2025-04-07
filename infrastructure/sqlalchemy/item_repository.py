from sqlalchemy.orm import Session
from infrastructure.sqlalchemy.models import ItemModel
from domain.entities.item import Item
from domain.repositories.item_repository import ItemRepository
from typing import List

class SQLAlchemyItemRepository(ItemRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_name(self, name: str) -> Item | None:
        item = self.db.query(ItemModel).filter_by(name=name).first()
        return self._to_entity(item) if item else None

    def save(self, item: Item) -> Item:
        model = ItemModel(name=item.name, description=item.description,
                          price=item.price, quantity=item.quantity)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return self._to_entity(model)

    def get_all(self) -> List[Item]:
        items = self.db.query(ItemModel).all()
        return [self._to_entity(m) for m in items]

    def _to_entity(self, model: ItemModel) -> Item:
        return Item(id=model.id, name=model.name, description=model.description,
                    price=model.price, quantity=model.quantity)