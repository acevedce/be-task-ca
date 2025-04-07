import bcrypt
from domain.entities.customer import Customer
from domain.repositories.customer_repository import CustomerRepository
from infrastructure.sqlalchemy.models import CustomerModel
from sqlalchemy.orm import Session

class SQLAlchemyCustomerRepository(CustomerRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_email(self, email: str):
        customer = self.db.query(CustomerModel).filter_by(email=email).first()
        if customer:
            return Customer(
                id=customer.id,
                first_name=customer.first_name,
                last_name=customer.last_name,
                email=customer.email,
                password_hash=customer.password_hash,
                shipping_address=customer.shipping_address
            )
        return None

    def save(self, customer: Customer):
        if not customer.password_hash.startswith("$2b$"):
            hashed = bcrypt.hashpw(customer.password_hash.encode(), bcrypt.gensalt())
            customer.password_hash = hashed.decode()
        model = CustomerModel(
            first_name=customer.first_name,
            last_name=customer.last_name,
            email=customer.email,
            password_hash=customer.password_hash,
            shipping_address=customer.shipping_address
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return Customer(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            password_hash=model.password_hash,
            shipping_address=model.shipping_address
        )
