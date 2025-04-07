from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from infrastructure.sqlalchemy.db import get_db
from infrastructure.sqlalchemy.customer_repository import SQLAlchemyCustomerRepository
from infrastructure.inmemory.customer_repository import InMemoryCustomerRepository
from use_cases.customer.create_customer import CreateCustomer
from domain.entities.customer import Customer
from app import USE_IN_MEMORY

router = APIRouter()

in_memory_repo = InMemoryCustomerRepository()

class CreateCustomerRequest(BaseModel):
    first_name: str = Field(..., example="Jane")
    last_name: str = Field(..., example="Doe")
    email: str = Field(..., example="jane.doe@example.com")
    password: str = Field(..., example="supersecure123")
    shipping_address: str = Field(..., example="123 Main St, Springfield")

class CustomerResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    shipping_address: str

@router.post("/customers", response_model=CustomerResponse)
def create_customer(req: CreateCustomerRequest, db: Session = Depends(get_db)):
    repo = in_memory_repo if USE_IN_MEMORY else SQLAlchemyCustomerRepository(db)
    use_case = CreateCustomer(repo)
    try:
        new_customer = Customer(
            id=None,
            first_name=req.first_name,
            last_name=req.last_name,
            email=req.email,
            password_hash=req.password,
            shipping_address=req.shipping_address,
        )
        customer = use_case.execute(new_customer)
        return customer
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/customers", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    if USE_IN_MEMORY:
        return in_memory_repo.customers
    else:
        from infrastructure.sqlalchemy.models import CustomerModel
        customers = db.query(CustomerModel).all()
        return [Customer(
            id=c.id,
            first_name=c.first_name,
            last_name=c.last_name,
            email=c.email,
            password_hash=c.password_hash,
            shipping_address=c.shipping_address
        ) for c in customers]