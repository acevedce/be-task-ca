from domain.entities.customer import Customer
from domain.repositories.customer_repository import CustomerRepository

class CreateCustomer:
    def __init__(self, repo: CustomerRepository):
        self.repo = repo

    def execute(self, customer: Customer) -> Customer:
        if self.repo.find_by_email(customer.email):
            raise ValueError("Customer already exists")
        return self.repo.save(customer)
