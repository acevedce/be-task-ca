from use_cases.customer.create_customer import CreateCustomer
from domain.entities.customer import Customer

class InMemoryCustomerRepo:
    def __init__(self):
        self.customers = []
        self.counter = 1

    def find_by_email(self, email: str):
        return next((c for c in self.customers if c.email == email), None)

    def save(self, customer: Customer):
        customer.id = self.counter
        self.counter += 1
        self.customers.append(customer)
        return customer

def test_create_customer():
    repo = InMemoryCustomerRepo()
    use_case = CreateCustomer(repo)

    customer = use_case.execute("Alice", "alice@example.com")
    assert customer.id == 1
    assert customer.name == "Alice"
    assert customer.email == "alice@example.com"

    try:
        use_case.execute("Alice", "alice@example.com")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass