import bcrypt
from domain.entities.customer import Customer
from domain.repositories.customer_repository import CustomerRepository

class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self.customers = []
        self.counter = 1

    def find_by_email(self, email: str):
        return next((c for c in self.customers if c.email == email), None)

    def save(self, customer: Customer):
        customer.id = self.counter
        self.counter += 1
        # Encrypt password if not already encrypted (assumes raw input)
        if not customer.password_hash.startswith("$2b$"):
            hashed = bcrypt.hashpw(customer.password_hash.encode(), bcrypt.gensalt())
            customer.password_hash = hashed.decode()
        self.customers.append(customer)
        return customer