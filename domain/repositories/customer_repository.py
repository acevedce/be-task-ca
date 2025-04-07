from typing import Protocol, Optional
from domain.entities.customer import Customer

class CustomerRepository(Protocol):
    def find_by_email(self, email: str) -> Optional[Customer]:
        ...

    def save(self, customer: Customer) -> Customer:
        ...