from domain.entities.item import Item
from domain.repositories.item_repository import ItemRepository
from typing import List

class GetAllItems:
    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def execute(self) -> List[Item]:
        return self.repo.get_all()