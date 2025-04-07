from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from infrastructure.sqlalchemy.db import get_db
from infrastructure.sqlalchemy.cart_repository import SQLAlchemyCartRepository
from infrastructure.inmemory.cart_repository import InMemoryCartRepository
from use_cases.cart.add_to_cart import AddToCart
from domain.entities.cart import CartItem
from app import USE_IN_MEMORY

router = APIRouter()

in_memory_cart_repo = InMemoryCartRepository()

class AddToCartRequest(BaseModel):
    item_id: int
    quantity: int

class CartItemResponse(BaseModel):
    item_id: int
    quantity: int

class CartResponse(BaseModel):
    customer_id: int
    items: list[CartItemResponse]

@router.post("/customers/{customer_id}/cart", response_model=CartResponse)
def add_to_cart(customer_id: int, req: AddToCartRequest, db: Session = Depends(get_db)):
    repo = in_memory_cart_repo if USE_IN_MEMORY else SQLAlchemyCartRepository(db)
    use_case = AddToCart(repo)
    result = use_case.execute(customer_id=customer_id, item_id=req.item_id, quantity=req.quantity)
    return result

@router.get("/customers/{customer_id}/cart", response_model=CartResponse)
def get_cart(customer_id: int, db: Session = Depends(get_db)):
    repo = in_memory_cart_repo if USE_IN_MEMORY else SQLAlchemyCartRepository(db)
    return repo.get_cart(customer_id)