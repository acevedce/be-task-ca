from domain.entities.item import Item
from domain.repositories.item_repository import ItemRepository

class InMemoryItemRepository(ItemRepository):
    def __init__(self):
        self.items = []
        self.counter = 1

    def find_by_name(self, name: str):
        return next((item for item in self.items if item.name == name), None)

    def save(self, item: Item):
        item.id = self.counter
        self.counter += 1
        self.items.append(item)
        return item

    def get_all(self):
        return self.items