from domain.entities.item import Item
from domain.repositories.item_repository import ItemRepository

class CreateItem:
    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def execute(self, name: str, description: str, price: float, quantity: int) -> Item:
        if self.repo.find_by_name(name):
            raise ValueError("Item already exists")
        item = Item(id=None, name=name, description=description, price=price, quantity=quantity)
        return self.repo.save(item)