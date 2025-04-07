from abc import ABC, abstractmethod
from typing import Protocol, List
from domain.entities.item import Item

class ItemRepository(Protocol):
    def find_by_name(self, name: str) -> Item | None:
        ...

    def save(self, item: Item) -> Item:
        ...

    def get_all(self) -> List[Item]:
        ...
