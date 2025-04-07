from use_cases.item.create_item import CreateItem
from domain.entities.item import Item
from typing import List

class InMemoryRepo:
    def __init__(self):
        self.items = []

    def find_by_name(self, name: str):
        return next((i for i in self.items if i.name == name), None)

    def save(self, item: Item):
        item.id = len(self.items) + 1
        self.items.append(item)
        return item

    def get_all(self) -> List[Item]:
        return self.items

def test_create_item():
    repo = InMemoryRepo()
    use_case = CreateItem(repo)

    item = use_case.execute("Apple", "Red fruit", 0.99, 10)
    assert item.id == 1
    assert item.name == "Apple"
    assert repo.find_by_name("Apple") is not None

    try:
        use_case.execute("Apple", "Duplicate", 1.0, 5)
        assert False, "Should raise error"
    except ValueError:
        pass